#!/usr/bin/env python3
"""E3: choose the arms on the search split and report sigma-hat per contrast. No confirmation read.

Runs as `augctl` on the frozen search replay tables and the retained search answers. It does the
three things that must happen before the analysis lock, and nothing else:

  1. freezes the best explicit arm — which signal and which threshold — by utility on search;
  2. freezes the best constant, and the proxy-selected and outcome-selected thresholds;
  3. measures sigma-hat of each family contrast on the same split.

The family is m = 6: per reader, best-explicit minus implicit, best-explicit minus best-constant,
and (vii) minus (vi). Every selection here happens on search, which the confirmation split never
touched, and the choices are written down so the confirmation run cannot revisit them.

Arms (vi) and (vii) differ in exactly one respect, and that difference is P5. Both sweep the same
grid over the same signal; (vii) picks the threshold with the best mean utility, which needs the
gold answer, and (vi) picks the threshold with the best self-consistency, which needs no label at
all. If proxy selection were as good as outcome selection, the two would land on the same place.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import e3_arms as arms

GRID = [round(0.05 * i, 2) for i in range(1, 20)]
SPAN = 2.4  # two utilities in an interval of width 1.2, from the design lock
M_FAMILY = 6
MARGIN = 0.02


def paired(left: dict, right: dict) -> dict:
    """sigma-hat of the paired difference, which is what the analysis lock records."""
    keys = sorted(set(left["per_question"]) & set(right["per_question"]))
    differences = [left["per_question"][key] - right["per_question"][key] for key in keys]
    n = len(differences)
    mean = sum(differences) / n
    variance = sum((d - mean) ** 2 for d in differences) / (n - 1) if n > 1 else 0.0
    return {"n": n, "mean": mean, "sd": variance ** 0.5}


def choose(rows: dict, gold: dict) -> dict:
    """Every frozen choice for one reader, with the sweep that produced it."""
    sweeps = {name: arms.sweep(rows, gold, name, GRID) for name in arms.SIGNALS}

    flat = [entry for entries in sweeps.values() for entry in entries]
    best_explicit = max(flat, key=lambda e: e["mean_utility"])
    # Arm (vi) may look at anything except the outcome, so it selects on self-consistency, and
    # ties break toward the lower threshold so the rule is deterministic rather than dict-ordered.
    proxy_pool = sweeps[best_explicit["signal"]]
    proxy = max(proxy_pool, key=lambda e: (e["self_consistency"], -e["threshold"]))
    outcome = max(proxy_pool, key=lambda e: (e["mean_utility"], -e["threshold"]))

    constants = {k: arms.evaluate(rows, gold, lambda row, kk=k: arms.run_constant(row, kk))
                 for k in arms.K_LEVELS}
    best_k = max(constants, key=lambda k: constants[k]["mean_utility"])
    return {
        "sweeps": {name: [{k: v for k, v in entry.items()} for entry in entries]
                   for name, entries in sweeps.items()},
        "best_explicit": {"signal": best_explicit["signal"],
                          "threshold": best_explicit["threshold"],
                          "search_mean_utility": best_explicit["mean_utility"]},
        "best_constant": {"k": best_k,
                          "search_mean_utility": constants[best_k]["mean_utility"]},
        "proxy_selected": {"signal": proxy["signal"], "threshold": proxy["threshold"],
                           "selected_on": "self_consistency, no label",
                           "search_self_consistency": proxy["self_consistency"],
                           "search_mean_utility": proxy["mean_utility"]},
        "outcome_selected": {"signal": outcome["signal"], "threshold": outcome["threshold"],
                             "selected_on": "mean_utility, which needs the gold answer",
                             "search_mean_utility": outcome["mean_utility"]},
    }


def contrasts_for(rows: dict, gold: dict, chosen: dict, reader: str) -> list[dict]:
    """The three contrasts this reader contributes to the family of six."""
    signal = arms.SIGNALS[chosen["best_explicit"]["signal"]]
    explicit = arms.evaluate(rows, gold, lambda row: arms.run_threshold(
        row, signal, chosen["best_explicit"]["threshold"]))
    implicit = arms.evaluate(rows, gold, arms.run_implicit)
    constant = arms.evaluate(rows, gold, lambda row: arms.run_constant(
        row, chosen["best_constant"]["k"]))
    proxy_signal = arms.SIGNALS[chosen["proxy_selected"]["signal"]]
    proxy = arms.evaluate(rows, gold, lambda row: arms.run_threshold(
        row, proxy_signal, chosen["proxy_selected"]["threshold"]))
    outcome = arms.evaluate(rows, gold, lambda row: arms.run_threshold(
        row, arms.SIGNALS[chosen["outcome_selected"]["signal"]],
        chosen["outcome_selected"]["threshold"]))

    # Direction, stated once because it is the opposite of E1's. E1 differenced COSTS, so the
    # candidate winning meant a negative difference read on the upper bound. E3 differences
    # UTILITIES, which are higher-is-better, so the expected winner is written on the left and a
    # POSITIVE difference favours it. The registered read is therefore the LOWER bound: superiority
    # of the left arm means LCB > +margin, and equivalence means the whole interval lies inside
    # ±margin. Writing this down is cheaper than rediscovering it while reading a result.
    rows_out = []
    for name, left, right in (("best explicit - implicit", explicit, implicit),
                              ("best explicit - best constant", explicit, constant),
                              ("(vii) outcome - (vi) proxy", outcome, proxy)):
        stats = paired(left, right)
        rows_out.append({"reader": reader, "contrast": name, "mode": "superiority",
                         "read_on": "lower bound; utilities are higher-is-better",
                         "margin": MARGIN, "span": SPAN, **stats})
    return rows_out, {"explicit": explicit, "implicit": implicit, "constant": constant,
                      "proxy": proxy, "outcome": outcome}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--table", action="append", required=True, metavar="READER=PATH",
                        help="one frozen search replay table per reader")
    parser.add_argument("--answers", type=Path, required=True,
                        help="the retained search answers; augctl only")
    parser.add_argument("--rerun-rate", type=float, required=True,
                        help="the realized determinism rate, which accompanies every E3 result")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)

    gold = {row["id"]: row["answer"]
            for row in json.loads(args.answers.read_text(encoding="utf-8"))}

    report = {"experiment": "E3", "family_size": M_FAMILY, "margin": MARGIN, "span": SPAN,
              "lambda": arms.LAMBDA, "grid": GRID,
              "realized_rerun_joint_disagreement": args.rerun_rate,
              "readers": {}, "contrasts": []}

    for spec in args.table:
        reader, _, path = spec.partition("=")
        table = json.loads(Path(path).read_text(encoding="utf-8"))
        rows = table["table"]
        missing = [key for key in rows if key not in gold]
        if missing:
            raise SystemExit(f"{reader}: {len(missing)} replayed questions have no retained answer")
        chosen = choose(rows, gold)
        contrasts, summaries = contrasts_for(rows, gold, chosen, reader)
        report["contrasts"].extend(contrasts)
        report["readers"][reader] = {
            "questions": len(rows),
            "table_sha256": hashlib.sha256(Path(path).read_bytes()).hexdigest(),
            "frozen_choices": {k: v for k, v in chosen.items() if k != "sweeps"},
            "sweeps": chosen["sweeps"],
            "arm_summaries": {name: {k: v for k, v in summary.items() if k != "per_question"}
                              for name, summary in summaries.items()},
        }

    if len(report["contrasts"]) != M_FAMILY:
        raise SystemExit(f"the family is {M_FAMILY} contrasts, not {len(report['contrasts'])}; "
                         "two readers with three contrasts each is what the lock registers")

    report["limits"] = [
        "Every choice here is made on the search split, which the confirmation split never touched.",
        "sigma-hat is measured on search; the realized sd on confirmation may differ, and the interval decides.",
        "Arms (ii)-(iv) threshold a probability whose rerun instability exceeds this margin; see the determinism receipt. That bounds transportability, not the internal comparison, because the tables are frozen.",
        "The proxy is self-consistency against the k=6 answer. It is label-free by construction, which is the property P5 needs, and it is not the only proxy a team might choose.",
        "Threshold arms never abstain; abstention is the implicit arm's own option, and giving the threshold arms a second parameter would change the registered comparison.",
    ]
    args.out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    slim = {k: v for k, v in report.items() if k not in ("readers", "grid")}
    slim["frozen_choices"] = {reader: value["frozen_choices"]
                              for reader, value in report["readers"].items()}
    slim["arm_summaries"] = {reader: value["arm_summaries"]
                             for reader, value in report["readers"].items()}
    print(json.dumps(slim, indent=2))
    print(f"\nreport sha256: {hashlib.sha256(args.out.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
