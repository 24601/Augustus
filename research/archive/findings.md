# Deep-read findings (evidence for research/notes.md)

Derived from `analysis/evidence.csv` (169 repos, README-lines / langs / noul / choice / score / api / tests / threshold histogram) plus full deep reads. Status labels: **Contract** = verified from source/docs, **Empirical** = repo-published measurement, **Hypothesis**.

## dabit3/jev-experiments — 21 latency-first applications (Empirical, self-reported)

The densest public corpus of Jev application patterns. Recurring, transferable mechanisms:

1. **Latency is the product.** Every app's thesis: ~100–170 ms median round-trip unlocks a UX/product class previously impossible (per-keystroke, per-message, per-tick, hold-before-publish). With a 2 s "typical LLM" toggle, every pipeline visibly collapses (backlog, stale decisions, agent collisions).
2. **Judge once, re-policy in code.** jev-firehose stores raw probabilities; moving a threshold slider re-filters thousands of already-judged messages with **zero new requests**. Policy (thresholds) is client-side; judgment is precomputed. (Related: inbox-blitz re-ranks 3,500 judgments in 5.3 s when policy sliders change.)
3. **Per-keystroke fan-out with staleness control.** jev-launcher/jev-lint/jev-instant-search fire one request per keystroke with **no debounce**, tag requests with sequence numbers, apply newest-first, discard stale (57 requests, median 104 ms, 3 stale discarded, $0.0034). Lexical retrieval (BM25/MiniSearch) narrows to top-30; Jev re-ranks → hybrid retrieve-then-judge.
4. **One request, many independent questions.** Standard shape: 6–7 Nouls + 1–2 Choices per item (intent, churn, severity, category, flags). agent-assist: intent + churn risk + frustration + 5 yes/no flags + confidence-gated macro suggestion in one call, ~100 ms.
5. **Confidence-gated action tiers.** commit-sentry / send-guard / shell-guard: judge → **block / warn / pass** tiers driven by question type + confidence; safe commands run silently, risky confirm, catastrophic refuse. Pre-execution guard rails for agent actions (shell `accept-line` hook, pre-commit hook).
6. **Fan-out judge streams at scale.** inbox-blitz: 3,500 judgments / 5.3 s ≈ 95 judgments/s with ~96 concurrent requests. Scale lever = concurrency, not model size.
7. **Game/swarm agents.** jev-swarm: 32 agents, each ~400 ms tick sends local perception (~1k tokens) → move/boost/pursue; ~$10/h at 65 decisions/s. joshbla 2048 + mizchi gomoku (MoonBit) same pattern: board state + move candidates → Choice.
8. **Realtime human-flow integration.** jev-voice-turn: turn-taking/barge-in decisions on every partial transcript (has-speaker-finished / intent / interrupting). live-minutes: action items appear ~150 ms after each utterance. jev-tower: code predicts conflicts 120 s ahead, Jev picks instruction, code validates — **Jev decides inside a validated control loop**, physics/prediction/validation in code.
9. **Spreadsheets-that-think.** judge-sheets: custom formulas `=JUDGE(text,"yes/no")` (Noul→probability cell), score, choice — semantic judgment as a first-class spreadsheet formula.
10. **Pixel-free computer use.** jev-ax-pilot: Accessibility tree → compact JSON of actionable elements → one batched question set per step → execute via AX actions. No screenshots.
11. **turbo-rerank / nl-palette numbers:** top-1 accuracy 50%→100% on 40-query benchmark; nl-palette 100% vs 20% fuzzy on 30 cases.

## Other deep-read repos

