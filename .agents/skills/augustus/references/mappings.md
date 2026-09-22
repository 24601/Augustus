# Mappings: classical methods -> judgment-class designs

Each card states what transfers, what remains exact, the theory preconditions,
and a falsifier. TypeSafe Jev is the default hosted exemplar, not a monopoly
and not evidence that another typed surface is calibrated. Status vocabulary:
**Theory** identifies a classical result under its assumptions; a placement is
**Hypothesis** until a specific run supports it. Use **Reported** or
**Reproduced** only with a named source or run, and **Rejected** for an invalid
substitution. A familiar architecture is not evidence of local improvement.

## 1. Semantic judgments -> features and explicit utility

**Method:** feature engineering and MCDA. A bounded model may turn text or an
image into named features; code may filter, rank, fit a supervised model, or
explore policies without re-inference.

```text
evidence -> {relevance_p, risk_p, quality_distribution}
policy   -> utility / vetoes / Pareto view -> act
```

**Preconditions:** stable, versioned rubrics; held-out outcomes; intended
comparability; no leakage from label-guided feature design. Score has no natural
units, and equal expectations can hide different tails. Hard exclusions remain
rules. **Falsifier:** the features fail to beat exact/lexical baselines or the
decision flips under harmless rubric paraphrases. **Status:** empirical shape;
every new feature set is a **Hypothesis**.

## 2. Probabilistic judgments -> cost-sensitive decisions

**Method:** Bayesian decision theory and selective classification. Evidence
supports acts; policy owns their costs and authority. For calibrated binary `p`:

```text
t = C_FP / (C_FP + C_FN)
```

**Preconditions:** calibrated probability on the target population, an adequate
loss model, and a measured fallback. Ranking affinity or top-choice mass is not
automatically `P(action succeeds)`. Abstention has a cost. **Falsifier:** a
held-out expected-loss/coverage curve does not beat the baseline, including
human escalation. **Status:** threshold formula is **Theory**; task threshold is
an empirically selected policy.

Fail-open/fail-closed is not a model-family property. It is an action policy:
retrieval may preserve original order on failure; a destructive act may require
exact authorization and human confirmation; a harmless classifier may select a
declared default. Model evidence never grants permission by itself.

## 3. Semantic predicates -> decision circuits

**Method:** decision tables, Boolean circuits, DAGs, and state machines. Model
evidence may estimate fuzzy predicates; code owns branches, compatibility,
transitions, and effects.

**Preconditions:** each question is atomic and answerable from state; compound
relations stay compound; exact predicates stay exact. Do not multiply correlated
parallel judgments into a joint. **Falsifier:** exhaustive decision-table cases
find contradictory or unsafe branches, or stale observations bypass the exact
recheck. **Status:** each circuit is a system-level **Hypothesis**.

Example: judgment estimates whether dialogue is conciliatory; game code enforces
inventory, chronology, and reachable scenes. Counterexample: one “is this trace
correct?” score hiding schema, order, authority, and outcome checks.

## 4. Retrieval -> bounded semantic reranking

**Method:** candidate generation plus a more expensive relevance function.
Retrieve broadly with exact filters/BM25/embeddings; judge a bounded shortlist
with a shared rubric; return citations from the source store.

**Preconditions:** adequate retrieval recall, sufficient evidence per candidate,
stable rubric, and candidate-set coverage. Choice distributions from different
pools are not directly comparable. **Falsifier:** end-to-end recall@k, top-k
quality, latency, or cost fails to improve over the retrieval baseline. Measure
retrieval and reranking separately. **Status:** local **Hypothesis**; reported
dataset claims do not transfer.

## 5. Hierarchy -> bounded heuristic search

**Method:** beam/A*/MCTS over a meaningful graph or taxonomy. Judgment may
provide branch priority, prune evidence, a prior, or a leaf heuristic; code owns
frontier, budget, transitions, and probes.

**Preconditions:** meaningful structure, recoverable breadth, and either a real
simulator or shallow speculative depth. A product/geometric mean of related
scores is a ranking heuristic, not a calibrated path probability. **Falsifier:**
greedy/beam/flat baselines expose pruning loss; exact outcome probes disagree
with high-valued leaves. **Status:** beam and grounded-search patterns have
empirical instances; a new domain is a **Hypothesis**.

## 6. Value of information -> gather as an enumerated act

**Method:** EVSI/EVPI. Add `retrieve`, `measure`, `ask`, or `escalate` to the act
set and buy evidence only when expected reduction in decision loss exceeds cost.

```text
EVSI = current minimum expected loss
       - expected minimum loss after observation
```

**Preconditions:** credible outcome, observation, and cost models. Model
uncertainty alone is not VOI; another call with no new evidence is not an
observation. **Falsifier:** gathered evidence rarely changes the act or its
benefit does not repay latency/cost. **Status:** placement is **Theory**; numeric
VOI from judgment outputs remains **Hypothesis** until act/outcome logs exist.

## 7. Signal detection -> criterion, not accuracy

**Method:** detection theory. Separate evidence separability from the policy
criterion. Plot ROC/PR under deployment prevalence; select operating points from
miss and false-alarm costs.

**Preconditions:** representative labels and attention to base-rate/subgroup
shift. Calibration and discrimination are different. **Falsifier:** the desired
false-alarm or miss budget cannot be met at useful coverage. **Status:**
**Theory**; every deployment curve is empirical.

