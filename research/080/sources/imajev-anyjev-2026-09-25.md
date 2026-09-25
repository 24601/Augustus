# imajev and AnyJev — card (2026-09-25)

Two Jev-shaped projects sighted the same day, read through the Librarian at file and commit level.
Nothing downloaded or run. **Neither calls TypeSafe's hosted API**: searches for `typesafe`,
`api.typesafe` and `jev-latest` are empty in both trees, imajev's `jev_api.py` is a local request
translator, and AnyJev's only HTTP client is a local vLLM server. Both copy the
Choice / Score / Noul contract from the outside.

They fail as comparators for opposite reasons, and the contrast is the useful part.

## imajev — `mohit67890/imajev`

A local vision-language decision model: up to two photos plus record text plus typed questions in,
probabilities out, with a trained `unknown`. LoRA r16/α32 on Qwen3.5 language layers plus a 255-code
linear readout, vision tower frozen; shipped weights are a 50/50 average of two adapters. Apache-2.0,
single author, **16 commits, created 2026-09-23** — the public history is a two-day export, not the
training history.

**Its provenance discipline is unusually good and its scoreboard is unusable.** The training
mixture is documented down to 36 named public sources and ~504k stage-1 decisions, every teacher is
named and open-weight, and the repo claims an 8-gram contamination lint against JevBench. Then:

> "The ImajevBench test split was also an input to choosing the shipped checkpoints (the release
> gates), so its numbers are not pure held-out estimates"

The 82.4% headline is on a benchmark the author wrote, whose 458 images are entirely AI-generated,
whose audit of 138 items was done by two models rather than people, and whose own datasheet says
"until then, imajev results on this benchmark are self-reported." The v2 preregistration is still
`Status: draft`. Internal numbers already disagree — README 82.1% against the leaderboard's 82.8%
for the same 9B, two different Unknown counts, two different ECE pairs — so the README is a
rewritten summary, not the ledger.

**The most valuable thing in the repo is a finding against itself.**
`results/benchmarks/decisionbench/contamination-check.md` reports that 1,030 of 1,145 RouteFinancial
rows share a BANKING77 training utterance and intent label with its own stage-1 data, and the author
writes that "RouteFinancial should be read as contaminated." That is the contamination gate the
`decider` card made us write, found and published by a competitor against his own headline.

**Its mixture overlaps all three M5 corpora**: `civil_comments`, `banking77` and CLINC are the
sources T2a, T2b and T2c are built from. That is the same situation as `decider`, and it is worth
saying precisely what it does and does not rule out, because "contaminated" is not a synonym for
"not allowed".

What it rules out is **one claim**: an imajev score on T2a–c is not a held-out score, and no seeded
partition of ours repairs that, because the leak is upstream of our partitioner. It cannot be
evidence about generalization to the superpopulation those corpora sample.

What it does not rule out is running it. A declared-contaminated reference row — scored by us, on
our confirmation partition, labelled as contaminated in the table — answers a question we otherwise
cannot answer: what an off-the-shelf trained decision model gets on these exact rows. Our own E1
and E3 already carry that kind of qualification rather than dropping the arm, since the readers
there are pretrained on public text too. The honest treatment is a row with a stated limit, not an
absence.

This is not a §3.6 matter and citing that section for it would be wrong. §3.6 is the
provider-provenance gate: licences, lineage, named teachers, and Jev output never becoming training
data. Nothing about imajev's public-corpus overlap engages it. The relevant limit is the
eligibility note on the estimand — the same one E3 carries for HotpotQA and pretrained readers.

## AnyJev — `nokia-applied-research/AnyJev`

A library that reads typed decisions off an already-running open causal LLM in one prefill: "Nothing
is generated and nothing is parsed." Four levels — `raw` restricted softmax; `L0` cyclic option
shifts plus a label prior, **zero labels**; `L1` temperature from 100–500 labels; `L2` a shrunk
LDA/ridge head on a mid-depth hidden state. Apache-2.0, four named authors, 29 commits since
2026-09-21.

Its headline, Qwen3-8B on BANKING77 20-way, 300 items:

| | raw | L0 | L1 |
| --- | --- | --- | --- |
| flips when options reversed | 0.230 | 0.073 | 0.077 |
| accuracy | 0.747 | 0.803 | 0.807 |
| ECE | 0.240 | 0.184 | 0.095 |
| auto-decidable at ≤5% error | 7.7% | 46.3% | 52.0% |

**This is R1's mechanism, published as a product, with the order-sensitivity measured rather than
assumed.** A 0.230 flip rate under option reversal is the kind of number our own R1 does not report
and should.

