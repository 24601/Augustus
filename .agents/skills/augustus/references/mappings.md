# Mappings: classical methods → judgment-class designs

Each card: what transfers, what does NOT, a composition sketch, a non-ticket
example, a counterexample, an acceptance test. Jev is the documented
exemplar in the sketches; family choice (open head / GLi\* encoder /
listwise / vision) is `judgment-class.md`. Status words: **Contract**
(documented), **Empirical recipe** (dated observation), **Hypothesis** (test
before relying). Cross-domain frames: `mental-models.md`. Formal /
semi-formal ownership: `formal-methods.md` / `formal-semi-formal.md`.
Cards §6–§19 are **Hypothesis as domain-general products** until an
acceptance test runs; do not promote them from analogy. Read each card's
own labels rather than the range: §8's ownership split (sensor ≠
constraint) is **Contract** as a rule and §9's jev-mcts example is
**Empirical**, and what those cards claim *beyond* those components is
Hypothesis like the rest. Curriculum cards §10–§16 (spec pipeline,
Alloy loop, RV sandwich, DST triage, durable agents, assignment hybrid,
situated density) are the same rule. §17–§18 add paraphrase-stability
and structural-prove ∩ remainder (jevgate / OCR-router *shapes* are
Empirical; the cross-domain reading is Hypothesis). §19 is the
effect-oriented loop: soft Choice on the transition, host owns the effect.

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
researchers re-rank and re-filter interactively.
**Offline re-threshold (Empirical as named receipts):**
[testimonial-miner](https://github.com/AppitStudio/testimonial-miner)
`redecide` reapplies `Thresholds` to logged answers with **no new model
calls** — judge once, explore policy in code (`notes.md` §48). Same family
as firehose sliders. **Beyond SWE
(Hypothesis until labeled):** vendor bid/no-bid (fit, urgency, risk
Nouls; price and deadline exact); apartment shortlist (commute/light/
noise Scores; rent exact); hiring scorecard (evidence Nouls; labor-law
vetoes in policy). Full gallery: `mental-models.md` §MCDA.
**Intent columns / catalog MCDA (Empirical as *shape*; clocks are
claims, 2026-09-19 ~00:38):**
[jevable.com](https://jevable.com/) class pattern: a heading
("Urgency") scores each row. Same hole as jevpandas / jevframe
(`mappings.md` §4) and dabit3 spreadsheet JUDGE/SCORE/CHOOSE.
Snack multi-criteria at catalog scale is a **maker claim** (3,000 /
28 s / $0.11) unless independently re-run. Weights and vetoes stay
in code (`notes.md` §56).
**Counterexample** (from **Contract** Score docs): levels 0,1,2 with
distributions `[0,1,0]` vs `[0.5,0,0.5]` both score 1.0 with radically
different extreme-outcome risk — always read probabilities beside the
score. **Test**: beat a simple baseline and survive reasonable
weight/wording perturbations.
Links: Score docs, composite-scoring pattern, autoresearch cookbook.

## 2. Probabilistic judgments → cost-sensitive decisions

**Method**: selective classification, decision theory, cascades. **Transfers**:
choosing among act / decline / gather-evidence / escalate from the
distribution, with thresholds owned by each action's consequences. For a
calibrated binary probability with FP/FN costs: `t = C_FP/(C_FP+C_FN)`.
**Does not transfer**: universal thresholds (no magic 0.8 — a product
band such as Abide's ≥0.8 repair is *their* operating point, still
re-measured on your labels); model probability
is not auto-calibrated on YOUR population — plot confidence vs accuracy on
your data (**Contract**: confidence summarizes distribution shape, nothing
more); Noul 0.5 ≠ medium-anything; top-Choice probability ≠ probability the
action succeeds when several options are acceptable.

```text
if confidence < floor: human review
elif action low-stakes: act
else: act only if confidence > high bar, else confirm
```

**Public pedagogy receipt (Empirical as article; 2026-09-19 ~10:25):**
[@akshay_pachaar “Jev Clearly Explained”](https://x.com/akshay_pachaar/status/2101037514945597645)
— high / medium / low confidence → auto / escalate / human;
thresholds in code; schema-safe ≠ correct. **200× / 400×**
are TypeSafe ceiling claims *theirs*, not Harbor. Shadow
first; questions-as-code. Do not copy the Python samples
(`notes.md` §85).

**Example**: trading bot acts on high-confidence reads, stands down when the
book state is ambiguous (jev-trader `late → hold`). **Banded fail-open
(Empirical as a named product receipt):**
[Abide](https://github.com/coldteadotai/abide) on project soft rules:
≥0.8 repair in-session, 0.5–0.8 human note, <0.5 silence; hooks exit 0;
no key → the edit proceeds (`notes.md` §47). Soft judgment is never the
sole hard veto. **Beyond SWE
(Hypothesis until labeled):** inbox reply/snooze/archive; "is this paper
on-question?"; "call this lead / nurture / drop" — same act/abstain/
gather table, costs written in hours or dollars, threshold per *action*.
VOI: pay for the full PDF or the customer call only if expected decision
change beats the cost (`mental-models.md` §VOI, §decision).
**Dual-process cascade (Empirical as a productized metaphor, routing
accuracy unmeasured):**
[dual-process-ai](https://github.com/taro1985/dual-process-ai) —
`confidence ≥ τ` → S1 decides; else escalate to S2 (generate). Routing
fails open; safety fails closed. Keyword fallback without a key is not
equivalent S1. Tune τ on *your* escalation log (`notes.md` §49).
**Domain specialist vs few-shot hosted (Empirical as their
RESULTS.md, 2026-09-18 ~20:43):**
[Domain-jev-maker](https://github.com/help-er/Domain-jev-maker) —
independent CLINC-150 labels, **not** a Jev teacher-copy.
Matched-precision KL (both systems rounded to two decimals,
zeros → 0.0025): local 1.5B KL 0.168 vs hosted zero-shot 0.580
banking (r +0.933 vs +0.343). Few-shot hosted (one example per
intent in `state`) matches or beats local determinate accuracy
(McNemar p=0.134 / p=1.000); calibration barely moves (KL still
2.5–3.8× higher). **Train the specialist when downstream code
reads the probability; use few-shot hosted when only argmax
matters.** Do not copy train how-to (`notes.md` §60).
**Active-learning triage / don't distill Jev as teacher
(Empirical as README architecture, 2026-09-18 ~21:39):**
[jev-triage](https://github.com/ThyFriendlyFox/jev-triage) —
high conf accept; middling expensive teacher; low or
near-boundary human. Logs full distributions to
`soft_labels.jsonl`. **Do not distill Jev as teacher of
record** — author ~68% ceiling compounds errors. Real
outcome labels remain the training targets. Noul belief
`|p−0.5|×2`; Choice top-two within 0.15 → human.
Distinguish Domain-jev-maker (independent gold specialist)
from openjev-lm (teacher-copy). Do not copy pip how-to
(`notes.md` §61).
**Harbor-shaped decide→policy leftover (Empirical as README
architecture):** [jav-email-cascade](https://github.com/skiingfalcon/jav-email-cascade)
— 8 typed questions; policy auto/review/llm; Noul 0.5 never
rounded; Score conf 0.0 never acted on. Mock gen-json
flat-confidence is *their mock*, not a live bake-off
(`notes.md` §60). **Counterexample**: a flat Choice over three fine categories may still
name a harmless best pick — low confidence need not veto a low-stakes
preference. **Test**: cost/coverage curve on held-out slices; score the
fallback too (escalation is not automatically correct). Links:
Confidence docs, confidence-routing pattern.

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
**Internals are not a state machine; placement is a component node**
(atlas: paraphrase vs reversed-meaning are LM understanding; "a node in
your state machine" is the architectural instinct — `notes.md` §49).

**Example**: game director — Jev judges whether player dialogue is
conciliatory or threatening; code enforces inventory, prerequisites,
chronology, reachable scenes (cf. HEIST//ONE: six guards batched, simulation
validates every proposal). **Merge-gate circuit (Empirical as README
behavior, 2026-09-18 ~16:48):**
[latch](https://github.com/CaseReed/latch) — Jev labels a clustered
cause; a **table** maps cause × confidence × fingerprint → PASS /
BLOCK / needs_human. The judge is a sensor, not the merge act
(`notes.md` §51). **Language primitive (Empirical as README /
example suite, 2026-09-18 ~17:48):**
[hunch](https://github.com/carldaws/hunch) — Ruby `chance` /
`pick` / `rate` map to Noul / Choice / Score; English is the
configuration; `Hunch.decide` batches over one `given:`.
Validations `rescue nil` = fail-open at save; spam gates should
fail closed. Stub backend for tests. Same interface ≠ same
guarantees for a future LLM backend. Cousin of probably-lang
(a language whose loop conditions are feelings) — this is a
library, not a new language. Do not copy gem/Rails
(`notes.md` §55). **BAML typed if (Empirical as README;
2026-09-19 ~17:49):**
[feelings](https://github.com/BoundaryML/feelings)
(license null; **0★**) — `.feels()` / `.how()` /
`.matches<T>()` / `.fill<T>()` / `.ask()`. README
*theirs*: “Jev makes the decisions, an LLM does the
writing, and BAML ties it together.” feelings `.feels()` default 0.5 is Noul-0.5-never-rounded — use `.how()`.
Exhaustive `match` is the exact envelope. **≠** hunch
**≠** Probably. Do not copy `baml toolchain`
(`notes.md` §89).
**Collapse late as Ruby primitive (Empirical as README;
2026-09-19 ~18:41):**
[s1_ruby](https://github.com/innocentdiaz/s1_ruby)
(MIT; **1★**) — ψ measures; `judge`/`choose`/`score`
measure; `?` collapses. s1_ruby collapse late.
`undecided?` abstain. Code asks; code decides. **≠**
carldaws/hunch **≠** feelings **≠** tpellet/hunch.
`notes.md` §90.
**Pointer-shell control flow (Empirical as README;
2026-09-19 ~18:41):**
[tpellet/hunch](https://github.com/tpellet/hunch)
(MIT; **0★**) — pick/why/is/run over *your* stdin/PATH.
tpellet/hunch exit 3. never-execute list. **≠**
carldaws/hunch. `notes.md` §90.
**Named circuit combinators (Empirical
as README architecture, 2026-09-19 ~01:47):**
[decision-combinators](https://github.com/voidning/decision-combinators)
— Then / Gate / Vote / Cascade / Weighted over
Choice/Score/Noul. README analogizes them as logic
gates; they are **not** literal Boolean AND/OR (those
aggregations stay in code — do not multiply parallel
Nouls). Vote is majority or mean; confidence discounted
by agreement. No measurements. GitHub SPDX null; package
MIT. **Hunch:** System One as a control plane, not chat
turns. Compose with skillranker. Do not copy npm
(`notes.md` §66). **Rename + extended five (2026-09-19
~04:39):** now
[jev-combinators](https://github.com/voidning/jev-combinators)
(same `created_at`; npm `jev-combinators` 0.1.0).
Digital-design slogan: primitives are transistors,
combinators are logic gates, you design the chip.
**Extended:** Router / Loop / Retry / Fallback / Memory.
Fallback is the fail-closed node. Still not literal
AND/OR. `notes.md` §69. **TLA+ consensus circuit (Empirical as
spec + chaos table; 2026-09-19 ~02:38):**
[jev-labs](https://github.com/copyleftdev/jev-labs)
— five paraphrased agents; stability gate; quorum 3 of 5
stable votes; escalate when budget spent. Code/TLA+ own
transitions (`Consulting → Decided | Escalated`). The
model never is the constraint. 1,080 golden: 0 wrong
*theirs*; underdetermined records still decided 34/120
split both ways (stability ≠ answerability). MIT.
`notes.md` §67. **Counterexample**: decomposing tool-trace
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

**Store as the index (Empirical as a *shape*, 2026-09-18):**
Cheap exact predicates first; typed questions on the remainder. Two
forks of the same hole: **in-engine extension**
([`mgaitan/sqlite-jev`](https://github.com/mgaitan/sqlite-jev), loadable
SQLite `jev_rows`; inspired by [`realZachi/pg-jev`](https://github.com/realZachi/pg-jev))
vs **out-of-process CLI** ([`kylemclaren/jevql`](https://github.com/kylemclaren/jevql)
— **judgment outside the store**: vanilla Postgres never
sees `jev()`; the CLI/serve/MCP/SDKs judge). sqlite-jev is a semantic full
scan, not an index; `max_rows` is a spend guard; thresholds stay in SQL.
[`ant4g0nist/joxide`](https://github.com/ant4g0nist/joxide): zoxide owns
the directory index; Jev scores a shortlist; destinations are existing
local paths only; fail-open. Dataframe cousin this hour:
[`yalindogusahin/jevpandas`](https://github.com/yalindogusahin/jevpandas)
— `evaluate` / `filter` / `classify` / `score` / batched `ask` over a
pandas frame; classify example includes `other`; failures never become
negative predictions; LICENSE absent this pass. Accessor sibling this
hour: [`ktaletsk/jevframe`](https://github.com/ktaletsk/jevframe) (MIT,
PyPI; pandas **and** Polars `.jev`; full `p__` columns; no silent
renormalize; one row per request). Same hole, two surfaces. Row
contents leave the store (same residency warning as AU health). Do not
copy SQL, env, or CLI flags.
`notes.md` §42, §44, §46, §48. Intent-column / snack MCDA *shape*:
`mappings.md` §1; `notes.md` §56.

**ORDER BY over probs is a ranking job, not a calibration
certificate (Empirical as independent measurement, 2026-09-18
~20:43):**
[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)
— `jev-1.13.0` passes all six pre-registered gates on 360
human-labeled 20 Newsgroups rows. Boolean inversion 0.036;
Score ordinal inversion **0.143** vs 0.15 (weak link / the
sort key); 53 rows tie at 0.99 so `LIMIT 20` is
engine-dependent; two-decimal quantization. Calibration
(ECE 0.0453 / Brier 0.0524) ≠ sortable. recodelabs default
40-row batching **fails** the ranking gate (inversion 0.171)
that one-row-per-request passes — request shape is part of
the measurement. Not a fourth DuckDB extension. Vendor 67.8%
agreement ≠ calibration. `udf.register()` refuses SQL unless
results pass. Do not copy curl / key how-to (`notes.md` §60).

**Decision-native evidence set (Empirical as architecture;
Hypothesis as a measured win, 2026-09-18 ~17:48):**
[decision-native-rag-skills](https://github.com/emergency-lee/decision-native-rag-skills)
promotes this card from "rerank a shortlist" to **retrieve wide →
decide → build an evidence set → resolve conflicts → generate only
over kept evidence**. Embeddings remain candidate generators; they
do not settle relevance, sufficiency, redundancy, conflict, time,
or authority. No bundled harness; no universal benchmark; default
migration gates are starting targets (`notes.md` §55). PubMed
title/abstract screening is the same *shape* on literature
([typesafe-screening-mcp](https://github.com/masa-med-ai/typesafe-screening-mcp):
include/maybe/exclude in code; 326 hits ~17 s ~$0.014 one run;
thresholds not calibrated; screening aid, not an SR replacement).
Local-file cousin:
[kazuhideoki/jev-search](https://github.com/kazuhideoki/jev-search)
(recursive files + fzf) — **not** superagents-lab/jev-search
(federated web). Max-over-chunks ≠ calibrated whole-file p.
**Classify-first MCP (Empirical as README / schema, 2026-09-19
~00:38):**
[jev-sift](https://github.com/kbhuw/jev-sift) is the same sandwich
on agent I/O: retrieve-wide (paths / public URLs / inline text) →
decide (relevance or 1–8 typed questions) → the main LLM opens
only the evidence set. Content never enters main agent context
first (paths/URLs). Hard envelope in code. Transport tests ≠
accuracy. No LICENSE this pass. Cousin of typesafe-screening-mcp
(abstracts never enter the LLM conversation). Not jev-routing
(host adapter). `notes.md` §56.
**Meaning-search without embeddings (Empirical as a named
stripped-repo card, 2026-09-18 ~18:46):**
[jevgrep](https://github.com/Bentlybro/jevgrep) — packed parallel
Jev relevance; two-stage outline → zoom top 30; no index. 228
questions, docstring-stripped repos: **79% top-5** vs BM25 40% /
grep 20%. Keyword still wins exact strings (BM25 top-10 96% vs
85%). Harbor-shaped: frozen copies + labeled questions +
comparable harnesses; not a Harbor taskset. Distinct from
kazuhideoki / superagents-lab / jev-sift (`notes.md` §58).
**Meaning-grep over line Nouls (Empirical as README + their
judge test, 2026-09-18 ~21:39; dedicated 2026-09-19 ~16:30):**
[jev-semgrep](https://github.com/uehaj/jev-semgrep) — AND/OR/NOT
on *thresholded* per-line Nouls (do not multiply p);
proposition ≠ embedding; contrast-set refund; no index;
cross-lingual; Semgrep.dev collision; **not a gate**.
Distinct from jevgrep (file/chunk) and jev-combinators
(metaphor). Precision 0.94 / recall 0.98 *theirs* (not
Harbor). **51★** ephemeral. LICENSE MIT (GitHub
NOASSERTION). `notes.md` §61, §86.
**Pointer path-then-window (Empirical as README,
2026-09-19 ~16:52):**
[JevFind](https://github.com/Peu77/JevFind) — score paths,
open windows, copy snippets. 0.25/0.55 still soft. Not
AST. **≠** jevex **≠** jev-semgrep. `notes.md` §87.
**NL memory → beam-search FS (Empirical as README;
2026-09-19 ~17:25):**
[findme](https://github.com/marc2332/findme) — beam over
listed names+metadata from an NL memory; parent
fallback ≤4. Ranking ≠ identity. **≠** JevFind.
`notes.md` §88.
**Evidence-packet explorer (Empirical as their performance.md,
author-run):**
[jev-semantic-explorer](https://github.com/jimmyhealer/jev-semantic-explorer)
— index once, BM25 shortlist, Jev ranks, citable packet.
SWE-bench Verified n=8: 1/8 → 6/8 finish (empty = miss).
Packet n=50 HitFile 0.233 vs BM25 0.159 is **not** the
product KPI. Distinct from jevgrep / jev-sift. `notes.md`
§61.
**Measured RAG rerank vs generative rerank (Empirical as one-run;
Hypothesis as a transfer):**
[Jev-RAG](https://github.com/Max-sm-yc/Jev-RAG) — ≥70% cost / 72%
latency vs Muse Spark *rerank* on ~30k tokens (costs include
embeddings). Full-context Spark is still **faster** (10.60 s).
Do not overclaim vs no-RAG. License null this pass
(`notes.md` §58).
**RAG rerank harness (Empirical as README plumbing;
2026-09-19 ~17:49):**
[jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark)
— quality/latency/cost; “Jev wins” is not an assumption.
OpenRouter Decisions ≠ TypeSafe direct.
`max_budget_usd` 0 blocks paid. **≠** Max-sm-yc/Jev-RAG.
`notes.md` §89.
**Pairwise sort-by-meaning (Empirical as README;
2026-09-19 ~18:41):**
[jsort](https://github.com/keltokhy/jsort)
— Bradley-Terry from pairwise Jev. jsort scores are
relative. Noul not Choice for scale. Ranking ≠
frequency. CommonLit r=0.824 / ρ=0.841 *theirs*.
`notes.md` §90.
**Native vs schema-guided groundedness (Empirical as
README; 2026-09-19 ~18:41):**
[groundedness-judge-bench](https://github.com/slavadubrov/groundedness-judge-bench)
— RAGTruth QA. groundedness-judge-bench native vs
schema-guided. Fastest/cheapest ≠ quality.
implicit_true included in yes. **≠** jev-judge-bench.
`notes.md` §90.
**Local prune ≠ hosted Noul (Empirical as README;
2026-09-19 ~19:47):**
[nanoprune](https://github.com/dmdjr1409/nanoprune)
— nanoprune 2.8MB ECE 2.58%. Distill ≠ hosted Noul.
Do not Noul-rerank already-good retrieval
(typed-judge-kit 14/15→13/15). `notes.md` §91.
**Calibrated rerank / pointer sieve (Empirical as README;
2026-09-19 ~20:41):**
[Jev-Reranker](https://github.com/uspraveen/Jev-Reranker)
— Jev-Reranker live Jev not yet measured. r@1 0.1667
is offline-judge. [jev-search](https://github.com/savka777/jev-search)
— jev-search pointer sieve. Score ≠ truth.
Always **savka777/jev-search**. **≠**
kazuhideoki/jev-search **≠** superagents-lab/jev-search.
[sessionwise](https://github.com/Nasrallah-AL/sessionwise)
— sessionwise opt-in relevance. `notes.md` §92.
**Evidence projection vs LLM summary (Empirical as README;
2026-09-19 ~21:41):**
[jackboykin/quarry](https://github.com/jackboykin/quarry)
(Go MIT; **0★**; **master**) — quarry evidence projection.
Fetch to disk; Jev scores line ranges. Pointer, never
paraphrase. 5 s fail-open. p&lt;0.5 dropped; top 3.
**≠** savka777/jev-search. `notes.md` §95.

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
failures). **Empirical beside this card (255 cap, synthetic n=180,
2026-09-18):** [`reachjalil/jev-tree-choice-cap`](https://huggingface.co/datasets/reachjalil/jev-tree-choice-cap)
walks an authored region→service→mode tree so each Choice stays under
Jev's 255. Truncate-to-255 is **90/180** and **0/90 on the tail** (Cape
Town sits past index 255). Authored tree **180/180** (3 calls). Keyword
also 180/180 on this invented catalog — do not sell the tree as beating
lexical lookup; sell it as *not silently dropping the tail*. Flat
auto-partition 179/180. Tournament brackets stay rejected. Code:
[jev-tree](https://github.com/reachjalil/jev-tree). `notes.md` §33.
**Counterexample**: an arbitrary 255-way tournament bracket over
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

## 6. Value of information → gather as an enumerated act

**Method**: Raiffa-line decision analysis, EVPI / EVSI. **Transfers**:
another observation is an *act* whose cost you know (a test, a search, a
human, another batch of Nouls, an LLM autopsy). Pay iff expected
reduction in *decision loss* beats that cost — improvement in the
probability is not the quantity
(`mental-models.md` §VOI). Cheap fan-out of independent questions is
often +VOI because the second question is nearly free (composition:
width is cheap). **Does not transfer**: infinite clarifying questions;
paying for a paragraph when a Noul would do; treating another LLM call
as free information; a numeric EVPI computed from uncalibrated scores
and labeled Contract.

```text
belief  = current Noul / Choice / Score
acts    = {decide now, buy observation, abstain, escalate}   # you enumerate
loss    = table you wrote
pay iff E[loss | now] − E[loss | after paying] > cost
```

**Example (Empirical as a *shape*, OpenSmoke / env triage):** LLM autopsy
only on flags — a negative flag has no VOI in the autopsy
(`applied-mappings.md` §3). **SREGym-Lite (Empirical as a *shape*):**
Jev ranks the *next diagnostic test* among candidates the agent already
holds; it does not run the test and does not diagnose
(`notes.md` §33). Pay for the next kubectl/log only if EV(decision)
improves — a high review score cannot buy missing evidence.
**Meta-VOI (Empirical as a 149-row receipt, 2026-09-18):**
[`wotai-dev/typesafe-jev-tools`](https://github.com/wotai-dev/typesafe-jev-tools)
asks whether the decision needs a model at all: regex/DNS/query → no
model; one-second human from shown text → System One; multi-step or
prose → frontier. Same 149 business rows: Jev 79.9% vs Haiku 4.5 83.2%;
Jev 1.6× faster, not 20–200×; Jev confidence monotonic, Haiku inverts
in 0.80–0.95. If you do not *branch on confidence*, use whatever you
already have (`notes.md` §42).
**Training-data VOI (Empirical as README architecture,
2026-09-18 ~21:39):**
[jev-triage](https://github.com/ThyFriendlyFox/jev-triage) —
pay for an expensive teacher or a human only where
confidence says the label will change the outcome. High-conf
accept is nearly free. Soft-label full distributions for a
local student; **real outcomes** stay the training targets.
Do not distill Jev as teacher of record (~68% ceiling).
Cost sketch *theirs*: ~$21 vs ~$8,400 LLM judge for 1M ×
500-tok. `notes.md` §61.
**Retrieve-then-state (Empirical as an axis proof, not a knowledge
estimate):** if the answer is not in `state`, **buy the passage first**,
then ask. Atlas history suite: wrong @ 0.90 without context → right @
0.97 with the passage (`notes.md` §49; `mental-models.md` §boundary).
That observation is VOI with a named receipt. Do not rely on bare
recall.
**Fail-open wake/resume (Empirical as README safety table; 21/21 is
smoke, 2026-09-18 ~16:48):**
[wakegate](https://github.com/shitianfang/wakegate) — skip a sleeping
agent's LLM turn only if Jev answers **and** p(wake) < 0.2; user
message / nothing-to-judge / skip-limit / error / unsure all **wake**.
Horvitz mixed-initiative: pay for the turn iff EV(decision) beats
the token cost. Savings unmeasured. Same-author scenarios+question;
not a benchmark (`notes.md` §51). Contrast pi-jev-approver
fail-closed without a key and jevgate cannot-block.
**Selective memory / scored recall (Empirical as README behavior;
9×3 is a hint, 2026-09-18 ~17:48):**
[carryforward](https://github.com/Dharundp6/jev-carryforward) —
verbatim ledger; Jev scores which facts are still live for the
task; constraints/corrections always return (never judged). Fail-
open dump if the scorer is down. Pay for a scored brief iff it
beats dumping the whole file. No accuracy claim until a proper
test (`notes.md` §55). Eval finding *theirs*: `recall`
**0/4** with tools available — SessionStart hook >
hoping. tools≠use (`notes.md` §68). Do not copy mcp add.
**Classify-first read (Empirical as README; Hypothesis as a
measured win, 2026-09-19 ~00:38):**
[jev-sift](https://github.com/kbhuw/jev-sift) — pay for a full
agent open iff the relevance (or typed question) says it might
change the act. Uncertain → closer look. Errors and truncation are
**not** evidence of irrelevance. Webpage fetch still costs
bandwidth; this saves the *agent's* read, not the download.
Mocks ≠ accuracy (`notes.md` §56).
**Decision-model latency cost (Empirical as a *negative*
on sync Jev; 2026-09-18 ~23:40):**
[slo-router](https://github.com/zeeshan8281/slo-router) —
pay for live Jev features on the routing hot path iff
expected decision quality beats **hundreds of ms** tail.
On their fixture, same routes/accuracy as local features;
p95 **77.93 → 490.38 ms**. Author: keep Jev off the
synchronous path for this workload. **Hunch:** Harbor-style
measurement of decision-model latency is mandatory before
claiming “Jev routing.” Eight-row demo is not a benchmark
(`notes.md` §63).
**Human-review VOI (Empirical as README architecture;
hunch as a placement):**
[jev-lens](https://github.com/rashedInt32/jev-lens) —
calibrated “do I need to look / which files / strip
debris?” Never blocks the agent; never says green unless
sure (`JEV_LENS_GREEN` 0.9). Minimize expected human cost
under **false-green** risk. Attention filter, not a
permission gate. Companion
[jev-lens.nvim](https://github.com/rashedInt32/jev-lens.nvim)
is display only. Distinct from jev-gates (stops writes)
and egma attention≠correctness (PR surface)
(`notes.md` §63). Distinct from
[dizk/jev-lens](https://github.com/dizk/jev-lens)
(pre-send views; 79% fewer tokens *theirs*;
`notes.md` §68).
**Pre-send token-econ (Empirical as 500-trajectory
bench; 2026-09-19 ~03:38):**
[jev-lens](https://github.com/dizk/jev-lens) — pay to
send a line iff it changes the next edit. Compress
**before** first send; post-send prune cost 17% more
because it broke the prompt cache. Code sent in full
unless Jev is confident. Harm: 2/26 later edits missed
their block. Distinct from rashedInt32/jev-lens.
Do not copy npm (`notes.md` §68).
**Skill-library VOI (Empirical as README architecture;
2026-09-19 ~01:47):**
[skillranker](https://github.com/Dicklesworthstone/skillranker)
— pay to load a skill iff it changes the next step.
Abstention ("none of these") is first-class. Failed hook
recommendation is quiet fail-open. Distinct from
skill-broker (grants). Compose with combinators
(`notes.md` §66).
**Same-intent cache admit (Empirical as n=100 live eval;
2026-09-19 ~04:39):**
[jevcache](https://github.com/kushals256/jevcache) — pay
for the LLM iff Jev says the intent is **not** the same.
Exact SHA-256 first; fail-open to upstream. 0 FP / recall
0.38 *theirs*. Stream/tools/multimodal bypass. Do not copy
npx (`notes.md` §69).
**Human-feed VOI (Empirical as unreviewed goldens;
qualify the owner; 2026-09-19 ~04:39):**
[ThinkyMiner/Winnow](https://github.com/ThinkyMiner/Winnow)
— pay for a click iff the card says read/skim. Distinct
from kevinpita/winnow (context sieve). 80%/90% *theirs*.
Do not copy unpacked-extension how-to (`notes.md` §69).
**Second-call VOI (Empirical as README + offline pytest;
license null; 2026-09-19 ~04:39):**
[hermes-jev-router](https://github.com/rsdkrasen/hermes-jev-router)
— pay for the *next* main-model call iff Jev says
generation is still required (WHETHER/HOW/WHAT). Skip-next
needs a core patch. Fail-open. Do not copy plugin how-to
(`notes.md` §69).
**Hunk-review VOI (Empirical as 22-run cost table;
2026-09-19 ~05:46):**
[prune-review](https://github.com/shubhangi013/prune-review)
— pay for generative review of a hunk iff Jev says it is
worth looking at (and the safety escarpment does not force
keep). Target ~20%; measured 1.18% with a 305% outlier
*theirs*. Cost not quality. Do not copy pnpm
(`notes.md` §70).
**Intent-search VOI (Empirical as CLI; under
construction):**
[jev-intent-review](https://github.com/yottayoshida/jev-intent-review)
— pay to judge a place the diff did not touch iff the
stated intent applies there. UNKNOWN is cheaper than a
false VERIFIED. Empty search ≠ proof (`notes.md` §70).
**Empty compact-proxy skip (description only; 2026-09-19
~06:43):**
[jev-context-pruner](https://github.com/IPECTER/jev-context-pruner)
— Codex compression-proxy slogan; repo empty. Not VOI
until there is a keep-set and a fail polarity
(`notes.md` §71).
**Batch ranking VOI (Empirical as README; 2026-09-19
~06:43):**
[jevfeed](https://github.com/fengyiqicoder/jevfeed)
— one Jev request per batch of ten; the distribution *is*
the ranking. Pay per *batch*, not per item (`notes.md`
§71).
**No-text-step VOI (Empirical as 95-call card):**
[jev-use](https://github.com/shitianfang/jev-use)
— pay the LLM only when writing is the job; 12 questions
in one call 186 vs 2,672 ms *theirs* (`notes.md` §71).
**Files-to-read VOI (Empirical as n=16 SWE; 2026-09-19
~07:49):**
[jevex](https://github.com/jimmyhealer/jevex) — pay for
Reads of cited ranges only. n=16 160s → 69s / $8.74 →
$3.13 / 16/16 both arms *theirs*. Keep n=8 finish 1/8 →
6/8. Rename of jev-semantic-explorer (`notes.md` §72).
**Commit-attention VOI (Empirical as 13 labelled):**
[commitjev](https://github.com/yodablocks/commitjev) —
pay a human iff a Noul clears 0.65 on the bad side;
middle band is review not a skip. Regex already settled
the literals (`notes.md` §72).
**Pi compact VOI (Empirical as latency table):**
[pi-jev-compact](https://github.com/dev-willbird1936/pi-jev-compact)
— pay Jev to keep/drop tool calls instead of an LLM
summary; fall back if savings <25%. 0.6 s replay vs 26 s
first spinner is host cost (`notes.md` §72).
**Empty compact-proxy skip (IPECTER runway too):**
[jev-runway](https://github.com/IPECTER/jev-runway) —
LICENSE-only Codex-proxy slogan; not VOI until there is
a keep-set (`notes.md` §72).
**Escalate-under-threshold VOI (Empirical as README;
life/business; 2026-09-19 ~08:37):**
[classifier-dev](https://github.com/mrmps/classifier-dev)
— pay a reasoning model **only** on single-label
answers below 0.7. Multi-label re-judge made it worse
(23 s) so the tier is ignored. gemini-3.8-flash helped;
other flashes did not. 0.7 is *theirs*. Cousin jev-use
(`notes.md` §73).
**Escalate-without-stall cousin (Empirical as README
delta; autonomy; 2026-09-19 ~09:50):**
[khordoo/jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab)
— pay S2 only under the confidence threshold, but
**never pause the reflex**. Log whether the returned
strategy was **consumed** (purple confidence), not
only that it arrived. 20% starting gate *theirs*
still soft. Local vs Live is an A/B of backends, not
a scored bake-off (`notes.md` §80).
**Split-question CU VOI (Empirical as README; desktop;
2026-09-19 ~09:51):**
[typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)
— pay three/four Choices in **one** request
(`kind`/`item`/`site`/`offscreen`) instead of one
255-way soup. Perception (crop+tile OCR, dates.py, AX
walk) is the expensive gather that rebuilds what
frontier reads from pixels for free. Exclusive
actions: overlap is loud doubt, not silent 1.00.
155× / $0.0002 is *theirs* on one screenshot, not a
taskset. Writer only when free text is the job
(`notes.md` §81).
**Partial-speech VOI (Empirical as README; voice;
2026-09-19 ~10:01):**
[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)
— pay 9–11 questions on every partial (~300 ms
*theirs*). Closed-set may act before the sentence
ends; free-text waits for final or 600 ms silence so
"search for alan" is not truncated. Numbered overlay
is cheaper than a second model. Spoken confirm is
not a gather. 27/27 fixtures *theirs*, not a taskset
(`notes.md` §82).
**Evidence-synthesis two-pass VOI (Empirical as README;
medicine/Cochrane; 2026-09-19 ~08:48):**
[choxos/jev-reviewer](https://github.com/choxos/jev-reviewer)
— fan-out every question over shared chunks (18-q
**4.6 s / $0.0101** *theirs*), then pay a second
**absolute** Noul only on the surviving lines. *Not
found* is cheaper than a paraphrase. Human tick is the
act that enters the review. **≠** egma-ai
(`notes.md` §74).
**Path-then-window VOI (Empirical as README; 2026-09-19
~16:52):**
[JevFind](https://github.com/Peu77/JevFind) — pay a path
Noul first (`--file-threshold 0.25`); pay window Nouls
only on surviving files (`--threshold 0.55`). Both still
soft. `--file-threshold 0` when recall matters. Keyword
still wins exact strings. **≠** jevex **≠** jev-semgrep
(`notes.md` §87).
**Frontier cascade VOI (Empirical as README; in-sample
cut; 2026-09-19 ~16:52):**
[jev-frontier-bench](https://github.com/manjunathshiva/jev-frontier-bench)
— pay Fable only when Jev top p < 0.9. Cascade 82.5% at
$4.41/1k *theirs* is **in-sample**. ChaosNLI JS 0.149
worse than uniform 0.127. Confidence = top of
probabilities, not a confidence field. **≠**
jev-frontier-100 (`notes.md` §87).
**Compaction-pi VOI (Empirical as README + bench;
2026-09-19 ~16:52):**
[fast-jev-compaction-pi](https://github.com/zaycruz/fast-jev-compaction-pi)
— pay one keep/drop Noul per paired tool call; fail-open
to pi's built-in LLM summary (no key / error / timeout /
`minReductionRatio`). ~50× vs LLM summary *theirs*.
**≠** pi-jev-compact **≠** pi-jev-compaction
(`notes.md` §87).
**Beam-search FS VOI (Empirical as README; 2026-09-19
~17:25):**
[findme](https://github.com/marc2332/findme) — pay Jev
only on listed names+metadata at each beam node, not
on file contents. Parent fallback ≤4 is extra
observation cost. Keyword/gitignore already answers
without a model. `notes.md` §88.
**Cache-vs-worker VOI (Empirical as README; 2026-09-19
~17:25):**
[jevsubrouter](https://github.com/leftspace89/jevsubrouter)
— do **not** pay cache-rebuild to save worker output.
Price the empty-context worker; keep the conversation
model. Stats are counts because worker tokens are
invisible from a hook. `notes.md` §88.
**Cheap decision-layer VOI (Empirical as README;
2026-09-19 ~17:49):**
[grok-bot-jev](https://github.com/Bodila51/grok-bot-jev)
— pay one cheap classify before browser/retry/research.
Shadow then honor. A/B proxies ≠ tokens. 13.0× is a
top-five cap. Skill cannot force a bot that ignores it.
`notes.md` §89.
**Question-preflight VOI (Empirical as README + studies;
2026-09-19 ~17:49):**
[jev-reliability](https://github.com/vcjdeboer/jev-reliability)
— pay to measure flip/framing *before* putting a number
behind an `if`. Nothing about accuracy. noul-gate
0.0%/12.5%/3.6% *theirs*. `notes.md` §89.
**Preview-first VOI (Empirical as README; 2026-09-19
~18:41):**
[jev-file-search](https://github.com/emilwagman/jev-file-search)
— filename/type/preview then deeper read.
jev-file-search scores not calibrated accuracy.
Recall unmeasured. 0.8 is *theirs*. **≠** JevFind.
`notes.md` §90.
**Rubric-rewrite VOI (Empirical as README; 2026-09-19
~18:41):**
[jev-linkmap](https://github.com/stas4000/jev-linkmap)
— TF-IDF candidates; Jev yes/no + anchor Choice.
jev-linkmap Jev never sees S2 prose. Anchors already
in copy. `notes.md` §90.
**Batch packing VOI (Empirical as README; 2026-09-19
~19:47):**
[alsoleg89/decide](https://github.com/alsoleg89/decide)
— alsoleg89/decide packing VOI. Keep bulk decisions
on disk; agent sees summary + review. 0.8 ≠ 80%
accuracy. **≠** jev-sift. `notes.md` §91.
**Screenshot-free / packing / HA fast-path VOI (Empirical as README;
2026-09-19 ~20:41):**
droidjev screenshot-free (~0.6 s/iter *theirs*).
Tewoto1 jevcu planner still writes (324–380 ms *theirs*).
ha-conversation-jev Jev→Grok. dsh-jev can only gate.
400ms Salesforce WebMCP. `notes.md` §92.
**Evidence-projection VOI (Empirical as README;
2026-09-19 ~21:41):**
[jackboykin/quarry](https://github.com/jackboykin/quarry)
— pay Jev only for which *spans* to read; agent
reads the file. quarry evidence projection.
Fail-open 5 s. Score ≠ truth. `notes.md` §95.
**Beyond SWE (Hypothesis until you log
act/outcome pairs):** full PDF vs abstract; customer call vs CRM fields
that already fail a hard rule (credit limit is exact); blood test vs
wait. **Counterexample**: gathering until p = 0.99 on an irreversible
act that needed a probe, not another Noul. **Test**: a labeled log
where the extra observation changed the *act* often enough to pay;
score the cost of the observation too. Until that log exists, this card
stays **Hypothesis**. Links: `mental-models.md` §VOI, §decision.

## 7. Signal detection → criterion, not accuracy

**Method**: Green & Swets detection theory; ROC / PR operating points.
**Transfers**: a yes/no Noul is a noisy evidence variable; **d′** is
separability on *your* population; the **criterion** t is where policy
places the bar given base rates and costs. Shift t when the base rate
shifts (incident week, flu season, inbox after a launch) without
retraining "to be more careful." Fail-open vs fail-closed is a criterion
choice. **Does not transfer**: accuracy as the summary when the class is
rare; copying 0.7 from a blog; treating d′ as a vendor property;
thresholding a listwise or CLIP affinity as if it were P(signal)
(`judgment-class.md`).

```text
Noul ≈ evidence variable (noisy)
criterion t from costs and base rate     # policy
ROC / PR on YOUR labeled cases           # you owe this plot
report hits / false alarms at the operating point, not accuracy
```

**Example (Empirical as family shape):** firehose / Near Here moderation
— judge once, re-policy in code.
**CI merge-gate (Empirical as README / demo, 2026-09-18 ~16:48):**
[latch](https://github.com/CaseReed/latch) — false PASS on a real bug
>> false BLOCK on infra; criterion lives in the policy table, not in
the cause label (`notes.md` §51).
**Physical-world criterion (Empirical as README +
measurements; 2026-09-19 ~03:38):**
[HA-Jev](https://github.com/AboveColin/HA-Jev) —
confidence gating on typed sensors; **not** for locks /
heaters / smoke. `background:` on the question triples
laundry separation *theirs*. Treat 0.9 as higher than
0.6, not as right nine times in ten (`notes.md` §68).
**Portable HA control (Empirical as README; 2026-09-19
~16:52):**
[ha-switchboard](https://github.com/grayslawson/ha-switchboard)
— HA remains source of truth and execution; Jev typed;
one bounded LLM handoff; allowlist / freshness /
idempotency / post-state verify. **≠** HA-Jev. Not for
locks/heaters. Leveson card: mapping §8 (`notes.md` §87).
**Stop-hook attention (Empirical as owner-run smoke):**
[jev-preflight](https://github.com/muse0509/jev-preflight)
— 0.85 uncalibrated; fail-open; one reinspect. Criterion
for *redirect*, not for *block* (`notes.md` §68).
[`jp-sns-jev7-estimator`](https://huggingface.co/kokuren/jp-sns-jev7-estimator)
is the rare-class warning in one table: seven distilled teacher scores
that the card says are **not** calibrated probabilities, and `threat`
F1@0.5 = 0.0000 while mean accuracy@0.5 looks fine. Criterion, not
accuracy (`notes.md` §33). **Beyond SWE (Hypothesis until plotted):**
phishing screen; "is this a real deadline?"; hiring screen (base rate of
qualified applicants is the thing that moves). **Counterexample**:
retrain the model because last week's incident made you "want fewer
misses" — that was a criterion shift. **Test**: ROC/PR on held-out *your*
cases; report the operating point you actually ship. **Hypothesis** for
non-SWE plots. Links: `mental-models.md` §SDT; evaluator script for
threshold/cost sweep.
**Operator owns the criterion (Empirical as measured OMP
suppression, 2026-09-18 ~22:38):**
[omp-greenlight](https://github.com/SemetricLabs/omp-greenlight)
— four presets, each measured for prompts removed *and*
unsafe auto-approvals. Default **40.9%** / **0 of 94** on
the 140-row corpus. The plugin **never self-tunes** the
safety bar: a self-adjusting bar cannot be audited by the
person accepting the risk. Live traffic has no labels.
Not a sandbox. `notes.md` §62.
**Exactness raises a floor, does not override capability
(Empirical as live analysis; 2026-09-18 ~23:40):**
[slo-router](https://github.com/zeeshan8281/slo-router) —
the exactness feature lifts the quality floor; it never
bypasses health/context/tool checks. 3/8 task-label
disagreements still did not change routes. **Hunch:**
signal-detection framing — a quality cue is a criterion
shift, not a capability override (`notes.md` §63).
**Privilege ≠ verdict (Empirical as certification):**
[construct-auto-classifier](https://github.com/godspede/construct-auto-classifier)
— `sudo` changes blast radius, not whether the act is
benign. Operator owns `minConfidence` / `riskThreshold`.
Jev 0 dangerous / 975; chat models leaked. **Hunch:** do
not threshold a privilege token as P(unsafe)
(`notes.md` §63).
**Ranking ≠ calibration (Empirical as 8,000-judgment
audit; 2026-09-19 ~00:39):**
[does-jev-confidence-mean-anything](https://github.com/Adilmp/does-jev-confidence-mean-anything)
— AUC **~0.91** (ranking works) while stated p is shifted
toward "yes": when Jev said **~75%**, humans flagged
**~10%**. Two-parameter recalibration removes **~96% of
ECE** without changing rank. Vendor "calibrated" here is
**rank-correlation**, not frequency units. Never
hard-threshold raw p as if it were P(event) without
**domain** recalibration (`jevcal`; ~100 labelled rows).
One dataset (`civil_comments`); do not cite `threat` (n=1).
License null. `notes.md` §64.
**OOD / AUC ≠ ECE (Empirical as 900-ticket + 3 public
benches; 2026-09-19 ~01:47):**
[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)
— in-domain public benches look almost honest (OpenBookQA
ECE 0.024 / T 0.96). On an **unknowable** org-policy
priority label absent from the text: 44.7% acc, mean
stated p **0.74**, ECE 0.325, refit T **3.40**. Sign
**flips by type** on the same tickets: Choice/Score
overconfident (T ~3.3), boolean underconfident (T 0.66).
Do not threshold the TypeSafe `confidence` field (worse
than max-p here). Complements does-jev-confidence
(in-domain humans) and dinostomp (instrument).
Gateway exposes no model version. `notes.md` §66.
**Sureness over the vector (Empirical as 60-q reverse-
engineer + library; 2026-09-19 ~02:38):**
[how-sure-is-jev](https://github.com/adarc8/how-sure-is-jev)
— max_prob / margin / entropy / gini / perplexity (plus
Score `spread` and Kass–Raftery `log_odds`) → one
`[0,1]` consensus and bands CERTAIN | CONFIDENT |
LEANING | TORN | CLUELESS. Choice `confidence ==
max_prob` to 3 decimals *theirs*; max_prob is the
**most generous** metric (75/25 → 0.5 vs entropy 0.19).
Thresholds are opinions. Pair with this OOD card: do not
threshold TypeSafe `confidence`. Zero-dep MIT.
`notes.md` §67.
**Conflict ≠ ignorance (Empirical as NCML field note v0.3
*theirs*; 2026-09-19 ~04:39):**
[jev-typed-evaluation-collapse](https://github.com/mleyvaz/jev-typed-evaluation-collapse)
— same evidence, three schemas. Noul/boolean collapses
conflict 0.50–0.57 vs ignorance 0.46–0.48; Choice with
named `conflicting_evidence` / `insufficient_evidence`
separates p=1.0; binary Choice without an escape is
lexically biased (red 0.67–0.85). Score exploratory
(severe conflict 2.04 vs no-evidence 3.95). Schema is
the interface. License null. `notes.md` §69.
**BBQ stereotype / uncertainty as SDT (Empirical as
full 58,492 *theirs*; 2026-09-19 ~05:46):**
[jev-bbq-experiment](https://github.com/simonmesmith/jev-bbq-experiment)
— Jev 1.13.0 **56,900 / 97.28%**; amb 99.96% / inf
94.60%; BBQ bias **0.04 / 0.34**; **$0.3429 / 7.75 min**.
12 of 13 ambiguous errors stereotype-aligned;
informative misses mostly `unknown` (1,487 / 1,579).
Order diagnostic 1/484 (0.21%). Dataset CC BY 4.0 BBQ.
License null. **Not a general bias cert** — English/U.S.
QA template does not certify hiring/lending/healthcare.
Always-unknown would score 50%; 97.28% is not abstention
theater. Pair with
[system-one-responsible-ai](https://github.com/david-j-lustig/system-one-responsible-ai)
(size-0 framing stub). `notes.md` §70.
**Cookbook moderation as a cost-sensitive dial (Empirical
as small samples, not a bench; 2026-09-19 ~06:43):**
[jev-cookbook](https://github.com/nexibeo/jev-cookbook)
recipe 12 — five hazard Nouls; act when sure, hold the
middle, escalate self-harm early. 16–36 handmade items;
authors say not benchmarks (`notes.md` §71).
**Dual-channel ECE / like-for-like (claim-audit, not
endorsement; 2026-09-19 ~06:43):**
[openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0)
— correctness-head ECE is not distribution ECE. Open PR
#1: like-for-like dist 15.13% vs Laya 21.40%; Jev 14.40%
slightly lower on that channel; do not put 1.44% beside
21.40% as a 15× win. Throughput ≠ latency. **≠**
IamBusy/OpenJev (`notes.md` §71).
**Commit middle band (Empirical as 13 labelled;
2026-09-19 ~07:49):**
[commitjev](https://github.com/yodablocks/commitjev) —
the operating point is a **three-way** criterion
(pass / review / warn), not a rounded yes. 0.65 is
theirs, not a universal t. Five clean is a small
control (`notes.md` §72).
**English-checkpoint confident-wrong OOD (Empirical as
MASSIVE; 2026-09-19 ~07:49):**
[laya-multilingual](https://huggingface.co/convaiinnovations/laya-multilingual)
— Khmer 0.000 acc at 0.952 confidence; mean conf never
< 0.885. **Gating cannot catch it.** Route by script
before the forward pass. Ships uncalibrated
(`notes.md` §72).
**Coverage ≠ correctness (Empirical as GUI 336):**
[chakuho](https://github.com/taku-me/chakuho) — 8B
coverage 1.00 while `__none__` hits 3/30. Coverage is
format-mass (`notes.md` §72).
**Peaked schema-scorer (Empirical as Hub eval):**
Hub schema-scorer v2 Choice 0.841 *theirs*; treat p as
ranking. GitHub 404 (`notes.md` §72).
**Escalate-under-threshold criterion (Empirical as
README; 2026-09-19 ~08:37):**
[classifier-dev](https://github.com/mrmps/classifier-dev)
— 0.7 is an operating point on *their* labels (emotion
≥0.9 → 82% / <0.5 → 29% *theirs*). Multi-label does
**not** share it. Do not copy 0.7. `notes.md` §73.
**Self-reported JSON ≠ calibrated Noul (Empirical as
eval caveats; 2026-09-19 ~08:56):**
[githubnext/localjev](https://github.com/githubnext/localjev)
— entropy confidence is computed from a generated
vector. Bake-off: do not treat outputs as calibrated
(wrong-BoolQ high conf → large NLL; 40 samples/task
*theirs*). Wire-compat ≠ logit-equiv. `notes.md` §75.
**Laya 0.85 still soft / post-T ≠ raw ECE (Empirical
as README; 2026-09-19 ~09:07):**
[NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)
— README `conf >= 0.85` is *theirs*, not Harbor-
calibrated. Khmer 0.000@0.952. vs-Jev ECE **0.081** is
post-temperature (raw 0.213 vs Jev 0.144). Banking77
token-budget, not a Jev loss. `notes.md` §76.
**External census ≠ scored bake-off (Empirical as
tweet; 2026-09-19 ~09:14):**
[@airesearch12](https://x.com/airesearch12/status/2101259522933186879)
— named ~18 openjevs + first leaderboard promised
"today." **≠** jevbench v1.1. Watch
[jev-models](https://benchmarkheaven.com/jev-models);
do not paste live ranks here. GLiNER2 and routers on
the list are **class-boundary**, not identity. Likes
ephemeral. Incomplete vs Laya/localjev/kev is lag.
Harbor still wants cal / cost / latency / silent
fallback named. `notes.md` §77.
**JevBench v1.2 scored board (Empirical as board +
RESULTS; 2026-09-19 ~09:24):**
[jev-models](https://benchmarkheaven.com/jev-models)
protocol `jevbench::v1.2`. Score = geometric mean of
I/C/S/K at 25% each. Jev 1.13.0 **75.3** / SemIf
**74.6** *theirs*. Calibration **on** the rank (delta
from §67). Luna I=96.8 rank #7. Self-host latency
×2 is an assumption; many costs est. Option-order
72%→21%. Laya absent (gap, not named-excluded).
Qwen3.8 27B Chutes TEE **≠** Archer. **≠** tweet
census **≠** v1.1 87.6. `notes.md` §78.
**Question preflight as SDT (Empirical as README +
studies; 2026-09-19 ~17:49):**
[jev-reliability](https://github.com/vcjdeboer/jev-reliability)
— flip rate is a criterion on *consistency*, not
accuracy. noul-gate 0.0%/12.5%/3.6% *theirs*. Confidence
straddling τ flips. **≠** dinostomp. `notes.md` §89.
**Triage buckets as criterion (Empirical as README;
2026-09-19 ~17:49):**
[dairui1/jev-lab](https://github.com/dairui1/jev-lab)
— p(urgent) 0/21/41/75/100% *theirs*; route 0.35–0.65
to human_review. 91% vs 79% is discrimination, not a
seal. **≠** BrendanH18/jev-lab. `notes.md` §89.
**Ranking ≠ frequency (Empirical as README;
2026-09-19 ~18:41):**
[jsort](https://github.com/keltokhy/jsort)
— logits are relative. Noul not Choice for scale.
Choice 93% extreme vs Noul 28% mid *theirs*. A logit
gap is not a frequency. `notes.md` §90.
**Unofficial CLI confidence ≠ winner p (Empirical as
README; 2026-09-19 ~18:41):**
[2389-research/judgement](https://github.com/2389-research/judgement)
— 2389-research/judgement license null. confidence ≠
winner p. Pin `jev-1.13.0` vs alias 24h. Live
arithmetic ≠ accuracy. **≠** jevql. `notes.md` §90.
**Calibration as product (Empirical as README;
2026-09-19 ~19:47):**
[Jev-Calibration](https://github.com/AnthusAI/Jev-Calibration)
— Jev-Calibration Platt ECE 0.117→0.052. Choice
50–95% sits at ~50–57%. `confidence` field ≠ top-p.
[jev-calibration-arena](https://github.com/pmcclelland/jev-calibration-arena)
— jev-calibration-arena never acts. **≠** jev-arena.
`notes.md` §91.
**Soft-score criterion (Empirical as README;
2026-09-19 ~19:47):**
[typed-gate](https://github.com/harshpuri84/typed-gate)
— typed-gate band [0.40,0.60] is refusal. 0.51 is
not a yes. rh-guard owns the gate cousin. `notes.md`
§91.

## 8. Control structure → sensor ≠ constraint (Leveson)

**Method**: STAMP / STPA — safety is a control problem, not a
component-accuracy problem
([Leveson STAMP intro](https://psas.scripts.mit.edu/home/wp-content/uploads/2016/04/STAMP-Intro-2016.pdf)).
**Transfers**: judgment as a *sensor* in a loop you own; constraints in
code, policy, checklist, two-person rule, physical interlock. STPA asks
what happens when the sensor is wrong, delayed, spoofed, or TOCTOU.
**Does not transfer**: a 99% Noul as the safety constraint; "the model
was confident" as the excuse for an unsafe control action; deleting the
interlock because ECE looked excellent in-distribution.

```text
constraint  = "do not give the drug without the allergy list"   # policy
sensor      = Noul("does this note mention an allergy?")        # model
actuator    = the person, the agent, the pump                   # not the model
STPA        = table of unsafe control actions if the sensor lies
```

**Example (Empirical as instrumentation shape):** OpenSmoke — cheap
judgment over every step so humans only autopsy flags. That is NATM
instrumentation of the control structure, not a safety case.
**Beyond SWE (Hypothesis):** hospital allergy list vs note-mentions-allergy;
kitchen thermometer vs "looks done"; two-person wire rule vs "this
invoice looks right"; incident command head-count vs "still contained?"
**Counterexample**: the agent proceeds because Noul 0.99. **Test**: name
the constraint that remains when the sensor is deleted; fill the unsafe-
control-action table. Ownership split is **Contract** as a rule
(`formal-methods.md`); the domain examples are **Hypothesis** until
labeled. Links: `mental-models.md` §Leveson; `boundary-audit.md` TOCTOU.
**Capability kernel (Empirical as README architecture, 2026-09-18
~19:48):** [interlock](https://github.com/somoore/interlock) — LLM
ring 3; kernel ring 0; secrets never enter the agent; closed action
space; Jev (or stand-in) is the sensor; `policy.py` decides
BLOCK/ASK/ALLOW. Type-safe ≠ correct; irreversible behind a
threshold **and** a human. Anti-pattern: launch-week firewalls that
ask "dangerous?" after the LLM already decided with real secrets in
scope. Distinct from toolgate (pre-exec of a proposed call). 38-case
set tunes the local judge, not a blind paper. `notes.md` §59.
**Host deny stays above the sensor (Empirical as README
safety model, 2026-09-18 ~22:38):**
[omp-greenlight](https://github.com/SemetricLabs/omp-greenlight)
— `bash.patterns: deny` is the constraint and fires ahead
of Jev prompt-suppression. Jev is permission-*probability*,
not permission. Agent prose withheld after 0→3 corpus
misses. Never shadows a built-in tool (would bypass deny).
`notes.md` §62.
**Spoken confirm ≠ constraint (Empirical as README;
2026-09-19 ~10:01):**
[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)
— destructive Noul is a sensor; spoken "confirm" is
not an interlock. Control-port reach grants. rh-guard
owns the gate cousin (`notes.md` §82).
**Wrap-as-execution is the constraint (Empirical as
README; 2026-09-19 ~10:20):**
[AgentGhost](https://github.com/reddpy/AgentGhost)
— the wrap *is* the actuator path; Jev is the sensor
on leftovers after rules. ASK throws; fail-closed on
judge error. `AUTO_APPROVE` is not a constraint.
rh-guard owns the gate cousin (`notes.md` §83).
**Judgment ≠ permission (Hypothesis / outline only):**
[skill-broker](https://github.com/adamjralph/skill-broker)
— code owns grants; Jev scores relevance and **never
grants access**. Jev down never broadens the catalog.
Not a production recipe. `notes.md` §62.
**Contracts on effects, not tokens (Empirical as
certification; hunch as FM angle):**
[construct-auto-classifier](https://github.com/godspede/construct-auto-classifier)
— the constraint is reversibility / blast radius, not a
`sudo` allowlist. Independent risk Nouls are sensors;
policy (minConfidence ∩ riskThreshold ∩ fast-deny) is the
constraint. Fail-closed when the sensor is missing.
**Landed-script** is a merge-gate receipt, not a name.
**Headless** escalation is deny-and-report, not
auto-approve (`notes.md` §63, §68).
**Attention filter ≠ permission (Empirical as README;
hunch as placement):**
[jev-lens](https://github.com/rashedInt32/jev-lens) —
never blocks the agent; never grants or withholds a
write. Complements skill-broker (Jev never grants access)
and omp-greenlight (operator owns the bar)
(`notes.md` §63).
**Jev supplies evidence, code owns authority (Empirical
as README slogan; 2026-09-19 ~00:39):**
[actiongate-jev](https://github.com/omkarghugarkar007/actiongate-jev)
— deterministic policy is the constraint; Jev is the
sensor. A positive score never overrides RBAC / schema /
limit failure. Financial / destructive / credential fail
closed if Jev is down. Distinct from construct (shell
effects) and interlock (secrets never in agent)
(`notes.md` §64).
**Wrap-as-execution cousin (Empirical as README;
2026-09-19 ~10:20):**
[AgentGhost](https://github.com/reddpy/AgentGhost)
— the wrap *is* execution; rules prove allow/deny/ask
before Jev; ASK throws. Distinct from actiongate
(policy/RBAC is the hard gate, Jev only evidence).
`notes.md` §83.
**Turnstile clone (Empirical as README architecture;
2026-09-19 ~01:47):**
[turnstile](https://github.com/zyphr-labs/turnstile) —
same doctrine (policy first; Jev remainder; evidence ≠
authority) with receipts and **threshold replay**. Missing
Jev → Review, not a silent allow. Starting 0.85/0.35 are
not calibrated. Experimental alpha. `notes.md` §66.
**Advance gate / coverage ledger (Empirical as README +
BEYOND-JEV.md; 2026-09-19 ~02:38):**
[seal](https://github.com/Reasonofmoon/seal)
— sensor (Strike / Jev / code) ≠ constraint (Seal +
coverage.path). Exception queue must be visible. Mint ≠
product brain. Effects locked while escalations open.
`notes.md` §67.
**Never confidently wrong (Empirical as TLA+ + chaos
table):** [jev-labs](https://github.com/copyleftdev/jev-labs)
— the constraint is "may escalate; must not return a
confident wrong." Hard-gating without that path is
soundness theater's inverse. Synthetic pharmacy, not
clinical. `notes.md` §67.
**Skill-broker sibling (Hypothesis / outline; delta
§67):** grants stay in code beside turnstile (runtime)
and skillranker (advisory). Same doctrine, different
hole. `notes.md` §62, §67.
**Conversational constraint sensor (Empirical as
79-session bench; 2026-09-19 ~05:46):**
[pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)
— user constraints persist as structured state across
compaction; replayed **without** calling Jev again.
Jev classifies KEEP/LIFT/…; **never writes policy**.
Side-effecting calls checked before they run. Fail-open.
Shadow default. *Theirs:* recall **98.5%** / false
block **0.0%** / lifecycle 100% / task success 98.7% /
**$0.000058**; mid-session rule change 8/13 off vs
0/13 on. Distinct from actiongate (RBAC/schema
authority) — this is *what the user meant* surviving
the context window. Do not copy `pi install`
(`notes.md` §70).
**Pi control-plane sensors (Empirical as README; license
null; 2026-09-19 ~06:43):**
[pi-jev-control](https://github.com/goodruizhan/pi-jev-control)
— router / tool gate / retry / sieve / review / GUI are
named sensors; code owns model switch, session bytes,
and click. GUI never force-clicks. Distinct from pi-heed
(constraint ledger) (`notes.md` §71).
**jev-use gate never grants (Empirical as 12/12
fail-open):**
[jev-use](https://github.com/shitianfang/jev-use)
— PreToolUse deny/ask; missing Jev does not deny
(`notes.md` §71).
**Inbox policy is the constraint (Empirical as README;
2026-09-19 ~07:49):**
[mailordinal](https://github.com/Milo318/mailordinal)
— typed signals are sensors; the 100-point policy and
the review lane are constraints. The model never sets
queue order. Humans own ambiguity (`notes.md` §72).
**Agnes branded as Jev is not a sensor (identity lock):**
[hermes-plugin-jev](https://github.com/Mrmimee/hermes-plugin-jev)
— chat-completions path wearing Choice/Noul/Score
vocabulary. Distinct from hermes-jev-router
(`notes.md` §72).
**Silent fallback is an unsafe control action
(Empirical as eval/README; 2026-09-19 ~08:37):**
[classifier-dev](https://github.com/mrmps/classifier-dev)
— delisted primary left granite serving F1 **0.546**
vs advertised ~**0.800** for weeks (*theirs*). Digest
now marks `FALLBACK`. The constraint is honesty about
which model answered, not a better softmax.
**rh-guard owns the eval-integrity gate**; this is the
lived product cousin (`notes.md` §73).
**HA remains execution (Empirical as README; 2026-09-19
~16:52):**
[ha-switchboard](https://github.com/grayslawson/ha-switchboard)
— Jev is the SENSOR (typed answers); HA is constraint
plus actuator (source of truth and execution). One
bounded LLM handoff. Allowlist / freshness / idempotency
/ post-state verify stay in code. **≠**
[HA-Jev](https://github.com/AboveColin/HA-Jev) (SDT
criterion in mapping §7). Not for locks/heaters. Skip
Archer (`notes.md` §87).
**Hybrid leftover / can-only-gate (Empirical as README;
2026-09-19 ~20:41):**
[ha-conversation-jev](https://github.com/luxus/ha-conversation-jev)
(license null; **1★**) — ha-conversation-jev Jev→Grok.
FAST_MIN 0.80 / NOUL 0.55/0.40 *theirs*. Whole-home
safety in **code**. **≠** HA-Jev **≠** ha-switchboard.
[dsh-jev](https://github.com/buberlo/dsh-jev) (MIT;
**2★**) — dsh-jev can only gate. HIGH delta of MED
§59. Default mock+shadow. Sensor, not a grant.
Do not copy OAuth `client_id`. `notes.md` §92.
**Calibrator / CI shadow / injection-firewall (Empirical as README;
cross-ref rh-guard; 2026-09-19 ~21:41):**
[seb4ez/jevguard](https://github.com/seb4ez/jevguard)
(MIT; **0★**) — jevguard calibrator/cache/escape.
Named escape + AMBIGUOUS_STATE. Cache is the exact
envelope (volatile masking). **≠** jevcache.
[guilhem/jev-ci-selector](https://github.com/guilhem/jev-ci-selector)
(license null; **0★**) — jev-ci-selector CI shadow mode.
Shadow default; enforce opt-in. skip_below 0.05 is
an experiment. Mandatory/path rules beat Jev.
[PavitarSinghArneja/one-dollar-tahoe](https://github.com/PavitarSinghArneja/one-dollar-tahoe)
(MIT; **0★**) — one-dollar-tahoe TypeSafe Jev defense eval.
Jev is SENSOR; blocklist is the exact remainder.
README has no ASR/FPR. rh-guard owns.
`notes.md` §95.
**Authorship / jevtest-as-merge-seal (rh-guard owns the
gate cousin; 2026-09-19 ~16:52):**
[jev-authorship-check](https://github.com/webstercharly/jev-authorship-check)
named Choice `uncertain` is a sensor, not courtroom
evidence. [jevtest](https://github.com/realZachi/jevtest)
0.85 still soft; the 0.15–0.85 band fails both polarities
— hard-gating a matcher as a merge seal is soundness
theater. rh-guard owns the eval-integrity gate cousin
(`notes.md` §87).
**Empty findings ≠ approval (Empirical as README;
2026-09-19 ~17:25):**
[stanley-code](https://github.com/devagrawal09/stanley-code)
— Jev is the SENSOR; `notChecked` is the coverage
ledger; there is no `pass`/`approved`. Exact signals
(`test.skip`, deleted assertions) prove before Jev.
Human `--promote-candidate` is the actuator; the
agent drafts. Soft Noul ≠ hard safety. rh-guard owns
the gate cousin if someone CI-gates on empty findings
(`notes.md` §88).
**Human every action (Empirical as README; 2026-09-19
~17:49):**
[Essentiel-Jev](https://github.com/JacquesGariepy/Essentiel-Jev)
— Jev SENSOR; human actuator; provider write +
read-back is the probe. Essentiel-Jev never authority. 0.75
provisional. **≠** jevmail **≠** mailjay. License null.
`notes.md` §89.
**Atom then sense (Empirical as README; 2026-09-19
~17:49):**
[enzo-mcp](https://github.com/mahawi1992/enzo-mcp)
— deterministic evidence is the constraint; Jev is
the remainder sensor; enzo-mcp UNKNOWN exposes gaps.
`allow_external_jev` is consent, not a grant.
**≠** jev-sift. `notes.md` §89.
**Pause-if-no-Jev (Empirical as README; 2026-09-19
~18:41):**
[ORIGIN-CIVILIZATION](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION)
— Jev SENSOR; world constraint is ORIGIN
pause-if-no-Jev. validResponse sums-to-1. LLMs plan
never decide. **≠** Essentiel-Jev. `notes.md` §90.
**Local AUTO_ACT is not a Noul (Empirical as README;
2026-09-19 ~18:41):**
[jevbrain](https://github.com/Synxneuos/jevbrain)
— n-gram/anchor overlap daemon. jevbrain AUTO_ACT is
not a Noul. τ≥0.80 theater if sold as calibrated
System One. README MIT vs SPDX null. **≠** TypeSafe
Jev. `notes.md` §90.
**Crawler risk bands (Empirical as README; 2026-09-19
~18:41):**
[jev-crawlers](https://github.com/russfranky/jev-crawlers)
— jev-crawlers risk bands never raw boolean. Verify
grounding, not exec. rh-guard owns the gate cousin.
`notes.md` §90.

## 9. Search / control loops → one substituted classifier step

**Method**: beam, A*, MCTS, hiring funnel, literature snowball, sales
stages, cook/rest/check. **Transfers**: the *algorithm* stays yours. The
judgment-shaped hole is a prior, a prune, a leaf value, or a "does this
branch still look live?" Noul (`methods-catalog.md` search rows;
mapping §5 is the taxonomy-beam special case). Economics inversion:
per-node judgments were known and too expensive; they are now default.
Control: hysteresis, continue / stop / retry / verify — the model
estimates named probabilities; the controller is a table with memory.
**Bounded Pi supervisor (Empirical as README policy, 2026-09-18
~16:48):** [jevons](https://github.com/LilDojd/jevons) — not a second
agent; Jev interprets evidence; code owns freshness/limits; default
recovery **shadow**; steering never generates commands
(`notes.md` §51). Distinguish from pi-jev-approver / pi-jev-context.
**Does not transfer**: Jev as the planner-writer that picks its next
tool *and writes* the call; bandits without observed rewards;
speculative depth without a simulator; PufferLib Ocean scores as a
capability claim (`formal-methods.md` DST trio). **Does transfer as a
split** ([jeffrey](https://github.com/thomasbrueggemann/jeffrey)): Jev
owns next-tool / progress / risk / done; the LLM **only fills args**;
the loop is Jev→tool→Jev. Pick ≠ fill. Mapping §9 still rejects the
fused planner.
**Continuous-control cousin (Empirical as README delta;
2026-09-19 ~09:50):**
[khordoo/jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab)
— the *algorithm* is the physics loop; the substituted
classifier step is typed flight Choice every tick.
Optional S2 is one-use strategy, not the next act.
Escalate **without stalling**. Local rule-based vs
Live `jev-latest` is an A/B of backends (**≠**
githubnext/localjev). Seed = geometry ≠ replay. No
pixels. 20% still soft. S2 never grants. Do not copy
npm / `.dev.vars` (`notes.md` §46, §80).
**OCR+AX desktop cousin (Empirical as README;
2026-09-19 ~09:51):**
[typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)
— the *algorithm* is the capture→OCR+AX→Choice→act
loop; the substituted classifier step is exclusive
kind/item/site. Perception stays in code. Writer is
leftover generation. Decision never ships pixels; the
answer reader may. Do not copy `uv` (`notes.md` §81).
**ASR voice-browser cousin (Empirical as README;
2026-09-19 ~10:01):**
[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)
— the *algorithm* is debounce→snapshot→Choice→Playwright;
the substituted classifier is 9–11 questions on a
partial transcript. ASR stays off-model. Confirm is
not a grant. Do not copy `npm` (`notes.md` §82).
**Hybrid S1 / closed verb menu (Empirical as README;
2026-09-19 ~16:52):**
[anima3](https://github.com/hulryung-uo/anima3) — the
*algorithm* is the tick loop + hard safety (HP 35%
menu shrink); the substituted classifier is a pick
among valid verbs. Qwen logprob **default**; jeff
pluggable and confidently flat on magnitude. Scene is
an a11y tree, not a screenshot. Do **not** invent Laya
as a backend (user brief ≠ live README). Tests first:
hulryung/jev-testbed. Skip Archer (`notes.md` §87).
**Full-distribution optimizer (Empirical as README /
mock Space; 2026-09-19 ~16:52):**
[jevloop](https://huggingface.co/spaces/async-dime/jevloop)
— the *algorithm* is UCB1+CEM; the substituted
classifier is Jev as a **value function** over the full
distribution, not argmax. **No LLM in the loop.** Mock
mode is the Space default; do not quote mock-mode
quality. **≠** Ax/DSPy (`optimizer-integration.md`;
`notes.md` §87).
**NL memory → beam-search FS (Empirical as README;
2026-09-19 ~17:25):**
[findme](https://github.com/marc2332/findme) — the *algorithm* is beam search (+ parent fallback ≤4);
the substituted classifier is Jev ranking listed
names+metadata. gitignore / symlink skip stay in
code. **≠** JevFind. Life/knowledge, not only SWE
(`notes.md` §88).
**Persona state-machine (Empirical as README;
2026-09-19 ~17:49):**
[apa-persona-engine](https://github.com/AiPersonacademy/apa-persona-engine)
— the *algorithm* is the registered graph; Jev is
the transition sensor; LLM writes leftover copy.
<250 ms ≠ microsecond marketing. 0.75/0.80/0.85 still
soft. **≠** jev-harness. `notes.md` §89.
**S1 decide / S2 plan (Empirical as README;
2026-09-19 ~18:41):**
[ORIGIN-CIVILIZATION](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION)
— the *algorithm* is the civ loop; the substituted
classifier is Jev on every voluntary action; LLMs
plan never decide. ORIGIN pause-if-no-Jev.
validResponse sums-to-1. **≠** Essentiel-Jev.
`notes.md` §90.
**Seed/expand/judge/verify (Empirical as README;
2026-09-19 ~18:41):**
[jev-crawlers](https://github.com/russfranky/jev-crawlers)
— the *algorithm* is Unix-style crawler stages; Jev
is the judge/verify sensor. jev-crawlers risk bands
never raw boolean. `notes.md` §90.
**Physical/control atlas (Empirical as README;
2026-09-19 ~21:41):**
[Frank-ZY-Dou/awesome-jev](https://github.com/Frank-ZY-Dou/awesome-jev)
(license null; **0★**) — Frank-ZY-Dou/awesome-jev robotics/3D/control.
The *algorithm* is physics/kinematics; the substituted
classifier is typed text-state. One seed-0 ≠ a rate.
**≠** walidboulanouar/awesome-jev-use-cases.
Do not re-card jev-drone / khordoo / HA-Jev.
**Decision-as-plugin next-act (Empirical as README;
2026-09-19 ~21:41):**
[petercr/jev-orchestrator](https://github.com/petercr/jev-orchestrator)
(MIT; **0★**) — difficulty + policy thresholds + JSONL trace.
Next-act Choice; code owns policy. Description ≠ live
Choice set. `notes.md` §95.

```text
loop     = yours (beam / funnel / stages / MCTS / incident command)
hole     = prior | prune | leaf | "still live?"
probe    = simulator / thermometer / CRM amount / exit code
estimate ≠ measure — irreversible milestones concede only to the probe
```

**Example (Empirical):** jev-mcts grounded vs speculative fidelity in
types; probes-only concession (mapping §5).
**Decider ≠ executor (Empirical as README; 2026-09-19 ~05:46):**
[jeffrey](https://github.com/thomasbrueggemann/jeffrey) — the
*algorithm* is the agent loop; the substituted classifier step is
next-tool / progress / risk / done. Arg fill is generation, not the
classifier. Risk Score ≥ 0.5 pauses mutating tools. Stuck ladder:
withhold the looping tool, re-ask Jev (2 Jev / 0 steps). Distinct
from jev-handoff (typed baton around an existing host) and
browser-jev (Playwright executes). Do not copy npm (`notes.md` §70).
**Tree-of-Choices writer (Empirical as README demo;
2026-09-19 ~06:43):**
[jev-gpt](https://github.com/florian-hoenicke/jev-gpt)
— the substituted classifier step is *which word next*;
the model never free-generates. ~400 calls / 75 s / 2¢
*theirs*. Architecture demo. Distinct from jeffrey (pick
next-tool). License null (`notes.md` §71).
**Pick≠write plugin (Empirical as 95-call card):**
[jev-use](https://github.com/shitianfang/jev-use)
— judgment steps to Jev; writing stays generated
(`notes.md` §71).
**1-token selector (Empirical as GUI 336 + mario;
2026-09-19 ~07:49):**
[chakuho](https://github.com/taku-me/chakuho)
— the substituted classifier step is *which declared
label*; the generic LLM never writes. Numeric rules stay
in code (mario loss is misapplied "< 6 tiles"). Softmax
≠ Noul (`notes.md` §72).
**Beyond SWE (Hypothesis):**
snowball citations ("still on-question?"); sales stages ("still a real
opp?" — amount and close date stay exact); cook/rest/check ("looks done?"
— thermometer is the probe). **Counterexample**: a weekly LLM summary of
"how the project feels" instead of per-item instrumentation (the rejected
opposite of NATM). **Test**: greedy vs looped baseline on realistic cases;
inspect pruning failures; the probe, not the estimate, concedes. Links:
`mental-models.md` §search; `formal-methods.md` PufferLib row.

**Game loops as a calibration substrate (Empirical as a *shape*):**
[`vtrivedy/jev-plays-games`](https://github.com/vtrivedy/jev-plays-games)
— legal moves from code, one Choice over that set, text state, no
screenshot. Choice probabilities are **not** win odds. Author probe (12
calls, both option orders): both chess mates found; Connect Four
immediate win missed once reversed; Fool's-mate confidence 31%/37% so a
0.50 gate would reject correct mates. pcdServer Tetris is the same
hole on the constrained-AR surface. Not a strength rating.
`notes.md` §42; `validation.md`.

**Computer-use observe → score → act (Empirical as README /
architecture behavior, 2026-09-18 ~16:56):**
[gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast)
— the *algorithm* is the browser loop; the substituted classifier
step is scoring among observed a11y/DOM controls. Local GLiNER2 is
one backend; Jev Ultrafast / solari-reflex are the Jev backends of
the same hole. Code owns actuators, dates, freshness. `DONE` is not
the probe — application verifiers are. Contrast blackwood-rlcd
(screenshot input). Hybrid remote TYPE is generation, not the
classifier step (`notes.md` §52).
[Cua-S1](https://github.com/trycua/cua/tree/main/libs/cua-s1) is the
same substituted-classifier *job* on a specialist form contract
(option-attention; plan ≠ execute; not TypeSafe Jev; source-only,
`notes.md` §54).
**Harness productization of the same job (Empirical as PR body,
2026-09-19 ~00:48; draft):**
[Stagehand #2951–#2955](https://github.com/browserbase/stagehand/pull/2955)
— the *algorithm* is Stagehand's act/observe/extract loop; the
substituted classifier step is Jev pick among a11y candidates, then
code copies or acts. LLM fallback when the pick/gate/schema fails.
Extract 37/75 no-LLM ~0.5 s vs 4.37 s is *their* card; pick ≠
replacement. Cache-check errors never block replay. Do not merge
with demo-loop clocks (`notes.md` §57).

**Robotics text-state, same job different body (Empirical as
showcase class pattern, 2026-09-19 ~00:38):**
MuJoCo robot-arm on [jevable.com](https://jevable.com/): Jev does
not accept images; simplified geometry and contacts **as text**;
two-call split (what to do, then how to move). MOSS: Jev picks the
target; the robot picks up. Cousins: [jev-drone](https://github.com/RomanSlack/jev-drone)
(code at 500/50 Hz, Jev advisory 2.5 Hz); Doom JSON, not pixels.
Drawing-pixel-parallel is a **claim** — contrast MuJoCo honesty.
Do not replace A* or a Sudoku solver with a Noul. Archer still
Watch (`notes.md` §56).

**Structure induction over a bag (Empirical as a *shape*, 2026-09-18):**
[`Joymfl/dag-jev`](https://github.com/Joymfl/dag-jev) — unordered items
in, pairwise "does i depend on j?" judgments, DAG in `petgraph`. Code
owns topology; the model does not emit edges. Experiment; empty README;
no metrics this pass (`notes.md` §48). Same hole as taxonomy beam (§5):
judgment is a pairwise (or Choice) classifier step, not the scheduler.

**Combinatorial grid assembly ≠ extractive keep/drop (Empirical as a
negative):**
[`simonmesmith/jev-arc-agi-v1-experiment`](https://github.com/simonmesmith/jev-arc-agi-v1-experiment)
— Direct Jev cell-wise Choice on ARC-AGI-1: **4/400 (1%)**. Dimensions
~90%; complete grids rarely. Many small extractive decisions do not
add up to a consistent transformation. Search / a program / a
simulator stay in code (`notes.md` §49).

**Query planner as the envelope (author-reported, 2026-09-18):**
[@mmalisper](https://x.com/mmalisper/status/2101001041903009987) on the
Join Order Benchmark. Jev picking join order was **2× slower**.
Cardinality estimates helped when outside context informed the plan;
when Jev was wrong, one query was ~10× slower. Hybrid: Postgres plans
first; Jev overrides **only when confident** → **+12% geomean**, no
dramatic slowdowns. A Jev call is 100s of ms, not yet practical on
every plan. The planner is the hard envelope; confidence is the gate;
fail-open to Postgres. **Hypothesis** until reproduced on *your*
workload. `notes.md` §44.

## 10. Spec property pipeline (Hypothesis)

**Method**: NL/ADR → candidate properties → human strengthens →
MC/ITP/DST → CEX triage → repair. **Transfers**: Choice/Score to *rank*
which candidate props to spend checker budget on; Noul/Choice to
cluster CEXs after the tool ran. **Does not transfer**: ranking ≠
validity. An LLM-written TLA+/Alloy sketch plus a Noul "looks good" is
double theater (`formal-methods.md` §5).

```text
candidates = LLM or human drafts from NL/ADR     # generation or a person
rank       = Choice/Score over the candidate set  # judgment
strengthen = human                                # exact values
check      = TLC / Apalache / Alloy Analyzer / DST / Dafny
triage     = cluster+severity of CEXs             # judgment, evidence only
```

**Example (Hypothesis):** Lamport-Agent drafts TLA+ from a codebase; a
human validates; the checker is source of truth in-model. **Counterexample:**
Hillel tautology (`canImport = P ∨ Q` then "prove" the definition).
**Test:** a property that fails on a planted concurrency bug; ranking
must not mark the tautology as "strong." Status: **Hypothesis**.
Links: `formal-methods.md` Alloy composition table; Amazon TLA+ PDF.

## 11. Alloy instance loop (Hypothesis)

**Method**: `run`/`check` → instances/CEXs → cluster+severity → edit
spec or scope → re-analyze. **Transfers**: post-judge and comparator
positions around the Analyzer. **Does not:** a Noul closing the check;
scope-blind "verified."

```text
Analyzer finds instances | CEXs in this scope
Jev clusters / scores novelty and severity
code or human edits the spec, the scope, or the scenario library
re-run — Analyzer is source of truth for the bounded claim
```

**Boundary:** Analyzer owns in-scope truth. **Test:** planted CEX is
not dropped by the triage Noul. **Hypothesis.** Links:
`formal-methods.md` §2.

## 12. Runtime assurance sandwich (Hypothesis)

**Method**: conformal / System One abstain → symbolic monitor / RV →
act. Curriculum names GUARDIAN / TemporalGuard / Perceive-with-Confidence
as *shapes*, not recipes. **Transfers:** judgment as the statistical
layer *around* a monitor. **Does not:** conformal sets as a proof of
the protocol; skipping exchangeability assumptions.

```text
estimate  = Noul / Score / conformal set     # statistical safety around learning
monitor   = RV / ptLTL / named invariant     # exact, compiled
act       = code, only if monitor admits
```

**Named live-stream shape (Empirical as a *shape*, 2026-09-18):**
[`affirmitv/bitrate-advisor`](https://github.com/affirmitv/bitrate-advisor)
— Jev proposes ABR rungs; deterministic policy (probe × headroom,
history percentiles, loss/queue/thermal/battery) is the monitor. Jev
may only match that envelope or be more conservative. Missing the
model returns the policy's answer. Author-measured three states
(~$0.00004, 0.25–0.39 s) are a receipt for the *shape*, not a codec
benchmark. `notes.md` §44.

**Counterexample:** "the model was confident" as the monitor.
**Test:** inject a monitor-violating trace the Noul would have admitted;
the sandwich must refuse. **Hypothesis** as domain-general; bitrate is
Empirical as the named envelope. Links: `mental-models.md`
conformal; `formal-methods.md` help list.

**Named compaction envelope (Empirical as README behavior, 2026-09-18
~16:22):** [gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction)
— the mutation monitor is **code** (mutating tools, unknown shell,
control operators / pipelines / substitutions / redirections →
`keep_full`). GLiNER2.5 may only propose a reduction on the remainder
or be more conservative; low-confidence / invalid evidence fail closed
to `keep_full`. Soft judgment inside a hard envelope, encoder backend
— not a Jev Score and not a summarizer (`notes.md` §50). Same sandwich
shape as bitrate-advisor; different family.

**Named stdout-prune envelope (Empirical as README / evals README,
2026-09-18 ~17:15):**
[jev-pruner](https://github.com/tamaratran/jev-pruner)
— the monitor is **code** (≤10k estimated tokens; errors;
JSON/XML/YAML/diff/binary; whole-document commands). Jev Noul may
only score residual noisy chunks. Archive/Jev/incomplete-score
failure keeps the original. Soft judgment inside a hard envelope,
Jev backend — same family as gliner25-compaction, different *job*
(command output vs session memory) (`notes.md` §53).

**Named computer-use envelope (Empirical as README / architecture,
2026-09-18 ~16:56):**
[gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast)
— the monitor is **code** (resolve to an observed node; freshness /
visibility / disabled / occlusion; no generated selectors or JS).
GLiNER2 may only pick among candidates the snapshot already holds.
`DONE` is not the monitor. Soft judgment inside a hard envelope,
encoder backend — not a screenshot VLM (`notes.md` §52).

**Named specialist-form envelope (Empirical as README / MODEL_CARD,
2026-09-18 ~17:21; weights Watch):**
[Cua-S1](https://github.com/trycua/cua/tree/main/libs/cua-s1)
— the monitor is **code** (plan ≠ execute; dry-run default; one
window; snapshot-bound tokens; reobserve; `execute`/`submit`
opt-ins; fail-closed unknown checkbox; fill execution fails closed
without advertised token `set_value`). The option-attention head may
only pick among observed elements and extracted `Label: value`
entities. Not TypeSafe Jev. No checkpoint scores (`notes.md` §54).

**Named harness extract envelope (Empirical as PR body, 2026-09-19
~00:48; draft Watch):**
[Stagehand #2955](https://github.com/browserbase/stagehand/pull/2955)
— the monitor is **code** (schema plan: scalars / bools-enums /
lists of flat objects else LLM; completion gate; screenshot extract
always LLM). Jev may only pick among a11y candidates; code copies
text. Invalid / abstain → LLM. Pick is a fast path, not a
replacement (`notes.md` §57).

## 13. DST multiverse triage (Hypothesis)

**Method**: Antithesis / Resonate DST artifacts → failure taxonomy →
patch → regress under the **same seed/timeline**. **Transfers:**
cluster failing timelines; Choice over root-cause hypotheses *after*
replay artifacts exist. **Does not:** guided-exploration coverage as
proof; Noul instead of an assert in-harness.

```text
harness states properties; DST searches; seed reproduces
judgment clusters novelty / suspected component
patch; re-run the same seed
```

**Test:** two failing timelines that share a symptom collapse to one
cluster; a distinct bug does not. **Hypothesis.** Links:
`formal-methods.md` §4.

## 14. Durable agent control (Hypothesis)

**Method**: Resonate HQ checkpoints own durability; Jev-class owns
semantic gates *inside* a step; the protocol oracle owns correctness of
promise state. **Transfers:** Choice/Score for human-in-the-loop resume
priority; Noul gates inside `ctx.run`. **Does not:** "agent-native" as
"judgment replaces Lean/oracle"; a done-Noul settling a promise.

```text
Resonate  = crash-resume, promise settlement     # protocol
Jev-class = semantic gate / route inside a step  # estimate
oracle    = differential disagreement            # probe
```

**Counterexample:** `if noul(done) > τ: complete_workflow()`.
**Test:** kill the process mid-step; the promise is still protocol-true
without consulting the Noul. **Hypothesis.** Links:
`formal-methods.md` Resonate row.

## 15. Assignment hybrid — soft affinity + hard solver (Hypothesis)

**Method**: operations-research assignment / scheduling. **Transfers:**
Score affinity or risk as a *cost feature*; ILP/heuristic owns
capacity, legality, fairness. **Does not:** replacing a VRP/assignment
solver with a Choice; soft costs violating a hard constraint.

```text
affinity = Score/Noul per pair (reviewer↔paper, agent↔incident)
solver   = code (capacity, skills, hours, law)
policy   = starvation/fairness rules in code
```

**Example (Hypothesis):** incident-commander assignment; grant-panel
paper allocation; GPU scheduling. **Empirical as a *shape*:**
[`affirmitv/bitrate-advisor`](https://github.com/affirmitv/bitrate-advisor)
— Jev's rung is the soft affinity; probe/history/thermal caps are the
solver; the model cannot violate them (`notes.md` §44).
**Empirical as a *shape* (2026-09-18 ~23:40):**
[slo-router](https://github.com/zeeshan8281/slo-router) —
Jev's task/exactness/evidence scores are soft features;
the controller is min expected cost s.t. health, context,
tools, quality floor, and SLO-success probability.
Fail-open to local features. Measured negative for *sync*
Jev on the fixture (same routes; p95 77.93→490.38 ms).
**Hunch:** never let the decision model be the sole hard
gate on the hot path (`notes.md` §63).
**Counterexample:** Choice over
assignees that ignores load. **Test:** a feasible assignment the solver
finds that the Score alone would skip because it "felt" worse; hard
constraints never yield. Links: `mental-models.md` §OR.

## 16. Situated density (Shirky) (Hypothesis)

**Method**: [Situated software](https://gwern.net/doc/technology/2004-03-30-shirky-situatedsoftware.html)
— form-fit to a named group; refuse false scale. **Transfers:** dense
full-traffic judgment *inside* a named community (one team, one
product, one agent). Local Choice sets, local τ. **Does not:**
copying those thresholds to another population (calibre:
thresholds don't transfer); enterprise ArchiMate theater for N=30.

```text
community boundary named (team / product / practice)
aggressive soft loops allowed only inside it
outside: retrieval, law, public metrics, FM where wrongness is intolerable
```

**Test:** the same τ on a second population; if cost/coverage moves,
the card was situated and must stay labeled. **Hypothesis.** Links:
`formal-methods.md` Shirky; `mental-models.md` harm "scale mismatch."

## 17. Input brittleness → sensitivity, calibration, selective abstention (Hypothesis)

**Method**: Chow reject-option / selective classification plus a
*stability* test. The model is a noisy sensor; question wording is part
of the stimulus. **Transfers**: semantically equivalent paraphrases that
swing p are a reason to **abstain** or to fix the question, not a reason
to ship the first number. Behavioral evals must include paraphrase pairs
(`validation.md`). **Does not transfer**: a single p as invariant to
wording; "the model is calibrated" as a license to skip sensitivity;
treating jitter as a vendor defect you can ignore (it is a *design*
constraint — [@brandonjcarl, 2026-09-18](https://x.com/brandonjcarl/status/2100976725660192989));
copying the ≤0.18 below as a jitter constant — that is jevgate's
measurement on jevgate's command set, a universal jitter bound stays
Hypothesis (`composition-algebra.md` open positions), and the number you
owe is your own observed spread.

```text
ask φ and paraphrase(φ) on the same state
if |p − p′| large → abstain / rewrite the question / raise t
threshold width ≥ observed jitter (jevgate: identical requests differ ≤0.18;
  a comment moved git checkout -- . from 0.91 → 0.37)
```

**Example (Empirical as published cautions, not a constant):** identity
match Noul ("Is this the same person as X?" vs "Same person as X?");
jevgate comment-injection. **Beyond SWE (Hypothesis):** "is this the
same invoice?" vs "same invoice?"; "does this look done?" vs "done?";
hiring "same candidate as the referral?" **Counterexample**: averaging
ten paraphrases and calling the mean Contract. **Test**: a labeled
paraphrase set where the *act* must not change when the wording is
synonymous; if it does, abstain. Until that set exists on *your*
questions, **Hypothesis**. Links: `mental-models.md` §thresholds;
`question-design.md` diagnosis; `validation.md` behavioral tests.
**Option-order cousin (Empirical as v1.2 footnote; 2026-09-19):**
[open-alternative-jev](https://github.com/ikermoel/open-alternative-jev)
scored **72% → 21%** on yes/no answer-judging when A/B were reversed
*theirs* (JevBench v1.2). Same act, swapped labels. Ranked row uses
the author's `A. yes, B. no`. Do not quote one order as the model.
`notes.md` §78.
**Preregistered framing measurement (Empirical as studies;
2026-09-19 ~17:49):**
[jev-reliability](https://github.com/vcjdeboer/jev-reliability)
— paraphrase ≫ perturbation ≫ repeat on `jev-1.13.0`.
noul-gate reworded **12.5%**; tier12-framing-fixed decision
flip **0.0%** while p still moves **1.7×** null. Nothing
about accuracy. **≠** dinostomp. `notes.md` §89.

## 18. Structural prove ∩ soft remainder (Hypothesis as domain-general; Empirical as named shapes)

**Method**: code (or a recipe, a law, a text layer) **proves** the easy
cases; a System One model judges only what the structure cannot decide.
Composition-algebra position 3 *after* a constraint, not instead of one.
**Transfers**: allowlist / refused-in-code / unknown→judge. The
allowlist **proves** every verb is a listed read-only tool; the model
judges **only unlisted** leftovers; the gate **cannot block** (fail-open
unless a sandbox sits under)
([jevgate](https://github.com/thevibeworks/jevgate): Proven / Refused /
Unknown; Jev alone leaks — `/bin/ls` at 0.04 is why it is the third
tier). Same sandwich as page OCR
([doc-router](https://github.com/misbahsy/doc-router): pdf-inspector
first, "needs OCR?" Noul on the remainder — 155→87 pages billed, **1.74×**
$ on 19 docs / 155 pages). **Does not:** putting the model first so a
comment or a watermark talks it into a write; treating 0 unsafe-unasked
on 59 held-out rows as a sandbox; copying 0.2 or 1.74×.

```text
if structure proves safe     → allow (no model)
if structure proves unsafe   → refuse / ask (no model)
else                         → typed questions on the remainder
fail open unless a real sandbox/interlock sits underneath
```

**Example (Empirical as shapes):** jevgate 249 labelled, worst-of-three,
held-out unsafe unasked 0/59, safe-unasked 30/35 vs allowlist 15/35;
doc-router 9 OCR-misses vs 28 for rules-only.
[`poponline63/hermes-jev-north-star`](https://github.com/poponline63/hermes-jev-north-star):
deterministic shell checks first; empty evidence refuses to judge; then
one Jev call on the remainder. Empty state was self-contradictory —
that is why the refuse-empty rule exists.
[`affirmitv/bitrate-advisor`](https://github.com/affirmitv/bitrate-advisor)
is the same sandwich on a live encoder: policy proves the cap; Jev
may only match it or be more conservative; missing the model returns
the policy's answer. Jev judges only inside it (`notes.md` §44).
Light sibling:
[`phin-tech/pi-jev-approver`](https://github.com/phin-tech/pi-jev-approver)
— regex `commandRules` prove allow/deny (a `deny` is a hard block);
typed Score/Nouls on the remainder; **fail-closed** without a key
(different polarity from jevgate). rh-guard-adjacent; light note only
(`notes.md` §48).
**Regex floor then remainder compact (Empirical as README +
one-session bench; 2026-09-19 ~00:39):**
[jev-compactor](https://github.com/edwardyen724-g/jev-compactor)
— code proves pins, dedup, and `rm -rf` / force-push / `DROP
TABLE` / `curl | sh` regardless of Jev; Jev keep/drop +
Foreman on the remainder. Compaction fail-open if Jev is
down; safety fail-closed on pending destructive/exfil
(`notes.md` §65).
**Local rules then remainder hide (Empirical as README +
small e2e):**
[x-reply-filter](https://github.com/zhuyansen/x-reply-filter)
— `rules.js` proves easy junk at zero cost; four Nouls on
the rest. Auto-hides are not examples until a human
confirms (`notes.md` §65).
**Pre-exec tool product (Empirical as README wiring, not as
accuracy; 2026-09-18 ~17:48):**
[toolgate](https://github.com/fdemir/toolgate) — `allow` / `block` /
`review` before execution; guard error or timeout **stops** (fail-
closed on the execution act). Jev is a probabilistic check, **not
authorization**. 72-case synthetic set is not independently
annotated. Distinct from the ndolinschi *vocabulary* (allow /
ask_human / deny) already in `agent-self-assessment.md`.
`onReview` must obtain authenticated human approval
(`notes.md` §55). Do not copy pnpm.
**Wrap-as-execution then remainder (Empirical as README;
fail-closed; 2026-09-19 ~10:20):**
[AgentGhost](https://github.com/reddpy/AgentGhost)
— `allow`/`ask`/`deny`/`matchArg` prove first; Jev on
leftovers; ASK/DENY throw; judge error → DENY. Distinct
from jevgate (fail-open, cannot block) and from toolgate
(proposed-call pre-exec). rh-guard owns the gate cousin.
Do not copy `npm` (`notes.md` §83).
**Tool-risk as a placement, not a wrap (Empirical as
article; 2026-09-19 ~10:25):**
[@akshay_pachaar](https://x.com/akshay_pachaar/status/2101037514945597645)
cites LangChain middleware as tool-risk gating. That is
the *placement*, not a product card. AgentGhost owns
wrap-as-execution; rh-guard owns the gate cousin. Do not
steal Flavio Copes (`notes.md` §85).
**OMP prompt suppression, host deny proves (Empirical as
measured traffic, 2026-09-18 ~22:38):**
[omp-greenlight](https://github.com/SemetricLabs/omp-greenlight)
— OMP `bash.patterns: deny` **proves** the floor; Jev may
only suppress remaining approval prompts above an
operator-owned bar. Plugin never self-tunes. Not a sandbox.
Default 40.9% / 0 of 94 *theirs*. Distinct from toolgate
(pre-exec of a proposed call) and omp-jev-extensions
(fail-open route). `notes.md` §62.
**Effect-based fast-path then remainder (Empirical as
certification; 2026-09-18 ~23:40):**
[construct-auto-classifier](https://github.com/godspede/construct-auto-classifier)
— fast-deny / fast-allow **prove** catastrophic and
read-only verbs in <1 ms; Jev judges blast radius /
reversibility on the remainder. Fail-closed on the
*execution* act (contrast jevgate cannot-block). Privilege
stripped before the allow rule, not used as the verdict.
Jev 0 dangerous / 975 *theirs*. Landed-script trust /
headless ≠ auto-approve (`notes.md` §68). **Hunch:** contracts on
effects, not tokens (`notes.md` §63).
**Capability kernel, different trust boundary (Empirical as README
architecture, 2026-09-18 ~19:48):**
[interlock](https://github.com/somoore/interlock) — the LLM never
saw the secret and cannot emit an unlisted action; Jev is SENSOR;
policy is the prove/constraint layer. Do not merge with toolgate.
**Human-confirmed kill (Empirical as README safety model):**
[port-cleanup](https://github.com/epiphany-dynamics/port-cleanup)
— Jev recommends; human confirm + identity re-check + shields are
the prove layer for SIGTERM; mapped explanations, not raw model
prose (`notes.md` §59).
[`coldteadotai/abide`](https://github.com/coldteadotai/abide) is the
same *family* on project instructions: the **linter proves** lintable
rules; Jev Scores only residual soft AGENTS.md rules; fail-open, banded
(`notes.md` §47). Different remainder from jevgate's unlisted verbs
and from rh-guard's eval-integrity hole — do not merge products.
**Skills → oxlint (Empirical as a named Phoenix experiment,
2026-09-18 ~18:46):**
[jev-oxlint](https://github.com/cephalization/jev-oxlint) — AST
facts and prechecks in **code**; guidance files copied whole into
`state`; one remaining request of atomic questions;
survey / calibrate / propose. Status: experiment, nothing
published. Phoenix: jev agrees with the human answer key on every
fixture; found a real flush-only-on-success bug (noul 0.07);
routing 0.80–0.94 vs <0.50 across 41 files; coarse hint is not;
~$0.002 fixtures / ~$0.015 41 files; second run zero requests.
Formal methods compose with soft judgment **without hard-gating**
a Noul as a proof. `tenbin` owns the lint skill. License null
this pass. MED cousin, **HIGH delta §92**:
[safe-sh](https://github.com/EpicEric/safe-sh)
(AGPL-3.0) static shell-script analysis — not pre-exec
authorization. EpicEric/safe-sh static remainder
(`notes.md` §58, §92). Do not copy pnpm.
**HIGH delta §95 remainder after exact rules:**
[seb4ez/jevguard](https://github.com/seb4ez/jevguard)
(MIT; **0★**) — jevguard calibrator/cache/escape.
Closed-world skips the escape. Cache is exact
(volatile masking). **≠** jevcache.
[guilhem/jev-ci-selector](https://github.com/guilhem/jev-ci-selector)
(license null; **0★**) — jev-ci-selector CI shadow mode.
Mandatory/path rules beat Jev; timeout/no-key keep
all. rh-guard owns (`notes.md` §95).
Compaction polarity is the other way:
[gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction)
— code proves mutating / dangerous shell → `keep_full`; the encoder
judges only the remainder; uncertain **fails closed to `keep_full`**
(`notes.md` §50). Same sandwich, opposite fail policy from jevgate
(cannot block) and Abide (fail-open on diffs): the authorized act is
a destructive reduction of memory.
**Stdout prune is the same polarity, different job (2026-09-18
~17:15).** [jev-pruner](https://github.com/tamaratran/jev-pruner) —
code proves ≤10k / JSON-diff-whole-doc pass-through; Jev scores the
remainder; uncertain **fails closed to original stdout** plus an
archive (`notes.md` §53). Harbor plugin-eval cannot reach Jev and
therefore cannot prune — fail-safe, not a missing score.
**Name the irreversible act (2026-09-18 ~16:48).** Wake *skip* is
irreversible (the agent stays asleep) →
[wakegate](https://github.com/shitianfang/wakegate) authorizes skip
only at p < 0.2 and otherwise **wakes** (fail-open on the skip).
Merge *PASS* is irreversible if the bug was real →
[latch](https://github.com/CaseReed/latch) `--gate` BLOCKs unless
infra is confirmed; the Playwright reporter stays fail-open.
[if-ai](https://github.com/Victor-Casado/if-ai) fails the Action on
error / empty / low confidence (fail-closed on the check).
`notes.md` §51.
**Beyond SWE (Hypothesis):**
recipe book ∩ "does this leftover look done?"; labor-law allowlist ∩
hiring-fit Noul; SPF/DKIM pass ∩ phishing Noul on the body. **Counterexample:**
Jev on `/bin/ls` as the first tier. **Test:** planted writers never
reach the model; planted remainder cases *do*; removing the model must
not admit anything the allowlist forbade. Domain examples stay
**Hypothesis** until labeled. Links: `formal-methods.md` sensor≠constraint;
`mental-models.md` §Leveson; composition-algebra gate after a constraint.

## 19. Effect-oriented state-machine loops (Hypothesis)

**Method**: decision circuits / FSMs (§3) inside an effect system.
Soft predicate on the transition; **code owns the transition** and
whatever effect it runs. Extends dual orchestration topology B
(`mixed-architecture.md`): the decision model answers the edge; a
generator, if any, is a callee; the host still executes.

**Transfers**: each turn the host mints the finite set of actions legal
in *this* state. One Choice asks which of these advances the state, or
a Noul asks a fuzzy edge the rules cannot name ("does this look
finished?"). The handler runs the effect (MCP, store, no-tool writing)
and returns continue-with-new-state or done. Only a compact view and
the option descriptions cross to the model; the action value stays
typed in the host. Unknown ids fail closed before the effect. Exact
edges (inventory, chronology, a hard iteration cap) never leave the
host.

**Does not transfer**: reading the tweet title "Effect Oriented" as the
TypeScript Effect library, or as a tutorial in either system. The image
is a ZIO loop in
[jamesward/zio-typesafe-ai](https://github.com/jamesward/zio-typesafe-ai)
(Ward's *Effect Oriented Programming* is Scala/ZIO). That client's
combinator is not the Jev HTTP contract and not an Augustus API. The
model does not invent the next state or the side effect. An id outside
the offered set is a protocol violation, not a branch. A Noul or an
encoder score is not a discharged invariant. Do not multiply edge
predicates into a joint probability. Handler time and a generative
callee's tokens are not model cost. The 1–255 option cap is Jev's, not
the class's.

```text
options(state) → finite legal actions the host minted
Choice / Noul  → which action, or is this fuzzy edge true?
handler        → effect, then continue(next) | done
unknown id     → fail closed; do not run the effect
exact edge     → host only; the model is not called
```

**Example (illustration, not a recipe):** the posted counter, where
"increment" continues and "finish" returns the state
([James Ward, 2026-09-18](https://x.com/JamesWard/status/2100981305009664299)).
Load-bearing sentence on the image: an action handler may run arbitrary
ZIO effects — MCP calls, database operations, or a no-tool generative
model call — while Jev remains the outer decision loop. **Beyond that
client (Hypothesis):** clinic intake — Choice picks the next question,
the chart write is the effect; hiring — advance / hold / stop is the
Choice, the letter is written inside the handler; a kitchen — "is this
step done?" is the predicate, the timer and the knife stay in the
recipe. **Counterexample:** free-text "what state next?", or a
generator emitting a tool name it might hallucinate. **Test:** a
planted illegal action is never offered; a planted unknown id does not
run; a deterministic edge never calls the model; a handler failure
still leaves that turn's distribution in the log. Until that labeled
trace exists, **Hypothesis**. Links: §3; `mixed-architecture.md` dual
orchestration; `notes.md` §28.
