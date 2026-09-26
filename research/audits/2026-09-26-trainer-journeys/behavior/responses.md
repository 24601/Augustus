# Application response

Use an exact router, not a trained text model. The reported failure is a stale
table; predicting from 30 notes would introduce uncertainty where the approved
field already gives the answer. I implemented `renewal_router.py`, a standard-library
callable and JSONL CLI with a single immutable approved mapping and a policy ID
on every result. Note text and old route fields cannot override `notice_type`.

The contract is case-sensitive exact matching: no undocumented aliases or trimming.
Unknown strings, missing fields, malformed field values, non-object records,
invalid JSON, duplicate JSON keys and non-JSON constants produce
`operations_review` with a distinct status. A corrected input is recomputed with
no cached route. Output is a local routing decision, not a delivered queue item.
The calling application remains responsible for handing review records to operations.

Run from this directory:

```sh
python3 -m unittest discover -s . -p 'test_renewal_router.py' -v
printf '%s\n' '{"notice_type":"renewal_due"}' | python3 renewal_router.py
```

Or import `route_notice` and pass a dictionary. Copying this one Python file is
sufficient for local use; it needs no labels, training data, external services or
model downloads. The tests include isolated fresh-process use of that copy.
The 30 actual notes and deployed table were not supplied; I did not invent them or
claim replay of last month's incident. The tests exercise synthetic contract cases.
There is no external deployment and no claim that the stale deployed table was fixed.
Use the policy ID and source digest to identify this local replacement rather than
silently reusing the old deployment identity. Reject the component if any approved
input routes incorrectly, note text overrides the field, or malformed input escapes
the review path. Exact execution results are saved separately.

# Advisory responses — no training or evaluation runs claimed

## 1. Support classifier from reply rows

Do not fit the 18,000 reply rows as if they were independent first messages.
First reconstruct one decision-time example per ticket: the first incoming message
as visible before routing. Remove future resolution notes, subsequent replies and
final queues from features; quoted conversation must not smuggle later information
back into the initial view. Customer IDs identify groups, not predictive features
for a new-customer target. If the initial messages cannot be recovered, these rows
do not support the requested deployment claim; collect the correct inputs first.

Define the target queue and annotation guide. A final queue is a weak historical
action label, not automatically the correct first-message route. Have independent
reviewers label decision-time evidence, adjudicate costly disagreements and retain
the original labels and rationale. Separate genuinely ambiguous cases from missing
labels and unknown intents; allow operations review rather than forcing a label.
Keep label-definition and dataset versions and label-availability timestamps.

Deduplicate same-ticket quotes and related examples before assigning roles. Use
customer-disjoint development/confirmation and forward time cutoffs, with training
labels available at the training cutoff. Reserve a future-month sample of genuinely
new customers; a random row split is not evidence for this goal. Fit vocabulary and
other learned transformations on training only. Audit exact and near duplicates,
ticket/customer overlap and class coverage; 18,000 rows may represent far fewer
independent units.

Start with existing routing and a sparse text linear classifier as comparators.
Choose policy on development data using queue-specific costs, critical-class recall,
review load and end-to-end latency. Freeze artifact and policy before confirmation.
Report independent customer counts, per-class errors, uncertainty and exclusions.
This is a proposed workflow; there is no fitted classifier without the source data
and resolved label definition.

## 2. Six intents, 700 labels, CPU-only constrained runtime

My first candidate is word/character TF-IDF with a regularized linear classifier,
not an instruction-model fine-tune. It needs no pretrained base, can learn useful
lexical distinctions on CPU, and is a plausible fit for a 150 MB offline envelope.
That is a hypothesis, not a measured 40 ms p95 promise. Pin the library/runtime and
export vocabulary, transformations, coefficients, class IDs and routing policy.

Use grouped development validation if labels share users or documents; keep an
independent final set for any generalization claim. Within two total CPU hours,
reserve time for data checks, reload and timing, and bound search to a few justified
word/character feature and regularization choices. Stop at the budget including
failed fits and evaluation. Compare to current rules and a cost-appropriate constant;
inspect confusion pairs and rare intents rather than optimizing accuracy alone.

Measure full input preprocessing plus inference at batch one on the actual target
CPU, realistic and long messages, cold start separately, and loaded peak memory as
well as artifact bytes. Clarify whether 150 MB covers the whole process or just
the model; until clarified, treat whole-process memory as the conservative bound.
If semantic paraphrases are the specific failure and time remains, consider one
small frozen encoder/head only after verifying its pinned license, offline assets
and resource fit. Do not assume a quantized encoder fits merely from its file size.
No GPU, hosted fallback, model rental or SetFit run is required. If no candidate
meets quality and resource constraints, retain the incumbent/review path and report
the constraint conflict, not a fabricated winner.

