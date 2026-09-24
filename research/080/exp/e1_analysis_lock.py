#!/usr/bin/env python3
"""Turn the E1 fit report into the analysis lock, deterministically.

The analysis lock is written after fitting and calibration and BEFORE any confirmation row is
read. Its job is to fix, in advance and in public, the things that decide what the confirmation
run is allowed to claim: sigma-hat per contrast, the required n, the powered set, the numeric
margins, and any prespecified narrowing.

Generating it from the fit report rather than writing it by hand is the point. A hand-written lock
is an opportunity to choose; a derived one is a record. The only inputs are the fit report and the
design lock's own constants, so the same fit report always yields the same lock, and anyone can
recompute it.

Nothing here reads a label or an outcome.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from statistics import NormalDist

ALPHA = 0.05
M_FAMILY = 19
POWER = 0.8
HELD_OUT = ("1:19", "1:49", "4:1")


def tail_level(m: int = M_FAMILY, alpha: float = ALPHA) -> float:
    return alpha / (2 * m)


def eb_radius(sd: float, n: int, span: float, m: int = M_FAMILY) -> float:
    delta = tail_level(m)
    log_term = math.log(2 / delta)
    return sd * math.sqrt(2 * log_term / n) + 7 * span * log_term / (3 * (n - 1))


def required_n(sd: float, margin: float, span: float, mode: str, true_delta: float = 0.0,
               m: int = M_FAMILY) -> int | None:
    """Smallest n reaching POWER for the registered claim. Normal/fixed-SD approximation."""
    phi = NormalDist().cdf

    def achieved(n: int) -> float:
        radius = eb_radius(sd, n, span, m)
        if mode == "equivalence":
            if radius >= margin:
                return 0.0
            return 2 * phi((margin - radius) * math.sqrt(n) / sd) - 1 if sd > 0 else 1.0
        # superiority via the upper bound: distance from the truth to -margin
        distance = abs(true_delta) - margin
        if distance <= 0 or radius >= distance:
            return 0.0
        return phi((distance - radius) * math.sqrt(n) / sd) if sd > 0 else 1.0

    if sd == 0:
        # A degenerate contrast, such as A against B-stale at 1:1 where the arms are identical.
        # No n makes a claim about it, and saying so is the honest answer.
        return None
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


def classify(contrast: dict) -> tuple[str, float, str]:
    """The registered mode, planning effect and its source for one contrast, from the design lock.

    A vs B-stale is a candidate-better superiority read at the planning effect the synthetic
    population gave. A vs B-retrain is non-inferiority. C, C* and E against A are equivalence.

    Under the prior shift S the design lock registers A-recal vs B-retrain_S as non-inferiority and
    the three escalation-shaped rows as superiority reads on A-recal. The synthetic population gave
    no planning effect for those three, so the calibration split supplies it. That is the same
    split that supplies sigma-hat, it is not the confirmation split, and the lock says so on the
    row rather than letting an invented number pass as registered.
    """
    name = contrast["contrast"]
    if name.startswith("A - B-stale"):
        return "superiority", -0.042, "synthetic population, design lock"
    if "B-retrain" in name:
        return "non_inferiority", 0.0, "registered margin, no effect needed"
    if contrast.get("ratio") == "S":
        return "superiority", contrast["mean"], "calibration split, not confirmation"
    return "equivalence", 0.0, "registered margin, no effect needed"


def build(fit: dict, available_n: int, corpus: str) -> dict:
    rows = []
    for contrast in fit["contrasts"]:
        mode, true_delta, true_delta_source = classify(contrast)
        margin = contrast["margin"]
        sd = contrast["sd"]
        span = contrast["span"]
        needed = required_n(sd, margin, span,
                            "equivalence" if mode != "superiority" else "superiority",
                            true_delta)
        powered = needed is not None and needed <= available_n
        rows.append({
            "ratio": contrast["ratio"],
            "contrast": contrast["contrast"],
            "held_out": contrast["held_out"],
            "mode": mode,
            "true_delta": true_delta,
            "true_delta_source": true_delta_source,
            "margin": margin,
            "span": span,
            "sigma_hat": sd,
            "calibration_mean": contrast["mean"],
            "required_n": needed,
            "available_n": available_n,
            "powered": powered,
            "counts_toward_an_outcome_row": powered and contrast["held_out"],
        })

    # The fit reports every ratio, but only the held-out rows and the S rows are the primary
    # family the α split pays for. If that count drifts from m, the family error claim is wrong,
    # and a silent table is the worst way to find out.
    primary = [r for r in rows if r["held_out"]]
    if len(primary) != M_FAMILY:
        raise SystemExit(f"the fit report has {len(primary)} primary contrasts, "
                         f"but the design lock's family is {M_FAMILY}")

    held_out_powered = sorted({r["ratio"] for r in rows
                               if r["powered"] and r["held_out"]})
    # The Supports row for the equivalence claims needs powered EQUIVALENCE contrasts at held-out
    # ratios. A powered superiority contrast at the same ratio says nothing about equivalence, so
    # counting it here would let a corpus that cannot carry the claim appear to carry it.
    held_out_powered_equivalence = sorted({r["ratio"] for r in rows
                                           if r["powered"] and r["held_out"]
                                           and r["mode"] == "equivalence"})
    outcome = ("at least two held-out ratios have a powered equivalence contrast, so the Supports "
               "row is reachable"
               if len(held_out_powered_equivalence) >= 2 else
               "fewer than two held-out ratios have a powered equivalence contrast, so the "
               "prespecified INCONCLUSIVE row applies to the equivalence claims before "
               "confirmation is read")
    return {
        "experiment": "E1",
        "corpus": corpus,
        "written": "after fitting and calibration, before any confirmation row was read",
        "family_size": M_FAMILY,
        "alpha": ALPHA,
        "tail_level": tail_level(),
        "power_target": POWER,
        "available_confirmation_n": available_n,
        "temperature": fit["temperature"],
        "cost_of_A_by_ratio": fit["cost_of_A_by_ratio"],
        "contrasts": rows,
        "powered_count": sum(1 for r in rows if r["powered"]),
        "powered_held_out_ratios": held_out_powered,
        "powered_held_out_ratios_equivalence": held_out_powered_equivalence,
        "powered_count_by_mode": {
            mode: sum(1 for r in rows if r["powered"] and r["mode"] == mode)
            for mode in ("superiority", "non_inferiority", "equivalence")
        },
        "prespecified_reading": outcome,
        "limits": [
            "required_n is a normal/fixed-SD planning approximation; the empirical Bernstein interval it plans for is distribution-free, this calculation is not.",
            "sigma-hat comes from the calibration split, which is not the confirmation split; the realized sd may differ and the interval, not this table, decides.",
            "A contrast with sigma-hat 0 is degenerate, not powered: at 1:1 the plug-in and the stale threshold are the same rule, so no n makes a claim about their difference.",
            "An unpowered contrast is still reported with its interval and counts toward no outcome row in either direction.",
        ],
    }


def render(lock: dict) -> str:
    lines = [
        f"# E1 analysis lock, {lock['corpus']}",
        "",
        "Derived from the fit report by `exp/e1_analysis_lock.py`, so it is a record rather than a",
        "choice: the same fit report always yields this file. Written after fitting and calibration",
        "and **before any confirmation row was read**.",
        "",
        f"- Family m = {lock['family_size']}, α = {lock['alpha']}, "
        f"per-tail level {lock['tail_level']:.6f}, power target {lock['power_target']}",
        f"- Available confirmation rows: **{lock['available_confirmation_n']:,}**",
        f"- Fitted temperature: {lock['temperature']:.6f} (scalar, no intercept)",
        f"- Powered contrasts: **{lock['powered_count']} of {len(lock['contrasts'])}**",
        f"- Powered held-out ratios: {', '.join(lock['powered_held_out_ratios']) or 'none'}",
        f"- Powered held-out ratios with an equivalence contrast: "
        f"{', '.join(lock['powered_held_out_ratios_equivalence']) or 'none'}",
        f"- Powered by mode: " + ", ".join(
            f"{mode} {count}" for mode, count in lock["powered_count_by_mode"].items()),
        "",
        f"**Prespecified reading:** {lock['prespecified_reading']}.",
        "",
        "| Ratio | Contrast | Held out | Mode | Margin | σ̂ | Span | Required n | Powered |",
        "| --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in lock["contrasts"]:
        needed = "infeasible" if row["required_n"] is None else f"{row['required_n']:,}"
        lines.append(
            f"| {row['ratio']} | {row['contrast']} | {'yes' if row['held_out'] else 'no'} | "
            f"{row['mode']} | {row['margin']:.5f} | {row['sigma_hat']:.4f} | {row['span']:.2f} | "
            f"{needed} | {'yes' if row['powered'] else 'no'} |")
    lines += ["", "## Limits", ""] + [f"- {limit}" for limit in lock["limits"]] + [""]
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--fit", type=Path, required=True)
    parser.add_argument("--available-n", type=int, required=True)
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)

    fit = json.loads(args.fit.read_text(encoding="utf-8"))
    lock = build(fit, args.available_n, args.corpus)
    lock["fit_report_sha256"] = hashlib.sha256(args.fit.read_bytes()).hexdigest()
    text = render(lock)
    args.out.write_text(text, encoding="utf-8")
    args.out.with_suffix(".json").write_text(json.dumps(lock, indent=2), encoding="utf-8")
    print(text)
    print(f"\nlock sha256: {hashlib.sha256(text.encode('utf-8')).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
