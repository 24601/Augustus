# Decision-model review: typed judgments, calibrated risk, and decision objectives

**Review date:** 2026-09-21 (America/Boise)

**Repository reviewed:** baseline Augustus 0.5.1 and the concurrent, unreleased 0.6.0-dev review, including `README.md` and focused references. This report records recommendations; the integration receipt tracks what was adopted.

**External evidence cutoff:** 2026-09-21

**Source policy:** primary papers, official documentation, and official project repositories only. X/Twitter and secondary market/adoption summaries were excluded.
**Change scope:** research report only. No existing skill, reference, script, or product documentation was edited.

This is deliberately **not a universal SOTA leaderboard**. It samples primary work that changes how Augustus should place or validate a decision boundary. Model-family inclusion means “architecturally relevant candidate,” not “best model,” broad adoption, or production endorsement. No external work published after the cutoff was included; the two 2026 conformal preprints are explicitly marked research watch.

## Evidence labels used here

- **Finding** — directly supported by a repository artifact or a cited primary/official source.
- **Inference** — synthesis across findings; plausible and useful, but not itself a result reported by one source.
- **Hypothesis** — an expected result that Augustus has not tested.
- **Unrun experiment** — a proposed comparison or acceptance test; it is not evidence of current capability.
- **Vendor claim** — an official provider statement that was verified as current but not independently reproduced here.
- **Research watch** — a recent preprint or early result that is relevant but not mature enough to become a default architectural promise.

Local hourly artifacts dated 2026-09-22 were not used as evidence because they are later than this review's local-date cutoff. External sources dated through 2026-09-21 were eligible. All URLs in the source register were accessed on 2026-09-21 unless a more specific version date is stated.

## Executive conclusion

Augustus's central separation is sound: exact work belongs in code; a model should supply a narrow semantic judgment; policy should own thresholds, permissions, and action; generation should be reserved for writing. The durable improvement is to stop treating “typed output” or a model-provided confidence as sufficient evidence of calibration or safe action.

The recommended invariant is:

> A decision model is a **versioned semantic estimator**. Its output schema defines shape; held-out evidence measures probability meaning and selective risk; explicit policy and accountable owners retain action authority.

That implies four separate contracts for every model-backed boundary:

1. **Task contract:** what is being predicted — class, independent property, span, order, score level, outcome, or action value?
2. **Score contract:** what does each number mean — class probability, affinity, distribution concentration, rank score, expected ordinal level, conformity score, or estimated utility?
3. **Risk contract:** what is empirically or statistically controlled — proper score, calibration gap, accepted-case risk, coverage, conformal expected loss, or nothing beyond a point estimate?
4. **Authority contract:** which actions code may take at which measured operating point, and what abstention or escalation path remains?
5. **Runtime-state contract:** whether the estimator is a memory-free/stateless function of explicit request state, or whether it depends on session history, retrieval state, recurrence, or an evolving policy.

The strongest near-term path is not to choose one universal “decision model.” It is to maintain a small family map, require the same evidence passport for each family, and promote a specialist only when it beats simple baselines on the decision metric that matters.

## 1. What the current Augustus framing gets right

### Findings

- The repository already distinguishes `decide`, `locate`, `categorize`, `rank`, and `perceive`. That is more useful than grouping every bounded output under “classification.”
- It correctly keeps deterministic rules, arithmetic, normalization, permissions, and side effects in code.
- It treats a listwise rank score as an ordering signal rather than a calibrated permission gate.
- It recognizes that a Choice answer is conditional on the offered alternatives and that `other` or `no_match` may be required.
- It treats a Noul value near 0.5 as uncertainty rather than a “medium” class.
- It requires shadow evaluation before a model gains gate authority, and it already calls for option-order, paraphrase, distractor, and missing-evidence tests.

### Gaps to close

1. **Calibration is sometimes too close to a model-family property.** It should be a measured relationship between a pinned model/question/version and a deployment distribution.
2. **ECE has too much implied authority.** ECE is a useful visualization/diagnostic only when its binning and uncertainty are reported. It should not be the sole promotion or recalibration objective.
3. **Conformal methods need an assumptions card.** “Distribution-free” does not mean assumption-free, per-instance, shift-proof, or action-conditional.
4. **Typed and structured outputs are occasionally conflated with semantic reliability.** Schema validity, correct semantics, probability calibration, selective risk, and decision utility are separate tests.
5. **Predictive classification and decision learning need a hard boundary.** Predicting an outcome, optimizing an action under costs, and estimating the causal effect of taking an action are different statistical tasks.
6. **Tabular decisions are underrepresented.** When the state is already a row of stable features with labels, a classical tabular model or a tabular foundation model is a first-class candidate, not an afterthought to a text model.
7. **Routing needs policy evaluation.** A router score chooses which estimator to call; it does not inherit permission to act from the chosen estimator.
8. **Versioned evidence needs to be first-class.** Current examples include moving TypeSafe aliases, rapidly changing GLiClass/GLiNER packages, and a TabPFN paper whose evaluated model and limits differ substantially from the current default release.

## 2. Verified current TypeSafe/Jev contract

The official TypeSafe skill tag `v0.5.7` points to commit `65a39f393687675ce170e6094757de20370365b9`. The skill itself directs integrators to the live documentation as the source of truth. The following is the observable contract on the review date, not an independent performance certification.

