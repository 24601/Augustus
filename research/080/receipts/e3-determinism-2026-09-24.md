# E3 determinism check: FAILED, and the consequence applies (2026-09-24)

Operator: an Amp thread on the runner `tabputer`, thread `T-01a0d413-fff9-768a-b321-6ae4730772cc`.
Run as `augexp` in the hardened profile, offline, reader `Qwen3-1.7B` at
`70d244cc86ccca08cf5af4e1e306ecf908b1ad5e`, BF16, non-thinking, greedy, `enforce_eager`,
`gpu_memory_utilization` 0.11.

**Verdict: the realized joint per-question disagreement is 100%, against a pre-registered
tolerance of 5%. The check fails.** The design lock's stated consequence applies without
amendment: the frozen replay tables become the sole source for every arm, resplit and P6 draw, and
the realized rate is reported beside every E3 result. **The check was run once. It was not
re-run, retried or tuned, and this verdict is final.**

| Item | Value |
| --- | --- |
| Source | `exp/e3_replay.py` at [`c17a878`](https://github.com/24601/Augustus/commit/c17a878), sha256 `70e24def…` |
| Questions | the 50 prespecified timing-pilot ids from the seeded search split |
| Calls | 900, two passes in one process |
| Table | `/srv/aug/receipts/e3-rerun-20260924T2040Z/e3-rerun-check-1.7b.json`, 55,221 bytes, sha256 `332710c7…` |
| Wall clock | 77.7 s |

## The realized rates

| Field | Exact identity across the two passes |
| --- | --- |
| `answer` text | **98.7%** (148 / 150) |
| `action` (stop / expand / abstain) | **96.0%** (144 / 150) |
| `p_answerable` (exact float) | **0.7%** (1 / 150) |
| Per call, pooled | 65.1% |
| **Per question, joint over all nine comparisons** | **0.0%** (0 / 50) |

## What this does and does not say

The joint failure is driven almost entirely by one field. **Exact float equality of a softmax
output across two batched GPU passes is close to impossible**, because the reduction order inside a
batch is not fixed; 1 of 150 matching is what that looks like. The two fields that are decisions
rather than floats — the answer string and the chosen action — reproduced at 98.7% and 96.0%.

That does not rescue the check, and the check is not being rescued. The comparison was defined
before the run, the tolerance was pre-registered, and the result stands as recorded. What it does
mean is that the *reason* for the failure should be stated precisely rather than left as "the
readers are nondeterministic":

- **The decisions are largely stable**; the exact probabilities are not bitwise stable.
- Arms (ii) and (iv) threshold `p_answerable`. Whether that instability matters to them depends on
  the **magnitude** of the wobble and on whether it crosses a threshold, and the first run measured
  exact identity only. The runner flagged exactly this: an exact-identity failure is not a
  measurement of numerical magnitude.
- The program now reports, beside exact identity and never instead of it, the distribution of
  |Δp| and the number of rerun threshold crossings at 0.1 through 0.9 — a crossing being a rerun
  that would have changed an arm's action. That is a diagnostic for a recorded failure, not a
  second and gentler test of it.

## Consequences carried forward

1. Every E3 result reports this realized rate beside it. Not a footnote.
2. The replay tables are generated once and frozen. No claim may depend on re-execution, which is
   what the lock already required and what this measurement now justifies rather than assumes.
3. The lock's `0.598⁹ ≈ 0.0098` figure was marked **[H]** because it assumes independence across
   calls. The measured joint identity is 0.0%, and the measured per-field identities are 0.987,
   0.960 and 0.007. Their product is 0.0064, which is close to the observed 0 only because one
   factor is near zero; **independence is neither confirmed nor needed** — the joint rate was
   measured directly, which is why the check exists.

## Timing, which passes comfortably

900 calls in 77.7 s scales to 133,290 calls at **3.20 GPU-h**, or 3.37 GPU-h if the 82 s outer
process time is scaled instead. The cap is 24 GPU-h, so this is 13% of it with about 7.5× headroom.
The prespecified narrowing that drops the 4B reader is therefore **not triggered by timing**. This
is a 1.7B extrapolation that includes model load and the MiniLM pass, not a decode-only figure, and
the 4B reader has not been timed.

## Limits

- One reader, one pass pair, 50 questions. The rate is measured, not bounded.
- `answer` identity is exact string identity, so two answers that would score the same EM count as
  a disagreement. That is the conservative direction.
- Nothing here says the readers are wrong, only that they are not reproducible at the bit level
  under batched decode, which is why the tables are frozen.

## Second run: the magnitude diagnostic, and what it costs E3

The same 50 ids, the same defaults, the program at [`df62963`](https://github.com/24601/Augustus/commit/df62963).
**This run diagnoses the recorded failure; it does not retest it.** Its own identity numbers came
out essentially the same — answer 149/150, action 144/150, `p_answerable` 1/150, joint 0/50 — which
is itself worth noting: the failure reproduces.

Table `/srv/aug/receipts/e3-diagnostic-20260924T204912Z/e3-diagnostic-1.7b.json`, 55,567 bytes,
sha256 `a5a5a792…`. Wall clock 80.0 s.

| |Δp| across 150 comparisons | Value |
| --- | --- |
| median | 5.61 × 10⁻⁷ |
| p99 | **0.1085** |
| max | **0.1244** |

| Rerun threshold crossings | 0.1 | 0.3 | 0.5 | 0.7 | 0.9 |
| --- | ---: | ---: | ---: | ---: | ---: |
| count of 150 | 0 | **2** | 1 | 1 | 0 |

**The distribution is not the story; the tail is.** Half the probabilities agree to six decimal
places, which is the floating-point noise anyone would predict. But the p99 is 0.109 and the
maximum is 0.124, so on roughly one call in a hundred the two passes disagree about answerability
by more than a tenth. Those are the cases where the reader is close to tied between yes and no and
the batch reduction order decides, and they are exactly the cases a threshold is sensitive to.

**Computed here, and corrected after the runner caught an error in my first arithmetic.** The
denominator 150 counts (question, k) **cells**, not questions. An arm spends one k per question —
whichever level its policy stops at — so the quantity that moves an arm's mean utility is the
per-**question** flip rate, and dividing by 150 understated it threefold.

| Reading of the 2 crossings at τ = 0.3 | Per-question rate | Worst-case shift in mean utility | Against the 0.02 margin |
| --- | ---: | ---: | ---: |
| Cell-level fraction (**not** a bound on an arm) | 2/150 = 1.33% | 0.016 | 0.8× |
| Both cells in **one** question | 1/50 = 2% | **0.024** | **1.2×** |
| Cells in **two distinct** questions | 2/50 = 4% | **0.048** | **2.4×** |

The diagnostic did not record which questions the crossing cells belong to, and the second table
was not retained, so the conservative reading is the operative one: **up to 0.048, which is 2.4
times the margin.** The realistic figure is lower, because a flipped action only changes utility
when it changes the answer that gets scored, and the diagnostic cannot say how often that happens.
But "lower for a reason we did not measure" is not a bound, and the bound is what goes in the lock.

My earlier figure of 0.016 stands only as a cell-level calculation. It is **not** a demonstrated
bound on mean per-question policy utility, and the correction makes the finding worse rather than
better: the rerun instability of the two answerability arms **exceeds** the margin they are tested
against, rather than sitting at 0.8 of it.

This does not invalidate E3, and it is precisely why the lock freezes the tables: every arm,
resplit and P6 draw reads one table, so the comparison between arms is exact and reproducible from
the artifact. What it bounds is something narrower and worth saying plainly: **a replication that
regenerated the tables could differ from this one, on the two answerability arms, by more than the
margin.** That belongs beside those two rows in the analysis lock, not in a footnote,
and it is a limit on E3's transportability rather than on its internal validity.

Arms (i), (iii), (v), (vi) and (vii) do not threshold `p_answerable`. Arm (i) reads the action,
which reproduced at 96%; arm (iii) reads a MiniLM cosine over frozen text, which is deterministic
at fixed batch composition.

### Caveats the runner attached, kept

- The grid is five thresholds, not every tenth from 0.1 to 0.9, so the crossing profile between
  them is unmeasured.
- Counts at different thresholds need not be distinct rows.
- One reader, 50 questions, one pass pair. The 4B reader remains untimed and untested for rerun
  behaviour, and nothing here extrapolates to it.
