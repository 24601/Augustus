# Mappings: classical methods → judgment-class designs

Each card: what transfers, what does NOT, a composition sketch, a non-ticket
example, a counterexample, an acceptance test. Jev is the documented
exemplar in the sketches; family choice (open head / GLiClass-adjacent /
listwise / vision) is `judgment-class.md`. Status words: **Contract**
(documented), **Empirical recipe** (dated observation), **Hypothesis** (test
before relying).

## 1. Semantic judgments → features and explicit utility

**Method**: feature engineering, ordinal measurement, multi-criteria decision
analysis. **Transfers**: turning unstructured evidence into named, reusable
numeric features (Noul probabilities, Score distributions, stable Choice
categories). Judge once; explore many policies without rerunning inference —
sliders, weights, filters, Pareto views, or a supervised model on top.
**Does not transfer**: Score has no natural units. Normalizing by the top
level aligns ranges only — not spacing, importance, or cross-concept
comparability. Weighted sums express a chosen compensating policy; hard
exclusions stay as separate rules. A downstream model (e.g. CatBoost,
**Empirical recipe** per the autoresearch cookbook) learns only what labeled,
held-out outcomes establish — split data before label-driven rubric/feature
discovery and version feature definitions with the model.

```text
state = {paper: {...}, question: "..."}
questions = {is_rct: Noul(...), reports_mace: Noul(...),
             evidence_strength: Score([...4 levels...])}
code: shortlist, rank, filter — weights adjustable without re-inference
```

**Example**: research-reading map — extract reusability dimensions once, let
researchers re-rank and re-filter interactively. **Counterexample** (from
**Contract** Score docs): levels 0,1,2 with distributions `[0,1,0]` vs
`[0.5,0,0.5]` both score 1.0 with radically different extreme-outcome risk —
always read probabilities beside the score. **Test**: beat a simple baseline
and survive reasonable weight/wording perturbations.
Links: Score docs, composite-scoring pattern, autoresearch cookbook.

## 2. Probabilistic judgments → cost-sensitive decisions

**Method**: selective classification, decision theory, cascades. **Transfers**:
choosing among act / decline / gather-evidence / escalate from the
distribution, with thresholds owned by each action's consequences. For a
calibrated binary probability with FP/FN costs: `t = C_FP/(C_FP+C_FN)`.
**Does not transfer**: universal thresholds (no magic 0.8); model probability
is not auto-calibrated on YOUR population — plot confidence vs accuracy on
your data (**Contract**: confidence summarizes distribution shape, nothing
more); Noul 0.5 ≠ medium-anything; top-Choice probability ≠ probability the
action succeeds when several options are acceptable.

```text
if confidence < floor: human review
elif action low-stakes: act
else: act only if confidence > high bar, else confirm
```

**Example**: trading bot acts on high-confidence reads, stands down when the
book state is ambiguous (jev-trader `late → hold`). **Counterexample**: a
flat Choice over three fine categories may still name a harmless best pick —
low confidence need not veto a low-stakes preference. **Test**: cost/coverage
curve on held-out slices; score the fallback too (escalation is not
automatically correct). Links: Confidence docs, confidence-routing pattern.

**Cascade / prefilter beside this card**: the same cost model, applied *before*
an expensive generator rather than after a decision. Drop or stub confident-
irrelevant chunks, log lines, or tool results so the LLM never sees them;
fail-open on retrieval (false drop loses evidence), fail-closed on dispatch
(wrong tool is an action). Detail cards: `references/applied-mappings.md`
(context sieve, keep/drop, ranking). Do not invent request fields here —
live docs own the call shape.

## 3. Semantic predicates → decision circuits

**Method**: decision tables, Boolean circuits, DAGs, finite-state machines.
**Transfers**: Jev estimates predicates too fuzzy for exact rules (tone,
aboutness, support); code owns branching, compatibility, transitions,
execution. **Does not transfer**: statistical independence — `P(A)·P(B)` is
NOT `P(A∧B)`; operation+target head pairs can be invalid (browser-use asks
both heads per request but executes only the matching target after
validation); relational judgments ("does passage support claim?") must stay
one question, not two split classifications; exact computation stays in code.

**Example**: game director — Jev judges whether player dialogue is
conciliatory or threatening; code enforces inventory, prerequisites,
chronology, reachable scenes (cf. HEIST//ONE: six guards batched, simulation
validates every proposal). **Counterexample**: decomposing tool-trace
verification into per-call schema nouls works; asking "is the trace correct"
as one Noul hides nine judgments. **Test**: full truth table / transition
cases incl. contradictory outputs, stale observations, invalid combos.
Links: how-to-build guide (decompose-state/questions), smart-home demo.