| Surface | Verified official contract | Architectural consequence |
| --- | --- | --- |
| Model identity | `jev-latest` and `jev-preview` both resolve to `jev-1.13.0` on this date. The response reports the resolved model. | Log the resolved ID. Pin it for thresholded production use and requalify before moving aliases. |
| Input | Text only; state may be a string, JSON object, or array of text values. No native image, audio, or video input. | Perception/transcription is a separate stage with separate error accounting. |
| Context | 64k tokens for the request; 32k for state plus the longest question. | The hard limit is not an accuracy guarantee. Retrieve/filter first because the official jaggedness guide also reports context distraction. |
| Choice | A distribution over up to 255 supplied alternatives. Missing alternatives cannot be selected. | Treat it as conditional choice within a supplied set; include `other`/`no_match` when semantically valid and perturb the option set during testing. |
| Score | A distribution over 2–10 ordered levels plus derived values. | The expectation is ordinal interpolation, not a natural-unit measurement. The official jaggedness guide says score levels are weak in numerical calibration. |
| Noul | Probability-like support for the affirmative proposition. It has no separate confidence field. | One Noul per overlapping property is valid, but separate questions do not obey complement identities. Calibrate thresholds per exact question. |
| Choice/Score confidence | Derived from concentration of the returned distribution. | This is not documented as probability that the answer is correct. Evaluate it as a selective score before using it to automate. |
| Question execution | Questions in one request are evaluated independently against the same state and cannot see each other's answers. | Dependencies and invariants belong in code or separate stages; batching does not create a reasoning chain. |
| Customization | Same weights serve accounts; behavior is shaped through state, instructions, and criteria, not customer LoRA/fine-tuning. | A domain integration is a versioned question-and-policy artifact, not merely a model name. |
| Language | English is the primary and best-supported language; other languages are uneven. | Non-English deployment requires its own evaluation slices and thresholds. |

### Current official limitations

The `jev-1.13` jaggedness page was last reviewed 2026-09-17. It explicitly identifies literal reading, unreliable counting and arithmetic, date/time comparison, indirection, irrelevant context, adversarial state, contradictory instructions/criteria, absent structural invariants across separately worded questions, weak numerical calibration of Score levels, and lack of text generation.

These limitations strongly support Augustus's existing placement rules. They also add two important qualifications:

- **Finding:** `P(noul)` and `1 - P(not_noul)` are not promised to sum to one, and a Noul threshold should not be transferred to an equivalent-looking Choice.
- **Finding:** the official documentation calls Jev “calibrated” and says it is trained with RLCD for calibrated decisions. The public pages reviewed here do not disclose the training objective, calibration protocol, datasets, confidence intervals, subgroup results, or an independent validation.
- **Inference:** Augustus should describe the RLCD/calibration statement as a verified **vendor training claim**, while treating calibration on an Augustus workload as an unverified property until measured.

No conclusion in this report compares Jev's quality or adoption with another model; there is no public evidence here to support such a superiority claim.

### Memory-free, low-latency judgment is a placement axis, not a paper result

The official State documentation describes each request as one explicit state evaluated against one or more independent questions. Augustus should preserve that request-local shape at narrow judgment boundaries: all decision-relevant state should be inspectable in the call or in a versioned feature record, not hidden in prior chat/session turns.

This is a design definition of **memory-free/stateless judgment**, not a claim that a provider retains no operational data and not a latency benchmark. It has two benefits when the task permits it: cases can be evaluated independently, and the workflow can reproduce a judgment from its receipt. It also has a limit: if history changes the estimand, code must summarize or retrieve that history explicitly rather than pretending the decision is memoryless.

Low latency is likewise an empirical deployment property. Measure warm and cold p50/p95/p99 latency, batching, queueing, retries, serialization, and fallback on the target traffic and hardware. A compact encoder or per-request decision API is a **candidate** for a low-latency stage; parameter count, advertised rate limits, or author-reported single-GPU throughput do not establish the cascade's latency.

## 3. Model families: task shape first, model brand second

The following family map is more durable than a catalog of model names.

| Family | Output semantics | Good default use | Not established by the interface | Required baseline/evaluation |
| --- | --- | --- | --- | --- |
| Exact rule/parser/solver | Deterministic value or proof obligation | Arithmetic, dates, permissions, schema, lookup, normalization, constraints | Semantic ambiguity handling | Unit/property tests and oracle cases |
| Closed decision API (for example Jev) | Bounded Choice, independent binary proposition, or ordered-level distribution | Narrow semantic judgments over rich text where criteria can be stated | Correctness probability, transfer calibration, causal effect, or action permission | Exact/prompt baseline; NLL/Brier where labels permit; risk-coverage; perturbation and drift slices |
| Task-specific classifier | Probability/logit over a fixed learned label space | Stable repeated taxonomy with enough labeled examples | Validity outside training distribution | Majority/rule/linear/tree baselines; proper scores; per-class and OOD slices |
| Label-conditioned sequence classifier (GLiClass) | Scores candidate labels jointly with text; single- or multi-label modes | Dynamic or large human-readable taxonomies; zero/few-shot shortlist | Cross-domain calibration or correctness of arbitrary labels | NLI cross-encoder, embedding, fine-tuned classifier, and closed decision API where eligible |
| Label-conditioned span extractor (GLiNER) | Labeled spans and scores | Locate names, concepts, or evidence spans with open label descriptions | Document-level categorization, calibrated action probability, or proof that extracted text entails a claim | Regex/parser and task NER baseline; exact/span F1 and boundary errors |
| Ranker/reranker | Relative score/order, often query-candidate affinity | Retrieval, shortlist construction, prioritization | Absolute threshold meaning or probability of correctness | BM25/vector/order baselines; NDCG/MRR/pairwise measures; downstream recall |
| Tabular learner (linear/tree/TabPFN) | Class probability or regression distribution from labeled feature rows | Repeated decisions with stable structured features and enough representative rows | Text understanding, causal effect, or robustness beyond the training support | Logistic/linear model, CatBoost/XGBoost/random forest; proper scores and temporal/group splits |
| Predict-then-optimize / decision-focused learner | Prediction or learned objective optimized for downstream decision loss | Known optimization problem, labeled outcomes/cost coefficients, measurable regret | Causal validity or safe deployment under unobserved shift | Two-stage prediction baseline; oracle regret; constraint violations; stress tests |
| Causal policy learner | Estimated value/effect of assigning actions under explicit identification assumptions | Actions change outcomes and logged/experimental data support policy evaluation | Identification under unmeasured confounding or no overlap | Current policy, randomized trial if possible, doubly robust/off-policy intervals, sensitivity analysis |
| Selective/conformal wrapper | Abstention decision, prediction set, or threshold with a scoped risk/coverage guarantee | Holding out uncertain cases; controlling a specified loss under stated assumptions | Per-instance correctness, automatic conditional/group guarantees, or shift immunity | Plain thresholding; risk-coverage; coverage/size; assumption and shift audits |
| Generator | Text/code/media sequence | Writing, explanation, transformation, open-ended synthesis | Stable bounded choice or calibrated confidence | Task-specific execution/factual/human review metrics |