## 8. Control structure -> sensor != constraint (Leveson)

**Method:** STAMP/STPA and feedback control. Judgment may estimate risk,
progress, or anomaly. Controller policy, authorization, interlocks, and
post-action probes remain exact.

**Preconditions:** explicit hazards, unsafe control actions, timing, fallback,
and sensor-failure analysis. **Falsifier:** model outage, spoofing, delay, or
TOCTOU allows the hazard. **Status:** control ownership is **Theory-informed**;
the sensor's utility is a **Hypothesis** until closed-loop tests pass.

## 9. Search / control loops -> one substituted classifier step

Replace only the judgment-shaped step, not the whole planner:

```text
observe exactly -> build candidates -> judge/rank -> policy selects
-> code validates and acts -> probe outcome -> update state
```

This supports tool routing, browser candidate selection, incident triage, and
human-in-the-loop queues. Candidate construction, permissions, arguments,
effects, and completion stay outside the model. **Falsifier:** the loop cannot
recover from a wrong choice, or completion is accepted without a probe.
**Status:** local **Hypothesis**; each loop needs system evaluation.

## 10. Spec property pipeline (Hypothesis)

People or generators draft candidate properties; bounded judgment may rank
them; humans approve them; a model
checker/prover runs; mutation and vacuity tests challenge the property. The
checker owns the result. Falsifier: proposed properties are tautological, omit
known bug classes, or never fail under seeded mutations.

## 11. Alloy instance loop (Hypothesis)

Alloy finds bounded instances/counterexamples; judgment clusters or prioritizes
them; the analyst revises the model. Never call the judgment a satisfiability
result. Falsifier: triage hides a distinct counterexample family or adds no
review efficiency at fixed discovery recall.

## 12. Runtime assurance sandwich (Hypothesis)

Separate preventive enforcement from outcome detection:

```text
observe -> judgment proposal -> policy -> exact enforcement -> action
        -> authoritative outcome monitor/probe
```

A monitor reports properties of the observed trace. Prevention needs an
enforceable property and a mechanism that can block or switch before violation,
with justified timing and recovery assumptions. A post-action probe cannot undo
an irreversible act. Physical control needs a safe fallback and a justified
recoverable region; software must validate and authorize the operation and target
at the effect boundary. Unknown/pending monitor results are not satisfaction.
Falsifier: the harmful effect can occur before the first veto, or stale judgment
bypasses the interlock. See `formal-methods.md` for claim ownership.

## 13. DST multiverse triage (Hypothesis)

Deterministic simulation testing supplies reproducible seeds and property
violations. Judgment may cluster traces or rank seeds for humans. Falsifier:
clusters merge causally distinct bugs or reduce unique-bug discovery at fixed
review budget. A clean search is coverage, not proof.

## 14. Durable agent control (Hypothesis)

Durable workflow engines own retries, idempotency, time, and settlement.
Judgment may classify a task state or recommend a bounded next route; workflow
policy owns transition and compensation. Falsifier: replay changes effects,
model outage prevents recovery, or soft “done” replaces durable settlement.

## 15. Assignment hybrid — soft affinity + hard solver (Hypothesis)

Use semantic affinity as one cost/feature in assignment; a solver enforces
capacity, eligibility, fairness, and coverage. Preconditions: comparable feature
scale and explicit constraints. Falsifier: perturbing affinity causes constraint
violations (a design bug) or no improvement over exact features.

## 16. Situated density (Hypothesis)

Frequent local judgments may outperform rare global summaries when each is
grounded in current state and paired with a short feedback loop. This is an
observational-design hypothesis, not a universal throughput claim. Falsifier:
local calls add correlated noise, alert fatigue, or no action change.

## 17. Input brittleness -> sensitivity, calibration, selective abstention (Hypothesis)

Run controlled paraphrase, order, distractor, and evidence-ablation suites.
Abstain/escalate when a declared instability statistic crosses policy limits.
Do not claim wording invariance. Falsifier: instability fails to predict errors
or the abstention band does not reduce risk at useful coverage.

## 18. Structural prove intersection soft remainder (Hypothesis as domain-general; empirical only for named shapes)

Let exact mechanisms settle what they can: schemas, allowlists, parsers, text
layers, lints, permissions. Send only unresolved semantic cases to judgment.

```text
exact allow/deny/prove -> unresolved remainder -> model evidence -> policy
```

Precondition: “unresolved” is distinct from “safe.” Falsifier: remainder routing
drops known positives or soft evidence overrides exact denial.

## 19. Effect-oriented state-machine loops (Hypothesis)

Represent actions by effects and state transitions, not surface command tokens.
Judgment may map intent/evidence to a closed effect class; exact handlers enforce
preconditions and verify postconditions. Falsifier: paraphrased commands with the
same effect receive materially inconsistent policy, or privileged effects bypass
the same handler.

## Mapping card template

```text
Classical method and preconditions:
Judgment-shaped component:
Model family and state boundary:
Exact remainder and authority owner:
Statistical-validity test:
Action policy, costs, fallback, reversibility:
Baseline and smallest falsifier:
Status (Theory / Reported / Reproduced / Hypothesis / Rejected):
```

Related: `mental-models.md`, `composition-algebra.md`, `methods-catalog.md`,
`toolbox-mapping.md`, `formal-methods.md`.
