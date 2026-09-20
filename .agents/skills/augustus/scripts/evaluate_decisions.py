#!/usr/bin/env python3
"""Offline evaluator for binary selective decisions (e.g. Jev Noul outputs).

Reads application-exported JSONL rows: {"id": str, "p": float, "y": 0|1,
"group": str (optional), "p_base": float (optional)}.
Reports Brier score (vs baseline when present), reliability bins with counts,
and coverage / FP / FN / expected-cost across thresholds.

Also reports (when asked, and always in --self-test):
  * equal-width ECE vs quantile ECE (binning is a real decision, not a
    detail — equal-width can dump most mass into one bin)
  * cost-optimal single threshold (policy arithmetic, not a Harbor score)
  * hysteresis enter/exit (dual thresholds; the model never actuates)
  * ranking vs calibration: accuracy/AUC can stay flat while ECE blows up
  * hop-ECE permutation invariance (shuffle the stream; ECE does not move)

Select thresholds on one split, evaluate on another: run twice with different
files. Missing labels or costs produce a stated limitation, not defaults.
Usage: evaluate_decisions.py labels.jsonl [--cost-fp 1 --cost-fn 5] [--self-test]
"""

import argparse
import json
import sys


def load(path):
    rows = []
    with open(path) as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            assert isinstance(r.get("p"), (int, float)) and 0 <= r["p"] <= 1, \
                f"line {i}: p must be a probability in [0,1]"
            assert r.get("y") in (0, 1), f"line {i}: y must be 0 or 1"
            rows.append(r)
    assert rows, "no labeled rows found"
    return rows


def brier(rows, key="p"):
    return sum((r[key] - r["y"]) ** 2 for r in rows) / len(rows)


def reliability(rows, bins=10):
    out = []
    for b in range(bins):
        lo, hi = b / bins, (b + 1) / bins
        bucket = [r for r in rows if (r["p"] >= lo and (r["p"] < hi or b == bins - 1))]
        if bucket:
            out.append({"bin": f"[{lo:.1f},{hi:.1f})", "n": len(bucket),
                        "mean_p": sum(r["p"] for r in bucket) / len(bucket),
                        "rate": sum(r["y"] for r in bucket) / len(bucket)})
    return out


def ece_equal_width(rows, bins=10, key="p"):
    """Guo-style equal-width ECE on max-probability (here the binary p).

    Empty bins contribute 0. This is the measurement, not a ranking.
    """
    n = len(rows)
    total = 0.0
    for b in range(bins):
        lo, hi = b / bins, (b + 1) / bins
        bucket = [r for r in rows if (r[key] >= lo and (r[key] < hi or b == bins - 1))]
        if not bucket:
            continue
        mean_p = sum(r[key] for r in bucket) / len(bucket)
        rate = sum(r["y"] for r in bucket) / len(bucket)
        total += (len(bucket) / n) * abs(mean_p - rate)
    return total


def ece_quantile(rows, bins=10, key="p"):
    """Quantile (equal-count) ECE. Same rows can disagree with equal-width.

    Ties at a cut are assigned left-to-right after a stable sort on p.
    Last bin absorbs the remainder so n is conserved.
    """
    n = len(rows)
    if n == 0:
        return 0.0
    ordered = sorted(rows, key=lambda r: r[key])
    bins = min(bins, n)
    total = 0.0
    start = 0
    for b in range(bins):
        end = n if b == bins - 1 else round((b + 1) * n / bins)
        if end <= start:
            continue
        bucket = ordered[start:end]
        mean_p = sum(r[key] for r in bucket) / len(bucket)
        rate = sum(r["y"] for r in bucket) / len(bucket)
        total += (len(bucket) / n) * abs(mean_p - rate)
        start = end
    return total


def accuracy(rows, key="p", t=0.5):
    return sum(1 for r in rows if (r[key] >= t) == bool(r["y"])) / len(rows)


def pairwise_ranking_auc(rows, key="p"):
    """Mann–Whitney ranking of p vs label. Translation-invariant in p.

    A model can rank well (high AUC) and still be badly calibrated
    (high ECE). Ranking ≠ calibration.
    """
    pos = [r[key] for r in rows if r["y"] == 1]
    neg = [r[key] for r in rows if r["y"] == 0]
    if not pos or not neg:
        return None
    wins = 0.0
    for p in pos:
        for n in neg:
            if p > n:
                wins += 1
            elif p == n:
                wins += 0.5
    return wins / (len(pos) * len(neg))


def sweep(rows, thresholds, c_fp, c_fn):
    out = []
    for t in thresholds:
        acted = [r for r in rows if r["p"] >= t]
        fp = sum(1 for r in acted if r["y"] == 0)
        fn = sum(1 for r in rows if r["p"] < t and r["y"] == 1)
        out.append({"threshold": t, "coverage": len(acted) / len(rows),
                    "fp": fp, "fn": fn,
                    "cost": (c_fp * fp + c_fn * fn) / len(rows)})
    return out


def cost_optimal_threshold(rows, c_fp, c_fn, grid=None):
    """Pick t from a grid that minimises expected cost. Policy, not a proof."""
    if grid is None:
        grid = [i / 20 for i in range(1, 20)]
    scored = sweep(rows, grid, c_fp, c_fn)
    return min(scored, key=lambda s: s["cost"])