### GLiNER and GLiClass are not interchangeable

**GLiNER finding:** the paper defines a compact bidirectional encoder for named-entity recognition that extracts arbitrary label-conditioned spans in parallel. This is a `locate` family. The current official release on the cutoff date is `v0.2.29` (2026-09-08).

**GLiClass finding:** the 2025 paper adapts the GLiNER idea to sequence classification, jointly processing text and labels so all labels can be handled in one forward pass. The paper reports task F1 and single-GPU throughput, and explicitly lists calibration variation across datasets, extreme label/text-length sensitivity, and fine-grained taxonomy variability as limitations. The current official package release on the cutoff date is `v0.1.20` (2026-07-21), later than the paper.

**Inference:** GLiNER belongs under `locate`; GLiClass belongs under `categorize`. Their scores should be called `score` or `affinity` until a held-out study establishes probability semantics for the exact checkpoint, label descriptions, label set, class balance, and deployment slice. A library default threshold is configuration, not evidence of calibration.

### TabPFN is relevant, with a strict evidence/version boundary

The peer-reviewed Nature paper (version of record 2025-01-08) evaluates TabPFN on tabular classification and regression, focusing on datasets up to 10,000 samples, 500 features, and ten classes, with accuracy/ROC-AUC or regression metrics and comparisons to tree, linear, SVM, and neural baselines. The paper also says CatBoost or XGBoost can be preferable for larger or highly non-smooth regression data.

The official repository has since moved much further. Release `v9.0.0` was published 2026-09-15, uses TabPFN-3.5 by default, and documents much larger accepted input limits. The code is Apache-2.0, but the current 2.5/2.6/3/3.5 model weights are non-commercial; the v2 weights have a distinct license. The repository also distinguishes GPU capacity from much lower practical CPU guidance.

**Finding:** current package capability and licensing are not the same evidence object as the Nature evaluation.

**Inference:** Augustus should treat “TabPFN Nature-v2 result,” “current TabPFN checkpoint,” and “current package/runtime” as three versioned records. The Nature headline must not be projected onto v3.5, one-million-row workloads, commercial availability, probability calibration, or a specific Augustus dataset.

**Recommendation:** add a `tabular` family. Begin with logistic regression and a strong tree model. Consider a pinned TabPFN checkpoint only after license review and only as an unrun candidate with a version-specific benchmark.

## 4. Calibration, selectivity, and conformal control answer different questions

### 4.1 A typed response is not a probability guarantee

The following properties are independent:

- **Schema validity:** the response can be parsed and contains an allowed answer.
- **Discrimination:** correct cases tend to receive better scores than incorrect cases.
- **Calibration:** among predictions assigned probability `p`, the relevant outcome occurs at approximately frequency `p`, under a stated conditioning notion and distribution.
- **Sharpness/refinement:** predictions are informative rather than all collapsing toward the base rate.
- **Selective performance:** cases accepted above a score threshold have acceptable risk at useful coverage.
- **Conformal risk/coverage:** a particular wrapper controls a specified marginal/expected risk under its assumptions.
- **Decision utility:** the resulting action minimizes expected cost or regret under an explicit loss and constraints.

An API can guarantee the first property without guaranteeing any of the others.

### 4.2 ECE is a diagnostic, not the promotion gate

Chidambaram and Ge (ICLR 2025) show that trivial recalibration can look excellent on common calibration metrics while making general predictive quality worse; they recommend reporting proper-score/generalization measures such as negative log-likelihood alongside calibration measures. Their example is especially relevant to Augustus: optimizing one binned calibration number can reward uninformative probabilities.

**Recommended minimum probability report:**

| Question | Metric | Notes |
| --- | --- | --- |
| Are the full probabilities useful and honest? | Multiclass/binary negative log-likelihood and Brier score | Strictly proper scores; report lower-is-better and uncertainty intervals. Clip only for numerical reporting and disclose the rule. |
| Is calibration visibly wrong? | Reliability diagram plus ECE/ACE or a smooth estimator | State bins/kernel, sample count, and interval. Never report ECE alone. |
| Does the score order mistakes usefully? | AUROC/AUPRC for error or correctness where meaningful | Ranking/discrimination is not calibration. AUPRC must be read against base rate. |
| Can the system abstain safely? | Risk-coverage curve, AURC, coverage at predeclared risk, risk at predeclared coverage | Report the whole operating curve and chosen point, not just a confidence histogram. |
| Does the policy improve outcomes? | Expected cost/utility, regret to baseline/oracle, constraint violations | Use the real asymmetric action costs, including review and abstention. |
| Is performance stable? | Per-class, group, temporal, source, language, ambiguity, OOD, and perturbation slices with intervals | Aggregate calibration can hide the slice that receives the harmful action. |

ECE remains useful for communication, but it should be labeled with binning choices and uncertainty. It is neither a proper scoring rule nor a sufficient test of a confidence-based automation policy.

### 4.3 Selective prediction is an operating curve

A selective model has two outputs in effect: a prediction and a decision to accept or abstain. Its central object is the risk-coverage curve:

