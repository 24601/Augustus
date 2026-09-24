#!/usr/bin/env python3
"""Turn the E3 sigma report into the analysis lock, applying the prespecified narrowing as written.

Derived, not authored: the sigma report and the design lock's own constants are the only inputs,
so the same report always yields the same lock and anyone can recompute it. Nothing here reads a
confirmation row.

The narrowing is the interesting part, and it is applied literally rather than favourably. The
design lock says: if the timing pilot projects past the cap, or if sigma-hat exceeds 0.24368057,
the 4B reader is dropped before any confirmation read, taking the family from m = 6 to m = 3; and
if sigma-hat still exceeds 0.26502213, the equivalence readings are declared inconclusive before
confirmation, while the superiority rows still run.

At sigma-hat near the boundary that sequence buys power. Far above it, dropping a reader buys
nothing and costs a second reader's superiority evidence. Applying it anyway is the point: a
narrowing that is only applied when its consequence is convenient is not prespecified, it is a
decision made after seeing the data. The lock records both the application and the fact that it
did not help, because the second half is the lesson for the next lock.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from statistics import NormalDist

ALPHA = 0.05
POWER = 0.8
FULL_FAMILY = 6
NARROWED_FAMILY = 3
NARROWING_SIGMA = 0.24368057
INCONCLUSIVE_SIGMA = 0.26502213
DROPPED_READER = "Qwen3-4B"
GPU_CAP_HOURS = 24.0


def tail_level(m: int) -> float:
    return ALPHA / (2 * m)


def eb_radius(sd: float, n: int, span: float, m: int) -> float:
    log_term = math.log(2 / tail_level(m))
    return sd * math.sqrt(2 * log_term / n) + 7 * span * log_term / (3 * (n - 1))


def required_n(sd: float, margin: float, span: float, m: int, true_delta: float) -> int | None:
    """Smallest n reaching POWER for a superiority read at `true_delta`. Normal/fixed-SD."""
    phi = NormalDist().cdf
    if sd == 0:
        return None

    def achieved(n: int) -> float:
        radius = eb_radius(sd, n, span, m)
        distance = abs(true_delta) - margin
        if distance <= 0 or radius >= distance:
            return 0.0
        return phi((distance - radius) * math.sqrt(n) / sd)

    lo, hi = 2, 200_000_000
    if achieved(hi) < POWER:
        return None
    while lo < hi:
        mid = (lo + hi) // 2
        if achieved(mid) >= POWER:
            hi = mid
        else:
            lo = mid + 1
    return lo


def build(report: dict, available_n: int, projected_gpu_hours: float) -> dict:
    sigmas = [row["sd"] for row in report["contrasts"]]
    worst = max(sigmas)

    timing_triggers = projected_gpu_hours > GPU_CAP_HOURS
    sigma_triggers = worst > NARROWING_SIGMA
    narrowed = timing_triggers or sigma_triggers

    kept = [row for row in report["contrasts"]
            if not narrowed or row["reader"] != DROPPED_READER]
    m = NARROWED_FAMILY if narrowed else FULL_FAMILY
    if len(kept) != m:
        raise SystemExit(f"after narrowing the family should be {m} contrasts, not {len(kept)}")

    worst_kept = max(row["sd"] for row in kept)
    equivalence_inconclusive = worst_kept > INCONCLUSIVE_SIGMA

    rows = []
    for row in kept:
        # The planning effect is the search-split mean. The design lock fixes planning effects for
        # E1 from a synthetic population; E3 has no such population, so search supplies it, and the
        # row says so rather than letting a number pass as registered.
        needed = required_n(row["sd"], row["margin"], row["span"], m, row["mean"])
        powered = needed is not None and needed <= available_n
        rows.append({
            "reader": row["reader"], "contrast": row["contrast"], "mode": "superiority",
            "read_on": "lower bound; utilities are higher-is-better",
            "margin": row["margin"], "span": row["span"], "sigma_hat": row["sd"],
            "search_mean": row["mean"], "true_delta_source": "search split, not confirmation",
            "required_n": needed, "available_n": available_n, "powered": powered,
            "equivalence_reading": "inconclusive, prespecified" if equivalence_inconclusive
                                   else "available",
            "rerun_transportability_note": (
                "This arm thresholds p_answerable, whose rerun instability was measured at up to "
                "2.4x this margin; the frozen table makes the comparison internally exact"
                if "explicit" in row["contrast"] or "outcome" in row["contrast"] else None),
        })

    return {
        "experiment": "E3",
        "written": "after the search split and before any confirmation row was read",
        "family_size": m,
        "family_size_if_not_narrowed": FULL_FAMILY,
        "alpha": ALPHA,
        "tail_level": tail_level(m),
        "power_target": POWER,
        "available_confirmation_n": available_n,
        "realized_rerun_joint_disagreement": report["realized_rerun_joint_disagreement"],
        "narrowing": {
            "applied": narrowed,
            "triggered_by_timing": timing_triggers,
            "triggered_by_sigma": sigma_triggers,
            "projected_gpu_hours": projected_gpu_hours,
            "gpu_cap_hours": GPU_CAP_HOURS,
            "worst_sigma_hat_before": worst,
            "worst_sigma_hat_after": worst_kept,
            "sigma_boundary": NARROWING_SIGMA,
            "dropped_reader": DROPPED_READER if narrowed else None,
            "did_it_help": worst_kept <= INCONCLUSIVE_SIGMA,
            "note": ("Applied as written. Dropping a reader lowers m and so widens nothing except "
                     "through the tail level; it buys power only when sigma-hat sits near the "
                     "boundary. Here it did not, and the equivalence readings are inconclusive "
                     "anyway. Applying a narrowing only when its consequence is convenient would "
                     "make it a post-hoc decision, so it is applied and the cost is recorded."),
        },
        "equivalence_readings": "inconclusive, prespecified" if equivalence_inconclusive
                                else "available",
        "equivalence_boundary": INCONCLUSIVE_SIGMA,
        "contrasts": rows,
        "powered_count": sum(1 for row in rows if row["powered"]),
        "limits": [
            "required_n is a normal/fixed-SD planning approximation; the empirical Bernstein interval it plans for is distribution-free, this calculation is not.",
            "The planning effect is the search-split mean, not an independently registered number. A search mean is an estimate, and an optimistic one for the arm that was selected on that split.",
            "sigma-hat comes from search, which is not confirmation; the realized sd may differ and the interval, not this table, decides.",
            "The determinism check failed at 100% joint per-question disagreement, so the replay tables are the sole source and this rate travels with every E3 result.",
            "Arms that threshold p_answerable carry a rerun instability measured at up to 2.4x the margin. That bounds transportability to a regenerated table, not the internal comparison, which is exact because the table is frozen.",
        ],
    }


def render(lock: dict) -> str:
    narrowing = lock["narrowing"]
    lines = [
        "# E3 analysis lock",
        "",
        "Derived from the sigma report by `exp/e3_analysis_lock.py`, so it is a record rather than",
        "a choice. Written after the search split and **before any confirmation row was read**.",
        "",
        f"- Family m = {lock['family_size']} "
        f"(unnarrowed {lock['family_size_if_not_narrowed']}), α = {lock['alpha']}, "
        f"per-tail level {lock['tail_level']:.6f}, power target {lock['power_target']}",
        f"- Available confirmation questions: **{lock['available_confirmation_n']:,}**",
        f"- Powered contrasts: **{lock['powered_count']} of {len(lock['contrasts'])}**",
        f"- Equivalence readings: **{lock['equivalence_readings']}** "
        f"(boundary σ̂ ≤ {lock['equivalence_boundary']})",
        f"- Realized rerun joint disagreement: **{lock['realized_rerun_joint_disagreement']}**",
        "",
        "## The prespecified narrowing",
        "",
        f"- Applied: **{'yes' if narrowing['applied'] else 'no'}**; "
        f"triggered by σ̂ {'yes' if narrowing['triggered_by_sigma'] else 'no'}, "
        f"by timing {'yes' if narrowing['triggered_by_timing'] else 'no'} "
        f"({narrowing['projected_gpu_hours']} of {narrowing['gpu_cap_hours']} GPU-h)",
        f"- Worst σ̂ before {narrowing['worst_sigma_hat_before']:.4f}, "
        f"after {narrowing['worst_sigma_hat_after']:.4f}, boundary {narrowing['sigma_boundary']}",
        f"- Dropped reader: **{narrowing['dropped_reader'] or 'none'}**",
        f"- Did it restore the equivalence readings: "
        f"**{'yes' if narrowing['did_it_help'] else 'no'}**",
        "",
        narrowing["note"],
        "",
        "| Reader | Contrast | Margin | σ̂ | Search mean | Required n | Powered |",
        "| --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in lock["contrasts"]:
        needed = "infeasible" if row["required_n"] is None else f"{row['required_n']:,}"
        lines.append(
            f"| {row['reader']} | {row['contrast']} | {row['margin']:.3f} | "
            f"{row['sigma_hat']:.4f} | {row['search_mean']:+.4f} | {needed} | "
            f"{'yes' if row['powered'] else 'no'} |")
    lines += ["", "## Limits", ""] + [f"- {limit}" for limit in lock["limits"]] + [""]
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--sigma-report", type=Path, required=True)
    parser.add_argument("--available-n", type=int, required=True)
    parser.add_argument("--projected-gpu-hours", type=float, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)

    report = json.loads(args.sigma_report.read_text(encoding="utf-8"))
    lock = build(report, args.available_n, args.projected_gpu_hours)
    lock["sigma_report_sha256"] = hashlib.sha256(args.sigma_report.read_bytes()).hexdigest()
    text = render(lock)
    args.out.write_text(text, encoding="utf-8")
    args.out.with_suffix(".json").write_text(json.dumps(lock, indent=2), encoding="utf-8")
    print(text)
    print(f"\nlock sha256: {hashlib.sha256(text.encode('utf-8')).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
