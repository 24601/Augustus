---
name: augustus-train
description: "Trains, fits, or compiles a small decision model for a bounded decision, and reports whether it was worth it. Use when choosing a rung (zero-shot, few-shot, fitted head, fine-tune, compiled program), sizing a fit to a label budget, running on rented or local GPUs, or deciding whether a trained artifact beats the free baseline. Companion to the augustus skill, which covers placement and evaluation."
license: MIT
metadata:
  version: 0.8.0-dev
  evidence: "research/080/receipts/m5-grading-2026-09-25.md — ten arms on three real-text tasks"
---

# Augustus Train

Build the cheapest artifact that meets a bounded decision's policy, and prove it beats doing
nothing. The companion `augustus` skill decides *whether* a decision model belongs somewhere; this one
builds it.

Every number in this skill was measured on three real-text tasks in one experiment
(`research/080/receipts/m5-grading-2026-09-25.md`), not taken from a vendor.

## The rung ladder, sized by labels you actually have

| Labels available | Rung | What it costs |
| --- | --- | --- |
| none | Zero-shot readout over label names | Nothing to fit, and see the warning below |
| none, and order matters | Zero-label de-biasing (cyclic option shifts) | Multiplies inference by the option count |
| 8–64 per class | Few-shot contrastive fit (SetFit) | Minutes on a small GPU |
| a few hundred to a few thousand | Small encoder fine-tune, or a head over a frozen encoder | 87 s to 8 min at 1,600 rows |
| a few thousand or more | Larger encoder fine-tune | Hours |
| a written rule you can state | Hand-written deterministic program | Free, and competitive on binary decisions |

**Climb only when the rung below fails a measurement, never because the next one sounds stronger.**
A contrastive fit on 1,600 rows beat a compiled program, a fine-tuned program, a hand-written
program and three readouts on the tasks measured. A 98-second encoder fine-tune could not be
separated from it on one task after 4,500 seconds of the alternative.

## Start with the two free baselines. Report both. Always.

1. **The constant.** Answer the majority class for every row and compute its cost.
2. **Zero-shot.** Score the untrained model that reads your label names, on the same held-out rows.

Do not skip these because they seem weak. On two binary tasks, **zero-shot scored 0.645 and 0.358
against constants of 0.945 and 0.918** — the free option was worse than answering the same thing
every time. On a 77-way task the same zero-shot reached 0.695 against a 0.022 constant. A rung that
does not report what the free options already got cannot claim it was necessary.

## The four measurements that decide whether a rung is real

Run all four. Each one caught a failure that accuracy alone did not.

### 1. Cost under the real matrix, not accuracy

Score with the decision's own costs. Where a false negative costs four times a false positive, an
arm that is **more accurate can cost more**: measured costs fell monotonically as arms called the
rare class more often, while their accuracy ran the other way. If your matrix is asymmetric and no
arm chose a threshold, the ranking you are looking at is mostly operating points.

### 2. Base rate of the class the cost matrix cares about

Emit rate against true rate, per class. Six artifact forms missed one 5.8% base rate in six
directions, from 2.3% to 91.7%. **Stating the base rate in the prompt does not make a model honour
it.** If the rare class is the expensive one, fix the operating point with a threshold rather than
hoping the fit learned it.

### 3. Option-order sensitivity

Run 300 rows, reverse the option list, count changed answers. Anything that reads its options is
suspect: measured flip rates ran to 0.25 on a two-option question, and one model changed 11% of
answers at the setting its vendor ships to hide the effect. Fitting collapses it — a GLiNER2 model
went 0.110 to 0.027 on a 77-way task and 0.203 to 0.000 on a binary one. **A zero-shot number from
an option-reading model is not a stable quantity.**

### 4. Calibration against the priced class

If the artifact emits a probability, bucket it against correctness *and* against the expensive
class. A measured confidence rose monotonically with correctness, 0.77 to 0.94, while **every call
of the rare class sat in its two lowest buckets** — a score that orders the easy majority perfectly
and says nothing about what the matrix prices. Ranking correctness is not calibration.

## Write the spec so an artifact can obey it

- **Enumerate the options verbatim.** "One of the 77 intent labels" is a reference a person looks up
  and a compiled artifact cannot. Enumerating them cut invented outputs from 1,749 distinct strings
  to 1,477 and turned the rest into real label names, and it cost nothing — the 77-line list still
  left all 24 worked examples inside a 5,120-token budget.
- **Say the answers in one vocabulary.** If stored labels are `0`/`1` and the spec says
  `toxic`/`not toxic`, an artifact that obeys the spec scores zero. Declare the mapping once, render
  both sides through it, and accept both spellings when grading.
- **Do not let an abstain option collide with a real class.** Pricing a correct answer as a refusal
  is a scoring bug that looks like a modelling result.
- **Check the spec describes the task the labels encode.** A spec asking for one of 150 intents,
  against labels that are binary, means every spec-reading arm answered a question nobody scored.
- **Some artifacts do worse with more instruction.** One model's own documentation reports a
  paragraph of rules scoring 0.24 against 0.67 for a single sentence. Read the artifact's
  documentation before pasting your whole spec into it, and record what you sent.

See [reference/spec-defects.md](references/spec-defects.md) for the full list with the symptoms each
one produces.

## Before you trust any GPU number

The three-step verification, each step added after the previous one lied:

1. The install log is not evidence — both `pip` and `uv` buffer a wheel build.
2. A capability flag and a device-init line are not evidence. A package can report CUDA support,
   enumerate the device, and run every layer on CPU.
3. **The proof is the layer assignment line plus a memory delta attributable to your process.**
   `load_tensors: layer N assigned to device CUDA0`, and your PID holding memory in `nvidia-smi`.

Getting this wrong raises no error. It finishes on CPU at a fortieth of the speed while a rented
card bills by the hour.

## When a run looks too expensive, measure the configuration before cutting the recipe

Four projections in one day collapsed once the serving path changed, with the recipe untouched:
17 hours to 58 minutes, 7.6 hours to 17 minutes, 8 hours to 42 minutes, and an unbatched teacher
from 29 to 442 examples a minute. **A rung that looks unaffordable is usually a claim about the
configuration measured.**

Legitimate serving changes, which alter no number the recipe states: batching, gradient
accumulation that preserves the effective batch, replica concurrency, a different installer, a
different card. Recipe changes, which must be recorded as a different arm: fewer examples, fewer
steps, a smaller effective batch, a shorter option list, a different model.

**An optimization whose error is the size of the effect is not an optimization.** A 4× batched path
was measured, found to disagree with the reference path on 4 of 300 rows — the same order as the
flip rate it was being used to measure — and discarded. Verify a speedup returns identical answers
before relying on it.

[reference/compute-envelope.md](references/compute-envelope.md) has the measured hardware figures,
including the two that point opposite ways.

## Report

State, for every arm: cost under the real matrix, accuracy, invalid-output rate, abstention rate,
emitted rate of the expensive class, option-order flip rate, training wall clock, and the two free
baselines. Name the hardware. If an artifact's training corpus includes your evaluation corpus, say
so on the row and run it anyway — a labelled contaminated row answers "is this whole ladder in the
right range", which nothing else does.

If you add an arm after seeing the others' scores, its interval is exploratory and carries no
pre-registered guarantee. Say that on the row rather than adjusting the multiplicity afterwards.