- at 100% coverage, it behaves like the base predictor;
- decreasing coverage should ideally remove higher-risk cases first;
- AURC summarizes the curve, while a production gate uses a predeclared operating point;
- the abstention path has its own latency, monetary, and human-error costs.

The 2025 ICML AURC paper gives a population formulation and analyzes finite-sample plug-in estimators. This supports using AURC for model comparison, but Augustus should still report the actual deployment point: `coverage at target risk` and `risk at target coverage` with intervals.

Distribution shift matters. The 2024 TMLR work on generalized selective classification evaluates in-distribution, covariate-shifted, label-shifted, and OOD cases and shows why a confidence score that works in one regime need not retain useful risk ordering in another. Therefore:

> A threshold is a property of `(model version, question/feature contract, calibrator, action, deployment slice, time window)`, not a universal constant.

### 4.4 Conformal risk control requires an assumptions card

The current Conformal Risk Control paper (arXiv v4, 2025-06-13; originally ICLR 2024) controls the expected value of a bounded loss that becomes no worse as a conservativeness parameter increases. Its proof uses exchangeability of the calibration and future loss functions; its principal bound is marginal/expected over the calibration and test draws. It explicitly shows that the basic procedure can fail arbitrarily for a non-monotone loss.

For every proposed conformal wrapper, record:

1. **Exchangeable unit:** what exactly is assumed exchangeable — records, users, sessions, documents, or time blocks?
2. **Calibration split:** is it untouched by model, prompt, label-description, threshold, and route selection?
3. **Nested output family:** what parameter makes outputs monotonically more conservative?
4. **Loss:** is it bounded, correctly observed, and monotone in that parameter?
5. **Guarantee:** marginal coverage, expected loss, high-probability/PAC risk, group-conditional, or action-conditional?
6. **Selection:** did a router, filter, subgroup rule, or human choice select the test subset after calibration?
7. **Shift:** what detects temporal, source, prevalence, or policy-induced shift, and what invalidates the certificate?
8. **Recalibration cadence:** what effective sample size and freshness are required before authority resumes?

What ordinary CRC does **not** establish:

- probability that this individual prediction is correct;
- conditional risk for every subgroup or score value;
- validity after arbitrary adaptive selection or routing;
- validity under unconstrained distribution shift;
- action-conditional safety when the action itself changes which outcomes are observed.

**Research watch:** Selective Conformal Risk Control (preprint v2, 2026-04-27) explicitly addresses selection followed by conformalization. Its transductive variant computes thresholds jointly with calibration and test samples to preserve exchangeability; its calibration-only variant gives PAC-style guarantees. This is directly relevant to Augustus routing but is not yet a default drop-in.

**Research watch:** Conformal Risk-Averse Decision Making with Action Conditional Guarantee (preprint v2, 2026-06-09) targets the gap between marginal conformal safety and guarantees conditioned on each selected action. It is conceptually important for action gates, but it is a recent preprint evaluated on two datasets, not a reason to claim action-conditional guarantees today.

## 5. Classification, decision-focused learning, and causal policy learning

These tasks can share an encoder while asking fundamentally different questions.

| Task | Estimand/objective | Required data | Typical failure if treated as ordinary classification |
| --- | --- | --- | --- |
| Predictive classification | `P(Y | X)` or a decision boundary for an observed label | Representative labeled `(X,Y)` pairs | High accuracy can still produce bad actions under asymmetric costs or shift. |
| Cost-sensitive classification | Action minimizing expected known misclassification cost from predictive probabilities | Labels plus explicit cost matrix | A default argmax ignores the action's asymmetric harm and abstention cost. |
| Predict-then-optimize | Predict uncertain coefficients/outcomes, then solve a known optimization problem | Context, realized uncertain quantities, decision constraints | Small coefficient errors can create large regret near optimizer discontinuities. |
| Decision-focused learning | Train the predictor/objective for downstream decision loss or regret | Same as above plus a differentiable/surrogate optimization path | Better prediction metric need not mean better decision; learned objective can overfit the decision distribution. |
| Causal policy learning | Value/effect of assigning action `a`, for example `E[Y(a) | X]`, under identification assumptions | Logged actions, outcomes, propensities/confounders or randomized data | `P(Y | X,A=a)` from observational data can encode selection rather than intervention effect. |
| Contextual bandit/RL | Sequential policy value under exploration and state transitions | Logged propensities or online exploration, rewards, state/action histories | Static labels ignore feedback, delayed effects, and support/overlap. |

### Decision-focused learning

The 2025 UAI `DF²` paper is a recent example of decision-focused learning. It identifies model-mismatch, sample-average-approximation, and gradient-approximation errors in probabilistic predict-then-optimize systems, and directly learns an expected optimization function in its proposed method. Its experiments cover two synthetic and three real problems.

**Finding:** this is evidence that “classification quality” and “decision quality” can require different training objectives.

**Inference:** decision-focused learning should be a separate Augustus family, not another synonym for classification. It becomes relevant only when the optimization problem, constraints, outcome labels, and regret metric are concrete. A paper's term “distribution-free” must not be generalized into assumption-free production safety.

### Causal decision models

Athey and Wager's policy-learning work is a durable reference point: it learns constrained treatment-assignment policies from observational data using doubly robust causal-effect estimates and evaluates policy regret. It requires a strategy that identifies causal effects; it does not obtain intervention validity from a classifier alone.

**Hard boundary for Augustus:** if the contemplated action changes the outcome being predicted, ask whether the product needs a predictive decision or an interventional policy.

- “Will this account churn?” is predictive.
- “Should we send this offer to reduce churn?” is causal/policy-oriented because treatment assignment changes the observed outcome and historical assignment is confounded by past policy.
- “Which offer maximizes expected retained revenue under budget and fairness constraints?” additionally introduces optimization and explicit policy constraints.

When there is no defensible identification design, the safe role of a typed judgment is advisory/routing/shadow evidence—not a claim about the effect of acting.

