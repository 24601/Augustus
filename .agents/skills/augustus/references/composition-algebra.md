# Composition algebra: where a judgment-class model sits relative to any method, operator, or algorithm

Let `J(s)` be bounded model evidence about state `s`, `P` an explicit policy,
and `F` any algorithm, tool, or action. TypeSafe Jev is the default hosted
exemplar, but the placement grammar is provider-independent.

```text
state -> J(state) -> P(evidence, exact facts) -> F -> observed outcome
```

The model supplies evidence; policy selects or authorizes acts. Position alone
does not determine fail-open/fail-closed behavior. Consequence, reversibility,
and an independent authority boundary do.

## The positions

| # | Position | Form | Legitimate use | Governing caveat |
|---|---|---|---|---|
| 1 | **Operand / feature** | `F(J(s))` | semantic feature in a statistical or optimization model | validate and version it; scale is not natural |
| 2 | **Post-judge** | `F(x) -> J(result)` | inspect output for named qualities | verdict is evidence; only this position sees the result |
| 3 | **Gate / filter** | `P(J(s)) ? F : fallback` | prefilter, review band, context sieve | policy owns branch; hard rules and authorization remain outside J |
| 4 | **Selector** | `J(s)` ranks `{F1...Fn}` | choose route, model, tool, effort | code supplies/validates candidates and dispatches |
| 5 | **Comparator / rank key** | `sort(xs,J)` | bounded semantic reranking | common rubric; measure candidate recall separately |
| 6 | **Prior / initializer** | `J(s) -> F`, then refine | beam/MCTS priority, starting hypothesis | heuristic prior is not posterior; observations correct it |
| 7 | **State estimator** | `J(s_t) -> P -> controller` | progress, risk, stuck, done evidence | controller, hysteresis, interventions stay exact |
| 8 | **Metric / loss proxy** | optimize `J(output)` | optimize a semantic rubric | qualify repeatability/proxy gaming; keep gold outcomes |
| 9 | **Verifier sensor** | `J(artifact,property)` | triage possible conformance or violation | does not discharge proof or replace a checker |
| 10 | **Discretizer / encoder** | unstructured `s -> J -> enum` | map observed candidates to typed values | closed answer space/evidence boundary must be real |
| 11 | **Budget / stop signal** | `P(J(history)) -> continue/stop` | decide whether more search/review is worth it | conservative limits and terminal probes stay in code |

These are placements, not validity claims. Each starts as a **Hypothesis**;
provider contracts establish output shape, while local evidence must establish
semantic and decision quality.

## Logical operators over judgment outputs

- **Negation.** For a genuine binary probability, `P(not A)=1-P(A)`.
  Ask the operational form directly when wording effects matter.
- **Conjunction/disjunction.** Do not multiply parallel answers from the same
  state without a validated conditional-independence model. Ask the compound
  relation directly or combine atomic evidence through documented policy.
- **Quantifiers.** Evaluate one item predicate per candidate, then let code
  apply `all`, `any`, counts, review bands, and exceptions. `min`/`max` are
  policy aggregators, not automatically probabilities of `forall`/`exists`.
- **Implication/chains.** Decompose observe -> judge -> policy -> act ->
  observe. Multi-hop claims in one question hide missing state and dependence.
- **Voting/ensembles.** Repeats estimate variability only if the source of
  diversity is understood. Agreement among correlated judgments is not proof.

## Rules that hold across every position

1. **Evidence is not authority.** Removing the model may change prioritization
   or convenience; it must not silently expand permissions. Policy and host own
   side effects.
2. **Estimate is not measurement.** Post-execution probes own facts such as
   “payment settled” or “test passed.” Pre-action scores cannot concede them.
3. **Statistical validity and action policy are separate.** First test
   discrimination, calibration, dependence, shift, and variance. Then choose
   thresholds from costs, reversibility, law, and fallback behavior.
4. **Calibration is positional and local.** A threshold validated for ranking
   visibility does not transfer to authorization or stopping.
5. **Shared-state width can be efficient; dependency depth is sequential.**
   Batch questions answerable from one state. Call again only when new state or
   candidates depend on prior results. Measure this engineering tendency; do
   not universalize latency or cost.
6. **Closed candidates stay closed.** Choice probabilities are conditional on
   offered options. Include abstain/other or retrieve more when coverage is open.
7. **TOCTOU applies.** Revalidate exact facts and authorization at use time.

## The application generator (traversal, not brainstorming)

Cross **positions (1–11)** with a classical construct from
`methods-catalog.md`:

1. State the construct and theorem-level preconditions.
2. For each position ask whether a knowledgeable person could make a bounded
   semantic judgment from supplied state.
3. Reject cells requiring arithmetic, exhaustive proof, missing knowledge,
   unconstrained generation, or authority.
4. Classify the substitution: **marginal** (replaces a heuristic/review),
   **newly feasible** (enables a previously uneconomic cadence), or **invalid**.
5. Name family, exact remainder, policy, failure mode, and fallback.
6. Write a falsifier first: held-out labels, perturbation, baseline,
   end-to-end cost, and action-level harm.

An untested candidate may enter `mappings.md` as a Hypothesis. Promote its
evidence status only after the relevant acceptance test runs and is recorded.

## Worked position distinctions

**Retrieval.** Judgment may be comparator (rerank), gate (discard only under a
recall-preserving policy), or budget signal (buy deeper retrieval). It is not
the index; evaluation includes recall.

**Tool use.** Judgment may select a documented tool. Code still checks grants,
schema, operation/target pairing, current state, and executes. Match is not
permission.

**Formal workflow.** Judgment may rank counterexamples or label likely failure
classes. The checker/prover owns the formal claim.

**Control.** Judgment may estimate `stuck` and `progress`; a controller applies
hysteresis and escalation. Completion is conceded only by an outcome probe.

## Falsification matrix

| Risk | Minimal test |
|---|---|
| missing evidence | redact evidence; confidence or coverage should fall |
| option effects | shuffle order, add distractors, remove winner |
| dependence fiction | compare aggregate formula with compound-event labels |
| poor calibration | reliability/Brier/log loss on deployment-like holdout |
| action mismatch | expected-loss/coverage curve including fallback |
| proxy gaming | optimize against J, then score independent gold outcomes |
| stale state | mutate facts between judgment and act; exact recheck catches it |
| hidden generation | outputs must be selected from code-owned candidates |

## Open positions (candidates, not yet evidenced)

- **Reward shaping inside RL**: **Hypothesis**; requires observed rewards and an
  independent environment, not model judgment as its own ground truth.
- **Grammar/sampling constraints**: **Hypothesis**; semantic guidance does not
  replace syntax or safety constraints.
- **Spec/criteria inference from failures**: **Hypothesis**; learned criteria
  need human review and non-vacuity tests.
- **Numeric VOI from model distributions**: **Hypothesis** until act/outcome
  logs validate the probability and observation model.
- **Formal/DST/runtime-assurance triage**: plausible placement; each product
  row remains **Hypothesis** until a checker-backed test runs.
- **Universal paraphrase-stability bounds**: **Rejected universally**; measure
  wording sensitivity per task and provider.

Related: `mental-models.md`, `mappings.md`, `methods-catalog.md`,
`toolbox-mapping.md`, `formal-methods.md`, `judgment-class.md`.
