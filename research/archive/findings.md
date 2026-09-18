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
