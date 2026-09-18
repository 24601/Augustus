# JEV research notes (baseline 2026-09-18)

## 1. What Jev is — contract facts (re-verify live before building)

- System One model: sends back **typed decisions, not text**. `POST
  https://api.typesafe.ai/v1/systemone`, body `{state, model, questions}`.
  SDKs: `typesafe-sdk` (Python 3.10+), `@typesafe-ai/sdk` (Node 20+).
  Default model alias `jev-latest` currently resolves to `jev-1.13.0`;
  **pin the version** (`model="jev-1.13.0"`) when thresholds are tuned, and
  log the response's `model` field.
- Three primitives. **Choice**: one of a fixed set, up to **255 options**,
  returns `choice` + full `probabilities` + `confidence`. Always add an
  explicit `other`/`none of the above` when coverage is uncertain. **Score**:
  position on 2–10 ordered, concretely described levels; returns fractional
  `score` (probability-weighted mean of level indices) + `probabilities` +
  `confidence` + `legend`. **Noul**: yes/no as a single probability
  `noul` in [0,1]; **no confidence field** — the number is the belief.
  Noul 0.5 = uncertainty between yes/no, NOT medium intensity.
- Parallelism: every question in one request sees the same state, is
  evaluated independently, costs only its tokens. Context: ~64k tokens for
  state + all questions, ~32k for state + longest question. Speculative
  questions are nearly free in latency (13-question cookbook: 12.2x cheaper,
  10.0x faster batched, answers identical).
