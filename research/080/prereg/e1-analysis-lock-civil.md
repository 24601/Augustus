# E1 analysis lock, civil

Derived from the fit report by `exp/e1_analysis_lock.py`, so it is a record rather than a
choice: the same fit report always yields this file. Written after fitting and calibration
and **before any confirmation row was read**.

- Family m = 19, α = 0.05, per-tail level 0.001316, power target 0.8
- Available confirmation rows: **1,367,024**
- Fitted temperature: 0.962589 (scalar, no intercept)
- Powered contrasts: **25 of 34**
- Powered held-out ratios: 1:19, 1:49, 4:1, S
- Powered held-out ratios with an equivalence contrast: 1:19, 1:49, 4:1
- Powered by mode: superiority 8, non_inferiority 6, equivalence 11

**Prespecified reading:** at least two held-out ratios have a powered equivalence contrast, so the Supports row is reachable.

| Ratio | Contrast | Held out | Mode | Margin | σ̂ | Span | Required n | Powered |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| 4:1 | A - B-stale | yes | superiority | 0.00031 | 0.0707 | 1.60 | 894 | yes |
| 4:1 | A - B-retrain_4:1 | yes | non_inferiority | 0.00031 | 0.0189 | 1.60 | 240,447 | yes |
| 4:1 | C - A | yes | equivalence | 0.00031 | 0.0389 | 1.60 | 573,958 | yes |
| 4:1 | C* - A | yes | equivalence | 0.00031 | 0.0776 | 1.60 | 1,805,553 | no |
| 4:1 | E - A | yes | equivalence | 0.00031 | 0.0240 | 1.60 | 307,436 | yes |
| 1:1 | A - B-stale | no | superiority | 0.00071 | 0.0000 | 1.00 | infeasible | no |
| 1:1 | A - B-retrain_1:1 | no | non_inferiority | 0.00071 | 0.0000 | 1.00 | infeasible | no |
| 1:1 | C - A | no | equivalence | 0.00071 | 0.0611 | 1.00 | 236,554 | yes |
| 1:1 | C* - A | no | equivalence | 0.00071 | 0.0289 | 1.00 | 83,823 | yes |
| 1:1 | E - A | no | equivalence | 0.00071 | 0.0775 | 1.00 | 354,068 | yes |
| 1:4 | A - B-stale | no | superiority | 0.00087 | 0.1314 | 1.60 | 1,178 | yes |
| 1:4 | A - B-retrain_1:4 | no | non_inferiority | 0.00087 | 0.0609 | 1.60 | 185,503 | yes |
| 1:4 | C - A | no | equivalence | 0.00087 | 0.1491 | 1.60 | 828,228 | yes |
| 1:4 | C* - A | no | equivalence | 0.00087 | 0.1294 | 1.60 | 638,451 | yes |
| 1:4 | E - A | no | equivalence | 0.00087 | 0.1128 | 1.60 | 499,640 | yes |
| 1:9 | A - B-stale | no | superiority | 0.00072 | 0.1837 | 1.80 | 1,569 | yes |
| 1:9 | A - B-retrain_1:9 | no | non_inferiority | 0.00072 | 0.0668 | 1.80 | 303,018 | yes |
| 1:9 | C - A | no | equivalence | 0.00072 | 0.1989 | 1.80 | 2,066,873 | no |
| 1:9 | C* - A | no | equivalence | 0.00072 | 0.1827 | 1.80 | 1,756,252 | no |
| 1:9 | E - A | no | equivalence | 0.00072 | 0.0728 | 1.80 | 345,412 | yes |
| 1:19 | A - B-stale | yes | superiority | 0.00052 | 0.2160 | 1.90 | 1,822 | yes |
| 1:19 | A - B-retrain_1:19 | yes | non_inferiority | 0.00052 | 0.0579 | 1.90 | 435,582 | yes |
| 1:19 | C - A | yes | equivalence | 0.00052 | 0.2333 | 1.90 | 5,319,662 | no |
| 1:19 | C* - A | yes | equivalence | 0.00052 | 0.2155 | 1.90 | 4,556,737 | no |
| 1:19 | E - A | yes | equivalence | 0.00052 | 0.0676 | 1.90 | 553,060 | yes |
| 1:49 | A - B-stale | yes | superiority | 0.00029 | 0.2368 | 1.96 | 1,985 | yes |
| 1:49 | A - B-retrain_1:49 | yes | non_inferiority | 0.00029 | 0.0381 | 1.96 | 667,553 | yes |
| 1:49 | C - A | yes | equivalence | 0.00029 | 0.2629 | 1.96 | 21,957,000 | no |
| 1:49 | C* - A | yes | equivalence | 0.00029 | 0.2370 | 1.96 | 17,884,332 | no |
| 1:49 | E - A | yes | equivalence | 0.00029 | 0.0537 | 1.96 | 1,126,107 | yes |
| S | A-recal - B-retrain_S | yes | non_inferiority | 0.00107 | 0.0764 | 1.80 | 185,858 | yes |
| S | A-raw - A-recal | yes | superiority | 0.00107 | 0.2114 | 1.80 | 4,513 | yes |
| S | C* - A-recal | yes | superiority | 0.00107 | 0.3615 | 1.80 | 606 | yes |
| S | E - A-recal | yes | superiority | 0.00107 | 0.2056 | 1.80 | 4,861 | yes |

## Limits

- required_n is a normal/fixed-SD planning approximation; the empirical Bernstein interval it plans for is distribution-free, this calculation is not.
- sigma-hat comes from the calibration split, which is not the confirmation split; the realized sd may differ and the interval, not this table, decides.
- A contrast with sigma-hat 0 is degenerate, not powered: at 1:1 the plug-in and the stale threshold are the same rule, so no n makes a claim about their difference.
- An unpowered contrast is still reported with its interval and counts toward no outcome row in either direction.
