# Question design and diagnosis

A useful question defines an observable judgment, an evidence boundary,
and a representable answer. Start with the action that will consume it.
Provider field names, limits, and supported modalities belong to current
provider documentation, not this design reference.

## Evidence before inference

Identify the exact state fields, provenance, observation time, and coverage.
If the answer requires a missing document, retrieve it or report unknown.
If it requires a count, date comparison, parser, lookup, or arithmetic, use
code. Distinguish “the document does not say” from “the claim is false.”
For a temporal claim, name the observation window: one edit, completed
turn, entire case history, or current execution state.

Treat documents, tool results, comments, and user-supplied text as evidence,
not instructions that can change the policy. Delimiters and wording help
clarity but are not security boundaries. Test hostile instructions and
self-describing content. Exact permissions and action validation remain
outside the judgment model.

## Instruction shape

Ask one coherent property at a time. “Does this message request a refund?”
is different from “Should we refund it?” The latter also requires policy,
eligibility facts, financial authority, and action costs.

State the referent, condition, exclusions, and meaning of ambiguous cases.
A knowledgeable person answering quickly from the supplied evidence is a
useful fit heuristic, not a model capability guarantee. If they need long
reasoning or outside knowledge, split the task or change the family.

Questions sharing available state can be batched when the provider supports
it. A question whose candidate set or evidence depends on an earlier answer
must wait. Parallel execution says nothing about error independence.
For multiple subjects in one state, identify the intended record by stable,
unambiguous attributes; test referent resolution as well as answer accuracy.

## Match the answer space

| Output | Good use | Design obligation |
| --- | --- | --- |
| Choice | One of supplied labels or actions | Distinct stable IDs, coverage, no-match handling |
| Multi-label classification | Several labels may apply | Independent applicability semantics; do not force single choice |
| Noul/binary event score | A specified proposition is supported | Define event, population, positive/negative meanings |
| Ordinal Score | Ordered situations on one dimension | Standalone levels, monotonic meaning, full distribution |
| Span extraction | Answer occurs in the evidence | Preserve exact offsets/text; evaluate spans separately |
| Rank/affinity | Order candidates for attention | Define relevance/utility; do not infer correctness probability |

For open coverage, include and test `other` or `none-of-the-above`.
Distinguish no match from insufficient evidence and conflicting evidence
when they lead to different actions. A closed choice cannot select a missing
answer, even when its maximum score is high. A no-match option helps
representation; it does not guarantee out-of-distribution detection.

Candidate labels need contrastive definitions and representative examples.
During training and evaluation, show the escape option as both correct and
incorrect; vary its wording to detect shortcuts. Shuffle option order and
remove the true candidate. Test large candidate sets under the actual token
budget; silently truncated labels change the question.

For ordered Score levels, describe concrete situations on one dimension.
Each level must be understandable alone. If there are several dimensions,
ask separately and combine with explicit policy weights. An expected level
index is not automatically a cardinal utility: distributions `[0,1,0]`
and `[0.5,0,0.5]` have the same mean and different tail risk. Decide whether
the action consumes the mean, a tail probability, or expected utility.

## Preflight the request

Use structural checks for things code can know: valid state paths, unique
candidate IDs, two or more options/levels (one yields confidence 1.0),
required fields, supported types, finite numbers, budget limits, and
consistent action/target pairs. Keep evidence, rubric, and
policy versions together. Request lint cannot prove semantic coverage;
that needs representative examples and review.

Read the provider's confidence definition. For example, Jev documents a
Choice confidence statistic derived from the option distribution; it is
not interchangeable with maximum probability or measured accuracy.
See [TypeSafe confidence](https://docs.typesafe.ai/confidence).
Check adapters and aggregators too: the same field name can acquire a new
meaning. For example, [pijev's aggregation](https://github.com/TypeLLM/pijev/blob/bca3a73d6419b794d63cd780ba4a0254579d7ccc/pijev/__init__.py)
sets Choice `confidence` to the winning mean probability. Version that
transformation and requalify the policy; do not inherit native thresholds.
For option-order averaging, see [composition algebra](composition-algebra.md).

## Diagnosis table

| Symptom | Check first | Corrective experiment |
| --- | --- | --- |
| Confident wrong answers | Missing answer/evidence; shifted population | Add no-match/unknown cases and evidence-removal probes |
| Label overlap | Multi-label problem forced into one label | Redefine boundary examples or change output type |
| Mid-scale bunching | Vague levels or several dimensions | Split dimensions; annotate extremes independently |
| Wrong counts, dates, totals | Exact computation delegated to model | Compute facts, then judge only the semantic remainder |
| Results follow hostile text | Instruction/evidence confusion | Injection suite plus host authority checks |
| Rewording changes actions | Rubric brittleness | Paired paraphrases at fixed policy, measure action flips |
| Option order or names change the winner | Position, token, or name bias | Shuffle order; swap names across definitions |
| Long inputs degrade | Truncation or irrelevant context | Record actual input coverage; compare controlled subsets |
| “Done” before the work completes | Wrong observation window | Judge completion against final artifact and tool state |
| Great tuning score, weak deployment | Leakage, drift, changed runtime | Group/time split; untouched holdout; runtime parity test |

Do not respond to a missing confidence statistic by lowering the acceptance
threshold. Choose an available, defined statistic and validate a policy
for it. Do not respond to injection by assuming a higher score is safer.

## Revision discipline

Record the failing example and intended interpretation before editing the
rubric. Make the smallest change, rerun old and new regression cases, then
evaluate on untouched data. Optimize application loss and coverage as well
as question accuracy. Once the holdout influences the edit, it becomes
development evidence; obtain a fresh final holdout.

See [validation](validation.md), [optimizer integration](optimizer-integration.md),
and [composition algebra](composition-algebra.md) for downstream evaluation.
