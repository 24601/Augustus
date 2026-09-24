# E1 design lock

**Locked 2026-09-24**, operator-signed under the maintainer's standing authorization. Its
sha256 is recorded in `prereg/README.md`. **It was hashed before window W2 opened**, and W2 has never opened: no experiment dataset is on tabputer-1. Once hashed, the only permitted change is a
**prespecified** narrowing this lock already names.

| Field | Value |
| --- | --- |
| Written against | `plan-v4.md` at commit `4486733`; its sha256 is recorded at signing |
| Tests | X1 (cost heterogeneity), and claims P1, P2, P9 |
| Estimand | The superpopulation the corpus samples, at the declared independent unit: **one comment**. The exact finite-population Δ over the confirmation partition is reported beside every interval |
| Eligibility limit | The instrument is a frozen encoder plus a head we fit, so benchmark contamination is bounded here. It is not eliminated, and §2.4 item 4 applies |

## Data and partitions

**Primary: CivilComments** (CC0, toxicity ≥ 0.5, about 2.0M rows [C, recheck at M2 from the
dataset card only, never from rows]). Exact-normalized-text dedup across partitions, verified by
the overlap audit before any fit.

| Partition | Size | Use |
| --- | --- | --- |
| fit | 200,000 | Fit the head |
| fit-B | 200,000 | A second, disjoint fit sample; the A-vs-A-on-fit-B comparison is an **outcome**, reported as fit variance, not a control |
| calibration | 100,000 | Temperature, thresholds, σ̂ |
| M5 pool | 100,000 | Disjoint, reserved for M5's T2c |
| confirmation | about 1,400,000 planned; **1,367,024 actual** after 32,490 exact duplicates were removed (M4 receipt, 2026-09-24). Every planning n still fits | Read once, after the analysis lock |

**Secondary: CLINC150** (CC-BY-3.0, human-written, 23,850 actual): fit 8,000, calibration 3,000,
confirmation **12,845** actual after 5 exact duplicates were removed. Its OOS class is id 42,
identified from the shards' own ClassLabel names. Its decision is **route-or-abstain against the OOS class**: s(x) = 1 − P(OOS);
an FP routes an OOS query to an intent handler, an FN abstains on an in-scope query. The same cost
ratios and plug-in rule apply. At 12,850 rows CLINC powers **no** equivalence contrast, so it
contributes superiority rows only.

Seeds: partitioning seed 80_101, resampling seed 80_102, control-redraw seed 80_103. Splits are
hashed by `augstage` at publication and the hashes go in the analysis lock.

## Arms

Calibration for the no-shift arms is **temperature only, with no intercept**, so B-stale is exactly
the plug-in frozen at 0.5 on the same scores.

A (plug-in threshold), A_tuned (descriptive only), A-raw and A-recal (under shift S), B-stale,
B-retrain_r, B-retrain_S, and C, C\*, E (learned implementations with c as an input). Definitions
are in plan v4 §2.2 and are incorporated here by reference; the arm hashes go in the analysis lock.

## Costs, margins and bounds

- C_FP + C_FN = 1. Training range {1:1, 1:4, 1:9}; **held out** {1:19, 1:49, 4:1}.
- Shift S: ratio 1:9, confirmation resampled to 3× the fit prior (about 0.24), capped at 0.5.
- **Margin** δ_r = 0.02 × the calibration-split cost of A at ratio r. Under S, 2% of A-recal's
  calibration cost at the S prior. Fixed here, never moved.
- **Loss bound** per ratio: a per-case cost is in {0, C_FP, C_FN}, so the paired difference has
  range R_r = 2·max(C_FP, C_FN): 1.60 at 4:1, 1.00 at 1:1, 1.60 at 1:4, 1.80 at 1:9, 1.90 at 1:19,
  1.96 at 1:49.

## Family, method and power

