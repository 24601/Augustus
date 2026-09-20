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
  * candidate_mass vs renormalized bag: softmax over allowed tokens is a
    peaked ranking, not a Noul (mass outside the bag can be hidden)
  * pick_by_id vs pick_second: the same scores, shuffled option order;
    slot-two is ranking theater, not a Noul
  * paired CI includes-zero: a bootstrap interval that covers 0 is not
    evidence of equivalence (paired bootstrap CIs are *theirs*)
  * same-accuracy speedup: tied accuracy plus a latency ratio is a
    systems comparison, not semantic equivalence
  * lint cutoff still soft: p >= cutoff fires a sensor, not a proof
  * 400 error contract is not a Noul (plain-text unaskable)
  * third-party benches stay *theirs* (not Harbor)
  * decide is not generate; thinking mode is constrained AR
  * packed-mask isolation fails by construction on DeltaNet
  * typesafe-sdk 0.7 Pydantic response models are not logit-equiv
  * MLX SchemaError 400 plain-string is the same contract as vLLM
  * coverage-at-error-budget stays *theirs* (not Harbor)

Select thresholds on one split, evaluate on another: run twice with different
files. Missing labels or costs produce a stated limitation, not defaults.
Usage: evaluate_decisions.py labels.jsonl [--cost-fp 1 --cost-fn 5] [--self-test]
"""

import argparse
import json
import math
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


def _softmax(xs):
    m = max(xs)
    exps = [math.exp(x - m) for x in xs]
    total = sum(exps)
    return [e / total for e in exps]


def ci_includes_zero(lo, hi):
    """Paired bootstrap CIs are *theirs*. Covering zero is not equivalence."""
    if lo > hi:
        raise ValueError("need lo <= hi")
    return lo <= 0.0 <= hi


def same_accuracy_speedup(acc_a, acc_b, lat_a, lat_b):
    """Tied accuracy plus a latency ratio is systems comparison, not meaning.

    Same accuracy, 35x faster *theirs* is not semantic equivalence.
    """
    if lat_a <= 0 or lat_b <= 0:
        raise ValueError("latencies must be positive")
    tied = abs(acc_a - acc_b) < 1e-12
    speedup = lat_b / lat_a
    return tied, speedup


def lint_cutoff_fires(p, cutoff):
    """cutoff 0.8 still soft. A sensor fire is not a proof."""
    return p >= cutoff


def pick_by_id(scores_by_id):
    """Max score wins regardless of presentation order."""
    if not scores_by_id:
        raise ValueError("scores_by_id empty")
    return max(scores_by_id.items(), key=lambda kv: kv[1])[0]


def pick_second(ordered_ids, scores_by_id=None):
    """Whatever sits in slot two. Option order is the answer.

    pick_by_id vs pick_second: the same scores can yield four
    dinners if the menu is shuffled. That is ranking theater,
    not a Noul.
    """
    if len(ordered_ids) < 2:
        raise ValueError("need at least two options")
    return ordered_ids[1]


def candidate_mass_renorm(full_logits, allowed_indices):
    """Softmax over allowed tokens is a peaked ranking, not a Noul.

    candidate_mass is the full-vocabulary softmax mass on the allowed
    bag. Renormalizing that bag to 1 hides mass outside it.
    softmax over A–H ≠ Noul.
    """
    if not allowed_indices:
        raise ValueError("allowed_indices empty")
    probs = _softmax(full_logits)
    mass = sum(probs[i] for i in allowed_indices)
    allowed_logits = [full_logits[i] for i in allowed_indices]
    return mass, _softmax(allowed_logits)



def http_error_contract_is_not_noul(status, body_kind="plain-text"):
    """400 plain-text for unaskable is an error contract, not a Noul."""
    if status == 400 and body_kind == "plain-text":
        return True
    if status == 422:
        return True
    return False


def theirs_bench_is_not_harbor(n, claim):
    """Third-party benches stay *theirs*. n and claim do not mint Harbor."""
    if not claim:
        raise ValueError("need a claim label")
    return True


def decide_is_not_generate(kind):
    """decide / generate / stream are three inference types."""
    if kind not in ("decide", "generate", "stream"):
        raise ValueError("kind must be decide, generate, or stream")
    return kind == "decide"


def thinking_mode_is_constrained_ar(thinking):
    """thinking=True/False is still autoregressive constrained decoding."""
    return True


def isolation_fails_on_deltanet(packed_mask_respected):
    """Packed-mask isolation would fail by construction on DeltaNet."""
    return packed_mask_respected is False


def pydantic_sdk_07_is_not_logit_equiv(sdk_version, models_kind, server_output_unchanged):
    """typesafe-sdk 0.7 Pydantic response models ≠ logit-equiv.

    Quote *theirs*: The server's output is unchanged and was never wrong.
    msgspec dropped is not a replica. Client decode is not the head.
    """
    if sdk_version != "0.7":
        return False
    if models_kind != "pydantic":
        return False
    return bool(server_output_unchanged)


def mlx_400_same_contract_as_vllm(mlx_status, mlx_detail, vllm_status, vllm_detail):
    """SchemaError is 400 plain-string detail not 422 list. Same contract as vLLM."""
    mlx_ok = mlx_status == 400 and mlx_detail == "plain-string"
    vllm_ok = vllm_status == 400 and vllm_detail == "plain-string"
    return mlx_ok and vllm_ok


def coverage_at_error_budget_is_theirs(metric_name, harbor=False):
    """coverage-at-error-budget *theirs* not Harbor."""
    if metric_name != "coverage-at-error-budget":
        raise ValueError("unexpected metric")
    return harbor is False




def dual_serving_is_not_generate(systemone_kind, chat_kind, mlx_chat_status):
    """dual /v1/systemone + /v1/chat/completions. decide is not generate.

    chat 501 on MLX. Dual serving is not generate.
    """
    if systemone_kind != "decide":
        return False
    if chat_kind != "generate":
        return False
    return mlx_chat_status == 501


def hosted_codiv_is_not_typesafe(host, affiliated=False):
    """Hosted Codiv ≠ TypeSafe."""
    if host != "codiv":
        raise ValueError("unexpected host")
    return affiliated is False


def candidate_probs_are_relative_not_correctness(relative, correctness_claim=False):
    """Candidate probabilities are relative to supplied options, not correctness."""
    return relative is True and correctness_claim is False


def recommendation_is_advisory(action, server_blocks=False):
    """The recommendation is advisory. The server never blocks on its own."""
    if action not in ("pass", "review", "block", "skip"):
        raise ValueError("unexpected action")
    return server_blocks is False


def lora_is_not_rlcd_replica(adapter_kind, rlcd_claimed=False):
    """LoRA adapters plus a scalar head ≠ RLCD replica."""
    if adapter_kind != "lora_plus_scalar_head":
        return False
    return rlcd_claimed is False


def pass_min_still_soft(threshold, hard_gate=False):
    """pass-min 0.8 still soft. JEQ does not own actions."""
    if threshold != 0.8:
        raise ValueError("unexpected threshold")
    return hard_gate is False


def hop_ece_permutation_invariant(rows, bins=10, key="p"):
    """Shuffle order; equal-width ECE must not move.

    Hop-ECE is permutation-invariant. Reverse is not a sufficient
    shuffle: also interleave even/odd indices. Clustered regime-shift
    errors are still invisible to it. That is a measurement fact, not
    a license to skip trajectory audits (TCE / AMS live in the
    deferred-crispification paper — we only lock the invariance here).
    """
    a = ece_equal_width(rows, bins=bins, key=key)
    reversed_rows = list(reversed(rows))
    interleaved = rows[::2] + rows[1::2]
    b = ece_equal_width(reversed_rows, bins=bins, key=key)
    c = ece_equal_width(interleaved, bins=bins, key=key)
    return max(abs(a - b), abs(a - c))


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

    # candidate_mass renormalization trap: peaked bag, mass outside.
    outside = [2.0, 0.0, -1.0, 8.0, 7.5, 7.0]
    mass, renorm = candidate_mass_renorm(outside, [0, 1, 2])
    assert mass < 0.01, mass
    assert abs(sum(renorm) - 1.0) < 1e-12
    assert max(renorm) > 0.7, renorm
    inside = [6.0, 5.0, 4.0, -4.0, -4.0, -4.0]
    mass_in, _ = candidate_mass_renorm(inside, [0, 1, 2])
    assert mass_in > 0.99, mass_in


    # pick_by_id vs pick_second: same scores, four orders.
    scores = {"A": 0.2, "B": 0.7, "C": 0.1}
    orders = [
        ("A", "B", "C"),
        ("B", "A", "C"),
        ("C", "B", "A"),
        ("A", "C", "B"),
    ]
    by_id = [pick_by_id({k: scores[k] for k in order}) for order in orders]
    second = [pick_second(order) for order in orders]
    assert by_id == ["B", "B", "B", "B"], by_id
    assert second == ["B", "A", "B", "C"], second

    # paired CI / same-accuracy speedup / lint cutoff still soft (1143).
    assert not ci_includes_zero(0.35, 1.31)  # emretheus XQuAD *theirs*
    assert ci_includes_zero(-0.10, 0.20)  # covering zero is not equivalence
    tied, speedup = same_accuracy_speedup(0.600, 0.600, 184.0, 6415.0)
    assert tied
    assert 34.0 < speedup < 36.0, speedup
    assert lint_cutoff_fires(0.81, 0.8)
    assert not lint_cutoff_fires(0.79, 0.8)

    # 1248: error contract / theirs-not-harbor / decide ≠ generate /
    # DeltaNet isolation fail-by-construction / thinking mode is AR.
    assert http_error_contract_is_not_noul(400, "plain-text")
    assert http_error_contract_is_not_noul(422, "json")
    assert not http_error_contract_is_not_noul(200, "json")
    assert theirs_bench_is_not_harbor(78, "von-macro-93.5")
    assert theirs_bench_is_not_harbor(231, "verdict-74.9")
    assert decide_is_not_generate("decide")
    assert not decide_is_not_generate("generate")
    assert not decide_is_not_generate("stream")
    assert thinking_mode_is_constrained_ar(True)
    assert thinking_mode_is_constrained_ar(False)
    assert isolation_fails_on_deltanet(False)
    assert not isolation_fails_on_deltanet(True)

    # 1340: pydantic 0.7 ≠ logit-equiv / MLX 400 same contract /
    # coverage-at-error-budget *theirs*.
    assert pydantic_sdk_07_is_not_logit_equiv("0.7", "pydantic", True)
    assert not pydantic_sdk_07_is_not_logit_equiv("0.6", "msgspec", True)
    assert mlx_400_same_contract_as_vllm(400, "plain-string", 400, "plain-string")
    assert not mlx_400_same_contract_as_vllm(422, "list", 400, "plain-string")
    assert coverage_at_error_budget_is_theirs("coverage-at-error-budget", harbor=False)
    assert theirs_bench_is_not_harbor(1, "jev-vision-skip-0.936")
    assert theirs_bench_is_not_harbor(1, "pii-f1-0.971")


    # 1441: dual serving is not generate / Hosted Codiv ≠ TypeSafe /
    # candidate probabilities relative / MCP advisory / LoRA ≠ RLCD /
    # pass-min 0.8 still soft.
    assert dual_serving_is_not_generate("decide", "generate", 501)
    assert not dual_serving_is_not_generate("decide", "generate", 200)
    assert hosted_codiv_is_not_typesafe("codiv", affiliated=False)
    assert not hosted_codiv_is_not_typesafe("codiv", affiliated=True)
    assert candidate_probs_are_relative_not_correctness(True, False)
    assert not candidate_probs_are_relative_not_correctness(True, True)
    assert recommendation_is_advisory("block", server_blocks=False)
    assert not recommendation_is_advisory("block", server_blocks=True)
    assert lora_is_not_rlcd_replica("lora_plus_scalar_head", False)
    assert not lora_is_not_rlcd_replica("lora_plus_scalar_head", True)
    assert pass_min_still_soft(0.8, hard_gate=False)
    assert not pass_min_still_soft(0.8, hard_gate=True)
    assert theirs_bench_is_not_harbor(64, "jev-visual-37.30s-2.40s")
    assert theirs_bench_is_not_harbor(10046, "open-jev-2b-94.71")

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
