# Methods catalog: named algorithms → judgment-shaped substitution

The toolbox sweep names families; this catalog names **methods**. Each row
names the algorithm, the component inside it that is exactly a fast semantic
judgment over a fixed answer space, the Jev substitution, and what
deliberately stays in code. Rows carry status honestly: **Empirical recipe**
(dated launch-week artifact), **Contract** (docs), **Hypothesis** (plausible,
untested), **Rejected** (violates a boundary). Grow one falsified row at a
time — a row without an acceptance test stays Hypothesis.

Prerequisite the user is pointing at: you must actually know the method.
You cannot substitute into CatBoost without knowing that CatBoost treats
features as ordered/unordered and trains on labels. If a row's "what stays
in code" is vague, you don't know the method well enough yet — learn it
before substituting (the method's math is in-distribution; only the
judgment component is new).

## Supervised learning & feature engineering

| Method | Judgment-shaped component | Jev substitution | Stays in code | Status |
|---|---|---|---|---|
| Gradient-boosted trees (CatBoost/LightGBM/XGBoost) | Text-derived features the model can't see | Nouls/Score expectations as named numeric features; train on labeled outcomes; version feature defs with the model | Splitting, loss, calibration of the final model | **Empirical recipe** (autoresearch cookbook: Jev probabilities as CatBoost features) |
| Logistic regression / Cox models | Scaled, interpretable predictors from messy text | One Noul per predictor, each with its own labeled validation | Fitting, regularization, coefficient interpretation | **Hypothesis** (same mechanism as CatBoost row; not separately measured) |
| Clustering / topic assignment of text | Assigning a document to a labeled bucket | Choice over the taxonomy (≤255), or hierarchy/beam beyond 255 | Vectorization for recall, distance metrics, cluster count | **Empirical recipe** (hierarchical_classification cookbook) |

## Statistical inference & estimation

| Method | Judgment-shaped component | Jev substitution | Stays in code | Status |
|---|---|---|---|---|
| Naive Bayes classifier | P(class \| evidence) needs P(evidence-feature) from text | Distribution over class options from one state; label-dependence still your problem — do NOT multiply parallel nouls as independent evidence | Prior counts, smoothing, combining rules | **Hypothesis** |
| Self-consistency / ensembling of judges | Repeated independent ratings of the same object | N repeats over one state (output tokens free); entropy/disagreement across repeats as the review signal | Aggregation, escalation policy | **Empirical recipe** (self-consistency: nouls cookbook) |
| Judge qualification (interrater reliability) | A judge worth gating must be repeatable | Repeated judgments over frozen outputs before trusting either Jev or LLM as judge | Variance stats, agreement metrics | **Empirical recipe** (jev-as-a-judge: 224–279× tighter than GPT judge) |
| Neyman–Pearson / selective classification | Decision threshold under error costs | One threshold per action, set on split A, reported on split B; abstention path | Loss model, ROC analysis | **Contract + empirical** (confidence-routing; evaluator script) |
| Value of information (EVPI / EVSI) | Whether another observation is worth its cost | Gather as an enumerated act; pay iff expected decision-loss drop > cost | Cost of the observation; the loss table | **Hypothesis** as a numeric calculator; **Contract** as the placement (`mappings.md` §6) |
| Signal detection (Green & Swets) | Evidence variable + criterion | Noul as noisy evidence; t from costs and base rate; ROC/PR on your labels | Operating point, base-rate tracking | **Hypothesis** for non-SWE plots; **Empirical** as moderation *shape* (`mappings.md` §7) |
| Reliability calibration (Platt/temperature) | Raw scores → calibrated probabilities | Noul is natively calibrated **in-distribution only**; verify with reliability bins on your own population; re-fit a correction out-of-distribution | Calibration fitting, binning | **Empirical recipe** (ECE 0.0313 in-distribution; 32% OOD collapse — Archer Hume) |
| Survey scoring / psychometrics | Rubric level judgment with defined anchors | Score with concrete level descriptions; probabilities read beside every score | Weighted aggregation, reliability analysis | **Contract** (score docs: split composite judgments) |