- Performance envelope (TypeSafe's self-run numbers, unreproduced):
  70–500ms end-to-end, $0.042/MTok input, output free, ~$0.0004/case.
  Rate limits jev-1.13: 250k tokens/s, 1200 req/min, `429` + `retry-after`,
  SDKs retry with backoff. Limits move without notice.
- Training: RLCD (Reinforcement Learning for Calibrated Decisions), 2 years
  stealth, founder Diogo Almeida (ex-OpenAI, InstructGPT/RLHF lineage),
  ~$40M led by DCVC. Eval claim: 67.8% on 4 internal workflows, level with
  GPT-5.6 Terra at ~1/200 cost, ~1/50 latency — measured as agreement with a
  GPT-6 Astra + Fable 5.1 consensus, NOT ground-truth accuracy. Treat as a
  lead, not a fact.
- "Hallucination-free" means: output is always schema-valid (0% type
  errors by construction). It can still return the WRONG valid value.

## 2. Design patterns (empirical recipes, dated)

- Speculative fan-out (docs/patterns/fan-out + parallel_questions cookbook,
  2026-09): ask everything possibly-needed in one call; code ignores what
  doesn't apply. Second requests ONLY when the next state/options depend on
  an earlier answer (skill_suggestion top-3 refetch, autoformat block
  building, hierarchical beam descent).
- Confidence-gated routing: one threshold PER ACTION scaled to cost of being
  wrong (floor ~0.5 unsure → human; read-only acts low; money/safety acts
  high + confirm). Tune on own data; plot confidence vs accuracy.
- Composite scoring (docs/primitives/score#splitting): split fuzzy judgment
  into atomic one-dimension Scores, normalize each by its top level index,
  weight in code. Re-weighting is a code change, not a re-prompt.
- Cascades: Jev routes/filters cheaply → code handles the deterministic
  majority → frontier LLM takes the hard minority → human takes the
  uncertain tail. 1kpapers: $3.99 summarize + $0.08 classify for 1018 papers.
- Retrieve-then-judge: Jev knows ONLY the state it is handed. Retrieval
  quality ceilings everything; filter state to what each question needs
  (context rot is real and measured).
- Hierarchy/beam search (cookbook, jev-1.12, 4 labeled examples): parallel
  beam K=3 over Choice distributions with geometric-mean path score beat
  greedy 4/4 vs 2/4. Mechanism demo, not a general superiority proof.
- Skill suggestion (cookbook, jev-1.12, 488 requests): rank-182 Choice +
  gate nouls in ONE request, rerank top-3 with fits-nouls in a second;
  wrong loads 16.8%→7.3%, needless 9.8%→4.0%. THE canonical answer to
  "hundreds of micro-skills vs one fat skill": keep a full roster, add a
  cheap Jev rank-then-verify front door, suggest at most one skill per turn,
  allow rejection. Choice settles WHICH, nouls settle WHETHER.
- Rubric discipline: levels must describe concrete situations, never bare
  degrees or "worse than previous" (levels are judged independently, numbers
  invisible). Structured criteria objects (`what`/`not_for`/`examples`) with
  same field names across options; examples must resemble real inputs.
  Same Score, different risk: [0,1,0] vs [0.5,0,0.5] both score 1.0 —
  always read probabilities + confidence beside the score.

## 3. Jaggedness — official failure modes (jev-1.13, reviewed 2026-09-16)

Literal reading (answers what you wrote, not what you meant); no counting /
math / numeric interpolation between Score levels (iterate per-item Nouls in
code, keep arithmetic in code); dates are text (extract parts via Choice with
explicit not-stated, assemble/compare in code); indirection/double-negatives
cost accuracy (name state paths with backticks); large irrelevant state
distracts (filter first, Noul-relevance pre-filter); state is NOT treated as
hostile (prompt injection moves answers — your threat model); contradictory
instructions/criteria confuse (align them); NO generation (candidates from
regex/LLM/code, Jev selects).

## 4. Ecosystem (launch week, stars as of 2026-09-17/18 — re-check)

- typesafe-ai/skills (official agent skill, MIT): live-docs-as-source-of-truth
  protocol. Our skill LAYERS on top, never duplicates it.
- typesafe-ai/typesafe-sdk-python, typesafe-sdk-js (official clients);
  system-one-adapter-python (same typed interface over OpenAI/Anthropic).
- browser-use/jev-ultrafast (~2100★, 2026-09-16): dynamic indexed action
  space, operation+target heads in ONE request (speculative targets), small
  LLM only for TYPE_TEXT; 7.1s Flights demo, $0.0039; 1092→101 browser calls.
- jarrodwatts/jev-trader (453★, 2026-09-16): per-Monad-block buy/sell Choice,
  ~81ms model latency, 2-RPC hot loop, dry-run mode.
- devagrawal09/jev-review: staged code review (Noul risk matrix →
  Choice/Score file profiles → evidence → severity → routing) + dashboard.
- TheoLeeCJ/openjev (40-166★): open-model interface-pattern reproduction
  (direct logits, 4B model) — pattern only, not the model/training.
- vinnylarouge/jevlike: Jev-like one-pass option probabilities + Doom/chess
  vision demos with tensor diagrams.
- awlevin/typesafe-computer-use: $0.0002/step vs $0.032 Opus; key caveat:
  "every piece of reasoning the frontier model does for free has to be
  rebuilt here as deterministic state" (OCR + explicit date parsing).
- RomanSlack/jev-drone: 500Hz control + 50Hz safety in code, classical CV to
  symbols at 15Hz, Jev advisory ~2.5Hz (Choice maneuver + Score risk + Noul
  lost-vs-occluded). "Cannot be the perception layer or run at control rate."
- fhshaik/typesafe-mario: emulator RAM → object JSON → legal-action Choice,
  no screenshots. phyous/tsai-sc: 421 Jev decisions through StarCraft
  campaign with verification report.
- Community clients: s1-rs / typesafe-rs (Rust), typesafe_sdk (Elixir),
  Ruby, .NET, Rails, Advocaat (TS), HA-Jev (Home Assistant), pi-typesafe +
  pi-warden (Pi guardrails), jev-mcp / typesafe-mcp (MCP servers), jev-axi
  (AXI CLI: its own benchmark found agents read fewer files but cost the
  same — judgments, not reading replacement), jev-mobile (Android PoC),
  Bicameral (LLM writes, Jev reflexes), Every (per-function Noul code
  search), Crowdcheck (10k synthetic personas demo), HEIST//ONE (stealth
  game, 6 guards batched), TypeSafe Typewriter (16 live judgments demo).
- Evals/research: jev-rerank-bench, jev-spam-eval (zero-shot vs TF-IDF +
  post-hoc caveats), typesafe-ai-benchmark (Jev vs Qwen-on-Cerebras),
  pjburnhill gist (6-question Jev suitability test: judgement/bounded/
  context-contained/fast-human/machine-consumed).
- AbdelStark/awesome-typesafe (45★): curated index, labels private-data and
  single-run caveats, last reviewed 2026-09-17. Start hourly refresh here.

## 5. X launch signal (via web index 2026-09-18; X API creds absent)

Founder thread (@CompleteSkeptic, Sep 15): RLCD, 20-200x faster, 40-400x
cheaper. @typesafeai out-of-stealth + waitlist. TestingCatalog, AGTPinsights
summaries. Trending: Browser Use + Jev flights ($0.0039, 7s). Vercel AI
Gateway listing. Builder anecdotes: flight search, email sorting, trading
bot, 1018-paper classification. Sentiment: excitement + "different primitive,
not cheaper LLM". No verified independent benchmarks yet.

## 6. Coverage gaps / unknowns

- No independent reproduction of TypeSafe's own speed/cost/quality claims.
  MCTS+Jev now FOUND and analyzed: paulobueno164/jev-mcts + lhemerly/mcts-agent
  (see §8 and mappings.md empirical recipe); supersedes the earlier
  "not yet observed" note — MCTS-as-value-function is EMPIRICAL, pending
  third-party reproduction.
- 255-option Choice at scale (>255 candidates) has no canonical public
  recipe; tournament-bracket decomposition is UNPROVEN (see skill warnings).
- Score cross-question comparability and calibration on deployment
  populations: unmeasured. Thresholds from cookbooks are examples, not rules.
- Prices/limits/aliases will move; evals page (evals.typesafe.ai) and
  Discord #show-and-tell are the fastest-moving sources — check every pass.

## 7. Additions from 2026-09-18 refresh (marked new)

### Agent self-supervision is the strongest emerging pattern
- Foreman (203★): "wide generative loop + narrow supervisory loop" run concurrently; the supervisor estimates named probabilities (implementation_complete .91, tests_sufficient .34, worker_stuck .02, ready_to_finish .21) and deterministic policy with hysteresis gates continue/stop/retry/verify. Treat as semantic state estimation, NOT command generation.
- winnow + yoshi + fast-jev-compaction: judge artifact RELEVANCE before it enters context (one Noul per block/span); hide confident-no with a stub + recall key; keep current instruction, recent turns, errors, opaque blocks always.
- pi-jev / pi-warden / jev-judgment: gate actions BEFORE execution (destructive, exfil, beyond-scope, impact) with per-action thresholds; judge output AFTER execution (leaks_secret, failure_class); all error paths fail-open; shadow mode first.
- Structure: pre-action gate → post-action output judge → done-check (claim "done" without a passing test = block) → stuck-detector (3 same-strategy failures) → slop/done judgments on final reply.

### Skill routing/modularity (updates §2)
- SkillRanker (23★): ranks skills from live session context via hook; local feedback + calibration loop; context windowing drops reasoning blocks/prior advice; explicit fail-closed paths.
- DECRUX router: chunk 240/request, gate=mean of 3 judgments ≥0.30, winner 'fits' noul ≥0.40, shortlist 3, 700-char excerpt per candidate, two requests, opt-in, nothing injected when nothing fits.
- GodsBoy router: route/no_skill/review tri-state; 94.4% vs 70.8% lexical on 72 synthetic requests; exploratory caveat: questions revised after inspecting first full run (tuning leakage — note the practice, don't copy it silently).
- Modularity conclusion stands: full roster of small skills + cheap Jev rank-then-verify front door; frontmatter description IS the routing payload — write it for a 700-character excerpt and one-second judgment.

### Statistical discipline numbers
- Calibration holds near-distribution (ECE 0.0313, Archer Hume) but collapses out of distribution: 32% accuracy + 0.30 mean top-prob on novel 2-step word problems → Jev flags uncertainty instead of reasoning through it. Rule: never use Jev where the judgment requires a derivation; decompose until each question is observational.
- Same Score ≠ same quality: [0,1,0] vs [0.5,0,0.5] both 1.0 (§1) — always read probabilities + confidence together.
- Open-model reverse engineering (openjev, openjev-sglang, jevmlx, NanoJev, reflex): consensus that the pattern is prefill-once + read typed option logits directly, no generation. Consistent with parallel fan-out behavior; treat as hypothesis about the closed model.

## 8. Topic-index pass (2026-09-18, ~80 more repos; archive = 184 clones)

- **Jev-as-a-judge, judge variance (danielgshea/jev-as-a-judge)**: 100 judge
  repetitions over 5 frozen agent outputs. Jev judge's ratings varied 224x
  LESS (quality metric) and 279x LESS (rubric) than a GPT judge's; outcome
  disagreement 0% vs 0.2%. Recipe: before trusting any judge (Jev or LLM),
  run repeated judgments over frozen outputs and compare spread, not just
  agreement. This is the measured basis for using Jev to test skills.
- **ndolinschi family (toolgate, harnessjudge, trustgate, swarmrouter,
  mcpmatch...)**: allow/ask_human/deny for planned tool calls; ok/retry/
  escalate/stop for agent steps — same gate vocabulary as pi-jev/pi-warden;
  a whole suite built on one judgment shape.
- **inanna-malick/jev-dsl (Haskell)**: questions written as typed packets,
  type-inferred, answers returned under the same labels as records; every
  answer consumed through a handler per alternative. Good reference for
  "callability": the branch that runs is always one the program wrote.
- **shamazharikh/qwen-rlcd (Qwen3.5-0.8B reproduction)**: mechanism =
  prefill state once, copy cache per branch, run every question+answer
  branch as one padded batch, read hidden state at last real token.
  Branches isolated by construction in both linear-attention and full
  attention layers → results cannot depend on question/option order.
  Confirms the openjev prefill-only hypothesis; hybrid-layer detail
  (18 DeltaNet + 6 attention) explains why naive tree masks fail.
- **awesome-jev-by-typesafe (410★)**: 18-case use-case map + production
  decision loop (inspect → evaluate → compose → gate → record → calibrate)
  and an explicit "what Jev is not" list. Already mirrored in skill; new
  only as: record-the-version step belongs in every decision card.

## 9. Optimizer/framework support (2026-09-18)
- ax-llm/ax: native `ai({name:'typesafe'})` signature adapter (boolean->Noul
  w/ trueThreshold local policy; class->Choice) + `typesafe().systemOne()`
  native client. TS-only (AxIR backlog). Adapter fails closed pre-network on
  optional/array/nested/numeric/freeform outputs; no streaming/temp/samples.
- DSPy: typesafeainate/dspy-typesafeify — @typesafeify(score_fields=...) reads
  signature output annotations (bool/Literal/score) and builds a hybrid plan:
  one Typesafe request for typed fields, generative LM after for freeform.
  PoC only; optimizer-aware tuning of thresholds NOT built.
- jev-dspy-lab: the measurement discipline for any such integration —
  dataset calibration w/ bootstrap CIs, selective-risk sweep, fail-closed
  abstention, canonical request hashes, confirmatory gate chosen pre-run
  (never report best sweep row).
- Skill: added references/optimizer-integration.md + index row.

## 10. Toolbox-mapping meta-method added to skill (2026-09-18)
New references/toolbox-mapping.md: the repeatable procedure for finding
approaches/applications for an out-of-distribution primitive — inventory a
classical toolbox family, locate its judgment-shaped component (answer in a
second, closed answer space, no derivation), substitute Jev, classify the win
(marginal substitute / newly-feasible via the 100-150x economics / invalid),
then falsify. Seeded table maps ~11 families to launch-week evidence; the
economics inversion ("what would I do at $0.0004/100ms per judgment?") is the
application-finder. Standing rejections recorded so they aren't rediscovered:
parallel-nouls-as-independent-evidence, Jev-as-p-value, cross-question Score
comparability, calibration-certifies-individual-answers.

## 11. Methods catalog + operators/theorems tier (2026-09-18)
New references/methods-catalog.md. Tier 1: named methods (CatBoost features
→ empirical recipe; judge qualification; screening; conformance checking...).
Tier 2: operators & theorems in three classes — substitutable operators
(argmax→Choice, expectation→Score, indicator→Noul), system-level theorems
with their governing preconditions (Bayes/independence, LLN/repeats-not-
parallel, Jensen/utility-from-distribution, Goodhart/probes-concede,
Simpson/per-population calibration, "re-ask-until-agrees" convergence
rejected), and non-substitutable constructs (arithmetic, gradients, CLT-on-
outputs, metric-space claims on Scores). Governing rule: every theorem's
preconditions become code-level checks; no named precondition = metaphor,
not mapping.

## 12. Composition algebra + application generator (2026-09-18)
New references/composition-algebra.md: 11 positions Jev can occupy relative
to any function/operator/algorithm (operand, post-judge, gate, selector,
comparator, prior, state-estimator/controller, optimizer metric, verifier,
discretizer, terminator) with per-position governing rules; logical
operators over Jev outputs (NOT multiplication for AND — ask the compound
question; ∀/∃ as batched-noul + code aggregation); cross-position invariants
(width-cheap/depth-linear, estimate≠measure, positional thresholds, oracle-
without-side-effects). The application generator = positions × constructs
traversal + economics inversion as the filter, replacing brainstorming;
a candidate is promoted only after falsification.

## 13. Full-archive analysis pass (2026-09-18)

- `jev-archive/analysis/evidence.csv`: 169 repos, per-repo README size, language, primitive/API usage, tests, threshold histograms. 186 clones (2 late adds: mizchi/jev-gomoku, joshbla/jev-plays-2048, arnabgho/rlcd-lite, dabit3/jev-experiments → 187), 0 failures.
- `jev-archive/analysis/findings.md`: deep-read distillation.
- New facts: calibre threshold non-transfer across datasets; jev-harness shadow-mode/gate/policy/eval-CLI pattern (24 rows: 48.9s claude CLI vs 1.3s Jev); parallelConstraintDecoding two-forward-pass schema fill + HF RLCD repo has no weights (stock Qwen2.5-1.5B + custom code); rlcd-lite GRPO+Brier proper-scoring-rule → calibration (binary reward doesn't calibrate); dabit3/jev-experiments 21 apps — latency-first taxonomy: streaming judges, keystroke-loop re-rank (seq-tagged, discard stale, judge-once/re-policy-in-code), pre-execution guards, swarm policies, realtime voice/meeting flows, spreadsheet formulas, accessibility-tree computer use, hybrid BM25→Jev re-rank (50%→100% top-1).

## 14. ProgramAsWeights assessment (2026-09-18)

- Cloned programasweights/programasweights-python; org has sdk-python, sdk-js (WASM), skills repo, paw-helper.
- Facts (Contract): NL spec → `.paw` = KV-cache prefix + optional LoRA over fixed interpreter (Qwen3-0.6B ~22MB / GPT-2 ~5MB, browser-capable); local, deterministic, no runtime API; ~0.03–0.5s/call; examples=[…] compile path; finetune compiler `paw-ft-bs48`; constrained decoding via llama.cpp logits_processor; offline mode fails closed; Hub at hub.programasweights.com.
- Relevance (Hypothesis, no measured integration in any archived repo): Jev as calibrated labeling teacher → PAW compile = distilled local judgment; or PAW shadowed with Jev as arbitration gate + drift signal. Non-pairing case: unstable decision surface. Test obligations written into optimizer-integration.md.

## 15. User-named batch deep reads (2026-09-18)

- dbreunig/building-with-jev-skill: best doc-grounded question-design/diagnosis skill found; distilled (source-attributed) into new reference `question-design.md`; SKILL.md mapping index updated. New doc facts recorded: 64k shared budget / 32k longest-question; instruction keys; confidence=peakedness; Noul no-confidence (distance from 0.5); score not quantity-interpolable; taxonomy-walk pattern; counting per-item; symptom table.
- dannote/jev: Elixir peer-process pattern (answers as messages, guards as policy, network-free tests).
- carlaiau/jev-reranking: TREC DL2019 — Jev zero-shot rerank MAP 0.4748 (best), nDCG@10 0.683 vs monoBERT 0.718; $0.76/41k pairs. First serious independent rerank benchmark; adjust rerank guidance honestly (competitive on MAP, behind best tuned cross-encoders on nDCG).
- riff: hybrid static+semantic linter, per-finding calibrated p, 14 calls $0.0004.
- open-typesafe-camoufox: $0.0002/step browser agent; 11-way action Choice; free text only when needed.
- hr98w/jev-visual: open Jev-like VLM direct-logit scoring; Breakout reduced to region classification (decomposition discipline).
- skillranker + jev-harness: previously analyzed (§7, findings.md).

## 16. Batch #5 (2026-09-18)

- probably-lang: Jev as control-flow primitive in a programming language (feeling-conditions as loop guards); judgment recordings + deterministic replay (record once, replay forever without credentials). New composition-algebra position: Jev as conditional operator / loop predicate.
- jev-search: Jev as both query-understanding head and result-ranking tail of a federated multi-engine search (speculative start, lane failures isolated, merge on URL+agreement+rank).
- super-jev: harness with permit() layer independent of confidence; idempotency keys; JSONL replay. Pattern: permission ≠ confidence — domain rules veto regardless of model certainty.

## 17. X+GH hourly scan (2026-09-18 ~13:39–14:39 UTC)

Raw artifacts: `research/archive/hourly/2026-09-18T14/` (USAGE-DIGEST,
theme-digest.json, github-topic-jev-last-hour.json). Method unchanged:
hourly archive + live HTTP checks; this pass's X coverage is a provided
theme digest (first ~400 posts) rather than X API. awesome-typesafe HEAD
moved `8b9e8aa3c44f` → `6eef30ba8c3f`. docs/evals/OpenRouter still HTTP 200.

### Discourse themes (counts from theme-digest)

| Theme | n | Design takeaway |
|---|---|---|
| cost/prefilter | 48 | Dominant: drop chunks/calls before the expensive generator |
| tool routing | 33 | Selector position; products (Toolrouter) + open harnesses |
| agent gate/linter | 27 | AGENTS.md as criteria; confidence gates; shadow mode |
| mixed architecture | 16 | Decision model + LLM writing; explicit anti-replacement |
| product ship | 14 | Moderation ~200ms, EffectTS SDK interest, HA, semantic SQL |
| reproduce/open | 13 | LightJev / open heads — training signal, not an Augustus clone |
| skepticism | 11 | "It's just classification" → answer *placement*, not novelty |
| rerank/search | 11 | Still a live mapping; LlamaIndex Jev rerank this hour |
| on-device/mobile | 2 | Thin evidence; newly-feasible candidate only |

Representative posts (do not treat as benchmarks):
- [@dt_sqr](https://x.com/i/status/2100957356389511173) — "Jev is classification. This is like the oldest task in AI"
- [@seb_jsilva](https://x.com/i/status/2100957104567685310) — mixed architecture, too early as stack replacement
- [@sydneyrunkle](https://x.com/i/status/2100956747729080714) — replace classification *steps* in agents
- [@buildwith_yash](https://x.com/i/status/2100957729208893516) — cheap irrelevance before the main model = cost, not just accuracy
- [@stoufax](https://x.com/i/status/2100956659128361097) — realtime chat moderation ~200ms (**Hypothesis** as a number)
- [@tool_router](https://x.com/i/status/2100957104752238821) — Toolrouter now routes with Jev
- [@hughesanalytics](https://x.com/i/status/2100957428799967514) — XGBoost is the trained-head alternative; Jev is flexibility
- [@whereischarly](https://x.com/i/status/2100955292150153225) — ECE ModernBERT 0.081 vs Jev 0.105 (**Hypothesis**; do not overwrite Archer Hume)

### GH movers (`topic:jev`, 34 repos in the hour) — novel shapes

Already-known stars still moving: awesome-typesafe 186★, skillranker 41★,
awesome-jev (AnotiaWang) 48★, jevmlx 19★, HA-Jev, jev-harness, jev-pref.

**New or newly-salient shapes (design, not APIs):**

- `ibrahemid/git-jev-stage` — per-hunk Choice include/exclude/mixed; exact
  patch; mixed stays unstaged; candidates from `git diff`.
- `ibrahemid/jevprune` — per-line relevance vs task; always-keep last-N +
  error signatures in code; full output recoverable.
- `WiktorB2004/llama-index-jev` — rerank **fails open** (BEIR nfcorpus
  MiniLM 0.340 → +Jev 0.396 nDCG@5); select **fails closed**. First clean
  public statement of per-action fail policy.
- `doeixd/jev-pref` — AGENTS.md prefs → Jev linter; YOU define the rule /
  JEV classifies evidence / CODE maps outcome / AGENT acts.
- `yousudip/lizard-agent` — browser loop with no LLM; extractive answers;
  prices/dates never touch the model.
- `kylemclaren/jevql` — semantic predicates as SQL `jev()` / `jev_prob()`;
  database sees ordinary SQL (CLI rewrite).
- `harrymunro/decision-first` — neighbor skill (try Jev first + lab log).
  Augustus does not absorb it.
- `simota/tenbin` — neighbor skill (design-time lint/eval/thresholds).
  Augustus does not absorb it.
- `aaravriyer193/OpenSmoke` — Jev over every agent step; LLM only on
  flagged runs (attention cascade).
- `frostney/clean-code-review`, `Eliran-Turgeman/repear`,
  `DanRWilloughby/snifftest` — rubric/smell/prose linters; snifftest makes
  the 0.5-unsure-band a non-flag.
- `luantak/is-malicious` — high-stakes pre-run Noul; fail closed + sandbox.
- `FirasSX914/Janus` — measure Jev vs other models on your data, then route
  (calibre's lesson as a product).
- `rongxinzy/LightJev` — train lightweight decision backbones. Record as
  reproduce/open; not an Augustus implementation task.
- Also this hour: refgarden, jevocks, xerify, ground-truth, jevcode,
  typesafe-sdk-java, several awesome-jev forks.

### Skill impact

New reference `references/mixed-architecture.md` + SKILL.md index rows and
the classification non-negotiable. Identity lock: Augustus stays
placement/method/falsification; `typesafe-ai` / `tenbin` / `decision-first`
keep contracts, measurement, and habit. No API fields invented this pass —
docs.typesafe.ai/llms.txt re-fetched HTTP 200; cookbook list unchanged
enough that sources.json docs rows stand.

## 18. Laya — open Choice/Score/Noul head (2026-09-18)

Source: [convaiinnovations/laya](https://huggingface.co/convaiinnovations/laya)
(Apache 2.0; PyPI `laya`; demo Space `convaiinnovations/laya-demo`).
Companion writeup on DEV is advocacy, not an independent bench.

**What it is (vendor card, Hypothesis until you measure):** a
self-hostable, non-autoregressive System-1 decision model with the same
three question types as TypeSafe Jev — Choice (winner + per-option
probabilities + confidence), Score (expected level + distribution +
confidence), Noul (P(true) in [0,1]). Text (or JSON-as-text) in; typed
answers out; no generation. Backbone: ModernBERT-large + a small decision
head (~421M). Multi-question in one forward pass. Claims RLCD-style
training with a proper scoring-rule reward.

**What it is not:** a TypeSafe API drop-in, a multimodal/omni model, or a
reason to fork Augustus into an install guide. Do not copy `laya.predict`
shapes into this skill — their package owns that contract; `typesafe-ai`
owns Jev's.

**Limits the card itself states:** text-only, English, **512 tokens per
question** (question + options + state; longer state truncated);
arithmetic / counting / date compare / multi-hop stay in code; evaluate
calibration on *your* distribution before automating.

**Tradeoff vs TypeSafe Jev (design, not a bake-off):**

| Axis | TypeSafe Jev (primary) | Open head (Laya as the example) |
|---|---|---|
| Mission fit | Documented API, 64k/32k envelope, live docs | Self-host, no egress, $0 inference after GPU |
| Calibration | Closed model; still re-measure on your data | You own eval end-to-end; weights are inspectable |
| Context | ~64k shared / 32k longest question (**Contract**) | 512 tok/question — prefilter state harder |
| Modality | See live docs; not assumed here | Text-only |
| Benches | TypeSafe self-run workflows (lead, not fact) | Vendor table vs Jev (latency/acc) — **claims** |

Their own eval split is the useful number, not the vs-Jev table: in-task
macro acc 0.838 / ECE 0.060 vs **zero-shot** acc 0.651 / ECE 0.207. Same
lesson as Archer Hume (§7): in-distribution calibration is not a license
to skip a held-out test.

**Augustus implication:** mappings, boundaries, and decision-design cards
name a *typed judgment provider*, not a vendor. Default provider remains
TypeSafe Jev (`typesafe-ai` + live docs). An open head is in play when
self-hosting or air-gap is the constraint *and* the 512-tok / text-only
envelope still fits the state — then the falsifying experiment is on that
head, on your labels, not on the vendor plot. LightJev / openjev stay the
"train or reproduce a backbone" bucket; Laya is the first shipped open
*product* with the Jev-shaped interface.

## 19. The judgment-model class (2026-09-18, literature + skill-scope)

Augustus's design surface is the **class** of fast/cheap
categorization-classification-scoring models, not TypeSafe Jev alone. Jev
remains the documented exemplar. This pass is literature + identity, not a
new X+GH hour (hourly method unchanged; last scan still
`archive/hourly/2026-09-18T14/`).

**In-class test.** Language or structured text (or image + closed
label/region set) in; score / distribution / label out; latency in the
per-chunk / per-hunk / per-frame band; code owns side effects. Out of
class: prompt→JSON LLMs, working regexes, trained heads on a frozen
taxonomy with enough of *your* data.

**Families (skill card `references/judgment-class.md`):**

| Family | Objective | Gate? |
|---|---|---|
| Closed decision API (Jev) | Proper-scoring / RLCD; Choice/Score/Noul | Yes, after your thresholds |
| Open System-1 head (Laya, openjev, LightJev) | Same *shape*; you host | Yes, after *your* ECE |
| GLiClass-adjacent | One-pass text+all-labels; sigmoid/softmax affinities | Sieve yes; silent authorize no |
| Listwise / pairwise ranker | Order (nDCG, ListNet); often translation-invariant | Fail open only |
| Vision scorer | CLIP/SigLIP affinity or region Choice | Calibrate; not VLM-as-judge |

**GLiClass (Empirical recipe as a paper, Hypothesis as a drop-in).**
[GLiClass: Generalist Lightweight Model for Sequence Classification
Tasks](https://arxiv.org/abs/2508.07662) (2508.07662). Joint encode of
text + all labels in one forward pass (labels interact; not sequential
cross-encoder pairs). Docs:
[Knowledgator intro](https://docs.knowledgator.com/docs/frameworks/gliclass/intro/).
Cousins: GLiNER (spans), NLI zero-shot, SetFit, ModernBERT heads. Design
use: large or changing tag sets, multi-label sieves. Not a gateable
decision API without a calibration plot on your labels. Jev's 255-option
Choice limit is Jev's, not the class's — this family is why.

**Listwise discriminative vs decision objectives.** The fail-open /
fail-closed fork. [Joint Optimization of Ranking and Calibration with
Contextualized Hybrid Model](https://arxiv.org/abs/2208.06164)
(2208.06164): many listwise losses (ListNet softmax-over-list) are
translation-invariant — adding a constant does not change ranking and
destroys any reading as P(click)/P(relevant). [Regression Compatible
Listwise Objectives for Calibrated Ranking with Binary
Relevance](https://arxiv.org/abs/2211.01494) (2211.01494, RCR) is the
patch *inside* ranking, not a reason to treat an off-the-shelf
cross-encoder as a decision API. Jev's product claim (act/abstain) lives
on proper scoring (log/Brier/spherical; RLCD — `arnabgho/rlcd-lite` in
the archive). Open heads that copy Choice/Score/Noul without that train
loop may *look* like Jev and still be uncalibrated. Rule already in
applied-mappings §4, now class-general: ranking error → quality → fail
open; selection/auth → control → fail closed, needs a decision-shaped
number. A listwise reranker *as* the gate is the rejected design.

**Vision scoring patterns.** Perception = candidate generation + scoring
(keep/drop card with pixels or an AX tree as the parser). Four postures:

1. Pixel-free (preferred when the environment is structured): RAM / AX /
   object JSON → closed action or region set → Choice. Launch-week:
   typesafe-mario, jev-drone, lizard-agent. The model never sees a
   screenshot.
2. Region/label Choice over extracted boxes. `hr98w/jev-visual`: Breakout
   only after reducing control to "which region holds the ball."
3. Dual-encoder affinity. CLIP softmax = competition in the offered set;
   SigLIP pairwise sigmoid = affinity, flatter closed-set margins
   ([SigLIP docs](https://huggingface.co/docs/transformers/v4.39.2/en/model_doc/siglip);
   posture note [2510.13364](https://arxiv.org/abs/2510.13364)). Class-
   conditional coverage can collapse under shift even when marginal
   coverage looks fine ([2608.19376](https://arxiv.org/abs/2608.19376)).
4. VLM-as-judge is *generation*. Verbal scores are not calibrated.

Laya is text-only / 512 tok: a vision hole is not "run Laya on a
caption."

**Portents for agent architecture** (independent of vendor — Hypothesis
as a product roadmap, Contract as a design pressure from the economics
already in the archive):

1. Full-traffic, not sampled (OpenSmoke, jevprune, git-jev-stage, firehose).
2. Skills/tools = catalog + decision, not a stuffed system prompt.
   Large catalogs may prefer GLiClass-adjacent one-pass.
3. Two numbers, two jobs: ranking orders context; decision authorizes.
4. Perception is not narration: extract candidates, score, act.
5. Open heads make the control plane local (air-gap / HA) *if* self-eval
   is accepted.
6. Cross-modal is still thin; "Jev but for images" is a hole, not a
   shipped omni API.
7. Generator-only agents are incomplete; ranker-only agents can sort
   and cannot abstain.

**Skill impact.** New reference `references/judgment-class.md`; SKILL.md
opening/protocol/index/design-card/family slot; FAQ rows for family
choice, GLiClass vs Jev vs cross-encoder, CLIP gating; mixed-architecture
and applied-mappings intros point at the class. Identity lock holds:
still not `typesafe-ai` / `tenbin` / `decision-first`, and not a Laya or
GLiClass how-to. No API fields invented.

## 20. Formal / semi-formal / crossover (2026-09-18, from brief)

Curriculum file `FORMAL-METHODS-SYSTEM-ONE.md` had **not** landed in the
repo or on GitHub search. Card written from the brief + fetched docs
(HTTP 200 unless noted). Skill: `references/formal-methods.md`.

**Ownership split (the load-bearing claim).** Proof/MC/contracts exhaust
a model or fragment. DST searches executions; a clean run is not a
proof. A judgment-class model estimates a *state*. Code owns
authorization. Judgment = sensor; proof/types = constraint; DST =
searchlight. Existing grammar already said this (composition-algebra
positions 3 and 9; estimate ≠ measure); this card names the tools.

**Design-time finders/checkers.** Alloy (scoped SAT instances), TLA+
(TLC/Apalache), Quint (TLA fragment; simulator ≠ proof; no TLAPS —
[FAQ](https://quint.sh/faq)), P, NuSMV, PRISM (model-p is not a Noul),
Event-B/Rodin ([wiki](https://wiki.event-b.org/index.php/Main_Page);
event-b.org itself failed HEAD this pass). Hole: triage
counterexamples / properties / POs. Not: close the obligation.

**Deductive.** Dafny, OpenJML, Frama-C, SPARK/GNATprove. Ranking failed
VCs is in-class; "the lemma holds" as a Noul is out.

**DST.** [Antithesis](https://antithesis.com/docs/introduction/how_antithesis_works/)
(deterministic hypervisor, properties, reproducible timelines).
[Resonate](https://docs.resonatehq.io/evaluate/how-resonate-is-tested):
Lean 4 protocol spec + differential oracle + DST of the TS SDK (CI
replays each seed twice to catch nondeterminism). Three owners in one
product.

**Harms.** TOCTOU-shaped soft checks (judge at t0, act at t1). Soundness
theater (toy bounds; tautological properties; Noul-as-safety-case).
[Hillel Wayne, 10 Mar 2026, "LLMs are bad at vibing
specifications"](https://buttondown.com/hillelwayne/archive/llms-are-bad-at-vibing-specifications/):
4% of GitHub TLA+ files mention Claude; example Alloy spec did not
compile and asserted tautologies; LLMs write "obvious" invariants, not
subtle concurrency/liveness. Force multiplier for experts who *run the
checker*. LLM spec + System One "does this spec look good?" = double
theater.

**Crossover (placement intuition, not SWE-only, not a mapping until a
precondition survives).** NATM observational method: instrument often,
adapt support in code. Snap-fit: designed give only where a miss is
reversible. Norman gulfs: judgment evaluates candidates; forcing
functions execute safely
([NN/g](https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/)).
Leveson STAMP: safety is a control problem; a 99% Noul is a sensor, not
a constraint
([STAMP intro PDF](https://psas.scripts.mit.edu/home/wp-content/uploads/2016/04/STAMP-Intro-2016.pdf)).

**Skill impact.** New card; SKILL.md protocol/index/non-negotiable/FAQ
("replace TLA+?" / "Noul ≈ proof?"); methods-catalog rejected row;
composition-algebra position 9; toolbox family row. Identity lock
holds. No invented APIs. When `FORMAL-METHODS-SYSTEM-ONE.md` lands,
fold named rows — do not wait on it.

## 21. Cross-domain mental models (2026-09-18, critical scope)

Augustus is **not SWE-only**. Design judgment for placing typed
probabilistic judgment using math/logic/algorithmic frames across AI,
SWE, business, knowledge work, and life. Formal methods remain one
pillar. Skill card: `references/mental-models.md`.

**Pillars (method, not vendor):** expected utility + Chow-style
abstention; calibration and Elkan cost-sensitive `t = C_FP/(C_FP+C_FN)`
([Elkan PDF](https://cseweb.ucsd.edu/~elkan/rescale.pdf), [sklearn
walkthrough](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html));
[VOI](https://en.wikipedia.org/wiki/Value_of_information) (gather as an
act); [MCDA](https://en.wikipedia.org/wiki/Multiple-criteria_decision_analysis)
(weights in policy); search/control substitutions; [signal
detection](https://en.wikipedia.org/wiki/Detection_theory) (criterion ≠
accuracy); Leveson sensor≠constraint; NATM/snap-fit/Norman as portable
intuition.

**Non-negotiable restated for any domain:** exact work in code *or
policy* (checklist, ledger, law, recipe); model owns narrow judgment;
never launder a Noul as proof.

**Status discipline:** SWE rows that already have launch-week artifacts
stay Empirical; inbox/hiring/apartment/bid-no-bid/cooking are
**Hypothesis** until labeled logs exist. Promote only with acceptance
tests.

**Skill impact.** SKILL.md opening/description/protocol/design-card
domain+pillar fields; FAQ "only for software?"; mappings.md beyond-SWE
paragraphs; boundary-audit practice-not-just-code + TOCTOU/vacuous-spec
red flags; marketplace/README exposure. Identity lock holds. No APIs
invented.

## 22. Formal-methods expansion + Hypothesis mapping cards (2026-09-18)

Queued follow-up after the mental-models hub: expand the FM pillar
without waiting on `FORMAL-METHODS-SYSTEM-ONE.md` (still 0 GitHub
hits), and add Hypothesis cards so exposure is not SWE-only.

**Alloy Analyzer vs Apalache.** Alloy is a model *finder* (SAT, finite
scope, relational; [FAQ](https://alloytools.org/faq/how_does_the_alloy_analyzer_differ_from_model_checkers.html)).
Apalache is a symbolic model *checker* for TLA+ (SMT; modes: some
traces ≤k, all traces ≤k, inductiveness if the invariant holds —
[apalache-mc.org](https://apalache-mc.org/)). TLC enumerates TLA+
explicitly. Same harm: bounded green ≠ proof. Judgment triages
counterexamples; a Noul does not sit in either seat.

**DST trio.** Antithesis = deterministic hypervisor around existing
software. Resonate = Lean 4 spec + differential oracle + DST of the TS
SDK (CI replays seeds twice). PufferLib = the env is already a
simulator; Serial + seeds for contract debugging; Ocean sanity envs are
trainer contracts, **not** comparative RL baselines
([arXiv 2406.12905](https://arxiv.org/abs/2406.12905);
[puffer.ai/docs](https://puffer.ai/docs.html)). A seed does not make
GPU training bitwise deterministic. Judgment clusters failing
episodes; it does not vote that the policy is correct.

**TOCTOU-of-Noul / AI×FM.** Judge at t0, act at t1 — the check was never
atomic. Same shape in agents, credit-then-wire, kitchen, hiring, and
"spec looks good" then merge. Hillel vibing specs (10 Mar 2026) plus
receipt theater (MCP ran a tautology) and mode laundering (Quint `run`
as `verify`; Apalache random-exec as BMC). QCon 2026 informal-methods
talk: spec / environment / properties are three views.

**Hypothesis cards** (`mappings.md` §6–§9): VOI/gather; SDT/ROC
criterion; Leveson sensor≠constraint; search/control loops outside SWE.
Promote only with an acceptance test that ran. Non-SWE gallery stays
Hypothesis.

**Non-negotiable unchanged:** code/policy owns exact work; model owns
narrow judgment; never launder a soft Noul as proof. Identity lock vs
`typesafe-ai` / `tenbin` / `decision-first`. No invented APIs.

## 23. Curriculum fold (2026-09-18)

Attached research docs landed under
`research/archive/curriculum/` (`FORMAL-METHODS-SYSTEM-ONE.md`,
1-pager, source list, `MENTAL-MODELS-ACROSS-DOMAINS.md`, seed table).
Named rows folded into the skill; the archive is provenance, not a
second doctrine.

**FM.** One-screen alias `references/formal-semi-formal.md`. Depth stays
on `formal-methods.md`: Amazon TLA+ PDF; mCRL2 / KeYmaera X; Alloy
composition-algebra table; semi-formal artifacts (UML/SysML/ArchiMate/
GWT/BPMN/ADRs); Lean/ITP/PBT + DafnyPro "propose, verifier decides";
Resonate HQ = Distributed Async Await (not "Resonate AI"); Cauli ∩
Hillel; Kent / Shirky / Vanderburg / Agans; help/harm checklist.

**Mental models.** Master rule; satisficing; conformal; A* inadmissible;
hysteresis/deadbands; alert fatigue; mechanism design; OR; epistemology;
ten harm patterns.

**Hypothesis cards** `mappings.md` §10–§16: spec pipeline, Alloy loop,
RV sandwich, DST triage, durable agent control, assignment hybrid,
situated density. Still do not promote without an acceptance test.

HTTP 200 this pass: Amazon FM PDF, Cauli, Shirky, Hillel dreidel,
Resonate why+tested, mCRL2, KeYmaera X, arXiv 2502.15441, Lamport Agent.

## 24. jevals — labeled-case workbench (2026-09-18)

[dayhaysoos/jevals](https://github.com/dayhaysoos/jevals) is a local MIT
workbench for running Jev questions against labeled cases (Noul / Choice /
Score, and combinations), comparing saved runs, with WebMCP plus an agent
skill. Not affiliated with TypeSafe. README fetched this pass (HTTP 200).

**Role for Augustus:** empirical acceptance-test *surface* for Hypothesis
mapping cards (`mappings.md` §6–§16). Complements
`scripts/evaluate_decisions.py` (offline Brier / reliability / cost on
exported JSONL). The workbench's existence is Empirical (public repo +
README); promoting a Hypothesis card still requires *your* labeled cases
plus a card-level test that ran. Augustus is not a jevals how-to — do not
copy CLI, env, or ports into skill cards. One-sentence cite:
`references/validation.md` (offline-eval section).

## 25. Hourly 10:07 Boise fold (2026-09-18T16:07Z)

Standing fold of the 10:07 America/Boise hour (16:07 UTC) into PR #1.
Discourse from named X posts (fetched live); GitHub READMEs HTTP 200.
Skill impact is **species map + Hypothesis cards**, not how-tos. Domain-
general mission unchanged. Identity lock vs `typesafe-ai` / `tenbin` /
`decision-first` holds. No invented APIs.

### GLiNER as a Jev-class *peer* (not a GLiClass footnote)

[GLiNER](https://arxiv.org/abs/2311.08526) (Zaratiana et al., NAACL 2024)
is a bidirectional encoder that **locates spans** matching open type
labels in one forward pass. [GLiClass](https://arxiv.org/abs/2508.07662)
is the sequence-classification sibling (Knowledgator): **categorize the
text**, not the spans. [GLiNER2.5](https://github.com/fastino-ai/gliner2)
(fastino-ai; HF `fastino/gliner2.5-{small,base,multi}-v1`) is a later
**local multi-head**: entities, classification, records, relations in one
schema; CPU-first (74M / 194M / 287M). Discourse this hour
([@singularity_sah](https://x.com/singularity_sah/status/2100980051550306418)
replying to the prior
[36×-cheaper Browser Use claim](https://x.com/singularity_sah/status/2100667967499386976)):
GLiNER can do the same *agentic decision* jobs as Jev, local / free /
laptop. **36× is a tweet, not a re-run** — Hypothesis as a number;
Empirical as family existence (paper + public checkpoints).

Species map (skill card `judgment-class.md`):

```text
locate      GLiNER / span extractors     what's *in* the text
categorize  GLiClass / sequence labels   what *is* the text
decide      Jev / Laya / openjev         Choice / Score / Noul over a state
rank        listwise                     order a retrieved shortlist
perceive    CLIP/SigLIP / region Choice  score candidates you extracted
```

A span-locator is not a drop-in Noul. Using GLiNER2.5 classification
heads as a local decision API still needs *your* ECE and fail policy.
Do not copy `AutoExtractor` into skill cards.

### openjev-lm — CPU distill of a hosted teacher

[DECRUX9812/openjev-lm](https://github.com/DECRUX9812/openjev-lm) (MIT):
Qwen2.5-0.5B-Instruct + LoRA (2.16M trainable), 2,591 rows of **Jev's
own API answers**, 400 steps, **6 vCPU, no GPU, 89 minutes**. Gold:
**65/70 = 92.9%** bucket accuracy on 70 hand-labelled Regina job
postings (two independent harnesses agree). Hosted Jev 68/70 = 97.1%;
classifier arm (frozen bge-small) 66/70 = 94.3% and 99.39% agreement on
a 2,631-posting stream. Fresh 106 postings: LM 104/106 = 98.1% *teacher
agreement* (ECE 0.004, Brier 0.031) — that is agreement with Jev, not
independent gold. Honest limits in the README: 2 `service_lead` rows;
one seed, one domain, one annotator; labels from a hosted API;
unaffiliated with TypeSafe. **Empirical** as a named receipted run;
**Hypothesis** as "overnight-CPU-distill any Jev workflow."

### Input brittleness → calibration / sensitivity / abstention

[@brandonjcarl](https://x.com/brandonjcarl/status/2100976725660192989):
semantically equivalent question wording ("Is this the same person as
X?" vs "Same person as X?") can swing probabilities a lot. Not a
blocker; a design constraint. Independently,
[jevgate](https://github.com/thevibeworks/jevgate) README: a comment
moved `git checkout -- .` from 0.91 to 0.37; identical requests differ
by up to 0.18; threshold leaves about one such width to the nearest
unsafe command. Fuel for `mappings.md` §17: paraphrase pairs as a
behavioral test; Chow abstain when paraphrase-disagreement is large;
do not treat a single p as invariant to wording. **Hypothesis** as a
law; **Empirical** as published cautions.

### Allowlist ∩ System One (jevgate)

[thevibeworks/jevgate](https://github.com/thevibeworks/jevgate): three
tiers — **Proven** (every verb is a listed read-only tool, 4 µs, nothing
sent) → **Refused** (code can prove a write/network/wrapper/credential
shape; model never asked) → **Unknown** (unlisted verb only, five Nouls,
admit iff every p < 0.2). It can say allow or say nothing; it **cannot
block**. Jev alone leaks (`/bin/ls` at 0.04) — that is why it is the
third tier. 249 labelled commands, worst-of-three: held-out unsafe
unasked **0/59** (allowlist alone also 0; jevgate lifts safe-unasked
15/35 → 30/35). Real traffic 116,979 Bash calls: 26.4% proven; 16.2%
reach Jev. Credits pi-warden for code-then-model. Mapping `mappings.md`
§18. Domain-general: recipes / law / text-layer first; judge leftovers.

### Langfuse LLM-as-judge framing

[@langfuse](https://x.com/langfuse/status/2100980004678971491): Jev
cannot write sentences and is framed as a **direct alternative to
LLM-as-a-judge** (Choice / Score / Noul + certainty). Placement, not a
Langfuse how-to: when the eval output is a typed decision, a judgment-
class model is the judge; when you need a paragraph rationale or a
trace UI, generation / Langfuse still own those seats. Verbal LLM
scores remain uncalibrated (`judgment-class.md` VLM-as-judge). FAQ
row. **Hypothesis** as "replace every LLM judge"; **Contract** as
"cannot write."

### OCR router measured econ

[@MisbahSy](https://x.com/MisbahSy/status/2100979973905592387) /
[misbahsy/doc-router](https://github.com/misbahsy/doc-router): page-by-
page "needs OCR?" — structural pdf-inspector first, Jev on the remainder,
merge. 19 docs / 155 pages, `mistral-ocr-latest` via LiteLLM, 3 runs:
155 → 87 pages billed; 35.6s → 20.7s (**1.72×**); $0.3100 → $0.1783
(**1.74×**). 9 pages that needed OCR and didn't get it vs **28** for a
rules-only judge. Same composition as jevgate (hard prove ∩ soft
remainder). VOI: do not buy an observation the text layer already has.
**Empirical** as this corpus; re-measure on yours. Not an OCR-vendor
tutorial.

### Pointers (next to jevals; not how-tos)

- [kevinpita/pi-jev-context](https://github.com/kevinpita/pi-jev-context)
  — reversible context sieve for Pi: hide, do not delete; always-keep
  user/system/todos; default τ=0.8 (aggressive); `/jev off` restores.
  Applied-mappings §1 cousin of winnow/jevprune. Independent, not
  official Pi/TypeSafe.
- [jeiel85/jevscope](https://github.com/jeiel85/jevscope) — local-first
  visual decision debugger + JSONL regression (Choice/Score/Noul,
  compare two definitions, expectations). Sits **next to**
  `dayhaysoos/jevals` (already §24) as an acceptance-test surface.
  Policy buckets are JevScope-derived, not Jev answers. Do not copy
  ports/env into skill cards.

HTTP 200 this pass: all seven GitHub URLs, GLiNER arXiv 2311.08526,
GLiClass 2508.07662, HF `fastino/gliner2.5-base-v1`, four named X posts.





