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
| Value of information (EVPI / EVSI) | Whether another observation is worth its cost | Gather as an enumerated act; pay iff expected decision-loss drop > cost. Wake/resume: skip the LLM turn only if the judge answers and p is low. Selective memory: score the ledger against the task; dump on failure. Classify-first: pay for a full agent open iff relevance says it might change the act | Cost of the observation; the loss table; skip-limit; always-keep rules; hard I/O envelope | **Hypothesis** as a numeric calculator; **Contract** as the placement (`mappings.md` §6). wakegate 21/21 is smoke (`notes.md` §51). carryforward 9×3 is a hint (`notes.md` §55). jev-sift mocks ≠ accuracy (`notes.md` §56) |
| Signal detection (Green & Swets) | Evidence variable + criterion | Noul as noisy evidence; t from costs and base rate; ROC/PR on your labels | Operating point, base-rate tracking | **Hypothesis** for non-SWE plots; **Empirical** as moderation *shape* (`mappings.md` §7) |
| Reliability calibration (Platt/temperature) | Raw scores → calibrated probabilities | Noul is natively calibrated **in-distribution only**; verify with reliability bins on your own population; re-fit a correction out-of-distribution | Calibration fitting, binning | **Empirical recipe** (ECE 0.0313 in-distribution; 32% OOD collapse — Archer Hume). Atlas: DAIR Emotion dangerous-high (48% / 0.819); DMB S5 ECE 0.246 (`notes.md` §49) |
| Frozen-protocol bake-off vs constrained LLMs | Same items, accuracy + ECE + latency + cost + honesty | Decision-model as one contender class, not the score | Protocol, raw logs, baselines | **Empirical as Harbor/jevals practice** (DMB v2; jevals-data CC-BY-4.0 recompute-from-logs; `notes.md` §49) |
| Pre-registered cascade vs nano/frontier/encoder | Kill/go printed; cascade R at a stated accuracy target; error-ranking AUROC ≠ ECE | Confidence as an escalation signal is a *hypothesis to kill* | Pre-reg hash, paired CIs, margin sensitivity, serving-path controls | **Empirical as Harbor/jevals practice (honest negative)** (jev-baselines-eval: both AMBIGUOUS; cascade sign-flip at exact parity; confidence=1.0 on 102/200 incl. 6 wrong; encoder 0.933/9ms; ~2.2× serving-path; errata ×3; `notes.md` §55) |
| Healthcare S1+S2 on synthetic FHIR | Remainder after NEWS2 / recon / routing in code | Typed Noul/Score/Choice; S2 blinded review | Labels first; independent outcome policy | **Empirical as a named report, not clinical validation** (explore-typesafe-ai; 20 cases/scenario; Claude wrote labels; `notes.md` §55) |
| Harbor on/off routing | Same task, routing on vs off, hidden verifier | Tool Choice per turn; cheaper unsolved is not a saving | Fresh gateway; perft / checks the agent never sees | **Empirical as a *shape* and one-run signal** (jev-gateway-bench chess-bugfix 36/36 both; 4 vs 6 LLM req; `notes.md` §51). Not a measurement until reps ≥5 |
| Survey scoring / psychometrics | Rubric level judgment with defined anchors | Score with concrete level descriptions; probabilities read beside every score | Weighted aggregation, reliability analysis | **Contract** (score docs: split composite judgments) |

## Search, planning & operations research

