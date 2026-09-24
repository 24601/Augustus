#!/usr/bin/env python3
"""E4b: the eligibility fixtures, run against the shipped confirmation helper.

Plan v4 section 2.7 and the E4 design lock. Each fixture is a case where the
honest answer is NOT "supported", and the point is that the helper reaches that
answer by itself rather than by a human noticing. Fixture and simulation
evidence only.

This runs no model and reads no data. It builds receipts, calls
compare_workflows.compare, and compares the verdict with what the design lock
says the verdict must be. A fixture the helper cannot yet decide is reported as
a GAP, not quietly passed: the list of gaps is the work this experiment
produces.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

HELPER = (Path(__file__).resolve().parents[3]
          / ".agents/skills/augustus/scripts/compare_workflows.py")


def load_helper(path: Path):
    spec = importlib.util.spec_from_file_location("compare_workflows", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def receipt(pairs, **overrides):
    base = {
        "schema_version": 1, "phase": "confirm",
        "incumbent_id": "incumbent", "candidate_id": "candidate",
        "dataset_id": "e4b", "outcome_definition": "bounded loss",
        "sampling_unit": "one independent episode", "evidence_kind": "observed",
        "loss_bound": 1, "alpha": 0.05, "comparison_count": 1,
        "minimum_improvement": 0.0, "sampling_design": "equal_probability",
        "pairs": pairs,
    }
    base.update(overrides)
    return base


def pair(identity, incumbent_loss, candidate_loss):
    return {"id": str(identity),
            "incumbent": {"loss": incumbent_loss, "cost": None, "latency_ms": None,
                          "violations": []},
            "candidate": {"loss": candidate_loss, "cost": None, "latency_ms": None,
                          "violations": []}}


def fixtures():
    """Every case, with the verdict the design lock requires."""
    cases = []

    # 1. Teacher-labeled confirmation rows cannot support a margin.
    cases.append(("teacher_labeled_confirmation",
                  receipt([pair(i, 1.0, 0.0) for i in range(400)], evidence_kind="proxy"),
                  {"assessment": "proxy_evidence_only"}))

    # 2. Synthetic text is fixture evidence, however good the numbers look.
    cases.append(("synthetic_text",
                  receipt([pair(i, 1.0, 0.0) for i in range(400)], evidence_kind="fixture"),
                  {"assessment": "fixture_evidence_only"}))

    # 3. An unequal-probability sample cannot carry the bound.
    cases.append(("unequal_inclusion_probability",
                  receipt([pair(i, 1.0, 0.0) for i in range(400)],
                          sampling_design="probability_proportional_to_size"),
                  {"raises": "unsupported_sampling_design"}))

    # 4. The 50/950 case: a candidate that looks better on the units it kept.
    #    Apparent -0.667 on 60 retained units, true +0.9 over all 1,000.
    kept = [pair(f"k{i}", 1.0, 0.0) for i in range(50)] + [pair(f"r{i}", 0.0, 1.0) for i in range(10)]
    cases.append(("selective_50_950",
                  receipt(kept, excluded_units=940,
                          missing_outcome_policy="candidate abstained; units dropped"),
                  {"note": "excluded_units must be surfaced, not silently averaged away"}))

    # 5. The sign case: direction is significant while the mean loss RISES.
    sign_pairs = ([pair(f"w{i}", 1.0, 0.0) for i in range(24)]
                  + [pair(f"l{i}", 0.0, 1.0) for i in range(9)]
                  + [pair(f"b{i}", 0.5, 0.5) for i in range(267)])
    cases.append(("sign_direction_vs_magnitude",
                  receipt(sign_pairs, method="sign_exact", minimum_improvement=0.0),
                  {"raises": "sign_exact requires losses in"}))

    # 6. sign_exact refuses a magnitude claim.
    cases.append(("sign_exact_with_a_margin",
                  receipt([pair(i, 1.0, 0.0) for i in range(40)],
                          method="sign_exact", minimum_improvement=0.1),
                  {"raises": "certifies direction only"}))

    # 7. THE case v3 got wrong: a rare-large difference where every observed
    #    value is zero. A variance-only interval collapses to [0, 0] and
    #    certifies equivalence. EB must not.
    cases.append(("zero_discordance_rare_large",
                  receipt([pair(i, 0.25, 0.25) for i in range(12_850)],
                          method="empirical_bernstein", mode="non_inferiority",
                          minimum_improvement=0.00005, comparison_count=19),
                  {"assessment": "insufficient_evidence",
                   "not_supported": True,
                   "why": "the radius floor must keep this unpowered, never equivalent"}))

    # 8. A correlated equal-probability cluster sample. Every row has equal
    #    inclusion probability and the rows are not independent.
    cluster = ([pair(f"a{i}", 0.0, 0.0) for i in range(3_000)]
               + [pair(f"b{i}", 0.0, 1.0) for i in range(3_000)])
    cases.append(("correlated_equal_probability_clusters",
                  receipt(cluster, sampling_unit="cluster of 3,000 correlated rows",
                          method="empirical_bernstein"),
                  {"gap_if_supported": "the helper cannot see dependence it is not told about"}))

    return cases


def run(helper) -> dict:
    results = []
    for name, document, expectation in fixtures():
        outcome = {"fixture": name, "expectation": expectation}
        try:
            report = helper.compare(document)
        except ValueError as exc:
            outcome["raised"] = str(exc)
            wanted = expectation.get("raises")
            outcome["verdict"] = "pass" if wanted and wanted in str(exc) else (
                "gap" if wanted is None else "fail")
        else:
            outcome["assessment"] = report["assessment"]
            confirmation = report.get("confirmation")
            outcome["supported"] = bool(confirmation and confirmation["strict_margin_supported"])
            outcome["upper"] = confirmation["upper_mean_loss_delta"] if confirmation else None
            outcome["excluded_units"] = report.get("excluded_units")
            if expectation.get("raises"):
                outcome["verdict"] = "fail"
                outcome["detail"] = "expected a refusal, got a report"
            elif expectation.get("not_supported"):
                outcome["verdict"] = "pass" if not outcome["supported"] else "fail"
            elif expectation.get("assessment"):
                outcome["verdict"] = ("pass" if report["assessment"] == expectation["assessment"]
                                      else "fail")
            elif expectation.get("gap_if_supported"):
                # Not a failure of the helper: a limit of what a declared
                # design can express. Recorded so it cannot be forgotten.
                outcome["verdict"] = "gap" if outcome["supported"] else "pass"
            else:
                outcome["verdict"] = "review"
        results.append(outcome)

    return {
        "experiment": "E4b",
        "fixtures": len(results),
        "passed": sum(1 for r in results if r["verdict"] == "pass"),
        "failed": [r for r in results if r["verdict"] == "fail"],
        "gaps": [r for r in results if r["verdict"] == "gap"],
        "review": [r for r in results if r["verdict"] == "review"],
        "results": results,
        "limits": [
            "Fixture evidence only. No fixture here supports a margin on any real task.",
            "A gap is a limit of what a declared design can express, not a helper bug; it is recorded rather than passed.",
            "Passing establishes that the helper reaches the required verdict on these cases, not that it is correct in general.",
        ],
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--helper", type=Path, default=HELPER)
    parser.add_argument("--out")
    args = parser.parse_args(argv)
    report = run(load_helper(args.helper))
    text = json.dumps(report, indent=2)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    print(text)
    return 1 if report["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
