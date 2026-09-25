#!/usr/bin/env python3
"""M5 scoring: grade every arm against withheld labels. Runs as `augctl`, the only holder of them.

The rule this file exists to fix in advance, before any score is seen: **what happens when an arm
emits a string that is not one of the task's labels.**

It is not hypothetical. The A2a run emitted 1,749 distinct strings over 6,000 T2a rows for a
77-label task, and 358 distinct strings over T2b's 12,845 for a 151-label one, including quoted
variants of the same answer. A generative artifact form answers in free text; a head over
embeddings cannot. Deciding how to treat that after seeing which arm it hurts would be choosing a
result.

So, fixed here:

  1. An output is matched to a label by exact string, then by a NORMALIZED comparison — casefold,
     strip quotes and surrounding punctuation, collapse whitespace, and treat underscores and
     spaces as the same character. Nothing cleverer. No fuzzy matching, no nearest neighbour, no
     prefix rule, because each of those is a small model that would help exactly one arm.
  2. An output that still matches no label is an **invalid output**, and it costs the task's
     wrong-answer cost — 1.0 for a misroute, and the false-positive or false-negative cost for
     T2c, whichever the true label implies. It is NOT treated as an abstention, because abstaining
     is a decision the arm could have made and did not.
  3. The invalid rate is reported per arm per task, always, whether it is zero or not.

Rule 2 is the conservative choice and it is deliberately unkind to the arms that need it. An
artifact form that cannot reliably emit one of the answers it was given is worse at the task, and
pricing that as a free pass would hide the difference the experiment exists to measure.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import unicodedata
from pathlib import Path
from statistics import NormalDist

ALPHA = 0.05
K_FAMILY = 6          # R1, R2a, R2b, A1, A2a, A2b
MARGIN = 0.01         # never widened
SPAN = 2.0            # costs in [0, 1], so paired differences have range 2
COMPARATOR = "R3a"
POWER = 0.8


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", str(text)).strip().casefold()
    text = text.strip("\"'`“”‘’ \t\n.,;:!?")
    text = re.sub(r"[_\s]+", " ", text)
    return text.strip()


def match(output: str, labels: list[str], lookup: dict) -> str | None:
    """Exact, then normalized. Returns the label, or None for an invalid output."""
    if output in lookup.values():
        return output
    return lookup.get(normalize(output))


def cost_of(action: str | None, truth: str, task: str, costs: dict) -> float:
    """The task's own cost matrix, with an invalid output priced as a wrong answer.

    T2a and T2b: misroute 1.0, abstain 0.3, correct 0.0.
    T2c: false positive 1.0 and false negative 4.0, normalized to [0, 1] by the larger of the two,
    so paired differences keep the range of 2 the design lock fixes.
    """
    if task == "T2c":
        c_fp, c_fn = costs["c_fp"], costs["c_fn"]
        scale = max(c_fp, c_fn)
        if action is None:
            # Invalid: charge whichever error the truth implies, which is the honest reading of
            # "it gave no usable answer" under an asymmetric matrix.
            return (c_fn if str(truth) in ("1", "toxic", "true") else c_fp) / scale
        if str(action) == str(truth):
            return 0.0
        return (c_fn if str(truth) in ("1", "toxic", "true") else c_fp) / scale

    if action is None:
        return costs["misroute"]
    if action in (costs.get("abstain_label"),):
        return costs["abstain"]
    return 0.0 if str(action) == str(truth) else costs["misroute"]


def eb_interval(differences, k: int, span: float) -> dict:
    n = len(differences)
    mean = sum(differences) / n
    sd = (sum((d - mean) ** 2 for d in differences) / (n - 1)) ** 0.5 if n > 1 else 0.0
    log_term = math.log(2 / (ALPHA / (2 * k)))
    radius = sd * math.sqrt(2 * log_term / n) + 7 * span * log_term / (3 * (n - 1))
    return {"n": n, "mean": mean, "sd": sd, "radius": radius,
            "upper": mean + radius, "lower": mean - radius}


def required_n(sd: float, margin: float, k: int, span: float, power: float = POWER) -> int | None:
    """One-sided non-inferiority at equality. Normal/fixed-SD planning, as the lock says."""
    if sd == 0:
        return None
    phi = NormalDist().cdf
    log_term = math.log(2 / (ALPHA / (2 * k)))

    def achieved(n: int) -> float:
        radius = sd * math.sqrt(2 * log_term / n) + 7 * span * log_term / (3 * (n - 1))
        if radius >= margin:
            return 0.0
        return phi((margin - radius) * math.sqrt(n) / sd)

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


def score_arm(actions: dict, truth: dict, labels: list[str], task: str, costs: dict) -> dict:
    lookup = {normalize(label): label for label in labels}
    per_row, invalid, abstained, correct = {}, 0, 0, 0
    for key, truth_label in truth.items():
        raw = actions.get(key)
        matched = None if raw is None else match(str(raw), labels, lookup)
        invalid += matched is None and raw is not None
        if matched == costs.get("abstain_label"):
            abstained += 1
        elif matched is not None and str(matched) == str(truth_label):
            correct += 1
        per_row[key] = cost_of(matched, truth_label, task, costs)
    n = len(per_row)
    return {"n": n, "mean_cost": sum(per_row.values()) / n,
            "invalid_outputs": invalid, "invalid_rate": invalid / n,
            "abstention_rate": abstained / n, "accuracy": correct / n,
            "per_row": per_row}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--actions", type=Path, action="append", required=True,
                        help="a checkpoint directory from m5_fit, or an actions file from m5_colab")
    parser.add_argument("--labels", type=Path, required=True,
                        help="directory of withheld confirmation labels; augctl only")
    parser.add_argument("--label-file", action="append", required=True, metavar="TASK=FILE")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args(argv)

    truth_by_task, labels_by_task = {}, {}
    for spec in args.label_file:
        task, _, filename = spec.partition("=")
        rows = json.loads((args.labels / filename).read_text(encoding="utf-8"))
        truth_by_task[task] = {row["id"]: row["label"] for row in rows}
        labels_by_task[task] = sorted({str(row["label"]) for row in rows})

    costs = {
        "T2a": {"misroute": 1.0, "abstain": 0.3, "abstain_label": "abstain"},
        "T2b": {"misroute": 1.0, "abstain": 0.3, "abstain_label": "out of scope"},
        "T2c": {"c_fp": 1.0, "c_fn": 4.0},
    }

    collected: dict[str, dict[str, dict]] = {}
    for path in args.actions:
        files = sorted(path.glob("*.json")) if path.is_dir() else [path]
        for file in files:
            payload = json.loads(file.read_text(encoding="utf-8"))
            if "actions" in payload and "arm" in payload:          # m5_fit checkpoint
                collected.setdefault(payload["task"], {})[payload["arm"]] = payload["actions"]
            elif "actions" in payload:                              # m5_colab report
                for key, actions in payload["actions"].items():
                    task, _, arm = key.partition("|")
                    collected.setdefault(task, {})[arm] = actions

    report = {"experiment": "M5", "family_size": K_FAMILY, "margin": MARGIN, "span": SPAN,
              "alpha": ALPHA, "comparator": COMPARATOR, "tasks": {}}
    for task, arms in sorted(collected.items()):
        truth = truth_by_task[task]
        labels = labels_by_task[task]
        if task in ("T2a", "T2b"):
            labels = labels + [costs[task]["abstain_label"]]
        scored = {arm: score_arm(actions, truth, labels, task, costs[task])
                  for arm, actions in sorted(arms.items())}
        block = {"labels": len(labels),
                 "arms": {arm: {k: v for k, v in value.items() if k != "per_row"}
                          for arm, value in scored.items()}}
        if COMPARATOR in scored:
            for arm, value in scored.items():
                if arm == COMPARATOR:
                    continue
                keys = sorted(set(value["per_row"]) & set(scored[COMPARATOR]["per_row"]))
                differences = [value["per_row"][k] - scored[COMPARATOR]["per_row"][k]
                               for k in keys]
                interval = eb_interval(differences, K_FAMILY, SPAN)
                needed = required_n(interval["sd"], MARGIN, K_FAMILY, SPAN)
                block["arms"][arm]["vs_comparator"] = {
                    **interval,
                    "non_inferior": interval["upper"] < MARGIN,
                    "superior_by_margin": interval["lower"] > MARGIN,
                    "required_n": needed,
                    "powered": needed is not None and needed <= interval["n"],
                }
        else:
            block["comparator_missing"] = (
                f"{COMPARATOR} has no actions for {task}; every outcome row is a contrast against "
                "it, so none of them is readable here")
        report["tasks"][task] = block

    report["limits"] = [
        "An output matching no label is invalid and costs the task's wrong-answer cost, fixed before any score was seen. It is not an abstention, because abstaining was a decision the arm could have made.",
        "Matching is exact then normalized — casefold, strip quotes and edge punctuation, collapse whitespace, treat underscore and space alike. No fuzzy or prefix matching, because each of those is a small model that would help exactly one arm.",
        "The invalid rate is reported for every arm on every task, zero or not.",
        "required_n is a normal/fixed-SD planning approximation; the empirical Bernstein interval is distribution-free and it decides.",
        "T2c's costs are normalized by the larger of the two, so paired differences keep the range of 2 the design lock fixes.",
    ]
    text = json.dumps(report, indent=2)
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    print(text)
    print(f"\nreport sha256: {hashlib.sha256(text.encode('utf-8')).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