## 6. Routing and small specialists

### Routing is a decision policy

RouteLLM (ICLR 2025) learns to route between stronger and weaker language models from preference data and evaluates a cost-quality tradeoff. It is useful evidence that learned routing is a distinct optimization surface, not evidence that an arbitrary router generalizes to an Augustus task or model pool.

An Augustus router should be evaluated on:

- final task quality, not router label accuracy alone;
- total cost, including router, fallback, retries, review, and downstream failures;
- end-to-end latency and tail latency;
- coverage of each route and capacity/availability failures;
- regret relative to always-small, always-large, deterministic rules, and an offline oracle;
- stability under new model versions, pricing, prompt changes, and traffic mix;
- safety/quality slices for each routed action;
- whether routing or filtering invalidates a downstream conformal guarantee.

If routing is learned from logged production choices, record propensities or randomize an ethically safe traffic slice. Otherwise, apparent quality differences may reflect the old router's selection. This is an inference from policy-learning requirements, not a completed Augustus experiment.

### Cascades change the population seen by every later stage

A first-stage accept/reject rule induces a selected distribution. The specialist sees the broad incoming population, while the fallback sees the residual hard cases. Consequently:

- report calibration and accepted-case risk conditional on each route, not only on the original aggregate population;
- fit or validate a calibrator for the exact `(route, downstream model version, representation, traffic window)` when sample size permits;
- evaluate the fallback on the residual cases it will actually receive, not only on an IID full-task benchmark;
- do not multiply stage confidences as if they were independent probabilities;
- include false early acceptance, false escalation, fallback failure, and recovery in final cascade loss;
- treat a route or threshold change as distribution shift for later-stage calibration and conformal assumptions.

An aggregate calibration curve can hide cancellation between an overconfident early-accept route and an underconfident fallback route. “Calibrated before routing” therefore does not imply “calibrated conditional on route,” and route-conditional calibration still does not by itself prove action-conditional safety.

### Promotion gate for a small specialist

A small classifier, GLiClass/GLiNER checkpoint, tabular model, or router should gain traffic only if all of the following are true:

1. It beats a simple exact or classical baseline on the primary decision metric with a predeclared practical margin and uncertainty interval.
2. It preserves protected/high-cost slice constraints.
3. Its probability or selective score is calibrated on the actual runtime representation; otherwise the score remains non-authoritative.
4. It survives label-description, option-order, distractor, paraphrase, missing-evidence, and temporal/source-shift tests appropriate to its family.
5. Its artifact, preprocessing, label map, threshold/calibrator, dependency version, hardware precision, and license are pinned.
6. It has an abstention/fallback path and a rollback trigger.
7. Shadow logs show end-to-end improvement before it receives action authority.

“Small” is a deployment property, not a quality claim. Latency, memory, throughput, calibration, and error costs must be measured on the target hardware and traffic.

## 7. Evaluation contract for reliable claims

### 7.1 Split responsibilities

- **Train split:** fit weights/features only.
- **Development split:** prompt, architecture, features, label descriptions, and model selection.
- **Calibration split:** fit temperature/isotonic/other calibrator, selective threshold, or conformal threshold after all upstream choices are frozen.
- **Locked test split:** one final estimate of the complete frozen pipeline and policy.
- **Shadow/temporal set:** detect operational shift; it is not a substitute for the locked test.

When data are grouped by customer, document, conversation, incident, or time, split at that unit. Record-level random splitting can leak near-duplicates and make intervals too narrow.

NeurIPS 2024 work questioning cross-validation as a universal gold standard is a useful caution: repeated folds are not automatically more reliable proof of out-of-sample performance. Use cross-validation for development when appropriate, but retain a locked, deployment-shaped evaluation and quantify uncertainty at the independent sampling unit.

### 7.2 Metrics by output family

| Family | Primary measures | Required stress measures |
| --- | --- | --- |
| Choice/single-label | Accuracy or cost-weighted error, macro-F1/per-class recall, NLL, multiclass Brier | Option order, added irrelevant option, removed true option, `other/no_match`, label wording, class/source/time slices |
| Noul/multi-label | Per-label precision/recall/F1, micro/macro summaries, binary NLL/Brier per label | All-low/all-high cases, co-occurrence, negation, prevalence shift, question paraphrase, separate-question inconsistency |
| Score/ordinal | Ordinal cost, ranked probability score, per-level confusion, downstream decision cost | Level description/order, monotonic policy behavior, edge levels, no claim of physical units |
| Locate/spans | Exact and overlap span F1, label F1, boundary error, empty-document/no-match | Nested/overlapping entities, repeated strings, long context, adversarial label descriptions, evidence entailment checked separately |
| Rank | NDCG, MRR, recall@k, pairwise accuracy, downstream answer/decision recall | Candidate-set shift, duplicate/near-duplicate items, score-scale drift, latency at k |
| Selective gate | Full risk-coverage curve, AURC, coverage at target risk, risk at target coverage, abstention cost | Group/source/time curves, shift, threshold interval, fallback quality/load |
| Conformal set/risk | Empirical coverage or specified loss, set size/usefulness, repeated calibration draws | Exchangeability/selection audit, conditional/group diagnostics, shift invalidation, loss monotonicity |
| Optimizer/policy | Realized utility/cost, regret, constraint violations, value interval | Coefficient perturbation, optimizer discontinuities, support/overlap, confounding sensitivity, policy-induced shift |
| Router | Quality-cost/latency frontier, route mix, regret to baselines/oracle | New candidate model/version, OOD traffic, router overhead, capacity failure, downstream certificate validity |

### 7.3 Reliability requirements

Every published comparison should include:

- sample counts and base rates overall and by material slice;
- an uncertainty interval, preferably paired across systems on the same cases;
- bootstrap/resampling at the independent group unit when records are clustered;
- repeated seeds for stochastic training/inference and explicit deterministic settings where available;
- data lineage, deduplication, contamination checks, and label adjudication notes;
- disagreement/ambiguity labels rather than forced certainty where humans do not agree;
- the exact model/checkpoint/resolved provider version, prompt/question hash, label-set hash, preprocessing version, calibrator, threshold, hardware/precision, and date window;
- both statistical and predeclared practical significance;
- correction or explicit caution when many models, prompts, slices, and thresholds were searched;
- no reuse of the locked test set to rewrite criteria or retune thresholds.

A single aggregate accuracy, F1, ECE, or “confidence” value is not sufficient evidence for authority.

### 7.4 Probability passport

Add a small sidecar record for every numeric model output used by policy:

```yaml
score_contract:
  task_id: refund_request_present
  output_family: noul
  model_id: jev-1.13.0
  question_hash: sha256:...
  state_schema_version: ticket-v4
  population: english_support_tickets
  evaluation_window: 2026-Q3
  semantic_meaning: support_for_affirmative_proposition
  not_claimed: probability_of_correctness
  calibrator: none
  threshold_action: review_if_below_0.82
  threshold_tuned_on: calibration-set-id
  primary_metrics: [log_loss, brier, risk_at_coverage, coverage_at_risk]
  slices: [locale, source, issue_family, ambiguity]
  expiry_or_recheck: 2026-10-15
```

The exact fields can change; the durable idea is that a bare float never carries action authority without its evidence context.

## 8. Concrete proposed changes to Augustus

These are proposals for the parent integration. They were not applied in this task.

| Priority | Proposed change | Destination | Concrete acceptance condition |
| --- | --- | --- | --- |
| P0 | Replace unqualified “calibrated decision model” language with “typed semantic estimator; calibration is model/question/population evidence.” Preserve the official Jev RLCD wording as a vendor claim. | Skill overview, `mental-models.md`, `validation.md` | No interface field is described as correctness probability without a measured contract. |
| P0 | Add the five-contract review: task, score, risk, authority, runtime state. | Skill activation/design checklist | Every model placement can answer all five or is explicitly marked exploratory. |
| P0 | Replace ECE-only validation with the probability/selective matrix: NLL, Brier, reliability/ECE with method, risk-coverage/AURC, operating-point risk/coverage, action cost/regret, slices, intervals. | `validation.md` | Promotion templates require proper scores and operating curves; ECE alone cannot pass. |
| P0 | Add a conformal assumptions card and distinguish marginal, expected, PAC, group-conditional, and action-conditional guarantees. | `mental-models.md`, `validation.md` | Any “guarantee” statement names unit, split, loss, assumptions, conditioning, and invalidation condition. |
| P0 | Add explicit `tabular`, `decision-focused`, and `causal-policy` families alongside decide/locate/categorize/rank/perceive. | `judgment-class.md` | A predictive classifier is never proposed as evidence of action effect without an identification design. |
| P0 | Separate structured output validity from semantic/calibration claims. | `judgment-class.md`, `mixed-architecture.md` | GLiNER remains Locate; GLiClass remains Categorize; neither score is called probability until tested. |
| P0 | Require resolved model/checkpoint and question/label-set hashes in decision receipts. | `validation.md`, integration templates | Moving aliases or label changes automatically make prior thresholds stale. |
| P1 | Add the probability passport sidecar. | Validation receipts/tooling | Every policy-consumed score has semantic meaning, population, metrics, calibrator, threshold, and recheck date. |
| P1 | Add routing as its own policy family with a cost-quality frontier and logged-selection requirements. | `mixed-architecture.md` | Router evaluation includes overhead, route mix, end-to-end result, baselines/oracle, and certificate interaction. |
| P1 | Add route-conditional calibration and residual-population evaluation to cascade acceptance. | `validation.md`, `mixed-architecture.md` | Each later stage is evaluated on the selected population it actually receives; aggregate calibration alone cannot pass. |
| P1 | Add a specialist promotion/rollback checklist including license and target-hardware measurements. | `validation.md` | No local model receives traffic based only on paper results or library defaults. |
| P1 | Make `other/no_match/insufficient_evidence` design mandatory when the ontology is not exhaustive. | Question-design/validation guidance | Missing-answer and irrelevant-option perturbations are in the behavioral suite. |
| P2 | Add a research-watch appendix for selective CRC and action-conditional conformal methods. | Research references only | Clearly marked preprint/unrun; no production guarantee implied. |

## 9. Findings, hypotheses, and unrun experiments

### Findings

1. The current Jev contract is narrower and more explicit than a generic classifier: typed questions, versioned IDs, parallel independent evaluation, and documented jaggedness. Its confidence field is not an advertised correctness probability.
2. TypeSafe's “calibrated/RLCD” wording is verifiably current official documentation, but its independent calibration quality and training objective are not publicly established by the materials reviewed.
3. Common calibration metrics can be made to look excellent while proper predictive scores worsen. ECE cannot carry the validation burden alone.
4. Selective risk is about the ordering of errors and the chosen coverage point, not merely probability calibration.
5. Ordinary conformal/CRC guarantees are scoped by exchangeability, split integrity, loss form, and conditioning. Selection, routing, action conditioning, and shift require separate treatment.
6. GLiNER is a span extractor and GLiClass a sequence classifier. The GLiClass paper itself reports cross-dataset calibration variation as a limitation.
7. TabPFN is a relevant tabular candidate, but the peer-reviewed v2-era results, current v3.5 checkpoint claims, runtime limits, and licenses must not be blended.
8. Decision-focused learning optimizes a downstream decision objective; causal policy learning additionally requires causal identification. Neither is merely “better classification.”
9. Learned routing is a policy with end-to-end cost and quality. Router confidence does not confer action authority.

### Hypotheses