| Method | Judgment-shaped component | Jev substitution | Stays in code | Status |
|---|---|---|---|---|
| MCTS / PUCT | Prune invalid actions; priors P(s,a); leaf value V(s) | Batched Noul pruning + Choice priors + Score value — depth-capped where no simulator | Tree, budget, backprop, probes | **Empirical recipe** (jev-mcts: 24/24 vs 1/24 greedy; speculative depth 2) |
| Beam search over taxonomies | Which branches deserve expansion | Choice distributions as branch priority; keep K paths where ambiguity is early | Frontier, budget, final selection | **Empirical recipe** (beam K=3 cookbook) |
| Structure induction over a bag | Pairwise "does i depend on j?" (or Choice over order) | One judgment per pair; DAG / scheduler in code | Topology, cycles, execution | **Empirical as a shape** (dag-jev experiment; empty README; no metrics, `notes.md` §48) |
| Collab-arm product loop | Scripted legal set vs LLM-propose vs unconstrained | Choice over legal actions; stop on low p rather than guess | Legality, Wilson/McNemar, ceiling flags | **Empirical as a harness shape** (jev-testbench; bake into jevals/Harbor, `notes.md` §48) |
| Computer-use observe → score → act | Which observed control matches the current requirement | Score / Choice / option-attention among a11y/DOM candidates (Jev *or* GLiNER2 *or* Laya *or* Cua-S1); code clicks. Harness cousin: Stagehand pick then copy/act. Robotics cousin: Choice on geometry-as-text, not pixels | Observation, freshness, dates; never generate selectors or values; independent outcome check (`DONE` ≠ success); plan ≠ execute; kinematics / Hz in code; schema/gate else LLM | **Empirical recipe** as shipped loops (jev-ultrafast / solari-reflex Jev; gliner2-ultrafast GLiNER2; laya-mind2web DOM-index Laya); **Empirical as README/MODEL_CARD** for Cua-S1 (source-only, not TypeSafe Jev, `notes.md` §54); **Empirical as PR body** for Stagehand #2951–#2955 (draft; 37/75 no-LLM ~0.5s vs 4.37s *theirs*; pick ≠ replacement, `notes.md` §57); contrast blackwood-rlcd screenshot, `notes.md` §48, §52. **Empirical as showcase** MuJoCo / MOSS text-state (`notes.md` §56); drawing-pixel claim ≠ Archer |
| Screening / Wald sequential tests | Pass / fail / keep-looking per candidate | One Noul gate per candidate in one batched request; budget in code | Sequential rule, stop boundaries | **Hypothesis** |
| STPA / STAMP control structure | Sensor reading vs enforced constraint | Judgment as sensor; constraints in policy/code/interlock; STPA table if the sensor lies | The constraint, the actuator, the probe | **Contract** as ownership; **Hypothesis** as domain product (`mappings.md` §8) |
| PufferLib / Ocean env contracts | Does this episode look like a known trainer-bug mode? | Cluster failing episodes; never "the policy is correct" | Seeded serial env, Ocean sanity, observed rewards | **Hypothesis** as placement; **Contract** that Ocean is not a comparative baseline (`formal-methods.md` DST trio) |
| Routing / dispatch (OR) | Which queue/agent owns this item | Choice + confidence-gated escalation; code owns capacity | Cost matrix, capacity constraints | **Empirical recipe** (intent-routing; LlamaIndex Jev selectors; skillranker) |
| Cascade / prefilter (IR) | Cheap reject before an expensive scorer or LLM | Per-candidate Noul/Score; fail-open on drop, fail-closed on dispatch. Decision-native: evidence-set after wide retrieve. Classify-first MCP: content to the judge without entering main agent context first. Meaning-search: packed parallel relevance, two-stage outline→zoom | Candidate generation, always-keep set, recall keys; conflict/provenance; hard I/O envelope; keyword baseline when the string is known | **Empirical recipe** (classifying RAG passages; jevprune; git-jev-stage). **Empirical as architecture** (decision-native-rag-skills; Hypothesis as a measured win, `notes.md` §55). **Empirical as README** (jev-sift; mocks ≠ accuracy, `notes.md` §56). **Empirical as stripped-repo card** (jevgrep 79% top-5, `notes.md` §58). **Empirical as one-run** (Jev-RAG vs Spark rerank; full-context Spark still faster, `notes.md` §58) |
| Knapsack / portfolio selection | Per-item feature vector from text | Fan-out nouls/scores as features; optimizer in code | Constraint solver, weights | **Hypothesis** (mapping 1 shape) |

## Information theory & signals