## Search, planning & operations research

| Method | Judgment-shaped component | Jev substitution | Stays in code | Status |
|---|---|---|---|---|
| MCTS / PUCT | Prune invalid actions; priors P(s,a); leaf value V(s) | Batched Noul pruning + Choice priors + Score value — depth-capped where no simulator | Tree, budget, backprop, probes | **Empirical recipe** (jev-mcts: 24/24 vs 1/24 greedy; speculative depth 2) |
| Beam search over taxonomies | Which branches deserve expansion | Choice distributions as branch priority; keep K paths where ambiguity is early | Frontier, budget, final selection | **Empirical recipe** (beam K=3 cookbook) |
| Screening / Wald sequential tests | Pass / fail / keep-looking per candidate | One Noul gate per candidate in one batched request; budget in code | Sequential rule, stop boundaries | **Hypothesis** |
| STPA / STAMP control structure | Sensor reading vs enforced constraint | Judgment as sensor; constraints in policy/code/interlock; STPA table if the sensor lies | The constraint, the actuator, the probe | **Contract** as ownership; **Hypothesis** as domain product (`mappings.md` §8) |
| PufferLib / Ocean env contracts | Does this episode look like a known trainer-bug mode? | Cluster failing episodes; never "the policy is correct" | Seeded serial env, Ocean sanity, observed rewards | **Hypothesis** as placement; **Contract** that Ocean is not a comparative baseline (`formal-methods.md` DST trio) |
| Routing / dispatch (OR) | Which queue/agent owns this item | Choice + confidence-gated escalation; code owns capacity | Cost matrix, capacity constraints | **Empirical recipe** (intent-routing; LlamaIndex Jev selectors; skillranker) |
| Cascade / prefilter (IR) | Cheap reject before an expensive scorer or LLM | Per-candidate Noul/Score; fail-open on drop, fail-closed on dispatch | Candidate generation, always-keep set, recall keys | **Empirical recipe** (classifying RAG passages; jevprune; git-jev-stage) |
| Knapsack / portfolio selection | Per-item feature vector from text | Fan-out nouls/scores as features; optimizer in code | Constraint solver, weights | **Hypothesis** (mapping 1 shape) |

## Information theory & signals

| Method | Judgment-shaped component | Jev substitution | Stays in code | Status |
|---|---|---|---|---|
| Entropy as uncertainty signal | Measuring "how spread is this belief" | Entropy of returned distributions across repeats or options — computed in code from returned probabilities | All arithmetic | **Empirical recipe** (cookbook pattern) |
| Detector / Neyman filter (context) | Is this artifact relevant to the current task? | One relevance Noul per block before it enters context; stub + recall key | Cache, recall, safety keeps | **Empirical recipe** (winnow ≤0.22 hide; compaction 2-noul rule; pi-jev-context hide-not-delete) |
| Anomaly detection | Does this deviate from expected shape? | Guard nouls + harm Score over {input, output, tool trace} | Baselines, alert thresholds | **Empirical recipe** (guardrails cookbook; pi-jev output judge) |
| Allowlist ∩ remainder (code-then-model) | Unlisted / unstructured leftovers after a proof | Typed questions only on the unknown tier; admit iff every p < τ | Proven/refused in code; cannot block unless a sandbox sits under | **Empirical recipe** (jevgate 0/59 unsafe unasked held-out; doc-router 1.74× $). Domain-general: `mappings.md` §18 |
| Teacher distill of judgments | Copy a hosted decision API onto a small local head | LoRA / frozen-encoder heads trained on teacher answers | Independent gold labels; ECE on *your* cases | **Empirical recipe** as one 70-row run (openjev-lm 92.9%); **Hypothesis** as a general recipe |

## Verification & logic

