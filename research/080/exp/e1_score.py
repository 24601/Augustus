#!/usr/bin/env python3
"""Score E1 predictions against held-out labels and read every claim from one interval.

Runs as `augctl`, the only principal that holds confirmation labels. It takes
prediction files written by `augexp` (per arm, per ratio: a 0/1 action per
confirmation id) and the labels it already has, and produces the 19 contrasts
the E1 design lock enumerates.

It refuses to score unless the analysis-lock hash it is given matches the one
recorded with the split. That is the mechanism behind "the grader refuses to
score confirmation data unless the analysis-lock hash is present and matches":
without it, the two-lock scheme is a promise rather than a control.

Every claim type is read from ONE two-sided empirical Bernstein interval at
alpha/(2m) per tail. Superiority, non-inferiority and equivalence are different
readings of the same interval, not different tests, so no extra penalty applies
for asking more than one question of it.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from pathlib import Path
from statistics import NormalDist

ALPHA = 0.05
M_FAMILY = 19
RATIOS = {"4:1": (4, 1), "1:1": (1, 1), "1:4": (1, 4),
          "1:9": (1, 9), "1:19": (1, 19), "1:49": (1, 49),
          # The prior-shift rows are evaluated at the S cost, which the design lock sets to 1:9.
          "S": (1, 9)}


def tail_level(m: int, alpha: float = ALPHA) -> float:
    """Two-sided Bonferroni over m contrasts: alpha/(2m) per tail."""
    return alpha / (2 * m)


def eb_interval(differences, m: int, span: float) -> dict:
    """Two-sided empirical Bernstein interval for bounded paired differences.

    The second term depends only on the range, n and the level, so the radius
    cannot collapse to zero when every observed difference is identical. That
    is the property the whole method was chosen for.
    """
    n = len(differences)
    if n < 2:
        raise ValueError("an interval needs at least two paired differences")
    mean = sum(differences) / n
    variance = sum((d - mean) ** 2 for d in differences) / (n - 1)
    sd = math.sqrt(variance)
    delta = tail_level(m)
    log_term = math.log(2 / delta)
    radius = sd * math.sqrt(2 * log_term / n) + 7 * span * log_term / (3 * (n - 1))
    return {"n": n, "mean": mean, "sd": sd, "radius": radius,
            "lower": mean - radius, "upper": mean + radius,
            "tail_level": delta, "span": span}


def read_claims(interval: dict, margin: float) -> dict:
    """Every claim the one interval supports. Each is a reading, not a new test."""
    return {
        "superiority_ucb": interval["upper"] < -margin,
        "superiority_lcb": interval["lower"] > margin,
        "non_inferiority": interval["upper"] < margin,
        "equivalence": -margin < interval["lower"] and interval["upper"] < margin,
        "margin": margin,
    }


def cost_of(action: int, label: int, c_fp: float, c_fn: float) -> float:
    """Per-case cost. Normalized so C_FP + C_FN = 1."""
    if action and not label:
        return c_fp
    if label and not action:
        return c_fn
    return 0.0


def required_n_equivalence(sd: float, margin: float, m: int, span: float,
                           power: float = 0.8) -> int | None:
    """Smallest n giving `power` to certify equivalence at true Delta = 0.

    A normal/fixed-SD planning approximation: the interval is distribution-free,
    this is not, and the receipt says so wherever the number appears.
    """
    phi = NormalDist().cdf
    delta = tail_level(m)
    log_term = math.log(2 / delta)

    def achieved(n: int) -> float:
        radius = sd * math.sqrt(2 * log_term / n) + 7 * span * log_term / (3 * (n - 1))
        if radius >= margin:
            return 0.0
        return 2 * phi((margin - radius) * math.sqrt(n) / sd) - 1

    lo, hi = 2, 200_000_000
    if achieved(hi) < power:
        return None
    while lo < hi:
        mid = (lo + hi) // 2
        if achieved(mid) >= power:
            hi = mid
        else:
            lo = mid + 1
    return lo


def expand(predictions: dict) -> dict:
    """Accept the compact prediction format and return {arm: {id: 0|1}}.

    The post-lock run writes ids once and each arm as a string of '0'/'1' in that order, because
    the per-id form repeats 1.37M id strings across 23 arms. A plain {arm: {id: action}} file is
    still accepted, so nothing that already exists stops working.
    """
    if "arms" not in predictions or "ids" not in predictions:
        return predictions
    ids = predictions["ids"]
    expanded = {}
    for arm, bits in predictions["arms"].items():
        if len(bits) != len(ids):
            raise ValueError(f"{arm}: {len(bits)} actions for {len(ids)} ids")
        expanded[arm] = {i: int(bit) for i, bit in zip(ids, bits)}
    return expanded


def shift_population(labels: dict, ids, target_prior: float, seed: int = 80_102) -> list:
    """The shifted evaluation population: every negative, positives drawn with replacement.

    The same construction the fit used, from confirmation labels and a fixed seed. It draws from a
    different stream than the fit's torch generator, which changes WHICH positives are repeated and
    not the prior they are drawn to, and the realized prior is reported beside the interval.
    """
    positive = [i for i in ids if labels.get(i) == 1]
    negative = [i for i in ids if labels.get(i) == 0]
    if not positive:
        raise ValueError("the shifted population needs at least one positive")
    needed = int(round(target_prior * len(negative) / (1 - target_prior)))
    rng = random.Random(seed)
    return negative + [positive[rng.randrange(len(positive))] for _ in range(needed)]


def score(predictions: dict, labels: dict, contrasts, analysis_lock: str,
          expected_lock: str, shift_target_prior: float | None = None) -> dict:
    """Produce every contrast, or refuse."""
    if not expected_lock:
        raise ValueError("no analysis-lock hash was recorded with this split; refusing to score")
    if analysis_lock != expected_lock:
        raise ValueError(
            f"analysis-lock mismatch: supplied {analysis_lock[:16]}…, "
            f"recorded {expected_lock[:16]}…; refusing to score")

    predictions = expand(predictions)
    results = []
    for contrast in contrasts:
        name = contrast["name"]
        ratio = contrast["ratio"]
        fp, fn = RATIOS[ratio]
        c_fp, c_fn = fp / (fp + fn), fn / (fp + fn)
        span = 2 * max(c_fp, c_fn)
        left, right = contrast["arms"]
        ids = sorted(set(predictions[left]) & set(predictions[right]) & set(labels))
        if not ids:
            raise ValueError(f"{name}: the two arms share no scored ids")
        realized_prior = None
        if ratio == "S":
            if shift_target_prior is None:
                raise ValueError(f"{name}: a shift contrast needs the lock's target prior")
            ids = shift_population(labels, ids, shift_target_prior)
            realized_prior = sum(labels[i] for i in ids) / len(ids)
        differences = [cost_of(predictions[left][i], labels[i], c_fp, c_fn)
                       - cost_of(predictions[right][i], labels[i], c_fp, c_fn)
                       for i in ids]
        interval = eb_interval(differences, M_FAMILY, span)
        margin = contrast["margin"]
        claims = read_claims(interval, margin)
        needed = required_n_equivalence(interval["sd"], margin, M_FAMILY, span)
        # Power is prespecified in the analysis lock, from calibration sigma-hat and the
        # registered mode. Recomputing it here from confirmation data would let the scored data
        # decide which claims count, which is the thing the two-lock scheme exists to prevent.
        # The realized figure above is reported beside it as description, never as the gate.
        if "powered" not in contrast:
            raise ValueError(f"{name}: no prespecified `powered` from the analysis lock; "
                             "refusing to decide power from the data being scored")
        powered = bool(contrast["powered"])
        results.append({
            "contrast": name, "ratio": ratio, "arms": [left, right],
            "mode": contrast["mode"], "span": span,
            "interval": interval, "claims": claims,
            "required_n_for_equivalence_realized": needed,
            "powered": powered,
            "counts_toward_an_outcome_row": powered,
            "finite_population_delta": interval["mean"],
            "realized_prior": realized_prior,
        })

    return {
        "experiment": "E1",
        "family_size": M_FAMILY,
        "alpha": ALPHA,
        "tail_level": tail_level(M_FAMILY),
        "contrasts": results,
        "powered_contrasts": sum(1 for r in results if r["powered"]),
        "analysis_lock": analysis_lock,
        "limits": [
            "Every claim is read from one two-sided empirical Bernstein interval; the readings are not separate tests and carry no extra penalty.",
            "Coverage needs independent units of the declared sampling unit. Equal inclusion probability alone does not give that.",
            "required_n is a normal/fixed-SD planning approximation; the interval itself is distribution-free.",
            "An unpowered contrast counts toward no outcome row in either direction, and its interval is still reported.",
            "`powered` comes from the analysis lock, fixed before confirmation was read. The realized required_n beside it is description, not the gate.",
            "The exact finite-population delta is reported beside every interval, so an enumerated quantity is never described only as unpowered.",
        ],
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--predictions", type=Path, required=True,
                        help="JSON: {arm: {id: 0|1}}")
    parser.add_argument("--labels", type=Path, required=True,
                        help="JSON: [{id, label}] as written by the partitioner")
    parser.add_argument("--contrasts", type=Path, required=True,
                        help="JSON list of {name, ratio, arms, mode, margin, powered}, "
                             "taken from the analysis lock")
    parser.add_argument("--analysis-lock", required=True,
                        help="sha256 of the analysis lock this run claims to be under")
    parser.add_argument("--shift-target-prior", type=float,
                        help="the lock's target_prior; required if any contrast is at ratio S")
    parser.add_argument("--recorded-lock", required=True,
                        help="the hash recorded with the split; a mismatch refuses")
    parser.add_argument("--out")
    args = parser.parse_args(argv)

    predictions = json.loads(args.predictions.read_text(encoding="utf-8"))
    label_rows = json.loads(args.labels.read_text(encoding="utf-8"))
    labels = {row["id"]: row.get("label") for row in label_rows}
    contrasts = json.loads(args.contrasts.read_text(encoding="utf-8"))

    try:
        report = score(predictions, labels, contrasts, args.analysis_lock, args.recorded_lock,
                       args.shift_target_prior)
    except ValueError as exc:
        parser.exit(2, f"error: {exc}\n")

    report["predictions_sha256"] = hashlib.sha256(
        args.predictions.read_bytes()).hexdigest()
    text = json.dumps(report, indent=2)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