- m = 19 per dataset. At each held-out ratio: A−B-stale, A−B-retrain_r, C−A, C\*−A, E−A (15).
  Under S: A-recal−B-retrain_S, A-raw−A-recal, C\*−A-recal, E−A-recal (4).
- Method: **empirical Bernstein**, two-sided at α/(2m) per tail. Normal-theory intervals may be
  reported as `descriptive_only`.
- **Direction per contrast, fixed here**: A−B-stale is `sup_ucb` (A is expected better, so Δ is
  negative and the read is on the upper bound). C−A, C\*−A and E−A are equivalence. A−B-retrain_r
  is non-inferiority. The escalation-shaped reads under S are `sup_ucb` on A-recal.
- **Planning effects (`true_delta`), fixed here**, from the synthetic population [H, `calc_v4.py`
  §2]: A−B-stale at −0.042 (1:19). Equivalence contrasts plan at `true_delta = 0`.
- Planning n [Rep, `calc_v4.py` §2]: equivalence of C\* to A needs 78k (1:1) to 401k (1:49) at
  τ = 0.1, and 159k to 688k at τ = 0.3 — all inside 1.4M. Superiority of A over B-stale needs
  1,425 (1:49) to 18,754 (4:1).
- **Powered set**: a contrast is powered iff its computed n at the analysis-lock σ̂ fits the
  available n. No σ̂ figure quoted in prose decides anything.

## Monotonicity

For each case the action switches **at most once**, abstain → act, as C_FN/C_FP increases along
4:1, 1:1, 1:4, 1:9, 1:19, 1:49. Violations are counted per arm and reported.

## Outcome rows, all prespecified

| Row | Condition |
| --- | --- |
| **Rejects X1 on this task** | B-stale equivalent to A at every powered held-out ratio; **or** B-retrain_r superior to A beyond δ_r at a powered ratio; **or** B-retrain_S superior to A-recal beyond δ |
| **Narrows: ownership** | C\* or E equivalent to A at every powered held-out ratio and to A-recal under S, with zero monotonicity violations. The claim then rests on c being an input, not on a closed form |
| **Narrows: implementation** | B-stale superior to A at a powered ratio means the calibrated plug-in failed. X1 is then unsupported on this task until calibration is repaired |
| **Supports** | At least 2 of the 3 held-out ratios powered; A superior to B-stale by δ_r and non-inferior to B-retrain_r at every powered ratio; and, if S is powered, A-recal non-inferior to B-retrain_S with no more labels |
| **Inconclusive** | Fewer than 2 powered held-out ratios, or none of the above |

## Controls, which test machinery only

- An identical frozen A through the full pipeline: Δ ≡ 0 on every case. Any deviation is a
  pipeline fault, not a result.
- Semi-synthetic: on a copy of confirmation, draw y\* ~ Bernoulli(s_i) from A's calibrated scores,
  so each threshold policy's expected cost is analytic. Plant (a) two analytically equal-cost
  thresholds, (b) Δ = 1.5δ_r, (c) Δ = δ_r. Over 200 redraws the pipeline must claim equivalence in
  (a) at about its planned power, inferiority in (b), and false equivalence in (c) at most at the
  α/m rate, judged by a binomial CI.

## Compute

MiniLM embedding of about 2.1M texts; measured at 2.1 s per 1,000 texts on GPU at M0 [Rep], so
roughly 75 minutes. GPU budget **8 GiB**, aggregate admission 38 GiB. The 2 GiB first written here was a planning
guess that a forward pass disputed: MiniLM at batch 256 and length 256 exceeded it immediately.
Amended 2026-09-24, before any confirmation row was read; no margin, size or contrast changed. Cap 6 hours. E1 needs no
generative model and no teacher.

## What would make E1 fail as an experiment

A failed machinery control; an overlap-audit leak; a split-hash drift; or a confirmation read
without a matching analysis-lock hash. Any of those invalidates the run, and the honest response
is to say so and re-run, not to amend the lock.