def hysteresis_actuate(p_series, enter, exit, start=False):
    """Dual-threshold latch. The model never actuates; policy holds state.

    enter > exit. Once on, stay on until p < exit; once off, stay off
    until p >= enter. Single-threshold 0.5 is measurement theater when
    the stream flaps around the bar.
    """
    if not (0 <= exit < enter <= 1):
        raise ValueError("need 0 <= exit < enter <= 1")
    on = start
    out = []
    for p in p_series:
        if on:
            if p < exit:
                on = False
        else:
            if p >= enter:
                on = True
        out.append(on)
    return out


def hop_ece_permutation_invariant(rows, bins=10, key="p"):
    """Shuffle order; equal-width ECE must not move.

    Hop-ECE is permutation-invariant. Clustered regime-shift errors are
    invisible to it. That is a measurement fact, not a license to skip
    trajectory audits (TCE / AMS live in the deferred-crispification
    paper — we only lock the invariance here).
    """
    a = ece_equal_width(rows, bins=bins, key=key)
    reversed_rows = list(reversed(rows))
    b = ece_equal_width(reversed_rows, bins=bins, key=key)
    return abs(a - b)


def self_test():
    rows = [{"id": str(i), "p": y, "y": y} for i, y in enumerate([0, 0, 1, 1])]
    assert abs(brier(rows)) < 1e-9, "perfect predictions score 0"
    assert len(reliability(rows, 2)) == 2
    s = sweep(rows, [0.5], 1.0, 1.0)[0]
    assert s["coverage"] == 0.5 and s["fp"] == 0 and s["fn"] == 0, s
    assert abs(ece_equal_width(rows, 2)) < 1e-9
    assert abs(ece_quantile(rows, 2)) < 1e-9
    assert accuracy(rows) == 1.0
    assert pairwise_ranking_auc(rows) == 1.0

    # Ranking ≠ calibration: same ranking, overconfident p.
    ranked = [
        {"id": "n1", "p": 0.95, "y": 0},
        {"id": "n2", "p": 0.90, "y": 0},
        {"id": "p1", "p": 0.99, "y": 1},
        {"id": "p2", "p": 0.96, "y": 1},
    ]
    auc = pairwise_ranking_auc(ranked)
    assert auc == 1.0, auc
    ece = ece_equal_width(ranked, bins=4)
    assert ece > 0.2, ece  # ranks perfectly; still miscalibrated

    # Equal-width vs quantile: mass piled in one band.
    piled = ([{"id": f"a{i}", "p": 0.82, "y": 0} for i in range(38)]
             + [{"id": f"b{i}", "p": 0.55, "y": 1} for i in range(17)]
             + [{"id": f"c{i}", "p": 0.35, "y": 0} for i in range(18)])
    ew = ece_equal_width(piled, bins=10)
    qe = ece_quantile(piled, bins=3)
    assert ew != qe, (ew, qe)  # binning choice is a real decision

    # Hysteresis: flap around 0.7 does not chatter.
    series = [0.5, 0.85, 0.72, 0.65, 0.55, 0.45]
    held = hysteresis_actuate(series, enter=0.8, exit=0.6)
    assert held == [False, True, True, True, False, False], held
    single = [p >= 0.7 for p in series]
    assert single != held, "single threshold flaps; hysteresis holds"

    # Hop-ECE permutation invariance.
    delta = hop_ece_permutation_invariant(piled, bins=10)
    assert delta < 1e-12, delta

    # Cost-optimal threshold moves with the loss table.
    cheap_fp = cost_optimal_threshold(ranked, c_fp=1, c_fn=10)
    expensive_fp = cost_optimal_threshold(ranked, c_fp=10, c_fn=1)
    assert cheap_fp["threshold"] <= expensive_fp["threshold"]

    print("self-test ok")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("labels", nargs="?")
    ap.add_argument("--cost-fp", type=float, default=1.0)
    ap.add_argument("--cost-fn", type=float, default=1.0)
    ap.add_argument("--bins", type=int, default=10)
    ap.add_argument("--thresholds", default="0.3,0.5,0.7,0.9")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        self_test()
        return
    if not a.labels:
        ap.error("labels.jsonl required (or --self-test)")
    rows = load(a.labels)
    print(f"n={len(rows)} brier={brier(rows):.4f}")
    print(f"ece_equal_width={ece_equal_width(rows, a.bins):.4f} "
          f"ece_quantile={ece_quantile(rows, a.bins):.4f} "
          f"(binning is a decision; ranking≠calibration)")
    auc = pairwise_ranking_auc(rows)
    if auc is None:
        print("auc: undefined (one class missing)")
    else:
        print(f"auc={auc:.4f} accuracy@0.5={accuracy(rows):.4f}")
    if any("p_base" in r for r in rows):
        base = [r for r in rows if isinstance(r.get("p_base"), (int, float))]
        print(f"baseline brier={brier(base, 'p_base'):.4f} (n={len(base)})")
    else:
        print("baseline: none supplied (limitation: no comparative claim)")
    for b in reliability(rows, a.bins):
        print(f"bin {b['bin']:>12} n={b['n']:>4} mean_p={b['mean_p']:.3f} rate={b['rate']:.3f}")
    for s in sweep(rows, [float(t) for t in a.thresholds.split(",")],
                     a.cost_fp, a.cost_fn):
        print(f"t={s['threshold']:.2f} coverage={s['coverage']:.3f} "
              f"fp={s['fp']} fn={s['fn']} cost={s['cost']:.4f}")
    best = cost_optimal_threshold(rows, a.cost_fp, a.cost_fn)
    print(f"cost_optimal t={best['threshold']:.2f} cost={best['cost']:.4f} "
          f"(policy arithmetic; not a Harbor score)")


if __name__ == "__main__":
    sys.exit(main())
