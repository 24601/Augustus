#!/usr/bin/env python3
"""Compare paired, bounded outcome losses; never execute or promote a policy.

Input is one JSON receipt with schema_version=1, phase (search/confirm),
incumbent_id, candidate_id, dataset_id, outcome_definition, sampling_unit,
evidence_kind (observed/adjudicated/proxy/fixture), loss_bound, and pairs.
Each pair has a unique id and incumbent/candidate objects with loss in
[0, loss_bound], cost (nonnegative or null), latency_ms (nonnegative or null),
and violations (a list of nonempty strings). Confirmation also needs alpha,
minimum_improvement, a positive integer comparison_count fixed in advance,
and a sampling_design, which must be equal_probability. Optional
excluded_units (nonnegative integer or null) and missing_outcome_policy
(nonempty text or null) record caller-declared attrition; absent means unknown.

Confirmation declares a mode and a method.

mode: superiority (default) needs the upper bound below -minimum_improvement.
non_inferiority needs it below +minimum_improvement; it never establishes an
improvement, only that the candidate is not worse by more than the margin.

method:
  hoeffding (default) is the 0.7.2 bound, one-sided at alpha/comparison_count,
    using only the declared loss_bound. Its output is unchanged.
  empirical_bernstein uses the sample standard deviation of the paired
    differences (Maurer-Pontil), read from the two-sided family interval at
    alpha/(2*comparison_count) per tail, so superiority, non-inferiority and
    equivalence can be read from one interval. It is tighter than hoeffding
    once the observed spread is small, and its radius never collapses to zero,
    because of a floor that depends only on the range, n and the level.
  sign_exact has no upper bound. Losses must be in {0, loss_bound},
    minimum_improvement must be 0, and it reports the one-sided exact binomial
    p-value on discordant pairs against alpha/comparison_count. It certifies
    direction only, never a magnitude.

Every method assumes independent representative units of the declared
sampling_unit, a fixed sample size, frozen policies and loss, and no adaptive
reuse of confirmation outcomes. Equal inclusion probability is not the same as
independence: a clustered sample can satisfy it and still break coverage, so
aggregate to the independent unit before calling this.

The program checks arithmetic/schema, NOT those empirical assumptions or
whether an observed outcome is causal evidence. Missing costs stay unknown.
Search is descriptive only. See references/optimizer-integration.md.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import statistics
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


def _exact_binomial_upper_tail(successes, trials):
    """Exact P(X >= successes) for X ~ Binomial(trials, 1/2), as a Fraction.

    Exact rational arithmetic: no floating point, so a p-value near alpha is
    decided by the arithmetic rather than by rounding.
    """
    total = sum(math.comb(trials, k) for k in range(successes, trials + 1))
    return Fraction(total, 2 ** trials)


def _eb_radius(differences, n, tail_level, span):
    """Maurer-Pontil empirical Bernstein radius, one tail at tail_level.

    span is the range of the paired differences (2 * loss_bound). The second
    term depends only on span, n and the level, so the radius cannot collapse
    when every observed difference is zero.
    """
    spread = statistics.stdev(differences) if n > 1 else 0.0
    return (spread * math.sqrt(2 * math.log(2 / tail_level) / n)
            + 7 * span * math.log(2 / tail_level) / (3 * (n - 1)))


def _mean(values):
    # statistics.mean accumulates exact ratios before rounding to float.
    # Dividing first can both overflow near float max and erase subnormals.
    return statistics.mean(values)


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
    excluded = receipt.get("excluded_units")
    if excluded is not None and (type(excluded) is not int or excluded < 0):
        raise ValueError("excluded_units must be a nonnegative integer or null")
    missing_policy = receipt.get("missing_outcome_policy")
    if missing_policy is not None:
        missing_policy = _text(missing_policy, "missing_outcome_policy")
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

    # Preserve paired differences before rounding/normalizing. Dividing each
    # loss first can erase a representable delta; subtracting rounded means
    # can also erase paired cancellation residuals. Losses are in [0, bound],
    # so the final exact mean difference is finite in [-bound, bound].
    exact_delta = sum(
        Fraction(new["loss"]) - Fraction(old["loss"])
        for old, new in zip(arms["incumbent"], arms["candidate"])
    ) / len(pairs)
    delta = float(exact_delta)
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
        mode = receipt.get("mode", "superiority")
        if mode not in ("superiority", "non_inferiority"):
            raise ValueError("mode must be superiority or non_inferiority")
        method = receipt.get("method", "hoeffding")
        if method not in ("hoeffding", "empirical_bernstein", "sign_exact"):
            raise ValueError("method must be hoeffding, empirical_bernstein, or sign_exact")
        design = receipt.get("sampling_design")
        if design is None:
            raise ValueError("confirmation requires sampling_design; 0.8.0 supports equal_probability only")
        design = _text(design, "sampling_design")
        if design != "equal_probability":
            raise ValueError(f"unsupported_sampling_design: {design}")
        differences = [new["loss"] - old["loss"]
                       for old, new in zip(arms["incumbent"], arms["candidate"])]
        threshold = -margin if mode == "superiority" else margin
        if method == "sign_exact":
            if margin != 0:
                raise ValueError("sign_exact certifies direction only; minimum_improvement must be 0")
            for name in arms:
                for row in arms[name]:
                    if row["loss"] not in (0.0, bound):
                        raise ValueError("sign_exact requires losses in {0, loss_bound}")
            wins = sum(1 for value in differences if value < 0)
            losses = sum(1 for value in differences if value > 0)
            discordant = wins + losses
            # One-sided exact binomial on discordant pairs, compared as exact
            # rationals against alpha/count so no rounding decides the verdict.
            p_value = _exact_binomial_upper_tail(wins, discordant) if discordant else Fraction(1)
            supported = p_value <= Fraction(alpha).limit_denominator(10 ** 12) / count
            confirmation = {
                "method": "sign_exact: one-sided exact binomial on discordant pairs; direction only",
                "family_alpha": alpha,
                "comparison_count": count,
                "mode": mode,
                "minimum_improvement": margin,
                "sampling_design": design,
                "discordant_pairs": discordant,
                "candidate_wins": wins,
                "exact_p_value": float(p_value),
                "upper_mean_loss_delta": None,
                "strict_margin_supported": supported,
            }
        else:
            if method == "hoeffding":
                # Unchanged 0.7.2 arithmetic, one-sided at alpha/count, so its
                # output stays byte-identical. The normalized range is 2.
                radius = math.sqrt(2 * (math.log(count) - math.log(alpha)) / len(pairs))
                radius_in_loss_units = Fraction(radius) * Fraction(bound)
                label = "one-sided paired Hoeffding; fixed sample; Bonferroni family"
            else:
                # Two-sided family interval at alpha/(2*count) per tail, so
                # every claim type is read from one interval.
                tail = alpha / (2 * count)
                radius_in_loss_units = Fraction(
                    _eb_radius(differences, len(pairs), tail, 2 * bound))
                label = ("empirical Bernstein (Maurer-Pontil); two-sided family interval"
                         " at alpha/(2*comparison_count) per tail")
            # Accumulate in loss units exactly, then round the reported upper
            # toward +infinity. Test that same upper so a rounded equality never
            # claims strict improvement. The transcendental radius still uses
            # platform binary64 math, not a certified interval implementation.
            exact_upper = min(Fraction(bound), exact_delta + radius_in_loss_units)
            upper = float(exact_upper)
            if Fraction(upper) < exact_upper:
                upper = math.nextafter(upper, math.inf)
            supported = upper < threshold
            confirmation = {
                "method": label,
                "family_alpha": alpha,
                "comparison_count": count,
                "minimum_improvement": margin,
                "upper_mean_loss_delta": upper,
                "strict_margin_supported": supported,
            }
            if method != "hoeffding" or mode != "superiority":
                confirmation["mode"] = mode
                confirmation["sampling_design"] = design
        if supported:
            assessment = ("bound_supports_loss_margin" if mode == "superiority"
                          else "bound_supports_non_inferiority")
        else:
            assessment = "insufficient_evidence"
    if kind in ("proxy", "fixture"):
        assessment = f"{kind}_evidence_only"
    if summaries["candidate"]["units_with_violations"]:
        assessment = f"{kind}_candidate_constraint_violation"

    return {
        "schema_version": 1,
        **metadata,
        "phase": phase,
        "evidence_kind": kind,
        "paired_units": len(pairs),
        "excluded_units": excluded,
        "missing_outcome_policy": missing_policy,
        "loss_bound": bound,
        "incumbent": summaries["incumbent"],
        "candidate": summaries["candidate"],
        "mean_loss_delta": delta,
        "confirmation": confirmation,
        "assessment": assessment,
        "limits": [
            "Arithmetic on supplied outcomes, not verification of labels, independence, causal identification, or dataset isolation.",
            "Paired summaries cover supplied pairs only; exclusions and missing-outcome policy are caller declarations, not attrition correction. Null means unknown.",
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
