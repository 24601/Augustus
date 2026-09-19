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
  2026-09-19T03:18:28Z; 0★. AND/OR/NOT line Nouls; JP↔EN.
  Precision 0.94 / recall 0.98 *theirs*.
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
