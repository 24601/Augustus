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

Note: `research/notes.md` §31. Cards: `judgment-class.md` compute graph;
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

## Batch #17 (2026-09-18, TypeAR constrained-AR surface)

Note: `research/notes.md` §32. Hume reconstruction is §31. Card:
`judgment-class.md` constrained-AR surface (not a species). Ward
`mappings.md` §19 already existed; cross-linked, not rewritten.

- **TypeAR (Contract as README, HTTP 200):** typed decisions on a
  pretrained open autoregressive model; no proprietary API, no
  retraining. Enums ≤16; string/int/number/boolean; open integer/number
  added 2026-09-18. Sequential conditions on prior values; batch forks
  after shared prefill. One output token per closed decision. Prefix
  reuse O(C + D·S). Argmax default; sample mode temperatures constrained
  scores. [Repo](https://github.com/zmtomorrow/TypeAR). No license file.
- **5.8× (Empirical only as their receipt):** Qwen3.8-27B, K=16
  booleans, batch vs sequential. Not re-run. Not a class benchmark.
- **WATCH:** Archer status tweet already in batch #15. Quantize-well
  and smarter-than-Jev stay claims. Hub authors `archerhume` /
  `4rcherhume` had no model repos this pass. Composition with TypeAR is
  Hypothesis until weights land.
- **rh-guard:** not a mapping in this fold. `24601/rh-guard` README
  is recorded under GLiGuard notes (§30) as a reward-hack hook, a
  different hole from jevgate. Cards still say abstention /
  jevgate-shaped gates.

Cross-repo addition: (ai) constrained AR decoding is a surface with a
next-token objective, not a decide species.


## Batch #18 (2026-09-18, GLiGuard README / paper)

Note: `research/notes.md` §30. Card: `judgment-class.md` categorize
row. FAQ: "Is GLiGuard Jev?" Ward card (`mappings.md` §19) already
present; not rewritten.

- **GLiGuard (Empirical as published architecture and author numbers):**
  0.3B schema-conditioned GLiNER2 encoder,
  `fastino/gliguard-LLMGuardrails-300M`. One bidirectional pass over
  prompt/response safety, toxicity, jailbreak, refusal. README: 23–90×
  smaller than 7–27B decoder guards; up to 16.2× throughput and 16.6×
  lower latency. Paper abstract says 17× lower latency; Table 3 matches
  the README. Not re-run. Not a Jev weight clone (WildGuardTrain, not
  Jev answers).
  [README](https://github.com/fastino-ai/GLiGuard);
  [arXiv:2605.07982](https://arxiv.org/abs/2605.07982).
- **Aggregation (their eval script, not new doctrine):** OR of unsafe /
  non-benign prompt labels; refusal overrides an unsafe response.
  Policy-in-code already taught. Not generalized.
- **"like jev" (discourse):** urchadeDS tweet, already §28. Same
  interface shape, different objective. A GLiGuard score is not a proof.
  LLM I/O safety ≠ coding-agent tool gates (jevgate shape).

Cross-repo addition: (ai) safety-schema encoder is a categorize peer,
not a decide clone.

## Batch #19 (2026-09-18 ~11:02 Boise — decision surfaces / HF / harness)

Note: `research/notes.md` §33. Card: `judgment-class.md` when-to-use
table. FAQ expanded. No Hub weights under `archerhume` / `4rcherhume`.
No Jev wrapper.

- **Archer still Watch.** Specs unchanged (Qwen3.8 27B, 265k,
  multimodal, no audio). New replies: 27B **dense** for one-forward-pass
  local speed once AR is removed, MoE next then shrink; multimodal base
  + text PT reportedly generalizes to images; driver is AU healthcare
  data-residency, not anti-TypeSafe; prefers "decision models" over
  "system one." Essay unchanged. Expected ~19 Sep Boise from the 18 Sep
  07:26Z hedge.
- **When-to-use (five surfaces):** proprietary Jev vs Archer Watch vs
  TypeAR vs encoder open-jev (DeBERTa-v3-large 434M, public gold, ECE
  0.022 / OOD 0.690) vs tiny LoRA distill (jev-gate-student-b,
  148,160-row corpus, yes/no logits). Axes: calibration, VOI, latency/$,
  deployment control, multimodal, enum size.
- **HF novel (HTTP 200):** jev-gate-student-b + jev-distill-corpus;
  jp-sns-jev7-estimator (not calibrated; threat F1@0.5 = 0);
  open-jev-deberta-v3-large; mini-jev-runs 27.9k (no token generated);
  jev-tree-choice-cap (truncate 0/90 on tail; keyword also 180/180).
- **Device / harness:** jev-mobile (Mobile MCP, candidate-only);
  jev-macos-loop (local perception, text-only Jev); jev-harness
  (already analyzed; selective abstention); routeKit (Jev estimates
  requirements, policy selects the model).
- **HacksonClark SREGym-Lite:** 20/50→24/50, 2 regressions. Jev ranks
  tests/evidence; does not diagnose. Coppe: keep tests closed; inspect
  regressions as calibration failures. Blog HTTP 200.

Cross-repo addition: (aj) decision-surface choice is an axis table, not
a sixth species; (ak) rank-next-test is VOI, not diagnosis.

## Batch #20 (2026-09-18, marginals / Nimble / djev-spark)

Notes: `research/notes.md` §34–§37. Cards: `judgment-class.md`
(marginals; holes table extended; Nimble subsection); FAQ; one
mental-models sentence; one `validation.md` sentence. Not a PPL
tutorial and not a serving how-to.

- **Erik Meijer (claim, his correction):** Jev is a cool API and not
  probabilistic programming. Kleisli qualifications exaggerate. Gloss
  he endorses: marginals vs joint.
  [Post](https://x.com/headinthebox/status/2100984170004824221).
  Matches §31 isolation; does not restate the essay. Joints and
  invariants stay with TLA+ / Alloy / contracts.
- **Bespoke Nimble (Empirical as their README receipt):** contrastive
  hard labels, not a Jev distill. 2,676 train / 324 holdout. Agreement
  90.12% / Jev 1.13.0 93.21% / untuned Qwen3.8-27B 84.88% / base 9B
  66.36%. Model card Apache-2.0 LoRA on Qwen3.5-9B; repo license
  absent. 9B-enough is **Hypothesis**. Tweet 100ms dropped.
  [README](https://github.com/bespokelabsai/nimble).
- **djev-spark (Empirical as interface; Hypothesis as a win):**
  DiffusionGemma 26B-A4B NVFP4, Jev-shaped I/O, images beyond stock
  Jev. Third compute graph beside a decision head and TypeAR.
  [README](https://github.com/mmastrac/djev-spark). Archer drop stays
  WATCH.
- **tenderizzation:** "welcome back ResNet-50." Discourse only. FAQ
  not expanded.

Cross-repo addition: (al) open contrastive recipe as a decision-head
data pattern beside RLCD; (am) diffusion structured reads as a third
Jev-shaped compute graph.

## Batch #21 (2026-09-18, Atallah entropy buckets)

Note: `research/notes.md` §38. Card: `judgment-class.md` (entropy as
allocator, next to marginals; when-to-use pointer). One sentence each
in `mental-models.md` and `formal-methods.md`. Not a mappings §N. Not
a Jev how-to.

- **Alex Atallah (claim / rhetoric):** decompose AI tasks into low,
  medium, and high entropy. Examples: who should review a PR; review
  the PR; write a PR. He thinks frontier models are needed only for
  the third.
  [Buckets](https://x.com/alexatallah/status/2099511056989147147)
  (2026-09-14). Later post claims Jev is the first model to truly
  optimize for the first two — a **claim**, not a result.
  [Quote](https://x.com/alexatallah/status/2100962947711295557)
  (2026-09-18). fxtwitter 200; x.com 403.
- **Placement (Hypothesis):** typed low/medium decisions are Meijer's
  factorized marginals (System One). High-entropy synthesis is the
  joint a decoder writes. Same axis as VOI / compute. Agent loop: many
  cheap scorers, rare writes. "Review this PR" as medium is still
  partly generative — decision-versus-generation cut, not an entropy
  meter. Charts are the same rhetoric, not a benchmark.

Cross-repo addition: (an) entropy buckets allocate a decision surface
versus a generator; they do not measure entropy and they do not make
Jev a probabilistic program.

## Batch #22 (2026-09-18, perception then judgment)

Note: `research/notes.md` §39. Card: `judgment-class.md` (next to
djev-spark / Archer Watch / when-to-use). One composition sentence in
`mental-models.md`. One contract-surface sentence in
`formal-methods.md`. Does not restate the entropy allocator (§38).

- **Basit ask (Hypothesis):** primary post not retrieved. No tweet id.
  SAM 3.1 + Jev and ASR + Jev are application patterns for omni-ish
  products: specialist perceive, then System One on the resulting
  state. They are not native omni System One. Information dies at the
  interface.
- **SAM 3.1 (name verified):** Meta Segment Anything 3.1. Masks and
  tracks. Object Multiplex.
  [Hub](https://huggingface.co/facebook/sam3.1) HTTP 200 (raw README
  gated 401).
  [Release](https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md)
  HTTP 200.
  [Blog](https://ai.meta.com/blog/segment-anything-model-3/) HTTP 200.
  Perceive, not decide. No API copied.
- **ASR instance, not the ask:** Moritz Kremb transcript → Jev
  (2026-09-17).
  [Post](https://x.com/moritzkremb/status/2100577979021832365). His
  latency and price stay his.
- **When the joint matters:** Archer Watch (no Hub weights; no audio;
  not Empirical), djev-spark images (think/sequential reject images),
  future audio-capable shared models.
- **Does not contradict:** Meijer marginals vs joint; Atallah buckets
  are rhetoric not a meter; "review this PR" is partly generative;
  "first model ever" is a claim. Noul is not a proof. Code owns the
  schema.

Cross-repo addition: (ao) perception-then-judgment is composition of
two species, not one omni decision model.

## Batch #23 (2026-09-18, eval & hill-climb)

Note: `research/notes.md` §40. Canonical section:
`references/validation.md` (Eval & hill-climb). One table, not five.
Cross-links only: SKILL.md, when-to-use, mental-models, optimizer
integration. Perception §39 and Atallah §38 left in place.

- **dayhaysoos/jevals** at `af6fecc`: README, PRODUCT.md, DESIGN.md,
  `skills/jevals/SKILL.md`. Independent keys; Noul/Choice/Score sharing
  state; correctness ≠ confidence (Brier / MAE / within-tolerance);
  immutable runs; compare only equivalent fully successful runs;
  question-scoped ranking. Agent skill: no dedicated split control;
  no `unknown` label. README/PRODUCT/DESIGN do not use those two
  phrases; they also do not document a split. Entry `npx jevals`
  verified; flags, keys, and ports not copied.
- **Harbor** ([repo](https://github.com/harbor-framework/harbor),
  [tasks](https://www.harborframework.com/docs/tasks)): not previously
  named here. Separate verifier environment is documented; default is
  a shared container. No CLI copied.
- **verifiers v1**
  ([post](https://www.primeintellect.ai/blog/verifiers-v1), Will Brown
  with Mika Senghaas and Florian Brand, 2026-07-10): taskset × harness
  × runtime. Harbor is a taskset format inside verifiers, not a second
  product.
- **Basit ask, primary post not retrieved:** score before the model;
  HoH planner/developer/QA; Room driver; video-as-judge last. No tweet
  id.
- **Bake-off:** jevals-shaped suite before Jev vs Laya vs TypeAR vs
  Nimble vs Archer vs openjev-lm; Harbor taskset for product loops.
  Archer still Watch. 9B-enough stays Hypothesis. ECE in the table is
  wanted, not Nimble's published number (agreement on synthetic labels).
- **rh-guard:** one composition row. Different surface from jevgate.

Cross-repo addition: (ap) measurement has two seats — labeled decision
cases, and a product taskset — and LLM-as-judge is neither primary
score.

## Batch #24 (2026-09-18, perception-decision pipeline)

Note: `research/notes.md` §41. Card: `validation.md` (pipeline,
measure, hill-climb). Does not replace §40's Eval & hill-climb, §39's
composition card, or §38's entropy allocator.

- **Basit ask, primary post not retrieved.** No tweet id. Pipeline is
  stages with a versioned state contract: perceive → optional fusion
  in code → typed marginals → policy in code. Joints across stages
  live in code (Meijer).
- **Measure before optimizers.** Stage metrics (IoU / track IDF1 /
  WER; accuracy + ECE/Brier + option-order; policy regret). Frozen
  taskset for end-to-end. Harbor and Verifiers names stay in §40.
  Falsifiers: flip one fact (Nimble pattern, not a tutorial);
  garbage-in must not look confidently correct; TOCTOU between
  perceive and act. jevals for the decision stage. LLM-as-judge is
  not the primary score for calibrated System One.
- **Hill-climb.** One stage or one interface per change. Latency and
  cost climb apart from quality. Axes: perception, schema, backend
  (Jev vs TypeAR vs Nimble vs openjev-lm), thresholds, or collapse to
  native multimodal System One when interface loss stalls end-to-end
  gains.
- **Ax vs DSPy (narrow yes).** Ax README verified: DSPy for
  TypeScript, [ax-llm/ax](https://github.com/ax-llm/ax), already in
  sources.json. LM-program knobs only. Not SAM, not ASR, not Jev
  calibration, not the architecture choice. Nimble holdout is
  agreement, not ECE.

Cross-repo addition: (aq) a perception-decision stack is climbed as
contracts and stage metrics; DSPy/Ax do not climb the perceiver or
the calibration.

## Batch #25 (2026-09-18, ~11:59 Boise hourly)

Note: `research/notes.md` §42. Docs-only. Archer still Watch.

- **pcdServer (Contract as README):** native TypeAR-class serving.
  MIT C++20 llama.cpp. 2–256 enums, 1–63 fields. Softmax over allowed
  ≠ Noul. Apple+Linux. No OpenAPI copied.
- **typesafe-jev-tools (Empirical as 149-row receipt):** Jev 79.9% vs
  Haiku 4.5 83.2%; Jev 1.6× faster not 20–200×; Jev confidence
  monotonic, Haiku inverts 0.80–0.95. Meta-VOI three-way test.
- **jev-mode:** synthetic 1,000; −77.8% tokens; accuracy is parity.
- **OpenSmoke:** env_broken vs agent's own bug; heuristic P=R=0.86 on
  12 traces; Jev on that fixture not measured.
- **jevql / joxide:** store or index in code; judge a shortlist.
- **jot:** topology B, closed catalog. Claim: first general-purpose.
- **openevals:** online full-traffic; beside Harbor.
- **hermes-jev-north-star:** deterministic then Jev; refuse empty.
- **pi-jev:** not pi-jev-context.
- **jev-plays-games:** legal moves from code; p ≠ win odds; 12-call
  option-order probe.
- **laya-typed-decisions:** companion packaging; unverified 0.766 /
  0.066. Do not overwrite §18.
- **X:** runtime schemas still closed per request; live typing sieve;
  60% / 20× claims; GLiNER lesson already taught; FunctionGemma
  on-device; fintech unit is a decision; Pareto takeaway.

Cross-repo addition: (ar) three open paths — encoder / constrained AR
serving / trained decision-only — plus a VOI gate *before* any of them.

## Batch #26 — second adversarial pass (2026-09-18)

Review of the whole skill at `7b3a0c3`. Zero blockers. Patched: no
install command on the jevals card (PRODUCT says unpublished); SAM/ASR
are producers not perceive; two call shapes removed from the optimizer
card; $0.042/MTok tagged vendor-stated; GodsBoy 94.4% tagged
exploratory. `notes.md` §43.

## Batch #27 (2026-09-18, ~12:58 Boise hourly)

Note: `research/notes.md` §44. Docs-only. Archer still Watch (no
architecture rewrite). Do not rehash §42 HIGH.

- **sqlite-jev (Contract as README):** in-engine SQLite extension;
  batched `jev_rows`; sibling *pattern* to jevql, different serving
  (DB sees `jev()`). Inspired by pg-jev. Semantic full scan, not an
  index. License file absent. 0★.
- **bitrate-advisor (Empirical as a shape):** Jev proposes ABR; policy
  is the envelope; never bolder. Missing model → policy answer.
  Three-state receipt author-reported.
- **jev-routing (Contract as README):** Go host adapter, not MCP, for
  Claude/Codex/Grok. Compact then one Choice + done.
- **jev-claw (Empirical as author's 10/10 + 11 offline tests):** Jev
  classifies; `decide()` maps; path regex floors risk; confidence is
  min.
- **jev-harness practice:** already §33; this hour assert-on-action
  as Harbor-adjacent substrate; recipes across business/life.
- **openjev-lm / jev-gate / DeBERTa / mini-jev-runs / tree-cap /
  jev-pref:** frames only (receipts economics; memory gate; encoder vs
  decoder replica). No rewrite.
- **jev-voice-control / JevML:** README-only stubs. Hypothesis.
- **X:** mmalisper JOB hybrid +12% geomean, join-order 2× slower,
  fail-open to Postgres (author-reported). Higgsfield GenAI auto-route
  is a claim.

Cross-repo addition: (as) structured-store semantic index has an
in-engine vs CLI fork; (at) soft judgment inside a hard envelope
(ABR, planner); (au) distill-to-device as a context sieve, not only
an action gate.

## Batch #28 (2026-09-18) — kev runnable Archer reconstruction

Note: `research/notes.md` §45. Docs-only. Folded into PR #2, not a
second PR. Archer 27B drop still Watch.

- **kev (Empirical as named ID receipt; Contract as README/API).**
  `jaredpalmer/kev`, Apache-2.0, 24★ this pass. Qwen2.5-0.5B LoRA +
  pointer; `POST /v1/systemone`; typesafe-sdk `base_url`. Public gold,
  not a Jev teacher. Isolation exact (Δ 3.7e-6; sibling p=0.03 vs
  state 0.99). ECE 0.065 / 0.031 after T; acc 0.799 / 1,350 ID.
  Permute 7.4%; IIA mean 0.13; boundary forgery held. 0.5B knowledge;
  ID calibration only; not multimodal.
- **Place:** trained decision-only open path next to Laya / Nimble /
  Watch. Cleanest *runnable* productization of Archer's reconstruction.
- **Contrast:** TypeAR (constrained AR ≠ Noul) vs encoder DeBERTa
  (OOD measured) vs proprietary Jev vs openjev-lm (teacher-copy).
- **Eval:** jevals/Harbor bake-off candidate; mechanism tests mirror
  Archer probes.
- **When-to-use:** laptop-local System One for development/eval; not a
  knowledge/frontier substitute. No serve how-to.

Cross-repo addition: (av) the trained decision-only path now has a
shipped API-compatible reconstruction (kev); Watch remains the 27B
announcement.

## Batch #29 (2026-09-18, ~14:03 Boise hourly)

Note: `research/notes.md` §46. Docs-only. Folded into PR #2. Archer
27B drop still Watch (Hub empty). No invented metrics.

- **blackwood-rlcd (Empirical as named vendor receipt; Hypothesis on
  your labels).** Open multimodal RLCD, CC BY-NC, Jev-compatible shim.
  Web 0.907 vs Jev 1.13 text-only 0.480; letter-shuffle 0.133 vs 0.587;
  ECE 0.037; ~200 ms H100. Jev still leads general text 0.850 vs 0.786.
  Screenshot vs Jev-text is not the same input. Omni decide can ship
  without waiting for Archer. Soft judgment over marked pixel
  candidates; code clicks.
- **open-jev-laya-bench (Empirical as that named receipt; not a Jev
  ranking).** 26+9 tasks, 11959 test / 3269 cal. Macro acc Δ +0.023
  [+0.013,+0.032] neutral, +0.229 [+0.198,+0.262] home. ECE/NLL/Brier.
  LLM-as-judge is not the score. Harbor/jevals practice in the wild.
- **Foodoo1 decision-token QLoRA (Empirical as 200-case receipt).**
  Train the single decision token under parallel constrained decode.
  fraud_risk 64→95%, overall 85.2→98.8% at ~234 ms/4-field. Synthetic;
  not a financial product. Softmax ≠ Noul.
- **jevgate frame (already §25):** allowlist *proves*; Jev judges only
  unlisted; fail-open (cannot block).
- **wellposed (Empirical as request-lint recipe):** missing `other` →
  confidence 1.00 wrong; gating cannot catch it. Broken state paths.
  `tenbin` owns the lint skill.
- **jev-reflex-autonomy-lab:** S1 keeps control; optional S2 one-use
  advice. No metrics. License null this pass.
- **MED:** jev-decision-layer (gate is part of the result); jev-e2e
  (Playwright checks; confident model cannot substitute); jevpandas
  (dataframe semantic index; LICENSE 404).

Cross-repo addition: (aw) omni decide is a shipped open head, not a
Watch-only hole; (ax) bake-off substrate with ECE/NLL/Brier in the
wild; (ay) decision-token LoRA is how you train constrained-AR, not a
new species; (az) confidence gating cannot catch a forced Choice.

## Batch #30 (2026-09-18) — Abide productized preference lint

Note: `research/notes.md` §47. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. No invented metrics. Text/diff only.

- **coldteadotai/abide (Empirical as README + dated replay; Hypothesis
  on your AGENTS.md).** MIT, created 2026-09-18, TypeScript, npm
  `@coldtea/abide`. Productized Jev hooks: one Score per soft project
  rule on the diff, never the conversation. Linter owns hard rules
  (jevgate-family sandwich, different remainder). Edit vs turn is an
  observation window. Bands ≥0.8 / 0.5–0.8 / <0.5 are their operating
  point, not a universal 0.8. Fail-open hooks. Rubric quotes source
  lines; calibrate/tune rewrite dead rules. Replay 93 sessions, 1,256
  edits / 147 turns, $0.22: independent-reviewer precision edit 26% /
  turn 73% before tune. Turn-phase soft rules held up better. No
  turn-number drift. Replay does not measure in-session repair.
- **Siblings:** jev-pref (contract Abide productizes); rh-guard
  (eval-integrity, not project soft rules); wellposed (request lint
  upstream); jevgate (hard envelope); JevLint (file-level conventions).
  Do not merge products. Do not copy hooks.

Cross-repo addition: (ba) preference lint has a productized compile /
calibrate / tune / replay path; (bb) observation window (edit vs turn)
is question design; (bc) banded fail-open means soft judgment is never
the sole hard veto; (bd) false positives in the rubric, not the model.

## Batch #31 (2026-09-18) — kev delta (Hub + NOTA)

Note: `research/notes.md` §45 delta. Docs-only. Folded into PR #2.
Not a rewrite of §45. No species change. No invented metrics.

- **Hub weights.** [`jaredpalmer/kev-0.5b`](https://huggingface.co/jaredpalmer/kev-0.5b)
  HTTP 200. `kev.publish`; `--run` accepts Hub ids; base still
  downloads on first load. GitHub release tarball remains. 61★ this
  pass (signal had 53★).
- **PEFT.** `task_type=FEATURE_EXTRACTION`; publish patches legacy
  adapters with null task_type. Docs mention only kev-0.5b.
- **NOTA training (HIGH question-design).** First run learned "this
  wording ⇒ pick it". Fix: add none-of-the-above as a wrong
  alternative too; vary wording; dedicated `none_of_the_above` eval
  (present vs removed). **No published rates.** wellposed still
  owns request-shape lint; training must confront the residual
  option.

Cross-repo addition: (be) bake-off fetch path is a Hub id; (bf)
Choice `"other"` is a training confrontation, not only a request hatch.

## Batch #32 (2026-09-18 ~14:52 Boise) — extractive / local surface / speed layer

Note: `research/notes.md` §48. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. No invented metrics. Do not re-fold
blackwood-rlcd, open-jev-laya-bench, decision-token LoRA, jevgate,
wellposed, jev-reflex-autonomy-lab, Abide, kev, jevpandas,
bitrate-advisor.

- **AppitStudio/testimonial-miner (Empirical as README fixture).** MIT.
  Gmail → numbered sentences in code → one broadcast (Choice/Noul/Score
  + per-sentence Nouls). Model never writes. `redecide` retunes
  thresholds on the log. 8-request fixture: 5 candidates / 3 rejected
  / 3 header skips. Offline tests use fakes.
- **choxos/jev-reviewer (Empirical as sample study).** MIT. Pointer at
  line ids; code copies verbatim with place. *Not found* is an answer.
  712-line article: 1q 10 req / 1.2–2 s; 9q 17 / 2.3 s. Spot checks,
  not a validation study.
- **us/jev-local (Contract as surface; Hypothesis on your labels).**
  `POST /v1/systemone` drop-in. Default scorer is a **deterministic
  stub** until `JEVLOCAL_SCORER=hf`. LICENSE absent this pass. Not a
  Jev reproduction.
- **hitakshiA/solari-reflex (Empirical as named table).** MIT.
  Observe → decide → verified act; no screenshots. Vs Codex on Solari:
  60.2 s vs 194.9 s; 66 s vs 460 s; 24.2 s vs 98.4 s (~3–7×).
- **ktaletsk/jevframe (Empirical as shape).** MIT, PyPI. pandas and
  Polars `.jev`; full `p__`; no silent renormalize. Sibling of
  jevpandas, not a re-fold.
- **MED:** jev-hermes (route ≠ memory); agent-workflow-typesafe-ai
  (advisory sidecar, Apache-2.0); dag-jev (structure induction;
  experiment; no metrics); jev-agentworld-web-simulator (decision
  control / generator content); jev-testbench (collab arms; LICENSE
  absent); jevscan (AST ∩ semantic; `tenbin` owns lint); pi-jev-approver
  (fail-closed without key; light note); Mattepiu/laya-onnx (~15 ms
  CPU; do not copy vs-Jev table).
- **Spotcheck:** SemIf 1551★; jevlike 866★; Awesomejev 488/21644 not
  re-derived; tracker lastModified 2026-09-18T20:12:57Z; Laya listed;
  Blackwood not.

Cross-repo addition: (bg) extractive keep/drop + offline re-threshold
is judge-once/re-policy; (bh) pointer-not-generator is citation
integrity; (bi) `/v1/systemone` drop-in is a surface — stub ≠ scorer;
(bj) observe→decide→verified-act needs no screenshots; (bk) route ≠
memory; (bl) advisory sidecar never changes host routing; (bm) collab
arms belong in the measurement curriculum.

## Batch #33 (2026-09-18 ~15:52 Boise) — boundary map / Harbor bake-off / dual-process

Note: `research/notes.md` §49. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. X discourse blocked this hour. No
invented metrics. Do not re-fold §48 items.

- **Zaious/jev-capability-atlas (Empirical as an axis, not a
  knowledge-breadth estimate).** README MIT / GitHub SPDX
  NOASSERTION. Unofficial. Extractable-from-state vs needs-outside
  knowledge. History suite table: A wrong@0.90 (Yongzheng; Kangxi by
  popular convention; GT contested); B near-flat 0.07 (luck);
  C right@0.97 with passage. N=3, single annotator. Internals ≠ FSM;
  placement is a component node. Confidence is a distribution
  statistic (RLCD). Dangerous-high ECE: DAIR Emotion 48% / 0.819 /
  16% p(correct)=0. Browser-use = DOM-as-text + speculative fan-out,
  not vision.
- **nibzard/decision-model-benchmark (Empirical as Harbor/jevals
  practice).** LICENSE absent this pass. Frozen protocol; v2 report
  of record; $28.34. jev banking 76.3%, spam 93.0%, S3 100%* at
  72.7% valid coverage (256+ cap), S4 flip 13%, S5 admits 49.7% /
  ECE 0.246; p50 264–276 ms; S1 $0.07/1k. No class wins on quality.
  Do not merge Banking77 87% / 76.3% / 79.67%.
- **Jevals/jevals-data (Contract as feedstock).** CC-BY-4.0. Boards +
  JSONL + suites. 2026-09-18 board, suite 0.1.0, 8 systems. Jev
  banking77 acc 0.7967 / ECE 0.0981 / p50 467 ms / $0.043/1k on
  *this* board. Recompute-from-logs; not a ranking.
- **taro1985/dual-process-ai (Empirical as a productized metaphor).**
  MIT. Kahneman S1 decide / S2 generate. Routing fails open; safety
  fails closed. Routing accuracy **unmeasured**. Keyword fallback ≠
  S1.
- **simonmesmith/jev-arc-agi-v1-experiment (Empirical as a
  negative).** LICENSE absent. Direct Jev 4/400 (1%), 1.125%, ~$2.32,
  10 min. Cell-wise Choice. Combinatorial ≠ extractive.
- **ikermoel/open-alternative-jev (Empirical as packed-logprob
  economics).** Apache-2.0. Not a Jev reproduction. RACE-H 92.9% @
  4.55 q/s; interference 6–9%.
- **wfzyx/von (Empirical as extreme speed/econ surface).**
  Apache-2.0. 14 MB SAN; authored144 52.6%. Not jev-local stub, not
  kev, not a Jev replica. Do not copy vs-Jev table.
- **jaredpalmer/kev (light delta).** 100★ this pass. No species
  rewrite.

Cross-repo addition: (bn) extractable-from-state is the placement
axis; (bo) retrieve-then-state is VOI with a named receipt; (bp)
Harbor-style class bake-off includes constrained LLMs and
baselines; (bq) public JSONL boards are feedstock, not rankings;
(br) dual-process is S1 decide / S2 generate with unmeasured
routing accuracy; (bs) combinatorial assembly is not extractive
keep/drop; (bt) local `/v1/systemone` has three surfaces (stub /
pointer / tiny SAN).

## Batch #34 (2026-09-18 ~16:22 Boise) — GLiNER2.5 extractive compaction

Note: `research/notes.md` §50. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. **Not Jev. Not multimodal.** No
invented metrics. Do not re-fold §48 extractive recipes, §49
bake-off, Abide, kev, GLiGuard species.

- **m-newhauser/gliner25-compaction (Empirical as README
  behavior).** Apache-2.0. Created 2026-09-18T17:22:34Z; 1★ at
  capture. Local GLiNER2.5 (`fastino/gliner2.5-base-v1`) chooses
  `keep_full` | `keep_evidence` | `keep_call_only` | `drop` for
  completed tool pairs and copies **exact character-offset** spans.
  Not a prose summarizer. Mutating tools / unknown shell / control
  operators → `keep_full`. Low-confidence / invalid evidence fail
  closed to `keep_full`. `shadowMode` default true (log, do not
  replace history). Reduction in characters, not tokens. No
  published retention-quality rates.
- **Mental models:** (1) pointer/extractive vs generator summarizers
  (family with testimonial-miner / jev-reviewer); (2) soft retention
  Choice under a hard mutation envelope — fail-closed contrast vs
  many fail-open Jev gates; (3) same compaction *job* as
  fast-jev-compaction / pi-jev-compaction, GLiNER encoder backend,
  Fastino/GLiGuard sibling class; (4) shadow mode as safe rollout.
- **rh-guard:** sibling note only (fail-closed retention, hard shell
  mutation, shadow). Not reward-hack detection.

Cross-repo addition: (bu) compaction that writes prose is a
different species from pointer keep/drop; (bv) fail-closed
`keep_full` names the *reduction* as the irreversible act; (bw)
compaction job is backend-agnostic (Jev Score/Noul vs GLiNER
encoder); (bx) shadow-mode default is the rollout for memory
mutation.

## Batch #35 (2026-09-18 ~16:48 Boise) — CI merge-gate, fail-open wake, S1 indexer, claim-evidence

Note: `research/notes.md` §51. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. No invented metrics. Do not re-fold
§50 compaction, §49 bake-off, Abide, kev, pi-jev-approver, jevgate,
rh-guard species.

- **CaseReed/latch (Empirical as README / offline demo).** MIT.
  Created 2026-09-18T22:09:12Z; 0★. Cluster in code; Jev labels
  cause; policy owns Gate PASS vs BLOCK. Judge never says ignore
  alone. Reporter never fails Playwright; `--gate` is a separate
  step. Demo: 8 connection errors → PASS; 5 assertions → BLOCK.
  Message-based grouping fragments (`pallets/click` 13→10). Pair
  Harbor + rh-guard.
- **shitianfang/wakegate (Empirical as safety table; 21/21 smoke).**
  MIT. Skip only if Jev answers and p(wake)<0.2. Same author wrote
  scenarios+question. Savings unmeasured. Contrast fail-closed
  pi-jev-approver / cannot-block jevgate / fail-closed compaction.
- **GreyssonEnterprises/s1-graphify-indexer (+ s1-indexer).** GLiNER2
  default; escalate LLM only if backend loaded. 10–50× **unfilled**.
  Degraded file-node graph if GLiNER cannot load; query does not
  invent edges. License not on GitHub this pass.
- **VladyslavHontar/clear-head (Empirical as README).** MIT. 1★.
  Stop hook: claims vs session lines. Keyword retriever; JEV_FIRM
  0.6 never blocks below.
- **reification-labs/foreman.** Description-only Phoenix scaffold.
  No Jev dep. Distinguish from super-jev "foreman" loop.
- **vinilana/jev-gateway-bench (Empirical as *shape* + one-run
  signal).** MIT. Chess perft hidden verifier; on vs off. Both
  36/36; 4 vs 6 LLM req. Author: not a measurement. Sibling
  jev-gateway fail-open if Jev down.
- **LightningK0ala/jev-marshal.** Empty repo. Watch / description.
- **LilDojd/jevons (Empirical as README policy).** MIT. Bounded Pi
  supervisor; shadow recovery; never generates commands.
- **MED:** Victor-Casado/if-ai (plain-English PR checks, fail-closed
  on error); alexsatch/omp-auto-mode (one-line README); jolehuit/
  jev-downloads-sorter (device-loop Choice); LakshyaChaudhry/
  jev-label-desk (empty README); flaviomartil/herdr-jev (~260 ms
  triage + triad; no-key heuristic).

Cross-repo addition: (by) cluster in code / judge labels / policy
decides (CI flaky-vs-real); (bz) name the irreversible act before
picking fail polarity (wake skip vs merge PASS vs compaction drop);
(ca) Harbor on/off routing with a hidden verifier; (cb) S1 extract
+ escalate-S2 is not a measured 10–50× until the table is filled;
(cc) claim/evidence Stop is anti-hallucinated-done, not a test
runner; (cd) description-only greenfield is not a product receipt.

## Batch #36 (2026-09-18 ~16:56 Boise) — GLiNER2 Ultrafast observe→score→act

Note: `research/notes.md` §52. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. **Not Jev. Not GLiNER2.5. Not
multimodal.** No invented metrics. Do not re-fold §48 solari, §50
compaction, §51 CI merge-gate / wake, GLiGuard species, or jev-ultrafast 7.1 s as this demo.

- **sahibzada-allahyar/gliner2-ultrafast (Empirical as README /
  architecture behavior).** MIT. Created 2026-09-18T19:35:23Z; 12★
  at capture. Adaptation of browser-use/jev-ultrafast. Local
  GLiNER2 (`fastino/gliner2-multi-v1`) extracts requirements and
  scores observed a11y/DOM controls. No screenshots. No generated
  selectors or JS. Code owns order, dates, freshness, clicks.
  Hybrid: local decide; Mercury 2.5 via OpenRouter for TYPE.
  `DONE` is loop termination; apps must verify outcomes
  independently. Inspector scores are not calibrated P(success).
  Demo (theirs, not re-run): NYC→SFO Flights 12.20 s visible /
  13.785 s loop / ~$0.0001 API. Demonstration, not a bake-off.
- **Mental models:** (1) observe→score-among-candidates→code-acts
  is backend-agnostic (Jev Ultrafast ↔ GLiNER Ultrafast; same
  lesson as compaction); (2) observed DOM/a11y candidates vs
  screenshot multimodal (solari / laya-mind2web DOM-index Laya vs
  blackwood-rlcd); (3) hybrid local decide + remote fill; (4)
  composition + independent outcome check.
- **rh-guard:** light note only (do not trust `DONE`). Not
  reward-hack detection.

Cross-repo addition: (ce) computer-use selection is
backend-agnostic on the same observed-candidate hole; (cf)
screenshot multimodal is a different input from DOM-as-text;
(cg) local decide + remote TYPE is mixed-architecture economics,
not dual-process-ai; (ch) `DONE` ≠ Harbor-verified success.

## Batch #37 (2026-09-18 ~17:15 Boise) — jev-pruner evidence-preserving Bash stdout prune

Note: `research/notes.md` §53. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. **Not a summarizer. Not session
compaction. Not GLiNER.** No invented metrics. Do not re-fold §50
gliner25-compaction as this product, §52 observe→score-act, or
fast-jev-compaction as a duplicate.

- **tamaratran/jev-pruner (Empirical as README / evals README
  behavior).** MIT. Created 2026-09-18T03:00:58Z; 5★ attached
  capture, 7★ live this pass. After Bash, Jev Noul-prunes stdout
  chunks before the main LLM sees them. No summary. Hard envelope
  (≤10k estimated tokens; JSON/XML/YAML/diff/binary; whole-document
  commands) then soft Noul. Fail-safe keep original; full archive.
  Marketplace id still `fast-jev-output`. Codex is opt-in wrapper.
  Manual sweep (theirs, 2026-09-18): needles 24/24; mean reduction
  83% (71–92%) on trim scenarios; wrongly trimmed 0/12; 240 ms.
  Harbor plugin-eval cannot reach Jev (fail-safe). Terminal-Bench
  paired pilot is integration, not a full bench.
- **Mental models:** (1) evidence-preserving prune ≠ summarizer
  (family with gliner25-compaction / jev-reviewer); (2) hard
  size/format envelope then soft Noul; (3) fail-safe keep original
  (reduction is the irreversible act); (4) stdout prune vs session
  compaction are different jobs; host capability shapes the product.
- **rh-guard:** sibling note only (fail-safe / envelope). Not
  reward-hack detection.

Cross-repo addition: (ci) command-output sieve and session compaction
share extractive honesty, not a product; (cj) structure-first
pass-through (≤10k / JSON-diff) is the sandwich, Jev is the remainder;
(ck) Harbor plugin-eval refusing Jev is a fail-safe receipt, not a
missing metric; (cl) marketplace id may lag the repo name.

## Batch #38 (2026-09-18 ~17:21 Boise) — Cua-S1 specialist form System One (source-only)

Note: `research/notes.md` §54. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. **Not TypeSafe Jev. Not GLiNER. Not a
general CUA. Not multimodal pixels-in.** No invented metrics. Do not
re-fold §52 gliner2-ultrafast as this product, §48 solari-reflex,
§53 jev-pruner, blackwood-rlcd as a screenshot cousin, or
laya-mind2web as a Laya DOM-index cousin.

- **trycua/cua `libs/cua-s1` (Empirical as README / MODEL_CARD
  behavior; weights Watch).** Parent MIT; ~23.3k★ this pass
  (updated 2026-09-18T23:21:08Z). Research family of small specialist
  computer-use models. Profile `cua-s1-form-v0`. Source-only: no
  weights, datasets, or checkpoint scores. `tinyx` byte encoder +
  option-attention: per observed element fill / check / click /
  skip. Fill values selected from extracted `Label: value` pairs,
  not generated. Code owns execution order. Plan ≠ execute; dry-run
  default; `execute`/`submit` opt-in; fail-closed unknown checkbox /
  fill without advertised token `set_value`. Tests exercise
  implementation, not checkpoint quality. Offline metric *names*
  only.
- **Mental models:** (1) specialist S1 vs general agent (narrow task
  contract; membership ≠ general CUA); (2) Choice among observed
  elements / fixed actions (same hole as jev-ultrafast /
  gliner2-ultrafast / solari / laya-mind2web; contrast blackwood
  screenshot); (3) plan ≠ execute, dry-run default, fail-closed
  envelope; (4) parallel "System One" naming, not TypeSafe Jev.
- **rh-guard:** light note only (dry-run / submit opt-in /
  fail-closed state). Not reward-hack detection.

Cross-repo addition: (cm) observe→score-among-candidates→code-acts
is backend-agnostic including a specialist CUA head; (cn) "System
One" in CUA research is a parallel name, not a TypeSafe contract;
(co) plan ≠ execute / dry-run is the sandwich around a soft
specialist; (cp) source-only drops publish metric *names*, not
checkpoint scores — Watch for `cua-s1-form-v0`.

## Batch #39 (2026-09-18 ~17:48 Boise) — CUDA replica, decision-native RAG, verbatim recall, Ruby primitive, FHIR Harbor, AMBIGUOUS baselines

Note: `research/notes.md` §55. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. X MCP flap; `since_id` not advanced.
Archive `234740` not present locally. No invented metrics. Do not
re-fold §50–§54. Student-b species already §33 — light delta only.

- **Mintzs/jevify (Empirical as README behavior).** Python. Created
  2026-09-18T23:41:21Z; 0★. CUDA/PyTorch parallel Choice/Score/Noul
  *shape* on Qwen2.5-1.5B (`ora_decision_engine` / `ora-decision`).
  CUDA graphs, branch kernels, literal-label scoring. Independent of
  Distillation. **Uncalibrated model likelihoods, not measured
  correctness.** Default refund workflow is not a validated policy.
  Default `--answer-encoding letters`. **No LICENSE file this pass.**
- **emergency-lee/decision-native-rag-skills (Empirical as
  architecture; Hypothesis as a measured win).** MIT. Created
  2026-09-18T23:29:20Z; 0★. Retrieve wide → decide → evidence set →
  conflict resolve → reason only over kept evidence. Provider-
  agnostic. No bundled Python harness. No universal benchmark.
  Offline replay → shadow → canary → A/B.
- **Dharundp6/jev-carryforward (Empirical as README behavior).** MIT,
  1★. npm `carryforward`. Verbatim JSONL ledger; Jev scores recall;
  constraints/corrections never judged; fail-open dump. 9×3 hint, not
  proof.
- **carldaws/hunch (Empirical as README / example suite).** MIT. Ruby
  `chance`/`pick`/`rate`; English-as-config; validations `rescue nil`
  fail-open at save. Stub backend. Cousin of probably-lang (library,
  not a new language).
- **si618/explore-typesafe-ai (Empirical as named report; not
  clinical validation).** Created 2026-09-18T23:48:44Z; 0★; license
  not in API. 100 synthetic Synthea; labels first; 60 requests / 403
  judgments to jev-1.13.0. Report: NEWS2 10/20 → 1/20 under-triage;
  98% of 143 med statuses; 7/20 inbox auto-dispatch all correct;
  p50 329 ms; $0.0038. Claude wrote labels. 20 cases/scenario.
- **ickma2311/jev-baselines-eval (Empirical as Harbor/jevals
  practice, including the honest negative).** MIT. Created
  2026-09-18T22:57:35Z. Pre-registered vs nano/frontier/encoder.
  **Both AMBIGUOUS.** CLINC150 Jev 0.870 vs nano 0.795 vs Terra
  0.915. Banking77 encoder **0.933 / 9 ms**. Cascade Δ +0.265 at
  1pp; **sign flips at exact parity** (R_jev=1.000) because
  confidence=1.0 on 102/200 incl. 6 wrong. AUROC neither direction;
  no ECE. Latency ~2.2× serving-path, not 40–200×. Errata ×3.
- **SargeDev/jev-gate-student-b (light delta).** HF card unchanged:
  MAE 0.187 / Pearson 0.791 / 90% n=60; ~59 ms; fail-open; teacher-
  copy.
- **MED:** fdemir/toolgate (MIT; allow/block/review; Jev not
  authorization; 72-case synthetic); masa-med-ai/typesafe-screening-mcp
  (MIT; 326 hits ~17s ~$0.014; screening aid); laurentfabre/
  databricks-jev-pdf-lab (honest negative; no OSS license);
  yannip1234/codex-jev (Apache-2.0; 185→44 estimated tokens
  integration demo; equal accuracy/lower cost not established);
  kazuhideoki/jev-search (file+fzf; **not** superagents-lab web
  search; no LICENSE).

Cross-repo addition: (cq) uncalibrated local likelihoods ≠ Noul;
(cr) retrieve-wide → decide → evidence set is the RAG sandwich;
(cs) verbatim ledger + scored recall, rules never judged; (ct)
judgment as a language primitive (English-as-config); (cu)
confidence=1.0 theater flips cascade sign at exact parity; (cv)
encoder-with-labels still wins; (cw) serving-path ≠ model-speed;
(cx) kazuhideoki/jev-search ≠ superagents-lab/jev-search; (cy)
toolgate product ≠ ndolinschi vocab; (cz) Precision PDF honest
negative is a result.

## Batch #40 (2026-09-19 ~00:38 UTC / ~18:38 Boise 2026-09-18) — classify-first MCP + living applied-mappings atlas

Note: `research/notes.md` §56. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. No invented metrics. Do not re-fold
§50–§55.

- **kbhuw/jev-sift (Empirical as README / schema; Hypothesis as a
  measured win).** JavaScript. Created 2026-09-18T00:13:31Z; 10★
  this pass; **no LICENSE file this pass.** Plugin
  `0.2.0+codex.20260918200547`; package 0.2.0; author Kush
  Bhuwalka. Classify first, read selectively: batch path / public
  URL / inline text → Jev relevance or 1–8 typed questions. Direct
  `POST /v1/systemone` `jev-latest`. Envelope (theirs): 50 items,
  60k char, 2 MB / 20 s, public-IP only, 3 redirects, no
  JS/cookies/login, PDFs unsupported. Uncertain/errors/truncation ≠
  irrelevant. Transport tests (mocks) ≠ accuracy. Same
  retrieve-wide → decide → evidence-set family as
  decision-native-rag-skills. Topology A MCP; not jev-routing
  (host adapter). Cousins: typesafe-screening-mcp,
  kazuhideoki/jev-search, jev-pruner, carryforward.
- **jevable.com (Empirical as public showcase; 342 is *their*
  count).** Independent curated atlas (Nikunj / `@nikunj` in
  JSON-LD). HTTP 200 Railway. Claimed **342**; JSON-LD first page
  **36**; `pageSize` 36. Categories: Agents, Browser extensions,
  Creative tools, Data & research, Developer tools, Experiments,
  Finance, Games, Marketing, Productivity, Robotics. No public API
  this pass. Class patterns, not a 342-title dump: (1) intent
  columns → jevpandas/jevframe / dabit3 formulas; (2)
  score-among-observed → jev-ultrafast / gliner2-ultrafast /
  solari / cua-s1 + Your Signal/Near Here (do not merge 7s/$0.0039
  with 12.20s; 100× is a claim); (3) VOI gates → tamara
  compaction / jev-pruner / gliner25 / routeKit / Gmail embeddings-
  first / jev-sift; (4) generative UI decide → json-render +
  jev-agentworld-web-simulator; (5) robotics text-state MuJoCo
  geometry-as-text / MOSS / jev-drone / Doom JSON (drawing-pixel
  claim ≠ Archer); (6) draft-gate silence-as-safer needs fail-open
  / heartbeat vs Abide `<0.5` (edit proceeds). Confirm-don't-
  invent: Higgsfield claim, jev-trader, Cambium, SEO 584/139
  `other`, snacks 3000/28s/$0.11 claim, ai-cli/hunch, Manhattan/
  Sudoku ≠ replace A*.

Cross-repo addition: (da) classify-first MCP is retrieve-wide →
decide → evidence-set on agent I/O; (db) errors/truncation ≠
irrelevant; (dc) topology A MCP ≠ host-adapter routing; (dd)
living atlas extracts class patterns, not a 342-row dump; (de)
draft-gate silence ≠ safer (heartbeat); (df) robotics text-state ≠
pixels; (dg) 342 is their count / JSON-LD 36 is page 1.

## Batch #41 (2026-09-19 ~00:48 UTC / ~18:48 Boise 2026-09-18) — Stagehand experimental Jev pick-and-copy

Note: `research/notes.md` §57. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. No invented metrics. Do not re-fold
§50–§56. Draft stack — Watch merge.

- **browserbase/stagehand #2951–#2955 (Empirical as PR-body
  architecture + their local eval).** Parent MIT. All OPEN draft.
  Author miguelg719. Created 2026-09-17T06:40Z. User link **#2955
  (5/5)**: extract completion **judge** + **pick-and-copy**. Jev
  picks a11y elements; code copies text. `extract` `"off"` |
  `"judge"` | `"pick"`. Both modes send page/extracted content to
  TypeSafe. Schema leftovers / screenshot extract / failed gate →
  LLM. Their card (gemini-3.8-flash, Browserbase, local, 25×3):
  69/75 vs 23/25 (92% both); **37/75** no-LLM ~0.5 s vs baseline
  **4.37 s** / two LLM calls; LLM-off **36/75** — pick is a fast
  path, not a replacement. Stack: #2951 editable ids (outline
  unchanged); #2952 client + pick (`best`+`strict`; ambiguity
  stops); #2953 act tree (LLM fallback); #2954 observe + cache-check
  (errors never block replay). Same observe→score-among-candidates→
  code-acts *job* as jev-ultrafast / gliner2-ultrafast / cua-s1 /
  solari, inside a major harness. Do not merge clocks.

Cross-repo addition: (dh) harness pick-and-copy is pointer-not-
generator at product scale; (di) pick is a fast path, not a
replacement (36/75 LLM-off honesty); (dj) cache-check errors fail
open (never block replay); (dk) best+strict is NOTA at pick time;
(dl) draft stack #2951–#2955 Watch merge.

## Batch #42 (2026-09-19 ~00:46 UTC / ~18:46 Boise 2026-09-18) — public wall, meaning-search, attention≠correctness, skills→oxlint, session-sticky route, measured RAG rerank

Note: `research/notes.md` §58. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. No invented metrics. Do not re-fold
§50–§57 (Stagehand is already §57).

- **waynesutton/ask-jev-ai (Empirical as README / live wall).**
  JavaScript. Created 2026-09-19T00:23:46Z; 0★; **license null.**
  Public realtime judgment wall; 6 parallel questions/ask; policy
  in `convex/questions.ts`; safety p≥0.6 blocked; no-key allowlist
  (UI says Jev offline). Cost $0.000032–$0.000041/ask from TypeSafe
  token counts → $32–$41/1M. Live askjev.ai. Productized System
  One primitive surface.
- **Bentlybro/jevgrep (Empirical as stripped-repo card).** Python
  MIT. Created 2026-09-19T00:09:47Z; 0★. Meaning-search CLI+MCP
  without embeddings. 228 questions on docstring-stripped
  Flask/httpx/Django/AutoGPT: **79% top-5** vs BM25 40% / grep 20%.
  Keyword still wins exact (BM25 top-10 96% vs 85%). Packed+parallel
  0.9 s vs serial ~23 min AutoGPT 4,329 files. Distinct from
  kazuhideoki / superagents-lab / jev-sift.
- **egma-ai/jev-reviewer (Empirical as README architecture).**
  JavaScript MIT. Created 2026-09-19T00:38:48Z; 0★. Jev assigns
  attention P0/P1/P2; OpenAI writes behavior deltas. Attention ≠
  correctness. **Not** choxos/jev-reviewer. Incomplete never P2.
  Demo: real Jev + labeled prepared explanation copy; live OpenAI
  pending funded API.
- **cephalization/jev-oxlint (Empirical as Phoenix experiment).**
  TypeScript. Created 2026-09-19T00:34:49Z; 0★; license null.
  Experiment; nothing published. AST/precheck prove; guidance
  whole-file in state; remainder judged; not a hard gate. Phoenix:
  answer-key agree on every fixture; flush-only-on-success noul
  0.07; routing 0.80–0.94 vs <0.50; coarse hint not. `tenbin` owns
  the lint skill.
- **jxu-dev-c/jev-adaptive-thinking (Empirical as README session
  machine).** Go. Created 2026-09-19T00:35:37Z; 0★; license null.
  Session-sticky first-prompt classification; later never
  reclassify; fail-closed lock to `gpt-5.6-sol`. Same family as
  routeKit. Live testing left to the deployer.
- **Max-sm-yc/Jev-RAG (Empirical as one-run).** Python. Created
  2026-09-19T00:33:02Z; 0★; license null. ≥70% cost / 72% latency
  vs Muse Spark *rerank*; full-context Spark still 10.60 s. Costs
  include embeddings.
- MED: EpicEric/safe-sh (AGPL-3.0; static shell analysis);
  ravikadam/jev-loan-triage (17 questions; policy in code);
  TurboGuo/jev-fedspeech + jev-dating (Jev vs chat arenas; prior
  empty search was a query miss); g-h-miles/jevbox (MIT; drums).
  hermes/mcp packs: **no new pack this pass.**

Cross-repo addition: (dm) productized public primitive surface
(six parallel questions; policy-in-code; cost-to-1M from tokens);
(dn) meaning-search without embeddings (packed parallel; keyword
still wins exact strings); (do) attention ≠ correctness on a PR
(anti-soundness-theater; not choxos pointer); (dp) skills→oxlint
AST prove ∩ remainder without hard-gating; (dq) session-sticky
first-prompt route fail-closed to a declared fallback; (dr)
measured RAG rerank vs generative rerank must keep the no-RAG
latency arm visible.

## Batch #43 (2026-09-19 ~01:48 UTC / ~19:48 Boise 2026-09-18) — capability kernel, typed DSPy control plane, calibration arena + fan-out suite, engine-owns-truth, human-confirmed port cleanup

Note: `research/notes.md` §59. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. No invented metrics. Do not re-fold
§50–§58. Skip SPFreedom/jef-mcp (parody) and rayelzz/jevregist
(account farming).

- **somoore/interlock (Empirical as README architecture).** Python
  MIT. Created 2026-09-19T01:41:58Z; 0★. Capability kernel: LLM
  ring 3 / Interlock ring 0. Secrets never in the agent. Closed
  action space. Jev SENSOR; `policy.py` BLOCK/ASK/ALLOW. Type-safe
  ≠ correct. Distinct from toolgate. 38-case local-judge set, not
  a blind paper.
- **manikanda-kumar/jev-dspy-control-plane (Empirical as README
  architecture + metric list).** Python MIT. Created
  2026-09-19T01:36:58Z; 0★. DSPy drafts AFTER route+action. OpenJEV
  / DSPy / JSON Schema share ontology. Offline heuristic ≠ quality.
- **meetr1912/jev-arena (Empirical as their live card).** Python
  MIT. Created 2026-09-19T01:28:11Z; 0★. 145 noul, Brier 0.0059,
  ECE 0.0620, 2 requests / 710 ms; overconfident in low bins.
  Siblings: jev-sonar (heatmap-as-policy), jev-vickrey (Jev never
  bids), jev-bracket (live Brier 0.2853 vs Elo 0.2322 — trailed
  Elo; honest).
- **JoelLewis/game-coach (Empirical as PRD; Hypothesis as shipped
  product).** TypeScript GPL-3.0. Created 2026-09-19T01:08:53Z;
  0★. Wave 0. Stockfish owns truth; Jev owns judgment.
- **epiphany-dynamics/port-cleanup (Empirical as README safety
  model).** Swift MIT. Created 2026-09-19T00:58:50Z; 0★. Human is
  the only kill trigger; identity re-check; shields; mapped
  explanations.
- MED: jev-pr-labeler, jevcumber, typedecide (not on npm), jevon,
  dsh-jev (not on npm), fast-jev-compaction-pi, jev-tetris-benchmark
  (not a rigorous eval), modelsystem (1★), opencode-system-one
  (license null; 1★), browser-ai (design done), semantic-bookmark.
  Star spike: SemIf 1607★ this pass; jevlike 897★.

Cross-repo addition: (ds) capability kernel vs post-decision
firewall (secrets never in agent; Jev SENSOR; type-safe ≠
correct); (dt) typed control plane around DSPy, not more LM knobs;
(du) native-probability calibration + fan-out as measurement
economics; (dv) engine owns truth / Jev owns judgment (anti-
soundness-theater with attention≠correctness); (dw) human-
confirmed kill + mapped explanations + identity re-check.

## Batch #44 (2026-09-19 ~02:43 UTC / ~20:43 Boise 2026-09-18) — domain specialist vs few-shot hosted, decide→policy leftover cascade, ORDER BY calibration≠sortable, GLiFormer wire-compat backend

Note: `research/notes.md` §60. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. No invented metrics. Do not re-fold
§50–§59.

- **help-er/Domain-jev-maker (Empirical as their RESULTS.md).**
  Python MIT. Created 2026-09-19T02:17:54Z; 0★. Independent
  CLINC gold, not a Jev teacher-copy. KL 0.168 vs 0.580
  banking; few-shot determinate McNemar n.s. Train specialist
  when policy reads p.
- **skiingfalcon/jav-email-cascade (Empirical as README
  architecture).** Python; license null. Created
  2026-09-19T02:28:24Z; 0★. Decide→policy→LLM leftover. Noul
  0.5 never rounded. Mock gen-json flat-confidence is *their
  mock*. Distinct from dual-process-ai.
- **yodablocks/jev-orderby-bench (Empirical as independent
  measurement).** Python MIT. Created 2026-09-19T01:31:53Z;
  0★. Six gates pass. Score ordinal 0.143 weak link; 53-way
  0.99 tie; recodelabs batch-40 fails ranking. Calibration ≠
  sortable.
- **logan-markewich/jeff (Empirical as their RESULTS.md).**
  Python; license null. Created 2026-09-19T02:17:25Z; 0★.
  GLiFormer-400M `/v1/systemone`. ~6× L4 HTTP / ~24× A10G
  direct; AG News 75.5% vs 90.5%. Not a Jev replica.
- MED: hraness/sysone (MIT, TypeScript; loopback gateway; no
  weights).

Cross-repo addition: (dx) specialist vs few-shot as a function
of whether downstream reads p; (dy) Harbor-shaped
decide/policy/LLM leftover with native vs verbalized vs
logprob arms; (dz) ranking family vs calibration family
(ORDER BY; request shape); (ea) wire-compat encoder backend
as a product economics decision, not a quality clone.

## Batch #45 (2026-09-19 ~03:39 UTC / ~21:39 Boise 2026-09-18) — active-learning triage / don't distill Jev as teacher, evidence-packet explorer, meaning-grep, closed-vote CU, Jev vs MLX PCD Harbor, host-owned waymode, OMP/pi fail-open gates

Note: `research/notes.md` §61. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. No invented metrics. Do not re-fold
§50–§60. Skip empty jev-compactor / laya-jolt.

- **ThyFriendlyFox/jev-triage (Empirical as README architecture).**
  Python MIT. Created 2026-09-19T03:37:23Z; 0★. Accept / teacher /
  human. Log full distributions. Do not distill Jev as teacher
  (~68% ceiling). Real outcomes stay the targets.
- **jimmyhealer/jev-semantic-explorer (Empirical as their
  performance.md, author-run).** Python MIT. Created
  2026-09-19T03:21:01Z; 0★. jevex. 1/8→6/8 SWE-bench Verified
  finish n=8 (empty = miss). Packet HitFile 0.233 vs BM25 0.159
  diagnostic, not product KPI.
- **uehaj/jev-semgrep (Empirical as README + judge test).**
  JavaScript; LICENSE MIT (GitHub NOASSERTION). Created
  2026-09-19T03:18:28Z; 0★ then. AND/OR/NOT line Nouls; JP↔EN.
  Precision 0.94 / recall 0.98 *theirs*. Dedicated fold §86.
- **buluoray/JevOnly (Empirical as README architecture).** Python
  Apache-2.0. Created 2026-09-19T03:24:36Z; 0★. Closed-vote; no
  planner LLM. 11/43/~$0.014/17s *theirs*.
- **mallahyari/system-one-benchmark (Empirical as their n=50
  table).** Python; license null. Created 2026-09-19T03:35:00Z;
  0★. Jev 84.0% / Brier 0.1096 vs PCD 52% / 0.3884. O(1) ≠ Noul.
- **mossburgh/waymode (Empirical as README + eval suite).**
  TypeScript MIT. Created 2026-09-19T02:43:12Z; 0★. Host-owned
  handlers. 24/26 + 34/36 *theirs*. Not a self-driving proof.
- **luw2007/omp-jev-extensions (Empirical as README fail
  polarity).** TypeScript MIT. Created 2026-09-19T02:55:18Z; 0★.
  Fail-open acceptance + route (`confidence: 0`). Contrast
  pi-jev-approver fail-closed.

Cross-repo addition: (eb) training-data VOI / don't distill Jev
as teacher of record; (ec) index-once evidence packets vs grep;
(ed) line meaning-grep AND/OR/NOT; (ee) closed-vote CU with no
planner LLM vs host-owned product surface; (ef) Harbor Jev vs
PCD: O(1) speed ≠ calibrated Noul; (eg) OMP/pi fail-open vs
fail-closed remainder gates.

## Batch #46 (2026-09-19 ~04:38 UTC / ~22:38 Boise 2026-09-18) — permission vs probability (greenlight), judgment ≠ permission (skill-broker outline), eval integrity / instrument-not-score (dinostomp)

Note: `research/notes.md` §62. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. No invented metrics. Do not re-fold
§50–§61. Watch archive `/workspace/jev-archive/2026-09-18/223856`
absent this VM; live GitHub receipts. Do not treat skill-broker as
a production recipe.

- **SemetricLabs/omp-greenlight (Empirical as measured traffic +
  labelled corpus).** Python MIT. Created 2026-09-19T04:06:43Z; 0★.
  1,013 calls / 10 sessions. Default 40.9% prompts removed; 0 of 94
  unsafe auto-approvals on 140-row corpus. Operator owns thresholds;
  plugin never self-tunes. Not a sandbox.
- **adamjralph/skill-broker (Hypothesis / outline only).** Language
  null; license null. Created 2026-09-19T04:35:59Z; 0★.
  PROJECT-OUTLINE.md authoritative. Code owns grants; Jev never
  grants access. Not a production recipe.
- **collapseindex/dinostomp (Empirical as FINDINGS.md + demo card).**
  Python; README Apache-2.0 / GitHub NOASSERTION. Created
  2026-08-09T07:59:32Z; 5★. Checks the instrument, not just the
  score. 189 findings / 99 against itself. `dinostomp jev` 24-example
  demo ECE 0.062 *theirs*. Beside jevals, not a Harbor taskset.
- MED: nrdz-labs/fast-jev-opencode (MIT TS; fail-open OpenCode V2
  port); yikangy873-gif/jev-desktop; MrDiamondBallz/jev-agent-integration;
  bohutang/sift; CorieW/JevExplore.

Census: Awesomejev 488/21644; SemIf 1641 (+13); jevlike 905 (+4);
tracker likes 41 (+1); lastModified unchanged; Laya yes; Blackwood
ABSENT; X MCP flapping (`pages_archived` 0).

Cross-repo addition: (eh) permission vs probability / operator-owned
safety bar; (ei) judgment ≠ permission (Jev never grants access);
(ej) eval integrity / instrument-not-score (`dinostomp jev` as
if-statement hygiene).

## Batch #47 (2026-09-19 ~05:40 UTC / ~23:40 Boise 2026-09-18) — constrained optimizer + S1 features (slo-router), privilege ≠ verdict (construct-auto-classifier), attention/VOI never-block (jev-lens)

Note: `research/notes.md` §63. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. No invented metrics. Do not re-fold
§50–§62. Watch archive `/workspace/jev-archive/2026-09-18/234027`
absent this VM; live GitHub + HF receipts. Hunches labeled. Do not
treat the eight-row slo-router demo as a benchmark. Do not treat
swift-jev LICENSE-only as a CLI product. Do not merge
sysone-help/sysone with hraness/sysone.

- **zeeshan8281/slo-router (Empirical as live analysis *shape* /
  negative for sync Jev).** Python; license null. Created
  2026-09-19T05:32:45Z; 0★. Jev features, constrained controller.
  Same routes/accuracy; p95 77.93→490.38 ms *theirs*. Fail-open
  local features. Exactness raises floor, never overrides
  capability.
- **godspede/construct-auto-classifier (Empirical as
  certification).** TypeScript Apache-2.0. Created
  2026-09-18T22:27:03Z; 0★. Effect-based shell gate. Jev 0
  dangerous / 975; every chat model leaked 16–104. Privilege ≠
  verdict. Fail-closed. Operator-owned dials.
- **rashedInt32/jev-lens + jev-lens.nvim (Empirical as README
  architecture).** JS MIT created 2026-09-19T04:46:01Z; Lua MIT
  created 2026-09-19T04:47:11Z; 0★. Never blocks; never edits;
  never green unless sure. Attention filter / VOI, not a
  permission gate.
- MED: sysone-help/sysone (MIT TS; evaluation-model-first SDK;
  not hraness/sysone); ctaxnagomi/INSTRUCT_JEV (HF MIT; 119 rows
  47/51/21; jevals seed); ckaik/swift-jev (MIT; LICENSE-only).

Census: Awesomejev 488/21644; SemIf 1652 (+11); tracker likes
42 (+1); lastModified unchanged; Laya yes; Blackwood ABSENT;
X MCP flapping.

Cross-repo addition: (ek) constrained optimizer + S1 features /
never sole hot-path gate (Harbor-style latency cost); (el)
privilege ≠ verdict / effect contracts not tokens; (em)
attention filter / VOI for human review / never blocks / never
green unless sure.

## Batch #48 (2026-09-19 ~06:39 UTC / ~00:39 Boise) — measurement owns endorsement (jev-packs), Jev supplies evidence / code owns authority (actiongate-jev), ranking ≠ calibration (does-jev-confidence)

Note: `research/notes.md` §64. Docs-only. Folded into PR #2. Not a
second PR. Archer still Watch. No invented metrics. Do not re-fold
§50–§63. Watch archive `/workspace/jev-archive/2026-09-19/0039`
absent this VM; live GitHub receipts. Hunches labeled. Do not treat
jevassert as a shipped product (404). Do not re-fold
sysone-help/sysone. Do not cite `threat` (n=1). Do not merge
gqgs/laya-onnx with Mattepiu/laya-onnx or local-jev with
us/jev-local.

- **dtduc-git/jev-packs (Empirical as registry tables /
  Harbor-jevals practice).** Python CC0-1.0. Created
  2026-09-19T06:35:36Z; 0★; GitHub size 0. Evidence-gated
  `pack.yaml` + `cases.jsonl` + `evidence.md`. Nine packs
  `verified` *theirs* on pinned `jev-1.13.0` (citation-support
  800 / 0.919 / 0.022 through banking-intent 150 / 0.840 /
  0.090). `unknown` mandatory. Named runner jevassert **not
  released** (404). Measurement owns endorsement.
- **omkarghugarkar007/actiongate-jev (Empirical as README
  slogan).** TypeScript Apache-2.0. Created
  2026-09-19T06:20:33Z; 0★; size 0. Deterministic policy owns
  ALLOW|REVIEW|BLOCK; Jev is semantic evidence only. Slogan:
  "Jev supplies evidence. Code owns authority." Positive
  score never overrides a hard fail. Fail-closed
  financial/destructive/credential if Jev is down. 500-case
  is label-baseline, not accuracy.
- **Adilmp/does-jev-confidence-mean-anything + jevcal
  (Empirical as 8,000-judgment audit).** Python; license
  null / MIT. Created 2026-09-19T04:51:58Z / 05:44:21Z; 0★ /
  1★. AUC ~0.91; stated ~75% vs human ~10%; ~96% ECE
  removed without rank change. Vendor "calibrated" =
  rank-correlation, not frequency units. jevcal ~100 labelled
  rows. One domain (`civil_comments`).
- MED: gqgs/laya-onnx (complete Laya→browser int8; conversion
  smoke; distinct from Mattepiu); kunchenguid/local-jev
  (ModernBERT approximation — not equivalence; distinct from
  jev-local stub and jeff).

Census: Awesomejev 488/21644; SemIf **1660** (+8); jevlike
**910** (+5); TypeAR 9; tracker likes 42; lastModified
unchanged; Laya yes; Blackwood ABSENT; X MCP flapping.

Cross-repo addition: (en) measurement owns endorsement /
evidence-gated question packs; (eo) Jev supplies evidence /
code owns authority (positive p never overrides a
deterministic security failure); (ep) ranking ≠ calibration
/ never hard-threshold raw p as a frequency.

## Batch #49 (2026-09-19 ~06:50 UTC / ~00:39 Boise remainder) — hot-click CU (ego-jev), Jev judges relevance / code decides structure (jev-compactor), local-rules-then-remainder + anti-self-train (x-reply-filter)

Note: `research/notes.md` §65. Same hour as §64. Docs-only.
Folded into PR #2. Archer still Watch. No invented metrics. Do
not re-fold actiongate / jev-packs / sysone-help. jev-compactor
was empty skip in §61; content landed. Hunches labeled.

- **jiangkoumo/ego-jev (Empirical as n=3 medians / README
  architecture).** JavaScript MIT. Created
  2026-09-19T06:33:03Z; 0★. Indexed viewport table →
  operation+target. Code owns observe/execute/`--until`.
  Text model only for type. HN 4.9 s vs 9.7 s; wiki 5.4 s vs
  10.1 s *theirs*. High variance. Not a benchmark.
- **edwardyen724-g/jev-compactor (Empirical as one-session
  bench).** TypeScript MIT. Created 2026-09-19T03:31:54Z;
  1★. Was empty skip. Jev judges relevance; code decides
  structure; never rewrite. 64.5% / 366 ms / $0.0004 / 0
  hallucinated / 4 of 4 vs Sonnet 96.2% / 1 invented path.
  Dual fail polarity. Regex floor independent of Jev.
- **zhuyansen/x-reply-filter (Empirical as README + small
  e2e).** JavaScript MIT. Created 2026-09-19T06:07:18Z; 0★.
  Local rules first; remainder Nouls; never auto-train on
  the model's own hides. 3-sample e2e 0.90/0.93 vs 0.08/0.10.

Census: same as batch #48 (Awesomejev 488/21644; SemIf 1660;
jevlike 910; tracker likes 42).

Cross-repo addition: (eq) hot-click CU / indexed element
table / S1 on click path; (er) Jev judges relevance, code
decides structure / never rewrite; (es) local rules first
then remainder / never auto-train on the model's own hides.

## Batch #50 (2026-09-19 ~07:53 UTC / ~01:47 Boise) — control-plane combinators, receipts-not-leaderboard, skill VOI, OOD/AUC≠ECE, frontier-100, turnstile, jevmlx

Note: `research/notes.md` §66. Docs-only. Folded into PR #2.
Archer still Watch. No invented metrics. Atlas axis already
§49; skillranker existence already §7 (hook polarity
**corrected** to fail-open); jevmlx reconstruction already
§1. Hunches labeled.

- **voidning/decision-combinators (Empirical as README
  architecture).** TypeScript. README MIT / GitHub license
  null. Created 2026-09-19T07:25:16Z; 0★. Then / Gate /
  Vote / Cascade / Weighted. Not literal AND/OR. No
  measurements.
- **Zaious/jev-capability-atlas (delta: eval-integrity
  cluster).** 10★ this pass (was 0). Receipts not
  leaderboard; type-safe ≠ correct. Do not rehash history
  suite.
- **Dicklesworthstone/skillranker (Empirical as README;
  correction).** Rust; 52★. Two-pass + none-of-these.
  Claude hook fail-open (quiet exit 0). VOI over skill
  library.
- **scienthoon/jev-ood-calibration (Empirical as 900-ticket
  + 3 public benches).** MIT. Created 2026-09-19T07:33:22Z.
  Synthetic ECE 0.107 = 4.4× floor; priority 44.7% / mean p
  0.74 / T 3.40; boolean T 0.66. AUC ≠ ECE.
- **softpudding/jev-frontier-100 (Empirical as exploratory
  100×3).** MIT. Jev 77.0%; Qwen3.5 4B/2048 96.7%; 4B off
  56.0%. Not preregistered. Not a ceiling.
- **zyphr-labs/turnstile (Empirical as README
  architecture).** Apache-2.0. Experimental alpha. Policy
  first; Jev remainder; replay. Missing Jev → Review.
  Actiongate-class.
- **bnsd55/jevmlx (Empirical as README library).** MIT;
  28★. One-pass schema→JSON+probs. Softmax ≠ Noul. No
  local leaderboard yet.
- MED: chopratejas/invalidate (5★; 0 of 157 false
  invalidations); yottayoshida/jev-intent-review (under
  construction); shubhangi013/prune-review (22-run cost
  1.18% with 305% outlier).

Census: not re-derived this hour (last §64/§65: Awesomejev
488/21644; SemIf 1660; jevlike 910; tracker likes 42).

Cross-repo addition: (et) combinators / System One as
control plane; (eu) receipts not leaderboard / type-safe ≠
correct jaggedness; (ev) skill-library VOI / abstention;
(ew) OOD / AUC ≠ ECE / sign by type; (ex) thinking-budget
bake-off; (ey) turnstile evidence≠authority + replay;
(ez) MLX one-pass replica economics.


## Batch #51 (2026-09-19 ~08:45 UTC / ~02:38 Boise) — TLA+ compose, SEAL coverage ledger, skill-broker sibling, sureness, JevBench v1.1, CI typed gate, Codex MCP

Note: `research/notes.md` §67. Docs-only. Folded into PR #2.
Archer still Watch. No invented metrics. Do not re-fold §66
HIGH except sibling contrast. skill-broker outline already
§62. Hunches labeled.

- **copyleftdev/jev-labs (Empirical as TLA+ + 1,080 golden
  chaos table).** Python MIT. Created 2026-09-19T08:07:12Z;
  0★. Never confidently wrong. 0 wrong golden; severe 46
  escalate. TLC 1,049,750 / 0 errors. Synthetic, not
  clinical.
- **Reasonofmoon/seal (Empirical as README + BEYOND-JEV.md).**
  Python MIT. Created 2026-09-19T08:10:05Z; 0★. No seal, no
  advance. coverage.path auto|code|human|escalate. Mint ≠
  product brain.
- **adamjralph/skill-broker (delta: sibling table).** Still
  outline; README restates grants-in-code. Contrast
  turnstile / skillranker.
- **adarc8/how-sure-is-jev (Empirical as 60-q library).**
  Python MIT. Choice confidence = max_prob. Most generous
  metric.
- **fstandhartinger/jevbench (Empirical as v1.1 artifact).**
  Python MIT. Unofficial. Main Score 0.6/0.2/0.2. Jev
  1.13.0 87.6. Calibration not scored.
- **NemanjaManic/ci-gatekeeper-bot-jev (Empirical as
  own-repo latencies).** package.json MIT / GitHub SPDX
  null. 504–629 ms. Conservative default.
- **teempai/jev-in-codex (Empirical as README).** TypeScript
  MIT. Codex MCP. Ranking unbenchmarked. Lexical fallback.

Census this hour (user-provided): Awesomejev 488/21644;
SemIf 1683 (+11); jevlike 923 (+5); tracker likes 43 (+1).
Archer still NOT landed. X MCP flap continues.

Cross-repo addition: (fa) never confidently wrong / TLA+
compose; (fb) no seal no advance / coverage ledger;
(fc) sureness / max_prob is generous; (fd) JevBench
calibration not in Main Score; (fe) CI typed gate before
expensive review; (ff) Codex MCP host adapter.

## Batch #52 (2026-09-19 ~09:55 UTC / ~03:38 Boise) — attention redirect, pre-send views, tools≠use, observational memory, open-Jev class, physical-world S1

Note: `research/notes.md` §68. Docs-only. Folded into PR #2.
Archer still Watch. No invented metrics. Do not re-fold §67
HIGH except sibling contrast. Hunches labeled.

- **muse0509/jev-preflight (Empirical as owner-run hook
  smoke).** Go MIT. Created 2026-09-18T13:54:37Z; 1★;
  v0.1.0 Public Beta. Eight risk axes; assist=one
  reinspect; fail-open; 0.85 uncalibrated. Claude Code
  2.1.267: no-key fail-open PASS; key-enabled exactly one
  continuation. Not a merge blocker.
- **godspede/construct-auto-classifier (delta).** Cert
  unchanged: Jev 0 dangerous / 975; $0.047/1k. Landed-
  script trust; headless ≠ auto-approve.
- **edwardyen724-g/jev-compactor (Empirical as product-arm
  table).** Later bench 73% / 350 ms / 4 of 4 *theirs*.
  30–250× cheaper. §65 64.5% is vs-Sonnet.
- **dizk/jev-lens (Empirical as 500-trajectory).**
  TypeScript MIT. Created 2026-09-18T08:16:12Z; 0★. 79%
  fewer tokens (11.6M→2.4M). Post-send prune +17% cost.
  Distinct from rashedInt32/jev-lens.
- **Dharundp6/jev-carryforward (delta).** recall 0/4.
  tools≠use. SessionStart > hoping.
- **willfish/pi-observational-memory-jev (Empirical as
  README).** TypeScript MIT. Created 2026-09-18T06:42:35Z;
  0★. Keep/kind verbatim; model-free compact.
- **genai-craft/openvons (Empirical as their docs).**
  Python Apache-2.0 LICENSE / GitHub SPDX NOASSERTION; 7★.
  Independent open-Jev class. JevPick 3.2–4.8×. Wire-compat
  ≠ replica.
- **AboveColin/HA-Jev (Empirical as README + measurements).**
  Python MIT; 17★. First real card. Not for locks/heaters.
- **kylemclaren/jevql (architecture note).** Judgment
  outside the store. CLI; DB never sees jev().
- **bohutang/sift (short bullet).** ~$0.00003/post.

Census this hour (user-provided): Awesomejev 488→561
(+73, agent tooling 87→107); SemIf 1683→1704. Archer
still NOT landed.

Cross-repo addition: (fg) attention redirect not merge
blocker; (fh) compress-before-first-send; (fi) tools≠use
/ SessionStart; (fj) observational keep/kind; (fk)
open-Jev class / wire-compat ≠ replica; (fl) physical-
world S1 / not for locks; (fm) judgment outside the store;
(fn) landed-script / headless≠auto-approve.

## Batch #53 (2026-09-19 ~10:55 UTC / ~04:39 Boise) — digital-design combinators, VOI cache, skill-routing Harbor, zeroshot displacement, typed handoff

Note: `research/notes.md` §69. Docs-only. Folded into PR #2.
Archer still Watch. No invented metrics. Do not re-fold §68
HIGH except sibling contrast / combinators rename. Hunches
labeled.

- **voidning/jev-combinators (delta: rename + extended five).**
  Same repo as decision-combinators (§66). Package MIT /
  GitHub SPDX null. Router / Loop / Retry / Fallback /
  Memory. Digital-design metaphor ≠ literal AND/OR. No
  measurements.
- **kushals256/jevcache (Empirical as n=100 live eval).**
  TypeScript MIT. Created 2026-09-19T09:40:18Z; 0★. Jev
  0 FP / precision 1 / recall 0.38 / fpr 0 vs Jaccard@0.35
  fpr 0.48; $0.00174 *theirs*. Fail-open.
- **iamdin/pi-jev-skill-bench + pi-jev-skill-suggestion
  (Empirical as README harness; no live Jev numbers).**
  TypeScript MIT. 43 gold; roster 50–500. No-key no-op.
- **zhuyansen/jev-zeroshot-vs-bert (Empirical as 7-set
  table).** Python MIT. +0.05–+0.13 vs DeBERTa-c;
  contamination 0.901 vs `-c` 0.763; ≈230 / >2048 labels;
  DiD 0.035 vs 0.112 *theirs*.
- **shitianfang/jev-handoff (Empirical as README + 40 tests).**
  TypeScript MIT. Alpha v0.1. Gate never grants. Fail-open.
  Vercel drops confidence.
- **ThinkyMiner/Winnow (Empirical as unreviewed goldens).**
  TypeScript MIT. 80%/90% *theirs*. Distinct from
  kevinpita/winnow.
- **rsdkrasen/hermes-jev-router (Empirical as README +
  offline pytest).** Python; license null. WHETHER/HOW/WHAT.
  Community plugin, not vendor.
- **mleyvaz/jev-typed-evaluation-collapse (Empirical as
  NCML field note v0.3).** License null. Noul collapse vs
  named Choice p=1.0 vs binary red 0.67–0.85 *theirs*.
- **DowLucas/browser-jev (Empirical as README).** TypeScript;
  license null. Sample-from-distribution. Playwright
  executes, Jev chooses.
- **IamBusy/OpenJev (Empirical as RESULTS.md).** Apache-2.0.
  45/60 vs v0.2 39/60. `/v1/decide` ≠ TypeSafe drop-in.
  Distinct from hraness/sysone runners.
- **dddanielliu/semif-serve (Empirical as latency table).**
  pyproject MIT / GitHub SPDX null. 1164 vs 178 ms *theirs*.
  Wire-compat ≠ replica.
- Toolbelt notes: win4r/jev-security-scan (MIT; not a cert);
  bojansandhaus/jev-decisions (MIT; 1★; advice never stops
  commands); TeoMastro (license null; summary.md 404).
  rh-guard owns reward-hack.
- **ctaxnagomi/DGUI_HYPERMEM-JEV (feedstock schema).** HF MIT;
  6 rows. Sibling INSTRUCT_JEV.

Census this hour (user-provided): Awesomejev flat 561/27007;
tracker likes 43→45; SemIf 1714 (+10); jevlike 926 (+3).
Archer still NOT landed.

Cross-repo addition: (fo) digital-design combinators /
extended five; (fp) VOI cache admission / 0 FP; (fq)
Harbor skill-routing roster-size; (fr) zeroshot vs BERT
displacement / contamination DiD; (fs) typed baton never
grants / inverted loop; (ft) worth-your-attention VOI /
qualify Winnow owner; (fu) WHETHER/HOW/WHAT; (fv) conflict
≠ ignorance / named Choice escape; (fw) Playwright
executes Jev chooses; (fx) OpenJev `/v1/decide` ≠ drop-in;
(fy) SemIf runoff wire; (fz) decision-as-memory flywheel.

## Batch #54 (2026-09-19 ~11:55 UTC / ~05:46 Boise) — record/replay CI, BBQ, decider≠executor, sentence-as-rule lint, open replica substrates

Note: `research/notes.md` §70. Docs-only. Folded into PR #2.
Archer still Watch. No invented metrics. Do not re-fold
§50–§69 HIGH except sibling contrast / jevassert landing /
prune-review, intent-review, laya-jolt, local-jev deltas.
Hunches labeled. Meanblock/JEV-CPU **404**.

- **dtduc-git/jevassert (Empirical as README + Action @v0).**
  Python Apache-2.0. Created 2026-09-19T06:48:15Z; 0★; size
  64. **LANDED** (was 404 §64). Record/replay CI:
  accuracy/ECE/Brier/cost/latency offline from recordings.
  Exit 0/1/2. McNemar. Backend-neutral.
- **dtduc-git/jev-packs (delta: runner pairing + 2,990
  matrix).** CC0-1.0; size 0→458. Jev/Sonnet 5 accuracy
  tie Δ≤0.018; Jev better calibrated 7/9; ~250× cheaper
  *theirs*. sms-spam this-pass 0.953 / ECE 0.040.
- **chenmingtang830/jevarena (Empirical as runnable
  harness; not findings).** TypeScript Apache-2.0; size
  724. Failure-finding not a leaderboard. **≠**
  meetr1912/jev-arena. Always qualify owner.
- **simonmesmith/jev-bbq-experiment (Empirical as full
  58,492).** R; license null; size 5365. 97.28%; bias
  0.04/0.34; $0.3429 / 7.75 min *theirs*. Not a general
  bias cert.
- **thomasbrueggemann/jeffrey (Empirical as README).**
  TypeScript MIT; size 71. Decider ≠ executor. Pick ≠
  fill. Risk≥0.5 pause. Stuck ladder 2 Jev / 0 steps.
- **mizchi/jevlint (Empirical as 13/15 corpus).**
  TypeScript MIT; size 338. ast-grep × `ask:`. 13/15
  1.00/1.00 *theirs*. **≠** huntedman/JevLint. Always
  qualify owner.
- **shubhangi013/prune-review (delta: size/star).**
  22-run numbers unchanged 1.18% with 305% outlier
  *theirs*. ~20% cost target. Cost not quality.
- **yottayoshida/jev-intent-review (delta: CLI).** Dual
  MIT/Apache-2.0; size 81. VERIFIED/VIOLATION/UNKNOWN.
  Empty search ≠ proof. Action not written.
- **Eran-BA/Jev_from_GLiNER2 (spec-only).** Size 0.
  Interface ≠ replica. Distinct from jeff GLiFormer.
- **bokuweb/grande (Empirical as JGLUE + isolation).**
  Rust; license null; 1★; size 583. JNLI 0.614 ECE
  0.088 T=2.81; JCQA 0.853; 270M 0.710/0.710 *theirs*.
  Softmax ≠ Noul until T.
- **jlt-commons/laya-jolt (delta: content landed).**
  Clojure Apache-2.0; size 5112. Byte parity vs Python
  system_one. ~1e-7 last-digit drift.
- **leesk212/JEV-CPU (Empirical as PoC).** Python MIT;
  1★. SemIf CPU + UI. Meanblock/JEV-CPU 404.
- **kunchenguid/local-jev (delta: measured).** 136
  checkpoints *theirs*: done 30% / shape 57% / r −0.06.
  Not equivalence.
- Toolbelt notes: actiongate-jev slogan already §64.
  **Nyarlathoteppppp/pi-heed (Empirical as 79-session
  bench).** TypeScript MIT; 3★; size 621. Recall 98.5%
  / false block 0.0% / $0.000058 *theirs*. Jev never
  writes policy.
- MED: david-j-lustig/system-one-responsible-ai size 0
  framing stub.

Census not re-derived this hour (last §69). Archer still
NOT landed.

Cross-repo addition: (ga) record/replay CI / calibration+
cost first-class; (gb) evidence-gated packs have a
runner / 2,990 matrix; (gc) failure-finding arena ≠
leaderboard / qualify jevarena owner; (gd) BBQ
stereotype/uncertainty/cost not a bias cert; (ge)
decider≠executor / pick ≠ fill; (gf) sentence-as-rule
lint / qualify jevlint owner; (gg) VOI hunk prune /
safety escarpment; (gh) whole-repo intent UNKNOWN;
(gi) GLiNER2 spec ≠ replica; (gj) open replica
substrates (grande / laya-jolt / JEV-CPU / local-jev);
(gk) persist constraints across compaction.

## Batch #55 (2026-09-19 ~12:50 UTC / ~06:43 Boise) — SGR-judge Harbor contract, control-plane productization, never-generates, recipes+life feed, NAR claim-audit

Note: `research/notes.md` §71. Docs-only. Folded into PR #2.
Archer still Watch. No invented metrics. Do not re-fold
§50–§70 HIGH except sibling contrast. Hunches labeled.
IPECTER/jev-context-pruner **empty**.

- **slavadubrov/jev-judge-bench (Empirical as frozen
  contract; not a quality score).** Python; README MIT /
  GitHub SPDX NOASSERTION. Created 2026-09-19T12:20:43Z;
  0★; size 0 lag. SLA-150. Invalid = FN. 21 offline tests.
  Canaries ≠ quality. **No headline yet.** ≠ jevarena /
  jevbench. Always qualify owner.
- **IPECTER/jev-context-pruner (empty skip).** Description
  only; contents 409 empty. Sibling contrast vs
  fast-jev-compaction / jev-compactor / dizk/jev-lens.
- **shitianfang/jev-use (Empirical as 95-call card).**
  TypeScript MIT v0.4.1; size 196. p50 220 ms; 186 vs
  2,672 ms; gate 12/12; Vercel margin 0.4; 17/20 then
  0/20 *theirs*. Fail-open. ≠ jev-ultrafast. Same author
  as jev-handoff.
- **goodruizhan/pi-jev-control (Empirical as README).**
  TypeScript; license null; v0.3.0 private. Control plane.
  GUI never force-click; compaction never writes session.
  No live quality numbers.
- **florian-hoenicke/jev-gpt (Empirical as README demo).**
  Python; license null. Never free-generates. ~400 calls /
  75 s / 2¢ *theirs*. Distinct from jeffrey.
- **nexibeo/jev-cookbook (Empirical as recipe samples, not
  benches).** JavaScript MIT; 1★; size 165. 425 calls /
  $0.015; browser 5/6 *theirs*. 16–36 handmade.
- **fengyiqicoder/jevfeed (Empirical as README + 17
  tests).** JavaScript MIT. No social graph. One request
  per batch of ten. Distinct from both Winnow products.
- **Heman10x-NGU/openJev-verdict-2.0 (claim-audit, not
  endorsement).** Python; README Apache-2.0 / GitHub SPDX
  NOASSERTION. 77.10%/0.0636/0.0144 *theirs* unverified.
  Open PR #1: throughput≠latency; Laya parity; like-for-like
  ECE. ≠ IamBusy/OpenJev.

Census not re-derived this hour (last §69). Archer still
NOT landed.

Cross-repo addition: (gl) Harbor SGR-judge contract /
canaries ≠ quality / no headline yet; (gm) hand no-text
steps / gateway drops confidence; (gn) Pi control plane /
GUI never force-click; (go) generation as tree of Choices;
(gp) recipe atlas / samples not benches; (gq)
personal-history ranking without a social graph; (gr)
competing NAR dual-channel ECE as claim-verification;
(gs) empty compaction-proxy skip.

## Batch #56 (2026-09-19 ~13:52 UTC / ~07:49 Boise) — 1-token logprob ≠ Noul, replica engine, Elixir SDK, commit/jevex VOI, inbox, laya-multilingual

Note: `research/notes.md` §72. Docs-only. Folded into PR #2.
Archer still Watch. No invented metrics. Do not re-fold
§50–§71 HIGH except sibling contrast. Hunches labeled.
Local archive `/workspace/jev-archive/2026-09-19/0747/`
missing; live GitHub + HF ~13:52 UTC. IPECTER/jev-runway
**LICENSE-only empty**. GitHub `size: 0` lags on repos
that have files.

- **taku-me/chakuho (Empirical as 336-case GUI).** Python
  MIT. 1-token logprob `/v1/systemone`. Softmax ≠ Noul.
  Coverage ≠ correctness. 27B 95%/92% vs Jev 89%/82%
  *theirs*. `__none__` 97% vs 8B 10%. Cousin jevify /
  TypeAR / pcdServer / jevmlx.
- **zerodegress/jevinf (Empirical as README speedup).**
  Python MIT; ≥3.14. 2.57×/2.27× 100% argmax *theirs*.
  MPS only. Wire-compat ≠ replica.
- **phiat/typesafe-elixir-sdk (Contract).** Elixir MIT;
  1★. Unofficial HTTP client. ≠ dannote/jev OTP peer.
- **jimmyhealer/jevex (delta of §61).** Rename of
  jev-semantic-explorer. n=16 160s→69s / $8.74→$3.13 /
  16/16 *theirs*. Keep n=8 1/8→6/8.
- **yodablocks/commitjev (Empirical as 13 labelled).**
  Python MIT. Middle band never rounded. 0 false on 5
  clean *theirs* (small control). Same owner as
  jev-orderby-bench.
- **Mrmimee/hermes-plugin-jev (identity lock).** README
  MIT / GitHub SPDX null. Agnes 3.0 Flash branded as
  Jev. ≠ hermes-jev-router.
- **dev-willbird1936/pi-jev-compact (Empirical as README
  + latency).** TypeScript MIT. ≠ vava-nessa/pi-jev-
  compaction. Fail-open if <25% saved.
- **IPECTER/jev-runway (empty skip).** LICENSE only.
- **Milo318/mailordinal (Empirical as README).**
  TypeScript MIT. Decision-native inbox. Humans own
  ambiguity.
- **aarora79/jev-samples (toolbelt).** License null. One
  sample. Not a bench.
- **shaharia-lab/jev-cli (not ready).** Rust Apache-2.0
  OR MIT; 0.0.0; 17 issues. ≠ jevql.
- **convaiinnovations/laya-multilingual (Empirical as
  Hub card).** Apache-2.0; 322M; 9 likes. MASSIVE
  0.366/0.387 vs 0.227/0.733. Khmer 0.000@0.952. Ships
  uncalibrated.
- **mobarmg/jev-schema-scorer-deberta-v3-large (Hub;
  GitHub 404).** MIT. v2 Choice 0.841. Peaked ranking ≠
  calibration.
- Skip: jev-routing host-surface delta (Cursor/Devin);
  laya-typed-decisions; open-jev-laya-bench /
  jev-tree-choice-cap / INSTRUCT_JEV HF 401; jevlogs
  GitHub 404 + HF 401.

Census not re-derived this hour (last §69). Archer still
NOT landed.

Cross-repo addition: (gt) 1-token logprob ≠ Noul /
coverage ≠ correctness; (gu) open replica engine
argmax-parity; (gv) unofficial Elixir SDK ≠ OTP peer;
(gw) jevex n=16 files-to-read VOI; (gx) commit
attention≠verdict / middle band; (gy) branding ≠
backend (Agnes as Jev); (gz) Pi compact ≠ compaction;
(ha) decision-native inbox; (hb) unofficial CLI not
ready; (hc) multilingual Laya confident-wrong OOD;
(hd) schema-conditioned peaked ranking; (he) second
IPECTER empty skip.

## Batch #57 (2026-09-19 ~14:37 UTC / ~08:37 Boise) — productized System One HTTP, escalate-under-threshold, silent FALLBACK

Note: `research/notes.md` §73. Docs-only. Folded into PR #2.
Skip Archer. No invented metrics. Hunches labeled.
User-provided SIGNAL + live README `6ae8bda` /
eval/README `2009d1f`.

- **mrmps/classifier-dev (Empirical as README +
  eval/README).** MIT; **185★**; https://classifier.dev.
  Public zero-shot HTTP; no key. Jev primary
  (`src/jev.ts`); LLM fallback only. 400 headlines
  **650 ms** *theirs*; packing 100 = one-at-a-time.
  Smart: single-label <0.7; multi-label ignores.
  Emotion ≥0.9 → 82% / <0.5 → 29%. gemini-3.8-flash
  87.5→90.0 / 61.8→63.7. Multi-label F1 **0.887** /
  **230 ms** vs cascade **0.799** / 1.5 s (eval 232 ms;
  AG News **87.7%** vs 82.0%; emotion **60.5%** vs
  57.0%). n=7 train-on-test; ~0.03 coin flip.
  granite-4.0-h-micro F1 **0.546** vs advertised
  ~**0.800**; digest marks `FALLBACK`. Distinct from
  ask-jev-ai. rh-guard owns the gate card. Life/business
  (spam/inbox/feedback).

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (hf) productized System One HTTP /
label+p public contract; (hg) escalate-under-threshold /
multi-label ignores tier; (hh) vs_jev tracked JSON not
transcription; (hi) silent FALLBACK / granite 0.546 vs
advertised 0.800; (hj) classification API for
spam/inbox/feedback.

## Batch #58 (2026-09-19 ~14:48 UTC / ~08:48 Boise) — choxos/jev-reviewer systematic-review pointer (delta of §48)

Note: `research/notes.md` §74. Docs-only. Folded into PR #2.
Skip Archer. **≠** egma-ai/jev-reviewer. No invented metrics.
Hunches labeled. User-provided SIGNAL + live README `d0220a1`.

- **choxos/jev-reviewer (Empirical as README; delta of
  §48).** MIT; **12★**; https://jevreviewer.xera.ac.
  Pointer-not-generator at Cochrane/PRISMA scale. Jev
  picks line ids; code copies verbatim. Two-pass Choice
  + Noul (quotes ≥ 0.5 *theirs*). *Not found* is an
  answer. Human tick never overwritten. 18-q template
  **4.6 s / $0.0101** *theirs* (spot check, not a
  validation study).

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (hk) two-pass relative Choice +
absolute Noul; (hl) *Not found* first-class; (hm) human
check as productized judgment; (hn) evidence-synthesis
as class application beyond SWE; (ho) name lock vs
egma-ai.

## Batch #59 (2026-09-19 ~14:56 UTC / ~08:56 Boise) — githubnext/localjev wire-compat ≠ logit-equiv

Note: `research/notes.md` §75. Docs-only. Folded into PR #2.
Skip Archer. **≠** kunchenguid/local-jev. No invented metrics.
Hunches labeled. User-provided SIGNAL + live README `39939e6`
/ eval `418cae7`.

- **githubnext/localjev (Empirical as README +
  evaluation-results-2026-09-18).** MIT; **261★**;
  GitHub Next. Bun `POST /v1/systemone` on DiffusionGemma
  via Chat Completions; TypeSafe SDK drop-in. Prompted
  JSON → validate/retry → normalize + entropy confidence.
  **Not** razorback16 structured-read logits. **Not**
  IamBusy/OpenJev `/v1/decide`. Bake-off *theirs*: 1,200
  req / ~23.5 min / M5 Max. Short macro Qwen3.6 **76.7%**
  / Gemma 4 26B-A4B **75.0%** (SST-5 MAE **0.533**) /
  DiffusionGemma **74.2%**. Qwen vs Gemma 26B = 2/120.
  Do not treat as calibrated. LM Studio cannot load
  DiffusionGemma (18 Sep 2026).

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (hp) wire-compat ≠ logit-equiv /
prompted JSON ≠ structured read; (hq) GitHub Next
institutional local `/v1/systemone`; (hr) Harbor-shaped
1,200-req bake-off with caveats; (hs) LM Studio runner
gap / structured-read primitives for OpenJev parity;
(ht) name lock vs kunchenguid/local-jev.

## Batch #60 (2026-09-19 ~15:07 UTC / ~09:07 Boise) — NandhaKishorM/laya packaging, not a new species

Note: `research/notes.md` §76. Docs-only. Folded into PR #2.
Skip Archer. No invented metrics. Hunches labeled.
User-provided SIGNAL + live README `f12882b`.
**≠** TypeSafe `/v1/systemone`. **≠** githubnext/localjev.

- **NandhaKishorM/laya (Empirical as README; delta of
  Hub Laya §18 / §42 / §46 / §72).** Apache-2.0;
  **710★**; 62 forks; Python. PyPI + `Router` over
  convaiinnovations/{laya, laya-multilingual,
  laya-typed-decisions}. T4 *theirs*: 1q **32.8 ms** /
  10q **72.3 ms** (~7.8× vs Jev p50 236–276 ms cited
  third-party). Post-T ECE **0.081** vs Jev **0.246**;
  raw 0.213 vs 0.144. Banking77 **0.425** vs **0.870**
  (77 vs 72; ~3–4 tok/label). typed-decisions **0.766**
  fine-tune (base 0.362/0.342 vs majority 0.461).
  Soft-acc 0.471 vs 0.580. Khmer **0.000@0.952** —
  Router because gating cannot catch. 0.85 still soft.
  Jev rows unpublished-here.

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (hu) packaging ≠ new species /
Router script-before-p; (hv) where Jev leads
(Banking77 / soft-acc / raw ECE); (hw) post-T ECE ≠
raw ECE / latency; (hx) 0.85 still soft / Khmer OOD
productized; (hy) vs-Jev third-party unpublished-here.

## Batch #61 (2026-09-19 ~15:14 UTC / ~09:14 Boise) — @airesearch12 Benchmark Heaven openjev census (tweet, not scores)

Note: `research/notes.md` §77. Docs-only. Folded into PR #2.
Skip Archer. No invented metrics. Hunches labeled.
User-provided SIGNAL_4b0c + live X MCP this pass.
**≠** fstandhartinger/jevbench v1.1. Do **not** paste
live board ranks.

- **@airesearch12 status/2101259522933186879
  (Empirical as tweet).** Florian S / Benchmark Heaven.
  Named ~18 openjevs including GLiNER2 and routers
  (class-boundary). Engagement ephemeral (SIGNAL
  ~417/9/3; this pass 564/15/5). Incomplete vs Laya /
  githubnext/localjev / kev / TypeAR / openvons /
  chakuho / jevinf / grande / laya-jolt / blackwood /
  classifier-dev. Watch
  https://benchmarkheaven.com/jev-models. Do not copy
  Stripe.

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (hz) external census ≠ scored
bake-off; (ia) GLiNER2+routers class-boundary; (ib)
incomplete census vs watch; (ic) Harbor honesty watch
(cal / cost / latency / silent fallback).

## Batch #62 (2026-09-19 ~15:24 UTC / ~09:24 Boise) — JevBench v1.2 scored board (measurement, not a hit list)

Note: `research/notes.md` §78. Docs-only. Folded into PR #2.
Skip Archer. No invented metrics. Hunches labeled.
User-provided SIGNAL_988e + live board + GitHub README
`bf1e79ba` / RESULTS-v1.2 `fdfab1a2` / HEAD `27ed3d6c`.
**≠** tweet census §77 **≠** v1.1 87.6.

- **JevBench v1.2 (Empirical as board).** Protocol
  `jevbench::v1.2`; 534 decisions; geo-mean I/C/S/K
  25% each. Jev 1.13.0 **75.3**; SemIf **74.6** (−0.7);
  OpenJev razorback16 67.6 *theirs*. Luna I **96.8**
  rank **#7**. Cal **ON** rank. Option-order 72%→21%.
  Self-host ×2 assumption; many costs est. Laya
  absent (gap). GLiNER2 mapping-excluded. Qwen3.8 27B
  Chutes TEE **≠** Archer. Do not copy Stripe / CLI.

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (id) geometric-mean product /
weak axis dominates; (ie) cal now ON rank (delta
from v1.1); (if) weight sensitivity; (ig)
option-order 72→21; (ih) instruction models
class-boundary; (ii) Harbor honesty ×2/est.; (ij)
Laya absent gap / Qwen3.8 27B ≠ Archer.

## Batch #63 (2026-09-19 ~15:37 UTC / ~09:37 Boise) — hourly 0842 already-folded watch (apply, don’t dump)

Note: `research/notes.md` §79. Docs-only. Folded into PR #2.
Skip Archer. No invented metrics. Hunches labeled.
**Do not re-card** §73–§78. Leftover thin is skip.
**≠** a hit list.

- **Apply-the-five (recipe).** Wire-compat ≠ logit-equiv
  (githubnext/localjev §75); productize label+p + mark
  FALLBACK (classifier-dev §73; granite 0.546 vs 0.800
  *theirs*); packaging ≠ new species / script-before-p
  (NandhaKishorM/laya §76); pointer-not-generator
  two-pass (choxos/jev-reviewer §74 ≠ egma-ai); external
  census ≠ scored bake-off / geo-mean I/C/S/K (§77+§78).
- **Skip thin.** uehaj/jev-semgrep already §61 (dedicated now §86); JEValuate
  0★ ≠ ElshinQ/jevaluate; jevspeak 1★ (jev-gpt cousin);
  fable-jev 1★; jev-model-router already §77.
- **Soundness-theater skip.** totally-tim/jev-gate 0★
  MIT; connectedGraph/claude-jev-warden 1★ MIT. Soft
  Noul ≠ merge seal. **≠** jev-gateway / MongLong0214/jev-gate
  / jev-gate-student-b.

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (ik) already-folded hourly as a
recipe not a dump; (il) hard-gate Noul as PR/quality
is soundness theater.

## Batch #64 (2026-09-19 ~15:50 UTC / ~09:50 Boise) — khordoo/jev-reflex-autonomy-lab delta of §46

Note: `research/notes.md` §80. Docs-only. Folded into PR #2.
Skip Archer. No invented metrics. Hunches labeled.
Quote README. Not a hit list. **Do not re-card** the
§46 one-liner. User SIGNAL_2f18 (~08:48 Boise; ★6)
+ live this pass **7★** / 1 fork; license null;
README SHA `130987c9`; ARCHITECTURE SHA `48da0769`;
HEAD `e3297ebe`. Demo watch-demo.html.

- **S1 never stalls / S2 one-use advisory.** Jev keeps
  steering; S2 does not fly and does not grant.
- **Consumption telemetry.** Purple confidence =
  that decision used returned S2; purple S2 bar =
  arrival; red = fail. Arrival ≠ used.
- **Local controller ≠ localjev.** Rule-based built-in
  vs hosted `jev-latest`. 20% starting gate *theirs*
  still soft; does not start a mission. Seed =
  geometry ≠ async replay.
- **No pixels.** Application contracts ≠ TypeSafe SDK;
  confidence ≠ selected probability; physics owns
  collisions. README GLM 5.3 vs ARCHITECTURE
  muse-spark-1.3-contributor — quote both *theirs*.

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (im) escalate-without-stall;
(in) mixed-initiative consumption mark;
(io) Local-vs-Live reflex A/B / Local ≠ localjev;
(ip) seed≠replay / 20% still soft / no-pixels
class discipline.

## Batch #65 (2026-09-19 ~16:05 UTC / ~10:05 Boise) — awlevin/typesafe-computer-use productized OCR+AX CU

Note: `research/notes.md` §81. Docs-only. Folded into PR #2.
Skip Archer. No invented metrics. Hunches labeled.
Quote README. Not a hit list. **Do not re-card** the
census one-liner ($0.0002/step; rebuild pixel-free
reasoning). User SIGNAL_0e9d (~08:49 Boise; MIT;
★419) + live this pass **427★** / 24 forks / 7 issues;
README SHA `369f4a6a`; HEAD `cc7b5066`.

- **Productized observe→score→act.** OCR+AX → numbered
  items → hosted TypeSafe Choices → code clicks/types.
  Same hole as jev-ultrafast / gliner2-ultrafast /
  cua-s1 / Stagehand / ego-jev. Backend here is hosted
  Jev, **not** GLiNER2 and **not** Cua-S1.
- **Mutually exclusive action set.** Overlapping
  options read as doubt (confidence is concentration).
  Split `kind`/`item`/`site`/`offscreen` as VOI / noise
  control.
- **Decision ≠ answer-reader.** Never ships a screenshot
  to frontier for the *decision*. The one-shot **answer**
  writer may receive the capture. Not omni. Skip Archer.
- **Writer/decider + soft Noul.** Writer only for free
  text. Post-type 0.5 and `--min-confidence` 0.4 still
  soft. AX bonus never sole (Spotify 0 *theirs*).
  `done` ≠ verified success.
- **Harbor-shaped one-screenshot table.** $0.0002 vs
  Opus $0.032 (155×) *theirs*; dates.py caveat. Not a
  taskset. **≠** jev-ultrafast **≠** cua-s1 **≠**
  jev-macos-loop **≠** camoufox.

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (iq) OCR+AX desktop CU family;
(ir) exclusive CU options / split questions;
(is) screenshot-to-frontier fail-closed on the
decision; (it) 155× one-screenshot ≠ Harbor score.

## Batch #66 (2026-09-19 ~16:10 UTC / ~10:10 Boise) — moritzkremb/jev-voice-browser productized ASR CU

Note: `research/notes.md` §82. Docs-only. Folded into PR #2.
Skip Archer. No invented metrics. Hunches labeled.
Quote README. Not a hit list. **Do not re-card** the
§39 tweet (~300 ms / $0.0002 *theirs*). User
SIGNAL_89ca (~08:50 Boise; MIT; ★100) + live this
pass **103★** / 12 forks / 0 issues; README SHA
`fa033303`; HEAD `054db0f3`.

- **Productized ASR observe→score→act.** Web Speech
  partials → Playwright snapshot ≤100 → one 9–11-
  question hosted Jev request → policy. Same CU hole
  as typesafe-computer-use OCR, different producer
  (waveform → transcript, not screenshot → OCR).
  Jev never hears audio. Skip Archer.
- **Partial-speech VOI.** Closed-set may fire on a
  partial; free-text waits for final or 600 ms
  silence. `complete` Noul + 900 ms silence *theirs*.
- **Pointer-not-generator.** Regex spans; Jev picks;
  code copies. Numbered overlay, no second model.
- **Spoken confirm ≠ auth.** `destructive ≥ 0.5` →
  say "confirm". README *theirs*: convenience, not a
  guarantee. Control-port reach is the grant.
  rh-guard owns the gate cousin. 0.5 / 0.55 / 0.6
  still soft.
- **27/27 fixtures ≠ Harbor.** ~$0.0002/call; p50
  ≈ 300 ms *theirs*. **≠** jev-voice-control **≠**
  nikolas-j **≠** Aj1905 **≠** typesafe-computer-use.

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (iu) ASR perception front-end;
(iv) partial-speech wait policy / free-text VOI;
(iw) spoken confirm ≠ auth; (ix) overlay
disambiguate without another model.

## Batch #67 (2026-09-19 ~16:20 UTC / ~10:20 Boise) — AgentGhost wrap-as-execution + studio_yebisu JP genre atlas

Note: `research/notes.md` §83–§84. Docs-only. Folded into PR #2.
Skip Archer. No invented metrics. Hunches labeled.
Quote README and tweet. Not a hit list. Dual-signal
turn. User SIGNAL_7c0f + SIGNAL_a92b (~08:50 Boise)
+ live this pass.

- **Wrap-as-execution ALLOW/ASK/DENY.**
  [reddpy/AgentGhost](https://github.com/reddpy/AgentGhost)
  TypeScript; MIT; **2★** / 0 forks / 0 issues;
  created 2026-09-18T21:16:55Z; HEAD `ac04e4fb`;
  README SHA `44145fa9`. The wrap *is* the tool's
  execution function. Rules first; ASK/DENY throw;
  `failMode: closed`. Judge is a slot. Hosted
  provider tools out of reach. `AUTO_APPROVE` is a
  demo hatch, not a grant. **≠** jwen5419807/agentghost
  **≠** vventirozos **≠** actiongate **≠** toolgate
  **≠** jev-use. rh-guard owns the gate cousin.
- **JP genre atlas, not a bake-off.**
  [@studio_yebisu](https://x.com/studio_yebisu/status/2101065176069886152)
  2026-09-18T21:45:48Z. Apps by hole. Stars
  research-time (typesafe-computer-use 203→**427**;
  jev-voice-browser 40→**103**). Not verified evals.
  Engagement ephemeral (this pass 131,234 / 1,934 /
  192). SAM 3.1 already §39. OpenRouter Jev
  no-waitlist is WATCH. **≠** @airesearch12 **≠**
  v1.2. Do not dump the 30 repos.

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (iy) wrap-as-execution / ASK
throws / fail-closed; (iz) application genre atlas
≠ class census ≠ scored board; (ja) star-count
drift as pedagogy.

## Batch #68 (2026-09-19 ~16:25 UTC / ~10:25 Boise) — Akshay Pachaar “Jev Clearly Explained”

Note: `research/notes.md` §85. Docs-only. Folded into PR #2.
Skip Archer. No invented metrics. Hunches labeled.
Quote ARTICLE.md. Not a hit list. User SIGNAL_55e5
(~08:51 Boise; ~183k views) + live this pass
**233,495** / **2,280** / **235** / **3,652**.

- **External pedagogy / how-to-apply.** Independent
  of TypeSafe docs. LLM hammer for bounded
  decisions; code owns branches; parallel
  questions; thresholds in code; schema-safe ≠
  correct; three placements with an LLM (routing /
  tool-risk / verify); shadow-mode; questions-as-code.
- **200× / 400× are TypeSafe ceiling claims.**
  Article *theirs*: 70–500 ms, $0.042/MTok input,
  output free; treat multiples as a ceiling, not a
  promise. Not Harbor.
- **Text-only.** Convert environment to text/JSON
  first. Not looking at the screen. Skip Archer.
- **Name locks.** ≠ official docs ≠ Flavio Copes
  (cited further reading) ≠ LangChain harness
  (cited; not a wrap card) ≠ AgentGhost §83.

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (jb) public pedagogy receipt
for mixed architecture; (jc) schema-safe ≠ correct
as the safer hallucination sentence; (jd) marketing
multiples as ceiling, not Harbor.

## Batch #69 (2026-09-19 ~16:30 UTC / ~10:30 Boise) — uehaj/jev-semgrep dedicated

Note: `research/notes.md` §86. Docs-only. Folded into PR #2.
Skip Archer. No invented metrics. Hunches labeled.
Quote README. Not a hit list. User SIGNAL_9afa
(~08:54 Boise; ★42) + live GitHub this pass **51★**
(ephemeral). HEAD `21120e9`; README SHA `923e6a5`.

- **Proposition ≠ embedding.** Cross-encoder
  line+question → does the proposition hold, not
  topical cosine. Contrast-set: all six about a
  refund; only customer-*asking* pass. Angry agent
  vs angry customer cosine ~1.
- **Boolean composition of soft Nouls.** AND/OR/NOT
  after threshold in code; do not multiply p.
  ≠ jev-combinators metaphor.
- **Semgrep.dev name collision.** Rename if both
  installed. **≠** SAST. **Not a gate** (ranking
  fail-open; rh-guard skip).
- **0.94/0.98 *theirs*.** LLM-as-judge 10 cases ×
  51-line corpus. Not Harbor. Stars research-time.

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (je) proposition ≠ embedding /
contrast-set; (jf) boolean composition of thresholded
Nouls; (jg) Semgrep.dev namesake + not-a-gate.

## Batch #70 (2026-09-19 ~16:52 UTC / ~10:47 Boise) — hourly 1047 HIGH + deferred 0945

Note: `research/notes.md` §87. Docs-only off main
(PR #2 merged). Skip Archer. No invented metrics.
Hunches labeled. Quote READMEs. Not a hit list.
0★ HIGHs still get real cards.

- **Decision-validated UI.** gram-render never authors
  text; jev2ui leftover Gemini. Valid tree ≠ good
  screen. Telegram/A2UI envelopes are exact.
- **Decision-as-assert.** jevtest ambiguous band fails
  both polarities; 0.85 still soft; record/replay ≠
  merge seal. typesafe-ai/jevtest 404.
- **Hybrid S1.** anima3 closed verb menu + hard safety
  first; Qwen logprob default; jeff confidently flat
  on magnitude; a11y tree. Do not invent Laya.
- **Pointer search.** JevFind path then window.
- **Harbor trio.** frontier-bench 72.5%/0.161 vs Fable
  84%/0.064 *theirs*; ChaosNLI JS worse than uniform;
  **≠** frontier-100. GLiClass product bakeoff 78/40/49.
  job-posting-triage floor 0.947; tfidf wins;
  calibration ≠ discrimination.
- **Non-SWE.** ha-switchboard HA remains execution
  **≠** HA-Jev. n8n Low Confidence. Authorship named
  escape, not evidence.
- **Compaction-pi / jevloop.** Namesake lock; ~50×
  *theirs*; fail-open. Full-distribution optimizer;
  mock default; no LLM in the loop.
- **Deferred class.** laya-vision SmolVLM `score`
  untrained **≠** blackwood **≠** Archer.
  Cerebellum `/v1/decide` ≠ TypeSafe; wire-compat vs
  agent-routing as separate Harbor axes; competing NAR
  **not endorsement**. laya-grounded not drop-in;
  phishing regress; Platt not temperature.

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (jh) decision-validated UI /
never-authors-text; (ji) ambiguous-band anti-round
assert; (jj) hybrid S1 hard-safety-first; (jk) Harbor
three bake-off shapes + majority floor; (jl)
wire-compat vs agent-routing as separate axes;
(jm) grounding can regress phishing.

## Batch #71 (2026-09-19 ~17:25 UTC / ~11:25 Boise) — queued SIGNALs + jevsubrouter

Note: `research/notes.md` §88. Docs-only on PR #3.
Skip Archer. No invented metrics. Hunches labeled.
Quote READMEs. Soft Noul ≠ hard safety. laya-vision
+ Cerebellum already §87 — not re-carded.

- **Open LoRA replica namesake.** GestaltLabs/Jeff-1
  Qwen3-4B LoRA **≠** logan-markewich/jeff GLiFormer.
  n=9730 *theirs*: acc **0.8183** ECE **0.0807** vs Jev
  **0.8283** / **0.0932**. Acc/Brier lose; ECE wins;
  set reused. Lower ECE ≠ individual correct.
- **Empty findings ≠ approval.** stanley-code: code
  owns decisions; `notChecked` first-class; no
  `pass`/`approved`; human `--promote-candidate` only;
  0.6/0.55/0.15 still soft. `jev-code` 0.0.1 does
  nothing; 0.1.0 not on npm.
- **NL memory → beam-search FS.** findme: algorithm
  stays yours; S1 ranks listed names+metadata.
  **≠** JevFind path-then-window. Ranking ≠ identity.
  License null.
- **Price workers, not the conversation.**
  jevsubrouter: bind at dispatch; advise at the turn;
  fail-open; low conf → balanced, never silent down;
  stats are counts, not dollars. Deferred 0945 HIGH.

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (jn) acc vs ECE tradeoff on a
named n with reused-set honesty; (jo) empty search ≠
proof for a coding-agent coverage ledger; (jp) S1 as
beam-ranking policy over FS candidates; (jq) prompt
cache as the exact envelope — never swap the live
conversation model.

## Batch #72 (2026-09-19 ~17:55 UTC / ~11:49 Boise) — hourly 1144 HIGH

Note: `research/notes.md` §89. Docs-only on PR #3.
Skip Archer. Do **not** re-fold 1047 / §87 / §88.
No invented metrics. Hunches labeled. Quote READMEs.
Soft Noul ≠ hard safety. Sibling jev-decisions
pointer only. jev-desktop already MED — pointer only.

- **Typed if.** BoundaryML/feelings `.feels()` is a
  typed method, not a new language. Default 0.5 is
  Noul-0.5-never-rounded. Exhaustive BAML `match`.
  **≠** hunch **≠** Probably. License null; **0★**.
- **Shadow then honor.** apa-agent-harness **≠**
  AntonioCoppe/jev-harness; unpublished npm; 0.85
  still soft; “mathematically fulfilled” overclaim.
  apa-persona-engine SM then leftover LLM; <250 ms ≠
  microsecond. grok-bot-jev skill honor; A/B proxies
  ≠ tokens; 13.0× is a top-five cap.
- **Human every action.** Essentiel-Jev never
  authority; 0.75 provisional; synthetic tests.
  License null.
- **Atom then sense.** enzo-mcp independently
  falsifiable claims; deterministic evidence outranks
  Jev; UNKNOWN useful; **≠** jev-sift.
- **File by Choice.** pigeonhole OTHER skip; 0.6
  still soft; **≠** jev-semgrep. HF playground static
  no-network; **≠** classifier.dev.
- **Question preflight.** jev-reliability Nothing
  about accuracy; noul-gate 0.0%/12.5%/3.6% *theirs*;
  **≠** dinostomp. clduab11/jev-test bars ≠ scores;
  **≠** realZachi/jevtest. jev-rag-benchmark “Jev
  wins” is not an assumption. dairui1/jev-lab 91% vs
  79% *theirs* synthetic; **≠** BrendanH18/jev-lab.
- **Inbox read-only vs write.** jevmail
  `gmail.readonly` ~3¢/1k *theirs*; mailjay
  archive/trash after review; **≠** mailordinal.

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (jr) decision-as-typed-control-flow
(`.feels()`); (js) shadow then honor / skill cannot
force a bot; (jt) human every action never authority;
(ju) atomize then sense / UNKNOWN useful; (jv)
decision-as-filing OTHER skip; (jw) question
preflight consistency ≠ accuracy; (jx) inbox
read-only vs write after review.

## Batch #73 (2026-09-19 ~18:41 UTC / ~12:41 Boise) — hourly 1241 HIGH

Note: `research/notes.md` §90. Docs-only on a fresh PR
off main. Never reopen merged #3 / #4 / #5. Skip Archer.
Do **not** re-fold 1144 / §89. No invented metrics.
Hunches labeled. Quote READMEs. Soft Noul ≠ hard safety.
0★ HIGHs still get real cards.

- **Observe→score→act namesake.** ZHUBoer/ego-jev
  reserved `__none__`. runWorkflow completed ≠ success.
  Exact work local. **≠** jiangkoumo/ego-jev. **0★**.
- **Decision-as-ranking.** jsort scores are relative.
  Noul not Choice for scale. CommonLit r=0.824 / ρ=0.841
  *theirs*. **1★**.
- **Native vs schema-guided Harbor.**
  groundedness-judge-bench native vs schema-guided.
  implicit_true included in yes. Fastest/cheapest ≠
  quality. **≠** jev-judge-bench. **0★**.
- **0 promotions / authored vs real.** jev_playground 0
  promotions. routing-backtest 0.0447%. Plumbing 83% ≠
  quality. **≠** HF playground. **0★**.
- **Offload + classifier-not-generator.**
  yuyang2230/jev-agent-skill jev-1.13-free.
  jev-techstack-classifier stack_config.json only.
- **Collapse late.** s1_ruby collapse late.
  `undecided?` abstain. Code asks; code decides. **≠**
  hunch **≠** feelings. **1★**.
- **Unofficial toolbelt.** 2389-research/judgement
  license null. confidence ≠ winner p.
  typesafeai-sdk-community not a new species.
- **Pointer shell.** tpellet/hunch exit 3. never-execute
  list. **≠** carldaws/hunch. **0★**.
- **Preview-first VOI / rubric rewrite.** jev-file-search
  scores not calibrated accuracy. jev-linkmap Jev never
  sees S2 prose.
- **Life fail-open covers.** muhammedilyasy/jev-mail
  metadata only. tidy none-of-folders stay. tab-bouncer
  pinned/audio/current never closed. lkclean Show
  fail-open. jev-yt-time-saver Show anyway.
- **S1 decide / S2 plan.** ORIGIN pause-if-no-Jev.
  validResponse sums-to-1. **≠** Essentiel-Jev. **1★**.
- **Seed/expand/judge/verify + local daemon ≠ Jev.**
  jev-crawlers risk bands never raw boolean. jevbrain
  AUTO_ACT is not a Noul. **9★**.

Census not re-derived. Archer still NOT landed (HF empty;
tracker likes 49 lastModified 2026-09-19T18:37:18Z still
promised). Laya yes. Blackwood ABSENT. SemIf 1846 (+17).
jevlike 962 (+3). TypeAR-AI/TypeAR 10 (+1). Awesomejev
flat 561/27007.

Cross-repo addition: (jy) observe→score→act namesake lock;
(jz) decision-as-ranking / Noul not Choice for scale;
(ka) native vs schema-guided Harbor; (kb) 0 promotions /
authored vs real; (kc) collapse late as language
primitive; (kd) unofficial CLI/SDK packaging; (ke)
pointer shell exit-3; (kf) preview-first VOI; (kg) life
fail-open covers; (kh) S1 decide / S2 plan pause-if-no-Jev;
(ki) crawler risk bands; (kj) local daemon AUTO_ACT is
not a Noul.

## Batch #74 (2026-09-19 ~19:47 UTC / ~13:47 Boise) — hourly 1347 HIGH

Note: `research/notes.md` §91. Docs-only on a fresh PR
off main. Never reopen merged #3 / #4 / #5 / #7. Skip
Archer. Do **not** re-fold 1241 / §90. No invented
metrics. Hunches labeled. Quote READMEs. Soft Noul ≠
hard safety. 0★ HIGHs still get real cards.

- **Judge harness as control API.** judgekit YAML
  classify/score/route/verify. typed-judge-kit
  verdict-in-code. 97.7% n=130 *theirs*. **≠**
  JudgeBench. **0★**.
- **Batch packing VOI.** alsoleg89/decide packing VOI.
  0.8 ≠ 80% accuracy. **≠** jev-sift. license null.
  **0★**.
- **Calibration as product.** Jev-Calibration Platt ECE
  0.117→0.052. jev-calibration-arena never acts. **≠**
  jev-arena. **0★**.
- **Decision-as-Plugin.** ctmx/openrouter-jev-mcp
  Decision-as-Plugin. FrancoisChastel/jev-code ≠ npm
  jev-code (**1★**). claudecode-jev-marketplace fail-open
  not hot path. pedroknigge/mcp_jev packs not ask_jev.
  cyrusasco/typesafe-mcp noul deadband 0.35–0.65.
  codaaiteam/jev-skill jevtypesafeai.com ≠ TypeSafe.
- **Policy-constrained skill select.** hermes-switchyard ≠
  hermes-jev-router ≠ hermes-plugin-jev. **0★**.
- **Tiny local econ pruner.** nanoprune 2.8MB ECE 2.58%.
  0 hallucination theater. **0★**.
- **Observe→score→act cousins.** smartdio/jev-browser-agent
  ≠ ZHUBoer/ego-jev. Dakai/omp-jev-web DONE ≠ proof.
  hari007sh/jev ≠ dannote/jev.
- **Deterministic verify ≠ System One.**
  0thernet/system-one-skills deterministic verify.
  **0★**.
- **Soft-score vs hard-argmax.** typed-gate band
  [0.40,0.60] is refusal. pi-jev-gate fail-closed; choice is the verdict.
  rh-guard owns.

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (kk) judge harness as control API;
(kl) batch packing VOI; (km) calibration as product;
(kn) Decision-as-Plugin; (ko) policy-constrained skill
select; (kp) tiny local econ pruner; (kq) observe→score→act
cousins; (kr) deterministic verify ≠ System One; (ks)
soft-score vs hard-argmax.

## Batch #75 (2026-09-19 ~20:41 UTC / ~14:41 Boise) — hourly 1441 HIGH

Note: `research/notes.md` §92. Docs-only on a fresh PR
off main. Never reopen merged #3 / #4 / #5 / #7 / **#8**.
Skip Archer. Do **not** re-fold 1347 / §91. No invented
metrics. Hunches labeled. Quote READMEs. Soft Noul ≠
hard safety. 0★ HIGHs still get real cards. rh-guard
owns the gate cousins; Augustus owns placement.

- **Self-hosted econ.** Foq ~25ms/2.2GB local (**1★**).
  rev prefill-only + HF jev-0.5b (**0★**).
  robfrase/jev planning memo. Sample 32.4 ms is not
  a bench.
- **Soft-judgment gate integrity.**
  typesafe_agent_gates 27/27 / 31/31. EpicEric/safe-sh
  static remainder (**1★**; HIGH delta of MED §58).
  pastepilot Confirm before act. rh-guard owns.
- **Retrieval as calibrated decision space.**
  Jev-Reranker live Jev not yet measured. sessionwise
  opt-in relevance. jev-search pointer sieve. Score ≠
  truth.
- **Enterprise reflexes.** 400ms Salesforce WebMCP
  (timestamps ≠ Harbor). typesafe-scheduler-diagnostics
  advisory (does not place Pods).
- **Screenshot-free / CU.** droidjev screenshot-free.
  Tewoto1 jevcu planner still writes. **≠** closed-vote.
- **Hybrid S1/S2.** ha-conversation-jev Jev→Grok
  (**1★**). dsh-jev can only gate (**2★**; HIGH delta of
  MED §59).
- **Harbor-jevals / SRE.** jev-classification-benchmark
  specified not run. jev-luna-pagerduty p≥0.50
  (synthetic n=3000 *theirs*; ≠ Loghub).
- **Laya densifies.** meldltd/meldecision laya-go ONNX.
  laya-doom never pixels. logixism/laya-api empty README.
  akpsahan/laya ≠ Archer. **≠** Qwen3.8-27B.
- **Demos / unofficial toolbelt.** choxos/jevchess
  engine owns truth (**1★**). jev-drive sim not AV.
  story-arc Jev never authors. jev-hs-assistant HS6.
  golergka/jev-plays-starcraft-2 UI-verified ≠ API
  Victory (**1★**). awesome-jev-use-cases catalog
  (**2★**). Nibir1/typesafe-go ≠ official.

Census not re-derived. Archer still NOT landed;
tracker likes **50** lastModified UNCHANGED
2026-09-19T18:37:18Z; SemIf 1873 (+7); jevlike 969
(+2); TypeAR 10 flat; Awesomejev 561/27007 flat.

Cross-repo addition: (kt) self-hosted econ; (ku)
soft-judgment gate integrity; (kv) retrieval as
calibrated decision space; (kw) enterprise reflexes;
(kx) screenshot-free / CU; (ky) hybrid S1/S2; (kz)
Harbor-jevals / SRE; (la) Laya densifies; (lb) demos
/ unofficial toolbelt.

## Batch #76 (2026-09-19 ~21:23 UTC / ~15:23 Boise) — SIGNAL jevcache + jev-align

Note: `research/notes.md` §93. Docs-only on a fresh PR
off main after #9 merge `059f3670`. Never reopen merged
#3 / #4 / #5 / #7 / #8 / **#9**. Skip Archer. Do **not**
re-fold 1441 / §92. No invented metrics. Hunches
labeled. Quote READMEs. Soft Noul ≠ hard safety.
rh-guard owns HIT-as-truth and training-score
auto-accept; Augustus owns placement.

- **Decision ledger / memoization.**
  hyperspaceai/jevcache (**8★** this pass, SIGNAL ★6;
  HEAD `a211d13`; README SHA `7c2abe99`). fingerprint
  after redact; recall vs decide; publish
  fingerprints+answers; CI replay as Harbor cousin.
  Cache hit ≠ correctness. hyperspaceai/jevcache ≠
  kushals256/jevcache.
- **GEPA alignment loop.** sutro-sh/jev-align
  (**60★** this pass, SIGNAL ★56; forks **7**; HEAD
  `49753df`; README SHA `363fccb7`). human labels
  only; score never auto-accepts; production capture
  flywheel. sutro-sh/jev-align ≠
  caiovicentino/jev-align.

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (lc) decision ledger /
memoization; (ld) GEPA alignment loop.

## Batch #77 (2026-09-19 ~21:35 UTC / ~15:32–15:35 Boise) — SIGNAL enzyme + JA ModernBERT + Gemma/Nemotron/djev-dev/Laya essay

Note: `research/notes.md` §94. Docs-only on a fresh PR
off main after #10 merge `30438eff`. Never reopen
merged #3 / #4 / #5 / #7 / #8 / #9 / **#10**. Skip
Archer. Do **not** re-fold jevcache/jev-align / §93.
No invented metrics. Hunches labeled. Quote READMEs.
Soft Noul ≠ hard safety. rh-guard owns
guidance-as-hook, unofficial-local-as-Jev,
hosted-bootstrap silent FALLBACK,
LFM-default-as-JA-softmax, Nemotron
“not calibrated replacement”, and Laya
confidence-without-competence; Augustus owns
placement.

- **Compile-time System One / questions-as-index.**
  byenzyme/enzyme (**63★** this pass, SIGNAL ★62;
  HEAD `c91d6b5`; README SHA `9af7c570`).
  guidance ≠ hook; catalysts ≠ summaries;
  compile-time System One; hosted bootstrap ≠
  silent TypeSafe. ~350×/1000× *theirs*.
- **Unofficial JA ModernBERT cross-encoder.**
  argos1111/modernbert-ja-310m-jev (CC-BY-SA-4.0;
  **2 likes**; sha `07cda235`) + Argos1111/jev_local
  (**14★**; HEAD `8ccc04d`; README SHA `ee7b536a`).
  unofficial ≠ TypeSafe; format_version
  modernbert-jev/1; Argos1111/jev_local ≠
  us/jev-local ≠ kunchenguid/local-jev; LFM
  default ≠ ModernBERT backend. JGLUE JNLI
  92.62% / JComQA 92.40% *theirs*.
- **NAR class legitimacy / multimodal /
  Router-OOD.** @googlegemma DiffusionGemma-as-Jev
  (~0.2s *theirs*); pst2154/Nemotron_Jev (**6★**;
  HEAD `983cc29`; README SHA `f2f3d052`; Nemotron ≠
  TypeSafe Jev; not a calibrated replacement);
  Davipar/djev-dev (**2★**; HEAD `3ce907e`; README
  SHA `6d59d020`; djev-dev complements djev-spark;
  images as Choice options); Laya essay numbers
  *theirs*; Router/OOD confidence.

Census not re-derived. Archer still NOT landed.

Cross-repo addition: (le) compile-time System One /
questions-as-index; (lf) unofficial JA ModernBERT;
(lg) NAR legitimacy / multimodal / Router-OOD.

## Batch #78 (2026-09-19 ~21:41 UTC / ~15:41 Boise) — hourly 1541 HIGH

Note: `research/notes.md` §95. Docs-only on a fresh PR
off main. Never reopen merged #7 / **#8** / **#9** / **#10** / **#12**.
Do **not** re-fold §93 / §94. Skip Archer. Do **not**
re-fold 1441 / §92. No invented metrics. Hunches
labeled. Quote READMEs. Soft Noul ≠ hard safety.
0★ HIGHs still get real cards. rh-guard owns the
injection-firewall / CI-gate cousins; Augustus owns
placement.

- **Decision-as-plugin for SWE.** difficulty +
  policy thresholds + JSONL trace (**0★**).
  jev-codex-pilot model + reasoning depth (**0★**).
  keep/shadow/hybrid/reject (license null; **0★**;
  20-case *theirs* failed the cost gate).
- **Evidence projection vs LLM summary.** quarry
  evidence projection (**0★**; **master**). Pointer,
  never paraphrase. 5 s fail-open.
- **Soft judgment integrity.** jevguard
  calibrator/cache/escape (**0★**). jev-ci-selector
  CI shadow mode (license null; **0★**). Shadow
  default; enforce opt-in. rh-guard owns.
- **Physical/control first-class domain.**
  Frank-ZY-Dou/awesome-jev robotics/3D/control
  (license null; **0★**). Text-state, not pixels.
  One seed-0 ≠ a rate.
- **Harbor-jevals / injection-firewall.**
  one-dollar-tahoe TypeSafe Jev defense eval
  (**0★**). ~74 demo; README has no ASR/FPR.
  rh-guard owns.
- **llama.cpp replica.** llama-jev llama.cpp replica
  (license null; **0★**). Softmax ≠ Noul. **≠**
  TypeSafe **≠** pcdServer.

Census not provided this hour (not re-derived).
Archer still NOT landed. Last pin from §92:
tracker likes **50** lastModified UNCHANGED
2026-09-19T18:37:18Z; SemIf 1873; jevlike 969;
TypeAR 10; Awesomejev 561/27007.

Cross-repo addition: (lh) Decision-as-plugin for SWE;
(li) evidence projection vs LLM summary; (lj) soft
judgment integrity; (lk) physical/control first-class
domain; (ll) Harbor-jevals injection-firewall;
(lm) llama.cpp replica.

## Batch #79 (2026-09-19 ~22:39 UTC / ~16:39 Boise) — hourly 1639 HIGH

Note: `research/notes.md` §96. Docs-only on a fresh PR
off main. Never reopen merged #7 / **#8** / **#9** /
**#10** / **#12** / **#13**. Do **not** re-fold §93 /
§94 / §95. Skip Archer. Do **not** re-fold 1441 /
§92. No invented metrics. Hunches labeled. Quote
READMEs. Soft Noul ≠ hard safety. 0★ HIGH still
gets a real card. Augustus owns placement.

- **OpenCode host-port of evidence-preserving
  stdout prune.** OpenCode jev-pruner context sieve
  (**0★**; GitHub license **null**; `package.json`
  MIT). observe→score-candidates→prune. jev-zen /
  jev-1.13-free. zen-chat ≠ Noul. fail-open original.
  keepScore >0.1 floor. **≠** tamaratran/jev-pruner
  **≠** nrdz-labs/fast-jev-opencode. Do not copy
  24/24 / 83%.
- **MEDIUM watch / tooling (do not over-weight).**
  jev-webagent-bench empty stub (size 0; 409).
  Kiln-AI/jev_jsonschema noul_threshold 0.5 (**5★**).
  NSStudent/JevSwiftSDK unofficial (**5★**).

Census not provided this hour (not re-derived).
Archer still NOT landed. Last pin from §92:
tracker likes **50** lastModified UNCHANGED
2026-09-19T18:37:18Z; SemIf 1873; jevlike 969;
TypeAR 10; Awesomejev 561/27007.

Cross-repo addition: (ln) OpenCode stdout-prune
host port; (lo) schema/SDK adapters + empty bench.

## Batch #80 (2026-09-19 ~23:17 UTC / ~17:17 Boise) — SIGNAL gliner-native-runtime

Note: `research/notes.md` §97. Docs-only on a fresh PR
off main. Never reopen merged #7 / **#8** / **#9** /
**#10** / **#12** / **#13** / **#14**. Do **not** re-fold
§93 / §94 / §95 / §96. Skip Archer. Do **not** re-fold
1441 / §92. No invented metrics. Hunches labeled. Quote
READMEs. Soft Noul ≠ hard safety. User-linked SIGNAL
(pushed 2026-08-26). Augustus owns placement. rh-guard
skips.

- **GLiNER2 native Apple path.** unofficial Swift/Core
  ML GLiNER 2.5-small (Apache-2.0; **4★**; HEAD
  `b44f661`; README SHA `901eb063`; size 1838). entity
  spans + confidence. not Choice/Score/Noul. not
  TypeSafe. label descriptions as schema. on-device ANE
  economics. honesty locks. shershah1024/gliner-native-runtime
  ≠ Fastino. **≠** gliner25-compaction **≠**
  gliner2-ultrafast **≠** Eran-BA/Jev_from_GLiNER2 **≠**
  NSStudent/JevSwiftSDK **≠** jevmlx. default threshold
  0.1 still soft. README 0.99 fixture. Do not invent
  ANE ms / ECE / Harbor.

Census not provided this hour (not re-derived).
Archer still NOT landed. Last pin from §92:
tracker likes **50** lastModified UNCHANGED
2026-09-19T18:37:18Z; SemIf 1873; jevlike 969;
TypeAR 10; Awesomejev 561/27007.

Cross-repo addition: (lp) GLiNER2 native Apple path.

## Batch #81 (2026-09-19 ~23:40 UTC / ~17:40 Boise) — hourly 1740 HIGH

Note: `research/notes.md` §98. Docs-only on a fresh PR
off main. Never reopen merged #7 / **#8** / **#9** /
**#10** / **#12** / **#13** / **#14** / **#15**. Do **not**
re-fold §93 / §94 / §95 / §96 / §97. Skip Archer rewrite.
Do **not** re-fold 1639 / gliner-native-runtime / 1541.
No invented metrics. Hunches labeled. Quote READMEs.
Soft Noul ≠ hard safety. Augustus owns placement.
rh-guard owns the silent-FALLBACK cousin; rh-guard
does not own protocol envelope / ranking fail-open /
replica honesty.

- **Decision Graph Protocol envelope.** numerous-com/dgp
  (Python MIT; **0★**; HEAD `a9cb3c4`; README SHA
  `655fc638`; size 303). Decision Graph Protocol
  frame→assess→commit. app retains permissions/effects.
  Jev-first assessor-neutral. guarded commit /
  receipt/next frame. assessment batching. hard-gating
  DGP as safety theater. numerous-com/dgp ≠ TypeSafe
  official. 106 tests *theirs*. Mock resolver ≠ Jev.
- **Calibrated meaning-grep over a live tree.**
  can1357/jegrep (Rust MIT; **13★**; HEAD `a280f14`;
  README SHA `6f241390`; size 511; v0.1.1). jegrep
  calibrated path+range Nouls. no embeddings/index/daemon.
  ~$0.01–0.03 typical. agent --json. can1357/jegrep ≠
  Bentlybro/jevgrep ≠ uehaj/jev-semgrep. No published
  Harbor. Do not copy 79%. OpenRouter/TypeSafe
  auto-failover is silent FALLBACK, not the same Noul.
- **Archer-arch fidelity + measured calibration gap.**
  jaredpalmer/kev family (Apache-2.0; **507★**; HEAD
  `2e9069be`; README SHA `50f828ea`). Archer-arch
  fidelity. kev family OOD 0.76–0.77 vs Jev 0.86.
  block-causal isolation. pointer/readout CE-trained.
  /v1/systemone drop-in. replica honesty. Score
  confidence is a stand-in (*theirs*). Do not rewrite
  §45. Jev-omni owns the replica/code fold.

Census not provided this hour except Archer tracker
likes **51** (+1); lastModified UNCHANGED
2026-09-19T18:37:18Z; Hub archerhume/4rcherhume HTTP
**401**. Archer still NOT landed. Last remaining pin
from §92: SemIf 1873; jevlike 969; TypeAR 10;
Awesomejev 561/27007.

Cross-repo addition: (lq) Decision Graph Protocol
envelope; (lr) calibrated meaning-grep live tree;
(ls) Archer-arch family OOD gap.

## Batch #82 (2026-09-20 ~00:43 UTC / ~18:43 Boise) — hourly 1843 HIGH

Note: `research/notes.md` §99. Docs-only on a fresh PR
off main. Never reopen merged #7 / **#8** / **#9** /
**#10** / **#12** / **#13** / **#14** / **#15** /
**#16**. Do **not** re-fold §93 / §94 / §95 / §96 /
§97 / §98. Skip Archer rewrite. Do **not** re-fold
1740 / gliner-native-runtime / 1639 / 1541. No invented
metrics. Hunches labeled. Quote READMEs. Soft Noul ≠
hard safety. Augustus owns placement. gut/judge are
overlays not species. jev-forge is class-architecture
not a sixth species. llm-vs-jev is a cross-note;
rh-guard owns steerability. Quote live REST over watch.
`invented_signal: false`.

- **Cost-derived YES/NO/UNSURE control flow (PRIMARY).**
  Kungie/gut (GitHub Apache-2.0 / LICENSE MIT /
  pyproject Apache-2.0 *theirs*; **0★**; HEAD `cb56c875`;
  README SHA `630474f6`; size 0; pre-alpha).
  cost-sensitive decision theory × System One
  probabilities → control flow. thresholds derived from
  costs not hard-coded. YES / NO / UNSURE from
  cost_false_yes / cost_false_no / cost_human.
  auto-batching same-object questions. Default
  `on_unsure="raise"` is app policy, not a System One
  hard gate. Kungie/gut ≠
  tpellet/hunch ≠ carldaws/hunch. Overlay, not a
  species.
- **Typed-callback twin.** Illusion47586/judge
  (TypeScript MIT; **0★**; HEAD `e69f65a1`; README SHA
  `08554c6f`; size 317; `@brkn-labs/judge` 0.1.0).
  judgment vs generation. deterministic execution after
  probabilistic judgment. exactly one app-owned
  callback. explicit uncertain branch.
  Illusion47586/judge ≠ lexingtonhibiki/judgekit ≠
  Ascurse/typed-judge-kit. Overlay, not a species.
- **Variable-N option scoring as the trainable object.**
  zwliJay/jev-forge (Python; GitHub NOASSERTION /
  LICENSE MIT; **1★**; HEAD `eb3e4a2d`; README SHA
  `359f3f57`). variable-N option scoring as the
  trainable object. dynamic candidate bags not fixed
  label sets. zwliJay/jev-forge ≠ NanoJev. Not a sixth
  species. Do not clone weights. Do not paste 0.579 as
  Harbor.
- **Open NAR replica economics (late-catch).** wfzyx/von
  (Apache-2.0; **43★**; HEAD `b9e42b26`; README SHA
  `574aa628`). NAR local drop-in. open replica economics
  / latency vs closed Jev. wfzyx/von late-catch HIGH.
  competing NAR claims / replica honesty. Do not merge
  Needle 52.6% with n=78 93.0%.
- **Typed vs chat judges on guardrailing (cross-note).**
  ishaannk/llm-vs-jev (Apache-2.0; **0★**; HEAD
  `182e0864`; README SHA `d9ebd40f`). typed judgments vs
  chat judges on guardrailing. nothing wins outright.
  can be argued out of guarding. ishaannk/llm-vs-jev
  cross-note only. deeper integrity fold is rh-guard.

Pulse: Archer still NOT landed. Hub archerhume/4rcherhume
HTTP **401**. Qwen3.8-27B ≠ Archer. Tracker likes **51**
flat; lastModified UNCHANGED 2026-09-19T18:37:18Z. Laya
yes. Blackwood ABSENT from tracker (Hub still 200).
Awesomejev 561/27007 flat (user-provided). Live REST:
SemIf **1936★**; jevlike **983★** (watch 984); TypeAR
**11★** flat. X MCP since_id held; pages_archived 0; no
invented tweets.

Cross-repo addition: (lt) cost-derived YES/NO/UNSURE
overlay; (lu) typed-callback control flow; (lv)
variable-N option scoring; (lw) von late-catch NAR;
(lx) typed vs chat judges on guardrailing.

## Batch #83 (2026-09-20 ~01:43 UTC / ~19:43 Boise) — hourly 1943 HIGH

Note: `research/notes.md` §100. Docs-only on a fresh PR
off main. Never reopen merged #7 / **#8** / **#9** /
**#10** / **#12** / **#13** / **#14** / **#15** /
**#16** / **#17**. Do **not** re-fold §93 mechanism /
§94 / §95 / §96 / §97 / §98 / §99. Skip Archer rewrite.
Do **not** re-fold 1843 / 1740 / gliner-native-runtime /
1639 / 1541. No invented metrics. Hunches labeled. Quote
READMEs. Soft Noul ≠ hard safety. Augustus owns
placement. probably is a language not an overlay.
jev-align is a live-star / framing delta. jev-lint is
jevlint rename. Quote live REST over watch.
`invented_signal: false`.

- **Jev IS the if-statement (PRIMARY).**
  southpolesteve/probably (TypeScript MIT; **3★**; HEAD
  `6bf671a4`; README SHA `c28570a9`; size 19; package
  `probably-lang` 0.1.0). Jev IS the if-statement.
  judgments/probabilities drive branches. text model only
  writes prose. interpreter owns variables/loops/budgets/
  replay. otherwise maybe / confidence gate. chaos samples
  after the gate. southpolesteve/probably ≠ carldaws/hunch
  ≠ feelings ≠ Kungie/gut ≠ Illusion47586/judge ≠
  tidymodels/probably. Language, not a library overlay.
- **GEPA live-star / framing delta.** sutro-sh/jev-align
  (Apache-2.0; **133★**; forks **10**; HEAD `49753df9`
  unchanged; README SHA `363fccb7` unchanged). 133★ /
  forks 10 live. build calibrated classifiers from human
  feedback. Do **not** re-dump the §93 loop.
- **Retrieve by relevance not resemblance.**
  samdotmak/jev-recall (MIT; **6★**; HEAD `d3e4acfb`;
  README SHA `ea774519`). retrieve by relevance not
  resemblance. one calibrated yes/no per memory in one
  request. pointer mode 17/18 19/20 *theirs*. embedding
  resemblance misses the allergy. samdotmak/jev-recall ≠
  jev-search ≠ jev-sift ≠ carryforward ≠
  chopratejas/invalidate.
- **Memory leases ended by new evidence (HIGH upgrade).**
  chopratejas/invalidate (Apache-2.0; **11★**; HEAD
  `d6ade601`; README SHA `8cccad5f`). memory leases ended
  by new evidence. six Nouls then fixed rules in code. 0
  of 157 false invalidations. questions/plans/directives
  are not evidence. unsure → review queue. host keeps the
  store.
- **Contract-of-artifact lint (rename).** mizchi/jev-lint
  (TypeScript MIT; **13★**; HEAD `62d73f8e` byte-identical
  to jevlint; README SHA `4c0e37cd`). name↔body / comment
  truth / test-claims. mizchi/jev-lint is mizchi/jevlint
  rename. no shipped rule has severity error. ~1 in 5
  findings wrong *theirs*. mizchi/jev-lint ≠
  huntedman/JevLint ≠ MichitoSugawara/jev-lint.
- **JSON Schema question compiler (HIGH upgrade).**
  Kiln-AI/jev_jsonschema (MIT; **5★**; HEAD `fccea8c2`
  unchanged). JSON Schema → typed JSON via Jev.
  noul_threshold 0.5 decoder not a proof.
  IncompatibleSchemaError lists every bad property.
- **On-device Laya CoreML ANE.** mizorewww/laya-coreml
  (Apache-2.0; **0★**; HEAD `47f4baf0`; README SHA
  `2068c661`). on-device Laya CoreML ANE. ~5 ms P50 short
  decisions. 189/189 FP16 checkpoint parity. 10× not
  achieved. mizorewww/laya-coreml ≠ gliner-native-runtime
  ≠ jevmlx ≠ NandhaKishorM/laya.
- **Local logit `/v1/systemone`.** Micha0827/snapjudge
  (Python MIT; **3★**; HEAD `2df5ce27`; README SHA
  `64a91458`). softmax over allowed tokens ≠ Noul.
  question-first cache. Micha0827/snapjudge ≠
  githubnext/localjev ≠ jevmlx ≠ cendress/SnapJudge.
- **Jev-first Pi agent loop.** direwolfiy/JevPi
  (TypeScript; license null; **0★**; HEAD `980f8895`;
  README SHA `88ec1a55`; GitHub size 0 with contents).
  Jev-first Pi agent loop. slow-LLM fallback. explicit
  action menu / CandidateSource unimplemented. 62 tests
  wiring not quality. direwolfiy/JevPi ≠
  standardagents/jevpilot ≠ pi-jev-control.

Pulse: Archer still NOT landed last pin from §99. Hub
archerhume/4rcherhume HTTP **401**. Tracker likes **51**
flat; lastModified UNCHANGED 2026-09-19T18:37:18Z. Live
REST: SemIf **1954★**; jevlike **989★**; TypeAR **11★**
flat. AnotiaWang/awesome-jev **83★** ≠ Awesomejev
561/27007. `invented_signal: false`.

Cross-repo addition: (lt) judgment-as-language primitive;
(lu) GEPA live-star delta; (lv) retrieve-then-judge
memories; (lw) memory-lease HIGH upgrade; (lx) jevlint
rename; (ly) schema-compiler HIGH upgrade; (lz) ANE /
local-logit / Pi-loop economics.
## Batch #95 (2026-09-20 ~14:10 UTC / ~08:06 Boise) — user-provided HIGH Merve Noyan ZS classifier lineage

User-provided 0806 uniqueness lock: people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 421 / 189; impressions 35498 / 9613; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29.

Note: `research/notes.md` §112. Docs-only on a fresh PR
off main. **HARD RULE:** do not reopen or amend PR #23 or #24 or #25 or #26 or #27 or #28 or #29.
Never reopen merged #7–**#29**. Do **not** re-fold §85 /
§111 / §110 64× Space / JevBench v1.2 board / §78 /
six-gates / §60 / claim-audit / §71. Skip Archer rewrite.
No invented metrics. Hunches labeled. Quote the tweets.
Soft Noul ≠ hard safety. Augustus owns placement.
Institutional HF voice. X MCP used. Quote live REST over
watch. `invented_signal: false`.

- **Category error (PRIMARY pedagogy).** @mervenoyann
  status/2101463303734067592. people who compare Jev against
  GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows.
  Jev vs GPT-5.6 bakeoffs are a category error. encoder / ZS
  classifiers. BERTForXYZ → DeBERTa → ModernBERT. likes **421** /
  impressions **35498**.
- **Skill-issue thesis.** many problems solved with LLMs could
  have been solved with them, it was a skill issue. Mixed
  architecture, not stack replacement.
- **DeBERTa / ModernBERT Hub pointers.** follow-up
  status/2101592535835529527. opt for DeBERTa and ModernBERT ones.
  likes **189** / impressions **9613**. hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0
  likes **139**. hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes **72**.
  bart-large-mnli likes 1616 is **not** her pick.
- **Multimodal ZS perception front-end.** image<>text Transformers
  guide. Perceive, then typed decide. Skip Archer.
- **softmax/ZS ≠ Noul.** Hub widget 0.504/0.479 *theirs*.
  soft scores ≠ hard gates. do not invent accuracy numbers.
  Maziyar quoted: Bart, bert, deberta, modernbert, these are all LLMs.

Pulse: X MCP used ~2026-09-20T14:28Z. Author @mervenoyann
(merve; 92,246 followers). Archer still promised_not_landed.
do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29.
`invented_signal: false`.

Cross-repo addition: (ra) category error Jev vs GPT-5.6;
(rb) skill-issue thesis; (rc) DeBERTa/ModernBERT Hub pointers;
(rd) multimodal ZS perception; (re) softmax/ZS ≠ Noul.

## Batch #94 (2026-09-20 ~12:46 UTC / ~06:46 Boise) — hourly 0646 HIGH

Hourly 0646 uniqueness lock: Calibration is not alpha; NO CURRENT ALPHA CANDIDATE; ΔR² approximately +0.00084; Brier 0.2131387; ECE 0.0421875; Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05; default 0.5 keeps zero non pinned; keepResult median 0.14 to 0.17; keepCall median 0.28 to 0.35; usable range is about 0.10 to 0.25; 7.8% to 57.9%; judges results it never sees; task-finish eval not built yet; $0.002 per compaction; slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench; Jev 108/120 $0.083 0.34 s; Luna SGR 114/120; paired Jev accuracy-difference intervals include zero; not evidence of equivalence; GLM SGR 26/120 93 format failures; Terra-planned Jev hybrid 55/120; rule-based by default, optionally Jev-backed; empty README; missing key cannot break the experience; prefill plus exactly one decode; softmax over A/B/C ≠ Noul; BBQ 9,053/10,000 (90.53%); ECE 0.0890; Mean confidence 0.9943; overconfident; score and noul not implemented; DGUI 12 rows (was 6); INSTRUCT 119 rows likes 2; encode the state once, decide everything in parallel; 0.740 accuracy against a 0.508 majority; ECE 0.047; fine-tune's advantage ends where its 384-token training data does; jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd; Space does not call Jev; recomputes routing from saved probabilities; 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22; synthetic repository benchmark; Jev evaluations are advisory; YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; default threshold 0.8 still soft; 40-line windows cannot prove whole function; token-native sequential start/end Choice; Gemini/Haiku stubs not configured yet; handful of hand-written examples, not a benchmark; Jev judged exactly what it was given; laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills; contract_passed is not a claim of guaranteed factual truth; Wilson lower bound 0.85 floor; fixture mode no savings claim; SemIf 2207★ (+21 vs §110 2186); jevlike 1043★ (+5 vs 1038); TypeAR 15★ (+1 vs 14); AnotiaWang 97★ (+1 vs 96); yibie/awesome-jev 506★ (+16 vs 490); Laya likes 822 (was 802); tracker likes 64 flat, lastModified UNCHANGED; do not reopen or amend PR #23/#24/#25/#26/#27/#28.

Note: `research/notes.md` §111. Docs-only on a fresh PR
off main. **HARD RULE:** do not reopen or amend PR #23 or #24 or #25 or #26 or #27 or #28.
Never reopen merged #7 / **#8** / **#9** /
**#10** / **#12** / **#13** / **#14** / **#15** /
**#16** / **#17** / **#18** / **#19** / **#20** /
**#21** / **#22** / **#23** / **#24** / **#25** / **#26** / **#27** / **#28**. Do **not** re-fold §93 mechanism /
§94 / §95 / §96 / §97 / §98 / §99 / §100 / §101 /
§102 / §103 / §104 / §105 / §106 / §107 / §108 / §109 / §110 / JevBench v1.2 board / §78 /
jev-orderby-bench six-gates / §60 / openJev-verdict claim-audit / §71 /
jev-judge-bench SLA-150 contract / §71 /
yuki-oshio/mini-jev 93.25%. Skip Archer rewrite.
Do **not** re-fold 0541 / 0439 / 0345 / 0243 / 0145 / 0042 / 2340 / 2246 / 2145 / 2041 / 1943 /
1843 / 1740 / gliner-native-runtime / 1639 / 1541. No
invented metrics. Hunches labeled. Quote READMEs. Soft
Noul ≠ hard safety. Augustus owns placement.
Measurement densifies PRIMARY (calibration ≠ alpha,
compaction 0.5 theater, SGR vs native TabFact, one-decode
BBQ overconfidence), datasets/Spaces (encode-once, DGUI 12
rows, jevlogs re-policy), and applied/skills/economics
(mailordinal 200-case, nlgrep, extract, cost-router 0.85
floor) are the *class* exemplars this hour. Quote live REST
over watch. `invented_signal: false`.

- **calibration-is-not-alpha (PRIMARY).** alakise/calibration-is-not-alpha
  (Python MIT; **0★**; HEAD `064b75f5`; size **268**).
  Calibration is not alpha. NO CURRENT ALPHA CANDIDATE.
  ΔR² approximately +0.00084. Brier 0.2131387. ECE 0.0421875.
  Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05.
- **compaction-bench (PRIMARY).** OrMizL/jev-compaction-bench
  (JS MIT; **0★**; HEAD `92fd33e6`; size **35**).
  default 0.5 keeps zero non pinned. keepResult median 0.14 to 0.17.
  keepCall median 0.28 to 0.35. usable range is about 0.10 to 0.25.
  7.8% to 57.9%. judges results it never sees. task-finish eval not built yet.
  $0.002 per compaction.
- **sgr-judge-bench (PRIMARY).** slavadubrov/sgr-judge-bench
  (Python; SPDX NOASSERTION; **0★**; HEAD `5e142707`).
  slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench.
  Jev 108/120 $0.083 0.34 s. Luna SGR 114/120.
  paired Jev accuracy-difference intervals include zero. not evidence of equivalence.
  GLM SGR 26/120 93 format failures. Terra-planned Jev hybrid 55/120.
- **atlas-replay-lab.** elyashium/atlas-replay-lab
  (**0★**; HEAD `9856ab9b`; size **197**).
  rule-based by default, optionally Jev-backed. empty README.
  missing key cannot break the experience.
- **jev-single-decode.** siren2345/jev-single-decode
  (Python MIT; **0★**; HEAD `65df86a3`; size **432**; README SHA `51817d8c` HOLD).
  prefill plus exactly one decode. softmax over A/B/C ≠ Noul.
  BBQ 9,053/10,000 (90.53%). ECE 0.0890. Mean confidence 0.9943.
  overconfident. score and noul not implemented.
- **DGUI densify.** hfdataset ctaxnagomi/DGUI_HYPERMEM-JEV (sha `ab3d3529`).
  DGUI 12 rows (was 6).
- **INSTRUCT densify.** hfdataset ctaxnagomi/INSTRUCT_JEV (sha `b0a09278`).
  INSTRUCT 119 rows likes 2.
- **pngwn encode-once.** hfspace pngwn/open-jev (likes **25**; sha `d41dc3cd`).
  encode the state once, decide everything in parallel.
  0.740 accuracy against a 0.508 majority. ECE 0.047.
  fine-tune's advantage ends where its 384-token training data does.
- **jasonkneen twin.** hfspace jasonkneen/open-jev.
  jasonkneen/open-jev ≠ pngwn/open-jev. same sha d41dc3cd.
- **IkerMoel Space densify.** hfspace IkerMoel/open-alternative-jev (sha `19b104c6`).
- **schema-scorer Space densify.** hfspace mobarmg/jev-schema-scorer (sha `14d35d7e`).
- **jevlogs explorer.** hfspace reachjalil/jevlogs-triage-explorer (sha `dcb785ed`).
  Space does not call Jev. recomputes routing from saved probabilities.
- **financial recorded lab.** IslamBaraka90/jev-typesafe-real-financial-use-cases
  (**0★**; HEAD `9d2eb48c`; size **6168**). Recorded ≠ alpha.
- **mailordinal 200-case densify.** Milo318/mailordinal (**0★**; HEAD `19ea819d`).
  200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22. synthetic repository benchmark.
- **Pleo2 skills.** Pleo2/awesome-jev-agent-skills (**0★**; HEAD `42e3d179`; size **18**).
  Jev evaluations are advisory.
- **nlgrep.** YehuiTang0316/jev-nlgrep (**1★**; HEAD `ceec0d92`; size **6734**).
  YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep.
  default threshold 0.8 still soft. 40-line windows cannot prove whole function.
- **jev-extract.** dangquan1402/jev-extract (**0★**; HEAD `20c2f19f`; size **105**).
  token-native sequential start/end Choice. Gemini/Haiku stubs not configured yet.
- **jyje pilot.** jyje/pilot-typesafeai-jev (**0★**; HEAD `cabd4778`; size **245**).
  handful of hand-written examples, not a benchmark. Jev judged exactly what it was given.
- **laguagu skills sibling.** laguagu/jev-skills (**0★**; HEAD `871ec586`; size **36**).
  laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills.
- **cost-optimizer.** lorensation/llm-cost-optimizer-jev (**0★**; HEAD `db200b7e`; size **227**).
  contract_passed is not a claim of guaranteed factual truth.
  Wilson lower bound 0.85 floor. fixture mode no savings claim.

Pulse: Archer still promised_not_landed. Hub
archerhume/4rcherhume HTTP **401**. Tracker
multimodalart/jev-reproductions-tracker likes **64**;
lastModified `2026-09-20T04:29:16Z` UNCHANGED. Live REST: SemIf
**2207★**; jevlike **1043★**; TypeAR **15★** (+1 vs 14).
AnotiaWang/awesome-jev **97★** ≠ yibie/awesome-jev **506★**.
Hub Laya likes **822**. Blackwood ABSENT. Qwen3.8-27B ≠ Archer.
do not reopen or amend PR #23/#24/#25/#26/#27/#28.
`invented_signal: false`.

Cross-repo addition: (qa) calibration-is-not-alpha PRIMARY;
(qb) compaction-bench PRIMARY; (qc) sgr-judge-bench PRIMARY;
(qd) atlas-replay-lab; (qe) jev-single-decode; (qf) DGUI 12 rows;
(qg) INSTRUCT likes 2; (qh) pngwn encode-once; (qi) jasonkneen twin;
(qj) IkerMoel Space; (qk) schema-scorer Space; (ql) jevlogs explorer;
(qm) financial recorded lab; (qn) mailordinal 200-case; (qo) Pleo2;
(qp) nlgrep; (qq) jev-extract; (qr) jyje; (qs) laguagu skills;
(qt) cost-optimizer 0.85 floor.

## Batch #93 (2026-09-20 ~11:41 UTC / ~05:41 Boise) — hourly 0541 HIGH

Hourly 0541 uniqueness lock: GH jev-haiku-benchmarking 404; ≠ RadRebelSam/awesome-jev; SemIf 2186★ (+20 vs §109 2166); jevlike 1038★ (+7 vs 1031); TypeAR 14★ flat; AnotiaWang 96★ (+1 vs 95); yibie/awesome-jev 490★; Laya likes 802 (was 783); tracker likes 64 flat, lastModified UNCHANGED.

Note: `research/notes.md` §110. Docs-only on a fresh PR
off main. **HARD RULE:** do not reopen or amend PR #23 or #24 or #25 or #26 or #27.
Never reopen merged #7 / **#8** / **#9** /
**#10** / **#12** / **#13** / **#14** / **#15** /
**#16** / **#17** / **#18** / **#19** / **#20** /
**#21** / **#22** / **#23** / **#24** / **#25** / **#26** / **#27**. Do **not** re-fold §93 mechanism /
§94 / §95 / §96 / §97 / §98 / §99 / §100 / §101 /
§102 / §103 / §104 / §105 / §106 / §107 / §108 / §109 / JevBench v1.2 board / §78 /
jev-orderby-bench six-gates / §60 / openJev-verdict claim-audit / §71 /
yuki-oshio/mini-jev 93.25%. Skip Archer rewrite.
Do **not** re-fold 0439 / 0345 / 0243 / 0145 / 0042 / 2340 / 2246 / 2145 / 2041 / 1943 /
1843 / 1740 / gliner-native-runtime / 1639 / 1541. No
invented metrics. Hunches labeled. Quote READMEs. Soft
Noul ≠ hard safety. Augustus owns placement.
Open-weight / RLCD / Blackwood watch (Brier identity,
Independent primitive, CPU twin, LFM NLI, teacher-copy vs
gold vs zeroshot), measurement densifies PRIMARY (jev-bench
ranking ≠ calibration, jev-measured economics), and
applied/theory placements (questionator, grill-jev, jev-lsp,
jev-spec 0.85 theater, Jev-LLM VERIFY) are the *class*
exemplars this hour. Quote live REST over watch.
`invented_signal: false`.

- **Blackwood densify.** hf BlackwoodAI/blackwood-rlcd
  (likes **2**; gated **manual**; sha `3b9e29df`). Blackwood tracker ABSENT; likes 2 gated manual.
- **Qwen3-0.6B RLCD.** hf anthonym21/qwen3-0.6b-rlcd-decision
  (apache-2.0; likes **2**; sha `b327ec5e`). r = c - p_a. ECE 0.021; acc 0.807 vs warmup 0.746.
  calibration beyond ~500 tokens unmeasured.
- **Gemma E2B Independent.** hf larkooo/gemma-e2b-rlcd
  (apache-2.0; likes **1**; sha `e099c730`). Independent primitive.
  11.57s vs 54.10s · 4.67× · 120/128 *theirs*.
  default path is pretrained Gemma probs not trained RLCD head.
- **Hub JEV-CPU twin.** hf Meanblock/JEV-CPU
  (mit; likes **7**; sha `759fa606`). GH Meanblock 404; lock leesk212/JEV-CPU.
  softmax over letter slots ≠ Noul.
- **Mímir LFM.** hf impacte/mimir-lfm-openjev
  (likes **0**; sha `5f9173bb`). WANLI 0.741 vs openjev v2 0.77 *theirs*. 3-way NLI ≠ Noul.
- **System One distilled.** hf shreyanbr/system-one-distilled
  (sha `56c9dba8`). priority 0.464 = majority floor. banking77 contaminated.
  raw margins not probabilities. do not distill Jev as teacher of record (they distilled Haiku).
  Gold `93e22fcf`; zeroshot `4b6659d5`.
- **jev-bench (PRIMARY).** Running-Dolphins/jev-bench
  (Python MIT; **0★**; HEAD `67d2ee42`; size **1070**).
  “0.9 is not one number”. ranking ≠ calibration.
  banking77 0.8–0.9 stated 0.86 actual 0.73 over-confident *theirs*.
  ≠ Praveenrajus/jev-bench ≠ fstandhartinger/jevbench.
- **jev-measured (PRIMARY).** WallerChen/jev-measured
  (Python MIT; **0★**; HEAD `4a12dfb3`).
  $0.0000153–$0.0000226 vs circulating $0.0004 (~20×).
  Score is 0..n-1 expectation not 0–1. Noul has no confidence field.
  TCP floor 198.8 ms. type reliability is not a reason to choose Jev (json_schema 5/5).
  gateway tax not one number.
- **decision-lab.** RadRebelSam/jev-decision-lab
  (TS MIT; **0★**; HEAD `e6d6d42d`; size **128**).
  Function-only 5/8 vs hybrid 8/8. 4/8 without Jev. 8 designed cases not conversion lift.
- **BigQuery pilot.** jackojacko05/compare-jev-bigquery-ai-functions
  (Jupyter MIT; **0★**; HEAD `cb9ef56b`; size **307**).
  200-row pilot Jev 86.5% 173/200 vs Gemini Flash-Lite 86.0% 172/200 vs Pro 87.0% 174/200 *theirs*.
  not a ranking.
- **fighting-ring.** Trecto34/openjev-fighting-ring
  (Python; license null; **0★**; HEAD `ac544f1e`).
  NLI Tetris argmax P(entail)−P(contradict).
- **joshhu 情緒測謊器.** joshhu/jevtest
  (HTML; license null; **0★**; HEAD `6a4df41d`; size **34**).
  情緒測謊器. 1q 396ms / 30q 567ms. ±0.03.
  33q $0.000045 vs Gemini ~5× slower ~60× cost *theirs*. ≠ realZachi/jevtest.
- **aahf Space.** hfspace aahf/JevBenchmark (likes **1**; sha `36c28088`).
  8-example Jev vs GPT-5.6 Sol ~64× cost 5.4× latency *theirs*.
  synthetic; no inference. ≠ JevBench v1.2 §78.
- **rhc98 catalog.** rhc98/awesome-jev (**1★**; HEAD `82898f25`).
  Judged 3317 / listed 2560. Jev judges, code applies policy. catalog ≠ endorsement.
- **APA catalog.** AiPersonacademy/Awesome-jev-use (**2★**; HEAD `29246f12`).
  APA “microsecond policy / zero hallucination” overclaim.
- **questionator.** erseco/questionator (JS MIT; **0★**; HEAD `b498f10b`).
  Client-side quiz; pointer from held docs; scanned-PDF warn. CSP only api.typesafe.ai.
- **grill-jev.** grgy078033/grill-jev (Python MIT; **1★**; HEAD `5ce6cbe8`).
  Jev judges / agent reasons / user decides. selecting an option is not permission to implement.
  degraded fallback.
- **jev-lsp.** makefunstuff/jev-lsp (Rust MIT; **0★**; HEAD `bce3d8ed`).
  pattern exact, judgement must clear floor. no matching pattern → no model call.
  not a correctness oracle. $0.00022 vs chat $0.00306 *theirs*.
- **jev-spec.** nozomi-koborinai/jev-spec (TS MIT; **1★**; HEAD `86f14198`).
  Spec vs artifact remainder. treating 0.85 as 85% / minProbability hard-gate as Harbor.
- **Jev-LLM.** 202620325-spec/Jev-LLM (Python MIT; **0★**; HEAD `da06b6d1`).
  VERIFY acquires discriminating evidence, never same-pool confidence-only rescoring.
  fast/full/max are ceilings not sizes. Solar writes, Jev chooses NEXT ACTION.

Pulse: Archer still promised_not_landed. Hub
archerhume/4rcherhume HTTP **401**. Tracker
multimodalart/jev-reproductions-tracker likes **64**;
lastModified `2026-09-20T04:29:16Z` UNCHANGED. Live REST: SemIf
**2186★**; jevlike **1038★**; TypeAR **14★** flat.
AnotiaWang/awesome-jev **96★** ≠ yibie/awesome-jev **490★**.
Hub Laya likes **802**. Blackwood ABSENT. Qwen3.8-27B ≠ Archer.
do not reopen or amend PR #23/#24/#25/#26/#27.
`invented_signal: false`.

Cross-repo addition: (qa) Blackwood densify; (qb) eve-rlcd Brier;
(qc) Gemma E2B Independent; (qd) Hub JEV-CPU twin; (qe) Mímir LFM;
(qf) system-one distilled/gold/zeroshot; (qg) jev-bench PRIMARY;
(qh) jev-measured PRIMARY; (qi) decision-lab; (qj) BQ 200-row;
(qk) fighting-ring; (ql) joshhu 情緒測謊器; (qm) aahf Space;
(qn) rhc98; (qo) APA; (qp) questionator; (qq) grill-jev;
(qr) jev-lsp; (qs) jev-spec; (qt) Jev-LLM.

## Batch #92 (2026-09-20 ~10:39 UTC / ~04:39 Boise) — hourly 0439 HIGH

Note: `research/notes.md` §109. Docs-only on a fresh PR
off main. **HARD RULE:** do not reopen or amend PR #23 or #24 or #25 or #26.
Never reopen merged #7 / **#8** / **#9** /
**#10** / **#12** / **#13** / **#14** / **#15** /
**#16** / **#17** / **#18** / **#19** / **#20** /
**#21** / **#22** / **#23** / **#24** / **#25** / **#26**. Do **not** re-fold §93 mechanism /
§94 / §95 / §96 / §97 / §98 / §99 / §100 / §101 /
§102 / §103 / §104 / §105 / §106 / §107 / §108 / JevBench v1.2 board / §78 /
jev-orderby-bench six-gates / §60 / openJev-verdict claim-audit / §71 /
yuki-oshio/mini-jev 93.25%. Skip Archer rewrite.
Do **not** re-fold 0345 / 0243 / 0145 / 0042 / 2340 / 2246 / 2145 / 2041 / 1943 /
1843 / 1740 / gliner-native-runtime / 1639 / 1541. No
invented metrics. Hunches labeled. Quote READMEs. Soft
Noul ≠ hard safety. Augustus owns placement.
Open reproduction densifies (Gemma-4 jevify Hub cards that
ship weights, bonzi 1.7/4/8 v1 family fill, ultra_laya REVIEW),
measurement densifies PRIMARY (cyrillic-audit XNLI/RU), and
applied class placements (table-tennis, evidence-lab,
pointer-not-generator, jevgraph, J++, paper-trader honest
negative) are the *class* exemplars this hour. Quote live REST
over watch. `invented_signal: false`.

- **Gemma-4 26B-A4B jevify.** hf kushalpatil/jevify-gemma4-26b-a4b
  (license gemma; likes **0**; sha `d4c0d1d4`). Hub jevify merged LoRA ships weights.
  PAWS 0.580/ece 0.288 is the weak cell. ≠ Mintzs/jevify. GH kushalpatil07/jevify 404.
- **26B-A4B LoRA twin.** hf kushalpatil/jevify-gemma4-26b-a4b-lora
  (license null; likes **0**; sha `ec4a3d22`). LoRA adapter twin not independent eval.
- **Gemma-4 E4B jevify.** hf kushalpatil/jevify-gemma4-e4b
  (license gemma; likes **0**; sha `a6b5a716`). smaller E4B slightly better OOD ECE than 26B-A4B.
- **E4B LoRA stub.** hf kushalpatil/jevify-gemma4-e4b-lora
  (license null; likes **0**; sha `cca1f55e`). E4B LoRA stub card.
- **Bonsai-8B v1.** hf NicolaiMTLassen/bonzi-8b-v1-jev
  (MIT; likes **0**; sha `588bc44e`). WANLI-256 64.5% *theirs*. rank #4 of 6.
- **Bonsai-1.7B v1.** hf NicolaiMTLassen/bonzi-1.7b-v1-jev
  (MIT; likes **0**; sha `48148bf9`). WANLI-256 52.0% *theirs*. rank #6 of 6.
- **Bonsai-4B v1.** hf NicolaiMTLassen/bonzi-4b-v1-jev
  (MIT; likes **0**; sha `d5545084`). WANLI-256 60.2% *theirs*. rank #5 of 6.
- **JulesHuisman scaffolding.** JulesHuisman/jev-eval
  (Python; license null; **0★**; HEAD `96c2a110`; README SHA `c356a584` (was empty `e69de29b`)).
  JulesHuisman/jev-eval scaffolding / README SHA c356a584 (was empty e69de29b).
- **Table-tennis.** LiuHao-1443/jev-table-tennis
  (Python MIT; **1★**; HEAD `0224c21c`). 7 bands 6/10 vs 40 bands 0/10.
- **Evidence lab.** laguagu/jev-evidence-lab
  (Python MIT; **0★**; HEAD `a9669e94`). 32/32 synthetic is smoke not production.
- **hfjev.** hemanth/hfjev (Python MIT; **1★**; HEAD `6f2aa501`).
  classify HF datasets across typed semantic dimensions.
- **ultra_laya.** roadius2/ultra_laya
  (Python Apache-2.0; **0★**; HEAD `0dff5bd2`).
  roadus2 watch misspelling; lock roadius2/ultra_laya. ultra_laya REVIEW defects.
- **RU calibration audit (PRIMARY).** AHTOOOXA/jev-cyrillic-audit
  (Python MIT; **0★**; HEAD `7167894a`).
  XNLI EN 88.3% ECE 0.032 → RU 77.3% ECE 0.096.
  Δ −11.0 pp [−14.2,−7.8]; ECE +0.063.
  MASSIVE no detectable difference at n=600.
  confidence is function of p_max (r=1.000).
- **jev-llm.** akash-kamat/jev-llm (JS; license null; **0★**; HEAD `194db1a6`).
  pointer-not-generator 400 human-authored responses.
- **jevgraph.** chenmingtang830/jevgraph
  (Python Apache-2.0; **0★**; HEAD `7a6f7d05`).
  proposed ≠ authorized. FewRel 160: Jev 85.0% vs lexical 13.125%.
  gated 100% (95/95) coverage 59.375%.
- **J++.** Towow-ai/jpp (Python MIT; **3★**; HEAD `14d77789`).
  J++ composable semantic computation language.
- **judge-jev.** Mishkun/judge-jev (TS; license null; **0★**; HEAD `1bf495d3`).
  judge-jev 0.5 still soft.
- **what-is-jev.** tunahansahin897/what-is-jev
  (Python; SPDX NOASSERTION; **0★**; HEAD `71d53be2`).
  947 repos scored; A 273 / B 302 / C 372. LLM rubric ≠ benches.
- **whyashthakker gallery.** whyashthakker/awesome-jev-use-cases
  (HTML MIT; **3★**; HEAD `74583663`). No benchmark winner is claimed.
- **dog-last guide.** dog-last/awesome-jev (Python MIT; **1★**; HEAD `206fdcab`).
  phishing: naive 62.6% vs regex 91.8%; 5-atomic + LR 95.0% *theirs*.
- **AITuber.** shinshin86/jev-aituber-tension-sample
  (TS MIT; **0★**; HEAD `8c0a8ffb`). AITuber tension ±15.
- **shinpr reranker.** shinpr/jev-reranker (Rust MIT; **1★**; HEAD `731deba3`).
  README npm global; repo is Rust.
- **git-confess.** AHTOOOXA/git-confess (Python MIT; **0★**; HEAD `54cd2849`).
  git-confess code owns counting/blame/ratio. httpx exhibit 11% (13/119) *theirs*.
- **paper-trader.** waterme7on/jev-paper-trader
  (JS; license null; **0★**; HEAD `73662f79`).
  90d trend +12.40% vs random +12.75% vs BH +41.71%. 5m win rate 25%.

Pulse: Archer still promised_not_landed. Hub
archerhume/4rcherhume HTTP **401**. Tracker
multimodalart/jev-reproductions-tracker likes **64**;
lastModified `2026-09-20T04:29:16Z` UNCHANGED. Live REST: SemIf
**2166★**; jevlike **1031★**; TypeAR **14★**.
AnotiaWang/awesome-jev **95★** ≠ Awesomejev 656 entries / 38,160 stars.
Hub Laya likes **783**. Blackwood ABSENT. Qwen3.8-27B ≠ Archer.
do not reopen or amend PR #23 or #24 or #25 or #26.
`invented_signal: false`.

Cross-repo addition: (pb) jevify 26B-A4B; (pc) 26B LoRA twin;
(pd) jevify E4B; (pe) E4B LoRA stub; (pf) bonzi-8b-v1;
(pg) bonzi-1.7b-v1; (ph) bonzi-4b-v1; (pi) JulesHuisman scaffolding;
(pj) table-tennis; (pk) evidence-lab; (pl) hfjev; (pm) ultra_laya;
(pn) cyrillic-audit PRIMARY; (po) jev-llm; (pp) jevgraph; (pq) jpp;
(pr) judge-jev; (ps) what-is-jev; (pt) whyashthakker; (pu) dog-last;
(pv) aituber; (pw) shinpr; (px) git-confess; (py) paper-trader.

## Batch #91 (2026-09-20 ~09:45 UTC / ~03:45 Boise) — hourly 0345 HIGH

Note: `research/notes.md` §108. Docs-only on a fresh PR
off main. **HARD RULE:** do not reopen or amend PR #23 or #24 or #25.
Never reopen merged #7 / **#8** / **#9** /
**#10** / **#12** / **#13** / **#14** / **#15** /
**#16** / **#17** / **#18** / **#19** / **#20** /
**#21** / **#22** / **#23** / **#24** / **#25**. Do **not** re-fold §93 mechanism /
§94 / §95 / §96 / §97 / §98 / §99 / §100 / §101 /
§102 / §103 / §104 / §105 / §106 / §107 / JevBench v1.2 board / §78 /
jev-orderby-bench six-gates / §60 / openJev-verdict claim-audit / §71 /
yuki-oshio/mini-jev 93.25%. Skip Archer rewrite.
Do **not** re-fold 0243 / 0145 / 0042 / 2340 / 2246 / 2145 / 2041 / 1943 /
1843 / 1740 / gliner-native-runtime / 1639 / 1541. No
invented metrics. Hunches labeled. Quote READMEs. Soft
Noul ≠ hard safety. Augustus owns placement.
Open reproduction densifies (bonzi GGUF family, HF verdict
twin, OpenJev Vision + dataset, Laya ONNX WebGPU, mini-jev
transfer) and measurement densifies PRIMARY (injection-bench
11.9k, dspy-bench, AbstentionBench-on-Jev, openkev, pdf-race,
flopcheck, Laya calibration lab, jev-atlas) are the *class*
exemplars this hour. Quote live REST over watch.
`invented_signal: false`.

- **Bonsai 27B v2 family card.** hf NicolaiMTLassen/bonzi-27b-v2-jev
  (MIT; likes **0**; sha `c4d21b74`). Hub still does not ship weights.
  WANLI-256 74.6% *theirs*. ternary still needs PrismML fork.
- **Ternary Bonsai 8B family card.** hf NicolaiMTLassen/bonzi-8b-ternary-v1-jev
  (MIT; likes **0**; sha `47b66187`). WANLI-256 65.2% *theirs*.
- **Bonsai 1 27B family card.** hf NicolaiMTLassen/bonzi-27b-v1-jev
  (MIT; likes **0**; sha `2fb8061a`). Bonsai 1 27B Q1_0 runs on stock llama.cpp.
  WANLI-256 71.1% *theirs*. Do not collapse into §107 Q2_0 gibberish.
- **Laya multilingual ONNX WebGPU.** hf mizchi/laya-multilingual-onnx
  (apache-2.0; likes **0**; sha `b6314ec9`). ships model.onnx 646.9MB.
  63/63 selected answers / 5.1e-4 CPU / 1.2e-2 WebGPU. Independent port.
- **OpenJev Vision.** hf IamBusy/OpenJev-Vision (license other; likes **0**; sha `8cf6cbd3`).
  OpenJev Vision image classification + uncertainty. CLEVR-4 held-out joint 0%.
- **HF verdict twin.** hf heman10x/openJev-verdict-2.0 (apache-2.0; likes **5**; sha `794d5e0d`).
  twin tokenizer-only. likes **5** ≠ GH **107★**. do not re-fold §71 as a beat.
- **Vision research dataset.** hfdataset IamBusy/OpenJev-Vision-Research-v0.1
  (license other; likes **0**; sha `43e49184`). 12,832 images.
  294,912 derived targets not independent samples.
- **mini-jev residual-head densify.** UpHash-Network/mini-jev
  (Python MIT; **0★**; HEAD `52fbae12`; README SHA `363441b6`).
  UpHash-Network/mini-jev is yuki-oshio transfer.
  residual-head 9,222-param decreased 73/96→67/96.
- **Prompt-injection ranking vs calibration (PRIMARY).** ASEVlad/jev-injection-bench
  (Python MIT; **0★**; HEAD `c0d0f25d`; README SHA `1b28498c`; size **107**).
  11,900 labelled prompts. Jev best ranking / Haiku better ECE 0.021 vs 0.058.
  0.5–0.9 band is where Jev's numbers do not mean what they say.
  Prompt wording moves panic 28%.
- **Jev vs DSPy quality-evaluator.** manojlds/jev-dspy-bench
  (Python Apache-2.0; **0★**; HEAD `d8c68d72`; README SHA `16100deb`).
  Jev agreement is similarity, never ground truth.
  no aggregate quality grade or merge gate.
  manojlds/jev-dspy-bench ≠ dspachos/jev-dspy ≠ jmanhype/jev-dspy-lab.
- **AbstentionBench-on-Jev.** sshariqali/jev-abstentionbench
  (Python; README MIT / SPDX NOASSERTION; **0★**; HEAD `f5c0c068`).
  rank 1 of 20 vs 2025 field. question-asymmetry.
  forward-looking 0.465 never extreme.
- **openkev calibration layer.** misakaikato/openkev
  (Python MIT; **0★**; HEAD `babcab1c`; README SHA `974d97f9`).
  openkev calibration layer not a runtime. ECE vs coverage independent.
  select_threshold returns inf. escalation catches uncertainty not ignorance.
  misakaikato/openkev ≠ jaredpalmer/kev.
- **Docling→Jev vs Gemini race.** goodrahstar/pdf-race
  (JS MIT; **0★**; HEAD `1c687fc6`; README SHA `05730787`).
  parser owns the wall clock. 12/12 tie is a tie. titles selected not generated.
- **Public TypeSafe JEV index.** ZeroX-01/jev-atlas
  (JS; license null; **0★**; HEAD `bc94bf50`).
  ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas.
  catalog not endorsement.
- **flopcheck tweet judgments.** samyakjain0606/jev-is-here
  (TS; license null; **0★**; HEAD `eb0de0ba`).
  flopcheck 16 calibrated tweet judgments. mechanical tells in code.
- **Laya calibration lab.** hfspace BunsDev/laya-calibration-lab
  (apache-2.0; likes **0**; sha `a3fc13ba`).
  T never changes argmax. confidence ≠ top-label p.
  easy probe set refused. 40–48 rows too small to ship T.

Pulse: Archer still NOT landed. Hub
archerhume/4rcherhume HTTP **401**. Tracker
multimodalart/jev-reproductions-tracker likes **60**;
lastModified `2026-09-20T04:29:16Z` UNCHANGED. Live REST: SemIf
**2128★**; jevlike **1026★**; TypeAR **12★** **flat**.
AnotiaWang/awesome-jev **94★** ≠ Awesomejev 561/27007.
Hub Laya likes **765**. Qwen3.8-27B ≠ Archer.
do not reopen or amend PR #23 or #24 or #25.
`invented_signal: false`.

Cross-repo addition: (ol) bonzi-27b-v2 family; (om) ternary-8b;
(on) 27b-v1 stock Q1_0; (oo) Laya ONNX WebGPU; (op) OpenJev Vision;
(oq) HF verdict twin tokenizer-only; (or) Vision-Research-v0.1;
(os) mini-jev transfer; (ot) injection-bench PRIMARY; (ou) dspy-bench;
(ov) AbstentionBench-on-Jev; (ow) openkev; (ox) pdf-race;
(oy) jev-atlas; (oz) flopcheck; (pa) Laya calibration lab.

## Batch #90 (2026-09-20 ~08:43 UTC / ~02:43 Boise) — hourly 0243 HIGH

Note: `research/notes.md` §107. Docs-only on a fresh PR
off main. **HARD RULE:** do not reopen or amend PR #23 or #24.
Never reopen merged #7 / **#8** / **#9** /
**#10** / **#12** / **#13** / **#14** / **#15** /
**#16** / **#17** / **#18** / **#19** / **#20** /
**#21** / **#22** / **#23** / **#24**. Do **not** re-fold §93 mechanism /
§94 / §95 / §96 / §97 / §98 / §99 / §100 / §101 /
§102 / §103 / §104 / §105 / §106 / JevBench v1.2 board / §78 /
jev-orderby-bench six-gates / §60 / openJev-verdict claim-audit / §71. Skip Archer rewrite.
Do **not** re-fold 0145 / 0042 / 2340 / 2246 / 2145 / 2041 / 1943 /
1843 / 1740 / gliner-native-runtime / 1639 / 1541. No
invented metrics. Hunches labeled. Quote READMEs. Soft
Noul ≠ hard safety. Augustus owns placement.
Measurement densifies (router benches, ticket/figure
routers, human-labeled feedstock) are the *class*
exemplar this hour. Quote live REST over watch.
`invented_signal: false`.

- **Benchmark-driven router + judge (PRIMARY).**
  erendikmenn/jev-llm-router-benchmark (Python MIT; **0★**; HEAD `f44ef450`;
  README SHA `df3687e5`; GitHub size 0 with contents).
  Benchmark-driven Jev router and judge. cheap alone is not success.
  Jev does not write, sum prices, or claim accuracy %.
  Sol 94.2 / Luna 83.9 / Jev path 89.7.
  19.2% Sol / 62.3% cost save / 4.5pp miss of 2pp non-inferiority.
  p50 latency worse than Sol due to routing overhead.
  erendikmenn/jev-llm-router-benchmark ≠ jev-rag-benchmark ≠ ryantsai/jev-llm-router.
- **Support ticket router.** aesaganda/jev-ticket-router
  (JS; license null; **0★**; HEAD `ecf00046`; README SHA `41c0b50f`; size **0** with contents).
  Express + node:sqlite. mock and Jev decision engines.
  previous_ticket_count >= 3 is code. MIN_CONFIDENCE 0.6 still soft.
  substring false positives.
  aesaganda/jev-ticket-router ≠ SarathChandraBellam/jev-vs-llm-ticket-router.
- **Universal figure router.** hoangngochuong24947-gif/jev-figure-router
  (Python MIT; **1★**; HEAD `4c51b1af`; README SHA `11d5302b`; size **340**).
  Universal Figure & Diagram Router. confidence ≥ 0.85 hard-gate is theater.
  generative AI banned from scientific plots. six visual branches.
- **Human-labeled feedstock.** hfdataset Praveenrajus/jev-bench
  (license other; likes **0**; sha `c9c3032c`).
  human-labeled (state, question, label). 166,054 rows / 22 configs.
  soft_label for human uncertainty. Praveenrajus/jev-bench ≠ fstandhartinger/jevbench.
- **Ternary bonsai GGUF.** hf NicolaiMTLassen/open-bonzi-jev
  (MIT; likes **0**; sha `09240156`). ternary bonsai System One GGUF.
  openjev's mechanism, Bonsai's weights. Hub does not ship weights.
  100/100 easy T/F is not Harbor. label_mass ≠ correctness.
  stock llama.cpp Q2_0 silently gibberish.
  NicolaiMTLassen/open-bonzi-jev ≠ NicolaiLassen.
  GH companion NicolaiLassen/open-bonzi-jev (Python MIT; **0★**; HEAD `1c2508fd`).
- **DeBERTa ONNX t.js port.** onnx-community/open-jev-deberta-v3-large-ONNX
  (apache-2.0; likes **0**; sha `3bc2553b`). transformers.js DeBERTa ONNX.
  source:com-kotobalabs/open-jev-deberta-v3-large. temperature 1.05.
  AutoModel from_pretrained works.
  onnx-community/open-jev-deberta-v3-large-ONNX ≠ system-one-qwen3.5-4b-scorer-ONNX.
- **verdict NAR densify.** Heman10x-NGU/openJev-verdict-2.0
  (Python; README Apache-2.0 / GitHub SPDX NOASSERTION; **107★**;
  HEAD `a458733c`; README SHA `05ca75af`; size **14728**).
  107★ densify. GH 151M vs README 149.6M. PR #1 now closed unmerged.
  do not re-fold §71 claim-audit as a beat.
- **Study notes densify.** wjdjdakf17/jev-study (TypeScript MIT; **0★**;
  HEAD `24b5d7d7`; README SHA `4ca30c93`; size **34**; default **master**).
  typed decisions, RLCD, confidence-gated routing. structured ≠ correct.
  mock not live API. 26 tests. wjdjdakf17/jev-study ≠ baekenough/jev-study.

Pulse: Archer still NOT landed. Hub
archerhume/4rcherhume HTTP **401**. Tracker
multimodalart/jev-reproductions-tracker likes **59**;
lastModified `2026-09-20T04:29:16Z` UNCHANGED. Live REST: SemIf
**2094★**; jevlike **1023★**; TypeAR **12★** **flat**.
AnotiaWang/awesome-jev **93★** ≠ Awesomejev 561/27007.
Hub Laya likes **729**. Qwen3.8-27B ≠ Archer.
do not reopen or amend PR #23 or #24.
`invented_signal: false`.

Cross-repo addition: (od) router bench PRIMARY; (oe) ticket mock+Jev;
(of) figure router 0.85 theater; (og) jev-bench feedstock;
(oh) ternary bonsai GGUF; (oi) DeBERTa ONNX t.js; (oj) verdict 107★ densify;
(ok) study RLCD + confidence-gated routing.

## Batch #89 (2026-09-20 ~07:45 UTC / ~01:45 Boise) — hourly 0145 HIGH

Note: `research/notes.md` §106. Docs-only on a fresh PR
off main. **HARD RULE:** do not reopen or amend PR #23.
Never reopen merged #7 / **#8** / **#9** /
**#10** / **#12** / **#13** / **#14** / **#15** /
**#16** / **#17** / **#18** / **#19** / **#20** /
**#21** / **#22** / **#23**. Do **not** re-fold §93 mechanism /
§94 / §95 / §96 / §97 / §98 / §99 / §100 / §101 /
§102 / §103 / §104 / §105 / JevBench v1.2 board / §78 /
jev-orderby-bench six-gates / §60. Skip Archer rewrite.
Do **not** re-fold 0042 / 2340 / 2246 / 2145 / 2041 / 1943 /
1843 / 1740 / gliner-native-runtime / 1639 / 1541. No
invented metrics. Hunches labeled. Quote READMEs. Soft
Noul ≠ hard safety. Augustus owns placement.
Architecture probes (train-or-local recipes) are the
*class* exemplar this hour. Quote live REST over watch.
`invented_signal: false`.

- **Jevify-any-LLM architecture probe (PRIMARY).**
  uspraveen/Jevify (license null; **0★**; HEAD `0f29d783`;
  README SHA `32608473`; GitHub size 0). Turn any open LLM into System-One Jev.
  uspraveen/Jevify ≠ Mintzs/jevify ≠ gulagala001/jevify.
  Jevify-any-LLM architecture probe. description-only stub / size 0.
- **Encoder-only from a task sentence.** Ruivalim/exu-base
  (Python MIT; **1★**; HEAD `7288cdca`; README SHA `45244838`; size **180**).
  Train encoder-only calibrated decision models from a task sentence.
  Exu is a toolkit, not a method. strictly proper scoring rule. Pre-alpha.
- **Scratch-trained recipe upgrade.** Colvin0315/MiniSystemOne
  (Python Apache-2.0; **0★**; HEAD `d7f9f803`; README SHA `a5b0d2fd`; size **814**).
  scratch-trained calibrated decision model. typed Q → probability dists.
  Colvin0315/MiniSystemOne ≠ hyusi2003/MiniSystemOne.
  no published weights download URL. 90.5 seconds / 29.2% pipeline evidence.
  p_i/p_j independent of other candidates.
- **Recipe small model out.** scienthoon/luce (Python Apache-2.0; **1★**;
  HEAD `8072b97d`; README SHA `5fbe226d`; size **10833**).
  Recipe for calibrated decision models — small model out.
  init → synth → train → eval → serve. 91.1 % / ECE 0.022 *theirs*.
  Jev zero-shot 75.1.
- **Headline claims trial.** RichardoMrMu/jev-mini (Python MIT; **0★**;
  HEAD `5adef5dc`; README SHA `154ae8b0`; size **0** with contents).
  Put Jev's three headline claims on trial. 0.5B local GPU.
  46x speedup / accuracy identical. ECE 0.624 sentiment catastrophe.
  bigger model worse calibration. RichardoMrMu/jev-mini ≠ yuki-oshio/mini-jev ≠ r-ms/mini-jev.
- **Local structured-choice engine.** tapsin/jev-local (Python; license null; **0★**;
  HEAD `96aac2a1`; README SHA `4d728cbf`; default **master**).
  System-1 decision engine for local LLMs. structured choices only.
  JSON parse of generated text ≠ Noul. TypefAI JEV / Journal Entry Voucher.
  tapsin/jev-local ≠ us/jev-local ≠ Argos1111/jev_local.
- **Reward-model 8-track.** goya4140/jev-reward-model-evaluation
  (Python MIT; **0★**; HEAD `f16a06d1`; README SHA `603587fd`).
  Jev 1.13 reward-model eval across 8 benchmark tracks.
  40,940 examples / 0 API errors. RewardBench v1 92.58%. Precise IF 50.63%.
- **Ticket-router scaffold.** SarathChandraBellam/jev-vs-llm-ticket-router
  (license null; **0★**; HEAD `0318ad72`; README SHA `8223dd6f`).
  Jev vs LLM support-ticket routing. Scaffolding in progress.
- **Cost bench.** Shilin237/jev-vs-llm-cost (HTML; license null; **0★**;
  HEAD `2d4bd6a9`; README SHA `f4e98bbf`). static + live decision bench.
  TypeSafe's own published benchmark. illustrative simulations, not live API calls.
- **JevBench v1.2.3 densify.** fstandhartinger/jevbench (Python MIT; **6★**;
  HEAD `c7ab99f5`; README SHA `8fe07c41`; size **8907**).
  JevBench v1 — smart/cheap/fast/reliable. I/C/S/K 25% geometric mean.
  classifier.dev fast tier 84.8 is Jev behind its own API.
  do not re-fold §78 v1.2 board as new. Laya (421M) 70.1 now on board.
- **Budget-in-code remainder.** AIGNLAI/ReflexRoute (Python MIT; **1★**;
  HEAD `5f475d80`; README SHA `6a1ae694`). Zero-shot/few-shot LLM routing.
  hard budget filter before Jev. Jev never asked to perform budget arithmetic.
- **XState compose.** priyankark/jev-state (TypeScript MIT; **0★**;
  HEAD `c73aef65`; README SHA `15410dbe`).
  Jev judges the next state, XState enforces transitions.
  simulation uses synthetic keyword fixtures.
- **Consistency Space.** hfspace mjyoke1111/jev-consistency-benchmark
  (apache-2.0; likes **0**). Consistency benchmark Space.
  This Space contains no benchmark result yet. 12-case plumbing fixture.
- **Catalog gravity.** v-modal/awesome-jev-tools (license null; **339★**;
  HEAD `f117e0c3`; README SHA `8ea9a669`; size **83**).
  catalog gravity. ★339 live REST. curation is not endorsement.
- **Crawler directory.** RadRebelSam/awesome-jev (JavaScript SPDX NOASSERTION; **0★**;
  HEAD `27629954`; README SHA `21ec8d51`; LICENSE SHA `2aa7fe23`; size **919**).
  crawler-maintained directory. Daily GitHub + npm sweep, human-merged.
  RadRebelSam/awesome-jev ≠ AnotiaWang ≠ yibie ≠ cobanov ≠ logicrw ≠ v-modal.
- **HF peft reranker.** rdxtremity/jev-reranking (apache-2.0; likes **0**; sha `cae796ea`).
  HF peft SPLADE/BGE reranker. rdxtremity/jev-reranking ≠ carlaiau/jev-reranking.
  query-side encoders, not a Jev replica.
- **ONNX scorer port.** onnx-community/system-one-qwen3.5-4b-scorer-ONNX
  (CC-BY-NC-4.0; likes **0**; sha `fa0bed22`). ONNX System One Qwen3.5-4B scorer.
  source:pngwn/system-one-qwen3.5-4b-scorer. temperature 1.75.
  transformers.js AutoModel cannot load this graph.

Pulse: Archer still NOT landed. Hub
archerhume/4rcherhume HTTP **401**. Tracker
multimodalart/jev-reproductions-tracker likes **59**;
lastModified `2026-09-20T04:29:16Z` UNCHANGED. Live REST: SemIf
**2074★**; jevlike **1022★**; TypeAR **12★** **flat**.
AnotiaWang/awesome-jev **92★** ≠ Awesomejev 561/27007 ≠
logicrw **146★** ≠ v-modal **339★**. Qwen3.8-27B ≠ Archer.
do not reopen or amend PR #23.
`invented_signal: false`.

Cross-repo addition: (nm) Jevify-any-LLM probe; (nn) encoder-only
task-sentence toolkit; (no) Colvin recipe upgrade; (np) luce recipe;
(nq) headline-claims trial; (nr) local JSON≠Noul; (ns) RM 8-track;
(nt) ticket-router scaffold; (nu) cost bench; (nv) JevBench densify;
(nw) budget-in-code; (nx) XState compose; (ny) consistency plumbing;
(nz) catalog gravity; (oa) crawler directory; (ob) SPLADE/BGE port;
(oc) ONNX scorer port.

## Batch #88 (2026-09-20 ~06:42 UTC / ~00:42 Boise) — hourly 0042 HIGH

Note: `research/notes.md` §105. Docs-only on a fresh PR
off main. Never reopen merged #7 / **#8** / **#9** /
**#10** / **#12** / **#13** / **#14** / **#15** /
**#16** / **#17** / **#18** / **#19** / **#20** /
**#21** / **#22**. After merged #22 (`98ded82`, hourly
2340 / `notes.md` §104). Do **not** merge from merged
**#22**. Do **not** re-fold §93 mechanism / §94 / §95 /
§96 / §97 / §98 / §99 / §100 / §101 / §102 / §103 / §104.
Skip Archer rewrite. Do **not** re-fold 2340 / 2246 /
2145 / 2041 / 1943 / 1843 / 1740 /
gliner-native-runtime / 1639 / 1541. No invented
metrics. Hunches labeled. Quote READMEs. Soft Noul ≠
hard safety. Augustus owns placement. Seeing the
distribution, measuring the instrument, and refusing to
hard-gate a soft Noul as safety are the *class*
exemplar this hour. Quote live REST over watch.
`invented_signal: false`.

- **Structured probability readouts (PRIMARY).**
  Arohtea/jev-readout (JavaScript; license null; README
  MIT; **0★**; HEAD `6f1e5900`; README SHA `67ee1e96`;
  GitHub size **44** (relock; was **0** with contents)).
  structured probability
  readouts. distribution > argmax. Noul 0.5 midpoint.
  score is expectation not integer. bare HTTP not SDK.
  Arohtea/jev-readout.
- **Ordinary-model Jev-shape.** gulagala001/jevify
  (JavaScript MIT; **0★**; HEAD `3d3e904a`; README SHA
  `0e2f8536`; GitHub size **145** (relock; was **0** with
  contents)). Jev-style Choice/Score/Noul from ordinary
  models. optional DSH plugin. schema-valid ≠ calibrated.
  gulagala001/jevify ≠ Mintzs/jevify.
- **Open-weight Laya measurement.**
  mourad-ghafiri/laya-rlcd-benchmark (Python; license
  null; **0★**; HEAD `3401ff26`; README SHA `d8d4859e`;
  GitHub size **164** (relock; was **0** with contents)).
  Laya RLCD benchmark. 40.3% below constant-answer.
  open-weight measurement.
  mourad-ghafiri/laya-rlcd-benchmark ≠ yibie/laya-jev-lab.
- **Cheap fail-open semantic edge.**
  SupremeDreamZ/jev-fastloop (Python MIT; **0★**; HEAD
  `1157841a`; README SHA `053a0885`; GitHub size **12**
  (relock; was **0** with contents)). cheap fail-open
  semantic edge. second signal not sole. FastLoopError
  catch. SupremeDreamZ/jev-fastloop ≠ jev-ultrafast.
- **Fan-out measurement.** TheWebDevel/jev-fanout
  (Python MIT; **0★**; HEAD `b30aaadc`; README SHA
  `394b2e1e`; GitHub size **206** (relock; was **0** with
  contents)). asking more questions in one call. 0.980
  at every N. nearly not fully deterministic.
  TheWebDevel/jev-fanout.
- **VLM+Jev RL teacher.** harneet2512/reflexrl (Python
  MIT; **0★**; HEAD `aa36be84`; README SHA `e6ff13cd`;
  default master; GitHub size **749** (relock; was **0**
  with contents)). Qwen3-VL perception + Jev decisions
  train RL. 0 model calls at deployment. VLM alone 1.7
  vs +Jev 4.4. harneet2512/reflexrl ≠
  khordoo/jev-reflex-autonomy-lab.
- **Independent Jev API vs Laya.** yibie/laya-jev-lab
  (Python MIT; **0★**; HEAD `30ba64dc`; README SHA
  `57bd1832`). independent Jev API vs Laya. cascade 0.60
  matches 78% at 1.8×. noul facts not judgements.
  yibie/laya-jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab.
- **Locate vs decide.** umstek/zero-shot-ie-bench
  (Python MIT; **0★**; HEAD `8770b16b`; README SHA
  `d69dc96a`; size **50** (relock; was **33**)). GLiNER vs GLiFormer vs Laya vs
  Jev. extractors ≠ decision engines. Laya
  dict-instructions collapse 58.3%.
  umstek/zero-shot-ie-bench.
- **Throughput arena.** angelgalvisc/snake-arena-jev-vs-llms
  (Python MIT; **0★**; HEAD `985a1c70`; README SHA
  `0db6f528`; size 194). decisions-per-minute & cost.
  204 moves vs 73. throughput not intelligence.
  angelgalvisc/snake-arena-jev-vs-llms ≠
  vtrivedy/jev-plays-games.
- **Behavioral contracts.** sathariels/jevcheck
  (Python MIT; **0★**; HEAD `fc49c795`; README SHA
  `5c832f81`; size 117). behavioral contracts. pin
  expectations eval upgrades. raw 0.94 is not a release.
  sathariels/jevcheck ≠ dayhaysoos/jevals ≠
  SivletLabs/jev-eval.
- **Evidence-linked upgrade review.**
  GaneshVG18/upgrade-radar (TypeScript MIT; **0★**; HEAD
  `e438f9bd`; README SHA `c32f7d18`; GitHub size **908**
  (relock; was **0** with contents)). evidence-linked
  dependency upgrade. Jev never generates filenames.
  no_direct_evidence ≠ safe to merge.
  GaneshVG18/upgrade-radar ≠ LYchoon/paper-radar-jev.
- **Knowledge-work discography.** lirantal/discoprint
  (TypeScript Apache-2.0; **0★**; HEAD `a9d3294f`;
  README SHA `9a64f473`; GitHub size **239** (relock; was
  **0** with contents)). discography
  theme/mood/complexity. five atomic questions one call.
  lirantal/discoprint.

Pulse (independent review relock after `0558f7d`): Archer still NOT landed. Hub
archerhume/4rcherhume HTTP **401**. Tracker likes **59**
(+3 vs §104 **56**); lastModified
`2026-09-20T04:29:16Z` **UNCHANGED** vs §104. Laya Hub likes **705**.
Blackwood Hub likes **2** gated manual — user census
absent from tracker. Live REST: SemIf **2069★**; jevlike
**1022★**; TypeAR **12★** flat. AnotiaWang/awesome-jev
**92★** ≠ Awesomejev 561/27007 ≠ yibie/awesome-jev
**450★**. Qwen3.8-27B ≠ Archer
(likes **15796**). `invented_signal: false`.

Cross-repo addition: (nb) structured probability
readouts; (nc) ordinary-model Jev-shape; (nd) open-weight
constant-answer bench; (ne) fail-open second-signal
edge; (nf) packed fan-out measurement; (ng) perceive≠
decide≠deploy RL; (nh) local-first cascade; (ni) locate
vs decide; (nj) decisions-per-minute arena; (nk)
behavioral pin-then-eval; (nl) evidence-linked remainder;
(nm) knowledge-work discography.

## Batch #87 (2026-09-20 ~05:40 UTC / ~23:40 Boise) — hourly 2340 HIGH

Note: `research/notes.md` §104. Docs-only on a fresh PR
off main. Never reopen merged #7 / **#8** / **#9** /
**#10** / **#12** / **#13** / **#14** / **#15** /
**#16** / **#17** / **#18** / **#19** / **#20** /
**#21**. Do **not** re-fold §93 mechanism / §94 / §95 /
§96 / §97 / §98 / §99 / §100 / §101 / §102 / §103 /
jev-orderby-bench six-gates / §60. Skip Archer rewrite.
Do **not** re-fold 2246 / 2145 / 2041 / 1943 / 1843 /
1740 / gliner-native-runtime / 1639 / 1541. No invented
metrics. Hunches labeled. Quote READMEs. Soft Noul ≠
hard safety. Augustus owns placement. From-scratch tiny
decision training is the *class* exemplar this hour.
Quote live REST over watch.
`invented_signal: false`.

- **From-scratch calibrated decision model (PRIMARY).**
  hyusi2003/MiniSystemOne (Apache-2.0; **0★**;
  HEAD `4385335b`; README SHA `83016bf8`; GitHub size 5).
  train calibrated ~27M from scratch. typed Q→prob dist / one forward pass / no LLM decode.
  hyusi2003/MiniSystemOne ≠ Colvin0315/MiniSystemOne.
  description-only stub / size 5.
- **ORDER BY ranking upgrade.** yodablocks/jev-orderby-bench
  (Python MIT; **0★**; HEAD `52397954`; README SHA
  `7bd075c3`; size **309**). ESCI hard probe fails four of six.
  jev_bool ECE 0.242 inversion 0.255. do not re-fold §60 six-gates as new.
- **Find/design/evaluate decision loops.** karanb192/jev-architect
  (HTML MIT; **0★**; HEAD `35ea6d93`; README SHA `68c2b5f9`).
  find/design/evaluate TypeSafe Jev decision loops.
  karanb192/jev-architect ≠ samtay32/jev-system-architect.
- **Distill-Jev UI stub.** Jairik/jev-distiller (MIT; **0★**;
  HEAD `0589d44c`; README SHA `aa408c5e`). Jairik/jev-distiller size 1.
  distill-Jev UI stub / do not distill Jev as teacher of record.
- **Post-launch scored opportunity map.** licensedsaucer9-web/jev-opportunities
  (license null; **0★**; HEAD `a47fa414`; README SHA `aa33f901`).
  post-launch scored use-case map / Jev self-scores then human curation.
- **Jev-inize a use case.** gavinHuang/jevinize (MIT; **0★**;
  HEAD `6d080632`; README SHA `5f48e622`).
  Jev-inize a use case into classifier/router.
  gavinHuang/jevinize → simple-jev not TypeSafe.
- **Saved-decision regression.** VihaanAgarwal/jev-diff
  (Python MIT; **0★**; HEAD `a3c98807`; README SHA `3b0ce75c`).
  compare saved decisions / same label can still change the branch.
  not tested with a live Jev API key.
- **Constrained-logprob API.** zhangcy122/OpenJevPro
  (HTML; SPDX NOASSERTION; **0★**; HEAD `94d77bcb`; README SHA `50c77ace`).
  constrained logprob + temp/Platt ≠ Noul.
  OpenJevPro pastes openjev-sglang JevBench as own. PolyForm Noncommercial.
- **SmolLM RLCD reproduction.** patelvishwa112/jev-system-one-rlcd
  (Python; license null; **0★**; HEAD `62b103b3`; README SHA `55994d69`).
  SmolLM-135M / sub-70ms / 0 output tokens.
  demo P(True) 0.5052 / Choice conf 0.2872 / Score conf 0.0055.
- **Source-backed Awesome radar.** logicrw/awesome-jev-projects
  (JavaScript MIT; **136★**; HEAD `97057cc1`; README SHA `25a19b31`).
  source-backed Awesome Jev radar / 306+ commit-pinned.
  auto GitHub sync / Issue-only submissions.
- **Rival-aware one-pass scorer.** olanotolu/jevbetter
  (Python MIT; **12★**; HEAD `bb0ebc82`; README SHA `5cbe01d4`).
  hashed n-gram encoder / rival-aware attention.
  olanotolu/jevbetter vs jevlike starter.
  shuffled-context control 0.335.

Pulse: Archer still NOT landed. Hub
archerhume/4rcherhume HTTP **401**. Tracker
multimodalart/jev-reproductions-tracker likes **56**;
lastModified `2026-09-20T04:29:16Z`. Live REST: SemIf
**2047★**; jevlike **1018★**; TypeAR **12★** **flat**.
AnotiaWang/awesome-jev **91★** ≠ Awesomejev 561/27007 ≠
logicrw **136★**. Qwen3.8-27B ≠ Archer.
`invented_signal: false`.

Cross-repo addition: (nb) from-scratch decision head;
(nc) ORDER BY ESCI upgrade; (nd) decision-loop skill;
(ne) distill-Jev UI stub; (nf) scored opportunity map;
(ng) Jev-inize scaffold; (nh) saved-decision regression;
(ni) constrained-logprob API; (nj) SmolLM RLCD;
(nk) source-backed Awesome radar; (nl) rival-aware scorer.

## Batch #86 (2026-09-20 ~04:46 UTC / ~22:46 Boise) — hourly 2246 HIGH

Note: `research/notes.md` §103. Docs-only on a fresh PR
off main. Never reopen merged #7 / **#8** / **#9** /
**#10** / **#12** / **#13** / **#14** / **#15** /
**#16** / **#17** / **#18** / **#19** / **#20**. Do
**not** re-fold §93 mechanism / §94 / §95 / §96 / §97 /
§98 / §99 / §100 / §101 / §102. Skip Archer rewrite. Do
**not** re-fold 2145 / 2041 / 1943 / 1843 / 1740 /
gliner-native-runtime / 1639 / 1541. No invented metrics.
Hunches labeled. Quote READMEs. Soft Noul ≠ hard safety.
Augustus owns placement. Independent evidence catalogs
and negative results are the *class* exemplar this hour.
Quote live REST over watch.
`invented_signal: false`.

- **Independent System One evidence catalog (PRIMARY).**
  reachjalil/system-one-bench (JavaScript MIT; **0★**;
  HEAD `ceb17269`; README SHA `d9e0c7b7`; GitHub size 90).
  independent System One evidence catalog. 19 reviewed
  records. scores not one leaderboard. no external record currently
  reproduced. TokenTrim no-Jev matched hybrid 62.4%.
  reachjalil/system-one-bench ≠ mallahyari/system-one-benchmark.
- **Typed eval freeze.** SivletLabs/jev-eval (Python MIT;
  **0★**; HEAD `3f9d976f`; README SHA `df16766c`).
  21 tasks · 134 items · 208 questions. scenes from public
  GitHub contracts, not production logs.
  SivletLabs/jev-eval ≠ willkelly/jev-evaluation ≠
  4esv/jev-eval ≠ xxkuboxx/jev-eval ≠ onlyoneaman/jev-eval ≠
  dayhaysoos/jevals.
- **Option-isolated tiny replica.** nafisazizir/hev
  (Python Apache-2.0; **0★**; HEAD `79a486f9`; README SHA
  `b995dce3`). option isolation (sibling-blind).
  permutation-equivariant. Hub OWNER not published.
  nafisazizir/hev ≠ jaredpalmer/kev.
- **Frozen-LLM typed decisions.** yuki-oshio/mini-jev
  (Python MIT; **0★**; HEAD `dff5b323`; README SHA
  `363441b6`; GitHub size **38370**). frozen local LLM logits, no trained
  decision head. residual-head 9,222-param decreased
  73/96→67/96. confidence = 1−normalized entropy, not
  P(correct). yuki-oshio/mini-jev ≠ r-ms/mini-jev.
- **AR next-token anti-pattern.** erik-dunteman/ChatJev
  (Python; license null; **1★**; HEAD `ea33ab8d`; README
  SHA `c763be19`). Jev classifier as autoregressive
  next-token predictor. ChatJev-style soundness theater.
  erik-dunteman/ChatJev ≠ dannote/jev ≠ jev-gpt.
- **Formal compose with scoring.**
  wufuju2023-cell/jev-alpha-proof-analysis (Markdown;
  license null; **0★**; HEAD `afd9bb6f`; README SHA
  `1810d7f6`). calibrated decision head × AlphaProof value
  head. implementation-layer isomorphism, semantic
  difference. timeout = censoring. do not launder Noul as
  proof.
- **Parallel rank vs serial selection.** zzzzzec/jevsort
  (HTML; license null; **1★**; HEAD `57067b90`; README SHA
  `85044740`). parallel rank-prediction vs serial
  selection. independent questions can conflict.
  zzzzzec/jevsort ≠ keltokhy/jsort.
- **Open-side ecosystem catalog.**
  rupeshpoojary9/awesome-open-system-one (CC0 1.0; SPDX
  NOASSERTION; **0★**; HEAD `637ee3d3`; README SHA
  `0007e343`; GitHub size **4**). curated open System One ecosystem catalog.
  rupeshpoojary9/awesome-open-system-one ≠
  AnotiaWang/awesome-jev.
- **Knowledge-work paper radar.** LYchoon/paper-radar-jev
  (Python MIT; **0★**; HEAD `fbadf01c`; README SHA
  `1cb8a9c3`; size **73**; default master). arXiv paper
  radar with Jev relevance scoring. ranking ≠ calibration
  / 0.5 still soft. fail-open failed evals not marked seen.

Pulse: Archer still NOT landed. Hub
archerhume/4rcherhume HTTP **401**. Tracker likes **54**;
lastModified `2026-09-20T02:59:13Z`. Live REST (review
relock): SemIf **2019★**; jevlike **1006★** (+4 vs §102
1002); TypeAR **12★** **flat**. AnotiaWang/awesome-jev
**87★** (+1 vs §102 **86**) ≠ Awesomejev 561/27007. Qwen3.8-27B ≠ Archer.
`invented_signal: false`.

Cross-repo addition: (ms) independent evidence catalog;
(mt) typed eval freeze; (mu) option-isolated replica;
(mv) frozen-LLM logit-read; (mw) AR next-token
anti-pattern; (mx) scoring × proof-search; (my) parallel
rank vs serial; (mz) open-side catalog; (na) paper radar.

## Batch #85 (2026-09-20 ~03:45 UTC / ~21:45 Boise) — hourly 2145 HIGH

Note: `research/notes.md` §102. Docs-only on a fresh PR
off main. Never reopen merged #7 / **#8** / **#9** /
**#10** / **#12** / **#13** / **#14** / **#15** /
**#16** / **#17** / **#18** / **#19**. Do **not** re-fold
§93 mechanism / §94 / §95 / §96 / §97 / §98 / §99 /
§100 / §101. Skip Archer rewrite. Do **not** re-fold 2041
/ 1943 / 1843 / 1740 / gliner-native-runtime / 1639 /
1541. No invented metrics. Hunches labeled. Quote
READMEs. Soft Noul ≠ hard safety. Augustus owns
placement. Open-weights Laya is the *class* exemplar this
hour. Quote live REST over watch.
`invented_signal: false`.

- **Question-linting of Jev questions themselves (PRIMARY).**
  yodablocks/jevq (Python MIT; **0★**; HEAD `40b2dd90`;
  README SHA `3198dde0`; GitHub size 0 with contents).
  question-linting of Jev questions themselves. nine
  jaggedness rules, no API key, no labelled data. static
  lint ≠ measured separation. yodablocks/jevq ≠ tenbin ≠
  JevLint ≠ commitjev.
- **Open-weights Laya as class exemplar (binding).**
  ChristianAlexander/laya_ex (Elixir Apache-2.0; **0★**;
  HEAD `99f9ce73`; README SHA `6361c920`). Nx/Bumblebee
  runtime. host chooses backend. ChristianAlexander/laya_ex
  ≠ system_one_sdk ≠ dannote/jev ≠ NandhaKishorM/laya.
- **On-chain/edge Laya deploy.** humandebri/IC-Laya
  (Rust MIT; **0★**; HEAD `055ef42f`; README SHA
  `85431606`). parity_verified stays false. model output
  never grants Tx. humandebri/IC-Laya ≠ laya_ex.
- **Auditable weekend replica.** agilabs-ai/jev48
  (Python MIT; **0★**; HEAD `aa697005`; README SHA
  `3f667dd4`). Jev outputs never used for training.
  unpaired 0.577 vs 0.727. agilabs-ai/jev48 ≠ JevBench ≠
  Mapika/decider.
- **Adversarial dual-judge / framing.** copyleftdev/ember
  (TypeScript MIT; **0★**; HEAD `c02f622b`; README SHA
  `6db00b56`). comparative framing is the usable judgment.
  prior injection crowds out evidence. copyleftdev/ember ≠
  ember.js.
- **Laya specialist + Hub replica.** PIXELZX0/XERON
  (Python; license null; **0★**; HEAD `5e870a4d`) training
  still GPU-pending. daliborsb/laya Hub replica drop ≠
  convaiinnovations/laya ≠ NandhaKishorM/laya.
- **Distillation economics.** MagaBitmex/jev-4b-distill-data
  gold is programmatic; teacher is closed-API clone; do
  not distill Jev as teacher of record; student checkpoint
  missing.
- **Non-LLM VIN System One.** lewislululu/jevon (HF AGPL;
  likes 3). planning depth not chat. lewislululu/jevon ≠
  douglance/jevon.
- **Source-bound evidence.** WaynezProg/jev-kit (MIT;
  **0★**; HEAD `4558554f`; README SHA `a7f14838`). local
  quote mismatch needs no API. exit 0 ≠ claim truth.
  WaynezProg/jev-kit ≠ jonathanavis96/jev-kit (Airlock) ≠ jev-use ≠ jev-mcp.

Pulse: Archer still NOT landed. Hub
archerhume/4rcherhume HTTP **401**. Tracker likes **54**;
lastModified `2026-09-20T02:59:13Z`. Live REST (review relock): SemIf
**2000★**; jevlike **1002★** flat; TypeAR **12★** (+1 vs §101 11).
AnotiaWang/awesome-jev **86★** ≠ Awesomejev 561/27007.
Qwen3.8-27B ≠ Archer. `invented_signal: false`.

Cross-repo addition: (mj) question-lint of questions;
(mk) open Laya BEAM binding; (ml) on-chain/edge deploy;
(mm) weekend replica honesty; (mn) dual-judge framing;
(mo) Laya specialist + Hub replica; (mp) distill corpus
≠ teacher-of-record; (mq) non-LLM VIN; (mr) source-bound
evidence.

## Batch #84 (2026-09-20 ~02:41 UTC / ~20:41 Boise) — hourly 2041 HIGH

Note: `research/notes.md` §101. Docs-only on a fresh PR
off main. Never reopen merged #7 / **#8** / **#9** /
**#10** / **#12** / **#13** / **#14** / **#15** /
**#16** / **#17** / **#18**. Do **not** re-fold §93
mechanism / §94 / §95 / §96 / §97 / §98 / §99 / §100.
Skip Archer rewrite. Do **not** re-fold 1943 / 1843 /
1740 / gliner-native-runtime / 1639 / 1541. No invented
metrics. Hunches labeled. Quote READMEs. Soft Noul ≠
hard safety. Augustus owns placement. rh-guard owns
injection/steer. Quote live REST over watch.
`invented_signal: false`.

- **Resume-screening bias audit (PRIMARY).**
  natemoo-re/bias-bench (JavaScript; license null; **0★**;
  HEAD `fe2f2535`; README SHA `a1c3e604`; GitHub size 0
  with contents). resume-screening bias audit methodology.
  name×resume factorial independent Nouls. callback
  determined by resume quality. mean-probability name
  gaps operationally negligible. natemoo-re/bias-bench ≠
  BBQ.
- **MCDA panel + code-owned verdict.**
  austindixson/planalyzer (Python MIT; **0★**; HEAD
  `39fc161f`; README SHA `6e4d8da3`). Plan/PRD panel →
  code-owned pass|review|block. cheerleading out of
  scope. austindixson/planalyzer ≠ single-goodness Noul.
- **EU cost-aware routing.** cannacre8ive/switchboard-ai
  (JavaScript MIT; **1★**; HEAD `5cae9d1c`; README SHA
  `872de837`; package 0.4.0). cost-aware multi-model
  routing/escalation. decide vs do. successful-task cost.
  cannacre8ive/switchboard-ai ≠ ha-switchboard ≠
  hermes-switchyard.
- **Frozen-protocol class bake-off.**
  elcronos/jev-vs-open-decision-models (Python; license
  null; **0★**; HEAD `b61e6cfc`; README SHA `b7256888`).
  frozen-protocol zero-shot bench. TypeSafe Jev vs
  PrismNLI vs Laya. contamination caveat.
  elcronos/jev-vs-open-decision-models ≠ JevBench ≠ DMB.
- **VOI admission.** cvsgireesh/jevusher (TypeScript MIT;
  **0★**; HEAD `d830d344`; README SHA `428a4a59`).
  context-window admission control. VOI gate which tokens
  are worth the expensive model. fail polarity per lens.
  on small inputs lenses lose money. cvsgireesh/jevusher ≠
  jev-sift ≠ winnow.
- **Typed decision control plane.** MokiMeow/jev-fabric
  (TypeScript Apache-2.0; **0★**; HEAD `95b9a4f3`; README
  SHA `f485dbdd`). typed decision control plane. receipt ≠
  authorization. historical-v0 zero retained cases.
  MokiMeow/jev-fabric ≠ jev-forge ≠ dgp.
- **Scoring economics.** jose-troche/live-rubric
  (TypeScript; license null; **0★**; HEAD `db8da8db`;
  README SHA `4a0be084`). live 15-dim typed rubric
  re-score per pause. scoring economics exemplar.
  OpenJev/Codiv ≠ TypeSafe hosted. jose-troche/live-rubric
  ~$0.000004 desc / ~$0.000006 README.
- **Pre-registered calibration science.**
  willkelly/jev-evaluation (Python MIT; **0★**; HEAD
  `c168c093`; README SHA `2d66ac22`). adversarial
  pre-registered Jev eval. 28 predictions before data.
  123,805 requests. confidence does not track ignorance.
  polite injection 65% / crude 0%. willkelly/jev-evaluation
  ≠ jevals ≠ jev-baselines-eval. rh-guard owns injection.
- **Class infrastructure SDK.** nshkrdotcom/system_one_sdk
  (Elixir MIT; **0★**; HEAD `c2a522ee`; README SHA
  `c117b4c4`; mix 0.5.0). provider-neutral Elixir/BEAM
  Noul/Choice/Score SDK. class infrastructure.
  nshkrdotcom/system_one_sdk ≠ typesafe_sdk ≠ dannote/jev.

Pulse: Archer still NOT landed. Hub
archerhume/4rcherhume HTTP **401**. Tracker likes **54**
(+3 vs §100 pin **51**); lastModified **CHANGED**
2026-09-20T02:59:13Z. Live REST: SemIf **1984★**; jevlike
**1002★**; TypeAR **11★** flat. AnotiaWang/awesome-jev
**84★** ≠ Awesomejev 561/27007. `invented_signal: false`.

Cross-repo addition: (ma) resume-audit methodology;
(mb) code-owned MCDA panel; (mc) cost-aware S1/S2
routing; (md) frozen-protocol bake-off; (me) VOI
admission; (mf) typed control plane; (mg) scoring
economics; (mh) pre-registered eval; (mi) BEAM class
SDK.

