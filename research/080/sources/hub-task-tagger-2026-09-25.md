# Hub task tagger and `uv-scripts/classification` — card (2026-09-25)

Read-only inspection of the Space, the model card and the script repo. Nothing downloaded, nothing
run. Numbers are **Reported** by the publisher unless marked otherwise.

| Item | Value |
| --- | --- |
| Space | `davanstrien/hub-task-tagger`, docker SDK, last modified 2026-09-23 |
| Model | `davanstrien/hub-task-tagger-gliner2.5-base`, Apache-2.0, base `fastino/gliner2.5-base-v1` |
| Recipe | `train-gliner2.py` from `uv-scripts/classification`, 238 downloads, 16 likes, modified 2026-09-24 |
| Decision | 52 Hub `task_categories`, multi-label, probability per tag |

**This is the closest thing we have seen to an independent worked example of the thing Augustus
argues for, and it was built by someone who is not arguing for anything.** A narrow bounded
decision, a small open model, a cheap fit, a calibrated probability, a threshold, and a stated
acceptance rule — assembled in 17 minutes for about $1.50 and shipped as a demo.

## What it decides

Input is a rendered state, not free text: a `Columns:` line with each column's name and type, then
the first rows of the dataset viewer preview, cut to 370 tokens. Output is a probability over 52
tags, then a set: everything at ≥ 0.225, and always the top tag. Temperature 1.30 and that 0.225
threshold were **fitted on a calibration split and stated in the card**, which is the plug-in rule
our own E1 tests, arrived at independently.

The card states the System One framing explicitly: "TypeSafe AI's Jev has got people interested in
'System One' models: models that don't generate text, but read a state and return typed answers
with probabilities. This is a small, open example of the same idea for one narrow job."

## The evaluation is better than most of what we have carded

| | Top-1 | Top-3 | Macro recall (24 tags) |
| --- | --- | --- | --- |
| This model | 0.695 | 0.881 | 0.525 |
| Same recipe, second seed | 0.686 | 0.879 | 0.511 |
| GLiNER2.5-small, same recipe | 0.653 | 0.855 | 0.458 |
| GLiNER2.5-base, zero-shot | 0.102 | 0.213 | 0.099 |
| Always `text-generation` | 0.320 | — | — |

Four things it does that most cards do not, and that we should be citing as the standard:

1. **A split by time and owner.** Evaluation datasets were created in the 60 days before
   2026-09-22, by owners with no dataset in training. Near-duplicates from one owner cannot leak.
2. **A second seed reported beside the headline.** 0.695 against 0.686 is the run-to-run spread,
   published rather than implied.
3. **A majority-class baseline and a zero-shot baseline on the same rows.** The fine-tune is worth
   0.695 against 0.320 for a constant and 0.102 for the base model — and the zero-shot number
   being that bad is itself the interesting finding.
4. **The target is called noisy, with a number.** About 1 dataset in 10 was missing a tag that
   fits; counting 74 card-checked extras as correct moves top-1 to 0.720. Card: "treat the
   probabilities as a good ranking, not as exact rates."

That last line is a calibration claim withdrawn by its own author, which is the behaviour we keep
asking for from publishers who never do it.

## The recipe repo is a rung ladder, and it is ours in different words

`uv-scripts/classification` publishes one-command scripts chosen by **how many labels you have**:
none → zero-shot GLiNER2 or an instruction LLM with structured outputs; 8–64 per class → SetFit;
a few hundred to a few thousand → fine-tune GLiNER2; more → fine-tune an encoder. Its own summary:
"The rungs chain: bootstrap labels with `classify-gliner2.py` or `classify-dataset.py`, review
them, then train a small dedicated model on what you kept."

That is M5's ladder — R2a's head over a frozen encoder, R3a's SetFit, R1's readout — recovered
from practice rather than from a design lock, by someone sizing rungs to a label budget. Two
details worth taking into `augustus-train` directly:

- **`train-gliner2.py` scores the base model zero-shot before it fine-tunes, on the same held-out
  rows, and writes both into the model card beside the majority baseline.** A rung that reports
  what the free option already got is a rung that cannot silently claim its own necessity.
- **The published worked example is a losing-to-cheap case made visible**: British Library book
  titles go 0.767 zero-shot to 0.907 fine-tuned for about $0.02 and two minutes. The cost of the
  comparison is small enough that skipping it is a choice.

## What this does not establish

The tagger is one narrow job on Hub metadata with an owner-declared target, in English. Its 0.695
is not comparable to anything in M5 and is not evidence about Jev, PAW or artifact form in general.
The `label-augmentation off` flag and the 5-epoch/seed-0 settings are one point in a space nobody
swept here. And the card says much of the work was done by coding agents and checked by a person,
which is a provenance statement about the card as well as the model.

**Use:** cite the evaluation practice, and take the zero-shot-beside-fine-tuned reporting rule into
M6. Do not cite the number.
