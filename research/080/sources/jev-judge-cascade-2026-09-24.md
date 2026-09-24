# JEV-as-a-Judge: accept when confident, escalate when unsure — card (2026-09-24)

arXiv [2609.26550](https://arxiv.org/abs/2609.26550) v1, submitted 2026-09-22, CC BY 4.0. Li, Miao,
Krishnan, Padman (CMU). Read from the abstract and the HTML full text; nothing run. All numbers
are **Reported** by the authors.

**This is the closest external work to E1-S and E3 that the record contains, and it is careful in
exactly the way that makes it usable.** It separates pre-specified policies from post hoc ones,
reports where its own rule fails to transfer, and states what its human adjudication cannot claim.

## What it establishes

A decision-only judge (Jev) is compared against sixteen generative and reward-model judges, with a
642-item pilot **frozen before any inference** and split 40/60 by source question into a selection
set (thresholds and temperatures only) and a pilot test set.

- On ordinary preference and evidence-grounded factuality, Jev lands within three points of the
  strongest comparator at **0.36% of its fee** — about $0.04 per 1,000 judgments at 0.15 s.
- **The frozen cascade is the result to cite.** At τ = 0.9 to GPT-6, over 510 held-out extension
  pairs: accepts 53.7%, scores 92.5% against 93.1%, paired difference −0.59 points
  [−1.78, +0.59], at 56.8% of the fallback's fee. Thresholds were chosen on 96 pilot selection
  pairs to maximise coverage subject to staying within two points of the fallback, and invalid
  first-stage outputs always defer.
- The confidence signal carries real information rather than merely correlating with difficulty:
  escalating the same 34% at random reaches 88.1% where the cascade reaches 91.3% and a label-aware
  oracle 94.4%, so \(q\) captures about half the attainable gain.

## What it does not establish, in the authors' own words

- **The 99%-retention headline is post hoc.** The single-order cascades of §7 read their thresholds
  off the items they are scored on; only the frozen two-order policies test a pre-specified rule,
  and those are the −0.59-point result above, not the 99% one.
- **Threshold transfer fails.** The GPT-5.6 policy accepts 81.0% at τ = 0.7 and loses 2.35 points,
  beyond its own two-point tolerance; three τ = 0.5 policies collapse to order averaging with no
  fallback at all. On reference-free prose the AUROC is **0.518** — no threshold helps.
- **The gap is real where reasoning is required.** Human adjudication of JudgeBench disagreements
  goes 27–0 for GPT-6 on reasoning, 9–0 on coding, 7–0 on math; the adjudicated difference is
  −16.0 points [−20.0, −12.3], slightly worse than the label-based −14.6. The benchmark labels, if
  anything, understate the gap.
- **The human adjudication is one team member on 183 disagreement-selected items**, not a random
  audit; the intended second human pass was replaced by an LLM rater, recorded as a deviation; the
  adjudicator is an author; 36 of 183 labels are indecisive; and RewardBench preferences remain
  partly subjective at human–LLM κ = 0.29. Benchmark labels are unchanged in every primary result.
- Simulated cascade fees say nothing about live cascade latency, which the authors list as open.

## What it changes here

**It corroborates E1-S's direction from an independent group, and it sharpens P4 rather than
proving it.** Our own E1 result is that intercept-only recalibration removes 42% of a prior-shift
penalty; theirs is that a frozen confidence cascade retains almost all of a far more expensive
judge's accuracy at about half the fee. Both are statements that a cheap typed decision plus an
explicit uncertainty band beats committing to either extreme.

Three specific transfers into our own work:

1. **Their failure mode is the one to design against.** Threshold transfer failing across fallbacks,
   and AUROC 0.518 on reference-free prose, is direct evidence for the plan's requirement that a
   deferral threshold be validated locally rather than inherited. Cite it where we claim a
   confidence band is portable — because they showed it is not.
2. **Their frozen/post hoc split is the same control E1 used**, arrived at independently. Worth
   citing in §3 as prior art for the discipline, not only for the result.
3. **It is not an M5 arm and not a comparator.** We ran nothing; every figure here is theirs.

An honest caution for our own writing: this paper is favourable to the position, which is exactly
when a source needs the most scrutiny. The two numbers to quote are the frozen −0.59 points and the
0.518 AUROC, not the 99%.