- **AntonioCoppe/jev-harness** (Contract): TypeScript production-harness library — policy (map answer→action), confidence gate, **shadow mode** (log would-do without changing behavior), recipes, offline eval CLI replaying fixtures and asserting on actions not text. Measured: 24-row filter 48.9 s via `claude -p` vs **1.3 s** Jev (concurrency 8). Pattern: shadow-mode rollout is the safe adoption path for any guardrail.
- **FirasSX914/calibre** (Empirical, key negative result): Jev confidence calibration study, 500 ex/dataset. Banking77: Jev alone 77.8%@$0.051; DeepSeek alone 78.8%@$0.221; **Jev→DeepSeek route @0.67 → 80.2%@$0.103** (DeepSeek on 11.6%). Web of Science: Jev 52.8%, routing **ties Jev alone for 46% more cost**. **No routing parameter (optimal threshold, sign of accuracy gap, routing ROI) transferred across datasets** → thresholds/anchors must be re-measured per dataset; never port gates across domains.
- **stephanj/parallelConstraintDecoding** (Contract): fills a whole JSON schema of booleans/enums in **two forward passes** (prefill once → one masked step per field, batched). Java/llama.cpp via FFM; MLX port referencing HF `harshatheg/Qwen-2.5-1B-RLCD` which contains **no weights** — stock Qwen2.5-1.5B + custom code. Confirms the prefill-then-parallel-field inference architecture attributed to Jev.
- **arnabgho/rlcd-lite** (Empirical): reproducible RLCD reconstruction: GRPO + **Brier (proper scoring rule) reward** → calibrated decisions; claims binary reward does not yield calibration. Independently supports "proper-scoring-rule training is why Jev confidence is calibrated."
- **gamesonrblx/Jevbridge** (Contract): ACP-compatible adapter so Jev's typed decisions sit alongside Codex/Claude/Grok/OpenCode as a co-model in agent harnesses.
- **BrendanH18/jev-lab** (Contract): six demo apps + workbench; every call's latency/cost shown live, nothing canned.
- **BunsDev/clarity-judge** (Contract): multi-check writing judge — separate **named checks** (hedging, em dash overuse, clarity, filler, tone, passive, actionability), each with verdict + confidence + supporting sentence; demo mode with deterministic local mocks. Pattern: decompose one opaque score into N named Noul checks with per-check evidence.
- **mizchi/jev-gomoku** (Contract): MoonBit client + CLI + Jev-vs-Jev gomoku with per-move latency logging → GIF replay. Jev-vs-Jev self-play as a test harness.
- **joshbla/jev-plays-2048** (Contract): Jev picks moves for visible 2048; exports full request/response JSON per move.
- **GodsBoy/jev-agent-skill-router** (Empirical, prior notes): 94.4% vs 70.8% lexical routing; gates 0.30/0.40; shortlist 3.

## Cross-repo taxonomy (application generator input)

Application families observed across the archive: (a) streaming judge (moderation/log/inbox/triage), (b) keystroke-loop re-rank/launcher, (c) pre-execution guards (shell/commit/send), (d) agent self-assessment & routing, (e) policy loops over cached judgments, (f) game/swarm policies, (g) voice/meeting realtime flows, (h) computer use via accessibility trees, (i) formula/DSL embedding (spreadsheets), (j) retrieval re-rank (BM25→Jev→top-1), (k) multi-check judge dashboards, (l) shadow-mode adoption harnesses.

## programasweights/programasweights-python (Contract + Hypothesis coupling)

Compile-once local neural functions from NL specs (KV-prefix+LoRA .paw bundles over Qwen3-0.6B/GPT-2; llama.cpp; WASM browser runtime; offline fails closed). No Jev+PAW integration found across the 187-repo archive. Hypothesis couplings: Jev as calibration-teacher for PAW example sets (distillation), or Jev as shadow arbitrator/gate with disagreement rate as recompile trigger. Added to optimizer-integration.md with test obligations.

## Batch #4 deep reads (2026-09-18, user-named repos)