1. A GLiClass-sized specialist may beat a closed decision API on latency/cost for a stable taxonomy after task-specific calibration, but will lose robustness when label descriptions or domain prevalence drift.
2. Jev Choice may produce a stronger ranking over a small mutually exclusive candidate set than independent Nouls, while independent Nouls may reject all options more naturally; a two-stage Choice-plus-absolute-gate could outperform either alone.
3. For repeated operational decisions represented by clean structured features, a calibrated tree/linear model or TabPFN candidate may outperform text serialization into a decision API.
4. Proper-score optimization plus a separately chosen selective threshold will be more reliable than directly minimizing ECE.
5. Routing a narrow specialist first and escalating low-score/OOD cases can improve the quality-cost frontier, but only if router overhead and selection bias do not consume the benefit.
6. Marginal conformal control may hide unacceptable action- or group-conditional risk; action-conditional methods may reduce that gap at the cost of data and wider/more conservative outputs.

None of these hypotheses is a current Augustus capability claim.

### Unrun experiments

| ID | Experiment | Frozen comparison | Primary outcome | Failure/stop condition |
| --- | --- | --- | --- | --- |
| E1 | Typed-family bake-off on 3–5 real narrow judgments | Exact/rule baseline, Jev pinned ID, GLiClass pinned checkpoint, task-specific linear/encoder where labels allow | Decision cost plus NLL/Brier and risk-coverage | Stop if labels/criteria are not independently auditable or the ontology is still changing. |
| E2 | Jev primitive semantics | Same proposition as Choice, Noul, and decomposed Nouls; fixed state | Per-form proper scores, risk-coverage, cross-form disagreement | Do not transfer thresholds between forms even if averages look similar. |
| E3 | Choice-set perturbation | Original, option order shuffle, irrelevant option, paraphrased labels, removed true option, explicit no-match | Regret and probability/choice stability | Any harmful action without a valid offered option blocks authority. |
| E4 | GLiClass runtime calibration | Current/pinned edge and base checkpoints; raw score, temperature scaling, isotonic where sample size permits | Held-out NLL/Brier and accepted-case risk | Reject calibrator if it improves ECE while degrading proper scores or action cost. |
| E5 | GLiNER evidence locator | Regex/parser, GLiNER pinned checkpoint, generative extractor if policy permits | Exact/overlap span F1 and downstream evidence-verification recall | Extraction score may not substitute for entailment or source validity. |
| E6 | Tabular decision track | Logistic regression, CatBoost/XGBoost, pinned licensed TabPFN checkpoint if approved | Temporal held-out cost, NLL/Brier, latency/memory | No TabPFN run before license/checkpoint approval; paper result is not a pass. |
| E7 | Selective threshold study | Raw confidence/entropy/margin/calibrated probability on same frozen model | Full risk-coverage/AURC; coverage at fixed risk by slice | Block if the selected operating point's interval crosses the harm budget. |
| E8 | Conformal wrapper audit | Ordinary threshold, split conformal/CRC on a suitable monotone loss | Empirical repeated-split risk/coverage and set usefulness | Abort guarantee language if exchangeability unit, monotone loss, or untouched calibration set cannot be defended. |
| E9 | Shift and selection break test | IID test, temporal/source/prevalence shift, router-selected subset | Delta in proper scores, selective risk, conformal coverage/risk | Any certificate must be invalidated rather than silently reused after failed shift checks. |
| E10 | Router frontier and conditional calibration | Always-small, always-large, deterministic rule, learned router, offline oracle | Paired final quality vs total cost and p95 latency; calibration/risk within every route and on the fallback residual | Reject if router overhead, selection-induced miscalibration, failure recovery, or slice harm erases the practical margin. |
| E11 | Decision-focused pilot | Two-stage predictor+optimizer vs a decision-focused method on one explicit optimization problem | Out-of-sample regret and constraint violations | Do not proceed without a stable utility function and realizable outcome labels. |
| E12 | Causal action audit | Predictive action heuristic vs current policy and a causal/off-policy estimator where identified | Policy value interval, overlap, sensitivity | No causal claim if propensities/confounders/support are unavailable; remain advisory/shadow. |
| E13 | Version drift canary | Pinned model against next version/alias on locked canary set | Paired decision/cost/proper-score changes and threshold requalification | Alias/version change cannot inherit production threshold automatically. |

## 10. Durable decision path

For a new Augustus boundary, use this order:

1. **Define the action and loss first.** Include false-positive, false-negative, abstention/review, latency, and capacity costs.
2. **Remove exact work.** Parse, calculate, constrain, and authorize in code.
3. **Choose the output family.** Proposition, exclusive choice, multi-label category, span, rank, ordinal level, tabular outcome, optimized decision, or causal policy.
4. **Build simple baselines.** Rules, majority/base rate, logistic/linear, tree, BM25/vector, or always-small/always-large routing.
5. **Pin the complete estimator.** Model/checkpoint, prompt/question, labels/options, preprocessing, state schema, dependency, hardware precision, and license.
6. **Evaluate prediction quality with proper metrics.** Add family-specific task metrics, proper scores where probabilities exist, and uncertainty intervals.
7. **Evaluate selectivity separately.** Plot risk-coverage; choose an operating point from action cost and a held-out calibration split.
8. **Use conformal control only when its assumptions and guarantee match the need.** Record the assumptions card and invalidation rules.
9. **Escalate to decision-focused or causal methods only when the objective and data justify them.** Do not use vocabulary as a substitute for an estimand.
10. **Shadow, then grant bounded authority.** Log receipts, monitor slices and shift, and requalify on any material version or contract change.

This path preserves Augustus's core taste: the narrowest model gets the narrowest job, while code retains explanation, constraints, and responsibility for acting.

## 11. Primary and official source register

All sources below were accessed 2026-09-21. Paper claims are limited to the reported setting; repository claims are identified as official project statements rather than independent validation.