Three honesty markers worth recording: the repo says plainly that on its typed-decisions set
"'accuracy' is agreement with a teacher LLM" whose fresh sample agrees with itself only 0.735 of the
time; it marks the Jev 0.727 row "not measured here"; and a commit on 2026-09-25 **retracts** an
earlier 1.49× prefix-caching claim that a second machine could not reproduce. Against that: the
LICENSE appendix has a blank copyright holder, PyPI `anyjev` 0.0.2 still points at a personal fork
while the tree says 0.1.0, and the L2 heads are fit on splits of the same public tasks they are
scored on.

## What each is good for

| | Source card | Comparator arm |
| --- | --- | --- |
| imajev | Yes — the mixture documentation and the self-reported contamination finding are worth citing | **Qualified.** Trained on all three M5 corpora, so it cannot carry a held-out claim there. It can carry a declared-contaminated reference row, scored by us and labelled as such |
| AnyJev | Yes — L0's zero-label de-biasing and the flip-rate metric are methods we can use | **Conditional.** "Open Qwen + L0" on a suite we freeze and score ourselves is fair. The shipped L2 heads on typed-decisions are not, and its Jev 0.727 is a published row, not a measurement |

**Neither supplies a hosted-Jev arm**, because neither contains a single call to `jev-latest` on
the same items. Any comparison with Jev in either repo is "as published" or, for imajev's images,
impossible. If an experiment needs the hosted API held fixed, these do not provide it — which is
itself the finding about how this ecosystem compares itself to Jev.

## Run notes, 2026-09-25: AnyJev L0 measured on M5

Qwen3-8B, bf16, A100-40GB, peak 23.6 GB, transformers backend, AnyJev at git `795a4970`. L0 only:
zero labels, no `calibrate()`, no `fit_head()`, `anyjev-heads/` never opened, 0 fit examples used,
and every returned `Decision.level` asserted to be `L0`. The zero-label claim holds exactly as
published — no level fell back.

### Its readout caps a decision at 26 options

`anyjev/question.py` sets `MAX_OPTIONS = 26`, because the readout is a single letter A–Z, and the
README says a span readout is roadmap rather than code. **A 77-way decision therefore cannot be one
AnyJev question at all** — `Question.choice` raises rather than degrading.

That is a structural property of reading a decision off one prefill, not a packaging gap. The
method's whole advantage is that nothing is generated and nothing is parsed, and the price of that
is an answer that must fit in one token position. Any claim of the form "turn any LLM into a
typed decision model" carries this ceiling, and it lands exactly where bounded-classification work
gets interesting: BANKING77 is 77 labels, CLINC is 151, and an intent taxonomy in production is
usually larger still.

The run worked around it honestly and recorded the workaround in the output's own `deviation`
field: four fixed sub-questions of at most 25 real options plus a literal `none of these`, global
argmax over per-option L0 probabilities. **T2a is therefore a different question shape from every
other arm's T2a** and is marked partitioned wherever it is compared.

### Order sensitivity, and where L0 actually removes it

First 300 confirmation rows, `options_enumerated` forward against reversed:

| task | options | raw flip | L0 flip |
| --- | --- | --- | --- |
| T2a | 77, partitioned | 0.3867 | 0.2467 |
| T2b | 2 | 0.1767 | **0.0000** |
| T2c | 2 | 0.0467 | **0.0000** |

**At two options L0 is exactly order-invariant, and the raw model is not** — one T2b answer in six
changes from swapping two strings. That is the cleanest confirmation we have of their central
claim, measured by us rather than read from their README.

At 77 partitioned options L0 removes about a third of the flips and leaves a quarter of answers
order-dependent. It is not comparable to their published 0.230 → 0.073 on a 20-way question:
reversing a 77-item list also reshuffles which options share a sub-question, so this is a strictly
harder test. Read it as a partitioned-L0 number.

The flip counts reproduced **bit-identically** across a session Colab reclaimed mid-run and the
rebuilt one, which is the determinism check the method's own design implies.

### The cost of a letter readout at scale

| task | rows | rows/s | wall clock | prefills/row |
| --- | --- | --- | --- | --- |
| T2a | 6,000 | 0.632 | 2.64 h | 81 |
| T2b | 12,845 | 61.06 | 210 s | 2 |
| T2c | 60,000 | 37.66 | 1,593 s | 2 |

Cyclic shifts multiply prefills by the option count, so the de-biasing that makes L0 order-invariant
is also what makes a 77-way decision two orders of magnitude slower per row than a binary one.
**Zero labels is not the same as zero cost**, and on this evidence the method is strongest exactly
where the option set is small.

Two packaging facts worth recording: PyPI `anyjev` is **0.0.1** against a repo at 0.1.0 and is
missing `heads.py`, `pipeline.py` and `truncate.py`, so an install from PyPI is not the library the
README describes; and vLLM was never exercised here because transformers worked first try.
