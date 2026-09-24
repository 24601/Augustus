# E3 analysis lock

Derived from the sigma report by `exp/e3_analysis_lock.py`, so it is a record rather than
a choice. Written after the search split and **before any confirmation row was read**.

- Family m = 3 (unnarrowed 6), α = 0.05, per-tail level 0.008333, power target 0.8
- Available confirmation questions: **6,405**
- Powered contrasts: **2 of 3**
- Equivalence readings: **inconclusive, prespecified** (boundary σ̂ ≤ 0.26502213)
- Realized rerun joint disagreement: **1.0**

## The prespecified narrowing

- Applied: **yes**; triggered by σ̂ yes, by timing no (5.7 of 24.0 GPU-h)
- Worst σ̂ before 0.4624, after 0.4004, boundary 0.24368057
- Dropped reader: **Qwen3-4B**
- Did it restore the equivalence readings: **no**

Applied as written. Dropping a reader lowers m and so widens nothing except through the tail level; it buys power only when sigma-hat sits near the boundary. Here it did not, and the equivalence readings are inconclusive anyway. Applying a narrowing only when its consequence is convenient would make it a post-hoc decision, so it is applied and the cost is recorded.

| Reader | Contrast | Margin | σ̂ | Search mean | Required n | Powered |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Qwen3-1.7B | best explicit - implicit | 0.020 | 0.3818 | +0.0967 | 1,080 | yes |
| Qwen3-1.7B | best explicit - best constant | 0.020 | 0.1980 | +0.0134 | infeasible | no |
| Qwen3-1.7B | (vii) outcome - (vi) proxy | 0.020 | 0.4004 | +0.0600 | 3,072 | yes |

## Limits

- required_n is a normal/fixed-SD planning approximation; the empirical Bernstein interval it plans for is distribution-free, this calculation is not.
- The planning effect is the search-split mean, not an independently registered number. A search mean is an estimate, and an optimistic one for the arm that was selected on that split.
- sigma-hat comes from search, which is not confirmation; the realized sd may differ and the interval, not this table, decides.
- The determinism check failed at 100% joint per-question disagreement, so the replay tables are the sole source and this rate travels with every E3 result.
- Arms that threshold p_answerable carry a rerun instability measured at up to 2.4x the margin. That bounds transportability to a regenerated table, not the internal comparison, which is exact because the table is frozen.
