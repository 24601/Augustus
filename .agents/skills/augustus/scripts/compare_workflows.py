#!/usr/bin/env python3
"""Compare paired, bounded outcome losses; never execute or promote a policy.

Input is one JSON receipt with schema_version=1, phase (search/confirm),
incumbent_id, candidate_id, dataset_id, outcome_definition, sampling_unit,
evidence_kind (observed/adjudicated/proxy/fixture), loss_bound, and pairs.
Each pair has a unique id and incumbent/candidate objects with loss in
[0, loss_bound], cost (nonnegative or null), latency_ms (nonnegative or null),
and violations (a list of nonempty strings). Confirmation also needs alpha,
minimum_improvement, and a positive integer comparison_count fixed in advance.

Confirmation uses a one-sided Hoeffding bound on paired loss differences.
Its assumptions are independent representative units, a fixed sample size,
frozen policies and loss, and no adaptive reuse of confirmation outcomes.
The program checks arithmetic/schema, NOT those empirical assumptions or
whether an observed outcome is causal evidence. Missing costs stay unknown.
Search is descriptive only. See references/optimizer-integration.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys


def _object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _number(value, name, *, minimum=0.0, maximum=None):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a finite number")
    try:
        value = float(value)
    except (ValueError, OverflowError) as exc:
        raise ValueError(f"{name} must be a finite number") from exc
    if not math.isfinite(value) or value < minimum:
        raise ValueError(f"{name} must be finite and >= {minimum}")
    if maximum is not None and value > maximum:
        raise ValueError(f"{name} must be <= {maximum}")
    return value


def _text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be nonempty text")
    return value


def _mean(values):
    # Divide first: a finite mean must not overflow from summing raw values.
    return math.fsum(value / len(values) for value in values)


def compare(receipt):
    if not isinstance(receipt, dict):
        raise ValueError("receipt must be an object")
    if type(receipt.get("schema_version")) is not int or receipt["schema_version"] != 1:
        raise ValueError("schema_version must be integer 1")
    phase = receipt.get("phase")
    if phase not in ("search", "confirm"):
        raise ValueError("phase must be search or confirm")
    metadata = {name: _text(receipt.get(name), name) for name in (
        "incumbent_id", "candidate_id", "dataset_id", "outcome_definition", "sampling_unit"
    )}
    if metadata["incumbent_id"] == metadata["candidate_id"]:
        raise ValueError("incumbent_id and candidate_id must differ")
    kind = receipt.get("evidence_kind")
    if kind not in ("observed", "adjudicated", "proxy", "fixture"):
        raise ValueError("evidence_kind must be observed, adjudicated, proxy, or fixture")
    bound = _number(receipt.get("loss_bound"), "loss_bound")
    if bound == 0:
        raise ValueError("loss_bound must be positive and fixed before evaluation")
    pairs = receipt.get("pairs")
    if not isinstance(pairs, list) or not pairs:
        raise ValueError("pairs must be a nonempty list")
    seen = set()
    arms = {"incumbent": [], "candidate": []}
    for index, pair in enumerate(pairs):
        if not isinstance(pair, dict):
            raise ValueError(f"pair {index} must be an object")
        identity = _text(pair.get("id"), f"pair {index} id")
        if identity in seen:
            raise ValueError(f"duplicate pair id: {identity}")
        seen.add(identity)
        for name in arms:
            arm = pair.get(name)
            if not isinstance(arm, dict):
                raise ValueError(f"pair {identity} {name} must be an object")
            prefix = f"pair {identity} {name}"
            loss = _number(arm.get("loss"), f"{prefix} loss", maximum=bound)
            values = {"loss": loss}
            for key in ("cost", "latency_ms"):
                if key not in arm:
                    raise ValueError(f"{prefix} requires {key}; use null for unknown")
                values[key] = None if arm[key] is None else _number(arm[key], f"{prefix} {key}")
            violations = arm.get("violations")
            if not isinstance(violations, list):
                raise ValueError(f"{prefix} violations must be a list")
            for violation in violations:
                _text(violation, f"{prefix} violation")
            values["violations"] = violations
            arms[name].append(values)

    summaries = {}
    for name, rows in arms.items():
        summary = {
            "mean_loss": _mean([row["loss"] for row in rows]),
            "units_with_violations": sum(bool(row["violations"]) for row in rows),
        }
        for key in ("cost", "latency_ms"):
            known = [row[key] for row in rows if row[key] is not None]
            summary[f"known_{key}_units"] = len(known)
            summary[f"mean_{key}"] = _mean(known) if len(known) == len(rows) else None
        summaries[name] = summary

    # Normalize before subtraction to avoid finite-extreme arithmetic overflow.
    normalized_deltas = [
        new["loss"] / bound - old["loss"] / bound
        for old, new in zip(arms["incumbent"], arms["candidate"])
    ]
    mean_normalized_delta = _mean(normalized_deltas)
    delta = mean_normalized_delta * bound
    confirmation = None
    assessment = "descriptive_search_only"
    if phase == "confirm":
        alpha = _number(receipt.get("alpha"), "alpha", maximum=1)
        if not 0 < alpha < 1:
            raise ValueError("alpha must be strictly between 0 and 1")
        count = receipt.get("comparison_count")
        if type(count) is not int or count < 1:
            raise ValueError("comparison_count must be a positive integer fixed in advance")
        margin = _number(receipt.get("minimum_improvement"), "minimum_improvement", maximum=bound)
        # Bonferroni across the declared, prespecified family. log form avoids
        # alpha/count underflow. Hoeffding range of normalized differences is 2.
        radius = math.sqrt(2 * (math.log(count) - math.log(alpha)) / len(pairs))
        normalized_upper = min(1.0, mean_normalized_delta + radius)
        upper = normalized_upper * bound
        supported = normalized_upper < -(margin / bound)
        confirmation = {
            "method": "one-sided paired Hoeffding; fixed sample; Bonferroni family",
            "family_alpha": alpha,
            "comparison_count": count,
            "minimum_improvement": margin,
            "upper_mean_loss_delta": upper,
            "strict_margin_supported": supported,
        }
        assessment = "bound_supports_loss_margin" if supported else "insufficient_evidence"
    if kind in ("proxy", "fixture"):
        assessment = f"{kind}_evidence_only"
    if summaries["candidate"]["units_with_violations"]:
        assessment = "observed_candidate_constraint_violation"

    return {
        "schema_version": 1,
        **metadata,
        "phase": phase,
        "evidence_kind": kind,
        "paired_units": len(pairs),
        "loss_bound": bound,
        "incumbent": summaries["incumbent"],
        "candidate": summaries["candidate"],
        "mean_loss_delta": delta,
        "confirmation": confirmation,
        "assessment": assessment,
        "limits": [
            "Arithmetic on supplied outcomes, not verification of labels, independence, causal identification, or dataset isolation.",
            "Confirmation needs a prespecified sample/family, frozen policies/loss, and representative independent units; no optional stopping or adaptive test reuse.",
            "Zero observed violations is not proof of constraint compliance; missing costs/latencies remain unknown.",
            "A loss bound does not satisfy separate latency, cost, subgroup, safety, or deployment gates. No policy is promoted or executed.",
        ],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", type=Path, help="paired workflow outcome receipt JSON")
    args = parser.parse_args(argv)
    try:
        raw = args.receipt.read_bytes()
        data = json.loads(raw, object_pairs_hook=_object)
        result = compare(data)
        result["input_sha256"] = hashlib.sha256(raw).hexdigest()
        print(json.dumps(result, indent=2, allow_nan=False))
    except (OSError, ValueError, RecursionError, OverflowError) as exc:
        parser.exit(2, f"error: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