| Method | Judgment-shaped component | Jev substitution | Stays in code | Status |
|---|---|---|---|---|
| Entropy as uncertainty signal | Measuring "how spread is this belief" | Entropy of returned distributions across repeats or options — computed in code from returned probabilities | All arithmetic | **Empirical recipe** (cookbook pattern) |
| Detector / Neyman filter (context) | Is this artifact relevant to the current task? | One relevance Noul per block before it enters context; stub + recall key. Encoder cousin: retention Choice + span locate, copy verbatim. Indexer cousin: GLiNER extract on the bulk, escalate LLM on the tail. Stdout cousin: Noul per chunk after a hard size/format envelope. Session-ledger cousin: score verbatim facts; rules never judged. Classify-first cousin: batch path/url/text to the judge before the main agent reads | Cache, recall, safety keeps; mutation/shell envelope; ≤10k/JSON-diff pass-through; archive dropped spans; do not dump the repo if S1 failed to load; fail-open dump of the ledger; 50 / 60k / 2MB / public-IP envelope | **Empirical recipe** (winnow ≤0.22 hide; compaction 2-noul rule; pi-jev-context hide-not-delete; gliner25-compaction GLiNER2.5 keep_full/keep_evidence/keep_call_only/drop, `notes.md` §50; s1-graphify-indexer degraded-load / no-invent-edges, 10–50× unfilled, `notes.md` §51; jev-pruner Bash stdout prune, `notes.md` §53; carryforward, `notes.md` §55; jev-sift classify-first, `notes.md` §56) |
| Anomaly detection | Does this deviate from expected shape? | Guard nouls + harm Score over {input, output, tool trace} | Baselines, alert thresholds | **Empirical recipe** (guardrails cookbook; pi-jev output judge) |
| Allowlist ∩ remainder (code-then-model) | Unlisted / unstructured leftovers after a **proof** | Typed questions only on the unknown tier; admit iff every p < τ | Proven/refused in code; cannot block unless a sandbox sits under | **Empirical recipe** (jevgate 0/59 unsafe unasked held-out; allowlist *proves* read-only verbs; doc-router 1.74× $). Domain-general: `mappings.md` §18 |
| Decision-token LoRA (constrained-AR) | Specialize a generator for parallel constrained fields | Loss only on the single decision token; KV broadcast across fields | Schema, candidate tokens, policy | **Empirical recipe** as Foodoo1 200-case / 4-field receipt (fraud_risk 64→95%, overall 85.2→98.8%, ~234 ms); **Hypothesis** as a general recipe. Synthetic; not a financial product. Softmax ≠ Noul |
| Teacher distill of judgments | Copy a hosted decision API onto a small local head | LoRA / frozen-encoder heads trained on teacher answers | Independent gold labels; ECE on *your* cases | **Empirical recipe** as one 70-row run (openjev-lm 92.9%); student-b n=60 MAE 0.187 / Pearson 0.791 / 90% vs vanilla (HF card unchanged ~17:48); **Hypothesis** as a general recipe |
| Domain specialist LoRA (independent gold) | Calibrated local head when policy *reads* p | Soft-target LoRA + pointer; matched-precision KL vs hosted few-shot | Argmax-only routing can stay hosted+examples; EU/thresholds in code | **Empirical as their RESULTS.md** (Domain-jev-maker; KL 0.168 vs 0.580 banking; few-shot determinate McNemar n.s.; not a teacher-copy; `notes.md` §60) |
| Decide→policy→LLM leftover | Typed decide; leftover text only | Shared Answer schema; three Harbor arms (native / verbalized / logprob) | Policy auto/review/llm; Noul 0.5 never rounded; Score conf 0.0 never acted | **Empirical as README architecture** (jav-email-cascade; mock gen-json flat is *their mock*; `notes.md` §60) |

## Verification & logic