| Method | Judgment-shaped component | Jev substitution | Stays in code | Status |
|---|---|---|---|---|
| Claim–evidence entailment (NLI) | supports / contradicts / not-established per claim–source pair | One Choice per pair + review flag; judge against the cited source text only | Quote extraction, citation graph, audit log | **Empirical recipe** (citation_check cookbook) |
| Spec vs artifact conformance (model checking *mindset*) | Property holds / violated / unverifiable for a named requirement | One Noul per requirement, batched; violated → named rule back into context (pi-warden shape). This is **not** TLC/Apalache/GNATprove | Requirement enumeration, enforcement, logging; the real checker if you have one | **Empirical recipe** (pi-warden: 6→0 rule breaks, 150 paired runs; jev-pref: YOU define the rule). Ownership split: `formal-methods.md` |
| Alloy finder vs Apalache / TLC | Which bound, which counterexample, is the property tautological? | Triage instances/CEs; never "this spec looks right" | Analyzer / SMT / explicit-state engine | **Hypothesis** as product; **Contract** as ownership (`formal-methods.md` §2) |
| Type-checking analog | Does this planned call match the schema/operation/target? | Decomposed nouls over {request, schema, trace}; never trust a Jev pass as authorization | Real validation of operation+target in code | **Empirical recipe** (validation.md self-monitoring) |

## Economics & game theory

| Method | Judgment-shaped component | Jev substitution | Stays in code | Status |
|---|---|---|---|---|
| Multi-criteria decision analysis | Attribute scores per alternative | Composite scores with weights in code (re-weight without re-inference) | Weight policy, Pareto views | **Empirical recipe** (mapping 1) |
| Mechanism/game response (adversarial state) | Opponent-intent / bluff / risk read on a state | Choice over reads + risk Score; policy in code; 2.5Hz-style advisory rate | Strategy solvers, exploitative math | **Empirical recipe** (jev-trader, game agents) |
| Auction/market event classification | Is this signal material? Direction? | Choice over event classes + urgency nouls; execution in code | Order execution, risk limits | **Empirical recipe** (jev-trader 81ms/block) |
| Assignment / scheduling (OR) | Soft affinity per pair | Score/Noul as a cost *feature*; solver owns capacity/legality | ILP/heuristic, fairness | **Hypothesis** (`mappings.md` §15) |
| Situated software (Shirky) | Local meaning inside a named group | Dense full-traffic judgment only inside a named community boundary | Public metrics, law, FM where wrongness is intolerable | **Hypothesis** (`mappings.md` §16) |

## Rejected (standing, so they aren't rediscovered)

- Parallel Noul answers multiplied into joint probabilities — same-state
  answers are not independent evidence.
- Jev as a p-value or test statistic — Noul is a calibrated belief, not a
  frequentist quantity.
- Cross-question Score comparability without a shared, versioned rubric.
- Calibration certifying an individual answer — it describes groups.
- Bandit value from Jev with no observed-reward environment.
- Jev as a stack replacement for an LLM. Mixed architecture is the default
  (`references/mixed-architecture.md`); generation, derivation, and exact
  work stay off Jev. Classification-skepticism is answered with placement,
  not a claim that classification is new.
- A Noul (or any judgment-class score) as a proof, a model-check, or a
  DST property. Judgment is a sensor; proof/types are constraints; DST
  is a searchlight (`references/formal-methods.md`).
- TOCTOU-of-Noul as fail-closed authorize (judge at t0, act at t1).
- Tautological / vacuous spec plus "the model said it looks good"
  (Hillel vibing specs; receipt theater).
- PufferLib Ocean scores as a comparative RL or judgment-class baseline.

## Operators and theorems (third tier)

Operators, theorems, and elementary functions are not one category. Split
them three ways, because each relates to Jev differently:

**1. Substitutable operators** — operators whose *argument is a semantic
judgment*. The operator stays in code; Jev supplies the operand.

