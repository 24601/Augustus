# Composition calculus: typed joins, decision loss, and useful placements

Let `J(s)` be bounded model evidence about state `s`, `P` an explicit policy,
and `F` any algorithm, tool, or action. TypeSafe Jev is the default hosted
exemplar, but the placement grammar is provider-independent.

```text
state -> J(state) -> P(evidence, exact facts) -> F -> observed outcome
```

The model supplies evidence; policy selects or authorizes acts. Position alone
does not determine fail-open/fail-closed behavior. Consequence, reversibility,
and an independent authority boundary do.

## Build a typed decision graph

This is a small conditional calculus, not a universal theory or proof that a
learned component works. Use only the laws needed by the proposed system.
First write the graph, including retrieval, human fallback, failed calls and
outcome collection. For each learned edge, qualify more than its JSON type:

```text
quantity: probability / rank / ordinal / measurement / causal effect
event/support; population and selection policy; evidence and prediction horizon
units; candidate coverage; model/rubric/adapter/calibration versions
assumptions; qualification artifact; missingness and outcome provenance
consumer preconditions; exact constraints; fallback and effect owner
```

A 30-day purchase probability among contacted leads is not intervention uplift
for all leads. Matching field names do not repair the population, horizon or
causal mismatch. A join must satisfy the consumer's assumptions or use an
explicit, independently qualified conversion. Declarations can be checked;
their empirical truth cannot be established by a schema validator.

### Laws for composing decisions

**Branches: total expectation.** For a mutually exclusive, exhaustive terminal
branch partition under one policy, `E[L] = sum_b P(b) E[L | b]`. Use common loss
units and count shared overhead once. Include human delay, fallback and missed
opportunities. A 90%-traffic branch losing 1 and a 10% branch losing 10 give
1.9, not the unweighted 5.5. Zero-mass branches have no estimated conditional
loss. Historical branch outcomes do not identify a new intervention's effects.

**Cascades: condition on what reaches the next stage.**
`P(G and H) = P(G) P(H | G)` when `P(G)>0`; if nobody passes G, joint coverage
is zero and conditional qualification is undefined. Likewise measure
`E[L | G and H]`, not the downstream model's global error. If `G=H` with
probability .5, joint coverage is .5, not .25. A changed selector can invalidate
downstream calibration without changing that downstream model's bytes.

**Failure budgets: no independence required.**
`P(union_i F_i) <= min(1, sum_i P(F_i))`. A system bound additionally needs
every relevant system failure to lie in that union. Include common causes and
the exposure horizon. Multiply conditional-on-reach rates by reach probability
for tighter accounting, or conservatively bound reach by one. Operational error
budgets and uncertainty in their estimates are
different quantities; simultaneous statistical bounds need their own confidence
allocation. A daily bound is not a lifetime guarantee.

**Sensitivity of an expected-loss policy.** For the same finite outcome space,
feasible acts and loss table `0 <= L(a,y) <= B`, let `a_p` and `a_q` minimize
risk under true law p and estimated law q. Then:

```text
TV(p,q) = 0.5 * sum_y abs(p_y-q_y)
E_p L(a_q,Y) - E_p L(a_p,Y) <= 2 B TV(p,q)
```

Each fixed action's risk changes by at most `B TV`; add/subtract the two q
risks and use q-optimality. An approximate optimizer adds its risk slack.
This connects estimation error to decision regret, not permission. ECE, teacher
agreement or confidence does not supply the unknown conditional TV. Unbounded
loss, a different action set or an unidentified causal law breaks the transfer.

**Information: augmentation is not substitution.** With fixed acts/loss and a
common joint model, an optimal policy may ignore a free extra observation, so
its Bayes risk cannot increase. Acquisition cost, delay, privacy and bounded
computation can reverse the practical value. Blackwell experiment dominance
is stronger than one accuracy score, but an isolated comparison need not hold
beside arbitrary background evidence. For independent fair bits Y,C, signals
`A=C` and `B=Y xor C` each reveal nothing about Y alone. Given C, B determines Y
and A still does not. Compare the relevant joint/conditional system.

Processing can help a bounded agent compute without creating new world
information. If Z uses only X and learned parameters Theta through a channel
with no extra Y information, data processing gives
`I(Y;Z | Theta) <= I(Y;X | Theta)` and `I(Y;Z) <= I(Y;X,Theta)`.
Do not drop Theta, retrieval or memory from the inputs. Redaction may reveal
prior knowledge rather than prove invalidity; check its permitted scope and age.

**Feedback: qualify a trajectory, not a frozen stage.** Once actions affect
future observations, log the policy-induced sequence and finite-horizon loss.
Control stability, safe exploration and termination require their own dynamics,
delay and disturbance assumptions. Perfectly predicting yesterday's labels can
coexist with oscillating retraining or an overloaded review queue. Check the
closed loop, interlocks and recovery; one-step accuracy is insufficient.

These identities and conditional bounds are **Theory**; whether their assumptions
hold and the composition improves the task remains an empirical question.
Primary foundations include [comparisons of joint signals](https://benjaminbrooks.net/downloads/bfk_comparisons.pdf),
[data-processing channels](https://arxiv.org/abs/1508.06025), and
[performative prediction](https://proceedings.mlr.press/v119/perdomo20a.html).
Do not import a paper's stronger theorem without its exact assumptions.

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

### Averaging option permutations

When order affects a Choice, test probability averaging as a bounded
experiment, not an automatic repair. Align vectors by stable semantic label
IDs, validate their support and mass, then average. Never average positions
after shuffling; majority votes and probability averages are different rules.

For fixed predictions `p_1...p_M`, label `y`, and convex loss `L`, Jensen gives
`L(mean(p), y) <= mean(L(p_m, y))`. This covers Brier and log loss where
defined. It does **not** promise improvement over the best ordering, better
accuracy, calibration, or lower action cost. Correlation does not invalidate
this inequality; it does limit claims about independent evidence.

Full group averaging is order-invariant for a fixed predictor after aligning
labels. A sampled subset needs its own argument: canonicalizing labels and
freezing the sampled orders can stabilize the construction, but does not make
it the full-group average or control server randomness. Record seed, orders,
question IDs, ties, and aggregation version; separate those effects in tests.
[pijev](https://github.com/TypeLLM/pijev/tree/bca3a73d6419b794d63cd780ba4a0254579d7ccc)
is an implementation example, not evidence of universal gains.

Compare one ordering, a deterministic canonical ordering, and a bounded
ensemble on untouched paired cases. Include action flips, proper scores,
coverage, and measured tokens/latency. Batched permutations still add questions
and consume context; one HTTP request does not mean one decision's cost.

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

For a transfer from physics, biology, economics or another field, map its
variables, units, conservation/transition assumptions, objective and observation
process into this graph. Keep a useful derivation; reject a decorative analogy.
For example, hysteresis can motivate a two-threshold controller, but does not
transfer a physical stability theorem without a qualified dynamical model.

Turn the graph into adapters, explicit policy, a trace recorder and an outcome
evaluator when implementation is requested. Ablate the model and each added
stage; test a deliberately invalid join and a dependence/selection counterexample.
Then use the [incumbent–challenger workflow](optimizer-integration.md) to compare
complete outcomes under a bounded budget. The calculus generates and rejects
designs; it does not count as evidence that an unrun design wins.

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
