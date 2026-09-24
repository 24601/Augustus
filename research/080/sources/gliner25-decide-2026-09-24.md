# GLiNER2.5-Decide — card (2026-09-24)

First sighting. Read-only inspection of the model card; nothing downloaded or run. Every number
below is **Reported** by the publisher unless marked otherwise.

| Item | Value |
| --- | --- |
| Model | `fastino/GLiNER2.5-Decide`, Apache-2.0, published by Fastino, 7 downloads at sighting |
| Base | `fastino/gliner2-large-v1`, encoder DeBERTa-v3-large |
| Size | card says **340M**; the Hub's own metadata panel says **0.5B params, F32**. DeBERTa-v3-large is ~304M backbone plus a 128k × 1024 embedding table, so ~435M total. The card's figure appears to exclude embeddings, and the two numbers are not reconciled on the page |
| Interface | `classify_text(text, schema)`; labels supplied at call time, single forward pass, no generated tokens, several heads scored in one call |
| Paper | GLiNER2, arXiv 2507.18546 (Jul 2025) — describes the family, not this checkpoint |

## What it is

A non-generative typed-decision classifier with a schema-driven interface: intent, routing,
sentiment, priority, policy, multi-label tags, yes/no gates, question-over-passage, described
labels, and ordinal scales. This is the same shape as a Choice or an ordinal Score, arrived at from
the information-extraction direction rather than the decision-model direction. It runs on CPU.

That it is Apache-2.0 **on the weights** is the material difference from LaKun: it is a thing we
could actually score ourselves, on a suite frozen first.

## The headline does not survive its own arithmetic

Reported exact-match accuracy on `fastino/fast-decisions`, 17 domains × 300 held-out examples
(n = 5,100), with the publisher running every baseline:

| Model | Avg |
| --- | --- |
| GLiNER2.5-Decide | 60.2% |
| GLiNER2 XL (1B) | 59.6% |
| JevK5 | 57.6% |
| SemIf (Qwen3.5-4B) | 56.4% |
| GLiFormer large-v1 | 49.0% |
| Laya Router | 46.6% |

**Computed here, not reported:** at p ≈ 0.6 and n = 5,100 the standard error of a single accuracy
is \(\sqrt{0.6 \cdot 0.4 / 5100} \approx 0.69\) percentage points. The claimed lead over GLiNER2 XL
is **0.6 points, smaller than one standard error on either arm**. A paired test could in principle
resolve a difference that small, and none is reported: no paired counts, no interval, no seed, no
per-domain table. So "leads open typed-decision models, including a 1B GLiNER2" is not established
by the evidence on the page. What the table does support is the more interesting claim the card
also makes — that a ~340–500M encoder is *not behind* models up to 4B on this suite.

The 4-point gap to SemIf (4B) and the 11-point gap to GLiFormer are larger than that noise floor
and are plausible as reported, subject to the caveat below.

## Caveats that would have to be removed before any use as a comparator

- **The suite is the publisher's own.** `fastino/fast-decisions` is theirs, held out from their own
  training distribution. "Not trained on public benchmarks" is a claim about contamination, not a
  claim of transfer; an in-distribution held-out split measures fit to their domains.
- **Every baseline was run by the party that wins.** Label sets, prompt handling and parsing for
  JevK5, SemIf, GLiFormer and Laya Router are all chosen by Fastino. Our climb ledger already
  refuses a headline where the scorer and the winner are the same party; this is that pattern with
  competent execution rather than sloppy execution.
- **Exact-match on supplied labels** rewards a parser as much as a decision. Nothing on the page
  separates the two.
- **JevK5 appears as a losing baseline.** That is a claim about a Jev model, run by a competitor, on
  a suite of their construction. It is not evidence about Jev in either direction and must not be
  cited as such.

## Disposition

**Discovery record only. Not an M5 arm.** It is not in the artifact-form ladder, it is not a
teacher, and nothing here changes a design decision or a lock.

The one thing it earns is a **standing candidate for an external comparator**, on the same terms as
Eikos: permissible only if we score it ourselves, on a suite frozen before we run it, with the
schema and parsing we publish. Its Apache-2.0 weights and CPU-sized footprint make that cheap to do
later. If that ever happens, the reported table above is not carried across — we would report our
own numbers with intervals, and the publisher's table stays labelled Reported.

Worth noting for the position paper's §3.6 rather than for an experiment: this is a second
independent arrival at *typed decisions with a call-time schema and no generated tokens*, from a
vendor whose starting point was information extraction. The convergence is evidence that the shape
is being rediscovered, which is a claim about the field, not about any one model's accuracy.