- **dbreunig/building-with-jev-skill** (Contract): 213-line doc-grounded skill (jev-1.13): workflow, primitive table, instruction keys (question/focus/inspect/note/compare/field), contrastive criteria, Score-level rules, state hygiene, speculative fan-out, confidence routing, taxonomy walk, counting via per-item Nouls, symptom→cause→fix diagnosis table, revision discipline. Distilled into skill reference `question-design.md`. Its sources list docs pages incl. `model-jaggedness/jev-1.13` and `llms.txt`.
- **dannote/jev** (Contract): Elixir/OTP — Jev as a **peer GenServer**; answers are messages pattern-matched; "clause order is the routing, thresholds are guards"; 100 calls in flight; tests call `handle_answer` with literal maps (no network). Pattern: decision policy as pure guard functions = maximal testability.
- **carlaiau/jev-reranking** (Empirical, honest benchmark): TREC DL2019 passage rerank, 41,042 pairs/43 queries: JEV nDCG@10 0.682–0.684 vs local monoBERT 0.718 (IDST 0.738); **JEV highest MAP 0.4748**; $0.76/41k pairs, ~37 s/query median. Conclusion: zero-shot Jev rerank competitive with tuned cross-encoders on MAP, behind on nDCG@10 — beats every zero-shot baseline in the paper row set except IDST. No marketing spin in the writeup.
- **scale-venture-partners/riff** (Contract): prose linter with ruff-style codes; static rules ms-fast, semantic rules one Jev call each with `p=0.92`-style calibrated output; 14 calls ≈ $0.0004. Pattern: hybrid static+semantic rule codes with per-finding probabilities.
- **matthewdonsemail-lab/open-typesafe-camoufox** (Contract): browser agent ~$0.0002/step, headed Camoufox, deterministic perception → 11 mutually-exclusive action kinds via Jev Choice; free-text writing model only when a text field genuinely needs it; full audit run folder. Shaped after awlevin/typesafe-computer-use.
- **hr98w/jev-visual** (Empirical): open Jev-like pattern on Apple Silicon (MLX Qwen3.5-0.8B): shared multimodal context reused, candidates scored directly from logits (no autoregressive generation); honest limits — Breakout works only after reducing control to "which region holds the ball" (region Choice, paddle code targets region center); 80 decisions → 9 bricks/6 returns. Insight: game control reduced to visual classification = the decomposition discipline in miniature.
- **Dicklesworthstone/skillranker** (already analyzed, §7): hook ranks skills from live context, calibration loop, fail-closed.
- **AntonioCoppe/jev-harness** (already analyzed, findings above): policy/gate/shadow-mode/eval-CLI.

## Batch #5 (2026-09-18, user-named)