1. **TypeSafe official integration skill.** `typesafe-ai` skill tag `v0.5.7`, commit `65a39f393687675ce170e6094757de20370365b9` (commit dated 2026-09-12): [tag](https://github.com/typesafe-ai/skills/releases/tag/v0.5.7), [pinned skill source](https://github.com/typesafe-ai/skills/blob/65a39f393687675ce170e6094757de20370365b9/skills/typesafe-ai/SKILL.md). Used for the programming contract and direction to treat live docs as authoritative.
2. **TypeSafe official live documentation.** [Models](https://docs.typesafe.ai/models.md), [HTTP API](https://docs.typesafe.ai/api.md), [State](https://docs.typesafe.ai/concepts/state.md), [Confidence](https://docs.typesafe.ai/confidence.md), and [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md) (jaggedness page last reviewed 2026-09-17). Used for model IDs, limits, per-request explicit-state shape, primitive semantics, confidence meaning, and official limitations.
3. **Zaratiana et al., “GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer.”** arXiv:2311.08526 v1 (2023-11-14), plus official release [`v0.2.29`](https://github.com/urchade/GLiNER/releases/tag/v0.2.29) (2026-09-08): [paper](https://arxiv.org/abs/2311.08526), [official repository](https://github.com/urchade/GLiNER). Used to classify GLiNER as a label-conditioned span/NER model, not a generic calibrated classifier.
4. **Stepanov et al., “GLiClass: Generalist Lightweight Model for Sequence Classification Tasks.”** arXiv:2508.07662 v1 (2025-08-11), plus official package release [`v0.1.20`](https://github.com/Knowledgator/GLiClass/releases/tag/v0.1.20) (2026-07-21): [paper](https://arxiv.org/abs/2508.07662), [official repository](https://github.com/Knowledgator/GLiClass). Used for model shape, author-reported F1/throughput, and reported calibration/large-label limitations.
5. **Chidambaram and Ge, “Reassessing How to Compare and Improve the Calibration of Machine Learning Models.”** ICLR 2025: [official proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/9a30247fcca95299c2fd48d4667282de-Abstract-Conference.html). Used to justify proper scores/generalization measures alongside calibration metrics and to reject ECE-only promotion.
6. **Zhou et al., “A Novel Characterization of the Population Area Under the Risk Coverage Curve (AURC) and Rates of Finite Sample Estimators.”** ICML 2025, PMLR 267: [paper page](https://proceedings.mlr.press/v267/zhou25y.html). Used for the population/finite-sample footing of AURC in selective classification.
7. **Angelopoulos et al., “Conformal Risk Control.”** arXiv:2208.02814 v4 (2025-06-13; work published at ICLR 2024): [paper and version history](https://arxiv.org/abs/2208.02814), [full HTML](https://arxiv.org/html/2208.02814v4). Used for the expected bounded monotone-loss guarantee, exchangeability proof condition, and non-monotone counterexample.
8. **Liang, Peng, and Sun, “Selective Classification Under Distribution Shifts.”** TMLR 2024, arXiv:2405.05160 v2 (2024-11-27): [paper](https://arxiv.org/abs/2405.05160). Used to require distribution-shift slices for selective confidence scores.
9. **Xu, Guo, and Wei, “Selective Conformal Risk Control.”** arXiv:2512.12844 v2 (2026-04-27), preprint: [paper](https://arxiv.org/abs/2512.12844). Used only as a research-watch source on selection plus conformal control.
10. **Zhu et al., “Conformal Risk-Averse Decision Making with Action Conditional Guarantee.”** arXiv:2606.05551 v2 (2026-06-09), preprint: [paper](https://arxiv.org/abs/2606.05551). Used only as a research-watch source distinguishing marginal from action-conditional guarantees.
11. **Hollmann et al., “Accurate predictions on small data with a tabular foundation model.”** Nature 637, 319–326, version of record 2025-01-08, plus official TabPFN release [`v9.0.0`](https://github.com/PriorLabs/TabPFN/releases/tag/v9.0.0) (2026-09-15): [paper](https://www.nature.com/articles/s41586-024-08328-6), [official repository](https://github.com/PriorLabs/TabPFN). Used for the tabular family and for the explicit separation between peer-reviewed model evidence and current checkpoint/runtime/license claims.
12. **Kong et al., “DF²: Distribution-Free Decision-Focused Learning.”** UAI 2025, PMLR 286: [paper page](https://proceedings.mlr.press/v286/kong25a.html), [official code](https://github.com/Lingkai-Kong/DF2). Used to distinguish decision-focused objectives from predictive classification.
13. **Athey and Wager, “Policy Learning with Observational Data.”** Econometrica 89(1), 133–161 (2021): [publisher page and full article](https://onlinelibrary.wiley.com/doi/full/10.3982/ECTA15732), [official replication repository](https://github.com/grf-labs/policytree/tree/master/experiments/athey_wager_2021). Used for causal-policy identification, doubly robust value estimation, constraints, and regret.
14. **Ong et al., “RouteLLM: Learning to Route LLMs from Preference Data.”** ICLR 2025: [official proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5503a7c69d48a2f86fc00b3dc09de686-Abstract-Conference.html), [official repository](https://github.com/lm-sys/RouteLLM). Used to treat model routing as a learned cost-quality policy, while not importing its benchmark claims into Augustus.
15. **Iyengar, Lam, and Wang, “Is Cross-validation the Gold Standard to Estimate Out-of-sample Model Performance?”** NeurIPS 2024: [official proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ac4106bcfff33140de7799d03daeb8a4-Abstract-Conference.html). Used as a caution against treating repeated cross-validation as automatic reliability proof.

## Bottom line

The reliable Augustus position is stronger when it is more precise:

- typed output is a software contract;
- probability meaning is an empirical contract;
- abstention is a policy evaluated on a risk-coverage curve;
- conformal control is an assumptions-scoped statistical contract;
- optimization is a decision objective;
- causal action requires identification;
- and explicit policy, enforced by code or an accountable human process, retains authority.
