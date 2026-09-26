# Methods catalog: named algorithms -> judgment-shaped substitution

This catalog asks where a bounded semantic judgment can replace one component
of a known method without replacing its mathematics. Every row inherits the
method's preconditions; a typed answer is not a warrant that they hold.

Labels: **Theory** (classical result under preconditions), **Pattern**
(architecture or procedure, not a claim of measured improvement), **Hypothesis**
(untested placement), **Rejected** (preconditions fail). A reported or reproduced
result additionally needs a named source or run. If “stays exact” is vague,
learn the method before substituting.

## Supervised learning and feature engineering

| Method | Judgment-shaped component | Stays exact | Preconditions / status |
|---|---|---|---|
| Gradient-boosted trees | named semantic features from text/image | split, labels, loss, fit, final calibration | leakage-free held-out outcomes; **Pattern** shape |
| Logistic/Cox model | interpretable semantic predictors | fit, regularization, time/censoring model | stable feature meaning and model assumptions; **Hypothesis** |
| Taxonomy classification | bounded label choice or hierarchical branch priority | taxonomy, retrieval, coverage, evaluation | true class is represented or `other`; **Pattern** shape |
| Learning-to-rank | relevance/quality features or bounded comparator | candidate retrieval, group split, ranking loss | shared rubric and query-group evaluation; **Hypothesis** |

Falsifiers: exact/lexical baseline wins; features are unstable to harmless
paraphrase; train/test leakage; subgroup or temporal collapse.

## Statistical inference and estimation

| Method | Judgment placement | Stays exact | Preconditions / status |
|---|---|---|---|
| Selective classification | score/ranking or probability evidence for act/abstain | selection rule, fallback, risk/coverage evaluation | deployment-relevant labels and valid selection/evaluation; calibration additionally needed when policy interprets values as probabilities; **Theory + empirical policy** |
| Reliability calibration | raw output evaluated/corrected on labels | binning/fitting, Brier/log loss, confidence intervals | representative calibration set; **Theory** |
| Self-consistency | repeated judgments estimate variability | aggregation and escalation | diversity/independence source understood; **Pattern**, not proof |
| Inter-rater reliability | model as one rater on frozen artifacts | agreement statistics and gold adjudication | fixed rubric and sampling; **Hypothesis** per judge |
| Psychometric/rubric score | distribution over anchored ordinal levels | weighting and reliability analysis | ordered, stable anchors; **Theory-informed** |
| Naive Bayes | possibly estimate one semantic feature, not a joint posterior | priors, likelihood combination, smoothing | conditional independence; usually **Rejected** for multiplying same-state judgments |

For calibrated binary `p`, the two-act cost threshold
`t=C_FP/(C_FP+C_FN)` is **Theory** only with adequate costs and calibration.
Calibration describes groups, not individual correctness.

## Search, planning, and operations research

| Method | Judgment placement | Stays exact | Preconditions / status |
|---|---|---|---|
| Beam search | branch priority / prune evidence | frontier, beam width, budget, terminal test | meaningful hierarchy; **Pattern** shape |
| A* / best-first | heuristic feature, never guaranteed admissible unless proven | graph, costs, closed set, goal test | if optimality requires admissibility/consistency, soft heuristic cannot claim it; **Hypothesis** |
| MCTS / PUCT | prior, prune evidence, leaf heuristic | tree, exploration, simulator, backprop, probes | trustworthy transitions/rewards; **Pattern** only in grounded settings |
| Sequential screening | pass/review/keep-looking evidence | stopping boundaries and error budget | representative labels and sequential-error accounting; **Hypothesis** |
| Routing/dispatch | affinity among eligible routes | capacity, eligibility, grants, solver | closed candidate set; **Pattern** shape |
| Knapsack/portfolio | semantic value/risk feature | exact constraints and optimizer | comparable utilities and explicit risk policy; **Hypothesis** |
| Assignment/min-cost flow | one affinity term | capacities, fairness, integrality, solver | scale/constraint validity; **Hypothesis** |

Never let a heuristic claim a theorem the search relied on. A model score is not
an admissible A* heuristic, a rollout reward, or a transition model by default.

## Information theory and signals

| Method | Judgment placement | Stays exact | Preconditions / status |
|---|---|---|---|
| Entropy | arithmetic over returned distribution | calculation and interpretation | distribution is meaningful for the task; **Theory** |
| Signal detection | evidence variable | criterion, ROC/PR, prevalence/cost model | representative positives/negatives; **Theory** |
| Change/anomaly detection | semantic anomaly feature | baseline, control limits, alert policy | stable reference distribution; **Hypothesis** |
| Kalman/Bayesian filtering | observation evidence only | state transition, covariance/update math | explicit generative/noise model; **Hypothesis** |
| Context sieve | relevance evidence per block | always-keep rules, cache, recall path | false-drop budget and recoverability; **Pattern** shape |

Entropy is uncertainty within the offered distribution, not truth uncertainty in
general. Low entropy can be confidently wrong or omit the correct option.

## Verification and logic

