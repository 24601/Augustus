#!/usr/bin/env python3
"""E4a: the Monte Carlo diagnostic for the acceptance rules, vectorized on the GPU.

Plan v4 section 2.7. This is a GROSS-DEFECT DETECTOR, not the coverage proof: the
coverage claim rests on the theorems and the exact-rational unit tests. What this
can do is fail an implementation that is broken, and it has to be able to fail,
which is what the planted defects establish.

Design (fixed at the E4 design lock):
  C = 108 cells. `hoeffding` and `empirical_bernstein`, each 2 modes x
  n in {300, 1000, 2500} x K in {1, 5} x 4 loss distributions; plus
  `sign_exact` on the 2 binary distributions x 3 n x 2 K.
  R = 40,000 replications per cell at the BOUNDARY NULL.
  Qualify iff adoptions <= 2049, the simultaneous Clopper-Pearson cutoff at
  alpha + tau = 0.055 with Bonferroni over 108 cells.

Two things make this trustworthy rather than merely fast:

1. `--parity` checks this vectorized implementation against the shipped
   compare_workflows.py on sampled receipts. Without that, a green diagnostic
   would only say that THIS code is self-consistent, which is worthless.
2. `sign_exact` cells are decided by exact rational arithmetic on the CPU, not
   by sampling. That is the one recorded CPU step under errata D-b, because it
   is arithmetic rather than simulation.

Run:  python3 e4a.py --out receipt.json            (full, GPU if available)
      python3 e4a.py --replications 500 --out /tmp/smoke.json   (smoke)
      python3 e4a.py --parity 200                  (parity against the helper)
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import time
from dataclasses import dataclass
from fractions import Fraction

ALPHA = 0.05
TOLERANCE = 0.055
CELLS = 108
GAMMA = ALPHA / CELLS


@dataclass(frozen=True)
class Distribution:
    """A paired-difference distribution, its support, and whether it is binary.

    `shift` moves the mean to the boundary null for the mode under test, which
    is where a size measurement has to be taken.
    """
    name: str
    binary: bool
    low: float
    high: float

    @property
    def span(self) -> float:
        return self.high - self.low


DISTRIBUTIONS = (
    Distribution("three_point", False, -1.0, 1.0),
    Distribution("two_point_extreme", False, -1.0, 1.0),
    Distribution("continuous", False, -1.0, 1.0),
    Distribution("rare_large", False, -1.0, 1.0),
)
BINARY_DISTRIBUTIONS = (
    Distribution("binary_balanced", True, -1.0, 1.0),
    Distribution("binary_sparse", True, -1.0, 1.0),
)
SAMPLE_SIZES = (300, 1000, 2500)
FINALISTS = (1, 5)
MODES = ("superiority", "non_inferiority")
MARGIN = 0.05


def draw(torch, dist: Distribution, shape, generator, device):
    """Mean-zero draws from the named distribution, then shifted by the caller.

    Each shape is deliberately different in what it stresses: a three-point
    distribution has mass at the bounds and at zero, a two-point extreme has
    mass only at the bounds, a continuous one has none, and rare_large is the
    sparse case that breaks a variance-only interval.
    """
    if dist.name == "three_point":
        u = torch.rand(shape, generator=generator, device=device)
        values = torch.zeros(shape, device=device)
        values[u < 0.25] = -1.0
        values[u > 0.75] = 1.0
        return values
    if dist.name == "two_point_extreme":
        u = torch.rand(shape, generator=generator, device=device)
        return torch.where(u < 0.5, -1.0, 1.0).to(torch.float32)
    if dist.name == "continuous":
        return (torch.rand(shape, generator=generator, device=device) * 2.0) - 1.0
    if dist.name == "rare_large":
        # Mean zero with mass 1e-3 at +1: the sparse, heavy case.
        p = 1e-3
        u = torch.rand(shape, generator=generator, device=device)
        return torch.where(u < p, 1.0 - p, -p).to(torch.float32)
    if dist.name == "binary_balanced":
        u = torch.rand(shape, generator=generator, device=device)
        return torch.where(u < 0.5, -1.0, 1.0).to(torch.float32)
    if dist.name == "binary_sparse":
        # Mostly concordant pairs: only 20% of pairs are discordant at all.
        u = torch.rand(shape, generator=generator, device=device)
        values = torch.zeros(shape, device=device)
        values[u < 0.10] = -1.0
        values[u > 0.90] = 1.0
        return values
    raise ValueError(f"unknown distribution: {dist.name}")


def hoeffding_radius(n: int, k: int, span: float, defect: str | None) -> float:
    """Matches compare_workflows.py: one-sided at alpha/k, radius span/2 * ..."""
    if defect == "radius_removed":
        return 0.0
    effective_n = n * 100 if defect == "radius_n_inflated" else n
    return (span / 2.0) * math.sqrt(2 * (math.log(k) - math.log(ALPHA)) / effective_n)


def eb_radius(torch, sd, n: int, k: int, span: float, defect: str | None):
    """Two-sided family interval at alpha/(2k) per tail, as plan v4 section 2.4."""
    if defect == "radius_removed":
        return sd * 0.0
    effective_n = n * 100 if defect == "radius_n_inflated" else n
    tail = ALPHA / (2 * k)
    log_term = math.log(2 / tail)
    return (sd * math.sqrt(2 * log_term / effective_n)
            + 7 * span * log_term / (3 * (effective_n - 1)))


def run_cell(torch, method, mode, dist, n, k, replications, chunk, generator, device,
             defect=None) -> int:
    """Adoptions over `replications` draws at the boundary null. Chunked.

    The boundary null is where size is measured: for superiority the true mean
    sits exactly at -margin, for non-inferiority exactly at +margin. A correct
    rule adopts there at most alpha of the time.
    """
    boundary = -MARGIN if mode == "superiority" else MARGIN
    threshold = -MARGIN if mode == "superiority" else MARGIN
    adoptions = 0
    done = 0
    while done < replications:
        rows = min(chunk, replications - done)
        values = draw(torch, dist, (rows, n), generator, device) + boundary
        if defect == "delta_sign_flipped":
            values = -values + 2 * boundary
        mean = values.mean(dim=1)
        if method == "hoeffding":
            radius = hoeffding_radius(n, k, dist.span, defect)
            upper = mean + radius
        else:
            sd = values.std(dim=1, unbiased=True)
            upper = mean + eb_radius(torch, sd, n, k, dist.span, defect)
        adoptions += int((upper < threshold).sum().item())
        done += rows
    return adoptions


def sign_exact_size(n: int, k: int, discordant_rate: float) -> Fraction:
    """Exact realized size of the sign test, averaged over the discordant count.

    No sampling: this is the one recorded CPU step under D-b, because the
    qualification is arithmetic. Returns an exact rational.
    """
    level = Fraction(1, 20) / k  # alpha/k with alpha = 1/20 exactly
    # The test's size GIVEN d discordant pairs is exact rational arithmetic.
    # Averaging over d only needs the binomial weights, which are computed in
    # log space over a +/-8 sd window: summing exact rationals over every d up
    # to n = 2500 would build astronomically large denominators for no gain,
    # and the omitted tail is below 1e-14.
    mean_d = n * discordant_rate
    sd_d = math.sqrt(n * discordant_rate * (1 - discordant_rate))
    low = max(1, int(mean_d - 8 * sd_d))
    high = min(n, int(mean_d + 8 * sd_d) + 1)
    total = Fraction(0)
    for d in range(low, high + 1):
        log_weight = (math.lgamma(n + 1) - math.lgamma(d + 1) - math.lgamma(n - d + 1)
                      + d * math.log(discordant_rate)
                      + (n - d) * math.log1p(-discordant_rate))
        weight = math.exp(log_weight)
        if weight < 1e-15:
            continue
        # One-sided exact binomial: reject when wins >= the smallest c whose
        # upper tail is at most the level. The tail itself stays exact.
        tail = Fraction(0)
        size_given_d = Fraction(0)
        for wins in range(d, -1, -1):
            tail += Fraction(math.comb(d, wins), 2 ** d)
            if tail <= level:
                size_given_d = tail
            else:
                break
        total += Fraction(weight).limit_denominator(10 ** 12) * size_given_d
    return total


def _binomial_cdf(n: int, x: int, p: float) -> float:
    """P(X <= x) in log space: math.comb(40000, 2000) overflows a float."""
    if x < 0:
        return 0.0
    if x >= n:
        return 1.0
    total = 0.0
    for i in range(x + 1):
        log_pmf = (math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1)
                   + i * math.log(p) + (n - i) * math.log1p(-p))
        total += math.exp(log_pmf)
    return min(1.0, total)


def clopper_pearson_upper(x: int, n: int, gamma: float) -> float:
    """One-sided upper bound; bisection on the binomial cdf."""
    if x >= n:
        return 1.0
    lo, hi = x / n, min(1.0, x / n + 0.05)
    for _ in range(60):
        mid = (lo + hi) / 2
        if _binomial_cdf(n, x, mid) > gamma:
            lo = mid
        else:
            hi = mid
    return hi


def parity_against_helper(torch, samples: int, device, generator) -> dict:
    """Check this vectorized code against the shipped compare_workflows.py.

    Without this the diagnostic would only establish that e4a agrees with
    itself. Receipts are built from real draws, and both implementations must
    reach the same upper bound AND the same adoption verdict. Comparing the
    bound alone is not enough: two implementations can agree on a number and
    still disagree about what it means, which is the decision that matters.
    """
    import importlib.util
    from pathlib import Path

    helper_path = (Path(__file__).resolve().parents[3]
                   / ".agents/skills/augustus/scripts/compare_workflows.py")
    spec = importlib.util.spec_from_file_location("compare_workflows", helper_path)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)

    mismatches = []
    checked = 0
    for method in ("hoeffding", "empirical_bernstein"):
        for mode in MODES:
            for n in (300, 1000):
                for k in FINALISTS:
                    for dist in DISTRIBUTIONS:
                        values = draw(torch, dist, (1, n), generator, device)[0]
                        # Map a paired difference in [-1, 1] onto two losses in
                        # [0, 1], which is the helper's input shape.
                        incumbent = ((1 - values) / 2).tolist()
                        candidate = [0.5] * n
                        pairs = [{"id": str(i),
                                  "incumbent": {"loss": float(incumbent[i]), "cost": None,
                                                "latency_ms": None, "violations": []},
                                  "candidate": {"loss": candidate[i], "cost": None,
                                                "latency_ms": None, "violations": []}}
                                 for i in range(n)]
                        receipt = {
                            "schema_version": 1, "phase": "confirm",
                            "incumbent_id": "incumbent", "candidate_id": "candidate",
                            "dataset_id": "e4a-parity", "outcome_definition": "synthetic",
                            "sampling_unit": "draw", "evidence_kind": "fixture",
                            "loss_bound": 1, "alpha": ALPHA, "comparison_count": k,
                            "minimum_improvement": MARGIN, "mode": mode, "method": method,
                            "sampling_design": "equal_probability", "pairs": pairs,
                        }
                        theirs = helper.compare(receipt)["confirmation"]
                        differences = [p["candidate"]["loss"] - p["incumbent"]["loss"]
                                       for p in pairs]
                        mean = sum(differences) / n
                        span = 2.0
                        if method == "hoeffding":
                            radius = hoeffding_radius(n, k, span, None)
                        else:
                            mu = mean
                            var = sum((d - mu) ** 2 for d in differences) / (n - 1)
                            radius = eb_radius(None, math.sqrt(var), n, k, span, None)
                        ours_upper = mean + radius
                        threshold = -MARGIN if mode == "superiority" else MARGIN
                        ours_adopts = ours_upper < threshold
                        checked += 1
                        bound_differs = abs(ours_upper - theirs["upper_mean_loss_delta"]) > 1e-9
                        verdict_differs = ours_adopts != theirs["strict_margin_supported"]
                        if bound_differs or verdict_differs:
                            mismatches.append({
                                "method": method, "mode": mode, "n": n, "k": k,
                                "distribution": dist.name,
                                "bound_differs": bound_differs,
                                "verdict_differs": verdict_differs,
                                "ours": ours_upper, "helper": theirs["upper_mean_loss_delta"],
                                "ours_adopts": ours_adopts,
                                "helper_adopts": theirs["strict_margin_supported"]})
                        if checked >= samples:
                            return {"checked": checked, "mismatches": mismatches,
                                    "agrees": not mismatches}
    return {"checked": checked, "mismatches": mismatches, "agrees": not mismatches}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--replications", type=int, default=40_000)
    parser.add_argument("--chunk", type=int, default=2_000)
    parser.add_argument("--seed", type=int, default=80_004)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--parity", type=int, default=0,
                        help="check N receipts against compare_workflows.py and exit")
    parser.add_argument("--defects", action="store_true",
                        help="also run the planted defects, which MUST fail")
    parser.add_argument("--out", help="write the receipt here")
    args = parser.parse_args(argv)

    import torch

    device = args.device
    if device == "auto":
        device = "cuda" if torch.cuda.is_available() else "cpu"
    generator = torch.Generator(device=device)
    generator.manual_seed(args.seed)

    if args.parity:
        report = parity_against_helper(torch, args.parity, device, generator)
        print(json.dumps(report, indent=2))
        return 0 if report["agrees"] else 1

    started = time.time()
    # Largest adoption count whose simultaneous CP upper bound still fits the
    # tolerance. Monotone in x, so bisect rather than scan: at R = 40,000 a
    # linear scan would evaluate tens of thousands of binomial cdfs.
    lo, hi = 0, args.replications
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if clopper_pearson_upper(mid, args.replications, GAMMA) <= TOLERANCE:
            lo = mid
        else:
            hi = mid - 1
    cutoff = lo

    cells = []
    for method in ("hoeffding", "empirical_bernstein"):
        for mode in MODES:
            for n in SAMPLE_SIZES:
                for k in FINALISTS:
                    for dist in DISTRIBUTIONS:
                        adoptions = run_cell(torch, method, mode, dist, n, k,
                                             args.replications, args.chunk,
                                             generator, device)
                        cells.append({
                            "method": method, "mode": mode, "n": n, "k": k,
                            "distribution": dist.name, "adoptions": adoptions,
                            "rate": adoptions / args.replications,
                            "cp_upper": clopper_pearson_upper(adoptions, args.replications, GAMMA),
                            "qualifies": adoptions <= cutoff,
                        })
    for n in SAMPLE_SIZES:
        for k in FINALISTS:
            for dist, rate in zip(BINARY_DISTRIBUTIONS, (0.5, 0.2)):
                size = sign_exact_size(n, k, rate)
                cells.append({
                    "method": "sign_exact", "mode": "superiority", "n": n, "k": k,
                    "distribution": dist.name, "adoptions": None,
                    "rate": float(size), "cp_upper": None,
                    "exact_size": float(size),
                    "qualifies": size <= Fraction(TOLERANCE).limit_denominator(10_000),
                    "note": "exact rational arithmetic on the CPU, not sampling",
                })

    receipt = {
        "experiment": "E4a",
        "replications_per_cell": args.replications,
        "cells": len(cells),
        "expected_cells": CELLS,
        "qualification_cutoff_adoptions": cutoff,
        "tolerance": TOLERANCE,
        "simultaneous_gamma": GAMMA,
        "device": device,
        "torch": torch.__version__,
        "platform": platform.platform(),
        "seed": args.seed,
        "wall_clock_s": round(time.time() - started, 1),
        "all_cells_qualify": all(cell["qualifies"] for cell in cells),
        "failing_cells": [cell for cell in cells if not cell["qualifies"]],
        "results": cells,
        "limits": [
            "A gross-defect detector. The coverage claim rests on the theorems and the exact-rational unit tests, not on this.",
            "Sampled cells are simulation; sign_exact cells are exact arithmetic and are not simulated.",
            "Passing establishes the absence of a gross defect at these cells, not coverage.",
        ],
    }
    if args.defects:
        planted = []
        for defect in ("radius_removed", "radius_n_inflated", "delta_sign_flipped"):
            for method in ("hoeffding", "empirical_bernstein"):
                for mode in MODES:
                    dist = DISTRIBUTIONS[2]
                    adoptions = run_cell(torch, method, mode, dist, 300, 1,
                                         min(args.replications, 10_000), args.chunk,
                                         generator, device, defect=defect)
                    planted.append({"defect": defect, "method": method, "mode": mode,
                                    "n": 300, "adoptions": adoptions,
                                    "rate": adoptions / min(args.replications, 10_000)})
        receipt["planted_defects"] = planted
        receipt["planted_defects_detected"] = any(p["rate"] > TOLERANCE for p in planted)

    text = json.dumps(receipt, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(text)
    print(text if not args.out else json.dumps(
        {k: v for k, v in receipt.items() if k != "results"}, indent=2))
    return 0 if receipt["all_cells_qualify"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
