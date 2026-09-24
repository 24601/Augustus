# E1 analysis lock, clinc

Derived from the fit report by `exp/e1_analysis_lock.py`, so it is a record rather than a
choice: the same fit report always yields this file. Written after fitting and calibration
and **before any confirmation row was read**.

- Family m = 19, α = 0.05, per-tail level 0.001316, power target 0.8
- Available confirmation rows: **12,845**
- Fitted temperature: 0.919470 (scalar, no intercept)
- Powered contrasts: **7 of 34**
- Powered held-out ratios: 1:19, 1:49, 4:1, S
- Powered held-out ratios with an equivalence contrast: none
- Powered by mode: superiority 7, non_inferiority 0, equivalence 0

**Prespecified reading:** fewer than two held-out ratios have a powered equivalence contrast, so the prespecified INCONCLUSIVE row applies to the equivalence claims before confirmation is read.

| Ratio | Contrast | Held out | Mode | Margin | σ̂ | Span | Required n | Powered |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| 4:1 | A - B-stale | yes | superiority | 0.00017 | 0.0629 | 1.60 | 861 | yes |
| 4:1 | A - B-retrain_4:1 | yes | non_inferiority | 0.00017 | 0.0350 | 1.60 | 1,344,236 | no |
| 4:1 | C - A | yes | equivalence | 0.00017 | 0.0765 | 1.60 | 5,313,847 | no |
| 4:1 | C* - A | yes | equivalence | 0.00017 | 0.0560 | 1.60 | 2,984,745 | no |
| 4:1 | E - A | yes | equivalence | 0.00017 | 0.0369 | 1.60 | 1,458,706 | no |
| 1:1 | A - B-stale | no | superiority | 0.00037 | 0.0000 | 1.00 | infeasible | no |
| 1:1 | A - B-retrain_1:1 | no | non_inferiority | 0.00037 | 0.0000 | 1.00 | infeasible | no |
| 1:1 | C - A | no | equivalence | 0.00037 | 0.0729 | 1.00 | 1,105,309 | no |
| 1:1 | C* - A | no | equivalence | 0.00037 | 0.0316 | 1.00 | 275,069 | no |
| 1:1 | E - A | no | equivalence | 0.00037 | 0.0639 | 1.00 | 868,465 | no |
| 1:4 | A - B-stale | no | superiority | 0.00041 | 0.0852 | 1.60 | 954 | yes |
| 1:4 | A - B-retrain_1:4 | no | non_inferiority | 0.00041 | 0.0565 | 1.60 | 623,002 | no |
| 1:4 | C - A | no | equivalence | 0.00041 | 0.0809 | 1.60 | 1,149,289 | no |
| 1:4 | C* - A | no | equivalence | 0.00041 | 0.0760 | 1.60 | 1,029,765 | no |
| 1:4 | E - A | no | equivalence | 0.00041 | 0.0723 | 1.60 | 943,215 | no |
| 1:9 | A - B-stale | no | superiority | 0.00036 | 0.1168 | 1.80 | 1,193 | yes |
| 1:9 | A - B-retrain_1:9 | no | non_inferiority | 0.00036 | 0.0703 | 1.80 | 1,147,112 | no |
| 1:9 | C - A | no | equivalence | 0.00036 | 0.0943 | 1.80 | 1,937,166 | no |
| 1:9 | C* - A | no | equivalence | 0.00036 | 0.1049 | 1.80 | 2,357,636 | no |
| 1:9 | E - A | no | equivalence | 0.00036 | 0.0626 | 1.80 | 944,196 | no |
| 1:19 | A - B-stale | yes | superiority | 0.00029 | 0.1345 | 1.90 | 1,329 | yes |
| 1:19 | A - B-retrain_1:19 | yes | non_inferiority | 0.00029 | 0.0614 | 1.90 | 1,364,735 | no |
| 1:19 | C - A | yes | equivalence | 0.00029 | 0.1064 | 1.90 | 3,676,896 | no |
| 1:19 | C* - A | yes | equivalence | 0.00029 | 0.1219 | 1.90 | 4,759,970 | no |
| 1:19 | E - A | yes | equivalence | 0.00029 | 0.0681 | 1.90 | 1,633,371 | no |
| 1:49 | A - B-stale | yes | superiority | 0.00022 | 0.1467 | 1.96 | 1,421 | yes |
| 1:49 | A - B-retrain_1:49 | yes | non_inferiority | 0.00022 | 0.0597 | 1.96 | 2,141,628 | no |
| 1:49 | C - A | yes | equivalence | 0.00022 | 0.1158 | 1.96 | 7,262,062 | no |
| 1:49 | C* - A | yes | equivalence | 0.00022 | 0.1346 | 1.96 | 9,709,345 | no |
| 1:49 | E - A | yes | equivalence | 0.00022 | 0.0599 | 1.96 | 2,153,600 | no |
| S | A-recal - B-retrain_S | yes | non_inferiority | 0.00073 | 0.1042 | 1.80 | 617,296 | no |
| S | A-raw - A-recal | yes | superiority | 0.00073 | 0.1372 | 1.80 | 14,678 | no |
| S | C* - A-recal | yes | superiority | 0.00073 | 0.2278 | 1.80 | 1,872 | yes |
| S | E - A-recal | yes | superiority | 0.00073 | 0.1603 | 1.80 | 6,893 | yes |

## Limits

- required_n is a normal/fixed-SD planning approximation; the empirical Bernstein interval it plans for is distribution-free, this calculation is not.
- sigma-hat comes from the calibration split, which is not the confirmation split; the realized sd may differ and the interval, not this table, decides.
- A contrast with sigma-hat 0 is degenerate, not powered: at 1:1 the plug-in and the stale threshold are the same rule, so no n makes a claim about their difference.
- An unpowered contrast is still reported with its interval and counts toward no outcome row in either direction.