| Method | Judgment-shaped component | Jev substitution | Stays in code | Status |
|---|---|---|---|---|
| Claim–evidence entailment (NLI) | supports / contradicts / not-established per claim–source pair | One Choice per pair + review flag; judge against the cited source text only. Stop-hook cousin: claims vs **session** evidence | Quote extraction, citation graph, audit log. When the answer *is* a span you already hold, **point** at line ids and copy verbatim — the model never writes the excerpt (jev-reviewer). Keyword retrieve is not semantic (clear-head) | **Empirical recipe** (citation_check cookbook; jev-reviewer sample study, `notes.md` §48; clear-head Stop, `notes.md` §51). Atlas: paraphrase_support and reversed_meaning_high_overlap correctly judged when both texts are in `state` (`notes.md` §49) |
| Extractive selection + offline re-threshold | Keep/drop over sentences, ids, character offsets, observed DOM controls, or stdout chunks code already holds | Per-item Noul/Choice + one broadcast; join in order; `redecide` on the log with no new calls. Compaction: retention Choice + span locate. Computer-use: score among a11y/DOM candidates. Stdout prune: Noul per chunk after hard envelope. Harness extract: pick elements, copy text | Numbering, header skip, thresholds, publish permission; mutation envelope; copy exact bytes; click in code; never generate selectors; archive dropped stdout; schema/gate else LLM | **Empirical recipe** (testimonial-miner 8-request fixture; jev-reviewer; gliner25-compaction char-offset copies, `notes.md` §48, §50; gliner2-ultrafast observe→score→act, `notes.md` §52; jev-pruner, `notes.md` §53). **Empirical as PR body** Stagehand #2955 pick-and-copy, `notes.md` §57. Cousin of applied-mappings §2 |
| Combinatorial grid / program synthesis | Consistent whole-object from many cells | **Rejected as extractive.** Cell-wise Choice does not assemble ARC grids (4/400 Direct Jev) | Search, a program, a simulator | **Empirical as a negative** (`notes.md` §49) |
| Spec vs artifact conformance (model checking *mindset*) | Property holds / violated / unverifiable for a named requirement | One Noul/Score per requirement, batched; violated → named rule back into context (pi-warden / Abide shape). This is **not** TLC/Apalache/GNATprove | Requirement enumeration, enforcement, logging; the **linter** if the rule is lintable; the real checker if you have one | **Empirical recipe** (pi-warden: 6→0 rule breaks, 150 paired runs; jev-pref: YOU define the rule; Abide: productized compile/calibrate/tune/replay, `notes.md` §47; if-ai: plain-English PR check, fail-closed on error, `notes.md` §51). Ownership split: `formal-methods.md` |
| AST ∩ semantic lint | Semantic remainder after a parser already extracted units | Typed questions on Tree-sitter targets; do not execute scanned code. Skills→oxlint: generic AST facts + prechecks, then remainder Noul; guidance whole-file in state | Parser, selection, fail-on; `tenbin` owns the lint *skill* | **Empirical as a shape** (jevscan 0.2.0rc4; not a calibration claim; `notes.md` §48). **Empirical as Phoenix experiment** (jev-oxlint; answer-key agree; not a hard gate, `notes.md` §58) |
| Alloy finder vs Apalache / TLC | Which bound, which counterexample, is the property tautological? | Triage instances/CEs; never "this spec looks right" | Analyzer / SMT / explicit-state engine | **Hypothesis** as product; **Contract** as ownership (`formal-methods.md` §2) |
| Type-checking analog | Does this planned call match the schema/operation/target? | Decomposed nouls over {request, schema, trace}; never trust a Jev pass as authorization | Real validation of operation+target in code | **Empirical recipe** (validation.md self-monitoring). Product: toolgate allow/block/review — Jev is not authorization; timeout stops (`notes.md` §55). Capability kernel: interlock — secrets never in agent; Jev SENSOR; policy.py decides; type-safe ≠ correct (`notes.md` §59). Human-confirmed kill: port-cleanup (`notes.md` §59) |
| Engine truth ∩ coaching judgment | Severity / error class / interrupt on engine facts | Typed questions; never re-evaluate the position | Engine eval/lines/swing; templates; capped writing model | **Empirical as PRD** (game-coach Wave 0; Stockfish owns truth; `notes.md` §59). Anti-soundness-theater with egma attention≠correctness |
| Native-probability calibration | Honesty of noul/choice/score vs analytic truth | Brier / ECE / reliability / risk-coverage; fan-out batches | World definitions; oracle stub; teeth miscalibrated stub | **Empirical as their live card** (jev-arena Brier 0.0059 / ECE 0.0620 on 145 noul; overconfident in low bins; `notes.md` §59) |
| Ranking family on soft scores | Pairwise inversion / Score ordinality / ties of a sort key | Gate SQL on a passing results.json; secondary key on two-decimal ties | The engine's LIMIT/tie break; request-shape measurement | **Empirical as independent measurement** (jev-orderby-bench; Score 0.143 weak link; 53-way 0.99 tie; recodelabs batch-40 fails ranking; `notes.md` §60) |

## Economics & game theory

| Method | Judgment-shaped component | Jev substitution | Stays in code | Status |
|---|---|---|---|---|
| Multi-criteria decision analysis | Attribute scores per alternative | Composite scores with weights in code (re-weight without re-inference). Intent columns: a heading scores each row | Weight policy, Pareto views, exact fields | **Empirical recipe** (mapping 1). Showcase *shape*: jevable intent columns; snack MCDA clocks are **claims** (`notes.md` §56) |
| Mechanism/game response (adversarial state) | Opponent-intent / bluff / risk read on a state | Choice over reads + risk Score; policy in code; 2.5Hz-style advisory rate | Strategy solvers, exploitative math | **Empirical recipe** (jev-trader, game agents) |
| Auction/market event classification | Is this signal material? Direction? | Choice over event classes + urgency nouls; execution in code | Order execution, risk limits | **Empirical recipe** (jev-trader 81ms/block) |
| Threshold-probe value CDF (Vickrey) | P(V > X) noul fan-out; code bids | Native probabilities; monotonize CDF; Jev never bids | Second-price / first-price payment rule | **Empirical as their live/offline cards** (jev-vickrey; oracle regret 0; live Brier 0.1391; overconfident stub loses money; `notes.md` §59) |
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
- A listwise / retrieval scorer (jina-reranker-v3.5 trolley: always pull
  the lever, 1 death or 1B) as an ethics/value Choice. Relevancy ≠
  decision rationality (`judgment-class.md`).

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
