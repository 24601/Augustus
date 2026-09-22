# FAQ (design judgment, not an API)

This FAQ explains placement and boundaries. TypeSafe Jev is Augustus's default
hosted exemplar by project preference, not an empirical adoption claim. Use live
provider documentation for API contracts.

## Isn't this just classification?

The underlying task often is classification. The design contribution is making
the judgment an explicit, typed, evaluated component between evidence and
policy. That makes candidate coverage, abstention, thresholds, errors, and
fallbacks reviewable. A stable supervised classifier may still be the best
model; a regex may make the model unnecessary.

## Is Jev probabilistic programming?

No. Parallel Choice/Score/Noul-like answers are normally marginal judgments
conditioned on shared state, not a joint probabilistic program. Do not multiply
them as independent probabilities or infer causal structure from them. Compose
them through explicit policy and test the composition end to end.

## Should we replace the LLM / the stack?

Usually no. Replace one decision-shaped step:

- code keeps exact work and control;
- a decision model handles a bounded semantic judgment;
- a generator writes prose/code or proposes open-ended candidates;
- the host authorizes, executes, and verifies.

A no-generator loop is valid when nothing needs writing. That is a property of
the task, not a reason to make a classifier generate.

## Is Jev the only model this skill covers?

No. The class includes classical supervised models, hosted typed APIs, open
decision heads, constrained autoregressive/logit readouts, span extractors,
sequence classifiers, rankers, and vision scorers. They share bounded outputs
but differ in objective and failure modes. See `judgment-class.md`.

## Jev or Laya (or some other open head)?

Start with constraints:

- choose hosted Jev as the project-default exemplar when hosted processing is
  acceptable and a quick bounded judgment is needed;
