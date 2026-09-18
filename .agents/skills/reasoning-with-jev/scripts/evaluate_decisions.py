#!/usr/bin/env python3
"""Offline evaluator for binary selective decisions (e.g. Jev Noul outputs).

Reads application-exported JSONL rows: {"id": str, "p": float, "y": 0|1,
"group": str (optional), "p_base": float (optional)}.
Reports Brier score (vs baseline when present), reliability bins with counts,
and coverage / FP / FN / expected-cost across thresholds.

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


def self_test():
    rows = [{"id": str(i), "p": y, "y": y} for i, y in enumerate([0, 0, 1, 1])]
    assert abs(brier(rows)) < 1e-9, "perfect predictions score 0"
    assert len(reliability(rows, 2)) == 2
    s = sweep(rows, [0.5], 1.0, 1.0)[0]
    assert s["coverage"] == 0.5 and s["fp"] == 0 and s["fn"] == 0, s
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


if __name__ == "__main__":
    sys.exit(main())
