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
**0042 HIGH (`notes.md` §105):** structured probability
readouts (distribution > argmax; Noul 0.5 midpoint; score
is expectation not integer; bare HTTP not SDK;
Arohtea/jev-readout); Jev-style Choice/Score/Noul from
ordinary models (optional DSH plugin; schema-valid ≠
calibrated; gulagala001/jevify ≠ Mintzs/jevify); Laya RLCD
benchmark (40.3% below constant-answer; open-weight
measurement; mourad-ghafiri/laya-rlcd-benchmark ≠
yibie/laya-jev-lab); cheap fail-open semantic edge (second
signal not sole; FastLoopError catch;
SupremeDreamZ/jev-fastloop ≠ jev-ultrafast); asking more
questions in one call (0.980 at every N; nearly not fully
deterministic; TheWebDevel/jev-fanout); Qwen3-VL
perception + Jev decisions train RL (0 model calls at
deployment; VLM alone 1.7 vs +Jev 4.4;
harneet2512/reflexrl ≠ khordoo/jev-reflex-autonomy-lab);
independent Jev API vs Laya (cascade 0.60 matches 78% at
1.8×; noul facts not judgements; yibie/laya-jev-lab ≠
dairui1/jev-lab ≠ BrendanH18/jev-lab); GLiNER vs GLiFormer
vs Laya vs Jev (extractors ≠ decision engines; Laya
dict-instructions collapse 58.3%; umstek/zero-shot-ie-bench);
decisions-per-minute & cost (204 moves vs 73; throughput
not intelligence; angelgalvisc/snake-arena-jev-vs-llms ≠
vtrivedy/jev-plays-games); behavioral contracts (pin
expectations eval upgrades; raw 0.94 is not a release;
sathariels/jevcheck ≠ dayhaysoos/jevals ≠
SivletLabs/jev-eval); evidence-linked dependency upgrade
(Jev never generates filenames; no_direct_evidence ≠ safe
to merge; GaneshVG18/upgrade-radar ≠
LYchoon/paper-radar-jev); discography
theme/mood/complexity (five atomic questions one call;
lirantal/discoprint). Soft Noul ≠ hard safety.
`notes.md` §105.
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
(`notes.md` §55). **Productized language (Empirical as README +
interpreter contract; 2026-09-19 ~19:43):**
[southpolesteve/probably](https://github.com/southpolesteve/probably)
(TypeScript MIT; **3★**) — Jev IS the if-statement.
judgments/probabilities drive branches. text model only
writes prose. interpreter owns variables/loops/budgets/replay.
otherwise maybe / confidence gate. chaos samples after the
gate. southpolesteve/probably ≠ carldaws/hunch ≠ feelings ≠
Kungie/gut ≠ Illusion47586/judge ≠ tidymodels/probably.
`notes.md` §100. **BAML typed if (Empirical as README;
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
**Cost-derived / typed-callback overlays (Empirical as
README target design; 2026-09-19 ~18:43):**
[Kungie/gut](https://github.com/Kungie/gut)
(GitHub Apache-2.0 / LICENSE MIT / pyproject Apache-2.0
*theirs*; **0★**; pre-alpha) — YES / NO / UNSURE
from expected cost over a System One p. cost-sensitive
decision theory × System One probabilities → control
flow. thresholds derived from costs not hard-coded.
YES / NO / UNSURE from cost_false_yes / cost_false_no /
cost_human. auto-batching same-object questions.
Default `on_unsure="raise"` is app policy, not a
System One hard gate. Kungie/gut ≠ tpellet/hunch
≠ carldaws/hunch.
[Illusion47586/judge](https://github.com/Illusion47586/judge)
(TypeScript MIT; **0★**; `@brkn-labs/judge` 0.1.0) —
judgment vs generation. deterministic execution after
probabilistic judgment. exactly one app-owned callback.
explicit uncertain branch. Illusion47586/judge ≠
lexingtonhibiki/judgekit ≠ Ascurse/typed-judge-kit.
Overlays, not species. Soft Noul ≠ hard safety
(`notes.md` §99).
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
**Calibrated meaning-grep over a live tree (Empirical as
README architecture + economics, 2026-09-19 ~17:40):**
[jegrep](https://github.com/can1357/jegrep) — absolute
yes/no per path + line range. jegrep calibrated
path+range Nouls. no embeddings/index/daemon.
~$0.01–0.03 typical. agent --json. Ranking fail-open.
No published Harbor. OpenRouter/TypeSafe auto-failover
is silent FALLBACK. can1357/jegrep ≠ Bentlybro/jevgrep
≠ uehaj/jev-semgrep. Do not copy 79% / `cargo`
(`notes.md` §98).
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
**Calibrated meaning-grep VOI (Empirical as README
economics; 2026-09-19 ~17:40):**
[can1357/jegrep](https://github.com/can1357/jegrep)
— pay per search over a live tree; no index to
amortize. jegrep calibrated path+range Nouls.
no embeddings/index/daemon. ~$0.01–0.03 typical.
agent --json. Ranking fail-open. can1357/jegrep ≠
Bentlybro/jevgrep ≠ uehaj/jev-semgrep. Do not copy
79%. `notes.md` §98.

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
**Decision-ledger memoization (Empirical as README;
2026-09-19 ~21:23):**
[hyperspaceai/jevcache](https://github.com/hyperspaceai/jevcache)
— pay for a backend decide iff the ledger misses.
fingerprint after redact; recall vs decide; publish
fingerprints+answers; CI replay as Harbor cousin.
VOI of cache hit is spend/latency saved *if* the
HIT is still the right answer. Cache hit ≠
correctness. hyperspaceai/jevcache ≠
kushals256/jevcache. Do not copy `curl | sh`
(`notes.md` §93).
**Uncertainty-acquisition labels (Empirical as README;
2026-09-19 ~21:23):**
[sutro-sh/jev-align](https://github.com/sutro-sh/jev-align)
— pay for a human label iff the row is ambiguous
(+ audit sample). human labels only; score never
auto-accepts; production capture flywheel.
sutro-sh/jev-align ≠ caiovicentino/jev-align.
Do not copy `uv` / keys (`notes.md` §93).
**Compile-time index VOI (Empirical as README;
2026-09-19 ~21:35):**
[byenzyme/enzyme](https://github.com/byenzyme/enzyme)
— pay for Jev at compile to shape the question
program; runtime retrieval is catalyst handles.
catalysts ≠ summaries. guidance ≠ hook. hosted
bootstrap ≠ silent TypeSafe. ~350×
cost / 1000× speed *theirs* for the compile path —
do not invent Harbor numbers. Do not copy
`curl | bash` (`notes.md` §94).
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
**Assessment-batching / live-tree search VOI (Empirical as
README; 2026-09-19 ~17:40):**
[numerous-com/dgp](https://github.com/numerous-com/dgp)
— assessment batching: pay the assessor for many
offered decisions on one immutable frame; commit
is the expensive act. Decision Graph Protocol
frame→assess→commit. Speculative assessments cannot
authorize effects. [can1357/jegrep](https://github.com/can1357/jegrep)
— ~$0.01–0.03 typical per search; no embeddings/index/daemon.
agent --json. `notes.md` §98.
**Cost-human gather / same-object auto-batch VOI
(Empirical as README target design; 2026-09-19
~18:43):**
[Kungie/gut](https://github.com/Kungie/gut) —
`cost_human` is a gather act: pay a human iff that
is cheaper than expected false-yes or false-no.
auto-batching same-object questions is measurement
economics (one backend call per object). YES / NO /
UNSURE from cost_false_yes / cost_false_no /
cost_human. thresholds derived from costs not
hard-coded. Soft Noul ≠ hard safety. `notes.md` §99.
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
accuracy (`notes.md` §33).
**Typed vs chat judges on guardrailing (Empirical as
RESULTS generated from summary.json; 2026-09-19
~18:43):**
[ishaannk/llm-vs-jev](https://github.com/ishaannk/llm-vs-jev)
— one spec, one policy, several perception backends.
typed judgments vs chat judges on guardrailing.
nothing wins outright. can be argued out of guarding.
ishaannk/llm-vs-jev cross-note only. deeper integrity
fold is rh-guard. Not a Harbor taskset. Soft Noul ≠
hard safety. `notes.md` §99.
**Beyond SWE (Hypothesis until plotted):**
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
**Decision Graph Protocol envelope (Empirical as README
+ spec; 2026-09-19 ~17:40):**
[numerous-com/dgp](https://github.com/numerous-com/dgp)
— Decision Graph Protocol frame→assess→commit.
app retains permissions/effects.
Jev-first assessor-neutral.
guarded commit / receipt/next frame.
assessment batching.
The application owns state, permissions, guards, and
execution. A model is neither a security boundary nor
the source of execution authority (*theirs*).
hard-gating DGP as safety theater.
numerous-com/dgp ≠ TypeSafe official.
rh-guard **does not own** this hole.
Soft Noul ≠ hard safety. `notes.md` §98.
**Cost table is policy / Noul is SENSOR (Empirical as
README target design; 2026-09-19 ~18:43):**
[Kungie/gut](https://github.com/Kungie/gut) — the
cost table is policy; the Noul is a SENSOR; default
UNSURE raises. Hard-gating 0.038 as a safety proof
is theater. [Illusion47586/judge](https://github.com/Illusion47586/judge)
— exactly one app-owned callback; explicit uncertain
branch. Deeper integrity fold is rh-guard
(`notes.md` §99).
**Memory retrieve vs lease (Empirical as README;
2026-09-19 ~19:43):**
[samdotmak/jev-recall](https://github.com/samdotmak/jev-recall)
— retrieve by relevance not resemblance. one calibrated
yes/no per memory in one request. pointer mode 17/18 19/20
*theirs*. embedding resemblance misses the allergy.
[chopratejas/invalidate](https://github.com/chopratejas/invalidate)
— memory leases ended by new evidence. six Nouls then
fixed rules in code. 0 of 157 false invalidations.
questions/plans/directives are not evidence. unsure →
review queue. host keeps the store. Soft Noul ≠ hard
safety. `notes.md` §100.
**2041 HIGH (`notes.md` §101):** resume-screening bias
audit methodology (SDT; natemoo-re/bias-bench ≠ BBQ);
Plan/PRD panel → code-owned pass|review|block
(austindixson/planalyzer); cost-aware multi-model
routing/escalation (decide vs do; successful-task cost;
cannacre8ive/switchboard-ai ≠ ha-switchboard ≠
hermes-switchyard); frozen-protocol zero-shot bench
(TypeSafe Jev vs PrismNLI vs Laya; contamination caveat);
context-window admission control (VOI gate; fail polarity
per lens; on small inputs lenses lose money);
typed decision control plane (receipt ≠ authorization;
historical-v0 zero retained cases); live 15-dim typed
rubric re-score per pause (scoring economics; OpenJev/Codiv
≠ TypeSafe hosted); adversarial pre-registered Jev eval
(28 predictions before data; 123,805 requests; confidence
does not track ignorance; rh-guard owns injection);
provider-neutral Elixir/BEAM Noul/Choice/Score SDK
(class infrastructure). Soft Noul ≠ hard safety.
`notes.md` §101.
**2145 HIGH (`notes.md` §102):** question-linting of Jev
questions themselves (yodablocks/jevq ≠ tenbin ≠ JevLint;
static lint ≠ measured separation); open-weights Laya as
class exemplar (binding; Nx/Bumblebee; host chooses backend;
ChristianAlexander/laya_ex ≠ system_one_sdk ≠ dannote/jev);
on-chain/edge Laya deploy (parity_verified stays false;
model output never grants Tx); auditable weekend replica
(Jev outputs never used for training; unpaired 0.577 vs
0.727); adversarial dual-judge / framing attack surface
(comparative framing is the usable judgment; prior
injection crowds out evidence; copyleftdev/ember ≠ ember.js);
Laya specialist + Hub replica (training still GPU-pending;
daliborsb/laya ≠ convaiinnovations/laya); distillation
economics (gold is programmatic; teacher is closed-API clone;
do not distill Jev as teacher of record); non-LLM VIN
System One (planning depth not chat; lewislululu/jevon ≠
douglance/jevon); source-bound evidence (local quote
mismatch needs no API; exit 0 ≠ claim truth;
WaynezProg/jev-kit ≠ jonathanavis96/jev-kit
(Airlock)). Soft Noul
≠ hard safety. `notes.md` §102.
**2246 HIGH (`notes.md` §103):** independent System One
evidence catalog (19 reviewed records; scores not one leaderboard; no external
record currently reproduced; TokenTrim no-Jev matched
hybrid 62.4%; reachjalil/system-one-bench ≠
mallahyari/system-one-benchmark); typed eval freeze
(21 tasks · 134 items · 208 questions; scenes from public
GitHub contracts, not production logs;
SivletLabs/jev-eval ≠ willkelly/jev-evaluation ≠
4esv/jev-eval); option isolation (sibling-blind);
permutation-equivariant; Hub OWNER not published;
nafisazizir/hev ≠ jaredpalmer/kev; frozen local LLM
logits, no trained decision head; residual-head
9,222-param decreased 73/96→67/96; confidence =
1−normalized entropy, not P(correct);
yuki-oshio/mini-jev ≠ r-ms/mini-jev; Jev classifier as
autoregressive next-token predictor; ChatJev-style
soundness theater; erik-dunteman/ChatJev ≠ dannote/jev ≠
jev-gpt; calibrated decision head × AlphaProof value
head; implementation-layer isomorphism, semantic
difference; timeout = censoring; do not launder Noul as
proof; parallel rank-prediction vs serial selection;
independent questions can conflict; zzzzzec/jevsort ≠
keltokhy/jsort; curated open System One ecosystem
catalog; rupeshpoojary9/awesome-open-system-one ≠
AnotiaWang/awesome-jev; arXiv paper radar with Jev
relevance scoring; ranking ≠ calibration / 0.5 still
soft; fail-open failed evals not marked seen. Soft Noul
≠ hard safety. `notes.md` §103.
**2340 HIGH (`notes.md` §104):** train calibrated ~27M from scratch; typed Q→prob dist / one forward pass / no LLM decode; hyusi2003/MiniSystemOne ≠ Colvin0315/MiniSystemOne; description-only stub / size 5; ESCI hard probe fails four of six; jev_bool ECE 0.242 inversion 0.255; do not re-fold §60 six-gates as new; jobbyjev one-request-per-company from batch-size result; find/design/evaluate TypeSafe Jev decision loops; karanb192/jev-architect ≠ samtay32/jev-system-architect; Jairik/jev-distiller size 1; distill-Jev UI stub / do not distill Jev as teacher of record; post-launch scored use-case map / Jev self-scores then human curation; licensedsaucer9-web/jev-opportunities; Jev-inize a use case into classifier/router; gavinHuang/jevinize → simple-jev not TypeSafe; featherless-ai/simple-jev; compare saved decisions / same label can still change the branch; VihaanAgarwal/jev-diff ≠ Saik0s/diffusiongemma-jev-macos; not tested with a live Jev API key; constrained logprob + temp/Platt ≠ Noul; OpenJevPro pastes openjev-sglang JevBench as own; zhangcy122/OpenJevPro ≠ IamBusy/OpenJev ≠ ekzhang/openjev-sglang; PolyForm Noncommercial; SmolLM-135M / sub-70ms / 0 output tokens; demo P(True) 0.5052 / Choice conf 0.2872 / Score conf 0.0055; README claims MIT / GitHub license null / no LICENSE file; patelvishwa112/jev-system-one-rlcd ≠ arnabgho/rlcd-lite ≠ blackwood-rlcd; source-backed Awesome Jev radar / 306+ commit-pinned; logicrw/awesome-jev-projects ≠ AnotiaWang/awesome-jev ≠ yibie/awesome-jev ≠ cobanov/awesome-jev ≠ rupeshpoojary9/awesome-open-system-one; auto GitHub sync / Issue-only submissions; hashed n-gram encoder / rival-aware attention; olanotolu/jevbetter vs jevlike starter; synthetic hard menus top-1 0.916 vs 0.873 / ECE 0.0182 vs 0.0367 / 40 vs 4608 menus/sec; shuffled-context control 0.335. Soft Noul
≠ hard safety. `notes.md` §104.
**0145 HIGH (`notes.md` §106):** Turn any open LLM into System-One Jev; uspraveen/Jevify ≠ Mintzs/jevify ≠ gulagala001/jevify; Jevify-any-LLM architecture probe; description-only stub / size 0; Train encoder-only calibrated decision models from a task sentence; Exu is a toolkit, not a method; strictly proper scoring rule; Pre-alpha; Ruivalim/exu-base; scratch-trained calibrated decision model; typed Q → probability dists; Colvin0315/MiniSystemOne ≠ hyusi2003/MiniSystemOne; no published weights download URL; 90.5 seconds / 29.2% pipeline evidence; p_i/p_j independent of other candidates; Recipe for calibrated decision models — small model out; init → synth → train → eval → serve; 91.1 % / ECE 0.022 *theirs*; Jev zero-shot 75.1; scienthoon/luce; Put Jev's three headline claims on trial; 0.5B local GPU; 46x speedup / accuracy identical; ECE 0.624 sentiment catastrophe; bigger model worse calibration; RichardoMrMu/jev-mini ≠ yuki-oshio/mini-jev ≠ r-ms/mini-jev; System-1 decision engine for local LLMs; structured choices only; JSON parse of generated text ≠ Noul; TypefAI JEV / Journal Entry Voucher; tapsin/jev-local ≠ us/jev-local ≠ Argos1111/jev_local; Jev 1.13 reward-model eval across 8 benchmark tracks; 40,940 examples / 0 API errors; RewardBench v1 92.58%; Precise IF 50.63%; goya4140/jev-reward-model-evaluation; Scaffolding in progress; Jev vs LLM support-ticket routing; static + live decision bench; TypeSafe's own published benchmark; illustrative simulations, not live API calls; JevBench v1 — smart/cheap/fast/reliable; I/C/S/K 25% geometric mean; classifier.dev fast tier 84.8 is Jev behind its own API; do not re-fold §78 v1.2 board as new; Laya (421M) 70.1 now on board; Zero-shot/few-shot LLM routing; hard budget filter before Jev; Jev never asked to perform budget arithmetic; Jev judges the next state, XState enforces transitions; simulation uses synthetic keyword fixtures; catalog gravity; v-modal/awesome-jev-tools; ★339 live REST; curation is not endorsement; crawler-maintained directory; Daily GitHub + npm sweep, human-merged; RadRebelSam/awesome-jev ≠ AnotiaWang ≠ yibie ≠ cobanov ≠ logicrw ≠ v-modal; HF peft SPLADE/BGE reranker; rdxtremity/jev-reranking ≠ carlaiau/jev-reranking; query-side encoders, not a Jev replica; ONNX System One Qwen3.5-4B scorer; source:pngwn/system-one-qwen3.5-4b-scorer; CC-BY-NC-4.0; temperature 1.75; transformers.js AutoModel cannot load this graph; Consistency benchmark Space; This Space contains no benchmark result yet; 12-case plumbing fixture; do not reopen or amend PR #23. Soft Noul
≠ hard safety. `notes.md` §106.
**0243 HIGH (`notes.md` §107):** Benchmark-driven Jev router and judge; cheap alone is not success; Jev does not write, sum prices, or claim accuracy %; Sol 94.2 / Luna 83.9 / Jev path 89.7; 19.2% Sol / 62.3% cost save / 4.5pp miss of 2pp non-inferiority; p50 latency worse than Sol due to routing overhead; erendikmenn/jev-llm-router-benchmark ≠ jev-rag-benchmark ≠ ryantsai/jev-llm-router; Express + node:sqlite; mock and Jev decision engines; previous_ticket_count >= 3 is code; MIN_CONFIDENCE 0.6 still soft; substring false positives; aesaganda/jev-ticket-router ≠ SarathChandraBellam/jev-vs-llm-ticket-router; Universal Figure & Diagram Router; confidence ≥ 0.85 hard-gate is theater; generative AI banned from scientific plots; six visual branches; hoangngochuong24947-gif/jev-figure-router; human-labeled (state, question, label); 166,054 rows / 22 configs; soft_label for human uncertainty; Praveenrajus/jev-bench ≠ fstandhartinger/jevbench; ternary bonsai System One GGUF; openjev's mechanism, Bonsai's weights; Hub does not ship weights; 100/100 easy T/F is not Harbor; label_mass ≠ correctness; stock llama.cpp Q2_0 silently gibberish; NicolaiMTLassen/open-bonzi-jev ≠ NicolaiLassen; transformers.js DeBERTa ONNX; source:com-kotobalabs/open-jev-deberta-v3-large; temperature 1.05; AutoModel from_pretrained works; onnx-community/open-jev-deberta-v3-large-ONNX ≠ system-one-qwen3.5-4b-scorer-ONNX; 107★ densify; GH 151M vs README 149.6M; PR #1 now closed unmerged; do not re-fold §71 claim-audit as a beat; typed decisions, RLCD, confidence-gated routing; structured ≠ correct; mock not live API; 26 tests; wjdjdakf17/jev-study ≠ baekenough/jev-study; do not reopen or amend PR #23 or #24. Soft Noul
≠ hard safety. `notes.md` §107.
**0345 HIGH (`notes.md` §108):** bonzi-27b-v2 / ternary-8b / 27b-v1 GGUF family densify; WANLI-256 74.6% / 65.2% / 71.1% *theirs*; Bonsai 1 27B Q1_0 runs on stock llama.cpp; ternary still needs PrismML fork; hf:heman10x/openJev-verdict-2.0 twin tokenizer-only; OpenJev Vision image classification + uncertainty; CLEVR-4 held-out joint 0%; hfdataset:IamBusy/OpenJev-Vision-Research-v0.1 12,832; 294,912 derived targets not independent samples; Laya multilingual ONNX WebGPU typed-decisions port; 63/63 selected answers / 5.1e-4 CPU / 1.2e-2 WebGPU; UpHash-Network/mini-jev is yuki-oshio transfer; jev-injection-bench 11,900 labelled prompts; Jev best ranking / Haiku better ECE 0.021 vs 0.058; 0.5–0.9 band is where Jev's numbers do not mean what they say; Prompt wording moves panic 28%; manojlds/jev-dspy-bench ≠ dspachos/jev-dspy ≠ jmanhype/jev-dspy-lab; Jev agreement is similarity, never ground truth; no aggregate quality grade or merge gate; AbstentionBench-on-Jev rank 1 of 20 vs 2025 field; question-asymmetry; forward-looking 0.465 never extreme; openkev calibration layer not a runtime; ECE vs coverage independent; select_threshold returns inf; escalation catches uncertainty not ignorance; misakaikato/openkev ≠ jaredpalmer/kev; pdf-race Docling→Jev vs Gemini; parser owns the wall clock; 12/12 tie is a tie; titles selected not generated; flopcheck 16 calibrated tweet judgments; mechanical tells in code; ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas; Laya calibration lab Gradio MCP; T never changes argmax; confidence ≠ top-label p; easy probe set refused; 40–48 rows too small to ship T; do not reopen or amend PR #23 or #24 or #25. Soft Noul
≠ hard safety. `notes.md` §108.
**0439 HIGH (`notes.md` §109):** Gemma-4 26B-A4B jevify classification+calibration; LoRA adapter twin not independent eval; Gemma-4 E4B jevify; E4B LoRA stub card; kushalpatil/jevify-gemma4 ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; GH kushalpatil07/jevify 404; PAWS 0.580/ece 0.288 is the weak cell; smaller E4B slightly better OOD ECE than 26B-A4B; Hub jevify merged LoRA ships weights; bonzi Bonsai-8B v1 GGUF densify; Bonsai-1.7B v1; Bonsai-4B v1; WANLI-256 64.5% / 60.2% / 52.0% *theirs*; rank #4 / #5 / #6 of 6; JulesHuisman/jev-eval scaffolding / README SHA c356a584 (was empty e69de29b); JulesHuisman/jev-eval ≠ SivletLabs/jev-eval ≠ willkelly/jev-evaluation ≠ 4esv ≠ xxkuboxx ≠ onlyoneaman ≠ dayhaysoos/jevals; 7 bands 6/10 vs 40 bands 0/10; source receipts + confidence slider re-policy without re-inference; 32/32 synthetic is smoke not production; classify HF datasets across typed semantic dimensions; roadus2 watch misspelling; lock roadius2/ultra_laya; ultra_laya REVIEW defects; default branch claude/laya-jev-review-gg5ppo; XNLI EN 88.3% ECE 0.032 → RU 77.3% ECE 0.096; Δ −11.0 pp [−14.2,−7.8]; ECE +0.063; MASSIVE no detectable difference at n=600; confidence is function of p_max (r=1.000); pointer-not-generator 400 human-authored responses; proposed ≠ authorized; FewRel 160: Jev 85.0% vs lexical 13.125%; gated 100% (95/95) coverage 59.375%; J++ composable semantic computation language; judge-jev 0.5 still soft; 947 repos scored; A 273 / B 302 / C 372; LLM rubric ≠ benches; No benchmark winner is claimed; phishing: naive 62.6% vs regex 91.8%; 5-atomic + LR 95.0% *theirs*; AITuber tension ±15; README npm global; repo is Rust; git-confess code owns counting/blame/ratio; httpx exhibit 11% (13/119) *theirs*; 90d trend +12.40% vs random +12.75% vs BH +41.71%; 5m win rate 25%; Awesomejev 656 entries / 38,160 stars; tracker likes 64 (+4) lastModified UNCHANGED; Laya present; Blackwood ABSENT; Archer still promised_not_landed; do not reopen or amend PR #23/#24/#25/#26. Soft Noul
≠ hard safety. `notes.md` §109.
**0541 HIGH (`notes.md` §110):** Blackwood tracker ABSENT; likes 2 gated manual; r = c - p_a; ECE 0.021; acc 0.807 vs warmup 0.746; calibration beyond ~500 tokens unmeasured; Independent primitive; 11.57s vs 54.10s · 4.67× · 120/128 *theirs*; default path is pretrained Gemma probs not trained RLCD head; GH Meanblock 404; lock leesk212/JEV-CPU; softmax over letter slots ≠ Noul; WANLI 0.741 vs openjev v2 0.77 *theirs*; 3-way NLI ≠ Noul; priority 0.464 = majority floor; banking77 contaminated; raw margins not probabilities; GH jev-haiku-benchmarking 404; do not distill Jev as teacher of record (they distilled Haiku); “0.9 is not one number”; ranking ≠ calibration; banking77 0.8–0.9 stated 0.86 actual 0.73 over-confident *theirs*; ≠ Praveenrajus/jev-bench ≠ fstandhartinger/jevbench; $0.0000153–$0.0000226 vs circulating $0.0004 (~20×); Score is 0..n-1 expectation not 0–1; Noul has no confidence field; TCP floor 198.8 ms; type reliability is not a reason to choose Jev (json_schema 5/5); gateway tax not one number; Function-only 5/8 vs hybrid 8/8; 4/8 without Jev; 8 designed cases not conversion lift; ≠ RadRebelSam/awesome-jev; 200-row pilot Jev 86.5% 173/200 vs Gemini Flash-Lite 86.0% 172/200 vs Pro 87.0% 174/200 *theirs*; not a ranking; NLI Tetris argmax P(entail)−P(contradict); 情緒測謊器; 1q 396ms / 30q 567ms; ±0.03; 33q $0.000045 vs Gemini ~5× slower ~60× cost *theirs*; ≠ realZachi/jevtest; 8-example Jev vs GPT-5.6 Sol ~64× cost 5.4× latency *theirs*; synthetic; no inference; ≠ JevBench v1.2 §78; Judged 3317 / listed 2560; Jev judges, code applies policy; catalog ≠ endorsement; APA “microsecond policy / zero hallucination” overclaim; Client-side quiz; pointer from held docs; scanned-PDF warn; CSP only api.typesafe.ai; Jev judges / agent reasons / user decides; selecting an option is not permission to implement; degraded fallback; pattern exact, judgement must clear floor; no matching pattern → no model call; not a correctness oracle; $0.00022 vs chat $0.00306 *theirs*; Spec vs artifact remainder; treating 0.85 as 85% / minProbability hard-gate as Harbor; VERIFY acquires discriminating evidence, never same-pool confidence-only rescoring; fast/full/max are ceilings not sizes; Solar writes, Jev chooses NEXT ACTION; SemIf 2186★ (+20 vs §109 2166); jevlike 1038★ (+7 vs 1031); TypeAR 14★ flat; AnotiaWang 96★ (+1 vs 95); yibie/awesome-jev 490★; Laya likes 802 (was 783); tracker likes 64 flat, lastModified UNCHANGED; do not reopen or amend PR #23/#24/#25/#26/#27. Soft Noul
≠ hard safety. `notes.md` §110.
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
**Cost-derived / typed-callback overlay (Empirical as
README target design; 2026-09-19 ~18:43):**
[Kungie/gut](https://github.com/Kungie/gut) — the
*algorithm* is ordinary control flow; the substituted
classifier step is a System One p that becomes
YES/NO/UNSURE from costs. cost-sensitive decision
theory × System One probabilities → control flow.
[Illusion47586/judge](https://github.com/Illusion47586/judge)
— judgment vs generation; deterministic execution
after probabilistic judgment; exactly one app-owned
callback; explicit uncertain branch. Overlays, not
species. Soft Noul ≠ hard safety (`notes.md` §99).
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
OpenCode host-port
([indiejoseph/opencode-jev-pruner](https://github.com/indiejoseph/opencode-jev-pruner)):
same envelope on `tool.execute.after`; default
`jev-zen` / `jev-1.13-free`; zen-chat ≠ Noul;
keepScore >0.1 floor; hook fail-open (`notes.md` §96).

**Named Decision Graph Protocol envelope (Empirical as README
+ spec, 2026-09-19 ~17:40):**
[numerous-com/dgp](https://github.com/numerous-com/dgp)
— the monitor is **application code** (freshness,
authorization, idempotency, provenance, side-effect
handling). Typed assessment may only record a judgment;
commit is the guarded act. Decision Graph Protocol
frame→assess→commit. app retains permissions/effects.
Jev-first assessor-neutral. guarded commit /
receipt/next frame. assessment batching.
hard-gating DGP as safety theater.
numerous-com/dgp ≠ TypeSafe official.
Speculative assessments cannot authorize effects
(`notes.md` §98).

**Named cost-table envelope (Empirical as README target
design, 2026-09-19 ~18:43):**
[Kungie/gut](https://github.com/Kungie/gut) — the
monitor is **the cost table in code**. Thresholds
derived from costs not hard-coded. The Noul may only
inform YES/NO/UNSURE; it does not grant. Hard-gating
0.038 is theater (`notes.md` §99).

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
OpenCode host-port (`notes.md` §96):
[indiejoseph/opencode-jev-pruner](https://github.com/indiejoseph/opencode-jev-pruner)
— same polarity; hook fail-open; zen-chat ≠ Noul.
**Native Apple locate (Empirical as README + source
comments, 2026-09-19 ~17:17):**
[gliner-native-runtime](https://github.com/shershah1024/gliner-native-runtime)
— encoder proposes spans; code owns offsets and
policy; default 0.1 still soft; not a Noul;
not keep/drop of held candidates; not position 4
Selector (`notes.md` §97).
**Decision Graph Protocol remainder after exact guards
(Empirical as README + spec, 2026-09-19 ~17:40):**
[numerous-com/dgp](https://github.com/numerous-com/dgp)
— JSON Schema proves record structure; the spec owns
freshness / authorization / idempotency; a structural
validator cannot prove those. Assessment is the
remainder sensor. Decision Graph Protocol
frame→assess→commit. app retains permissions/effects.
hard-gating DGP as safety theater.
numerous-com/dgp ≠ TypeSafe official (`notes.md` §98).
**Cost-derived remainder after the cost table
(Empirical as README target design, 2026-09-19
~18:43):**
[Kungie/gut](https://github.com/Kungie/gut) —
costs prove the *rule*; the Noul is the remainder
sensor. thresholds derived from costs not
hard-coded. Default UNSURE raises so an unhandled
middle band cannot become `False`. Soft Noul ≠ hard
safety (`notes.md` §99).
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



**0920 jcr HIGH (`notes.md` §116):** retrieve-wide → decide → evidence-set on a capability tree. one tool; returns context; **does not execute**. 0.6 band is application policy. routing ≠ permission. docs ≠ authority to run. n=1 lookup+explain; Not Harbor task-execution. NiazMorshed2007/jcr ≠ skill-broker ≠ skillranker ≠ jev-sift ≠ jev-lens ≠ jevusher ≠ jev_select_capability.

**0743 HIGH (`notes.md` §113):** Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%; abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%; 0.85 coverage 84.60% selective risk 1.18%; 26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled; Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084; reliability 0.007 but resolution 0.000; 27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624; 22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f; Student B MAE 0.148 / Pearson 0.836 / 86.0%; pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2; HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000; 2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated; E2 recomputes from saved probabilities; Space sha eda59e0a; MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T; T never changes argmax; siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling; second pass must be $0.00 from cache; The pages never call Jev; Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%; restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask; They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%; ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench; ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome; confidence is descriptive provider output, not a substitute for probability; Quality denominators include only valid scored answers; an exact halfway tie chooses the lower level; aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills; The local path does not claim to turn a smaller checkpoint into Jev; Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION; current-llm; 结构兼容，不是 Jev 模型能力; altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; Find where Jev belongs. Design the questions. Measure the difference; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★; SemIf 2241★ (+34 vs §111 2207); jevlike 1051★ (+8 vs 1043); AnotiaWang 98★ (+1 vs 97); yibie/awesome-jev 525★ (+19 vs 506); Laya likes 864 (was 822); tracker likes 67 (+3 vs 64); lastModified UNCHANGED `2026-09-20T04:29:16.000Z`; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32/#33; notes.md §113

Hourly 0743 uniqueness lock: Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%; abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%; 0.85 coverage 84.60% selective risk 1.18%; 26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled; Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084; reliability 0.007 but resolution 0.000; 27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624; 22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f; Student B MAE 0.148 / Pearson 0.836 / 86.0%; pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2; HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000; 2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated; E2 recomputes from saved probabilities; Space sha eda59e0a; MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T; T never changes argmax; siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling; second pass must be $0.00 from cache; The pages never call Jev; Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%; restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask; They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%; ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench; ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome; confidence is descriptive provider output, not a substitute for probability; Quality denominators include only valid scored answers; an exact halfway tie chooses the lower level; aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills; The local path does not claim to turn a smaller checkpoint into Jev; Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION; current-llm; 结构兼容，不是 Jev 模型能力; altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; Find where Jev belongs. Design the questions. Measure the difference; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★; SemIf 2241★ (+34 vs §111 2207); jevlike 1051★ (+8 vs 1043); AnotiaWang 98★ (+1 vs 97); yibie/awesome-jev 525★ (+19 vs 506); Laya likes 864 (was 822); tracker likes 67 (+3 vs 64); lastModified UNCHANGED `2026-09-20T04:29:16.000Z`; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32/#33; notes.md §113

**0806 HIGH (`notes.md` §112):** people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 421 / 189; impressions 35498 / 9613; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29

**0646 HIGH (`notes.md` §111):** Calibration is not alpha; NO CURRENT ALPHA CANDIDATE; ΔR² approximately +0.00084; Brier 0.2131387; ECE 0.0421875; Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05; default 0.5 keeps zero non pinned; keepResult median 0.14 to 0.17; keepCall median 0.28 to 0.35; usable range is about 0.10 to 0.25; 7.8% to 57.9%; judges results it never sees; task-finish eval not built yet; $0.002 per compaction; slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench; Jev 108/120 $0.083 0.34 s; Luna SGR 114/120; paired Jev accuracy-difference intervals include zero; not evidence of equivalence; GLM SGR 26/120 93 format failures; Terra-planned Jev hybrid 55/120; rule-based by default, optionally Jev-backed; empty README; missing key cannot break the experience; prefill plus exactly one decode; softmax over A/B/C ≠ Noul; BBQ 9,053/10,000 (90.53%); ECE 0.0890; Mean confidence 0.9943; overconfident; score and noul not implemented; DGUI 12 rows (was 6); INSTRUCT 119 rows likes 2; encode the state once, decide everything in parallel; 0.740 accuracy against a 0.508 majority; ECE 0.047; fine-tune's advantage ends where its 384-token training data does; jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd; Space does not call Jev; recomputes routing from saved probabilities; 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22; synthetic repository benchmark; Jev evaluations are advisory; YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; default threshold 0.8 still soft; 40-line windows cannot prove whole function; token-native sequential start/end Choice; Gemini/Haiku stubs not configured yet; handful of hand-written examples, not a benchmark; Jev judged exactly what it was given; laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills; contract_passed is not a claim of guaranteed factual truth; Wilson lower bound 0.85 floor; fixture mode no savings claim; SemIf 2207★ (+21 vs §110 2186); jevlike 1043★ (+5 vs 1038); TypeAR 15★ (+1 vs 14); AnotiaWang 97★ (+1 vs 96); yibie/awesome-jev 506★ (+16 vs 490); Laya likes 822 (was 802); tracker likes 64 flat, lastModified UNCHANGED; do not reopen or amend PR #23/#24/#25/#26/#27/#28.

Hourly 0843 mappings (`notes.md` §114): hysteresis policy latch; instruct-tuning honesty collapse; equal-width vs quantile; calibration does not compose; ranking ≠ calibration; catalog ≠ endorsement; advisory ≠ calibrated; independence recorded in AND-product.
User-provided 0806 uniqueness lock: people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 421 / 189; impressions 35498 / 9613; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29.


Hourly 0843 uniqueness lock: A hunch is a probability with a policy attached; { enter: 0.8, exit: 0.6 } is hysteresis; replay a policy change without inference; Decision models are providers, not the product; huncho ≠ Kungie/gut ≠ carldaws/hunch ≠ tpellet/hunch; pretrained Qwen2.5 base ECE 0.030 (0.5B) / 0.040 (7B); instruct 0.302 / 0.269; 70.9% → 70.0% mean conf 74.1% → 96.7%; temperature scaling still matches it in-distribution; No Jev API was called; Qwen2.5 ≠ Archer; Qwen/Qwen3.8-27B ≠ Archer; 学習済みモデル v0.1 は準備中です; bool AUROC 0.523; 先頭だと0件、末尾だと250件; 温度を渡さない場合、確率は較正されていません; このリポジトリには Jev を呼ぶコードが存在しません; g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev (same GitHub id 1378007307); 947 repos scored; A 273 · B 302 · C 372; LLM rubric ≠ benches; Data as of 2026-09-20; HEAD 895b9498; README SHA 3ae98c56; 13 focused checks and one mutually exclusive outcome; Probabilities are advisory, not calibrated guarantees; omni-/ask-jev ≠ pedroknigge/mcp_jev; pd.cut bins by equal width while jeval bins by quantile; ECE 0.113 and ECE 0.076; jeval drift is not implemented yet; rlaope/jeval ≠ dayhaysoos/jevals; calibration does not compose; ECE has exactly zero statistical power to detect the failure mode that kills trajectories; 25–60× headline withdrawn; P(all-correct): 0.0071 vs 0.0001; TCE / AMS; Qwen 3.8 sparring ≠ Archer; Deferred Crispification; light_cutoff_applied_to_combination 0; recorded run, kinematic animation; BANKING77 Accuracy BERT-Base 93.02 Jev 79.90; Analyse jev calibration (NLL, ECE) backlog; BERT figures are published supervised references, not zero-shot; 档位措辞效应 分数极差中位 0.50、最大 1.32; 修好后对照组是 0.01; 不是 benchmark; 概率没做 calibration; ~1,430 API calls, about $0.15; xiaohuaxi/jev-study ≠ wjdjdakf17/jev-study ≠ baekenough/jev-study; AND: product (independence assumed and recorded in the trace); chat model's stated confidence is not calibrated; circuit-vl-4b ≠ Archer; Bring your own API key; vamsikrishna2421/jev-usecases ≠ whyashthakker/awesome-jev-use-cases; catalog ≠ endorsement; SemIf 2237★ (+30 vs §111 2207); jevlike 1049★ (+6 vs 1043); TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 520★ (+14 vs 506); Laya likes 861 (was 822); tracker likes 66 (+2 vs 64) lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §114
**0915 HIGH (`notes.md` §115):** TianyuCodings/NanoJev unified-games-v1 densify; A 0.6B parallel decision model: states and questions in, complete probability distributions out. Zero output-token decoding.; One model, four games; ViZDoom Basic 128/128 vs Jev 56/128; Predict Position 27/128 vs Jev 11/128; Maze 225 attempts vs Jev 2738; Snake 30 food / 256 steps; held-out Maze 4/10 Snake 8/8 Basic 128/128 Predict 27/128; Untuned Qwen3-0.6B baseline; not TypeSafe Jev; open replica / specialist gameplay S1; Game success ≠ calibrated Noul; local type boolean ≠ TypeSafe noul; caijinchun/nanojev-arena ≠ liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠ NanoJev; do not reopen or amend PR #31/#32/#33/#35; notes.md §115
User-provided 0915 uniqueness lock: TianyuCodings/NanoJev unified-games-v1 densify; A 0.6B parallel decision model: states and questions in, complete probability distributions out. Zero output-token decoding.; One model, four games; ViZDoom Basic 128/128 vs Jev 56/128; Predict Position 27/128 vs Jev 11/128; Maze 225 attempts vs Jev 2738; Snake 30 food / 256 steps; held-out Maze 4/10 Snake 8/8 Basic 128/128 Predict 27/128; Untuned Qwen3-0.6B baseline; 18,760 questions per variant; 16,333 ViZDoom; 896 Predict Position expert episodes; hard_lr1e5; mix weights 1/3, 1/3, 1/6, 1/6; Hub C-Tianyu/NanoJev revision unified-games-v1 likes 58; dataset C-Tianyu/NanoJev-Data likes 5; HEAD 618cea6d906d54e128360786d12f703fff2b1245; 1289★ / 158 forks / size 64035; README SHA 4190093c64ee75b26e9726daa3b00cbcf6d3157a; MIT; caijinchun/nanojev-arena ≠ liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠ NanoJev; not TypeSafe Jev; open replica / specialist gameplay S1; soft scores ≠ hard gates; Game success ≠ calibrated Noul; local type boolean ≠ TypeSafe noul; invented_signal false; do not reopen or amend PR #31/#32/#33/#35; notes.md §115


User-provided 0920 jcr uniqueness lock: NiazMorshed2007/jcr MIT; site https://jcr.niazmorshed.dev; topics ai-agents,jev,mcp; **4★**; HEAD `138b3832`; README SHA `2a49dbc1`; LICENSE SHA `46231303`; size **14850**; Jev Capability Resolver; one tool to find documented deterministic commands in a nested capability tree; returns context; **does not execute**; skills = workflow+judgment; capabilities = individual operations; format independent of Jev; proposed open standard exploration; classify (Jev) → optional OpenAI decompose compound → beam search geometric mean of routing probs; keep up to 3 paths ≥60% of best (JCR_BAND_RATIO 0.6); ambiguity / no-match / depth-limit explicit; soft scores ≠ hard gates; 0.6 band is application policy; routing ≠ permission; docs ≠ authority to run; sol-vs-opus5-20 *theirs*: 20 scenarios × 4 variants = 80 runs; lookup+explain only, no execution; Claude Opus 5: agent input 108,585→15,819 (−85%), cost $0.3700→$0.1222 (−67%), wall 105.5s→77.7s; Codex GPT-5.6-Sol: 61,952→47,669 (−23%), $0.1377→$0.1151 (−16%), wall 25.3s→62.4s (Sol slower with JCR in 19/20); One Sol outlier 372.6s / 193 Jev calls; n=1 per cell; Not Harbor task-execution; Claude/Codex harnesses; compare mode; 50 scenarios bundled; 11 groups, 960 nodes, 11,360 items; 16 routing rounds per step; NiazMorshed2007/jcr ≠ skill-broker ≠ skillranker ≠ jev-sift ≠ jev-lens ≠ jevusher ≠ jev_select_capability; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34; notes.md §116

User-provided 0922 (`notes.md` §117 / items 330–336 / batch #100). SemIf was formerly OpenJev; MLX backend; 5.21× systems≠semantic; Softmax over options ≠ calibrated Noul; live REST 2282★. Do not reopen #23–#36/#38; do not push onto open #39/#40.
User-provided 0922 uniqueness lock: SemIf was formerly OpenJev; independent; not affiliated with Jev or TypeSafe; homepage openjev.com; default master; MIT; HEAD ca3ba65f1429; Tolerate float roundoff in MLX evidence verification; pushed 2026-09-19; live REST 2282★ / 140 forks; size 9177; README SHA 74ab7f7f; LICENSE SHA ca562883; interface pattern reproduction with open models; does not reproduce Jev undisclosed model/training; Direct option logits; 0 output tokens; shared-state parallel; MLX backend for Apple Silicon (`--backend mlx`); Qwen3.5-4B 3090 direct 1.023s vs AR JSON 5.332s (**5.21×**); argmax agree 18/21; systems comparison ≠ semantic equivalence; Parallel suffixes 20.03 dec/s on 777 decisions; Browser ladder Qwen3.5-4B authored BA 0.813, pert 0.766, TypeSafe subset agreement 0.845 vs Published Jev 0.883 (102 across 20 cases); Softmax over options ≠ calibrated Noul; typed output does not guarantee semantic correctness; wire/agreement ≠ replica of TypeSafe; SemIf ≠ kw2828/OpenJev playground ≠ zhihz/openjev ≠ apiplant/semif-rs port ≠ dddanielliu/semif-serve; rename is densify not a second census; JevBench 74.6 is §78 not this ladder; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#38; do not push onto open #39/#40; notes.md §117
User-provided 0940 uniqueness lock: Turn decision-shaped LLM prompts into proposed Jev primitives; This is a conversion assistant, not an automatic guarantee of equivalent behavior; The compiler uses deterministic heuristics, not an LLM or evaluation model; It understands a deliberately small set of common prompt patterns; Generated instructions and criteria must be reviewed before production use; Score ranges such as 0 to 1 are translated into ordered Jev criteria; Prompts requiring open-ended prose are not a fit; suitability strong/partial/not_a_fit; compatibility full/partial/none; Writing new text stays with an LLM; Review the generated Score rubric; Jev scores ordered criteria, not an arbitrary 0-to-1 range; Everything runs locally in the browser; There is no framework, database, account, API, or server-side prompt processing; The key is read from the process environment and is never stored or printed; connect-src 'none'; alexwestco/llm-to-jev ≠ altryne/jevify ≠ ryana/jevify ≠ fidecastro/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; HEAD 234058ab372d; README SHA 43cd94fb; LICENSE SHA 5f334006; compiler SHA fdf235d0; 2★; MIT; JavaScript; size 29; Pages https://alexwestco.github.io/llm-to-jev/; invented_signal false; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §118
Hourly 0947 uniqueness lock: Fast and cheap agent evals. jev as judge.; 18,041 skills from the 200 most-starred repos; Not a security scanner; 最简 Jev 调用演示器; confidence 不是正确率; q93304989-bit/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; 75% cheaper and 18% faster withdrawn; jev @0.15 100% recall 87% savings; 33Audits/jev-auto ≠ gargpratyush/jev-router; no Typesafe key, no PI_API_BASE, zero deps; tool-emitted Score/Noul ≠ calibrated Noul; semantic_compatibility: false; candidate_mass; Qwen3.5-2B ≠ Archer; Jev evaluates decisions; it cannot run a coding-agent session; Status: no model yet; S1LV3RJ1NX/openjev ≠ TheoLeeCJ/openjev; 28 accepted decisions; 3 targets; score 800; health 100; arcade game not a flight trainer; A successful live TypeSafe call has not been verified for v0.1.0; abhibansal60/tidy ≠ MANISH007700/tidy; No model, Jev included, predicted which channels its owner keeps; seed 1 selected on a held-out 400-item validation split; Brier 0.342 → 0.378; more accurate and more overconfident; Qwen3.5-4B ≠ Archer; static quants of kushalpatil/jevify-gemma4-26b-a4b; The labels were corrected, and one earlier result was retracted; zero of 23,869 eligible rows; Do not compare cost without checking task success; Exit 1 is not a proof; kisshan13/typesafe-ai-go ≠ Nibir1/typesafe-go ≠ official; 38 tests that cannot fail in a 356-model warehouse; if a parser can answer it, Jev is never asked; 359 of them; Games & Simulation 82; Education & Learning 1; Ratings are heuristics; syedabbasshaheer-art/jev-atlas ≠ ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas; anandi1989/awesome-jev-usecases ≠ whyashthakker/awesome-jev-use-cases ≠ walidboulanouar/awesome-jev-use-cases ≠ vamsikrishna2421/jev-usecases; Every headline result above is self-reported; Archer Hume 84.6% MMLU-Pro is a third-party probe not landed Archer; catalog ≠ endorsement; judge ≠ actuator; softmax over A–H ≠ Noul; SemIf 2270★; jevlike 1054★; TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 538★; Laya likes 889; tracker likes 68 lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#35/#36/#37/#38/#40; do not push onto open #39; notes.md §119


**Hourly 1049 HIGH (`notes.md` §120).** ggmlc GGUF is not llama.cpp. serving substrate ≠ calibrated replica. Qwen3.5-9B ≠ Archer. planner writes JEV selects. pick_by_id vs pick_second. soft scores ≠ hard gates. catalog ≠ endorsement. Do not reopen or amend PR #23–#42. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1049 uniqueness lock: ggmlc GGUF is not llama.cpp; Loading them in llama.cpp will fail; one encoder pass; hf:mys/laya-GGUF sha 713ae6f6e39f likes 0 apache-2.0; hf:mys/laya-multilingual-GGUF sha 3b645ae54281; hf:mys/laya-typed-decisions-GGUF sha 1e9e8ba1f527; hf:tozp/laya-onnx sha 0862aeba1e65 Opset 14 FP32 and INT8; tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; docker-laya MIT HEAD 1b8239a51ddd README SHA 9cb7bdc3; laya.cpp RTX ggml CUDA HEAD 8590937c79a2 README SHA cdd429b9; serving substrate ≠ calibrated replica; Softmax over options ≠ calibrated Noul; Qwen3.5-4B ≠ Archer; Qwen3.5-9B ≠ Archer; jev-position-test n=6 HEAD 7a56ca1c2698 README SHA 23f194c9; jevmlx slots 5 of 6; hosted Jev 0 of 6; prior_correction made it worse; jevSweeper mean Spearman ρ −0.274; picked exact-optimal 1/25 (4%); 31 of 36 still logically decidable; 86% of the time we should not have been asking; game success ≠ calibrated Noul; LLM2Jev 64★ Apache-2.0 HEAD 924618721277 README SHA da35fe61; not affiliated with or endorsed by Jev or TypeSafe; No answer tokens are generated; OpenSourceJev llama.cpp Qwen3-1.7B HEAD 3c41fba3681d; JEV-MLX Qwen3.5-9B HEAD dec24cd929ea; decision-head-rlcd Qwen3.5-4B 4.9M LoRA; AUTO_ACT is not a Noul; closed-set fail-open stdlib-only; verified=False; soft scores ≠ hard gates; 22 to 40% cheaper *theirs*; first version 70% more expensive; 111-case benchmark *theirs*; CDC 5,000 Jev 72.2% AUC 0.7725 *theirs*; accuracy is a trap; 9.0% base rate always-no 91.0%; catalog ≠ endorsement; jev-skill 109★ 90 scenarios HEAD 4f6e899a24d4; awesome-jev-live 673 entries 4★; minecraft-agent 214★ 131 JEV decisions 35 Astra calls; nether-final-08 8 minutes 43.300 seconds; planner writes JEV selects; RoboJEV structured simulator state not images; ashare-trader 策略未通过自己的回测门槛; 36 组参数全部净期望为负; no positive expectation under real costs; typed_evals NOT an official TypeSafe AI product; jev-as-judge is a sensor; third-person-audit 40% & 60% watermarks still soft; The included experience uses a handwritten demo provider; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42; notes.md §120


**Hourly 1143 HIGH (`notes.md` §121).** open recreation ≠ calibrated replica. semantic lint is a sensor not a proof. cutoff 0.8 still soft. paired bootstrap CIs *theirs*. Same accuracy, 35x faster *theirs*. systems comparison ≠ semantic equivalence. serving substrate ≠ calibrated replica. catalog ≠ endorsement. permission ≠ confidence. Do not reopen or amend PR #23–#43. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1143 uniqueness lock: open recreation ≠ calibrated replica; Qwen3.5-4B ≠ Archer; It is an open re-creation of Jev; less calibrated; perch 164★ MIT HEAD ba775a9940b6 README SHA 7ad0403b; semantic lint is a sensor not a proof; oxlint-plugin-jev cutoff 0.8 still soft; nassim-arifette/jevgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; patdown fuzzy linter; PanAchy/jevvy ≠ Atominac/jevvy; No orders, no advice; SmartMoney-Cub 25★ HEAD d93cf493853d; paired bootstrap CIs *theirs*; emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; +0.82 pts XQuAD-EN 95% CI +0.35 to +1.31; +7.62 pts SciFact CI +4.88 to +10.38; Same accuracy, 35x faster *theirs*; systems comparison ≠ semantic equivalence; BANKING77 500 Jev 81.0% GPT-OSS 82.8% Mercury 73.2% Gemini 85.4% *theirs*; frozen cascade missed its evaluation accuracy target 430/500 vs GPT-5 432/500; This is not demonstrated equal-quality savings; 24 invented tickets; Routing errors caught by the gate 0 of 3; sample too small to establish calibration; This is not TypeSafe Jev; No real API requests were made; wire-compat ≠ replica; KonghaYao/laya-jev 按官方接口写的客户端只改一个 base URL; gqgs/laya-onnx densify 496.8 MiB; tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; serving substrate ≠ calibrated replica; BeatAPI/awesome-jev ≠ 99hansling/awesome-jev ≠ Vishnurr2k01/awesome-jev ≠ robokrunch/awesome-jev ≠ rudy2steiner/awesome-jev-hub; All 125 projects; catalog ≠ endorsement; Pasblinn/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab ≠ q93304989-bit/jev-lab; Independent project. Not affiliated with TypeSafe; Kevthetech143/super-jev densify experimental V0.2.0; permission ≠ confidence; allay-team/openjev ≠ piyush-infocusp/openjev ≠ TheoLeeCJ/openjev; 2022 Mineflayer Jevalent collision; kushalpatil/jevify-gemma4-e4b GGUF densify; static quants; This dataset and model are independent research artifacts, not reproductions of Jev or RLCD; pngwn demo accuracy 0.705 ECE 0.046 ~112 ms *theirs*; cutoff 0.8 still soft; soft scores ≠ hard gates; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43; notes.md §121

**Hourly 1248 HIGH (`notes.md` §123).** decide is not generate. tryDecide returns typed calibrated judgments not a token stream. GLiNER/GLiClass ports are class members not Jev replicas. 93.5% *theirs* not Harbor. 74.9 *theirs* not Harbor. 8.7x *theirs* not Harbor. wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#45. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1248 uniqueness lock: decide is not generate; tryDecide returns typed calibrated judgments not a token stream; juspay/neurolink 133★ MIT HEAD 268b0fe83130 README SHA e709cadfa6b6 tag v12.19.0; GLiNER/GLiClass ports are class members not Jev replicas; MacPaw/Gliner2Swift ≠ Knowledgator/GLiClass.c ≠ fbilhaut/gliclass-rs ≠ Knowledgator/GLiClass.js ≠ gravitee-io/GLiNER4j ≠ apiplant/gliner-rs ≠ codesoda/gliner2-rs; 8.7x faster 4.4x fewer prompts *theirs*; 153 was a reporting error; corrected 156-case 9.8x faster 4.2x fewer prompts *theirs*; independent v0.2.1 1.24x vs Mini *theirs*; Approvals only; anpicasso/hermes-jev-approvals ≠ hermes-switchyard; scx-router GLiClass ranks candidate LLMs in one non-generative pass; typesafeai-dotnet-sdk Not affiliated with TypeSafe AI; hyperspaceai/jevcache ≠ kushals256/jevcache; ST-jeved measures each reply; 400 plain-text for unaskable question; razorback16/openjev:0.2.1 Docker densify HEAD 794a81b87131; wire-compat ≠ logit-equiv; Option-Marker joint attention 93.5% macro *theirs*; 93.6% micro *theirs*; n=78; T = 1.0367 vs T = 1.1692 two temperatures; guaranteeing is soundness theater; wfzyx/von densify HEAD bed7e7337791; Benchmark Heaven leaderboard #2 74.9 *theirs*; NLL calibration assets; 77.10% still §71 claim-audit; do not re-fold as a beat; Heman10x-NGU/openJev-verdict-2.0 densify HEAD bff28567cff4; kev-family weight tarballs; PLAN_Qwen35 proposal for review; deadline 0.53→0.82 at 9B *theirs*; Qwen3.5-9B ≠ Archer; isolation would fail by construction on DeltaNet; jaredpalmer/kev densify; JevBench v1.2.2 jeff 66.9 (#9) jev 75.3 (#2) *theirs*; logan-markewich/jeff densify HEAD 34b32f99a727; thinking=True/False per-field budget; type safety does not guarantee factual accuracy; TypeLLM/TypeLLM densify HEAD c4b03ba9e792; us/jev-local stub until hf; Eran-BA/Jev_from_GLiNER2 spec ≠ replica; lsu-ub-uu/systemone ≠ TypeSafe System One; Layan/Laya HF spaces name-match; catalog ≠ endorsement; decide ≠ generate ≠ stream; 93.5% *theirs* not Harbor; 74.9 *theirs* not Harbor; 8.7x *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45; notes.md §123