**Rejected beside this card**: "many Jev checks = independent verification."
Shared evidence, rubrics, and biases correlate failures. Ground checks in
authoritative evidence or executable constraints (citation_check,
classifying-RAG-passages, llm_guardrails cookbooks) and evaluate the
combined verifier as one system.

## 4. Retrieval → bounded semantic reranking

**Method**: candidate generation + expensive relevance function.
**Transfers**: retrieve broadly (index, filters, embeddings, BM25), then one
shared Score rubric for graded relevance, Nouls for binary relations, Choice
for picking among a bounded candidate set. **Does not transfer**: Choice
probabilities across DIFFERENT candidate pools are not comparable absolute
scores; a shared rubric is necessary but not sufficient for comparability
(evidence per candidate must be sufficient and consistent); reranking cannot
recover missing candidates; the 255-option limit is not a dataset-size limit.

**Example**: 1018-paper triage — cheap summarizer + one Jev Choice over 24
topics ($3.99 + $0.08). **Counterexample**: top-1 accuracy measured only when
the right answer is already shortlisted flatters the reranker — always
measure retrieval recall separately from rerank quality, end-to-end top-k +
cost. **Test**: recall split + end-to-end top-k + $/query.
Links: rerank, semantic_find, entity_alignment cookbooks.

**Budget note beside this card**: exhaustive pointwise scoring of huge sets
is not intrinsically wrong (offline, modest corpora) but it is not an index —
per-query work still scales with candidates. Low latency ≠ no retrieval.

## 5. Hierarchy → bounded heuristic search

**Method**: beam search over a meaningful taxonomy or candidate graph.
**Transfers**: Choice distributions as branch-priority heuristics; keep K
paths where early ambiguity matters; code owns frontier, budget,
termination, final selection. **Does not transfer**: the geometric-mean path
score is a ranking heuristic, NOT a calibrated leaf probability; multiplying
related-question outputs is not a path probability without a coherent
conditional structure; pruned branches never recover.

**Example**: patent/retail/biomedical/code hierarchies (cookbook,
**Empirical recipe** jev-1.12, 4 labeled cases: beam K=3 fixed 2 greedy
failures). **Counterexample**: an arbitrary 255-way tournament bracket over
an unstructured shortlist — grouping changes judgments, early elimination
discards global top-k, log rounds ≠ sublinear work. Prefer retrieval or a
real hierarchy; tournaments are benchmarks, not defaults. **Test**: greedy vs
beam vs flat-shortlist baseline on realistic cases; inspect pruning failures;
judge finalists under one common leaf criterion.
Links: hierarchical_classification, skill_suggestion cookbooks.

**Empirical recipe beside this card (MCTS+Jev, launch week — verified in the
archive, not yet independently reproduced):** two implementations now exist.
`lhemerly/mcts-agent` splits roles: a generator proposes candidate actions
(once per expansion), then **one batched call** does all Jev work — Noul
prunes invalid actions (all candidates in parallel, keep ≥0.8) and gates
early stop (≥0.85); Choice supplies PUCT policy priors P(s,a) and picks the
branching factor from primes by uncertainty; Score (1–10 rubric) is the leaf
value V(s), replacing random rollouts. Q normalized /10; unvisited children
inherit the parent's value (first-play urgency) so one lucky child doesn't
starve siblings. `paulobueno164/jev-mcts` is the correction that makes the
pattern defensible:

1. **Fidelity is typed, not commented.** `grounded` environments (a real
   simulator exists) get depth up to 24; `speculative` ones (no simulator —
   every `apply()` is a guess) are hard-capped at depth 2, and `rollout()`
   throws. A tree built on guessed transitions scored by another model
   composes error instead of reducing it; the cap lives in code, not prose.
2. **Only probes concede.** Agent claims ("it worked") go to the journal and
   decide nothing; exit-code probes measured after execution are the sole
   source of granted milestones. "The tree supposes; the probe measures; only
   the probe concedes."
3. **Calibrate before thresholding.** Raw cutoffs (0.8/0.85) are replaced by
   a confidence curve calibrated against exact-search ground truth.
4. **Debias position.** Candidate order is shuffled with a seeded RNG and a
   second debias pass averages judgments with reversed order.
5. **Measured result** (24 scenarios, known ground truth, evaluator-prior
   arm): MCTS 24/24 vs greedy 1/24 — the win comes from a delayed-reward
   trap a 1-ply heuristic cannot see; evaluator-supplied priors changed cost,
   not outcome: 5893→2743 calls, 8.0→7.0 turns, $0.101→$0.047. First-call
   latency ~2s (handshake), then ~0.5s/judgment on a hobby key.

Still true, and sharpened: the Score value heuristic is the weakest link —
trust it only where the environment validates outcomes, and keep the
grounded/speculative split in types. Any depth beyond a simulator is
estimation wearing a measurement costume.