- choose an open head such as [Laya](https://github.com/NandhaKishorM/laya) or
  [kev](https://github.com/jaredpalmer/kev) for privacy, offline operation,
  inspectability, or deployment control;
- choose a classical model when you have representative labels for a stable
  domain.

Open hosting transfers evaluation responsibility to you. Wire compatibility is
not logit equivalence, and neither implies calibration.

## Open weights vs Jev vs constrained decoding vs encoder vs LoRA?

These are not a single axis.

- **Hosted typed API:** productized bounded decisions; validate on your data.
- **Trained head/LoRA:** weights adapted for the task; inspect training target,
  holdout discipline, and shift behavior.
- **Constrained decoding:** guarantees valid output form, not semantic truth.
- **Logit readout:** obtains mass over declared tokens; prompt/model dependent.
- **Encoder classifier/extractor:** efficient one-pass labels or spans; often a
  strong local choice.

Pick by the required output and eval, not by serving technology.

## GLiNER vs GLiClass vs Jev vs a cross-encoder?

- [GLiNER](https://arxiv.org/abs/2311.08526) locates spans in text.
- [GLiClass](https://arxiv.org/abs/2508.07662) categorizes a whole input against
  supplied labels.
- A decision head answers a bounded question about state.
- A cross-encoder commonly ranks query–candidate pairs.

Use locate when the answer is literally present, categorize for tags, decide
for an action-relevant proposition, and rank for order. A score from one species
does not inherit the semantics of another.

## Can I threshold CLIP / SigLIP as a safety gate?

Not by default. Their outputs are affinities or relative candidate scores.
Calibrate and validate them on the actual task, especially under shift, or use
them only to shortlist candidates. [SigLIP documentation](https://huggingface.co/docs/transformers/v4.39.2/en/model_doc/siglip)
does not turn affinity into permission.

## Is this skill only for software engineering?

No. The same pattern applies to inbox triage, operations, research screening,
document routing, moderation, knowledge work, and personal workflows. In a
practice without code, the checklist, ledger, law, or two-person rule is the
policy layer.

## Can a System One model replace TLA+ / Dafny / DST?

No. Formal tools own proof, constraint solving, model checking, and systematic
execution. A judgment model can rank properties, classify counterexamples, or
route attention. It cannot discharge a proof obligation. See
`formal-methods.md`.

## Isn't a high-confidence Noul basically a proof?

No. It is model evidence about a proposition under supplied state. Proof comes
from a valid derivation; runtime truth comes from observation; authorization
comes from policy. High confidence cannot compensate for missing evidence,
stale state, or an incomplete candidate set.

## Is Augustus another Jev how-to?

No. Augustus selects the placement, family, policy boundary, and falsifying
experiment. Provider docs own request fields and SDK behavior.

## Is Jev a drop-in for LLM-as-judge?

Only for rubrics that decompose into narrow bounded questions. It can be useful
when a cheap, repeatable distribution is preferable to generative prose. It is
not automatically an adequate judge of overall quality, and the judge must be
validated against independent labels. Measure variance as well as agreement.

## Allowlist first, then judgment?

Yes when exact structure can prove easy cases. Apply allow/deny/schema checks
first and send only the semantic remainder to the model. The model cannot
override a deterministic deny. On the action path, error handling follows the
action's consequence, not a universal “model family” policy.

## Can confidence gating catch a forced wrong Choice?

Not reliably. If the correct answer is absent, the model may confidently select
the least-wrong offered option. Candidate coverage and explicit `other`/`none`
must be tested separately from calibration.

## Should the model write the quote / citation / click target?

Prefer pointer-not-generator. Code enumerates lines, spans, records, or observed
controls; the model selects identifiers; code copies exact bytes and validates
the target. A missing candidate should trigger retrieval/gathering, not
fabrication.

## Should compaction summarize?

Not when provenance or recovery matters. An extractive sieve can keep verbatim
evidence and hide the rest behind a recall key. Use a generator summary only as
an explicit lossy product, retain the original, and evaluate downstream answer
quality—not compression ratio alone.

## Fail-open or fail-closed—which?

Name the action first.

- Dropping evidence fails to **keep**.
- Reranking failure preserves baseline order.
- A reversible route may use a declared default.
- A mutating tool call with stale/missing approval does not execute.
- A draft may go to a human rather than remain stuck forever.

Provider timeout is neither approval nor rejection. Specify the concrete
fallback for each action and error class.

## Type-safe or correct?

Typed output prevents structural surprises. It does not establish factual
accuracy, calibration, candidate completeness, policy correctness, or safe
execution.

## Is Jev the policy? Is Jev authorization?

No. The model estimates a named proposition. Policy code combines evidence with
costs, deterministic constraints, user grants, and state. The host owns
authorization and execution. Re-check identity, permissions, target, and live
state immediately before a consequential effect.

## Does a typed answer unlock the next step?

Only if explicit policy says so and all non-model preconditions still hold.
The answer is one input to the transition, not the transition itself.

## Does “trained for calibration” mean I can threshold p as a frequency?

No. It means the training objective sought useful probabilities. Verify
reliability, Brier/log loss, risk–coverage, subgroup behavior, and OOD drift on
the deployment population. Calibration can change with wording, candidate set,
base rate, model version, and runtime.

## Does AUC mean the probabilities are honest?

No. AUC measures ordering across positives and negatives. Calibration measures
the relationship between predicted probabilities and observed frequencies.
Both can matter; neither substitutes for action-specific expected cost.

## Can I gate on confidence alone?

No. Gate on the semantic answer, its distribution, deterministic checks,
candidate coverage, evidence freshness, and action cost. A large top-1 margin
can still be confidently wrong.

## Is a local `/v1/systemone` the same as Jev?

No. It may reproduce a wire shape. Model objective, weights, input envelope,
errors, probabilities, and calibration can differ. Label it by its actual
provider and version.

## Are local CUDA likelihoods a Noul?

No. They are model likelihoods/readouts until validated for the requested
proposition. A softmax over answer tokens is not automatically calibrated
`P(event)`.

## Should RAG stop at Top-K / a reranker?

Only if ranking is the product. For evidence selection, retrieve broadly, rank,
then make an absolute keep/no-match judgment or send the shortlist to a human.
Measure retrieval recall separately because later stages cannot recover omitted
evidence.

## Does Jev `done` mean the task succeeded?

No. `done` is a termination judgment. Success must be checked against server
state, tests, a task oracle, or independently observed post-state.

## Do Ax / DSPy own the control plane?

No. They can optimize LM-program prompts, examples, and module choices. Exact
ontology, permissions, thresholds, state transitions, and tool allowlists remain
outside the optimizer. See `optimizer-integration.md`.

## Train a specialist, or few-shot the hosted API?

Few-shot a hosted decision API when volume is moderate, the surface changes,
and only the final choice matters. Train a specialist when privacy/latency/scale
requires it or downstream code consumes the probability distribution. Use
independent gold and validate in the deployment runtime; teacher outputs alone
are not ground truth.

## Is Noul 0.5 “maybe / medium”?

It represents maximum uncertainty for a binary proposition, not medium
intensity. For graded intensity, use an ordered Score rubric with concrete
levels and inspect the full distribution.

## When does a decision model hold?

It holds when evidence is available, the output is bounded, candidate coverage
is adequate, an abstention/fallback exists, and end-to-end evaluation beats a
simpler baseline on quality, latency, and total expected cost. Total cost must
include generator fallback, human review, retries, and recovery—not only model
price.