| Method | Judgment placement | Stays exact | Preconditions / status |
|---|---|---|---|
| Claim/evidence entailment | triage supports/contradicts/not-established | quote extraction, source identity, audit | evidence is present and relation is atomic; **Pattern** shape |
| Spec conformance | prioritize named requirements or suspicious artifacts | requirement set, checker, enforcement | model verdict is evidence only; **Hypothesis** per task |
| Type/schema validation | route likely mismatch for review | actual parser/type checker and authorization | machine-checkable facts never delegated; **Rejected** as replacement |
| Model-checker output triage | cluster/rank counterexamples | model, property, scope, solver result | preserve unique failure modes; **Hypothesis** |
| Deductive proof workflow | rank failed obligations/lemmas | proof assistant, annotations, kernel | proof object/checker remains authority; **Hypothesis** |
| Runtime verification | soft anomaly sensor beside monitor | temporal monitor and actuator | monitor sees authoritative events; **Hypothesis** |

## Experimental design and measurement

| Method | Use | Preconditions / status |
|---|---|---|
| Held-out evaluation | select rubric/threshold on A, report once on B | prevent adaptive test reuse; **Theory** |
| Behavioral perturbation | option order, distractor, paraphrase, evidence ablation | preserve intended semantics; **Pattern** |
| Ablation | compare exact-only, model-only, and composition | same workload and policy; **Theory-informed** |
| Bootstrap/confidence interval | quantify metric uncertainty | sampling assumptions and enough units; **Theory** |
| Mutation/vacuity test | verify properties can fail on seeded defects | representative mutations; **Pattern** for specs |
| Shadow mode | log proposed actions without effects | faithful traffic, privacy, outcome capture | **Pattern** for rollout safety, not correctness |

## Economics and game theory

| Method | Judgment placement | Stays exact | Preconditions / status |
|---|---|---|---|
| Expected utility | belief evidence | acts, utilities, constraints, argmin/argmax | calibrated beliefs and adequate utility; **Theory** |
| Value of information | estimate state relevant to gather decision | observation model/cost and policy | act/outcome validation; numeric use is **Hypothesis** |
| MCDA | semantic criterion features | weights, vetoes, Pareto analysis | legitimate compensability; **Theory-informed** |
| Mechanism/game response | opponent-state evidence | rules, equilibrium/solver, risk limits | adversarial shift expected; **Hypothesis** |
| Auction/market triage | materiality/direction evidence | orders, limits, accounting, compliance | no execution authority; **Hypothesis** |

## Human factors, organizations, and control

| Method | Judgment placement | Stays exact | Preconditions / status |
|---|---|---|---|
| STAMP/STPA | sensor for unsafe-context cues | hazards, constraints, controller, interlock | analyze sensor failure/delay/spoofing; **Theory-informed** |
| Hysteresis controller | noisy state estimate | enter/exit thresholds and memory | stable sampling/timing; **Pattern** shape |
| Triage queue | priority evidence | eligibility, SLA, ownership, escalation | measure starvation and subgroup effects; **Hypothesis** |
| Two-person rule | may prioritize review, never replace approver | identity and dual authorization | independence of approvers; **Rejected** as model substitute |

## Rejected (standing, so they are not rediscovered)

- Multiplying parallel same-state judgments into a joint without validated
  conditional independence.
- Treating a probability-like output as a p-value or frequentist test statistic.
- Comparing Scores across questions without a shared, versioned rubric.
- Treating calibration as certification of an individual case.
- Using judgment as reward/value without independent observed outcomes.
- Calling bounded model checking, simulation, or DST unbounded proof of the
  deployed implementation.
- Letting a ranker, classifier, or generator grant permission.
- Replacing arithmetic, counts, dates, schemas, permissions, or settlement with
  semantic judgment.

## Operators and theorems (third tier)

### Substitutable operators

| Construct | Judgment role | Preconditions |
|---|---|---|
| `argmax` | winner from a closed Choice | candidate coverage; `other`/abstain if open |
| expectation | Score expectation over defined levels | ordered numeric utilities; inspect full distribution |
| indicator | `p >= t` inside policy | validate the action-specific operating point; calibration is additionally needed when policy assumes probability meaning |
| conditional filter | evidence selects branch | fallback and authority remain explicit |
| ordering | bounded rerank | shared rubric; retrieval recall measured |

### Theorems as system-level guarantees

| Theorem/concept | Valid transfer | Precondition to preserve |
|---|---|---|
| Bayes | update after genuinely new evidence | likelihood model; no invented independence |
| LLN / variance reduction | average suitable repeated samples | independence/weak dependence and stable distribution |
| Jensen | compute nonlinear utility from full distribution | for convex `f`, `f(E[X]) <= E[f(X)]`; concavity reverses the inequality; equality is possible; preserve distribution/utility assumptions |
| Markov property | compact state for a loop | state contains all history relevant to transition/outcome |
| Goodhart | independent outcome check for optimized judgment metric | gold signal not identical to proxy |
| Simpson's paradox | inspect population strata | meaningful stratification and enough data |

### Non-substitutable constructs

Sums, products, counts, date math, gradients, transforms, schema checks, proof
steps, and cryptographic/authorization operations stay exact. Judgment may
choose which exact operation to inspect or run; it does not become that
operation.

## Open rows (test these next; do not cite until measured)

- Kalman-style observation updates where the transition/noise model is real.
- Proposal distributions for importance sampling, with bias diagnostics.
- Program-synthesis candidate reranking over exact test results.
- Counterexample clustering with unique-bug recall as the target.
- Semantic assignment features inside a hard constraint solver.

Every experiment must name baseline, split, perturbations, action-level metric,
fallback, and the result that would reject the row.