| Construct | Jev shape | Preconditions that govern it | Status |
|---|---|---|---|
| argmax | Choice winner | The offered set must contain the right answer; conditional on the set; `other` when coverage is open | **Contract** |
| Expectation (over a defined distribution) | Score fractional score | It's a mean over *your* levels, not a natural quantity; read the full distribution beside it | **Contract** |
| Indicator / predicate application | Noul ≥ threshold | Threshold set on your data; noul has no separate confidence | **Contract** |
| Conditional filter (`if p`) | Noul gate in a policy chain | Filter ≠ authority: validate operation+target in code | **Empirical recipe** |
| Ranking / order statistics over candidates | Shortlist → rerank by Noul/Score | Comparability needs a shared rubric; recall measured separately from rerank | **Empirical recipe** |
| Soft argmax / distributional output | Return the whole distribution, not just the winner | Distribution is over *your* options; absent candidates can never win | **Contract** |

**2. Theorems as system-level guarantees** — the theorem applies to the
*composition* around Jev, and only as far as its preconditions survive.
The preconditions are the acceptance test:

| Theorem | How it enters a Jev system | Precondition that governs | Status |
|---|---|---|---|
| Bayes | Sequential re-scoring: earlier answer → new state → next call. Fine. | Parallel same-state nouls are NOT conditionally independent — no joint posteriors by multiplication | **Contract-adjacent, enforced** |
| Law of large numbers / variance reduction | Self-consistency repeats as a variance-reduction ensemble | Independence must come from *repeats*, not from parallel same-state questions | **Empirical recipe** |
| Jensen's inequality | Using Score expectations inside nonlinear utility: E[X] ≠ f(E[X]) | Compute utility from the returned distribution, not from the single score | **Contract** |
| Markov/stationarity assumptions | State shape in judgment loops (foreman hysteresis) | Jev sees only the state given; history must be folded in by code | **Empirical recipe** |
| Goodhart's law (proxy gaming) | Judge/agent self-reports are proxies | Only post-execution probes concede; claims go to the journal and decide nothing (jev-mcts) | **Empirical recipe** |
| Simpson's paradox / aggregation bias | Pooling Jev decisions across populations | Calibrate and threshold per population segment | **Hypothesis** (unmeasured on Jev) |
| Convergence of iterative refinement | Re-asking the same question until it agrees is not convergence — repeats quantify uncertainty, they don't resolve it | Each repeat must carry NEW evidence/state, or it's the same draw | **Rejected as stated** |

**3. Non-substitutable** — the construct's meaning depends on arithmetic,
derivatives, continuity, or derivation Jev doesn't have. Never map:

| Construct | Why it fails | Where it goes |
|---|---|---|
| Sum/product/count over state content | No counting or arithmetic (jaggedness, dates are text) | Code |
| Derivatives / gradients / smoothness | No continuous function exists to differentiate; only pointwise behavioral perturbation | Perturbation tests (validation.md) |
| Convolution, Fourier, transforms | No analog of the operation itself | Code |
| CLT on Jev outputs | Bounded discrete outputs, correlated across questions; preconditions fail | Design around it, don't claim it |
| Triangle inequality on Score distances | Score levels aren't a metric space | Code-side embeddings if needed |

The general rule: **every theorem carries its preconditions into the design
as code-level checks.** If you can't name the precondition that could
break (independence, monotonicity of rubric levels, in-distribution
calibration), you don't yet have a mapping — you have a metaphor.

## Open rows (test these next; don't cite until measured)

- Kalman-style filtering: predict–update needs state transition math — Jev
  supplies only the observation update as a judgment; the filter stays in
  code. **Hypothesis.**
- Importance sampling / proposal distributions from Choice distributions —
  untested; correlations between options make this risky.
- Program synthesis candidate ranking — fan-out nouls as the ranker, kept
  to shortlists (heuristics→rerank shape). **Hypothesis.**