## 3. Warranty costs and changing taxonomy

Assuming correct actions cost zero and 0.08 is a reliable probability of the binary
urgent event, not a raw score: escalating costs 5 × 0.92 = 4.6 in expectation;
not escalating costs 200 × 0.08 = 16. Escalate. The binary threshold is
5 / (200 + 5) ≈ 0.02439, with an explicit tie convention. A threshold of 0.5
ignores the asymmetric costs. Verify probability meaning/reliability on the target
population; if those assumptions fail, select a score policy empirically on
development outcomes instead of presenting this arithmetic as calibrated behavior.

For routine/urgent/fraud, obtain a full action-by-true-class loss matrix and select
the action with minimum expected loss using class-identity-bound probabilities.
Maximum softmax above 0.5 neither encodes that loss nor detects unseen types. A
model can confidently assign an unknown to a known class. Specify distinct unknown,
insufficient-evidence and malformed paths, route them to a named reviewer, and
evaluate real unknown/challenge examples plus representative known traffic. Choose
and freeze review policy from costs, capacity and measured risk/coverage; do not
reuse the binary threshold as a multiclass certainty cutoff. Safety/authority
checks remain outside the classifier. No classifier was run for this answer.

## 4. Adaptive four-CPU-hour search

Reuse development data for preprocessing/head search; log every candidate and its
outputs, elapsed CPU cost and rejected trials. Those scores are exploratory and
selection-biased. Set the budget, stop rules, loss, constraints, independent unit,
comparison count and acceptable margins before searching. Leave enough budget to
reload and evaluate the frozen finalist. Keep the future-month customer-disjoint
sample sealed from preprocessing, tuning, error reflection and candidate selection.

No: if its mistakes choose another candidate, it cannot remain the independent final
test for that new candidate. Preserve the original finalist's result, mark the
revealed sample as development for subsequent selection, and obtain new independent
confirmation. Alternatively use a prospectively justified adaptive-valid procedure
with its actual assumptions; ordinary holdout reuse is not one. If no fresh sample
or budget is available, report the new candidate as exploratory and retain the
incumbent rather than asserting a confirmed improvement. This is advice, not a
completed four-hour search.

## 5. Notebook to Choice JSON

Export the entire trusted inference bundle, not only weights: preprocessing and
tokenizer/vocabulary, model revision, ordered training class IDs, canonical labels,
policy, optional calibration, dependency lock and content hashes. Map each score
column through the exported class IDs to stable option identities; never zip scores
to the caller's incidental option order. For a fixed three-class head reject
unrecognized/missing/duplicate options or use an explicitly designed error/review
result. It is not a general arbitrary-choice engine merely because its JSON is
Choice-shaped. Match the consumer's actual schema rather than inventing a vendor
API contract.

Raw maximum logit is not a confidence probability. Adding the same constant to all
logits changes it without changing class probabilities or rankings. Do not let it
authorize skipping human review. If a probability consumer is required, define the
event, assess reliability on representative independent data and fit calibration
only where warranted, using separate or out-of-fold evidence. A validated raw-score
policy is possible but must be labeled as such, not as probability.

Test every class and all six label-order permutations mapped back to identity,
unknown options, empty/malformed input, nonfinite scores, ties and review boundaries.
In a fresh process without notebook state or fit files, replay both ordinary and
boundary inputs and compare reference scores under declared tolerances and actual
actions exactly where required. Keep review until the frozen policy has evidence
supporting the permitted automation risk. No export or model replay occurred here;
the notebook and consumer contract were not provided.

## 6. Replace Jev using last quarter's outputs

Do not start this distillation from the proposed data yet. The installed guidance
flags TypeSafe/Jev output training restrictions. Verify the applicable current
terms and obtain specific authority covering the proposed replacement training;
access to old outputs is not permission. I have not checked current contractual
terms here and will not treat a provenance declaration as legal clearance. This
also includes indirect use for filtering, selection or reward. Use independently
human-labeled permitted data or another explicitly permitted source if that
authority is unavailable.

Even with permission, a last-quarter ticket specialist only learns that task and
taxonomy, not a general instruction-conditioned Jev replacement. Preserve teacher
revision, prompts, input time, sampling, filtering and source lineage; exclude
confirmation examples from teacher generation or selection. Audit class mix,
abstention omissions, stale policies, invalid outputs and duplicates. Teacher
agreement measures imitation. Compare against current Jev/current rules using
independent human-adjudicated labels on the future deployment population, with
costly slices, unknowns, review load and full serving cost. Keep the incumbent
until the candidate and policy support the required outcome. No teacher calls,
training, uploads or replacement activation were performed.

## 7. Rewrite

The training job now saves the tokenizer with the exported model weights.