- **probably-lang (southpolesteve/probably)** (Contract): an entire **programming language whose control flow runs on Jev judgments** — `while draft feels "like a LinkedIn influencer post" { … }`. Real parser + async interpreter (Bun/TypeScript); Jev supplies judgments, a text model supplies strings, interpreter owns variables/loops/budgets/replay. Judgment-state **recordings** enable exact deterministic replay (hosted demo = cached recordings, zero inference). Novel position: Jev as the *conditional operator* of a DSL.
- **superagents-lab/jev-search** (Contract): retrieval pipeline where Jev is both head and tail: understand (typed questions → query + sources + time range) → concurrent multi-engine lanes (site-restricted Google/DDG + vertical engines, one failed lane doesn't discard others) → per-result relevance Score → merge by URL + engine agreement + original rank, streaming NDJSON; speculative Google start while Jev interprets. Budgets: 15s per engine, 30s overall.
- **Kevthetech143/super-jev** (Contract): domain-independent harness = evidence → batched typed questions → decide → **permit (independent of model confidence!)** → execute one tool with idempotency key + cancellation → verify → JSONL trace/replay. Domain hooks: observe/questions/decide/permit/tools.validate/execute/reduce/success. Policy insight: the permission layer enforces domain rules regardless of what the model says — separate axis from confidence gating.

## Batch #6 (2026-09-18T14, X theme digest + topic:jev hour)

Design distillation only — no clone audit this hour. Raw files:
`archive/hourly/2026-09-18T14/`. Skill card: `references/mixed-architecture.md`.

- **Discourse (Hypothesis as social evidence, Empirical as placement pressure):**
  cost/prefilter 48, tool routing 33, agent gate/linter 27, mixed architecture
  16, skepticism 11. Stack replacement is the rejected reading; "just
  classification" is answered with *where typed judgment beats ad-hoc LLM
  classify* (schema-valid + calibrated + batched + cheap enough for per-item
  gates), not with novelty of classification.
- **ibrahemid/git-jev-stage** (Contract from README): candidates from `git
  diff`; one Choice per hunk (`include`/`exclude`/`mixed`); mixed and
  low-confidence stay unstaged; lines never split; atomic exact-patch apply;
  working tree never written.
- **ibrahemid/jevprune** (Contract from README): per-line relevance vs the
  task; last-N lines + error signatures kept in *code* before Jev; dropped
  ranges recoverable by run id. Context-economy family with winnow.
- **WiktorB2004/llama-index-jev** (Empirical, self-reported BEIR nfcorpus):
  MiniLM 0.340 nDCG@5 → MiniLM+Jev 0.396. **Rerank fails open** (keep
  retrieval order); **select fails closed** (or a declared default). First
  clean public per-action fail-policy split.
- **doeixd/jev-pref** (Contract, principles.md): YOU define the rule / JEV
  classifies evidence / CODE maps outcome / AGENT acts. Poor checks invent
  taste ("is this clean?"); good checks name visible evidence.
- **yousudip/lizard-agent** (Contract as decomposition): no LLM in the loop;
  closed action space from the page; extractive answers; prices/dates never
  touch the model. Mixed architecture with the generator omitted because
  nothing needs writing.
- **kylemclaren/jevql** (Contract): `jev()` / `jev_prob()` in SQL; CLI
  evaluates; database sees ordinary SQL. Judgment as a WHERE primitive.
- **aaravriyer193/OpenSmoke** (Contract as cascade): Jev over every agent
  step; LLM only on flagged runs for root cause. Prefilter of analyst
  attention, not of RAG chunks.
- **DanRWilloughby/snifftest** (Contract): countable rules score 1.00;
  judgment rules do not flag inside the unsure band (~0.4–0.6) because Noul
  0.5 on unreadable input would look like a clean draft.
- **frostney/clean-code-review** / **Eliran-Turgeman/repear**: rubric-then-
  prose (Jev against named rules, LLM writes review) and semantic smell
  gates (silent failures, weakened tests, scope creep).
- **luantak/is-malicious**: high-stakes pre-run gate — fail closed, sandbox
  still required; Jev yes is not authorization.
- **FirasSX914/Janus**: measure Jev vs other models on your data, then route
  (calibre's non-transfer result as a product).
- **Neighbor skills, do not absorb:** `harrymunro/decision-first` (try Jev
  first + lab log), `simota/tenbin` (design-time lint/eval). Augustus stays
  placement/method/falsification.
- **rongxinzy/LightJev**: train lightweight decision backbones. Reproduce/
  open — not an Augustus implementation.
- **convaiinnovations/laya** (Hypothesis, vendor card 2026-09-18): first
  shipped open *product* with the Jev-shaped interface (Choice/Score/Noul,
  no generation, Apache 2.0, ~421M, text-only, 512 tok/question). Not a
  TypeSafe drop-in. Vs-Jev latency/accuracy table is a claim; their own
  zero-shot ECE 0.207 vs in-task 0.060 is the transferable warning. Design:
  typed judgment provider, self-eval duty on open weights. Full note:
  `research/notes.md` §18.

Cross-repo addition to the taxonomy: (m) mixed-architecture cascade around a
generator, (n) exact-candidate selection (hunks/lines/elements) where Jev
never invents the candidate, (o) spec-as-rubric preference lint, (p)
fail-open retrieval vs fail-closed dispatch as a pair of policies,
(q) open vs closed typed-judgment provider (same primitives, different
eval/hosting duty).

## Batch #7 (2026-09-18, class-scope literature — Jev exemplar, not monopoly)

Not a clone audit. Design distillation for the *class* of fast/cheap
categorization-classification-scoring models. Skill card:
`references/judgment-class.md`. Full note: `research/notes.md` §19.

- **GLiClass** ([2508.07662](https://arxiv.org/abs/2508.07662), Knowledgator
  intro HTTP 200): joint encode text + all labels, one forward pass;
  sigmoid multi-label / softmax single-label. Cousin of GLiNER/NLI/SetFit.
  **Empirical** as an architecture; **Hypothesis** as a Jev substitute.
  Use for large/changing tag sets. Scores are affinities — not a silent
  fail-closed authorize. This is why Jev's 255-option Choice limit is not
  the class's limit.
- **Listwise vs decision** ([2208.06164](https://arxiv.org/abs/2208.06164),
  [2211.01494](https://arxiv.org/abs/2211.01494)): translation-invariant
  listwise losses improve order and destroy P(relevant). Cross-encoders
  that emit a "score" are usually this family. Proper-scoring / RLCD
  (archive: `arnabgho/rlcd-lite`) is the decision family Jev claims.
  Composition rule already observed in LlamaIndex Jev (batch #6) is now
  class-general: rerank fail-open, select fail-closed.
- **Vision scoring**: pixel-free (AX/JSON) preferred; region Choice over
  extracted boxes (`hr98w/jev-visual`); CLIP softmax = competition in the
  offered set; SigLIP sigmoid = pairwise affinity
  ([docs](https://huggingface.co/docs/transformers/v4.39.2/en/model_doc/siglip),
  [2510.13364](https://arxiv.org/abs/2510.13364)); VLM-as-judge is
  generation. Class-conditional coverage can collapse under shift
  ([2608.19376](https://arxiv.org/abs/2608.19376)). Laya is text-only —
  do not caption then score.
- **Agent-architecture portents** (Hypothesis as products, Contract as
  design pressure from batch #6 economics): full-traffic judgment;
  catalog+decision not stuffed prompts; two numbers two jobs; perception
  ≠ narration; open heads make the control plane local; cross-modal still
  thin; generator-only (and ranker-only) agents are incomplete.

Cross-repo addition to the taxonomy: (r) encoder-classifier one-pass over
a large label set, (s) listwise ranker as a *cousin* not a decision API,
(t) vision as candidate-generation plus scoring, (u) judgment-class model
as agent control plane independent of TypeSafe.

## Batch #8 (2026-09-18, formal/semi-formal/crossover — from brief)

Curriculum `FORMAL-METHODS-SYSTEM-ONE.md` not found. Design
distillation only. Skill card: `references/formal-methods.md`. Note:
`research/notes.md` §20.

- **Ownership:** proof/MC exhaust a model; DST searches executions;
  judgment estimates a state; code authorizes. Sensor ≠ constraint ≠
  searchlight. Noul-as-proof is rejected (also SKILL.md non-negotiable).
- **Hillel (Empirical as a published case, 10 Mar 2026):** 4% of GitHub
  TLA+ mentions Claude; example Alloy spec did not compile and checked
  tautologies; LLMs write obvious invariants, not subtle
  concurrency/liveness.
  [Source](https://buttondown.com/hillelwayne/archive/llms-are-bad-at-vibing-specifications/).
- **Resonate (Contract from their test docs):** Lean 4 spec +
  differential oracle + DST of the TS SDK — three layers, three owners.
- **Antithesis (Contract from intro docs):** deterministic hypervisor;
  you state properties; it searches; bugs reproduce from a seed.
- **Crossover metaphors (Hypothesis as mappings, Contract as
  intuition):** NATM / snap-fit / Norman gulfs / Leveson STAMP. Place
  judgment; do not substitute until a precondition survives.

Cross-repo addition: (v) judgment as sensor around a real checker/DST
harness, never instead.

## Batch #9 (2026-09-18, cross-domain mental models — not SWE-only)

Design distillation. Skill card: `references/mental-models.md`. Note:
`research/notes.md` §21.

- **Mission:** place typed probabilistic judgment with math/logic/
  algorithmic frames in AI, SWE, business, knowledge work, and life.
  Formal methods are one pillar, not the skill.
- **Frames:** EU + Chow abstention; Elkan cost-sensitive threshold;
  VOI; MCDA; search/control substitution; SDT criterion; Leveson
  sensor≠constraint; NATM/snap-fit/Norman as portable intuition.
- **Status:** non-SWE gallery is **Hypothesis** until labeled logs.
  Promote only with acceptance tests.
- **Non-negotiable:** code/policy owns exact work; model owns narrow
  judgment; never launder a Noul as proof.

Cross-repo addition: (w) judgment as a sensor in any control loop that
already has a policy — CRM, inbox, reading list, kitchen probe, not
only git.

## Batch #10 (2026-09-18, FM expansion + Hypothesis cards)

Design distillation. Cards: `references/formal-methods.md` (expanded),
`references/mappings.md` §6–§9. Note: `research/notes.md` §22.
Curriculum `FORMAL-METHODS-SYSTEM-ONE.md` still not found.

- **Alloy vs Apalache (Contract from named docs):** Analyzer is a model
  finder (SAT, scope). Apalache is SMT TLA+ with three analysis modes
  plus scripts. TLC is explicit-state. Bounded green ≠ proof.
- **DST trio:** Antithesis hypervisor; Resonate Lean+oracle+SDK;
  PufferLib env+seed / Ocean trainer contract (authors: not a
  comparative baseline). Judgment clusters failures; does not vote on P.
- **TOCTOU-of-Noul / AI×FM:** t0 judgment is not t1 authorize; vibing
  specs + receipt theater + mode laundering.
- **Hypothesis cards:** VOI/gather, SDT/ROC, Leveson control structure,
  search/control outside SWE. Promote only with an acceptance test.

Cross-repo addition: (x) three DST seats (hypervisor / in-product
harness / env-as-sim) around the same sensor/constraint split.

## Batch #11 (2026-09-18, curriculum fold)

Attached docs archived under `research/archive/curriculum/`. Skill
cards: `formal-semi-formal.md` (alias), expanded `formal-methods.md` +
`mental-models.md`, `mappings.md` §10–§16. Note: `research/notes.md` §23.

- **Resonate HQ (Contract from product docs):** durable async
  (Distributed Async Await), not an unrelated AI brand; promises settle
  in protocol.
- **Cauli ∩ Hillel:** typecheck-cost collapsed; strong-property cost did
  not. Vacuous models are a harm.
- **Kent / Shirky / Vanderburg / Agans:** ontology, situated density,
  measurement-under-load, debug sequence — portable, not SWE-only.
- **Hypothesis cards B–F + OR + situated:** spec pipeline, Alloy loop,
  RV sandwich, DST triage, durable agent, assignment hybrid, Shirky
  density. Promote only with an acceptance test.

Cross-repo addition: (y) semi-formal diagrams as *vocabulary* for
questions, compiled to a monitor before they enforce.

## Batch #12 (2026-09-18, jevals workbench)

Pointer only. Note: `research/notes.md` §24. Cite:
`references/validation.md` (offline-eval). Catalog: `docs/ecosystem.md`.

- **dayhaysoos/jevals** (Contract from README; Empirical as workbench
  existence): local MIT workbench for Jev questions against labeled
  cases (Noul / Choice / Score, combinations); compare saved runs;
  WebMCP + agent skill. Complements `scripts/evaluate_decisions.py`
  (Brier / reliability / cost on exported JSONL). Not affiliated with
  TypeSafe. [Source](https://github.com/dayhaysoos/jevals).
- **Status split:** the tool exists (Empirical). Hypothesis mapping
  cards (`mappings.md` §6–§16) stay Hypothesis until *your* labeled
  cases plus a card-level acceptance test pass. Do not promote from
  the workbench's example seeds.
- **Skill identity:** Augustus is not a jevals how-to. No CLI, env, or
  ports copied into skill cards.

Cross-repo addition: (z) labeled-case workbench as the acceptance-test
surface for Hypothesis cards, beside the offline JSONL evaluator.

## Batch #13 (2026-09-18T16:07Z, 10:07 Boise hour)

Standing fold. Note: `research/notes.md` §25. Cards: `judgment-class.md`
species map; `mappings.md` §17–§18; FAQ GLiNER / LLM-as-judge /
allowlist-then-judge.

- **GLiNER species (Contract as papers; Hypothesis as Jev drop-in):**
  locate = GLiNER spans ([2311.08526](https://arxiv.org/abs/2311.08526));
  categorize = GLiClass ([2508.07662](https://arxiv.org/abs/2508.07662));
  local multi-head = GLiNER2.5 ([fastino-ai/gliner2](https://github.com/fastino-ai/gliner2)).
  Discourse: laptop agentic decisions
  ([tweet](https://x.com/singularity_sah/status/2100980051550306418));
  36× is a tweet. Not a how-to.
- **openjev-lm (Empirical as named receipts):** 65/70 = 92.9% gold,
  6 vCPU overnight, teacher = hosted Jev. Independent gold still owed.
- **Brittleness (Empirical as published cautions):** brandonjcarl
  paraphrase swings; jevgate 0.91→0.37 on a comment, ±0.18 jitter.
  Mapping §17 Hypothesis as a law.
- **jevgate (Empirical):** Proven/Refused/Unknown; 0/59 unsafe unasked
  held-out; cannot block. Mapping §18.
- **doc-router (Empirical, this corpus):** 1.74× $; 9 vs 28 OCR misses.
- **Langfuse framing:** typed judge vs paragraph; not a Langfuse skill.
- **Pointers:** kevinpita/pi-jev-context (hide-not-delete sieve);
  jeiel85/jevscope next to dayhaysoos/jevals.

Cross-repo addition: (aa) GLiNER locate as a class *peer*; (ab) code
proves easy cases, model judges leftovers.

## Batch #14 (2026-09-18, trolley / dual orchestration / JevLint)

Same Boise morning. Note: `research/notes.md` §26.

- **Han Xiao trolley (Empirical as a demonstration):** Jev-style API on
  jina-reranker-v3.5 always pulls the lever, 1 or 1B.
  [Tweet](https://x.com/hxiao/status/2100973209114075330). Listwise
  relevancy ≠ decision rationality. Reinforces the standing rejection.
- **James Ward (Empirical as topologies, Hypothesis as AST planner):**
  Jev-as-LLM-tool vs Jev-as-outer-loop; MCP output schemas as plan state.
  [Tweet](https://x.com/JamesWard/status/2100976393546772628).
- **huntedman/JevLint (Contract from README):** file-level Noul ≥ 0.8;
  write→check→fix; no line-level/auto-fix. Sibling of jev-pref.
  Independent. [Source](https://github.com/huntedman/JevLint).

Cross-repo addition: (ac) listwise I/O can *look* like System One and
still fail the trolley; (ad) two mixed-architecture loops, not one.

## Batch #15 (2026-09-18, Hume architecture reconstruction)

Note: `research/notes.md` §27. Cards: `judgment-class.md` compute graph;
`mental-models.md` calibration; `faq.md`; `formal-methods.md`;
`validation.md` IIA clause. Not a TypeSafe contract.

- **Archer Hume essay (reconstruction):** [Jev's Architecture
  Unmasked](https://archerhume.com/posts/jevs-architecture-unmasked/),
  17 Sep 2026, HTTP 200, `jev-1.13.0`, ~10k API calls. Direct readout
  (`output_tokens` is billing, observed); question isolation observed,
  prefix KV inferred; causal decoder inferred, Qwen-closest tokenizer
  observed but not exact; IIA-style odds shift and order sensitivity
  observed; RLCD name published, loss identity inferred, confidence
  arithmetic observed; sparse MoE inferred not observed; batch not
  conversation, duplicate non-determinism observed.
- **Envelope:** ~32,768 / ~65,536 / 255 options re-measured. Independent
  probe of the existing contract, not a replacement.
- **WATCH:** [status tweet](https://x.com/4rcherhume/status/2100848840643612729)
  — Qwen3.8 27b-based, 265k, multimodal, no audio, ~65% done. "Smarter
  than Jev" is his claim against his own calibration and order warnings.
  Not shipped. Laya remains text-only.
- **TypeAR:** comparison sentence only (constrained AR vs readout). No
  how-to. The public Qwen3.8-27B checkpoint is a base, not this drop.

Cross-repo addition: (ae) black-box probe of a decision API is a
reconstruction with explicit inferred rows, not a second contract.

## Batch #16 (2026-09-18, effect-oriented loops + GLiNER author)

Note: `research/notes.md` §28. Cards: `mappings.md` §19;
`judgment-class.md` species map (GLiGuard on the categorize row);
dual-orchestration paragraph. FAQ "Is GLiGuard Jev?" confirms, does
not move locate.

- **James Ward (Hypothesis as a placement; Contract as that client's
  README):** "Effect Oriented Jev-driven state-machine loops." Image
  sentence: the handler may run arbitrary ZIO effects while Jev remains
  the outer decision loop.
  [Tweet](https://x.com/JamesWard/status/2100981305009664299);
  [zio-typesafe-ai](https://github.com/jamesward/zio-typesafe-ai).
  Not Effect.ts. Not the Jev HTTP contract. Code owns transitions.
- **urchade (primary source, confirms species map):** GLiNER2
  multi-task classification "like jev" is GLiGuard Figure 3 —
  linearized schema, shared MLP, softmax or sigmoid, one pass.
  [Tweet](https://x.com/urchadeDS/status/2100929613857804379);
  [arXiv:2605.07982](https://arxiv.org/abs/2605.07982). Categorize
  beside decide. 36× Browser Use unchanged (tweet/Hypothesis).

Cross-repo addition: (ag) effectful FSM — soft Choice, host effect;
(ah) GLiNER author's own "like jev" is still categorize.


