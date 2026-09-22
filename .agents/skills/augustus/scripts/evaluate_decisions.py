#!/usr/bin/env python3
"""Offline evaluation for labeled binary decision probabilities.

Input is JSONL with unique ``{id: str, p: float, y: 0|1}`` rows. ``p`` is the
probability assigned to the positive class; it is not automatically a
probability of correctness. Optional ``p_base`` values support a Brier
comparison only when present on every row.

The complete-binary threshold report treats every row as either positive or
negative. Its ``action_rate`` is the predicted-positive fraction, not
selective coverage. The returned ``coverage`` field is a deprecated alias for
``action_rate`` kept only for programmatic compatibility.

Selective evaluation is opt-in: --lower-threshold / --upper-threshold decide
negative at p <= lower, positive at p >= upper, and abstain strictly between
them. It reports decided coverage and selective error separately. Costs are
never invented: full-binary costs require --cost-fp and --cost-fn; selective
cost additionally requires --cost-abstain.
"""

import argparse
from fractions import Fraction
import json
import math
import statistics
import sys


def _finite_number(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a finite number")
    try:
        value = float(value)
    except OverflowError as exc:
        raise ValueError(f"{name} must be a finite number") from exc
    if not math.isfinite(value):
        raise ValueError(f"{name} must be a finite number")
    return value


def _probability(value, name):
    value = _finite_number(value, name)
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be in [0,1]")
    return value


def _nonnegative_cost(value, name):
    value = _finite_number(value, name)
    if value < 0.0:
        raise ValueError(f"{name} must be non-negative")
    return value


def _positive_bins(bins):
    if isinstance(bins, bool) or not isinstance(bins, int) or bins <= 0:
        raise ValueError("bins must be a positive integer")
    return bins


def _format_boundary(value):
    """Avoid labels such as [0.3,0.7) for thirds when bins is not ten."""
    return format(value, ".12g")


def _validate_rows(rows, key="p"):
    if not rows:
        raise ValueError("no rows supplied")
    for row in rows:
        _probability(row[key], key)
        if row.get("y") not in (0, 1) or isinstance(row.get("y"), bool):
            raise ValueError("y must be 0 or 1")


def _utf8_lines(path):
    """Yield text lines while turning invalid UTF-8 into a normal input error."""
    try:
        with open(path, encoding="utf-8") as source:
            yield from source
    except (OSError, UnicodeDecodeError) as exc:
        raise ValueError(f"cannot read UTF-8 JSONL: {exc}") from exc


def load(path):
    """Load and validate unique, labeled decision rows from JSONL."""
    rows = []
    ids = set()
    for line_number, line in enumerate(_utf8_lines(path), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line, object_pairs_hook=_unique_object)
        except (ValueError, RecursionError) as exc:
            raise ValueError(f"line {line_number}: invalid JSON: {exc}") from exc
        if not isinstance(row, dict):
            raise ValueError(f"line {line_number}: row must be a JSON object")
        row_id = row.get("id")
        if not isinstance(row_id, str) or not row_id:
            raise ValueError(f"line {line_number}: id must be a non-empty string")
        if row_id in ids:
            raise ValueError(f"line {line_number}: duplicate id {row_id!r}")
        ids.add(row_id)
        try:
            row["p"] = _probability(row.get("p"), "p")
            if row.get("y") not in (0, 1) or isinstance(row.get("y"), bool):
                raise ValueError("y must be 0 or 1")
            if "p_base" in row:
                row["p_base"] = _probability(row["p_base"], "p_base")
            if "group" in row and not isinstance(row["group"], str):
                raise ValueError("group must be a string when present")
        except ValueError as exc:
            raise ValueError(f"line {line_number}: {exc}") from exc
        rows.append(row)
    if not rows:
        raise ValueError("no labeled rows found")
    return rows


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def brier(rows, key="p"):
    _validate_rows(rows, key)
    return sum((row[key] - row["y"]) ** 2 for row in rows) / len(rows)


def log_loss(rows, key="p"):
    """Mean binary log loss without epsilon clipping.

    An exact zero probability for the observed outcome is reported as infinity;
    replacing it with an arbitrary epsilon would silently change the metric.
    """
    _validate_rows(rows, key)
    losses = []
    for row in rows:
        p = row[key]
        if row["y"] == 1:
            if p == 0.0:
                return math.inf
            losses.append(-math.log(p))
        else:
            if p == 1.0:
                return math.inf
            # Forming 1-p first discards small but representable losses.
            losses.append(-math.log1p(-p))
    return statistics.mean(losses)


def reliability(rows, bins=10, key="p"):
    """Non-empty equal-width reliability bins with mathematically exact labels."""
    _validate_rows(rows, key)
    bins = _positive_bins(bins)
    result = []
    for index in range(bins):
        lo, hi = index / bins, (index + 1) / bins
        bucket = [
            row for row in rows
            if lo <= row[key] and (row[key] < hi or index == bins - 1)
        ]
        if bucket:
            right = "]" if index == bins - 1 else ")"
            result.append({
                "bin": f"[{_format_boundary(lo)},{_format_boundary(hi)}{right}",
                "n": len(bucket),
                "mean_p": sum(row[key] for row in bucket) / len(bucket),
                "rate": sum(row["y"] for row in bucket) / len(bucket),
            })
    return result


def ece_equal_width(rows, bins=10, key="p"):
    """Equal-width expected calibration error for a binary positive probability."""
    buckets = reliability(rows, bins=bins, key=key)
    total = len(rows)
    return sum(bucket["n"] / total * abs(bucket["mean_p"] - bucket["rate"])
               for bucket in buckets)


def ece_quantile(rows, bins=10, key="p"):
    """Tie-preserving quantile ECE, invariant to JSONL ordering for tied p."""
    _validate_rows(rows, key)
    bins = min(_positive_bins(bins), len(rows))
    ordered = sorted(rows, key=lambda row: row[key])
    start = 0
    total = 0.0
    for index in range(bins):
        if start == len(ordered):
            break
        end = len(ordered) if index == bins - 1 else math.ceil((index + 1) * len(ordered) / bins)
        end = max(end, start + 1)
        while end < len(ordered) and ordered[end - 1][key] == ordered[end][key]:
            end += 1
        bucket = ordered[start:end]
        total += len(bucket) / len(rows) * abs(
            sum(row[key] for row in bucket) / len(bucket)
            - sum(row["y"] for row in bucket) / len(bucket)
        )
        start = end
    return total


def accuracy(rows, threshold=0.5, key="p"):
    _validate_rows(rows, key)
    threshold = _probability(threshold, "threshold")
    return sum((row[key] >= threshold) == bool(row["y"]) for row in rows) / len(rows)


def pairwise_ranking_auc(rows, key="p"):
    """O(n log n) Mann-Whitney AUC. It is ranking, not calibration."""
    _validate_rows(rows, key)
    positive_total = sum(row["y"] == 1 for row in rows)
    negative_total = len(rows) - positive_total
    if not positive_total or not negative_total:
        return None
    ordered = sorted(rows, key=lambda row: row[key])
    negative_before = 0
    wins = 0.0
    start = 0
    while start < len(ordered):
        end = start + 1
        while end < len(ordered) and ordered[end][key] == ordered[start][key]:
            end += 1
        group = ordered[start:end]
        group_positive = sum(row["y"] == 1 for row in group)
        group_negative = len(group) - group_positive
        wins += group_positive * negative_before + 0.5 * group_positive * group_negative
        negative_before += group_negative
        start = end
    return wins / (positive_total * negative_total)


def _weighted_cost(total, *cost_counts):
    # Exact rational accumulation avoids rounded shares overflowing a finite
    # mean or erasing subnormal costs. Only the final result rounds to float.
    return float(sum(Fraction(cost) * count for cost, count in cost_counts) / total)


def _complete_cost(fp, fn, total, cost_fp, cost_fn):
    if cost_fp is None and cost_fn is None:
        return None
    if cost_fp is None or cost_fn is None:
        raise ValueError("cost-fp and cost-fn must be supplied together")
    cost_fp = _nonnegative_cost(cost_fp, "cost-fp")
    cost_fn = _nonnegative_cost(cost_fn, "cost-fn")
    if cost_fp == 0.0 and cost_fn == 0.0:
        raise ValueError("at least one of cost-fp or cost-fn must be positive")
    return _weighted_cost(total, (cost_fp, fp), (cost_fn, fn))


def sweep(rows, thresholds, cost_fp=None, cost_fn=None, key="p"):
    """Evaluate complete binary threshold policies.

    ``action_rate`` is predicted-positive fraction. ``coverage`` is its
    deprecated compatibility alias; it must not be read as selective coverage.
    """
    _validate_rows(rows, key)
    if not thresholds:
        raise ValueError("at least one threshold is required")
    result = []
    for raw_threshold in thresholds:
        threshold = _probability(raw_threshold, "threshold")
        positive = [row for row in rows if row[key] >= threshold]
        fp = sum(row["y"] == 0 for row in positive)
        fn = sum(row[key] < threshold and row["y"] == 1 for row in rows)
        action_rate = len(positive) / len(rows)
        result.append({
            "policy": "threshold",
            "threshold": threshold,
            "action_rate": action_rate,
            "coverage": action_rate,  # Deprecated alias; see docstring.
            "fp": fp,
            "fn": fn,
            "cost": _complete_cost(fp, fn, len(rows), cost_fp, cost_fn),
        })
    return result


def always_negative(rows, cost_fp=None, cost_fn=None, key="p"):
    """The explicit zero-action comparator for a full binary policy search."""
    _validate_rows(rows, key)
    fn = sum(row["y"] == 1 for row in rows)
    return {
        "policy": "always_negative",
        "threshold": None,
        "action_rate": 0.0,
        "coverage": 0.0,  # Deprecated alias; see sweep().
        "fp": 0,
        "fn": fn,
        "cost": _complete_cost(0, fn, len(rows), cost_fp, cost_fn),
    }


def cost_optimal_threshold(rows, cost_fp, cost_fn, key="p"):
    """Find the lowest-cost complete binary policy, including always-negative.

    This transparent small-dataset search is O(n * distinct scores), worst-case
    O(n squared); use a cumulative sorted-count implementation for large files.
    """
    _validate_rows(rows, key)
    candidates = sweep(rows, sorted({0.0, 1.0, *(row[key] for row in rows)}),
                       cost_fp, cost_fn, key)
    candidates.append(always_negative(rows, cost_fp, cost_fn, key))
    return min(candidates, key=lambda result: result["cost"])


def selective_policy(rows, lower, upper, cost_fp=None, cost_fn=None, cost_abstain=None, key="p"):
    """Evaluate abstention with inclusive decision boundaries.

    p <= lower is negative; p >= upper is positive; only lower < p < upper
    abstains. Requiring lower < upper gives every equality a single policy.
    """
    _validate_rows(rows, key)
    lower = _probability(lower, "lower-threshold")
    upper = _probability(upper, "upper-threshold")
    if not lower < upper:
        raise ValueError("need 0 <= lower-threshold < upper-threshold <= 1")
    positive = [row for row in rows if row[key] >= upper]
    negative = [row for row in rows if row[key] <= lower]
    abstained = len(rows) - len(positive) - len(negative)
    fp = sum(row["y"] == 0 for row in positive)
    fn = sum(row["y"] == 1 for row in negative)
    decided = len(positive) + len(negative)
    if cost_fp is cost_fn is cost_abstain is None:
        cost = None
    elif cost_fp is None or cost_fn is None or cost_abstain is None:
        raise ValueError("cost-fp, cost-fn, and cost-abstain must be supplied together")
    else:
        c_fp = _nonnegative_cost(cost_fp, "cost-fp")
        c_fn = _nonnegative_cost(cost_fn, "cost-fn")
        c_abstain = _nonnegative_cost(cost_abstain, "cost-abstain")
        if c_fp == c_fn == c_abstain == 0.0:
            raise ValueError("at least one policy cost must be positive")
        cost = _weighted_cost(len(rows), (c_fp, fp), (c_fn, fn), (c_abstain, abstained))
    return {
        "lower_threshold": lower,
        "upper_threshold": upper,
        "tie_policy": "p <= lower: negative; p >= upper: positive",
        "decided_coverage": decided / len(rows),
        "abstention_rate": abstained / len(rows),
        "abstentions": abstained,
        "fp": fp,
        "fn": fn,
        "selective_error": None if decided == 0 else (fp + fn) / decided,
        "cost": cost,
    }


def self_test():
    """Small numerical smoke test; comprehensive cases live in tests/."""
    rows = [
        {"id": "a", "p": 0.0, "y": 0},
        {"id": "b", "p": 0.5, "y": 1},
        {"id": "c", "p": 1.0, "y": 1},
    ]
    assert brier(rows) == 1 / 12
    assert log_loss(rows) == -math.log(0.5) / 3
    assert reliability(rows, bins=3)[0]["bin"] == "[0,0.333333333333)"
    assert reliability(rows, bins=3)[-1]["bin"] == "[0.666666666667,1]"
    assert sweep(rows, [0.5], 1, 1)[0]["action_rate"] == 2 / 3
    selective = selective_policy(rows, 0.0, 1.0, 1, 1, 0.25)
    assert selective["decided_coverage"] == 2 / 3 and selective["abstentions"] == 1
    assert always_negative([{"id": "only", "p": 1.0, "y": 0}], 1, 1)["cost"] == 0.0
    print("self-test ok")


def _parse_thresholds(value):
    try:
        thresholds = [float(part.strip()) for part in value.split(",") if part.strip()]
    except ValueError as exc:
        raise ValueError("thresholds must be comma-separated numbers") from exc
    if not thresholds:
        raise ValueError("at least one threshold is required")
    return thresholds


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("labels", nargs="?")
    parser.add_argument("--cost-fp", type=float)
    parser.add_argument("--cost-fn", type=float)
    parser.add_argument("--cost-abstain", type=float)
    parser.add_argument("--bins", type=int, default=10)
    parser.add_argument("--thresholds", default="0.3,0.5,0.7,0.9")
    parser.add_argument("--lower-threshold", type=float)
    parser.add_argument("--upper-threshold", type=float)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if not args.labels:
        parser.error("labels.jsonl required (or --self-test)")
    try:
        rows = load(args.labels)
        thresholds = _parse_thresholds(args.thresholds)
        for threshold in thresholds:
            _probability(threshold, "threshold")
        _positive_bins(args.bins)
        if (args.cost_fp is None) != (args.cost_fn is None):
            raise ValueError("cost-fp and cost-fn must be supplied together")
        if args.cost_fp is not None:
            _complete_cost(0, 0, 1, args.cost_fp, args.cost_fn)
        selective_requested = args.lower_threshold is not None or args.upper_threshold is not None
        if selective_requested and (args.lower_threshold is None or args.upper_threshold is None):
            raise ValueError("lower-threshold and upper-threshold must be supplied together")
        if args.cost_abstain is not None and not selective_requested:
            raise ValueError("cost-abstain requires --lower-threshold and --upper-threshold")
        if selective_requested:
            selective_policy(rows, args.lower_threshold, args.upper_threshold,
                             args.cost_fp, args.cost_fn, args.cost_abstain)
    except ValueError as exc:
        parser.error(str(exc))

    loss = log_loss(rows)
    loss_text = "inf" if math.isinf(loss) else f"{loss:.4f}"
    print(f"n={len(rows)} brier={brier(rows):.4f} log_loss={loss_text}")
    print(f"ece_equal_width={ece_equal_width(rows, args.bins):.4f} "
          f"ece_quantile={ece_quantile(rows, args.bins):.4f}")
    auc = pairwise_ranking_auc(rows)
    print("auc: undefined (one class missing)" if auc is None
          else f"auc={auc:.4f} accuracy@0.5={accuracy(rows):.4f}")
    baseline_rows = [row for row in rows if "p_base" in row]
    if len(baseline_rows) == len(rows):
        print(f"baseline brier={brier(rows, 'p_base'):.4f} (n={len(rows)})")
    elif baseline_rows:
        print(f"baseline: partial (n={len(baseline_rows)}/{len(rows)}; no comparative claim)")
    else:
        print("baseline: none supplied (limitation: no comparative claim)")
    for bucket in reliability(rows, args.bins):
        print(f"bin {bucket['bin']:>18} n={bucket['n']:>4} "
              f"mean_p={bucket['mean_p']:.3f} rate={bucket['rate']:.3f}")
    for result in sweep(rows, thresholds, args.cost_fp, args.cost_fn):
        cost = "unavailable" if result["cost"] is None else f"{result['cost']:.4f}"
        print(f"t={result['threshold']:.4g} action_rate={result['action_rate']:.3f} "
              f"fp={result['fp']} fn={result['fn']} cost={cost}")
    if args.cost_fp is None:
        print("cost_optimal: unavailable (provide --cost-fp and --cost-fn)")
    else:
        best = cost_optimal_threshold(rows, args.cost_fp, args.cost_fn)
        threshold = "always_negative" if best["threshold"] is None else f"{best['threshold']:.4g}"
        print(f"cost_optimal policy={threshold} cost={best['cost']:.4f} "
              "[IN_SAMPLE_CALIBRATION_ONLY: select on one split; evaluate on another]")
    if selective_requested:
        result = selective_policy(rows, args.lower_threshold, args.upper_threshold,
                                  args.cost_fp, args.cost_fn, args.cost_abstain)
        error = "undefined" if result["selective_error"] is None else f"{result['selective_error']:.4f}"
        cost = "unavailable" if result["cost"] is None else f"{result['cost']:.4f}"
        print(f"selective lower={result['lower_threshold']:.4g} upper={result['upper_threshold']:.4g} "
              f"decided_coverage={result['decided_coverage']:.3f} "
              f"abstention_rate={result['abstention_rate']:.3f} "
              f"selective_error={error} fp={result['fp']} fn={result['fn']} cost={cost}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
