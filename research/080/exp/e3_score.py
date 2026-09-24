#!/usr/bin/env python3
"""E3 confirmation: the three contrasts, P6's resplits, and the two controls. Refuses without the lock.

Runs as `augctl`, the only principal holding the confirmation answers. It refuses to open them
unless the analysis-lock hash it is given matches the one recorded with the split, and that check
runs BEFORE the answers are read, because a refusal that arrives after the outcome is in the
process is not a control.

Every arm is the one the sigma report froze on the search split. Nothing is selected here. The
three contrasts are read from one two-sided empirical Bernstein interval each, at α/(2m) per tail,
and because utilities are higher-is-better the registered read is on the LOWER bound: superiority
of the left arm means LCB > +margin.

P6 asks a different question, and it is the reason the confirmation truth is held here and never
exposed to selection. Over 200 resplits it compares two acceptance procedures on the same draws:

  adopt-best            take the arm with the best sample mean, whenever it beats the incumbent
  incumbent-challenger  keep the incumbent unless the paired interval clears zero

A false adoption is adopting an arm whose TRUE utility, over all 6,405 confirmation questions, is
below the incumbent's. The truth is computable here and nowhere else, which is the whole design.

Two controls, from the design lock. An identical frozen incumbent against its own copy must give
Δ ≡ 0 and must never be adopted. A planted +0.05 utility shift must be adopted at its planned
power. A machine that adopts nothing passes the first control and fails the second; a machine that
adopts everything does the reverse. Both are needed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from pathlib import Path

import e3_arms as arms

ALPHA = 0.05
RESPLITS = 200
RESPLIT_N = 500
PLANTED_SHIFT = 0.05
P6_SEED = 80_302


def tail_level(m: int) -> float:
    return ALPHA / (2 * m)


def eb_interval(differences, m: int, span: float) -> dict:
    n = len(differences)
    if n < 2:
        raise ValueError("an interval needs at least two paired differences")
    mean = sum(differences) / n
    sd = (sum((d - mean) ** 2 for d in differences) / (n - 1)) ** 0.5
    log_term = math.log(2 / tail_level(m))
    radius = sd * math.sqrt(2 * log_term / n) + 7 * span * log_term / (3 * (n - 1))
    return {"n": n, "mean": mean, "sd": sd, "radius": radius,
            "lower": mean - radius, "upper": mean + radius, "tail_level": tail_level(m)}


def read_claims(interval: dict, margin: float) -> dict:
    """Every claim this one interval supports. Readings, not separate tests."""
    return {
        "superiority_lcb": interval["lower"] > margin,
        "superiority_ucb": interval["upper"] < -margin,
        "equivalence": -margin < interval["lower"] and interval["upper"] < margin,
        "margin": margin,
    }


def build_arms(rows: dict, gold: dict, choices: dict) -> dict:
    """Every arm the frozen choices name, evaluated on the confirmation split."""
    explicit_signal = arms.SIGNALS[choices["best_explicit"]["signal"]]
    proxy_signal = arms.SIGNALS[choices["proxy_selected"]["signal"]]
    outcome_signal = arms.SIGNALS[choices["outcome_selected"]["signal"]]
    return {
        "explicit": arms.evaluate(rows, gold, lambda row: arms.run_threshold(
            row, explicit_signal, choices["best_explicit"]["threshold"])),
        "implicit": arms.evaluate(rows, gold, arms.run_implicit),
        "constant": arms.evaluate(rows, gold, lambda row: arms.run_constant(
            row, choices["best_constant"]["k"])),
        "proxy": arms.evaluate(rows, gold, lambda row: arms.run_threshold(
            row, proxy_signal, choices["proxy_selected"]["threshold"])),
        "outcome": arms.evaluate(rows, gold, lambda row: arms.run_threshold(
            row, outcome_signal, choices["outcome_selected"]["threshold"])),
    }


def contrast(left: dict, right: dict, m: int, span: float, margin: float) -> dict:
    keys = sorted(set(left["per_question"]) & set(right["per_question"]))
    differences = [left["per_question"][k] - right["per_question"][k] for k in keys]
    interval = eb_interval(differences, m, span)
    return {"interval": interval, "claims": read_claims(interval, margin),
            "finite_population_delta": interval["mean"]}


def adopt_best(sample, incumbent: str, per_arm: dict) -> str:
    """Take whichever arm looks best on this sample. No evidence bar at all."""
    means = {name: sum(per_arm[name][key] for key in sample) / len(sample) for name in per_arm}
    best = max(means, key=lambda name: (means[name], name))
    return best if means[best] > means[incumbent] else incumbent


def incumbent_challenger(sample, incumbent: str, per_arm: dict, m: int, span: float) -> str:
    """Keep the incumbent unless a challenger's paired interval clears zero.

    The incumbent is untouched: it is not re-estimated, re-tuned or re-selected, and a challenger
    has to beat it on the evidence rather than on the point estimate.
    """
    for name in sorted(per_arm):
        if name == incumbent:
            continue
        differences = [per_arm[name][key] - per_arm[incumbent][key] for key in sample]
        if eb_interval(differences, m, span)["lower"] > 0:
            return name
    return incumbent


def p6(per_arm: dict, truth: dict, incumbent: str, m: int, span: float) -> dict:
    """200 resplits, two procedures, judged against the truth only augctl can compute."""
    keys = sorted(per_arm[incumbent])
    rng = random.Random(P6_SEED)
    false_best = false_ic = 0
    differences = []
    for _ in range(RESPLITS):
        sample = rng.sample(keys, min(RESPLIT_N, len(keys)))
        chosen_best = adopt_best(sample, incumbent, per_arm)
        chosen_ic = incumbent_challenger(sample, incumbent, per_arm, m, span)
        wrong_best = int(truth[chosen_best] < truth[incumbent])
        wrong_ic = int(truth[chosen_ic] < truth[incumbent])
        false_best += wrong_best
        false_ic += wrong_ic
        differences.append(wrong_ic - wrong_best)
    mean = sum(differences) / RESPLITS
    sd = (sum((d - mean) ** 2 for d in differences) / (RESPLITS - 1)) ** 0.5
    half = 1.96 * sd / math.sqrt(RESPLITS)
    return {
        "resplits": RESPLITS, "sample_n": RESPLIT_N, "incumbent": incumbent,
        "false_adoption_adopt_best": false_best / RESPLITS,
        "false_adoption_incumbent_challenger": false_ic / RESPLITS,
        "difference": mean,
        "ci95": [mean - half, mean + half],
        "supports_p6": (mean < 0) and (mean + half < 0),
        "note": "A false adoption replaces the incumbent with an arm whose utility over all "
                "confirmation questions is lower. The interval is normal-approximate over "
                "resplits, which are not independent draws from a population; it describes the "
                "procedure's variability across resplits and nothing wider.",
    }


def control_sample_size(shift: float, sd: float, m: int, span: float, cap: int) -> int:
    """The smallest resplit at which a `shift` is detectable at all by this interval.

    The empirical Bernstein radius has a range term that does not shrink with the sd, only with n:
    at R = 2.4 and m = 3 it alone is 0.062 at n = 500, which exceeds the planted 0.05. A control
    run at that size would report that a genuine effect was never adopted, and the true reason
    would be that no effect of that size is detectable there, not that the procedure is timid.
    So the control runs at the size its own requirement implies, and the size is reported.
    """
    log_term = math.log(2 / tail_level(m))
    n = 2
    while n < cap:
        radius = sd * math.sqrt(2 * log_term / n) + 7 * span * log_term / (3 * (n - 1))
        if radius < shift:
            return n
        n += 1
    return cap


def controls(per_arm: dict, truth: dict, incumbent: str, m: int, span: float) -> dict:
    """The two the design lock names, and they must fail in opposite directions."""
    keys = sorted(per_arm[incumbent])
    rng = random.Random(P6_SEED + 1)

    # Control 1: an identical frozen incumbent against its own copy.
    copy_arms = {incumbent: per_arm[incumbent], "copy": dict(per_arm[incumbent])}
    identical_deltas = [per_arm[incumbent][key] - copy_arms["copy"][key] for key in keys]
    adopted_copy = 0
    for _ in range(RESPLITS):
        sample = rng.sample(keys, min(RESPLIT_N, len(keys)))
        adopted_copy += incumbent_challenger(sample, incumbent, copy_arms, m, span) != incumbent

    # Control 2: a planted +0.05 shift on a copy of the incumbent, which must be adopted. The
    # shift is exact, so the paired difference has sd 0 and only the range term stands between it
    # and detection; the control therefore runs at the size that term requires.
    planted = {key: value + PLANTED_SHIFT for key, value in per_arm[incumbent].items()}
    planted_arms = {incumbent: per_arm[incumbent], "planted": planted}
    control_n = max(RESPLIT_N, control_sample_size(PLANTED_SHIFT, 0.0, m, span, len(keys)))
    adopted_planted = 0
    rng = random.Random(P6_SEED + 2)
    for _ in range(RESPLITS):
        sample = rng.sample(keys, min(control_n, len(keys)))
        adopted_planted += incumbent_challenger(sample, incumbent, planted_arms, m,
                                                span) == "planted"
    return {
        "identical_copy": {
            "max_abs_delta": max(abs(d) for d in identical_deltas),
            "adoptions": adopted_copy,
            "passes": max(abs(d) for d in identical_deltas) == 0 and adopted_copy == 0,
            "requirement": "delta identically zero and never adopted",
        },
        "planted_shift": {
            "shift": PLANTED_SHIFT,
            "sample_n": control_n,
            "sample_n_note": "the smallest resplit at which this interval can detect a shift of "
                             "this size at all; the range term alone exceeds 0.05 at n = 500",
            "adoptions": adopted_planted,
            "adoption_rate": adopted_planted / RESPLITS,
            "passes": adopted_planted / RESPLITS >= 0.8,
            "requirement": "adopted at its planned power, which is 0.8",
        },
        "note": "A procedure that adopts nothing passes the first and fails the second; one that "
                "adopts everything does the reverse. Both are required.",
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--table", type=Path, required=True, help="the frozen confirmation table")
    parser.add_argument("--answers", type=Path, required=True, help="confirmation gold; augctl only")
    parser.add_argument("--sigma-report", type=Path, required=True)
    parser.add_argument("--lock", type=Path, required=True, help="the analysis lock JSON")
    parser.add_argument("--analysis-lock", required=True, help="sha256 of the lock markdown")
    parser.add_argument("--recorded-lock", required=True,
                        help="the hash recorded with the split; a mismatch refuses")
    parser.add_argument("--reader", default="Qwen3-1.7B")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args(argv)

    # Before the answers are opened. A refusal after the outcome is in the process is not a control.
    if not args.recorded_lock:
        parser.exit(2, "error: no analysis-lock hash was recorded with this split; "
                       "refusing to open the answers\n")
    if args.analysis_lock != args.recorded_lock:
        parser.exit(2, f"error: analysis-lock mismatch: supplied {args.analysis_lock[:16]}…, "
                       f"recorded {args.recorded_lock[:16]}…; refusing to open the answers\n")

    lock = json.loads(args.lock.read_text(encoding="utf-8"))
    sigma = json.loads(args.sigma_report.read_text(encoding="utf-8"))
    if args.reader not in sigma["readers"]:
        parser.exit(2, f"error: {args.reader} is not in the sigma report\n")
    if lock["narrowing"]["applied"] and args.reader == lock["narrowing"]["dropped_reader"]:
        parser.exit(2, f"error: {args.reader} was dropped by the prespecified narrowing; "
                       "scoring it would make the drop meaningless\n")

    m = lock["family_size"]
    span = lock["contrasts"][0]["span"]
    margin = lock["contrasts"][0]["margin"]
    choices = sigma["readers"][args.reader]["frozen_choices"]

    table = json.loads(args.table.read_text(encoding="utf-8"))["table"]
    gold = {row["id"]: row["answer"]
            for row in json.loads(args.answers.read_text(encoding="utf-8"))}
    missing = [key for key in table if key not in gold]
    if missing:
        parser.exit(2, f"error: {len(missing)} replayed questions have no retained answer\n")

    built = build_arms(table, gold, choices)
    per_arm = {name: summary["per_question"] for name, summary in built.items()}
    truth = {name: summary["mean_utility"] for name, summary in built.items()}

    pairs = (("best explicit - implicit", "explicit", "implicit"),
             ("best explicit - best constant", "explicit", "constant"),
             ("(vii) outcome - (vi) proxy", "outcome", "proxy"))
    locked = {row["contrast"]: row for row in lock["contrasts"]}
    results = []
    for name, left, right in pairs:
        row = contrast(built[left], built[right], m, span, margin)
        results.append({
            "contrast": name, "arms": [left, right], "mode": "superiority",
            "read_on": "lower bound; utilities are higher-is-better",
            "powered": locked[name]["powered"],
            "required_n": locked[name]["required_n"],
            "search_mean": locked[name]["search_mean"],
            "equivalence_reading": lock["equivalence_readings"],
            **row,
        })

    report = {
        "experiment": "E3",
        "reader": args.reader,
        "family_size": m,
        "alpha": ALPHA,
        "tail_level": tail_level(m),
        "analysis_lock": args.analysis_lock,
        "realized_rerun_joint_disagreement": lock["realized_rerun_joint_disagreement"],
        "arm_summaries": {name: {k: v for k, v in summary.items() if k != "per_question"}
                          for name, summary in built.items()},
        "contrasts": results,
        "p6": p6(per_arm, truth, "explicit", m, span),
        "controls": controls(per_arm, truth, "explicit", m, span),
        "table_sha256": hashlib.sha256(args.table.read_bytes()).hexdigest(),
        "limits": [
            "Every claim is read from one two-sided empirical Bernstein interval; the readings are not separate tests and carry no extra penalty.",
            "The equivalence readings were declared inconclusive in the analysis lock before confirmation was read. Intervals are still printed, because an unpowered contrast is reported with its interval and counts toward no outcome row; the lock governs what may be concluded, not what may be printed.",
            "Power comes from the analysis lock, fixed before confirmation was read.",
            "The determinism check failed at 100% joint per-question disagreement; the frozen table is the sole source and that rate travels with this result.",
            "P6's interval is over resplits of one finite population, not over independent draws from a superpopulation.",
        ],
    }
    text = json.dumps(report, indent=2)
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
