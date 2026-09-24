# E3 design lock

Written against `plan-v4.md` at commit `0547e27`. Tests X5, P5 and P6. **Strongly recommended, not
required**: if the timing pilot or σ̂ makes it inconclusive, that is a reported outcome, and E3
does not gate the release.

| Field | Value |
| --- | --- |
| Population | HotpotQA distractor validation, CC-BY-SA-4.0, 7,405 hard questions [C, recheck at M2 from the dataset card only]. The train split mixes difficulty levels and is excluded |
| Estimand | The superpopulation of questions the benchmark samples, **not** the enumerated 7,405. The exact finite-population Δ is reported beside every interval. **HotpotQA is public and the readers are pretrained**, so the superpopulation reading carries the §2.4 item 4 contamination limit explicitly; the finite-population Δ does not |
| Utility | U = EM − λ·rounds/3 − μ·tokens/1000, **clipped to [−0.2, 1]**. λ = 0.1 primary. μ = 0.0 (fixed here; token cost is reported descriptively rather than priced into the utility, because a price would need a defensible exchange rate we do not have) |
| **Loss bound** | Two utilities in an interval of width 1.2 differ by up to ±1.2, so the paired difference has range **R = 2.4**. This is the value the v4 reviews corrected; it is not 1.2 |
| Identification | Full-information replay: every answer at every k, so X5b holds by construction. This is the reason E3 can speak about selection at all, and it is also why E3 is not a claim about live agents |

## Readers and determinism

Qwen3-1.7B and Qwen3-4B at pinned revisions, BF16, non-thinking, greedy, served by the image's
vLLM. **Revisions recorded 2026-09-24**, filling the slot this lock left open rather than changing
a commitment: `Qwen/Qwen3-1.7B` at `70d244cc86ccca08cf5af4e1e306ecf908b1ad5e` and `Qwen/Qwen3-4B`
at `1cfa9a7208912126459214e8b04321603b3df60c`, both `torch_dtype: bfloat16`, both staged
root-owned and read-only to `augexp` with per-file hashes in their `MANIFEST.json`. The 4B weights
were absent when E3 began and were acquired in a bounded window; **the prespecified narrowing was
not used to drop that reader**, because it is conditioned on the timing pilot or on σ̂, and using
it for a missing download would launder an operational gap into a statistical decision.

**Replay tables are generated once and frozen**, and every arm, every resplit and every P6
draw reads the same tables, so no claim depends on re-execution.

M0 measured **59.8% per-prompt** batched-rerun identity [Rep]. The 0.598⁹ ≈ 0.0098 figure for a
whole 9-call question assumes independence across calls and is **[H]**, not a measured joint law.
Before confirmation, a 50-question check measures the realized rerun disagreement rate against a
**pre-registered tolerance of 5%**; exceeding it means the frozen tables are used as the sole
source and the realized rate is reported beside every result.

## Arms and family

Arms: (i) implicit prompt; (ii) threshold on LLM answerability; (iii) threshold on dense
similarity; (iv) composite; (v) constants; (vi) proxy-selected threshold; (vii) outcome-selected
threshold. The best explicit arm is chosen on the search set and frozen.

**m = 6.** Per reader at λ = 0.1: best explicit − implicit; best explicit − best constant;
(vii) − (vi).

| Contrast | Mode and direction | `true_delta` |
| --- | --- | --- |
| best explicit − implicit | `sup_ucb` (explicit expected better) | −0.04 |
| best explicit − best constant | `sup_ucb` | −0.04 |
| (vii) − (vi) | `sup_ucb` | −0.04 |
| The same three, read as equivalence when superiority fails | equivalence at `true_delta = 0` | 0 |

Margin **0.02 utility**, about 2 EM points, for superiority and equivalence alike. Method:
empirical Bernstein, two-sided at α/(2m) per tail.

## n, and what is reachable [Rep, `calc_v4.py` §3]

Search 1,000 questions, including a 100-question σ pilot and a 50-question timing pilot.
Confirmation is the remaining **6,405**.

| σ̂ | n needed, m = 6 | n needed, m = 3 |
| --- | --- | --- |
| 0.20 | 5,181 | 4,675 |
| 0.25 | 6,598 | 5,971 |
| 0.30 | 8,271 | 7,501 |

So the equivalence rows are powered at m = 6 only if σ̂ ≤ **0.24368057**, and at m = 3 only if
σ̂ ≤ **0.26502213**. These are computed boundaries; the rule is n(σ̂) ≤ available, never a rounded
figure. A true 0.04 gain is a **gap of 0.02** beyond the margin and needs 7,318 (m = 6) or 6,592
(m = 3) at σ = 0.30. These are normal/fixed-SD planning approximations: the acceptance interval is
distribution-free, the power calculation is not.

**Prespecified narrowing**: if the timing pilot projects past the cap, or σ̂ > 0.24368057, drop the
4B reader before any confirmation read (m = 3). If σ̂ > 0.26502213 even then, the equivalence rows
are declared **inconclusive before confirmation**; the superiority rows still run. The margin never
changes and the population is never enlarged after an outcome is seen.

## Calls and compute

9 calls per question per reader. **Full replay of all 7,405 is the planned workload**: 133,290
calls for two readers, 66,645 under the narrowing. At the measured 2,004 tok/s batched and 64
output tokens per call that is 1.2 and 0.6 GPU-h of decode [Rep]; prefill and the timing pilot
govern the real figure. Cap **24 GPU-h**. GPU budget 14 GiB, aggregate admission 44 GiB.

**P6's finite population is the 6,405 confirmation questions**, which the search set never touched:
115,290 of those calls for two readers. That truth is held by `augctl` and is never exposed to
selection.

## Outcome rows

| Claim | Supported | Rejected | Otherwise |
| --- | --- | --- | --- |
| Explicit vs implicit | The best explicit arm is superior by 0.02 for every powered reader | The two are equivalent for every powered reader | Inconclusive |
| Policy vs constants | Same, against the best constant | Same | Inconclusive |
| P5 (episode vs proxy selection) | (vii) superior to (vi) | Equivalence | Inconclusive |
| P6 (false adoption) | Over 200 resplits, incumbent–challenger is lower than adopt-best with the 95% CI of the difference excluding 0 | — | Not supported |

## Controls

An identical frozen incumbent against its own copy: Δ ≡ 0, never adopted. A planted +0.05 utility
shift on a replay copy must be adopted at its planned power. The per-question oracle is reported as
headroom, never used as a control.
