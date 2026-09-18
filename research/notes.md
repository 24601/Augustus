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
- Calibration holds near-distribution (ECE 0.0313, Archer Hume) but collapses out of distribution: 32% accuracy + 0.30 mean top-prob on novel 2-step word problems → Jev flags uncertainty instead of reasoning through it. Rule: never use Jev where the judgment requires a derivation; decompose until each question is observational. Architecture reconstruction (readout, isolation, IIA, confidence-as-arithmetic): §31. Not a new contract.
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

## 26. Same window — trolley, dual orchestration, JevLint (2026-09-18)

Standing-order extras from the same Boise morning. HTTP 200 on named
posts/READMEs. doc-router already in §25 (add: judge is **2.5% of the OCR
bill it authorises**; heuristic is cheaper still and misses 3× more).

### Listwise I/O ≠ decision rationality (Han Xiao trolley)

[@hxiao](https://x.com/hxiao/status/2100973209114075330): a Jev-style
API on **jina-reranker-v3.5** as a "System 1" decision engine. It
**always pulls the lever** in the trolley problem, whether one person
dies or one billion. The model was trained to maximize retrieval
relevance, not decision rationality. I/O works: a listwise reranker can
be *dropped in* as a "decision maker." That is the rejected design made
visible. **Empirical recipe** for Augustus: never treat a listwise
retrieval scorer as an ethics/value Choice without a separate policy.
No public repo found this pass; cite the tweet. Skill: `judgment-class.md`
listwise fork; FAQ; mappings §4 / non-negotiable.

### Dual orchestration (James Ward)

[@JamesWard](https://x.com/JamesWard/status/2100976393546772628): two
topologies, same ownership split:

```text
A. LLM outer loop; Jev is a *tool* that selects/plans MCP calls
B. Jev outer loop; LLM is a *tool* that writes
MCP output schemas are the state Jev can plan over
```

He then has Jev build a workflow AST. **Hypothesis** as a product
("Jev is the planner"); **Empirical** as named topologies. MCP schemas
are exact structure; Jev judges among tools those schemas describe;
code still dispatches. Do not thin into an MCP how-to. Card:
`mixed-architecture.md`.

### JevLint — convention lint as write→check→fix

[huntedman/JevLint](https://github.com/huntedman/JevLint) (MIT,
independent, not TypeSafe): plain-English conventions → file-level Noul
≥ 0.8 findings. Built-ins: `magic-strings`, `descriptive-names`. Custom
plugin = a yes/no question. **No** line-level diagnostics, generated
names, or auto-fixes — the agent/CI owns when to run and how to fix.
  Sibling of `doeixd/jev-pref` (YOU define the rule / Jev classifies /
  code maps outcome). Pointer only; do not copy CLI/env into skill cards.

## 27. Adversarial review of the whole skill (2026-09-18) — review findings, not doctrine

Hostile read of `SKILL.md` + all 16 reference cards + README / CHANGELOG /
marketplace / `docs/ecosystem.md`, against the skill's own non-negotiables.
**This section is a defect list, not a card.** Nothing here is a new
mapping, a new pillar, or a new status label. Where a finding names a
concrete defect, the fix landed in the skill and is noted inline; where
the skill was already right, it is recorded as cleared so the next pass
does not re-litigate it.

Scope note: the read started from the tree at §26 (commit `55b1379`).
Folds §28, §30, §31, and §32 landed *while* this review was running; they
are re-checked in the addendum at the end of this section. §29 is an
unused number left by that concurrent fold — not a missing note.

### Defects found and fixed

**S1 (high) — "every error path fails open" stated as a universal gate
rule, in the one position where side effects live.**
`composition-algebra.md` position 3 (Gate) carried the governing rule
"every error path fails open", and its own example column is a
*pre-action destructive gate* (destructive .90 / exfil .70).
`agent-self-assessment.md` stated the same rule as a non-negotiable
boundary. Read literally, a timeout on a destructive-action gate admits
the destructive act. Every other card says the opposite: fail policy is
**per action**, and dispatch / side-effect gates fail **closed**
(`SKILL.md` protocol 6, `mixed-architecture.md` prefilter table,
`judgment-class.md` composition rule, `applied-mappings.md` §4–§5,
`methods-catalog.md` cascade row). `mappings.md` §18 already words the
precondition correctly ("fail open unless a real sandbox/interlock sits
underneath"). Fixed: both places now carry that precondition — advisory
guards fail open *because* a hard interlock/sandbox is underneath;
selection and authorization gates fail closed.

**S2 (high) — dual-orchestration topology A said the decision model
"plans" MCP calls.** `mixed-architecture.md` transcribed the James Ward
topology (§26) as "Jev is a *tool* that selects / plans MCP calls" while
the same file, 40 lines earlier, calls "the model chooses its next tool
in a loop" a standing red flag — as do `mappings.md` §9,
`mental-models.md`, and `boundary-audit.md`. The section's "Does not"
line only forbade the narrower "planner that invents tools". Fixed:
topology A selects from a closed catalog and code dispatches; the
planner rejection is restated in place. "Jev builds the AST" stays
Hypothesis.

**S3 (medium-high) — the trolley result was labeled "Empirical
recipe".** `judgment-class.md`'s own legend reserves that label for a
named paper or repo; §26 records no public repo, only a tweet. Worse,
the label invites reuse of what is a **rejection**. Fixed: relabeled an
Empirical *rejection* (one tweet, no repo), content unchanged.
`faq.md` and `methods-catalog.md` already had it right.

**S4 (medium) — the skill's own advice violated its species map.**
Three places (`SKILL.md` protocol 4, `judgment-class.md` portent 2,
`applied-mappings.md` §5) offered "GLiClass tags **or GLiNER spans**" as
the one-pass alternative when a label set or tool catalog outgrows Jev's
255 options. Routing over a closed catalog is *categorize* / *decide*;
nothing is located, and `judgment-class.md` itself says a GLiNER span is
not a drop-in Noul. Fixed: GLiClass (categorize) is the substitute for
large/changing label sets; GLiNER (locate) applies only where the answer
*is* a span in the text.

**S5 (medium) — the openjev-lm caveat was attached to the wrong
number.** `judgment-class.md` and `faq.md` both read "92.9% on 70 gold …
is not independent gold". Per §25 the 92.9% *is* measured against 70
hand-labelled postings; the figure that is teacher-agreement rather than
gold is the 98.1% on 106 fresh postings. The real limits are: training
labels came from the hosted teacher, n=70, one annotator, one domain,
one seed. A caution that misreads its own source is worse than none —
a reader who checks stops trusting the label. Fixed in both cards.

**S6 (medium) — one live API constructor leaked into a skill card.**
`optimizer-integration.md` carried
`typesafe({apiKey}).systemOne({state, questions})` — request shape plus a
credential argument. `mixed-architecture.md`'s neighbor table says
Augustus is not for "curl snippets, field names, SDK versions" and
`boundary-audit.md` red-flags "SDK fields written from memory instead of
live docs". Fixed: the call form is gone, the placement rule stays, and
the card points at the framework's own docs and `typesafe-ai`.

**S7 (medium) — `question-design.md` enumerated request-body field
names.** The accepted `instructions` object keys are contract surface
owned by `typesafe-ai` + live docs, and were listed from a dated
snapshot with no re-read hedge (the envelope numbers likewise). The
card's mechanics — one property per question, crisp conditions, the
symptom→cause→fix table — are legitimately Augustus and stay. Fixed:
the key enumeration is replaced by a pointer, and the dated
contract surface is marked as a pin to re-read live.

**S8 (medium) — `mappings.md`'s preamble overclaimed uniformity, and the
range reference went stale.** The preamble read "Cards §6–§18 [now §19]
are **Hypothesis** until an acceptance test runs", which the cards' own
bodies contradict: §8's ownership split is Contract, §9's example is
Empirical (jev-mcts), §18's named shapes are Empirical. `SKILL.md`'s
index was *more* precise than the file it points at. A blanket claim the
body contradicts teaches the reader to skim the labels. Separately, when
§19 was added mid-review, four files kept pointing at §6–§18
(`faq.md`, `formal-methods.md`, `formal-semi-formal.md`, `README.md`)
while `SKILL.md`, `mappings.md`, and `docs/ecosystem.md` moved to §6–§19.
Fixed both: Hypothesis **as domain-general products** with the exceptions
named, and all seven range references aligned.

**S9 (low-medium) — §17 quoted jevgate's ≤0.18 jitter without forbidding
its reuse as a constant.** §18 explicitly forbids copying 0.2 and 1.74×;
`composition-algebra.md` open positions already say a universal jitter
bound is Hypothesis. Fixed: one clause in §17's "does not transfer".

**S10 (low-medium) — four cards had no trigger term in the SKILL.md
description.** `boundary-audit.md` (which protocol step 1 *requires* for
any existing system, PR, or workflow), `question-design.md` (the
diagnosis table — "my Noul sits at 0.5" matched nothing),
`agent-self-assessment.md`, and `optimizer-integration.md`.
`validation.md`'s own frontmatter rule says to name the jobs and warns
that trigger-term gaps are the top routing failure. Fixed: one compact
clause naming those four jobs.

**S11 (low) — evidence label disagreement on the ownership split.**
`toolbox-mapping.md` labeled proof-vs-judgment ownership **Empirical**;
`mappings.md` §8, `methods-catalog.md`, and `formal-methods.md` call it
Contract. Fixed to Contract.

**S12 (low) — the done-check spent a Noul on a countable fact.**
`agent-self-assessment.md` gate 3 asked one Noul for "'done' claimed
after code changes with no test/build/lint result". Whether a
test/build/lint result exists in the trace is structural; only the
*claim* is semantic. Spending the model on the countable half is the
"Jev on `/bin/ls` as the first tier" pattern §18 rejects. Fixed: the
check is split — structure first, Noul on the remainder.

### Cleared (checked, no change needed)

- `GLiClass-adjacent` no longer appears in any skill card; it survives
  only in notes §19 above, as provenance.
- Resonate HQ is correctly identified as durable async execution (not the
  unrelated "Resonate AI" brand) in all five places it appears, and
  promise settlement is never delegated to a Noul.
- Alloy model-finder vs Apalache modes vs TLC explicit-state are never
  collapsed; the Apalache mode list is intact in both FM cards.
- The 36× Browser Use figure is labeled a tweet everywhere it appears.
- jevgate 0/59, doc-router 1.74×, and openjev-lm's numbers are never
  offered as universal constants; §18 and `applied-mappings.md` §6
  forbid copying them.
- No `npx`, `AutoExtractor`, `TYPESAFE_API_KEY`, port, or install-command
  leaks in any skill card (S6 was the only API-shape hit).
- Domain-general mission holds: `mental-models.md` carries all five
  domains with SWE rows marked Empirical and the rest Hypothesis;
  SWE-scoped cards say so in their titles and in `SKILL.md`'s index.
- Non-negotiables are stated in `SKILL.md` and repeated, not weakened, in
  `mental-models.md`, `formal-methods.md`, `formal-semi-formal.md`, and
  `methods-catalog.md`'s standing-rejections list.
- CHANGELOG's "§6–§16" is historically accurate for the order 0.3.0 was
  assembled in (§17–§18 arrived in the hourly fold, on the next line) —
  not a stale cross-reference.

### Standing risks (not defects; watch, do not fix by adding text)

- `optimizer-integration.md` and `agent-self-assessment.md` remain the
  most vendor-shaped cards in the skill. They earn their place as
  placement cards; they are the first place to look if Augustus starts
  drifting back into a how-to.
- Card count is 16 and several cards now cross-reference four or more
  others. The duplication guard ("do not duplicate doctrine") is holding
  but is the thing most likely to break next.

### Addendum — re-check of the folds that landed mid-review (§28, §30–§32)

Those four folds (effect-oriented loops, GLiGuard, Archer Hume,
TypeAR) were written into the same tree while this review ran, so they
got the same hostile read. **No new defects.** Specifically checked:

- **Species map held under pressure.** GLiGuard is placed on the
  *categorize* row and explicitly not as a sixth species or a Jev weight
  clone; TypeAR is placed as a **surface** on a generator, not as
  `decide`. Both are the discriminations §25's species map exists to
  force, and both landed on the right side.
- **Evidence labels held.** The Hume essay is labeled a *reconstruction*,
  not a TypeSafe contract, with his own published / observed / inferred
  split preserved; the announced open-weight drop is **Watch, not
  shipped**; TypeAR's ~5.8× is marked "their example, not a portable
  benchmark"; GLiNER2's "like jev" is read as naming the *job*, not the
  objective. None of these is copied as a constant.
- **Non-negotiables held.** `mappings.md` §19 keeps transitions and the
  side effect in the host, fails closed on an unknown option id, and
  refuses to multiply edge predicates. The new IIA / option-order
  material is added as a *property test* in `validation.md` with the
  explicit rider that a clean PBT run is not a proof — sensor, not
  constraint.
- **Identity lock held.** §19 refuses the Effect.ts misreading and says
  the ZIO client's combinator is neither the Jev HTTP contract nor an
  Augustus API; the GLiGuard and TypeAR cards say "do not invent a call
  shape." No CLI, env, port, or `AutoExtractor` leak arrived with them.
- **Cross-references resolve.** Every `notes.md §N` pointer in the skill
  and in `docs/ecosystem.md` was validated against the section titles
  actually present; none dangles. The Hypothesis range was left stale at
  §6–§18 in `faq.md`, `formal-methods.md`, `formal-semi-formal.md`, and
  `README.md` after §19 was added — repaired here (see S8), which is the
  recurring failure mode of range references and an argument for citing
  card names rather than ranges next time.

Process note, not a skill finding: two agents wrote this working tree
concurrently during this pass. That is how the §29 gap and a transient
duplicate `mappings.md` §19 appeared (the duplicate resolved itself
before commit and was never a defect in the skill). Worth avoiding, not
worth documenting in a card.

## 28. Effect-oriented loops + GLiNER2 "like jev" (2026-09-18)

Two posts, both image-primary. `note_tweet` was requested and absent.
HTTP 200: both X URLs, GLiGuard arXiv 2605.07982, `fastino-ai/GLiGuard`,
`jamesward/zio-typesafe-ai` (README loop section matches the image).

### Effect-oriented state-machine loops (James Ward)

[@JamesWard](https://x.com/JamesWard/status/2100981305009664299)
(2026-09-18T16:12Z): "Effect Oriented Jev-driven state-machine loops!"
The image is titled "Jev-driven state-machine loops." Load-bearing
sentence, same wording as the
[client README](https://github.com/jamesward/zio-typesafe-ai):

> An action handler may run arbitrary ZIO effects—MCP calls, database
> operations, or a no-tool generative model call—while Jev remains the
> outer decision loop.

Architecture note in that repo, not a second claim: "Jev never generates
an action; on every iteration the host generates the *entire* finite set
of legal actions and Jev answers one `Question.Choice`."

**Not Effect.ts.** "Effect Oriented" is Ward's name for effect systems
(*Effect Oriented Programming*, Scala 3 / ZIO). The diagram is
`TypeSafeAI.loop` in that ZIO client. Do not transcribe it as an
Effect.ts snippet, and do not treat the client's combinator as the Jev
HTTP contract or as an Augustus API. Identity lock holds: `typesafe-ai`
owns integration contracts; this skill owns placement.

**What transfers (Hypothesis, `mappings.md` §19):** §3 decision circuits
with the effect made explicit. Soft Choice on the transition; code owns
continue/done and the side effect. Extends §26 dual orchestration
topology B (Jev outer loop; generator is a callee; MCP schemas are
state). Unknown option id fails closed before the effect. **Does not:**
Jev inventing tools; handler latency counted as model cost; 1–255 as a
class law.

### GLiNER2 multi-task classification (urchade, primary source)

[@urchadeDS](https://x.com/urchadeDS/status/2100929613857804379)
(2026-09-18T12:47Z), GLiNER author: "how does GLiNER2 performs multi-task
classification (like jev)" — from their GLiGuard paper
([arXiv:2605.07982](https://arxiv.org/abs/2605.07982)). The image is
Figure 3. Load-bearing caption:

> It jointly encodes a linearized task-label schema with the input text,
> then scores each label via a shared MLP classifier to perform
> multi-task safety classification in a single pass.

Figure mechanics (not an API): linearized `[P]` task / `[L]` label
schema, bidirectional encoder, shared MLP, **softmax** for single-label
tasks and **sigmoid** for multi-label, all tasks in one pass. Paper:
0.3B encoder adapted from GLiNER2; task and label blocks composed in
the input schema. Code/models: `fastino-ai/GLiGuard`. Do not invent a
GLiNER call shape.

**Confirms the species map; does not move it.** "Like jev" names the
*job* — multi-task classification in one forward pass — not a
calibrated Choice / Score / Noul. That is **categorize** beside
**decide**. Locate stays GLiNER spans. GLiNER2.5 local multi-head (§25)
is a different checkpoint; do not collapse GLiGuard into it. 36×
Browser Use stays a tweet/Hypothesis, not a re-run. Species map:
categorize row, not a new species (`judgment-class.md`). Author-reported
scale, the README aggregation rule, and the FAQ row: §30.

## 30. GLiGuard — README and paper claims (2026-09-18)

Extends §28 (tweet / Figure 3). Does not replace the Ward card there
or in `mappings.md` §19. HTTP 200 this pass: GitHub README (HTML and
raw), [arXiv:2605.07982](https://arxiv.org/abs/2605.07982), Hugging Face
`fastino/gliguard-LLMGuardrails-300M`.

**Author-reported, not re-run.** Fastino; Urchade Zaratiana, Mary
Newhauser, George Hurn-Maloney, Ash Lewis. Schema-conditioned encoder
guardrail on the GLiNER2 interface. One non-autoregressive bidirectional
pass. Named tasks: prompt safety, response safety, toxicity / harm,
jailbreak, refusal. Paper: 14 fine-grained harm categories and 11
jailbreak strategies, composed as task and label blocks in the input
schema. README checkpoint: `fastino/gliguard-LLMGuardrails-300M` (0.3B).

Scale, do not collapse the two wordings: README says 23× to 90× smaller
than comparable 7B–27B decoder guards, and up to 16.2× throughput and
16.6× lower latency. Paper abstract says up to 16× throughput and 17×
lower latency; paper body (Table 3) matches the README (16.2× / 16.6×).
README benchmark averages: 87.7 prompt F1, 82.7 response F1.

Training: adapted from GLiNER2; WildGuardTrain for safety and refusal;
auxiliary harm and jailbreak labels are automatic and, in the paper,
weakly supervised (GPT-4.1 on unsafe samples). **Not a Jev weight
clone.**

**Aggregation** is the README's benchmark script, not new doctrine. A
prompt is unsafe if safety says unsafe **or** toxicity / jailbreak is
any non-benign label. A response is unsafe only if safety says unsafe
**and** refusal does not fire — refusal overrides. Paper §3.6 is the
same monotonic override. Point at existing policy-in-code (`mappings.md`
§3; judge-once / re-policy; explicit policy in `mixed-architecture.md`).
Not generalized past that script, so not a Hypothesis. Their script's
default operating point is 0.5; do not copy it.

**Placement.** Same interface shape as batched System One questions;
different objective (safety schema vs Choice / Score / Noul).
**Empirical** open encoder class next to Laya and GLiClass. "like jev"
stays discourse (§28). A GLiGuard score is not a proof. LLM I/O safety
is not coding-agent tool gates. rh-guard README (HTTP 200) is the
reward-hack / eval-integrity hook; jevgate is the allowlist shape.
Different holes. Do not copy either install.

## 31. Archer Hume — architecture reconstruction (2026-09-17)

[Jev's Architecture Unmasked](https://archerhume.com/posts/jevs-architecture-unmasked/)
(17 Sep 2026, ~28 min; HTTP 200 this pass). Probe of `jev-1.13.0`, one
early-access account, one region. Headline is ~10,000 API calls; the
methods section itemizes probe, benchmark, and follow-up requests (shared
benchmark items — not 10k independent problems). **Reconstruction, not a
TypeSafe contract.** Live shapes and the ~32k/~64k envelope stay in §1
and the docs. Labels are his: published by TypeSafe, observed in probes,
inferred from them.

1. **End with a readout, not AR text.** Published: probabilities in
   parallel, not token-by-token generation. Observed: `output_tokens` is
   a billing figure from the serialized response, not a decode trace (the
   question id is not sent to the model, yet the count moves with it;
   `0.0` costs the same as `0.01`; latency tracks input length). Inferred:
   the head (slot softmax, reserved vocab rows, or a pointer). Reserved
   label tokens remain possible.
2. **Share state, isolate questions.** Observed: a secret in a sibling
   question is invisible (0.00); the same text in state is visible
   (~0.90–0.92). Accounting is additive; up to ~100 questions, server time
   barely moves. Inferred, not measured: prefix KV plus causal suffixes.
   Hydragen/DeFT are prior art he cites, not a library claim. The mask
   itself is not exposed.
3. **Causal backbone — inferred.** Probes cannot separate a causal decoder
   from a bidirectional encoder. He assumes a pretrained causal decoder
   (MMLU-Pro 84.6%; RLCD described as post-training) and says bidirectional
   cannot be ruled out. Tokenizer is observed: none of 192 public
   tokenizers matched; closest public agreement is Qwen (348/415), not an
   exact match; o200k is close and ruled out by digit splitting. Closest
   tokenizer is not an identified base model.
4. **Options interact before the choice — behavior observed.** Appending
   an irrelevant option moved log-odds of two existing options in all ten
   blocks (~+0.38 → ~+0.11; mean change −0.28). That breaks IIA for fixed
   independent logits plus a fixed softmax. Mechanism is not unique (a
   set-dependent temperature can do it). Order sensitivity, separate
   probe: reversing options moved a probability from roughly 0.84–0.89 to
   0.93–0.96, so a threshold near 0.9 can change the act.
5. **Train the distribution; confidence is arithmetic.** Published name:
   RLCD. Which loss is unpublished — log or Brier is his proposed proper
   scoring recipe, not a disclosed objective. Observed in the adapter he
   cites (`confidence_metrics.py`, rev `fb52b103`): for K>1, Choice
   confidence is `(p_max − 1/K) / (1 − 1/K)` — distance from uniform, not
   a second learned correctness score. A peaked distribution can still be
   wrong. MMLU ECE 0.0313 and the fresh-math collapse are already §7.
   Properness is not a deployment guarantee.
6. **Sparse MoE — inferred, not observed.** He expects sparse experts and
   says a dense swap would leave the interface, shared state, isolation,
   and readout unchanged. Nothing else depends on it.
7. **Batch branches, not a conversation.** Observed: no dependency chain
   between answers; duplicate questions in one request still differ, so
   do not assume API determinism. That noise does not prove text sampling.
   Inferred: suffixes packed against a shared prefix. A later question
   that needs an earlier answer requires another stage. Code owns that
   transition.

Limits he re-measured — same envelope as §1, **independent probe, not a
new contract**: ~32,768 tokens per branch; ~65,536 per request with state
counted once; at most 255 options, request validation not a measured
256-slot head; non-determinism across duplicates.

**WATCH, not shipped.** Tweet hedges and the hub search are §32.
Weigh "smarter than Jev" against *this* essay: order can cross a ~0.9
threshold, and calibration is in-distribution (§7), not a leaderboard.
The public Qwen3.8-27B checkpoint is a base; the decision-model drop is
not that checkpoint. Laya stays text-only (§18).

Design card and the TypeAR comparison (constrained AR vs this readout;
not a how-to): `judgment-class.md`. IIA / order as a property test:
`formal-methods.md`, `validation.md`. Confidence question: `faq.md`.

## 32. TypeAR — constrained-AR surface (2026-09-18)

[zmtomorrow/TypeAR](https://github.com/zmtomorrow/TypeAR). GitHub API
this pass: description "Type-Safe Decoding for Autoregressive LLMs";
language Python; created 2026-09-17T12:41:27Z; updated
2026-09-18T12:32:37Z; default branch `main` at `a49c320`; README blob
`43f456ae`. `license` null; no LICENSE file in the root listing. HTTP
200 on the repo and on the raw README. **Contract** as that README.
Not a how-to: no install, ports, or client signatures in skill cards.
README names SGLang as the serving stack for a compatible open model;
that name stays in this note.

**What the README actually says.** A typed-decision interface on a
compatible pretrained open autoregressive model, without a proprietary
model API, retraining, or manual KV management. Their serving stack is
named in the README; skill cards do not repeat it. Finite enums at most
16 values. Fields: string / integer / number enums, open integer, open
number (tokenizer-native constrained decoding, update dated 2026/09/18),
boolean. Sequential mode is the default: each later field is conditioned
on earlier selected values. Batch mode forks independent fields after a
shared prefill; the two modes compute different conditionals. Closed
decisions generate one token. With prefix reuse, newly processed input
is O(C + D·S); without it, O(D·C + D²·S); output is O(D + N) where N is
open-numeric tokenizer steps. Probabilities over allowed values; argmax
default; sample mode applies temperature to constrained scores.

**Their throughput number.** One local run: Qwen3.8-27B, K=16 one-token
booleans, sequential 9.35 s vs batch 1.61 s, relative throughput 5.8×.
They call it a single example, not a portable benchmark. **Empirical
only as that self-reported receipt.** Not re-run here.

**Not a sixth species.** Next-token constraint is a different objective
from a proper-scoring decision head (Jev, Laya, openjev-lm). A
constrained distribution is not a Noul. The README schema has no
abstention type. Enum ≤16 plus "must pick" is brittleness: compose with
`mappings.md` §2 and §17, and with a jevgate-shaped structural gate
(§18) before the model is asked. `rh-guard` is not a mapping here.
§30 already records `24601/rh-guard` (README HTTP 200) as a reward-hack
hook, a different hole from jevgate; this card does not cite it.

**Versus Jev fan-out and Ward.** Questions on one Jev request do not
see each other's answers (`question-design.md`; §31 item 7).
TypeAR sequential mode does the opposite. `mappings.md` §19
(effect-oriented state-machine loops) already existed at this write:
code owns transitions. Sequential conditioning is not that machine.
Batch mode is the isolation pattern.

**Composition hypothesis.** TypeAR's example and Hume's announced drop
(§31) both name Qwen3.8 27B. Running this surface on those weights
versus stock Qwen is **Hypothesis** until the weights, license, and
evals exist. Hub search this pass: no model repos under authors
`archerhume` or `4rcherhume`, and none for query "archer hume jev".
Watch list, do not pretend they exist: weights drop, license, eval
claims vs Jev, whether a Noul or abstention exists, candidate-set size
limits. Tweet hedges to keep: "probably like 65% done", "will probably
release tomorrow" (posted 2026-09-18T07:26:10Z — **WATCH**, not
shipped), "seemingly quantises pretty well", "from early experiments
seems to be smarter than Jev (surprisingly)" — a **claim**, not
Empirical gold. Compare, when it exists, to Laya (text-only, §18),
this surface, and jev-visual (region Choice, findings). `note_tweet`
was requested on both posts and was absent; the full text is in `text`.

Card: `judgment-class.md` constrained-AR surface. One FAQ row. One
formal-methods paragraph (open weights vs API; sensor still isn't a
proof).

## 33. Hourly fold ~11:02 America/Boise (2026-09-18) — decision surfaces, HF novel, device/harness

Window: America/Boise ~11:02 ≈ 17:02 UTC. Docs-only. No Jev wrapper, no
serving-stack how-to, no copied `predict()` / env / install. HTTP 200
this pass on every cited Hub card, GitHub README, essay, and X URL
below. Hub authors `archerhume` / `4rcherhume` still have **no** model
repos (empty `?author=` lists). Drop remains **WATCH**, expected ~19 Sep
Boise from the 18 Sep 07:26Z hedge ("will probably release tomorrow").

### Archer Hume — clarifications, still not landed

Status tweet already in §32:
[2100848840643612729](https://x.com/4rcherhume/status/2100848840643612729)
(2026-09-18T07:26:10Z). Specs unchanged: Qwen3.8 27B-based, 265k,
multimodal, no audio, "seemingly quantises pretty well"; "smarter than
Jev" is an early claim against *his* order-sensitivity and in-distribution
calibration warnings (§7, §31). Essay still a reconstruction, not a
TypeSafe contract:
[Jev's Architecture Unmasked](https://archerhume.com/posts/jevs-architecture-unmasked/).

New replies (all `note_tweet` absent; full text in `text`):

1. **Not anti-TypeSafe.** Immediate self-reply
   [2100849091504980126](https://x.com/4rcherhume/status/2100849091504980126):
   "I have nothing against TypeSafe, it's a great idea. I just run a
   healthcare startup which means we need control over deployments, so
   we can't use Jev." Follow-up
   [2100955652025893086](https://x.com/4rcherhume/status/2100955652025893086):
   Australia; "very specific laws about where you can send private data
   (especially health)"; vendors exist, they just have AU infra.
   Deployment control / data-residency, not a product feud.
2. **27B dense for one-forward-pass local speed.**
   [2100856685153935699](https://x.com/4rcherhume/status/2100856685153935699):
   "Chose 27b dense because it has a decent balance of base intelligence
   and small-ish footprint (when you remove AR decoding it's actually
   really fast locally since it's one forward pass). Next step would be
   getting it done with an MoE base, then it's seeing how small I can
   get it." Dense-now, MoE-next, then shrink. Matches the essay's
   inferred readout (item 1) as a *design intent*, still not a shipped
   checkpoint.
3. **Multimodal generalization is a report, not a recipe.**
   [2100950467245387937](https://x.com/4rcherhume/status/2100950467245387937):
   "Weirdly it seems like as long as the base model is multimodal the
   text post training generalises to images pretty well. Doesn't need
   that much intentional training (I think)." Hedge ("I think") stays.
   Laya remains text-only (§18). jev-visual remains region Choice.
4. **Class name.**
   [2100604161821979134](https://x.com/4rcherhume/status/2100604161821979134)
   (17 Sep): "I desperately don't want to call this new paradigm
   'system one models' so if I manage to get an open weight one released
   tomorrow can we all agree to call them decision models?" Follow-up
   "God I hope decision model catches on"
   ([2100616134328459574](https://x.com/4rcherhume/status/2100616134328459574)).
   Augustus keeps TypeSafe's "System One" when quoting the exemplar and
   uses **decision model** / judgment-class for the family. Not a rename
   of this skill.

When-to-use axes (calibration, VOI, latency/$, deployment control,
multimodal, enum size): `judgment-class.md`. FAQ row expanded. Still
Watch until weights, license, and evals exist.

### HF novel (verified this pass)

1. **Local memory-gating LoRA (teacher-copy).**
   [`SargeDev/jev-gate-student-b`](https://huggingface.co/SargeDev/jev-gate-student-b)
   (created 2026-09-18T16:52:35Z, apache-2.0): LoRA r=16 α=32 on
   `Qwen/Qwen2.5-0.5B-Instruct`; P(relevant) from softmax over final-token
   `yes`/`no` logits; no token generated. Card: MAE 0.187 / Pearson 0.791 /
   agreement 90.0% on held-out n=60 vs vanilla 0.5B 0.536 / −0.067 / 38.3%;
   ~59 ms RTX 3060. Corpus
   [`SargeDev/jev-distill-corpus`](https://huggingface.co/datasets/SargeDev/jev-distill-corpus)
   (created 02:14Z, lastModified 16:52Z): datasets-server this pass
   **148,160** train rows; tags `100K<n<1M`. The dataset *card* currently
   duplicates the model card (incl. a 5,605-row test table); row count is
   from the Hub size API, not from that README. Same teacher-copy caution
   as openjev-lm (§25): agreement with Jev labels is not independent gold.
   Card says gate at 0.5 and **fail-open on errors**. Placement: context
   sieve (`applied-mappings.md` §1) beside `kevinpita/pi-jev-context` and
   the Pi compaction family (`tamaratran/fast-jev-compaction`;
   `vava-nessa/pi-jev-compaction` as a named Pi cousin). Do not copy the
   usage snippet into skill cards.

2. **Domain-local categorize (JP SNS).**
   [`kokuren/jp-sns-jev7-estimator`](https://huggingface.co/kokuren/jp-sns-jev7-estimator)
   (created 14:48Z, apache-2.0, ONNX INT8 DistilBERT Japanese): seven
   sigmoid scores (insult, threat, obscene, identity_attack,
   sexual_explicit, targetedness, indirect_hostility). Card's own
   sentence: "continuous distilled teacher scores, **not calibrated
   probabilities**." `threat` F1@0.5 = 0.0000 on their held-out table
   (rare-class; accuracy@0.5 is the wrong summary — `mappings.md` §7).
   Mean Pearson 0.75. Domain-local System One *shape*, still categorize /
   score, not a Noul. Threshold on *your* labels.

3. **Encoder open-jev (not a Jev teacher-copy).**
   [`com-kotobalabs/open-jev-deberta-v3-large`](https://huggingface.co/com-kotobalabs/open-jev-deberta-v3-large)
   (created 10:01Z, apache-2.0, `microsoft/deberta-v3-large` ≈434M):
   Choice ≤255 / Score 2–10 / Noul from **one bidirectional pass**;
   softmax within each question's option group; CE + Brier; post-hoc
   temperature on a validation split. Public gold only (Banking77, SST-5,
   BoolQ) — "no synthetic answers, no teacher model." In-domain 0.854 acc
   / Brier 0.213 / ECE 0.022 (1,500 states / 3,508 questions); OOD 0.690 /
   0.399 / 0.035 (new instructions and option sets). 512 tok total (state
   cut to 256). Author latency: 1.8 s / 4 questions M1 Max CPU fp32;
   28 ms e2e / 10 questions H100 bf16. Code:
   [kotoba-lang/typed-decisions](https://github.com/kotoba-lang/typed-decisions).
   Independent of TypeSafe. Self-eval duty unchanged. Do not copy the
   client signature.

4. **Constrained-decoding / calibration gold (no token generated).**
   [`Mikhail/mini-jev-runs`](https://huggingface.co/datasets/Mikhail/mini-jev-runs)
   (created 12:05Z, MIT): **27,900** schema-driven decisions on frozen
   `Qwen/Qwen3-4B-Instruct-2507`; lettered options; **one forward pass**;
   answer read from next-token logits over option letters; full candidate
   logits kept. Write-up [r-ms/mini-jev](https://github.com/r-ms/mini-jev)
   (20★ this pass). Headline from the card: unconstrained argmax is an
   option letter 13,600/13,600; vs grammar-constrained JSON Δ −0.22 pp
   (CI covers 0); scores "deliberately *not* calibrated." Rotated-options
   split is an IIA / position-prior test surface (`validation.md`,
   `formal-methods.md`). Out-of-scope + "none of the above": 41/50
   reading vs 47/50 generating. Compose with TypeAR (`notes.md` §32):
   same *read-the-letter* graph, different serving claim. Not a how-to.

5. **Hierarchy vs Jev's 255 cap (search / taxonomy / MCDA).**
   [`reachjalil/jev-tree-choice-cap`](https://huggingface.co/datasets/reachjalil/jev-tree-choice-cap)
   (created 01:17Z, MIT): synthetic 320-leaf region→service→mode catalog,
   n=180, seed 20260917, live `typesafe-ai/jev` on Vercel AI Gateway.
   Code [reachjalil/jev-tree](https://github.com/reachjalil/jev-tree).
   Headline: keyword 180/180 (0 calls); authored tree **180/180** (3
   calls); flat+partition 179/180; truncate-to-255 **90/180** and
   **0/90 on the tail** (Cape Town `af-south-1` is past index 255).
   Spend estimate $0.142 at $0.042/M input — author. **Empirical** as
   "truncation silently drops the tail"; **not** a quality win over
   keyword on this invented catalog (keyword also 180/180). Tournament
   brackets stay rejected (`mappings.md` §5). Prefer an authored
   taxonomy or retrieval.

### Device + harness patterns

- [`Friedjof/jev-mobile`](https://github.com/Friedjof/jev-mobile) (MIT,
  Python, 0★ this pass; pushed 16:59Z): durable Android worker, USB
  Portal ADB, **stdio Mobile MCP** for task delegation (`start_task` /
  `get_task` / …). Jev sees prevalidated candidates; it never generates
  coordinates, MCP calls, or code. Perception in code (UI tree /
  companion AccessibilityService). Escalation always available.
  Sensitive/external-effect classes are not autonomous. Previously "thin
  evidence" in `mixed-architecture.md` — the *placement* (pixel-free
  candidates + closed Choice) is now a named recipe; app coverage is
  still Keep/fixture-scoped. Do not copy `.env` or MCP URLs.
- [`jcpsimmons/jev-macos-loop`](https://github.com/jcpsimmons/jev-macos-loop)
  (AGPL-3.0, Apple silicon; created 05:17Z, pushed 16:57Z): OmniParser
  CoreML + Vision OCR + accessibility locally; **text-only** Jev
  decisions; pixels/coordinates stay on the Mac. Finder demo: 9 files →
  3 group moves in 7.39 s, independently verified. 6/6 native GUI tasks
  on Vercel and OpenRouter (small sample, warmup excluded). DONE is a
  model decision; benchmarks check the app. Vision portent 1
  (`judgment-class.md`). Not a how-to.
- [`AntonioCoppe/jev-harness`](https://github.com/AntonioCoppe/jev-harness)
  (already §7 / findings): policy + **confidence gate** + **shadow mode**
  + eval CLI asserting on *actions*. Selective abstention
  (`mappings.md` §2). 24-row filter 48.9 s Claude CLI vs 1.3 s Jev.
  README this pass still that contract. Not a compact-transcript
  replacement (their own "what this is not").
- [`rajdhakad9826/routeKit`](https://github.com/rajdhakad9826/routeKit)
  (MIT, TypeScript, created 15:25Z, 2★): Jev estimates task
  *requirements* (difficulty / reasoningNeed / ambiguity /
  toolComplexity); **code** applies hard constraints (context, tools,
  vision, structured output) and a deterministic policy (cost / quality /
  latency / balanced). Jev does not pick the model. Fallback is
  configured. Early development. Placement: selector + policy
  (`applied-mappings.md` §5). Hypothesis until measured on *your*
  catalog. Do not copy the client signature.

### HacksonClark discourse (SREGym-Lite) — rank tests, do not diagnose

[@HacksonClark](https://x.com/HacksonClark/status/2100993319878721665)
(2026-09-18T17:00:16Z) + blog
[sregym.com/blog/jev-sregym-lite](https://sregym.com/blog/jev-sregym-lite)
(HTTP 200). Codex harness, `gpt-5.6-luna`, 10 SREGym-Lite problems × 5
attempts: **20/50 → 24/50** (40% → 48%). 4 faults improved, **2
regressed**, 4 unchanged. Authors: not a universal 8-point gain.
Biggest lift: internal traffic policy 0/5 → 3/5. Tools: `jev_plan`
ranks 3–5 proposed tests (does not run them, does not reveal the
benchmark answer); `jev_submit` reviews evidence at 0.70 on every
required question before diagnosis/mitigation. **Jev did not diagnose.**
Finding 3: it can only rank hypotheses it receives; a high score cannot
compensate for missing evidence. Finding 2: "healthy now" ≠ durable
repair (quota left in place; unsafe rollout strategy). Future work
(untested): action-loop votes, prospective mitigation-safety.

Placement sentence, same thread
([@Antoniocoppe](https://x.com/Antoniocoppe/status/2100993869680615552)):
"Jev ranks next tests/evidence; it shouldn't diagnose. Keep tests
closed and inspect 2 regressions as calibration failures (was
confidence high on the wrong Choice?). Low-confidence rankings can go
back to the agent instead of silently steering mitigation."

That is VOI / gather (`mappings.md` §6) + selective abstention (§2) +
harness triage (`applied-mappings.md` §3) + dual-orchestration topology
A (Jev-as-tool). Closed candidate set is already a non-negotiable
(`SKILL.md`). Not an SREGym how-to; not a 0.70 to copy.

Cards: `judgment-class.md` when-to-use; FAQ; `applied-mappings.md` §1 /
§3 / §5; `mappings.md` §5 (tree) and §6 (next-test as gather);
`mixed-architecture.md` on-device + routeKit; `validation.md` mini-jev
IIA surface; `formal-methods.md` logit dump still isn't a proof.
## 34. Erik Meijer — not probabilistic programming (2026-09-18)

[Post](https://x.com/headinthebox/status/2100984170004824221) (Erik
Meijer, `headinthebox`, 2026-09-18T16:23:55Z). HTTP 200. X API
`note_tweet` is the full text. It quotes
[jamespearce](https://x.com/jamespearce/status/2100859300038234473)
asking for a take given Meijer's Facebook probabilistic-programming
history. **Claim** as his correction, not a TypeSafe contract.

**What he says.** "I think Jev is a cool API, but it is not
probabilistic programming; qualifying it as a Kleisli arrow that I
have seen people do here is exaggerating." He endorses the gloss:
**"Jev gives you the marginals; a decoder gives you the joint."** In
ordinary words from the note, not a category-theory lesson: N questions
about one fixed state are a fan-out. You get N marginals, not a
distribution over the tuple. The jointly best answer need not be the
tuple of marginally best answers. A later question is read off the
same state, never off an earlier answer, and there is no conditioning
update. He says Jev emits a fixed readout.

**Design card** (`judgment-class.md`). System One / Jev-class =
factorized marginals over typed questions given shared state. That is
§31 item 7 and the compute-graph card, cited, not copied. The joint
lives in application code, sequential TypeAR, or a generative decoder,
not inside one Jev call. Do not market or teach Jev as a probabilistic
programming language or as Kleisli sugar. Frames: decision theory,
calibration, value of information (`mental-models.md`). Joints and
invariants: TLA+ / Alloy / contracts. Fast calibrated factors: System
One. One paragraph there, not a new formal-methods doctrine. A Noul is
still not a proof.

FAQ row. One mental-models sentence. One SKILL.md trigger.

## 35. Bespoke Nimble — open recipe, not a distill (2026-09-18)

HTTP 200 this pass:
[bespokelabsai/nimble](https://github.com/bespokelabsai/nimble) README
(raw `main`),
[bespokelabs/Bespoke-Nimble-9B](https://huggingface.co/bespokelabs/Bespoke-Nimble-9B),
[announcement](https://x.com/madiator/status/2100990591215783946)
(Mahesh Sathiamoorthy, `madiator`, 2026-09-18T16:49:26Z; `note_tweet`
present).

**License.** Model-card frontmatter: `apache-2.0`, `library_name:
peft`, `base_model: Qwen/Qwen3.5-9B`, `base_model_relation: adapter`,
tag `lora`. **Contract** as that card. GitHub API `license` is null;
raw `LICENSE` is HTTP 404. The repository is not Apache-2.0 on the
evidence in hand.

**Recipe (Contract as the README).** They did not distill from Jev.
LoRA on Qwen3.5-9B (rank 16, lr 5e-5, effective batch 8, seed 17, one
epoch, BF16, 2,048-token limit), cross-entropy over allowed candidate
logits, hard reference labels not derived from Jev. Saved Jev
probabilities are described as available for a future soft-target run,
not used in the published objective. Contrastive curation: two examples
differ in one focus fact (at most eight words in one evidence
sentence) so the correct answer flips; question and policy stay.
Labels are synthetic; a model checked them; no person has reviewed
them. `data/train.jsonl` has 2,826 rows; 2,676 trained the published
model, across 10 categories. Holdout `data/eval.jsonl` is 324 examples
(162 pairs, six source families). The tweet adds "No RL yet" and
"calibration is implicit." The README says temperature was not tuned
so probabilities match how often answers are right. Implicit
calibration is a **claim**, not a measured ECE.

**Holdout agreement (Empirical as their named receipt, not a
ranking).** Same 324 synthetic labels. Not re-run here.

| Model | Matches | Agreement |
|---|---:|---:|
| Jev 1.13.0 | 302/324 | 93.21% |
| Bespoke-Nimble-9B | 292/324 | 90.12% |
| Qwen3.8-27B (untuned, their word) | 275/324 | 84.88% |
| Qwen3.5-9B base | 215/324 | 66.36% |

The announcement rounds these to about 93 / 90 / 66. The infographic
rounds to 93.2 / 90.1 / 66.4. The table is the receipt. They call the
test narrow. Jev figures are a reused API run; Nimble figures a reused
earlier H100 run. **Hypothesis:** a 9B open LoRA is enough versus
proprietary Jev on your labels. The 3.09-point gap on this set is an
existence proof that the gap can be small, not an ordering.

**Serving (README; not copied into skill cards).** Candidate codes are
one token; logits become probabilities by softmax. On Mac,
`ParallelScorer` processes the shared context once, then scores
fields. The CUDA scorer repeats the full prompt per field. Fields
cannot see each other. Text only, even though the base model has a
vision part. An enum has 1 to 26 choices. Prompts over 2,048 tokens
are rejected, not truncated. Probabilities sum to 1 over the supplied
candidates and are not a correctness guarantee; add an answer that
means "no match" if none may fit. That is the standing
Choice-conditional-on-offered-set boundary, pointed at, not restated.
The tweet's "100ms on H100" is not the table: Nimble median 106.0 ms
on 120 H100 examples, and 444.0 ms median on an M5 Pro for all 324.
"Parallel constrained decoding" is the announcement's name for the
serving idea; the README mechanism is candidate-logit scoring. Do not
promote 100ms.

**Placement.** (a) open training recipe for the class; (b) contrastive
curation beside RLCD, not a replacement; (c) Hypothesis until your
labels; (d) jevals bake-off candidate beside Laya / openjev-lm /
TypeAR. Not a how-to. Card: `judgment-class.md`. One sentence:
`validation.md`.

## 36. djev-spark — diffusion backbone, Jev-shaped I/O (2026-09-18)

[mmastrac/djev-spark](https://github.com/mmastrac/djev-spark) README
HTTP 200. GitHub API license null. Description: "DiffusionGemma NVFP4
structured decisions on a DGX Spark: container recipe." Pushed
2026-09-18T17:03:19Z.

**What the README says (Contract as that file).** DiffusionGemma
26B-A4B (NVFP4) on a DGX Spark, or another GB10 box. A container runs
an engine with structured-reads patches and a server that speaks Jev's
`POST /v1/systemone`. Patches cited as
[vllm-project/vllm#57250](https://github.com/vllm-project/vllm/pull/57250)
(HTTP 200; patch body not reviewed) on fork branch
`structured-reads-spark` (HTTP 200). `model` is ignored. No API key
unless one is set. Images are an extension: the README says Jev's API
has no images; this server takes multipart or JSON base64, ahead of
the state. `think` and `sequential` need a text-only state and return
422 with images. `sequential` (default false) runs chunks so later
answers condition on earlier ones. `think` (default 0) allows tokens
before the read. `samples` defaults to `"auto"`: one read, then more
if entropy is above `auto_threshold` (default 0.1), up to `auto_max`
(default 4). Latency tables on one GX10, dated 2026-09-18, are
**their** receipt — not re-run, not a class benchmark. Do not copy
routes, ports, env, or patches into skill cards.

**Status.** **Empirical** as a public repo and interface claim.
**Hypothesis** that diffusion structured reads beat a trained decision
head on your task. Third compute graph for Jev-shaped I/O: trained
decision-only transformer, constrained AR (TypeAR, §32), this.
Image-in System One without waiting on Hume's audio-less drop, which
stays **WATCH** (§31). Not a new species. The holes table in
`judgment-class.md` is extended with this graph; the seven-point essay
is not rewritten.

## 37. Light discourse — "welcome back ResNet-50" (2026-09-18)

[tenderizzation](https://x.com/tenderizzation/status/2100766765043343689)
(2026-09-18T02:00:01Z, HTTP 200, no `note_tweet`; the `text` field is
the whole post): "when they said it was a classification model it
suddenly all made sense. welcome back ResNet-50." Cultural landing of
"it's just classification." Not a design card. The FAQ already answers
that question and was not expanded.

## 38. Alex Atallah — entropy buckets as an allocator (2026-09-18)

Two posts, Alex Atallah (`alexatallah`, OpenRouter CEO). Direct X fetch
was HTTP 403. Both verified via `api.fxtwitter.com` (`code` 200), and
the later post's `quote` object is the earlier post.

- [Buckets](https://x.com/alexatallah/status/2099511056989147147)
  (2026-09-14T14:50:17Z). He tells customers to decompose AI tasks into
  three buckets: low entropy, example "who should review this PR";
  medium, example "review this PR"; high, example "write a PR". He
  thinks today you only need frontier models for the third. Two photos
  attached (OpenRouter "Log Cost vs Log Usage by Category"). Bands are
  labeled Deterministic / Semi-variable / Variable. One overlay points
  programming at code scanning, code review, and code writing. Axis
  figures and the other category dots were not transcribed. Not a
  benchmark. Not copied into the card.
- [Quote](https://x.com/alexatallah/status/2100962947711295557)
  (2026-09-18T14:59:35Z), quoting the first. Claim, his words in short:
  Jev by TypeSafe is the first model ever to truly optimize for low-
  and medium-entropy tasks. **Claim**, not an Empirical fact. No
  `note_tweet`.

**Design card** (`judgment-class.md`, entropy as allocator;
when-to-use pointer). Map the work before the model. Typed low- and
medium-entropy *decisions* → System One / Jev-class, factorized
marginals (Meijer, §34: not a probabilistic program, not Kleisli).
High-entropy *synthesis* → a generative frontier decoder, the joint.
Same axis as VOI / compute budget (`mental-models.md`). Agent loop:
many cheap low-entropy scorers per turn; a high-entropy write is rare
and downstream. Code fuses the marginals.

**Caveat (load-bearing).** "Review this PR" as medium entropy is still
partly generative. Treat Atallah's buckets as product rhetoric that
needs a decision-versus-generation cut, not a literal entropy meter.
"First model ever" is a claim, not an Empirical fact.

Formal methods, one sentence: low- and medium-entropy decisions are
where contracts, property tests, and gates attach; high-entropy
writing is where specs stay soft. Not a new mappings §N (§19 stays
Ward). **Hypothesis** until a labeled act/outcome log shows the cut
beats a frontier model on every bucket, on your costs. No API, port,
env, or CLI.

## 39. Perception specialist then judgment specialist (2026-09-18)

**Attribution.** Basit ask, primary post not retrieved. Searched X
(`Basit` + Jev/SAM; `SAM 3.1` + Jev) and the web on 2026-09-18. The
token "basit" mostly hit Turkish "simple," not a person. No tweet id
invented. The design card is **Hypothesis** from that ask, not from a
verified post.

**SAM 3.1 is Meta Segment Anything 3.1 (verified name, not a copied
API).** [facebook/sam3.1](https://huggingface.co/facebook/sam3.1) HTTP
200 (gated raw README 401). [RELEASE_SAM3p1.md](https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md)
HTTP 200: Object Multiplex, shared-memory joint multi-object tracking,
checkpoints on that Hub repo, 27 Mar 2026. [Meta blog](https://ai.meta.com/blog/segment-anything-model-3/)
HTTP 200. Output of the species is masks and tracks. **Perceive.**
Not a SAM tutorial. No routes, ports, or install copied.

**ASR + Jev** is the same composition: a transcript is perceive;
System One decides on utterances. Independent public instance, not
Basit: [Moritz Kremb](https://x.com/moritzkremb/status/2100577979021832365)
(2026-09-17T13:29:51Z, `note_tweet` present). Talk → transcript → Jev
probabilities → browser click. His ~300 ms and $0.0002 are his
receipt, not a class number.

**Not native omni System One.** Information dies at the interface: the
decision call sees the schema you serialized, not the pixels or the
waveform. Prefer a shared multimodal decision model when the joint
signal matters. Archer Hume stays **Watch** (no Hub weights this pass;
multimodal, no audio; do not promote to Empirical). djev-spark images
are the third compute graph (§36): multipart or JSON; think and
sequential reject images. Future audio-capable shared models are the
same hole.

**Fits the allocator, does not restate it.** Low/medium entropy (§38)
is product rhetoric for "specialist state, then a typed decision," not
a meter. "Review this PR" stays partly generative. One Jev call is
still Meijer's factorized marginals (§34); the joint of the raw signal
and the decision lives outside the call. Not a probabilistic program.
Not Kleisli. A Noul is not a proof and is not over raw pixels or raw
audio. The handoff is a contract surface — one sentence in
`formal-methods.md`. Code owns the schema and the act.

Card: `judgment-class.md`. One composition sentence:
`mental-models.md`. SAM and ASR are upstream producers, not the
perceive species; Jev on that state is decide. Composition ≠ one model.
Corrected in §43; the first draft of this section called them perceive.

## 40. Eval & hill-climb — jevals practices + Harbor substrate (2026-09-18)

**Attribution.** Basit standing order: imbue jevals practices and Harbor
as the ideal measurement / hill-climb substrate, while Augustus stays
design judgment. Primary post not retrieved. X search for Basit +
jevals/Harbor returned nothing. No tweet id invented. Clauses the
fetched docs do not state are labeled "Basit ask, primary post not
retrieved."

**Jevals files fetched** at commit `af6fecc` (GitHub contents API):

- [README](https://github.com/dayhaysoos/jevals/blob/af6fecc0776dd5d97d5dc89fc0a72cae5e3e2580/README.md)
  — local MIT workbench; Noul / Choice / Score and combinations;
  documented entry is `npx jevals`. Not copied beyond that one fact.
- [PRODUCT.md](https://github.com/dayhaysoos/jevals/blob/af6fecc0776dd5d97d5dc89fc0a72cae5e3e2580/PRODUCT.md)
  — correctness separate from model probability; compare only equivalent
  case sets; editable cases and immutable runs; only fully successful
  runs qualify as best. An earlier sentence says Score execution is
  future work; a later sentence says Noul, Choice, and Score are
  enabled, and README/DESIGN treat Score as present. Taught as enabled.
  PRODUCT also says no npm publication; the README is what documents
  the entry command. Not reconciled further.
- [DESIGN.md](https://github.com/dayhaysoos/jevals/blob/af6fecc0776dd5d97d5dc89fc0a72cae5e3e2580/DESIGN.md)
  — stable question IDs; best-run labels only for complete runs on the
  same case set; no blended accuracy across evaluations; question-scoped
  ranking; confidence describes the distribution rather than establishing
  correctness; Choice multiclass Brier; Score MAE and within-tolerance;
  unset expectation blocks a run; runs open immutable snapshots.
- [skills/jevals/SKILL.md](https://github.com/dayhaysoos/jevals/blob/af6fecc0776dd5d97d5dc89fc0a72cae5e3e2580/skills/jevals/SKILL.md)
  — paraphrased, not copied. WebMCP order: discover → define → author
  independent keys → save/verify → run → inspect. No dedicated split
  control (separate held-out Jeval). Do not encode unsupported
  `unknown` labels. README, PRODUCT, and DESIGN do not themselves say
  "no built-in split"; the skill does, and those three files do not
  document one.

**Dropped or narrowed.** Did not paste flags, env, or ports. Did not
claim PRODUCT/DESIGN/README contain the words "no built-in split" or
"unknown" — those limits are the agent skill, plus DESIGN's unset
expectation. Did not invent a Harbor CLI.

**Harbor / verifiers (verified, not previously named in this repo).**

- [harbor-framework/harbor](https://github.com/harbor-framework/harbor)
  README: Terminal-Bench creators; evaluate and optimize agents;
  shared benchmarks; parallel environments; rollouts for RL.
- [Task structure](https://www.harborframework.com/docs/tasks): default
  verifier shares the agent container. Separate verifier environment
  when grading must not be visible; sidecar evidence from a filesystem
  the agent container cannot write.
- [PrimeIntellect-ai/verifiers](https://github.com/PrimeIntellect-ai/verifiers)
  (Will Brown) and
  [verifiers v1](https://www.primeintellect.ai/blog/verifiers-v1)
  (Will Brown, Mika Senghaas, Florian Brand, 2026-07-10): taskset =
  data, tools, scoring; harness = rollout program; runtime = where it
  runs. Harbor is a taskset format inside verifiers, not a second
  product.

**Basit ask, not in those docs.** Write the score before picking a
model (the blog does put scoring on the taskset). Room driver and live
Room as harness/runtime examples. If only one harness passes, you
measured the harness. HoH: Planner (no code) → Developer (single
writer) → QA (read-only, evidence E); next loop from (A, E). Room/omni:
structural gates first, video-as-judge last. Composes with §39
(information dies at the interface; Noul is not over raw pixels) and
with `mappings.md` §18.

**Does not contradict.** Meijer: marginals, not a PPL, not Kleisli.
Nimble: not a Jev distill; model card Apache-2.0; repo LICENSE 404;
holdout is agreement, not ECE. djev-spark stays a third graph. TypeAR
is constrained AR. openjev-lm keeps that name. Atallah buckets stay
rhetoric; "first model ever" stays a claim. Archer stays Watch (no Hub
weights as of 2026-09-18). "9B LoRA enough vs Jev" stays Hypothesis.
LLM-as-judge is not the primary System One score. rh-guard is one
composition-table row, not a jevgate rewrite.

**Shorter hill-climb card, upgraded, not deleted.** A concurrent fold
had a pipeline / measure / hill-climb card. Its one-liner is the Order
line of `validation.md` Eval & hill-climb. Kept from that card, not
restated as a second essay: stages (perceive → optional fusion →
typed marginals → policy in code); versioned handoff contract; stage
metrics IoU, track IDF1, WER, plus decision Brier/ECE and policy
regret; frozen taskset; falsifiers (contrastive pair, garbage-in,
TOCTOU); HoH changes one stage or one interface; climb axes include
collapsing to a shared multimodal model only when interface loss
stalls end-to-end. DSPy/Ax remain the LM-program slice only.

**Skill.** One section: `validation.md` Eval & hill-climb. Pointers in
SKILL.md (triggers, index, card field), when-to-use, mental-models
calibration, optimizer-integration (no API shapes). No second table.

Card is **Contract** as the fetched workbench and Harbor/verifiers
docs, **Hypothesis** as the Basit loop (HoH, Room, video-last) until
the post is retrieved. Not a how-to.

## 41. Pipeline, measure, hill-climb perception into a decision (2026-09-18)

**Attribution.** Same Basit ask as §39 and §40, a different question:
how to pipeline, measure, and hill-climb perception into a decision,
and the narrow Ax versus DSPy answer. Primary post not retrieved.
Searched X (`Basit` + SAM/Jev; `SAM` + Jev) and the web on 2026-09-18.
No tweet id invented. Do not treat §40's HoH paraphrase (Planner writes
no code) as replaced. This note's hill-climb is the stage reading:
Planner writes a bounded change from evidence; Developer changes one
stage or one interface; QA is read-only on a frozen taskset and emits
the next evidence.

**Ax identity (verified).** [ax-llm/ax](https://github.com/ax-llm/ax)
README, fetched 2026-09-18: "DSPy for TypeScript." Already listed in
`sources.json` (typesafe-provider note). Not a second URL. Not a call
shape. DSPy is the Python counterpart. Both climb LM-program knobs
only: prompts, demonstrations, module graphs, sometimes model choice.
Use on a generative or constrained-AR head (TypeAR, schema-prompted
LLM) and on an optional rewrite of a perception-to-state summary. Do
not expect them to climb SAM multiplex, ASR decoding or diarization,
Jev calibration, or pair-versus-native-omni. Proprietary Jev: schema,
criteria, and thresholds on labeled eval (jevals), not a search over a
decoder. Nimble: data curation and LoRA; published holdout is agreement
on synthetic labels, not a measured ECE (§35).

**Card.** `validation.md` pipeline section. Cross-links: perception
card (`judgment-class.md`, §39), entropy allocator (§38, not a meter),
Eval & hill-climb (§40 — Harbor / Verifiers / jevals hygiene, not
restated). One-liner in `mental-models.md`. One hill-climb pointer in
`formal-methods.md`; the versioned-contract sentence was already there
and was not rewritten. Judgment paragraph in
`optimizer-integration.md` with no new call shape. Mapping-index row
and description triggers only.

**Does not contradict.** Meijer: marginals at the decision stage;
joints across stages live in code. Atallah: rhetoric, not a meter;
"review this PR" is partly generative; "first model ever" is a claim.
openjev-lm keeps that spelling. Fail-open is not universal. A Noul is
not a proof and is not over raw pixels. **Hypothesis.** No CLI, env,
port, or install.

## 42. Hourly fold ~11:59 America/Boise (2026-09-18) — serving, meta-VOI, env vs policy, store, games

Window: America/Boise ~11:59 ≈ 17:59 UTC. Novel versus §33 (~11:02).
Docs-only. No Jev wrapper, no serving-stack how-to, no copied
`predict()` / env / hook regex / OpenAPI. Local path
`/workspace/jev-archive/2026-09-18/175905` was not present this pass;
GitHub READMEs, Hub cards, and X posts fetched live. HTTP 200 on every
cited URL below. Archer drop still **WATCH**: Hub `archerhume` /
`4rcherhume` empty; latest `@4rcherhume` posts this calendar day are
replies (newest 14:39Z "I realise that now…"). Expected ~19 Sep Boise.

Five frames, then the artifacts.

**(a) Three open paths, not three species.** Encoder open-jev
(DeBERTa), AR constrained decode (TypeAR + native serving), trained
decision-only (Laya / Nimble / Archer Watch). Constrained softmax over
allowed tokens is still not a Noul.

**(b) Meta-VOI.** Abstain from calling *any* model when a regex, DNS
lookup, or query already answers. The System One band is "a sensible
person answers in under a second from text you can show them."

**(c) Env-break vs policy-break.** OpenSmoke's cut is already the
harness-triage card; this hour the README names it: `env_broken` as
opposed to the agent's own bug; pre-mortem of a new sandbox *before*
users meet it.

**(d) Store as decision surface.** Vanilla Postgres never learns
`jev()`; the CLI judges schema-conditioned row objects. Cheap SQL
first; row contents leave the database.

**(e) Game loops as calibration / hill-climb substrate.** Legal moves
from code; Choice over that set; option-order and confidence-vs-correct
are the tests. Probabilities are not win odds.

### HIGH

1. **[`stephanj/pcdServer`](https://github.com/stephanj/pcdServer)**
   (created 17:06Z, MIT, C++20, 0★ this pass). Native Parallel
   Constrained Decoder REST for Apple Silicon (Metal) and Linux
   (llama.cpp GGUF). Same *family* as TypeAR (§32): next-token
   constraint, not a proper-scoring head. Differences that matter for
   placement: 2–256 string choices per field (TypeAR README enums
   ≤16); 1–63 parallel fields sharing one prefix checkpoint; booleans
   as `[false, true]`; collision-tree for shared prefixes; full
   sequence checkpoints because Qwen3.5 hybrid recurrent state cannot
   be partially rewound. Default demo GGUF is Qwen3.5-0.8B-Q8_0. The
   model never writes JSON syntax; the server assembles values from
   allowed scalars and returns a softmax over those scalars. That
   distribution is still not a Noul. Tetris view: every piece is one
   decode — game loop as a constrained-decode demo, not a strength
   claim. No auth; default bind is loopback. Cousin of the same
   author's `parallelConstraintDecoding` (already in the ecosystem
   snapshot). Do not copy OpenAPI, flags, or install. Card:
   `judgment-class.md` constrained-AR row.

2. **[`kylemclaren/jevql`](https://github.com/kylemclaren/jevql)**
   (already in the gallery; this hour the *store* frame). Semantic SQL
   over vanilla Postgres: `jev` / `jev_prob` / `jev_choice` /
   `jev_score` as schema-conditioned typed questions on row objects.
   The database only ever sees ordinary SQL. Full scan of the
   post-SQL-filter row set — indexed predicates first; `--explain`
   counts before you pay. Row contents go to TypeSafe: same residency
   warning as AU health (§33). Not a Postgres extension. Do not copy
   connection strings. `mixed-architecture.md` gallery; `mappings.md`
   §4.

3. **[`aaravriyer193/OpenSmoke`](https://github.com/aaravriyer193/OpenSmoke)**
   (already §3; this hour the cut is explicit). Per step, one request:
   Noul `env_broken` *as opposed to* the agent's own bug; Choice
   category (`missing_credential`, `broken_tool`, `network`, …);
   Noul `workaround`. Run status silent / disclosed / recovered /
   clean. Heuristic judge on 12 labeled traces: precision = recall =
   0.86; `jev-1.13` "not yet measured" on that fixture — do not invent
   a number. Pre-mortem shape: scan an eval suite against a new
   sandbox image and fail the build on *silent* env-breaks. Motivating
   case unchanged (KeyError then "Done!"). `applied-mappings.md` §3.

4. **[`ddfeyes/jev-mode`](https://github.com/ddfeyes/jev-mode)**
   (created 14:51Z, MIT, Python, 0★). Move bulk semantic judgments out
   of frontier context (triage 400 tickets, tag files, six-way route)
   onto a typed decision model. Measured on 1,000 synthetic triage
   judgments vs a Jev-free control: −77.8% tokens, 16× less
   work-attributable input, 40→14 round trips; department accuracy
   96.1% vs 93.7%. Author's own hedges: control ranged 93.4–98.2% so
   the honest claim is **parity**, not superiority; corpus is
   synthetic so the **token ratio** is the durable result. Question
   design moved 5–12 points (one terse Choice beats nine atomic
   Nouls; one record per call). Step gate: fail-open; consecutive
   denial budget (lifetime budget was wrong); `unsafe` recorded not
   enforced. Latency-class split: leaving those 400 tickets in the
   frontier loop **stalls** later turns (re-read tax); moving them
   off **degrades the frontier to render/write**. Same axis as
   Atallah (§38), not a new meter. Do not copy the client. Cards:
   `mixed-architecture.md`; `applied-mappings.md` §5.

5. **[`runta-dev/jot`](https://github.com/runta-dev/jot)** (created
   10:46Z, license file absent, 1★). "First general-purpose System One
   agent" is a **claim**. Loop: closed tool catalog → Jev picks a
   call → host executes → result back into state. Calculator does the
   arithmetic. That is dual-orchestration topology B with a *closed*
   catalog (`mixed-architecture.md`), not a license to invent tools.
   Hypothesis as a shell; standing red flag if the catalog is open.
   Do not copy `.env`.

6. **[`wotai-dev/typesafe-jev-tools`](https://github.com/wotai-dev/typesafe-jev-tools)**
   (created 17:04Z, MIT, 0★). Claude Code hook that asks whether the
   decision *being written* needs a model at all. Three-way test:
   (1) regex / DNS / query → write the code; (2) multi-step reasoning
   or generated prose → frontier; (3) one-second human from shown text
   → System One. Never blocks; recommends plain code at least as
   often. **Empirical as a 149-row receipt, 2026-09-18, same business
   rows:** Jev `jev-1.13.0` 79.9% / p50 432 ms / p95 620 ms / 507 in +
   84 out tok; Claude Haiku 4.5 **83.2%** / 702 / 1,244 / 422 + 19.
   Agreed 143/149. Jev 1.6× faster, **not** the 20–200× landing-page
   band. Jev accuracy climbs monotonically with stated confidence
   (0.00–0.60: 28.6%; 0.95–1.00: 93.9%). Haiku **inverts** in
   0.80–0.95 (55.2%). Haiku produced 10 distinct confidence values and
   put 0.95 on 98/149; Jev 32. TypeSafe `/pricing` and `/limits` both
   404 this day, so "40 to 1,000× cheaper" is not checkable. Punchline
   the hook exists for: if your code does not *branch on confidence*,
   use whatever you already have. Do not copy the hook matcher. Cards:
   `mappings.md` §6; `mental-models.md` VOI; FAQ.

### MED

7. **[`memovai/openevals`](https://github.com/memovai/openevals)**
   (created 07:43Z, MIT, 1★). Online, every trace, every step, written
   back to Langfuse. Code graders first (free, crisp); Jev per-step
   four questions (progress / on_task / redundant / corrective);
   low-confidence / Noul≈0.5 escalates. Calibration vs human
   ANNOTATION scores (κ, MAE, false-pass). Adjacent to jevals/Harbor
   (§40): Harbor is an offline product taskset; this is production
   full-traffic measurement. Same full-traffic portent already in
   `judgment-class.md`. Do not copy env. `validation.md` one sentence.

8. **[`poponline63/hermes-jev-north-star`](https://github.com/poponline63/hermes-jev-north-star)**
   (created 10:37Z, MIT, 1★). Intention → checkable finish line.
   Two-layer gate: deterministic shell checks first (failure
   short-circuits); empty evidence **refuses to judge**; then one Jev
   call (Noul every-requirement, Score progress, Choice weakest).
   Empty state was self-contradictory (0.14 done beside "nothing
   met") — that is why the refuse-empty rule exists. Numbers move
   between calls on the same state: treat the threshold as coarse;
   deterministic checks are load-bearing. `mappings.md` §18 / §12.

9. **[`TheoOliveira/pi-jev`](https://github.com/TheoOliveira/pi-jev)**
   (created 17 Sep, MIT, 6★). Semantic tool/skill routing + typed
   `jev_evaluate` for the Pi coding agent. **Not**
   `kevinpita/pi-jev-context` (sieve). Fail-open to local keyword
   shortlists. Auto-mode / compaction / auto-model are opt-in.
   `applied-mappings.md` §5.

10. **`rajdhakad9826/routeKit`** — already §33. Still Hypothesis until
    *your* catalog. No rewrite.

11. **[`vtrivedy/jev-plays-games`](https://github.com/vtrivedy/jev-plays-games)**
    (created 17:57Z, license file absent, 0★). Chess / Connect Four.
    Board → legal moves from code → one Choice over that set →
    validate. Text state, no screenshot. Choice probabilities **are
    not win odds**. Probe (author, 12 paid calls, both option orders):
    both chess mates found; Connect Four immediate win missed once
    under reversed order; Fool's-mate confidence 31% and 37% — a 0.50
    gate would reject both correct mates. Self-play chess hung a queen
    on move 2 and drew by repetition; Connect Four filled columns then
    won the bottom row. Small selected sample; reversing options is a
    new call, so it does not isolate IIA from request noise. Hill-climb
    substrate: option-order, confidence-vs-correct, state-format
    ablations. `mappings.md` §9; `validation.md`.

12. **[`ant4g0nist/joxide`](https://github.com/ant4g0nist/joxide)**
    (created 17:36Z, license file absent, 0★). zoxide owns the index;
    Jev scores a shortlist of known directories by description.
    Destinations come only from existing local paths. Fail-open (API
    error leaves you where you were). Thresholds are initial policy,
    not calibrated guarantees. `mappings.md` §4.

13. **[`convaiinnovations/laya-typed-decisions`](https://huggingface.co/convaiinnovations/laya-typed-decisions)**
    (created 17:45Z, apache-2.0, 421.3M — same parameter count as
    `convaiinnovations/laya`). Companion packaging: Hub tags
    `typed-decisions` / `system-one` / `rlcd`; model-index on
    `LocalLLaMA/typed-decisions` acc **0.766** / Brier **0.066**,
    `verified: false`. Not a new architecture. Do not overwrite §18
    ECE claims. Point at Laya as the trained decision-only open path.

### X discourse this hour (verified)

- [@jsmagoon](https://x.com/jsmagoon/status/2101008113952567316)
  (17:59:03Z): "dynamic classifiers based on user input" / "derive the
  output schema at runtime." Still a **closed set at request time**.
  Not generation. IIA/envelope still apply.
- [@yoheinakajima](https://x.com/yoheinakajima/status/2101008182521037242)
  (17:59:20Z): chat/beep sees typing live; Enter clears. Live
  keystroke sieve — judge on partial state; sequence-tagged staleness
  already in the latency-first archive. Hypothesis as a number.
- [@IAmMattGreen](https://x.com/IAmMattGreen/status/2101008081962614823)
  (17:58:56Z): a use-case "could immediately cut our costs by 60%."
  **Claim**, not a labeled receipt.
- [@mrluiscalderon](https://x.com/mrluiscalderon/status/2101007751098851382)
  (17:57:37Z): Coach testing "~20× faster"; "quality still needs
  verification."
- [@thePartyPartyUS](https://x.com/thePartyPartyUS/status/2101007875313205573)
  (17:58:06Z): "classifiers are cheap… jump on GLiNER." Species-map
  lesson already taught; do not adopt "Jev will be discarded."
- [@Yash_Bhadange07](https://x.com/Yash_Bhadange07/status/2101007720195498235)
  (17:57:29Z): closed Jev → FunctionGemma for Android tool calling.
  Same hole as jev-mobile / AU residency: deployment control, not a
  FunctionGemma tutorial.
- [@linfluence](https://x.com/linfluence/status/2101008235385794628)
  (17:59:32Z): fintech / market-structure; LLMs price on a paragraph a
  user reads; software-native unit is a decision.
- [@brunoqgalvao](https://x.com/brunoqgalvao/status/2101008125356626019)
  (17:59:06Z): takeaway — new Pareto of performance/cost will drive
  many use cases, especially latency. The numbered receipt he is
  closing (16:53Z, ~1,200 items, four classification tasks): Jev
  91–96% vs flash 96–99%; 23× faster and 39× cheaper than flash at
  1–5 accuracy points; yes/no ECE 8–15% over-hedge vs flash 0.5–2%.
  **Author-reported**, not re-run. Ranking "is good though." Do not
  overwrite in-dist ECE 0.0313 (§7) with this phishing-set ECE.

Cards: `judgment-class.md` three open paths + pcdServer on the TypeAR
row; FAQ; `applied-mappings.md` §3 / §5; `mappings.md` §4 / §6 / §9 /
§18; `mixed-architecture.md` gallery + topology B; `mental-models.md`
VOI; `validation.md` games + openevals; `formal-methods.md` softmax
still isn't a proof.

## 43. Second adversarial pass (2026-09-18) — review findings, not doctrine

Read-only pass on HEAD `7b3a0c3` (whole skill, not only the diff).
Prior memo is §27 at `31c8914`. §27 fixes still held: per-action fail
policy, Nimble license split, openjev-lm 92.9 vs 98.1, Archer Watch,
Ward as ZIO, jevgate constants not universal, Noul is not a proof.
Zero blockers. Four candidates dropped after a second read (Harbor
"first fully supported" is verbatim in the verifiers v1 post;
`mini-jev-runs` has two legitimate uses; SKILL.md "translation-invariant"
names the discriminative family; SREGym 20/50→24/50 is attempt-level,
improved/regressed is over 10 faults).

Kept, and patched in the cards:

1. `validation.md` named `npx jevals` as a verified entry. PRODUCT.md at
   `af6fecc` says no npm publication. The command is gone from the card.
   Flags, keys, and ports stay in that README.
2. SAM 3.1 and ASR were called the **perceive** species. Perceive scores
   candidates you already extracted (CLIP / SigLIP / region Choice).
   Masks and transcripts are upstream producers. `judgment-class.md`,
   `docs/ecosystem.md`. §39's species sentence corrected above.
3. `optimizer-integration.md` said "no call shape" and then showed
   `ai({name:'typesafe'})` and `paw.compile(...)`. Those two forms are
   gone. Seat names stay. `paw.compile` had no symbol in the archive.
4. Proprietary Jev latency cell now tags ~$0.042/MTok as their figure;
   `/pricing` 404 on this day (§42).
5. GodsBoy 94.4% in `applied-mappings.md` §5 now says exploratory
   (questions revised after the first full run). §7 already had the
   leakage note.

Not patched, standing risk: doctrine is copied across cards and the
next fold is where copies drift; `notes.md` §1 is a one-day pin, not a
live contract.

## 44. Hourly fold ~12:58 America/Boise (2026-09-18) — store siblings, hard envelopes, distill-to-device, harness practice

Window: America/Boise ~12:58 ≈ 18:58 UTC. Watch run 185349. Novel
versus §42 (~11:59). Docs-only. No Jev wrapper, no serving-stack
how-to, no copied SQL/`advise()`/proxy ports/`predict()`. Local
`/workspace/jev-archive` path for this run was not present; GitHub
READMEs, Hub cards, and X posts fetched live. HTTP 200 on cited URLs.
**Archer drop still WATCH** — no architecture rewrite this hour. User
watch says ~65% done, Qwen3.8-27B multimodal no-audio still expected
~19 Sep Boise. This pass did not retrieve a new Archer status tweet
(rate-limit / query constraint); Hub was not treated as a landing.

Do **not** rehash pcdServer, jevql's already-folded CLI frame,
OpenSmoke, jev-mode, jot, typesafe-jev-tools, openevals,
hermes-north-star. Already-folded HIGH from §33 (jev-harness,
openjev-lm, jev-gate-student-b, open-jev-deberta, mini-jev-runs,
jev-tree-choice-cap, jev-pref) get a *frame*, not a second card.

Six frames, then the artifacts.

**(a) Structured-store semantic index.** Cheap exact predicates first;
typed questions on the remainder. Two *forks* of the same hole:
**in-engine extension** (`mgaitan/sqlite-jev`; inspired by
`realZachi/pg-jev`) vs **out-of-process CLI** (`kylemclaren/jevql` —
vanilla Postgres never sees `jev()`). zoxide (`joxide`, §42) is the
same hole over a path index. A semantic full scan is not an index.
Row contents leave the store: same residency warning as AU health
(§33).

**(b) Distill-to-device memory/context gates.** System One as a
**sieve**, not only an action permit. Already §33 / `applied-mappings.md`
§1: `jev-gate-student-b` P(relevant) from yes/no logits. This hour the
meta is: vector recall → local yes/no gate → inject or stub. Fail-open
on errors. Teacher-copy ≠ gold.

**(c) Encoder vs AR open replicas.** Already the three-open-paths cut
(§42). Encoder DeBERTa = public gold, OOD drop; decoder LoRA
(openjev-lm, jev-gate) = teacher-copy; constrained AR (TypeAR /
pcdServer) = softmax over allowed tokens, not a Noul. Do not pick a
path until meta-VOI says a model is needed at all.

**(d) Soft judgment inside a hard safety envelope.** The model may
only **match the envelope or be more conservative**. Deterministic
policy is load-bearing; missing the model must still be safe.
bitrate-advisor is the named live-stream shape. mmalisper's JOB
planner is the named search/control shape (Postgres plans first; Jev
overrides only when confident).

**(e) Perception → decision.** ASR / vision produce schema'd state;
System One decides; code acts. SAM and ASR are **producers**, not the
perceive species (§43). `jev-voice-control` is a README-only stub of
that pipeline.

**(f) Harbor/jevals-style harness + shadow + confidence.** Assert on
the **action**, not on free text. LLM-as-judge is not the primary
System One score (`faq.md`). jev-harness already named this; this hour
the practice is first-class: recipes across alerts / RTB / sports-bet /
prediction-markets, offline fixtures, shadow until evals pass.

### HIGH

1. **[`mgaitan/sqlite-jev`](https://github.com/mgaitan/sqlite-jev)**
   (created 18:25Z, C, license file absent, 0★). Loadable SQLite
   extension: batched NL Noul/Choice/Score over row objects
   (`jev_rows` virtual table; up to 40 rows per shared state).
   Inspired by [`realZachi/pg-jev`](https://github.com/realZachi/pg-jev)
   (in-engine Postgres, 152★ this pass — pointer, not a second card).
   Sibling *pattern* to jevql, **not** the same serving choice: here
   the database *does* see `jev()` as SQL. README limits: semantic
   full scan, not an index; deterministic SQLite filters first;
   `max_rows` is a spend guard; row contents go to TypeSafe. Thresholds
   stay in SQL so they can rise with false-positive cost. Mock-server
   tests never call TypeSafe. Do not copy `.load`, env, or SQL
   signatures. Card: `mappings.md` §4.

2. **[`AntonioCoppe/jev-harness`](https://github.com/AntonioCoppe/jev-harness)**
   — already §33 (policy, confidence gate, shadow, 24-row 48.9s Claude
   CLI → 1.3s Jev). This hour the *practice*: Harbor/jevals-adjacent
   measurement substrate. Eval CLI asserts on the **action**, not on
   prose. Recipes span alerts, NL row-filter, high-freq reflex (order /
   RTB / fraud), prediction-market and sports-bet gates — business and
   life, not SWE-only. Explicitly **not** a `/compact` replacement.
   Do not copy the client. `validation.md`; gallery.

3. **[`DECRUX9812/openjev-lm`](https://github.com/DECRUX9812/openjev-lm)**
   — already §25. This hour the *receipts pattern*: overnight 6-vCPU,
   $0/call, two independently written harnesses both 65/70 = 92.9% on
   the same 70 hand-gold rows; 98.1% on 106 later postings is teacher
   **agreement**, not gold; rare-class cells are one-row wide. Encoder
   vs this decoder LoRA is the (c) fork, not a new architecture. Do
   not copy train commands.

4. **`SargeDev/jev-gate-student-b` + `jev-distill-corpus`** — already
   §33. This hour the meta: **context sieve / memory gate**, not only
   an action gate. Vector recall → P(relevant) yes/no logits → inject
   or stub. Fail-open. Teacher-copy. `applied-mappings.md` §1.

5. **`com-kotobalabs/open-jev-deberta-v3-large`** — already §33
   (434M, Banking77/SST5/BoolQ, in-domain ECE 0.022, OOD acc 0.690).
   This hour: the **encoder** arm of open-replica, as opposed to
   decoder LoRA (openjev-lm / jev-gate) and constrained AR. Public
   gold, not a Jev teacher. Do not overwrite those numbers.

### MED

6. **[`affirmitv/bitrate-advisor`](https://github.com/affirmitv/bitrate-advisor)**
   (created 15:27Z, MIT, TypeScript, 0★). Live-stream ABR: Jev
   proposes initial rung / ceiling / resolution / next step from
   telemetry + venue/carrier history; **deterministic policy fences
   it in**. Jev may be as bold as the measured network allows and as
   cautious as it likes, **never bolder**. Without an API key the same
   call returns the policy's answer (`source: "policy"`). Power plan
   (finish-the-game battery/thermal) is deterministic; Jev may only
   make it more conservative. Author-measured 2026-09-18, three
   states, OpenRouter billed ~$0.000041–0.000044, 0.25–0.39 s; ~$0.015
   per hour of stream at one decision / 10 s — **author-reported**,
   not re-run. Domain: youth-sports phone streams (life / business),
   not a codec tutorial. Empirical as a *shape* for §12 / §15 / §18.
   Do not copy `advise()` or keys.

7. **[`chris-wozniczek/jev-voice-control`](https://github.com/chris-wozniczek/jev-voice-control)**
   (created 18:47Z, license absent, README-only this pass, 0★).
   Speech → Jev typed decisions → macOS actions. Menu-bar Swift
   **claim**. Hypothesis as a product; useful as the perception→decision
   pipeline with ASR as producer (§39 / §43). Do not invent a Swift
   API.

8. **`doeixd/jev-pref`** — already the preference-lint contract
   (YOU define the rule / Jev classifies / code maps outcome). No
   rewrite. This hour it sits next to bitrate's envelope: policy-as-
   prefs is the same ownership split on a diff instead of a live
   stream.

9. **[`nekowasabi/jev-routing`](https://github.com/nekowasabi/jev-routing)**
   (created 08:13Z, MIT, Go, 0★). Host **adapter**, not an MCP
   server: one Go binary in front of Claude Code / Codex / Grok
   Build. Compacts tool results (verbatim drop/truncate, same
   contract as fast-jev-compaction), then one Choice (next tool) +
   Noul (done), then shrinks `tools[]` to **one schema**. README:
   adding this via `mcp add` makes the catalog *worse*. No key →
   on-device classifier. Do not copy ports, env, or install.
   Host-adapter breadth, not a new species. `applied-mappings.md` §5.

10. **[`trietphan/jev-claw`](https://github.com/trietphan/jev-claw)**
    (created 18:44Z, MIT, JS, 0★). Typed routing for OpenClaw
    agents. **Jev classifies** (task_type / complexity / risk /
    second-opinion); **`decide()` in code** maps to a route.
    Sensitive-path regex floors risk even if Jev underrates a
    migration. Confidence is the **minimum** across classifications,
    not the average. 11 offline policy tests (no network). Live eval
    10/10 on the author's 10 samples — **author-reported**, tiny.
    Same hole as routeKit (§33): Jev does not get to skip the
    escalation `if`. Do not copy the eight route names as doctrine.

11. **[`gamesonrblx/JevML`](https://github.com/gamesonrblx/JevML)**
    (created 18:47Z, license absent, README-only, 0★). "PCA / MCMC /
    text-diffusion / NCA primitives + a harness that picks the right
    tool." Meta-VOI adjacent: which primitive, if any. Hypothesis.
    Do not invent those APIs.

12. **`Mikhail/mini-jev-runs`** — already §33 (27.9k option-logit
    runs, frozen Qwen3-4B, no token generated). Calibration /
    constrained-decode corpus. No rewrite.

13. **`reachjalil/jev-tree-choice-cap`** — already §33 / mappings §5.
    Hierarchical Choice under the 255 cap. No rewrite.

### X discourse this hour (verified)

- [@mmalisper](https://x.com/mmalisper/status/2101001041903009987)
  (17:30:57Z) and thread: Jev-assisted Postgres query planner on the
  Join Order Benchmark. Join-order Choice **2× slower** (defaulted to
  smallest table). Cardinality estimates helped when outside context
  informed the plan; when Jev was wrong, one query was an **order of
  magnitude slower**. Hybrid: Postgres plans first; Jev overrides
  **only when confident** → **+12% geomean**, no dramatic slowdowns.
  Downside: a Jev call is 100s of ms, not yet practical on every
  plan. **Author-reported**, not re-run. Frame (d) + search/control
  (§9): the planner is the envelope; confidence is the gate.
  Fail-open to Postgres.

- [@higgsfield_ai](https://x.com/higgsfield_ai/status/2101022473248727177)
  (18:56:07Z) and [demo](https://x.com/higgsfield_ai/status/2101022133753430365)
  (18:54:46Z): "perfect use case" — Jev auto-routes GenAI (video/image)
  models for cost/speed/quality on the Higgsfield API. **Claim**, no
  labeled catalog receipt. Same hole as routeKit / jev-claw:
  classify requirements, policy picks the generator. Hypothesis
  until *your* catalog.

Cards: `mappings.md` §4 / §9 / §12 / §15 / §18; `mixed-architecture.md`
gallery + host-adapter note; `applied-mappings.md` §1 / §5;
`validation.md` harness practice; `mental-models.md` envelope +
planner; FAQ in-engine vs CLI; `judgment-class.md` encoder vs decoder
replica (no new species). No wrapper.

## 45. kev — runnable Archer reconstruction, not a distill (2026-09-18)

HTTP 200 this pass:
[jaredpalmer/kev](https://github.com/jaredpalmer/kev) README (raw
`main`), [MODEL_CARD.md](https://github.com/jaredpalmer/kev/blob/main/MODEL_CARD.md),
[LICENSE](https://github.com/jaredpalmer/kev/blob/main/LICENSE)
(Apache-2.0; GitHub API `license.key` apache-2.0),
[release v0.1.0](https://github.com/jaredpalmer/kev/releases/tag/v0.1.0),
[Archer Hume, *Jev's Architecture Unmasked*](https://archerhume.com/posts/jevs-architecture-unmasked)
(with and without trailing slash), TypeSafe
[System One API](https://docs.typesafe.ai/api).

GitHub API this pass: created 2026-09-17T20:49:39Z; pushed
2026-09-18T19:50:58Z; 24★; language TypeScript (playground); default
branch `main`. Description: "tiny Jev-like model built on top of
Qwen2.5-0.5B you can train and run on your MacBook." Not
`Kevthetech143/super-jev`.

**What it is (Contract as README + model card).** Jared Palmer, Apache-2.0
adapter/head (Qwen2.5-0.5B under the Qwen license). LoRA (r=16) + a
pointer readout on that 0.5B causal backbone. Typed questions in,
calibrated probabilities out, one prefill pass, no decode. State and
questions packed into one sequence; a block-causal mask lets each
question see the document and never a sibling. The pointer head scores
each option against the question's `<decide>` token and softmaxes.
Trained with cross-entropy against labelled outcomes. Architecture
explicitly follows Hume's reconstruction (§31): shared state, isolated
questions, pointer head, CE vs labelled outcomes. API follows TypeSafe
`POST /v1/systemone`; official `typesafe-sdk` works with a `base_url`
change. Weights `kev-0.5b` (38 MB: LoRA adapter, readout head,
tokenizer) on GitHub release v0.1.0; base model from the Hub on first
load. Trains ~1h45m on an Apple M5; ~160 ms for a six-question
request. Model card: research prototype, not production, not Jev.
Do not copy serve flags, ports, or train commands into skill cards.

**Not a distill.** Six public datasets converted to TypeSafe-shaped
requests (Banking77, AG News, MNLI, BoolQ, SST-5, Yelp): 9,000 records,
13,500 questions, two epochs. No LLM-generated data. Distinct from
openjev-lm / jev-gate on the *same* 0.5B backbone: those copy a hosted
Jev teacher. Distinct from Nimble: 9B contrastive synthetic labels, no
measured ECE. Distinct from encoder open-jev: bidirectional DeBERTa,
OOD drop measured. Distinct from TypeAR / pcdServer: those decode a
constrained next token. Distinct from proprietary Jev: closed weights,
~32k envelope. Distinct from Archer Watch: 27B announced, multimodal,
no Hub weights this pass.

**Evidence (README / model card; not re-run; Empirical as their named
receipt).** Isolation exact: packed vs separate max Δ **3.7e-6**;
secret-in-sibling / absent / in-state **p = 0.03 / 0.03 / 0.99**.
Held-out ECE **0.065** (10 bins) on 1,350 ID questions; **0.031** after
one-parameter temperature scaling (T=1.47). Overall acc **0.799**.
Permute (4 orders, Choice K ≥ 3): argmax flips **7.4%**. IIA: log-odds
shift from one irrelevant option **mean 0.13**, p90 0.34. Boundary
forgery: option count unchanged, forged option p ≤ 0.09. Per-source
cells (acc / ECE) stay in the model card; do not promote them into a
ranking against Jev.

**Honest limits (their words).** 0.5B knowledge (on the TypeSafe docs'
structured-criteria example kev picks `return_policy` where Jev picks
`return_status`). Calibration is in-distribution; ECE on the training
datasets says nothing about a new workflow. Not multimodal. Trained at
384 state / 1,024 branch tokens; serving caps at 8,192 vs Jev ~32k.
Score confidence is a stand-in; TypeSafe has not published theirs.
Choice `confidence` uses `(p_max − 1/K) / (1 − 1/K)` — the same
arithmetic Hume reconstructed in the official adapter (§31), as *their*
API derivation, not a TypeSafe contract.

**Placement.** (a) trained decision-only open path next to Laya / Nimble
/ Archer Watch; (b) cleanest *runnable* productization of Archer's
reconstruction (API-compatible); (c) contrast vs TypeAR (constrained
AR decode) vs encoder open-jev vs proprietary Jev; (d) jevals/Harbor
bake-off candidate; mechanism tests mirror Archer probes — they
falsify the reconstruction, they do not prove kev = Jev; (e) when to
use: laptop-local System One API drop-in for development/eval; not a
knowledge/frontier substitute. **Empirical** as a public repo + named
ID receipt. **Hypothesis** that it substitutes for Jev on *your*
labels. Cards: `judgment-class.md`; FAQ; `validation.md`;
`mental-models.md`; `mixed-architecture.md`; `formal-methods.md`
(pointer-softmax is still a sensor); `optimizer-integration.md`.
No wrapper.

### Delta (~14:35 Boise) — Hub weights, PEFT task_type, NOTA training

Not a rewrite of §45. No architecture species change. HTTP 200 this
pass: Hub [`jaredpalmer/kev-0.5b`](https://huggingface.co/jaredpalmer/kev-0.5b)
(Apache-2.0 adapter; `peft` / `text-classification` card); GitHub
README now names that Hub id as the fetch path; release tarball
remains. GitHub this pass: **61★**, pushed ~20:29Z (signal had 53★).
Do not copy `--run` / publish flags into skill cards.

1. **Hub weights.** `kev.publish` uploads the adapter; `--run` accepts
   Hub ids (`jaredpalmer/kev-0.5b`); the Qwen2.5-0.5B base still
   downloads on first load. Bake-off fetch path for jevals/Harbor
   (`validation.md`).
2. **PEFT.** `LoraConfig(task_type="FEATURE_EXTRACTION")` (`kev/model.py`).
   Publish patches legacy adapters that saved `task_type` null (Hub
   warns; PEFT treats both the same on a bare backbone). Docs mention
   only kev-0.5b. Pointer readout, not a new species.
3. **HIGH — `none_of_the_above` is a training question, not only a
   request hatch.** First training run learned "this wording ⇒ pick
   it" when NOTA appeared only as the correct answer (`kev/data.py`
   comment). Fix: add NOTA as a **wrong alternative** too
   (`p_none_distract`); vary wording (`NONE_OPTIONS`: "None of the
   above" / "Something else" / "Not listed here" / …); dedicated
   `test_none_of_the_above` (true option still present → little mass
   on none; true option removed → pick none; a shortcut model picks
   it in both cases). **No published rates this pass — do not
   invent them.** Model card already augments with p=0.10
   true→`other: None of the above`; the *delta* is confronting the
   hatch as a distractor as well. Cross-link wellposed / Choice
   `"other"`: request-shape lint puts the residual option on the
   offered set; **training must confront that option** or the hatch
   becomes a wording shortcut. Cards: `question-design.md`; FAQ
   forced Choice; `validation.md`.

## 46. 14:03 Boise hourly — open multimodal RLCD, bake-off substrate, decision-token LoRA (2026-09-18)

America/Boise 14:03 = 20:03 UTC. Docs-only fold into PR #2
(`cursor/augustus-store-envelope-00b4`). Archer Hume 27B drop still
**WATCH** (Hub authors `archerhume` / `4rcherhume` empty this pass;
user watch still ~2026-09-19). No invented metrics. Frames first,
not a hit list. Identity lock vs `typesafe-ai` / `tenbin` /
`decision-first` holds. No wrapper, no serve how-to.

HTTP 200 / Hub fetch this pass:
[`BlackwoodAI/blackwood-rlcd`](https://huggingface.co/BlackwoodAI/blackwood-rlcd)
README; [`pngwn/open-jev-laya-bench`](https://huggingface.co/datasets/pngwn/open-jev-laya-bench)
`RESULTS.md` (no dataset README); [`Foodoo1/Qwen3-14B-RLCD-Decision-LoRA`](https://huggingface.co/Foodoo1/Qwen3-14B-RLCD-Decision-LoRA)
README; GitHub READMEs for
[`thevibeworks/jevgate`](https://github.com/thevibeworks/jevgate),
[`suraj-phanindra/wellposed`](https://github.com/suraj-phanindra/wellposed),
[`khordoo/jev-reflex-autonomy-lab`](https://github.com/khordoo/jev-reflex-autonomy-lab),
[`Wany-i/jev-decision-layer`](https://github.com/Wany-i/jev-decision-layer),
[`perixtar/jev-e2e`](https://github.com/perixtar/jev-e2e),
[`yalindogusahin/jevpandas`](https://github.com/yalindogusahin/jevpandas).

### HIGH

1. **[`BlackwoodAI/blackwood-rlcd`](https://huggingface.co/BlackwoodAI/blackwood-rlcd)**
   (Hub, 2026-09-18 v1; `pipeline_tag: image-text-to-text`; CC BY-NC 4.0;
   likes=1 this pass). **Open multimodal RLCD decision model.**
   Screenshot or text in; Choice / Score / Boolean out in one prefill;
   Jev-compatible `/v1/systemone` shim. Options listed as letters;
   answer from option-letter logits at the last position; temperature-
   calibrated; no sampling; `output_tokens` always 0. Not Archer's 27B
   drop. Not CLIP/SigLIP (those are vision *scorers*). Same *decide*
   species as Jev / Laya / kev, with image-in.

   **Architecture (load-bearing).** Omni perception→decision can ship
   **without waiting for Archer**. Soft judgment over **pixel
   candidates code already marked** (letters drawn on the screenshot;
   criteria keyed by those letters) inside a deterministic click/act.
   Specialist composition (SAM / OCR / AX → text → Jev) still exists
   (`§39`); this is the shared multimodal System One that card was
   waiting for. Information still dies at the *act*: the model picks a
   letter; code clicks. A Noul is still not a proof. CC BY-NC: research
   / personal, not a commercial drop-in. Do not copy vLLM flags, the
   shim, or curl bodies into skill cards.

   **Evidence (model card; paired per item; not re-run; Empirical as
   their named receipt).** Web element choice, 300 held-out steps:
   acc **0.907** vs Jev 1.13 text-only **0.480**; letter-shuffle flip
   **0.133** vs **0.587** (lower better); ECE **0.037** vs **0.091**;
   latency **~200 ms** (1×H100) vs 441 ms (Jev via OpenRouter).
   4-lettering (four orderings averaged, 4× compute) acc **0.953**.
   Desktop held-out acc **0.76** vs **0.654**. NL predicates over
   records **0.973** vs **0.965**. Tetris lines / 60 pieces **14.2** vs
   **13.6**. General text, 85 public sets / 8,456 items: blackwood
   **0.786**, Jev **0.850** — Jev still leads. Domain sets 27 / 12,746:
   **0.710** vs **0.703**. Pixel rows use a randomized viewport crop.
   Jev is text-only by design: screenshot rows compare screenshot
   input with Jev's *text* input on the same steps. **Hypothesis** that
   it substitutes for Jev on *your* labels. Boolean questions on skewed
   sets can be over-confident (their limit). Cards: `judgment-class.md`
   (family, holes, when-to-use, dedicated card, perception rewrite);
   FAQ wait-for-Archer; `validation.md` letter-shuffle; `formal-methods.md`
   one sentence; `mixed-architecture.md` gallery; `applied-mappings.md` §2.

2. **[`pngwn/open-jev-laya-bench`](https://huggingface.co/datasets/pngwn/open-jev-laya-bench)**
   (`RESULTS.md` this pass; no dataset README). Shared bake-off:
   [`pngwn/system-one-qwen3.5-4b-scorer`](https://huggingface.co/pngwn/system-one-qwen3.5-4b-scorer)
   `@ e6464dce` vs [`convaiinnovations/laya`](https://huggingface.co/convaiinnovations/laya)
   `@ 7c76b622`. **26 neutral + 9 home** tasks, **11,959** test items,
   **3,269** cal items. Hardware: NVIDIA A100-SXM4-80GB. Config chosen
   on `cal` (scorer vs `laya_text`). **Not TypeSafe Jev vs Laya** — do
   not launder this table into a proprietary-Jev ranking. Laya's
   published in-task acc/ECE sit on unpublished sets and are context,
   not like-for-like.

   **Harbor / jevals practice in the wild.** Measurement substrate
   exemplar: accuracy + **ECE / NLL / Brier** (and acc@50% coverage),
   held-out `test`, temperature chosen on `cal`, leave-one-task-out,
   prompted-base / prompted-instruct arms on the same 4B, per-task T
   vs shipped T. **LLM-as-judge is not the primary System One score.**
   That is the eval path the skill already wanted (`validation.md`
   Eval & hill-climb; `notes.md` §40). Do not copy the scoring scripts.

   **Evidence (`RESULTS.md`; not re-run; Empirical as that named
   receipt).** Neutral, shipped T: System One 4B macro acc **0.760**,
   Laya **0.737**, Δ **+0.023 [+0.013, +0.032] \*** (interval excludes
   0). Neutral ECE-10 **0.074** vs **0.122**; macro NLL **0.569** vs
   **1.272**; macro Brier **0.324** vs **0.392**. Home (the 4B's own
   held-out split): **0.715** vs **0.486**, Δ **+0.229 [+0.198, +0.262]
   \***. Home ECE-10 **0.072** vs **0.272**; NLL **0.697** vs **3.836**;
   Brier **0.363** vs **0.759**. Ahead on 13/26 neutral and 8/9 home.
   Neutral prompted-instruct (same 4B, ≤26 options) macro acc **0.763**
   vs fine-tune **0.760**, Δ **+0.003 [-0.004, +0.011]** — interval
   includes 0; do not slogan "fine-tune always wins zero-shot." Home
   prompted arms drop banking77 / ticket-queue (enum >26). Latency
   one-question p50 on the same GPU: tweet_emotion Laya 27.9 ms vs
   scorer 76.7 ms; home_banking77 (K=77) 30.0 vs 382.8 ms. **Hypothesis**
   as a ranking of *your* head. Cards: `validation.md` bake-off; FAQ
   LLM-as-judge; `judgment-class.md` Laya companion.

3. **[`Foodoo1/Qwen3-14B-RLCD-Decision-LoRA`](https://huggingface.co/Foodoo1/Qwen3-14B-RLCD-Decision-LoRA)**
   (Apache-2.0 adapter; base `Qwen/Qwen3-14B`; PEFT). **Decision-token
   QLoRA** under **parallel constrained decoding**: one prefill, KV
   broadcast across fields, logit slice over candidate first tokens —
   the TypeAR / pcdServer / `stephanj/parallelConstraintDecoding`
   inference pattern (`findings.md` batch #1). Loss computed **only on
   the single decision token** of each field. The base already hits
   easy fields (language/sentiment 100%); reasoning-heavy fields fail
   because the decision happens at one token with no room to think.
   Pattern, not a fraud product: train the decision token, do not
   fine-tune generated prose. Evaluated with
   [`harshatheg/Qwen-2.5-1B-RLCD`](https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD)
   inference code (that Hub repo still has no weights — stock Qwen +
   custom code; already archived). Synthetic fraud-triage schema;
   **do not use for real financial decisions** (their limit). Do not
   copy the prompt or LoRA flags into skill cards.

   **Evidence (card; held-out 200-case, 4 fields, 4-bit NF4, RTX 3090;
   not re-run).** fraud_risk (4-way) **64.0% → 95.0%**; block_account
   **77.0% → 100%**; language and sentiment stay **100%**; overall
   (800 decisions) **85.2% → 98.8%**. Mean latency **~234 ms** per
   case (all 4 fields in one broadcast). Remaining errors all
   LOW→ELEVATED (conservative); zero high-risk judged low. Train:
   16,608 single-token examples from 4,152 synthetic cases (648
   templates × 72 messages EN/ZH/ES/JA), 1 epoch, ~97 min on one 3090.
   **Empirical** as that named receipt. **Hypothesis** as a general
   recipe on *your* schema. Cards: `judgment-class.md` constrained-AR;
   `methods-catalog.md`; FAQ open-weights vs constrained decode.

4. **[`thevibeworks/jevgate`](https://github.com/thevibeworks/jevgate)**
   — already §25 / `mappings.md` §18. This hour the *mental model*,
   matching the GitHub description: **an allowlist proves** every verb
   is a listed read-only tool; **Jev judges only unlisted** leftovers;
   **fail-open (cannot block)**. Hard envelope in code + soft judgment
   only on the residual. Proven runs in 4 µs and never leaves the box;
   Refused never asks the model (so a comment cannot talk a writer
   through); Unknown is five Nouls, admit iff every p < 0.2. Jev on
   `/bin/ls` alone leaks (0.04) — that is why it is the third tier.
   Real-traffic counts already on the README (116,979 Bash calls:
   26.4% proven; 16.2% reach Jev; 47 admitted, all read-only by hand)
   stay author-reported; do not re-promote 0/59 as if new. MIT. 0★
   this pass. No rewrite of the 0.2 threshold as a constant. Cards:
   `mappings.md` §18 "proves"; FAQ allowlist-then-judge; methods-catalog.

5. **[`suraj-phanindra/wellposed`](https://github.com/suraj-phanindra/wellposed)**
   (MIT, JS, 0★, created 2026-09-17). **Lint the request before it
   comes back confidently wrong.** Neighbor-skill identity: `tenbin`
   still owns design-time lint/measure; this is an Empirical *recipe*
   of that hole, not a second Augustus skill and not a wellposed
   how-to. Standing Choice contract (`SKILL.md`): probabilities are
   conditional on the offered set; absent candidates can never be
   chosen; add `other` where coverage is open. wellposed is the
   receipt that **violating that contract is silent**.

   **Evidence (README; not re-run).** 40 generated requests: **0/40**
   syntax errors (API validation already covers that); **16/40 (40%)**
   asked something that did not make sense; **0/11** list-questions
   included a none-of-the-above. Live probe: unsubscribe email, four
   department options, no `other` → `"support issue"` **confidence
   1.00**; with `other` → `"other"` confidence 0.93. Overlapping
   `angry`/`furious` collapsed confidence to **0.19** — loud; ordinary
   gates catch it. Forced wrong Choice is quiet. Structural lint (35
   rules, offline) then optional jev-on-jev semantic layer. Labeled
   corpus: recall **22/26 = 85%**, precision **22/24 = 92%** (computed
   live from the corpus). Honest limits: one-model labels, so 40% is a
   floor; 2026-09-18 adversarial audit added 36 items because the
   metric could not see ordinary-English false positives. Broken state
   paths (`ticket.assigned_agent.name` with no such path) are
   *provably* wrong. Confidence gating **cannot** catch a forced
   Choice. Cards: `question-design.md` diagnosis; validation gate #2;
   FAQ; tenbin identity lock.

6. **[`khordoo/jev-reflex-autonomy-lab`](https://github.com/khordoo/jev-reflex-autonomy-lab)**
   (TypeScript, 0★, created 2026-09-18T19:46Z; GitHub license null this
   pass). Interactive multi-drone lab. **S1 Jev reflex keeps control**;
   optional S2 planner (OpenRouter / GLM 5.3) is **one-use advice** on
   low confidence. Jev does not pause while the planner responds. S2
   does not fly the drone. Kahneman row already taught the split
   (`toolbox-mapping.md`: S2 proposes, S1 discriminates; never the
   reverse) — this is that split as a control loop, not a flight
   controller. Experimental visualization; mock mode without keys;
   live fleet success varies. No metrics to promote. Do not copy the
   adapter, `.dev.vars`, or ports. Cards: `mixed-architecture.md` dual
   orchestration; `agent-self-assessment.md`; toolbox Kahneman row.

### MED (pointers, not cards of their own)

7. **[`Wany-i/jev-decision-layer`](https://github.com/Wany-i/jev-decision-layer)**
   (MIT, Python stdlib, 0★). Wrap the decision model as a **business
   decision tool**: caller names the *judgment*, not the model.
   `decide(name, fields)` → outcome + confidence + **`gate` (part of
   the result)**. Registry JSON; hard guards in code; `other` required
   on Choice. OpenRouter `POST /api/alpha/decisions` (not
   `chat/completions` — that 400s). Text-only: screenshots must be
   textualized — contrast with blackwood. 28 offline tests, no key.
   Unofficial. Do not copy the registry or MCP install.

8. **[`perixtar/jev-e2e`](https://github.com/perixtar/jev-e2e)**
   (MIT, TypeScript, alpha, 0★). Natural-language cases; Jev selects
   observed controls; **Playwright executes and independently checks
   expectations**. Verdicts PASS / FAIL / BLOCKED. A completed
   navigation or a confident model response **cannot substitute for
   checked expectations**. Harbor/jevals practice on a browser taskset
   (score on the task; harness rolls out). Alpha: controlled demo does
   not establish reliability across arbitrary sites. Do not copy CLI
   flags or ports.

9. **[`yalindogusahin/jevpandas`](https://github.com/yalindogusahin/jevpandas)**
   (Python; GitHub LICENSE 404 this pass). pandas frame as the store:
   `evaluate` / `filter` / `classify` / `score` / batched `ask`.
   Classify example includes `other`. Failures never become negative
   predictions. No generative chat, no joins, no training on review
   labels. Store-as-semantic-index cousin of jevql / sqlite-jev
   (`mappings.md` §4) over a dataframe instead of SQL. Samples in
   `data/` are synthetic. Do not copy the client.

Cards: `judgment-class.md`; `validation.md`; `question-design.md`;
`mappings.md` §18 / §4; `mixed-architecture.md`; `faq.md`;
`agent-self-assessment.md`; `mental-models.md`; `formal-methods.md`;
`applied-mappings.md` §2; `methods-catalog.md`; `toolbox-mapping.md`.
No wrapper.

## 47. Abide — productized soft-rule preference lint (2026-09-18)

America/Boise ~14:34 = 20:34 UTC. Docs-only fold into open PR #2
(`cursor/augustus-store-envelope-00b4`). Not a competing PR. Archer
27B drop still **WATCH**. Identity lock vs `typesafe-ai` / `tenbin` /
`decision-first` holds. No wrapper, no hook how-to, no copied `npx` /
init / ports. Text/diff only — **not multimodal**. Do not invent
metrics.

HTTP 200 this pass: GitHub README for
[`coldteadotai/abide`](https://github.com/coldteadotai/abide)
(MIT, TypeScript, created 2026-09-18, npm `@coldtea/abide`, 4★ this
pass); replay method in-repo at `benchmarks/replay/README.md`.
Attached SIGNAL + replay README + repo.json as primary placement
guidance.

### HIGH

1. **[`coldteadotai/abide`](https://github.com/coldteadotai/abide)**
   — productized Jev hooks for Claude Code / Codex / OpenCode that
   enforce **soft project rules** (AGENTS.md / CLAUDE.md / instruction
   files) no linter can check. On every edit (or turn) it asks Jev
   **one Score / probability per rule against the diff only**, never
   the conversation. A break names the rule and asks the agent to
   repair in-session. jev-pref already stated the contract (YOU define
   the rule / Jev classifies / code maps outcome). Abide is the
   fuller productized path: compile / calibrate / tune / replay /
   audit + multi-host. Do not clone the CLI.

   **Architecture (load-bearing; not a hit list).**

   1. **Soft rules → soft judgment; hard rules → linter.** Rules a
      linter can check are handed to the linter. Same layering family
      as jevgate's hard envelope (`mappings.md` §18): structure
      **proves** what it can; typed judgment only on the residual.
      jevgate's remainder is unlisted shell verbs; Abide's remainder
      is project-instruction soft rules. Different holes; same
      sandwich. Soft judgment is never the sole hard veto.
   2. **Edit-phase vs turn-phase is an observation-window question.**
      Each compiled rule runs at `edit` (this hunk) or `turn` (the
      whole turn diff). "Did this add more than was asked?" has no
      answer after edit 1 of 12. Question design must name when the
      evidence exists (`question-design.md`).
   3. **Banded confidence + fail-open.** Their product bands: ≥0.8
      repair in-session; 0.5–0.8 human note, agent silent; <0.5
      silence. That 0.8 is **their** operating point, not a universal
      threshold (`mappings.md` §2 already forbids magic 0.8). Hooks
      always exit 0, hard deadline; no key / no network → the edit
      proceeds and the miss is logged. Soft judgment never sole hard
      veto.
   4. **Rubric as editable artifact.** `.abide/rubric.json` quotes the
      source instruction line. A wrong verdict is a rule rewrite.
      `calibrate` scores rules against recent git history; `tune`
      rewrites dead rules. False positives live in the question
      (scope, criteria), not in the model.
   5. **Eval honesty / Harbor-adjacent.** Replay of 93 real Claude
      Code sessions against each repo's own AGENTS.md (two private
      repos + public `pr-lens`; hunks unpublished). Nothing is
      re-run: diffs come from transcripts. Independent reviewer
      (Claude, reading each rule's own text strictly; owner
      spot-checked four first-pass comment flags and agreed). Replay
      does **not** measure whether the agent repairs when told.
      Harbor/jevals practice in the wild: frozen transcripts, phase
      split, independent confirmation — not a Harbor taskset and not
      a second jevals (`validation.md`).

   **Evidence (README + `benchmarks/replay/README.md`; not re-run;
   Empirical as that named receipt).** 93 sessions with edits; 1,256
   edits judged; 147 turns judged; Jev cost **$0.22**; wall **~2
   min**. Edits flagged at 0.8+: **39 (3.1%)**. Turns flagged at
   0.8+: **15 (10%)**. After independent review: edits **10/39 =
   26%** precision; turns **11/15 = 73%**; all **21/54 = 39%**.
   Author's gloss: 8 confirmed violations per 1,000 edits; 1 turn in
   13 ends with a confirmed violation of a rule no linter could
   express; 11 of 93 sessions contained at least one. Recall probe
   from 20 cleared hunks closest to the line (0.31–0.48): one real
   miss (props-ordering). Most false positives from two edit-phase
   rules (`plain-error-for-expected-failure`, `comment-volume`) —
   fixable with `scope` and criteria, which is what calibrate / tune
   exist for; the table is **before** either ran on the tightened
   rubric. No turn-number drift: pr-lens-app flat ~2.5% through early
   / mid / late turns; coldtea falls 5.8% → 1.3% because big
   new-file writes happen early. Agents break these rules from the
   first edit at a steady rate. Economics (README, author-measured
   2026-09-18, direct to TypeSafe): a check was ~2,500 tokens with an
   ordinary LLM (cent+, seconds, prose to parse); Jev ~300 ms,
   **$0.00004–0.00007** per check on this repo's 13 rules (1,000–1,600
   input tokens). Do not promote those $ / ms figures as class
   constants.

   **Siblings — complementary, do not merge.**

   - **`doeixd/jev-pref`:** earlier watch; the contract Abide
     productizes. Keep the contract quote; point here for compile /
     calibrate / tune / replay / multi-host.
   - **`24601/rh-guard`:** reward-hacking / eval-integrity on agent
     tool use. Abide: project-instruction soft rules on diffs. Same
     hook-host surface, different judgment class. Shared fail-open /
     host-adapter lessons; no code dependency.
   - **`suraj-phanindra/wellposed`:** request-shape lint still
     upstream of any Score call (`tenbin` owns the skill).
   - **`thevibeworks/jevgate`:** hard envelope owns safety; Abide is
     soft residual judgment on residual soft rules.
   - **`huntedman/JevLint`:** file-level convention Nouls; sibling,
     not a substitute.

   **Placement.** Verifier over rules the project already wrote
   (`mixed-architecture.md` preference lint; composition-algebra #9).
   Pillar: selective classification / abstention + structural-prove ∩
   remainder. Hole: gate. Family: closed decision API (typed Score
   per rule). Fail-open, banded. Eval path: replay + independent
   review (named receipt above); not a substitute for jevals/Harbor
   on *your* rubric. **Empirical** as README + dated replay. **Hypothesis**
   that the same bands / precision transfer to *your* AGENTS.md.
   Cards: `mixed-architecture.md`; `question-design.md`;
   `validation.md`; `mappings.md` §2 / §18; `faq.md`;
   `agent-self-assessment.md`; `toolbox-mapping.md`;
   `methods-catalog.md`; `mental-models.md`. No wrapper.

### Omni / Jev-omni

Text/diff only today. Usage + measurement exemplar (replay harness,
precision by phase). Not a multimodal substrate and not a reason to
wait on Archer.

## 48. Extractive selection, pointer-not-generator, local contract drop-in (2026-09-18 ~14:52 Boise)

America/Boise ~14:52 = 20:52 UTC (run 205210). Docs-only fold into
open PR #2 (`cursor/augustus-store-envelope-00b4`). Not a competing
PR. Archer 27B drop still **WATCH**. Identity lock vs `typesafe-ai` /
`tenbin` / `decision-first` holds. No wrapper, no install.sh, no
copied ports / Docker / PyPI how-tos. No invented metrics. Do not
re-fold blackwood-rlcd, open-jev-laya-bench, decision-token LoRA,
jevgate, wellposed, jev-reflex-autonomy-lab, Abide, kev, jevpandas,
bitrate-advisor.

Backend-agnostic: these are categorization / scoring *placements*
(extractive keep/drop, pointer evidence, contract-compatible local
scorer, structured observe→decide→act, dataframe columns, route≠memory,
advisory sidecar, structure induction, AST∩semantic). TypeSafe Jev is
the exemplar in the READMEs, not a monopoly.

### HIGH

1. **[`AppitStudio/testimonial-miner`](https://github.com/AppitStudio/testimonial-miner)**
   (MIT, Python, created 2026-09-18T20:42Z, 0★ this pass). Gmail/IMAP
   → numbered sentences in **code** → **one** typed request per email
   (Choice kind + app, Nouls for user/praise/problem/English, Score
   quotability, **one Noul per sentence**). **The model never writes
   text.** The stored quote is the sender's sentences, selected by
   those Nouls and joined in order. All thresholds live in
   `Thresholds` and `redecide` reapplies them to logged answers
   **without new model calls**. Header rules skip newsletters /
   outbound / quoted replies before any call. Pattern: **extractive
   selection + multi-question broadcast + offline re-thresholding.**
   Cousin of exact-text keep/drop (`applied-mappings.md` §2), not a
   testimonial product and not a Gmail how-to.

   **Evidence (README; not re-run; Empirical as that named receipt).**
   Developed against `typesafe-sdk` 0.7.0 / `jev-1.13.0`. Their
   *product* bars (not class constants): candidate if user ≥0.5,
   praise ≥0.6, quality ≥1.5 on 0–3; borderline praise ≥0.35 /
   quality ≥1.0; quote sentences ≥0.6. Live fixtures (8 requests,
   ~22k input tokens): **5** candidates, **3** rejected, **3** header
   skips. Offline tests use fakes and say nothing about model
   accuracy. Author cost gloss: ~$0.042 / M input; typical email
   2–3k tokens; 10k judged emails ~$1. Do not copy IMAP setup.
   Cards: `applied-mappings.md` §2; `mappings.md` §2; `methods-catalog.md`.

2. **[`choxos/jev-reviewer`](https://github.com/choxos/jev-reviewer)**
   (MIT, JavaScript, 1★, created 2026-09-18T14:47Z). Systematic-review
   data extraction: PDF/Office/HTML/CSV stay in the **browser**;
   segmenter assigns line ids (`A001`…); the decision model **points
   at ids**; **code copies verbatim quotes with file and place**.
   Nothing is paraphrased, so nothing can be invented. Two-pass:
   screening Choice "which line answers q?" (+ none) over chunks,
   then verifying Nouls "does this line itself answer q?". **Not
   found is an answer.** Speculative fan-out: every question against
   the same text. Pattern: **pointer-not-generator** for evidence
   synthesis / citation integrity. Same species as keep/drop over
   candidates code already holds; GLiNER locate is the cousin when
   the answer *is* a span the encoder proposes.

   **Evidence (README; sample study, Sep 2026; not a validation
   study).** 17-page article + 12-page analysis plan + CONSORT,
   712 lines: 1 question 10 req / 1.2–2 s / $0.0016; 9 questions
   17 / 2.3 s / $0.0052; 18-question template 27 / 4.6 s / $0.0101.
   Chunks of 12k characters matched 7k with a third fewer requests.
   Treat as spot checks. Scanned PDFs need OCR first (their limit).
   Do not copy the relay. Cards: `applied-mappings.md` §2;
   `methods-catalog.md` claim–evidence; `mental-models.md`.

3. **[`us/jev-local`](https://github.com/us/jev-local)**
   (LICENSE absent this pass; Python; 0★; created 2026-09-18T19:28Z).
   Local `POST /v1/systemone` drop-in (Docker / `pip` / SDK
   `base_url`). Open-weights *path*, no waitlist. **Default scorer is
   a deterministic stub and carries no intelligence** until
   `JEVLOCAL_SCORER=hf`. That flag is load-bearing: a green smoke
   test on the stub is not a local Jev. Pattern: **contract-compatible
   local scorer for offline/dev**, beside kev's Hub drop-in and
   Laya's native head — not a fourth species. Their README: interface-
   compatible baseline, **not a reproduction of Jev's undisclosed
   model or training**. Softmax ignores level ordering; option order
   can shift logits. Do not copy `install.sh`, ports, or model ids
   into skill cards.

   **Evidence (README; Empirical as *their* named tables, Hypothesis
   on *your* labels).** Official `typesafe-sdk==0.6.0` with only
   `base_url` pointed at the server (4B backend) is the drop-in
   proof. When `hf` is on they publish Wilson-CI / ECE / NLL tables
   on templated sets (set1 / set2 / set3); do not re-promote those
   rows as a ranking of TypeSafe Jev. Head-to-head vs published
   jev-1.13.0 on 5 questions: 4/5 top-answer agree; payout
   billing-vs-technical is an ambiguous prior, not a prompt bug.
   Cards: `judgment-class.md`; `faq.md`; `validation.md`.

4. **[`hitakshiA/solari-reflex`](https://github.com/hitakshiA/solari-reflex)**
   (MIT, TypeScript, 0★, created 2026-09-18T15:24Z). Computer-use
   **speed layer** on Solari (browser + Linux desktop): **one
   structured observation → one typed decision → one verified
   action**. **No screenshots in the loop.** Observation is
   numbered controls / a11y tree / visible text (Calc: used visible
   rows, never 2³¹ cells). Decision: which operation, which target
   (speculative, same request), done/blocked. Write: a small model
   only for TYPE as strict JSON. Act: guard check, refuse covered
   controls, pipeline input; model output **never** becomes a
   selector, coordinate, or script. Deny lists are **absent from the
   question**, not merely disfavoured. Sibling of
   `browser-use/jev-ultrafast` / jev-use / typesafe-computer-use.
   Pattern: **perception → decision → act** with Harbor-style
   measurement (score the task; independently checked by the app /
   Stripe API / answer key).

   **Evidence (README + [solari-fast-showcase](https://github.com/hitakshiA/solari-fast-showcase);
   vs Codex CLI GPT-6 Astra on the same Solari machines; not re-run).**
   Stripe Checkout (qty 2, promo, card): **60.2 s**, $0.011 vs
   **194.9 s**, 34 tool calls. Six different Stripe checkouts:
   **66 s**, $0.064 vs **460 s**, 86 tool calls. 30 Calc expenses:
   **24.2 s**, $0.0008 vs **98.4 s**, 77 tool calls. Ratios on that
   table sit in ~3–7×. Their step table: decide ~400 ms / ~$0.0001;
   TYPE write ~600 ms. **0.6** is *their* Advisor handoff, not a
   universal threshold. Do not copy npm git-install. Cards:
   `mixed-architecture.md`; `validation.md`; `applied-mappings.md` §2;
   `agent-self-assessment.md`.

5. **[`ktaletsk/jevframe`](https://github.com/ktaletsk/jevframe)**
   (MIT, Python 3.10+, PyPI `jevframe`, pandas **and** Polars,
   created 2026-09-18T17:06Z, 0★). `.jev` accessor: `noul` / `choice`
   / `score` / `evaluate` with **full probability columns** (`p__…`),
   preserved row order/indexes, one input row per request, questions
   about a row share the request, default `max_concurrency` 16.
   **No result is thresholded or silently renormalized.** `score` is
   the expected zero-based level, not a probability. Sibling of
   [`yalindogusahin/jevpandas`](https://github.com/yalindogusahin/jevpandas)
   (`notes.md` §46): both are dataframe-native semantic columns;
   jevpandas is the store-as-index cousin (`evaluate`/`filter`/
   `classify`/`score`); jevframe is the accessor + Polars + packed
   struct layout. Neither is SQL `jev()`. Pattern: **dataframe-native
   semantic columns** (class, not vendor). v0: no chat, no generated
   records, no custom dtypes. Do not copy the client. Cards:
   `mappings.md` §4; `mixed-architecture.md` gallery.

### MED (pointers, not cards of their own)

6. **[`de-niji/jev-hermes`](https://github.com/de-niji/jev-hermes)**
   (MIT, Python, 0★). Intent **gate before a Hermes turn**:
   `calendar` / `mail` / `status` → config + flat tools, **no memory
   search spam that turn**; `complex` / people / prefs / "what did
   we…" → memory + normal agent. Memory providers still **write** in
   the background. Token savings come from skipping long tool/memory
   *tours*, **not from turning memory off**. Pattern: **route ≠
   memory**; S1 gate preserves S2+memory for hard routes. OpenRouter
   `POST /api/alpha/decisions` (same surface as jev-decision-layer).
   Do not copy `docker cp`. Cards: `applied-mappings.md` §5;
   `mixed-architecture.md` dual orchestration.

7. **[`ngallodev-software/agent-workflow-typesafe-ai`](https://github.com/ngallodev-software/agent-workflow-typesafe-ai)**
   (Apache-2.0, Python, 0★). Advisory-only host plugin. Projects
   bounded redacted evidence into typed questions; normalizes answers
   into versioned secret-free **semantic receipts**. **Never changes
   host routing**, executor, model policy, lifecycle, evaluation,
   review, or acceptance. Missing credentials / SDK / uncertain
   answers / failures → distinct `no_action` outcomes. Pattern:
   **soft sidecar receipts** (fail-open evidence). Complementary to
   Abide (Abide is in-session Score on a diff; this is advisory
   metadata the host may ignore). Do not copy the TOML.

8. **[`Joymfl/dag-jev`](https://github.com/Joymfl/dag-jev)**
   (Rust + petgraph; README empty this pass; 0★; created
   2026-09-18T20:42Z). GitHub description: DAG from unordered items
   via Jev. Source: pairwise "does task i depend on j?" over a bag
   of numbered steps (reads/writes in `input.txt`); answers intended
   to build a `petgraph`. Experiment; graph wiring incomplete in
   `main.rs` this pass; **no metrics**. Pattern: **structure
   induction over bags** — code owns the DAG; the model only answers
   pairwise (or Choice) dependency questions. Do not clone the
   request builder. Cards: `mappings.md` §9 / §5.

9. **[`knowlet/jev-agentworld-web-simulator`](https://github.com/knowlet/jev-agentworld-web-simulator)**
   (MIT, TypeScript, 0★). Fictional web: Jev Choice for **search
   intent** and (same request) **layout / palette**; an
   OpenAI-compatible generator writes `SearchDocument` /
   `PageDocument`; Zod validates; a **deterministic** compiler emits
   json-render spec; SQLite is the world. Model cannot add
   components or handlers. Mock mode does **not** silent-fallback
   to live. Pattern: **decision for control, generator for content**
   in a simulated world. Live smoke (when run) is an integration
   test (budget **3 Jev + 3 generator**), **not** calibration or
   world-consistency. Offline CI: 27 unit/contract + 2 Chromium
   browse tests; [CI #2](https://github.com/knowlet/jev-agentworld-web-simulator/actions/runs/35391369860)
   on `b1dd6d7` passed. Do not copy `.env`. Cards:
   `mixed-architecture.md`.

10. **[`ufx7/jev-testbench`](https://github.com/ufx7/jev-testbench)**
    (LICENSE absent this pass; TypeScript; 0★). Two tools: black-box
    **determinism / latency / context / concurrency** (`src/bench/`);
    collaboration harness (`src/collab/`) with three arms —
    `llm_autonomous` (unconstrained; illegal actions tracked),
    `scripted_plus_jev` (code enumerates legal actions; Choice
    picks; **no LLM**), `llm_plus_jev` (LLM proposes; Choice
    arbitrates on the legal set; low p escalates then **stops**
    rather than guessing). **Jev is not a peer arm.** Reports
    Wilson intervals, exact McNemar per level (p < 0.05 **and** ≥5
    discordant pairs), ceiling-effect flags, cost/latency **per
    model**. Pattern: bake this into the jevals/Harbor **measurement
    curriculum**, not a second product. Grid-task demo uses a mock
    LLM to prove the harness; swap before trusting a real model.
    Cards: `validation.md`.

11. **[`alexykn/jevscan`](https://github.com/alexykn/jevscan)**
    (MIT, Python 3.12+, `0.2.0rc4`, 0★). Tree-sitter extracts
    lexical units (Python/Rust/Perl/TS/JS); typed questions on
    those targets; **does not execute or import the scanned code**.
    Release candidate: **not a claim of calibrated semantic
    accuracy.** Pattern: **structural AST + semantic judgment
    compose** (sibling of riff / JevLint / Abide). `tenbin` still
    owns the lint *skill*; this is a recipe of AST∩remainder, not
    a second Augustus skill. Do not copy YAML. Cards:
    `toolbox-mapping.md` spec/lint; `mixed-architecture.md`.

12. **[`phin-tech/pi-jev-approver`](https://github.com/phin-tech/pi-jev-approver)**
    (LICENSE present this pass; TypeScript; 0★). Pi **shell safety
    gate**. Facts (git branch, path scope, registry-publish regex)
    computed in code; typed Score `risk_level` + Nouls + Choice
    `primary_concern` on the remainder. `commandRules` regex
    **short-circuits** allow/deny — a `deny` rule is a hard block
    no LLM or human prompt can overturn. **No key → fail closed.**
    Optional LLM escalation can only reduce how often you are
    asked, never replace the human as last resort. Author
    side-by-side (their `jev-test` project): classification
    **~500 ms** vs **~2.5–3.5 s** chat-model. Live-tested: `aws s3
    rm` 1.72/2, `ec2 terminate-instances` 1.80/2 in the ask band;
    read verbs matching `action: allow` never called the model.
    **Light note only** — rh-guard-adjacent (coding-agent tool
    gate), different remainder from jevgate (unlisted verbs) and
    Abide (soft project rules). Do not copy the Pi install.

13. **[`Mattepiu/laya-onnx`](https://huggingface.co/Mattepiu/laya-onnx)**
    (Apache-2.0 ONNX export of [`convaiinnovations/laya`](https://huggingface.co/convaiinnovations/laya);
    Hub likes **1** this pass; updated 2026-09-18T10:45Z). Open
    **replica deployment path**: non-autoregressive marker-token
    head in onnxruntime. Card example: **~15 ms on CPU** for one
    Noul. **Do not copy the inherited vs-Jev accuracy table** —
    those rows remain vendor claims (`notes.md` §18,
    `judgment-class.md`). Pattern: ONNX/runtime port of a trained
    decision-only head, beside Laya native and kev Hub. Not Archer.

### Spotcheck (not a fold)

- **[`TheoLeeCJ/SemIf`](https://github.com/TheoLeeCJ/SemIf):** **1551★**
  this pass (2026-09-18T20:51Z). Watch cited awesome claim **1491**
  → **+60**. Independent; not affiliated with Jev/TypeSafe.
- **[`vinnylarouge/jevlike`](https://github.com/vinnylarouge/jevlike):**
  **866★** this pass.
- **Awesomejev 488 / 21644:** watch cited "unchanged." This pass did
  **not** independently re-derive 488/21644.
  [awesomejev.com](https://awesomejev.com/) still showed **410
  entries / 10,093 stars** (refreshed 2026-09-17) in the public
  snapshot fetched here. Do not invent a new count.
- **Tracker** [`multimodalart/jev-reproductions-tracker`](https://huggingface.co/spaces/multimodalart/jev-reproductions-tracker):
  Hub `lastModified` **2026-09-18T20:12:57Z**. Space `models[]`
  still lists **`convaiinnovations/laya`**. **`BlackwoodAI/blackwood-rlcd`
  is not in that array.** Archer remains a *promised* trained-head
  card. Omni decide that shipped (blackwood) is still off the
  tracker this pass.

Cards: `judgment-class.md`; `validation.md`; `applied-mappings.md`
§2 / §5; `mappings.md` §4 / §9; `mixed-architecture.md`; `faq.md`;
`mental-models.md`; `methods-catalog.md`; `toolbox-mapping.md`;
`agent-self-assessment.md`. No wrapper.

## 49. Boundary map, Harbor bake-off vs constrained LLMs, dual-process (2026-09-18 ~15:52 Boise)

America/Boise ~15:52 = 21:52 UTC (archive 214908). Docs-only fold into
open PR #2 (`cursor/augustus-store-envelope-00b4`). Not a competing
PR. Archer 27B drop still **WATCH** (still ~2026-09-19; not landed).
X MCP flap blocked discourse this hour — no tweets invented. Identity
lock vs `typesafe-ai` / `tenbin` / `decision-first` holds. No wrapper,
no install.sh, no copied `uv` / `von serve` / pip how-tos. No invented
metrics. Do not re-fold §48 items, blackwood-rlcd, open-jev-laya-bench,
decision-token LoRA, jevgate, wellposed, jev-reflex-autonomy-lab, Abide,
kev species, jevpandas, bitrate-advisor.

Backend-agnostic: these are **placement / measurement** cards
(extractable-from-state axis; Harbor-style frozen-protocol bake-off;
recompute-from-logs feedstock; Kahneman S1 decide / S2 generate;
combinatorial assembly ≠ extractive keep/drop; packed one-forward open
LLM economics; tiny non-AR local surface). TypeSafe Jev is the
exemplar in the READMEs, not a monopoly. kev is a **star/activity
delta only** this hour (100★ this pass; user cited 97).

### HIGH

1. **[`Zaious/jev-capability-atlas`](https://github.com/Zaious/jev-capability-atlas)**
   (README claims MIT; GitHub SPDX **NOASSERTION** this pass; Python;
   created 2026-09-18T21:30:40Z; 0★; unofficial, not TypeSafe).
   Independent **when-it-holds map with real API receipts**, not a
   leaderboard. They cite [jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)
   and thaiexam charts; they do not redo them. Primary mental model
   this hour: **place the task on one axis** —

   > Is the correct answer fully recoverable from the `state` you hand
   > the model, or does it require outside knowledge that is not in
   > `state`?

   **Self-contained (strong):** classification they cite from
   jev-benchmarks (AG News 91%, Banking77 **87%** — a *different*
   protocol from DMB 76.3% and jevals.com 79.67%; do not merge);
   citation support-checking with claim + quote both given
   (`paraphrase_support` and `reversed_meaning_high_overlap` both
   correctly judged); sarcasm when the trigger is in the given text.
   **Not self-contained (fails, often confidently):** pure recall
   without a supporting passage; scoring that needs a whole-field
   comparison; genuinely overlapping categories.

   **History suite** (`suites/history-recall-context/`, receipt
   `runs/2026-09-19.json`; N=3, single annotator, Chinese history
   only — qualitative axis proof, **not** a knowledge-breadth
   estimate). Cite the table, not the README's 30-second slogan:

   | Case | Question | Context? | Pick | Conf | Dist | Correct? |
   |---|---|---|---|---|---|---|
   | A | 2nd Qing emperor | No | Yongzheng | 0.90 | 0.04 / 0.93 / 0.03 | ✗ (Kangxi by popular convention; ground truth itself contested) |
   | B | 7th Qing (obscure) | No | Xianfeng | 0.07 | 0.25 / 0.37 / 0.38 | ✓ by luck (near-flat) |
   | C | Same as B | Passage in state | Xianfeng | 0.97 | 0.00 / 0.02 / 0.98 | ✓ |

   Informal unsaved B rerun picked Daoguang at 0.08 — both near-flat.
   Teaching: **bare memory is unreliable; reading comprehension over
   supplied text is reliable.** Conflating the two misjudges the risk.
   Retrieve first; put the passage in `state`.

   **Not a state machine internally** (distributed LM understanding —
   paraphrase vs reversed-meaning contrast). **Correctly placed as a
   component node** in *your* code ("a node in your state machine" is
   the architectural instinct; "its internals are a state machine" is
   not). Confidence is a **statistic from the distribution** (RLCD
   trains the distribution; `confidence` is arithmetic on how peaked
   it is), not a second trained correctness score. Calibration is
   **population-level** and can fail **dangerous-high**: DAIR Emotion
   via jev-benchmarks — 48% acc, mean conf **0.819**, 16% of items
   p(correct)=0. That is the "blind guessing" concern that actually
   lands: overlapping blurred categories, overconfident.

   **Browser-use strength is placement, not vision.** Third-party
   `jev-ultrafast` (Browser Use): Google Flights 9.5s → 7.1s; 12-task
   vs Playwright MCP 1.5× faster / 1.6× cheaper, comparable accuracy;
   standalone loop ~1.8s / $0.0005 / 97% (their figures, not
   re-run). Jev is text-only. What held: **DOM snapshot as `state`**
   (a visual task translated into extractive text) + **speculative
   fan-out** over candidate elements. Not screenshots. Same
   component-node placement as lizard-agent / solari-reflex.

   Pattern: **boundary map / placement judgment.** Cards:
   `mental-models.md` (primary); `faq.md`; `question-design.md`;
   `applied-mappings.md` §2 / §6; `mappings.md` §3 / §6; `mixed-architecture.md`.

2. **[`nibzard/decision-model-benchmark`](https://github.com/nibzard/decision-model-benchmark)
   (DMB)** (LICENSE **absent** this pass; Python; created
   2026-09-18T21:48:07Z; 0★; no vendor sponsorship). Independent
   **frozen protocol**: typesafe:jev vs **8 constrained LLMs** vs
   **3 deterministic baselines** (keyword / majority / random). Five
   suites, 60 cells, **$28.34** measured spend; every raw log
   published. **`results/v2/v2.md` is the report of record** (v1
   majority-prior defect corrected; mixed protocol versions merged
   by explicit `--allow-protocol-mix`). Harbor-style measurement
   exemplar: protocol frozen before the run; negative results ship;
   recompute from logs; unknown usage is never a measured zero; later
   runs replace cells whole. Do not copy `uv` how-to.

   **jev (v2, named receipt, not a ranking):**

   | Suite | Acc | Notes |
   |---|---|---|
   | S1 banking77 77-way | **76.3%** | ECE 0.083; cost/1k **$0.07**; p50 **274 ms** |
   | S2 SMS spam | **93.0%** | ECE 0.249 (overconfident vs GLM 0.042) |
   | S3 cardinality | **100%*** | valid coverage **72.7%** (225 failed = **256+ Choice cap**, `400 Too many choices`); 254–255 still 100% |
   | S4 order permute | **76.7%** | flip **13%** (worst LLM 37%) |
   | S5 honesty | **14.3%** | admits-ignorance **49.7%** vs most LLMs 97.3–100% (gpt-5.4-mini **64.7%**); ECE **0.246**; mean conf on no-good **0.543** |

   p50 across jev cells **264–276 ms**, flat 2→255 options. Fastest
   *measured* vs thinking-mode LLMs is **10–16×**, **1.2×** vs
   gpt-oss-120b on Cerebras — **not** the vendor 40–200× claim
   against LLMs left in their slowest default. gpt-oss-120b banking
   **81.3%**; glm-5.3 **80.4%** / spam **94.9%**. **No class wins on
   quality.** Axes that *do* separate: latency, cost, schema-validity
   (jev 0% malformed), Choice cap, honesty. Two OpenAI models sit
   *below* the 87.7% majority baseline on spam.

   **Do not collapse Banking77:** atlas/jev-benchmarks **87%**, DMB
   **76.3%**, jevals.com 2026-09-18 **79.67%** — n / split / protocol.
   Cite named receipts. Pattern: **Harbor/jevals practice +
   when-to-use-vs-constrained-LLM table.** Cards: `validation.md`;
   `judgment-class.md`.

3. **[`Jevals/jevals-data`](https://github.com/Jevals/jevals-data)**
   (CC-BY-4.0; created 2026-09-18T21:36:00Z; 0★). Release boards +
   per-decision JSONL run logs + suite files behind
   [jevals.com](https://jevals.com). Cite "Jevals (jevals.com),
   release \<release\>". **2026-09-18** board: suite **0.1.0**, **8
   systems**, tasks banking77 / helpsteer2 / pubmedqa. Formulas at
   https://jevals.com/methodology/. **Recompute-from-logs pattern**,
   not a third ranking to merge with DMB or atlas.

   Jev on *this* board (native probabilities; n=300 × 5 repeats;
   **not** DMB n): banking77 acc **0.7967**, ECE **0.0981**, p50
   **467 ms**, cost/1k **$0.043**; helpsteer2 Score acc **0.4127**
   (label-prior 0.4167 — barely above chance on that primitive);
   pubmedqa Noul acc **0.9127**, ECE **0.0504**, p50 **438 ms**. Do
   not dump the board as a ranking. Feedstock for Harbor/jevals:
   frozen suite files, item ids pointing at public datasets (item
   text not republished), run header + per-decision rows
   (`item_id`, `epoch`, `target`, `order_seed`, `output`,
   `usage`, `cost_usd`, `seconds`, `malformed`, `refusal`,
   `retries`). Cards: `validation.md`.

4. **[`taro1985/dual-process-ai`](https://github.com/taro1985/dual-process-ai)**
   (MIT; Python; created 2026-09-18T20:55:08Z; 0★). Explicit
   **Kahneman S1 (Jev) / S2 (Gemini)** design pattern. S1: typed
   decision + confidence, ~70–500 ms. S2: free-form text. Mechanism:
   `confidence ≥ τ → S1 decides; else escalate to S2`. **Routing
   fails open** (low conf → S2; the router never refuses). **Safety
   fails closed** (unparseable denied). **Routing accuracy is not
   measured yet** (misroute rate / escalation rate / Brier on
   held-out — the numbers this project needs and does not have).
   Without a key it runs **degraded keyword mode** — **not an
   equivalent S1** (no calibrated confidence; anything not on the
   allowlist escalates). Do not copy hooks / Discord / pip. Crossover
   metaphor for **business/life**, not only SWE: cheap classify /
   route / gate on S1; write / reason / generate on S2. Same split as
   jev-reflex-autonomy-lab (S1 keeps control) and jev-hermes (route ≠
   memory), productized as a cascade. Cards:
   `mixed-architecture.md`; `toolbox-mapping.md`; `mappings.md` §2;
   `agent-self-assessment.md`; `faq.md`.

### MED (brief)

5. **[`simonmesmith/jev-arc-agi-v1-experiment`](https://github.com/simonmesmith/jev-arc-agi-v1-experiment)**
   (LICENSE **absent** this pass; Python; created 2026-09-18T21:32:19Z;
   0★). Direct Jev on ARC-AGI-1 public eval: **4/400 (1%)** fully
   solved; **1.125%** task-weighted (4 + 0.5 / 400); **5/419** exact
   grids; **~$2.32**; **10 minutes**; `jev-1.13.0`; two guesses per
   grid. **Cell-wise Choice assembly:** height/width 1–30, then one
   of ten colours per cell; cells do not see one another; transpose
   for the second guess. Dimensions ~**90%** on first attempt; rarely
   a complete grid. No partial credit for cells. Teaching:
   **combinatorial grid tasks ≠ extractive keep/drop.** A program
   library with no competing candidates **never called Jev** (6
   tasks / 1.5%). Combined policy 2.375% includes hand-written
   programs — tells you less about Jev. Frozen protocol, traces,
   `PROTOCOL.md`. Not a ceiling claim. Cards: `validation.md`;
   `mappings.md` §9; `faq.md`.

6. **[`ikermoel/open-alternative-jev`](https://github.com/ikermoel/open-alternative-jev)**
   (Apache-2.0; Python; 3★; Space
   [`IkerMoel/open-alternative-jev`](https://huggingface.co/spaces/IkerMoel/open-alternative-jev)).
   Packed **one-forward** System One on **any open-weights LLM**
   (HF + vLLM). **Not a Jev reproduction** — packages a capability
   chat APIs hide; no claim about how Jev works. RACE-H (250
   passages × 4 questions, n=1000) on Qwen3.6-27B 8-bit: packed
   **92.9% @ 4.55 q/s** vs one-at-a-time 92.6% @ 1.66; 2.5× fewer
   tokens. Interference **6–9%** of answers move vs a 2.7% numeric
   noise floor; order rotation 8% MMLU / 2.4% RACE-H. Temperature
   scaling ECE 5.4%→2.1% MMLU, 2.8%→1.1% RACE-H. Small 4B packing
   costs 2.8 points — use `separate` when accuracy at stake. On
   vLLM, prefix-cache `separate` is fastest. Economics/architecture
   of **open replicas on the constrained-AR / logprob path**, not
   trained decision-only. Cards: `judgment-class.md`.

7. **[`wfzyx/von`](https://github.com/wfzyx/von)** (Apache-2.0;
   Python; 3★). **14 MB** Needle 3 SAN; non-AR local `POST
   /v1/systemone` drop-in; sub-15 ms CPU *claim* / ~**38 ms** embed
   in their table; ~28 MB RAM. Default needle **52.6%** balanced acc
   on OpenJev `authored144` — **not a calibrated Jev replica**. Other
   backends (berta-v3 / modern / laya) are optional heavier heads.
   **Do not copy the vs-Jev ranking table** (includes a speculative
   Jev weight estimate). Distinguish: jev-local **stub until hf**;
   kev **trained pointer** on Qwen2.5-0.5B; von **tiny SAN** at the
   extreme of the speed/econ class. Cards: `judgment-class.md`;
   `faq.md`.

8. **[`jaredpalmer/kev`](https://github.com/jaredpalmer/kev) delta**
   — still active this hour; **100★** this pass (user cited 97;
   prior fold 61★). Pushed through 2026-09-18T21:51Z. **Light note
   only.** No species rewrite. Hub weights + NOTA training remain
   §45.

### Not this hour

Archer drop **not landed**. X discourse **blocked** (MCP flap) — no
invented tweets. Do not re-fold §48.

Cards: `mental-models.md` (boundary map); `validation.md` (DMB +
jevals-data + ARC); `judgment-class.md` (vs constrained LLM; von;
open-alternative-jev); `mixed-architecture.md` (dual-process;
component node; DOM-as-text); `faq.md`; `mappings.md` §2 / §3 / §6 /
§9; `applied-mappings.md`; `question-design.md`; `methods-catalog.md`;
`toolbox-mapping.md`; `agent-self-assessment.md`. No wrapper.

## 50. GLiNER2.5 extractive compaction — encoder backend, same keep/drop job (2026-09-18 ~16:22 Boise)

America/Boise ~16:22 = 22:22 UTC. Docs-only fold into open PR #2
(`cursor/augustus-store-envelope-00b4`). Not a competing PR. Archer
27B drop still **WATCH**. Identity lock vs `typesafe-ai` / `tenbin` /
`decision-first` holds. No wrapper, no `--plugin-dir` / `uv` how-to,
no copied timeouts or Hub download scripts. No invented metrics.
**Not Jev. Not multimodal.** Do not re-fold §48 extractive recipes,
§49 bake-off, Abide, kev, GLiGuard as a species rewrite, or
pi-jev-compaction as a new product.

Backend-agnostic: this is a **compaction / context-sieve placement**
(pointer keep-drop, soft Choice under a hard mutation envelope,
shadow-mode rollout). TypeSafe Jev is one backend for that *job*
(`tamaratran/fast-jev-compaction`, `vava-nessa/pi-jev-compaction`);
GLiNER2.5 is another. Augustus stays family-first.

### HIGH

1. **[`m-newhauser/gliner25-compaction`](https://github.com/m-newhauser/gliner25-compaction)**
   (Apache-2.0; Python + Claude Code plugin; created
   2026-09-18T17:22:34Z; 1★ at capture). Local, **evidence-first**
   context compaction. Default checkpoint
   [`fastino/gliner2.5-base-v1`](https://huggingface.co/fastino/gliner2.5-base-v1)
   (checkpoint model card Apache-2.0 per their README) chooses a
   retention action for **completed** eligible tool interactions and
   extracts **exact source spans** when the full result is unnecessary.
   **Not a prose summarizer.** User and assistant text unchanged.
   Retained evidence is copied from original **character offsets**.
   Mutating tool interactions are preserved in full. Inference runs in
   a local Python worker after Hub download; transcript analysis does
   not require a remote inference API.

   Per completed pair, one retention action (closed set):

   - `keep_full` — complete call and result
   - `keep_evidence` — exact excerpts from the result
   - `keep_call_only` — call stays; result replaced with a rerun notice
   - `drop` — paired call and result removed

   Inputs: current goal, nearby conversation, tool name and input,
   original tool result. Deterministic safeguards override uncertain
   predictions, protect validated diagnostic spans, preserve recent
   messages and mutations, validate exact offsets, and reject orphaned
   tool results.

   **Four load-bearing mental models (architecture, not a plugin
   catalog):**

   1. **Pointer / extractive, not generator.** Same family as
      [testimonial-miner](https://github.com/AppitStudio/testimonial-miner)
      and [jev-reviewer](https://github.com/choxos/jev-reviewer)
      (`notes.md` §48): the model **selects**; code **copies
      verbatim**. Compaction that invents a prose summary is a
      different (worse) species for auditability. GLiNER locate is not
      a footnote here — character offsets *are* the keep/drop
      candidates. One local multi-head does **categorize** (which
      retention action) and **locate** (which spans) in the same job
      (`judgment-class.md` species map).

   2. **Soft retention Choice under a hard envelope.** Code owns the
      mutation monitor: mutating tools, unknown shell, and shell
      control operators / pipelines / substitutions / redirections are
      treated as mutating → `keep_full`. Missing or invalid evidence
      **fails closed to `keep_full`**. Low-confidence retention
      predictions likewise fail closed to `keep_full`. Contrast: many
      Jev *preference / remainder* gates fail-open (Abide; jevgate
      cannot block). Compaction *drop* (and lossy `keep_evidence`) is
      the irreversible act, so the authorized reduction fails closed.
      From the evidence-preservation view the outcome looks like
      context-sieve "keep on error" (`applied-mappings.md` §1) — name
      the *act*, not the slogan. Conservative shell over-retention is
      their documented limit, not a bug to "fix" by failing open.

   3. **Same compaction job, encoder backend.**
      [`tamaratran/fast-jev-compaction`](https://github.com/tamaratran/fast-jev-compaction)
      asks two Nouls (should the *call* stay? should the *result* stay
      verbatim?). [`vava-nessa/pi-jev-compaction`](https://github.com/vava-nessa/pi-jev-compaction)
      is the Pi cousin: verbatim drop, never summarize. Here GLiNER2.5
      chooses discrete retention actions + evidence spans. Fastino /
      GLiGuard sibling *class* (schema-in-encoder, local) — not a
      GLiGuard safety-schema clone, not a Jev Score, not a Noul.
      Augustus does not pick a vendor for the hole.

   4. **Shadow mode as safe rollout.** Public default `shadowMode:
      true`: local analysis logs the proposed reduction **without
      replacing session history** until explicitly set false. Same
      rollout instinct as jev-harness / is-malicious (log would-do
      first). Compaction mutates memory; shadow is the default because
      a bad drop is not a reversible token cost.

   **Limits (theirs, README; experimental).** Reduction measured in
   **characters, not tokens**. Conservative shell policy may retain
   commands that are actually read-only. Only completed
   tool-call/result pairs are candidates. Domain-specific tuning and
   broad production evaluation remain future work. No published
   token-reduction or retention-quality rates this pass — do not
   invent them. Their config defaults (`minimumConfidence` 0.7,
   `minimumEvidenceConfidence` 0.5, `minReductionRatio` 0.25,
   `preserveRecentMessages` 6) are *their* knobs, not class constants.

   **Siblings — complementary, do not merge.**

   - **`24601/rh-guard`:** reward-hack / eval-integrity on tool use.
     Shared notes only: fail-closed retention, hard shell mutation
     policy, shadow-mode rollout. Different hole. This is not
     reward-hack detection.
   - **GLiGuard:** Fastino encoder sibling (safety-schema classify).
     Compaction is locate+categorize on tool transcripts, not LLM I/O
     moderation.
   - **Abide:** same Claude Code hook-host surface; Abide is fail-open
     Score on diffs; this is fail-closed `keep_full` on compaction.

   **Placement.** Context sieve + exact-text keep/drop
   (`applied-mappings.md` §1–§2). Pillar: selective classification /
   SDT criterion (false drop >> false keep) + runtime-assurance
   sandwich (mutation monitor in code). Hole: sieve / keep-drop.
   Family: GLi\* encoder (GLiNER2.5 local multi-head). Fail-closed on
   the reduction. Eval path: none published this pass (experimental);
   characters≠tokens is the honesty constraint. **Empirical** as
   README behavior. **Hypothesis** that the same envelope transfers to
   *your* transcript domain. Cards: `judgment-class.md` (primary);
   `applied-mappings.md` §1–§2; `mappings.md` §12 / §18;
   `mixed-architecture.md`; `faq.md`; `mental-models.md`;
   `methods-catalog.md`; `toolbox-mapping.md`;
   `agent-self-assessment.md`. No wrapper.

### Omni / Jev-omni

Not multimodal. Usage: extractive context management as a
perception/memory hygiene stage **before** decide. Archive +
landscape pointer.

## 51. CI merge-gate, fail-open wake VOI, S1 indexer, claim-evidence Stop (2026-09-18 ~16:48 Boise)

America/Boise ~16:48 = 22:48 UTC. Docs-only fold into open PR #2
(`cursor/augustus-store-envelope-00b4`). Not a competing PR. Archer
27B drop still **WATCH**. Identity lock vs `typesafe-ai` / `tenbin` /
`decision-first` holds. No wrapper, no npm/wrangler/install.sh/devenv
how-to, no copied ports, thresholds as class constants, or invented
metrics. Do not re-fold §50 GLiNER2.5 compaction, §49 bake-off, Abide,
kev, pi-jev-approver, jevgate, or rh-guard as a species rewrite.

Backend-agnostic: this hour is **decision-model as classifier /
gate / coordinator** (flaky-vs-real CI, VOI resume, S1 extract +
escalate-S2, claim/evidence integrity, Harbor on/off routing,
policy-as-judgment). TypeSafe Jev is the documented exemplar, not
the monopoly. Augustus stays family-first.

### HIGH

1. **[`CaseReed/latch`](https://github.com/CaseReed/latch)**
   (MIT; TypeScript; created 2026-09-18T22:09:12Z; 0★ at capture).
   Merge-gate triage for a **finished** red test run (Playwright /
   Jest / pytest / JUnit XML): cluster failures by signature in
   **code**, TypeSafe Jev labels each cause (one call per cluster, at
   most 8; cached free), **code owns** Gate: PASS (infra noise) vs
   Gate: BLOCK (real failure). The judge never gets to say "ignore"
   alone. `ignore_as_infra` needs `env_cascade` + an infra
   fingerprint. Missing key still prints clusters (`needs_human` /
   `no_key`) and **never fails Playwright** — the reporter is
   fail-open; `--gate` is a **separate** CI step.

   Demo (offline, README): 8 identical connection errors → 1 cause →
   Gate PASS; 5 failing assertions → Gate BLOCK. Policy (theirs, not
   class constants): no key / API error / `cause.confidence < 0.55` /
   `same_root < 0.5` → `needs_human`; `env_cascade` + `same_root >=
   0.7` + fingerprint → `ignore_as_infra`; flake / locator_drift →
   `fix_test`; `assertion_bug` and (`blocks_merge >= 0.55` or Jev
   `action = fix_product`) → `fix_product`. `blocks_merge` sits in a
   noise band ~±0.03; 0.55 is in the empty gap (their calibrate
   claim).

   **Limits (theirs).** Grouping is message-based; a logic regression
   fragments. Measured on `pallets/click`: 2 real regressions → 13
   failures → **10 clusters**. The "70 → 1" figure is an infra-cascade
   property, not a general one. Signature = `apiName` + first 80 chars
   of the normalized error. Error text is redacted in every output.

   **Four load-bearing mental models:**

   1. **Cluster in code, judge labels, policy decides.** Same split as
      OpenSmoke (scan every step; LLM autopsy only on flags): the
      model estimates a *cause class*; the merge act is a table.
      Internals are not a state machine; placement is a component
      node (`notes.md` §49).
   2. **Decision-model as CI flaky-vs-real classifier.** The hole is
      SDT criterion (false PASS on a real bug >> false BLOCK on
      infra), not "make CI smarter." Pair with Harbor (frozen
      artifacts × PASS/BLOCK labels; independent verifier) and
      rh-guard (eval-integrity — do not let the agent game the tests
      latch is classifying). Different holes; shared notes only.
   3. **Fail polarity is per surface.** Reporter never fails
      Playwright (false block of the *run* loses evidence). `--gate`
      fails closed on merge when a cluster is not confirmed infra.
      Name the *act*.
   4. **Do not copy the reporter.** Thresholds, ledger path, and npm
      wiring stay theirs.

   **Placement.** Environment / harness triage
   (`applied-mappings.md` §3) + decision circuits (`mappings.md` §3)
   + SDT (`mappings.md` §7). Pillar: SDT + Leveson sensor≠constraint.
   Hole: triage / gate. Family: closed decision API. Eval path: none
   published as Harbor this pass (demo + unit goldens). **Empirical**
   as README behavior / demo. **Hypothesis** that the same cluster →
   label → policy transfers to *your* runner. Cards:
   `applied-mappings.md` §3; `mappings.md` §3 / §7 / §18;
   `mixed-architecture.md`; `validation.md`; `faq.md`. No wrapper.

2. **[`shitianfang/wakegate`](https://github.com/shitianfang/wakegate)**
   (MIT; TypeScript; created 2026-09-18T22:13:11Z; 0★). Fail-open
   **wake gate** before resuming a sleeping agent (Workers / Durable
   Objects / Node). One typed question: given `waitingFor` plus an
   optional event/observation, is this worth a full LLM turn? Code
   owns sleep duration, skip counters, and force-wake. Skip only if
   Jev answers **and** p(wake) < 0.2. Every other path wakes:
   `fromUser`, nothing-to-judge, skip-limit (default 10), error / no
   key / timeout (5 s), unsure band 0.2–0.5, p ≥ 0.5.

   **Eval (theirs; discount).** 21/21 on 21 hand-written scenarios
   (11 wake / 10 sleep); p50 253 ms, p95 519 ms (n=21). Two of the
   11 correct wakes came only from the unsure band (calendar invite
   0.38; sold out 0.48). Same person wrote the scenarios and the
   question. First yes/no wording scored 16/21 on this set. Current
   three-way Choice picked on a separate 16-scenario **dev** set
   (not in repo). **Smoke, not a benchmark.** Savings unmeasured.

   **Contrast (fail polarity, not products).**
   [`phin-tech/pi-jev-approver`](https://github.com/phin-tech/pi-jev-approver)
   fails **closed** without a key (tool remainder). jevgate **cannot
   block** (allowlist proves; remainder fail-open). Compaction
   (`notes.md` §50) fails closed to `keep_full` because *drop* is
   irreversible. Wake *skip* is the irreversible act here (the agent
   stays asleep), so the authorized skip is the rare, high-confidence
   path; everything else wakes. Horvitz mixed-initiative / VOI: pay
   for the LLM turn only if EV(decision) beats the token cost; a
   regex / user-message / skip-limit already answers without a model
   (meta-VOI). Event/observation are untrusted; `maxSkips` bounds
   sleep, "neither is a security boundary" (their README).

   **Placement.** VOI / gather (`mappings.md` §6) + durable-agent
   control (`mappings.md` §14, Hypothesis) + mixed-architecture
   per-action fail table. Hole: gate / abstain. Family: closed
   decision API. **Empirical** as README safety table. **Hypothesis**
   as production savings. Do not copy wrangler/npm. Cards:
   `mappings.md` §6 / §18; `mixed-architecture.md`; `faq.md`.

3. **[`GreyssonEnterprises/s1-graphify-indexer`](https://github.com/GreyssonEnterprises/s1-graphify-indexer)**
   (+ sibling [`s1-indexer`](https://github.com/GreyssonEnterprises/s1-indexer);
   created 2026-09-18T22:23:04Z / 22:21:15Z; 0★; **license not on
   GitHub this pass — do not invent**). Local-first semantic
   indexer: small zero-shot System-1 models build a knowledge graph
   of a repo; an LLM is used only on the ambiguous tail, and **only
   when the System-1 backend actually loaded**. Default backend
   `gliner2`. Stubs `jev` and `needle` ship `available=False` until
   implemented. GitHub one-liner "10–50× faster than LLM-based
   indexing" is a **target, not a measured speedup**. README: do not
   treat it as a benchmark until the table is filled from one repo,
   both backends, same machine. Table is TBD.

   If GLiNER2 cannot load: artifacts still written (file nodes from
   the chunker, `run_status: degraded`), process exits nonzero, repo
   is **not** dumped to `S1_LLM_CMD`. `query` tokenizes, matches node
   names, walks two hops; no match prints `Insufficient evidence`;
   **it does not invent edges**. `gliner2[local]` extra is heavier
   than declared deps and is not pulled by default.

   **Mental model.** S1 zero-shot **locate/extract** (GLiNER spans /
   relations) on the bulk; escalate-to-S2 only on low-confidence
   remainder — same sandwich as allowlist ∩ remainder and as
   dual-process `conf ≥ τ` → S1 else S2, here the expensive act is
   *indexing tokens* not a chat reply. GLiNER-as-Jev-class cousin
   (`judgment-class.md` locate vs decide): the indexer is not a Noul.
   Same *family* as gliner25-compaction (encoder on code/text) with a
   different hole (graph construction vs memory keep/drop). Do not
   copy pip extras.

   **Placement.** Locate species + escalate-S2. Hole: perceive /
   gather. **Hypothesis** as 10–50×. **Empirical** as degraded-load
   and no-invent-edges README behavior. Cards: `judgment-class.md`;
   `mixed-architecture.md`; `faq.md`.

4. **[`VladyslavHontar/clear-head`](https://github.com/VladyslavHontar/clear-head)**
   (MIT; Python; created 2026-09-18T22:15:08Z; 1★). Claude Code
   **Stop** hook: Jev checks factual claims in the assistant's answer
   against **what it actually read this session**. Anti-hallucinated-
   done. Per claim, keyword-and-frequency retriever (not semantic)
   sends matching tool-output *lines* — not whole files. Classifies
   sentences as factual / proposal / recap / neither; then
   supports / contradicts / doesn't-address. Blocks on contradicted,
   or unsupported with **no** relevant evidence. Coverage below
   `JEV_EVIDENCE_FLOOR` (default 0.3) is "nothing relevant found";
   above the floor, "Jev can't confirm a specific derived fact" is
   usually their documented limit, not a block. `JEV_FIRM` default
   0.6: below that, logged, **never blocks**.

   **Limits (theirs).** Keyword retriever misses paraphrases and can
   match stale session evidence on generic overlap (no recency /
   topic-boundary). A true claim unread this session still flags
   unsupported. Excerpts leave the machine. Do not copy `install.sh`.

   **Placement.** Done-check / claim–evidence entailment
   (`agent-self-assessment.md`; `methods-catalog.md` NLI row).
   Pointer family with jev-reviewer: the model judges against
   retrieved lines, never against another model's prose. Hole: gate.
   **Empirical** as README behavior. **Hypothesis** as transfer to
   *your* transcript domain. Cards: `agent-self-assessment.md`;
   `applied-mappings.md` §2; `faq.md`.

5. **[`reification-labs/foreman`](https://github.com/reification-labs/foreman)**
   (created 2026-09-18T22:46:57Z; 0★; **no license field in
   `mix.exs` — do not invent**). GitHub description: "Parallel
   specialist agents returning typed, calibrated answers behind a
   single System Two foreman. Elixir/Phoenix, Jev/TypeSafe-native —
   `{value, probability}` everywhere." **The checkout is a stock
   Phoenix 1.8 scaffold.** README is the Phoenix generator starter;
   `AGENTS.md` is Phoenix guidelines; `mix.exs` has Phoenix/Ecto/
   Bandit/Req — **no typesafe / jev dependency**. Fold as
   **description-only greenfield**, not a measured product. Do not
   invent an Elixir Jev API.

   **Distinguish** from the existing "foreman" *shape* in
   `agent-self-assessment.md` (Kevthetech143/super-jev loop:
   progress/stuck/complete → continue/stop/retry/verify; the model
   estimates named probabilities; code owns hysteresis). Dual-process
   cousin of [dual-process-ai](https://github.com/taro1985/dual-process-ai)
   (`notes.md` §49): S1 specialists decide; S2 coordinates / writes.
   Typed probability everywhere is the *class* claim, not a receipt
   this pass.

   **Placement.** Mixed architecture / dual-process. **Watch /
   description-only.** Cards: `mixed-architecture.md`;
   `agent-self-assessment.md`; `mental-models.md`.

6. **[`vinilana/jev-gateway-bench`](https://github.com/vinilana/jev-gateway-bench)**
   (MIT; created 2026-09-18T22:29:58Z; 0★). Harbor-shaped bench for
   sibling [`vinilana/jev-gateway`](https://github.com/vinilana/jev-gateway)
   (MIT; product; fail-open if Jev down/slow/wrong key; never fails
   the LLM request). Real coding agents (Codex / Claude Code) on
   chess-engine tasks with Jev routing **on vs off**. Hidden verifier
   (perft + targeted checks) the agent never sees. Chess chosen
   because perft counts are published and one wrong rule changes
   them. Tasks: `chess-engine` (build), `chess-bugfix` (five injected
   bugs), `chess-san` (notation feature). Modes alternate; order
   swaps between reps.

   **Preliminary one-run (author: first signal, not a measurement;
   2026-09-18; Codex 0.154 / `gpt-6-astra` / `jev-latest`;
   `chess-bugfix`):** both 36/36 hidden checks; routing on 4 LLM req /
   76,678 in / 1,313 out / 35 s vs off 6 / 118,709 / 3,231 / 88 s;
   Jev 4 calls ~$0.0008. Jev forced `exec` three times (p 0.91 / 0.99
   / 0.94) then switched tools off to answer (0.98). An earlier pair
   the same day (pre token-metering fix) showed the same *shape* (4
   vs 6 requests; 40 s vs 69 s). With fewer than five runs per mode
   the summary says so. A cheaper unsolved run is not a saving. A
   wrongly forced tool can derail a turn. Do not copy npm/ports.
   Public repo caveat: an agent with web access could find the
   reference; tasks give no reason to look.

   **Placement.** Harbor/jevals practice (`validation.md`): taskset
   (chess + hidden verifier) × harness (Codex/Claude) × runtime
   (fresh gateway per run) × on/off treatment. Sibling of DMB
   (class bake-off) and jev-testbench (collab arms). **Empirical** as
   a *shape* and as one-run signal. **Hypothesis** as a cost/quality
   claim. Cards: `validation.md`; `methods-catalog.md`;
   `toolbox-mapping.md`.

7. **[`LightningK0ala/jev-marshal`](https://github.com/LightningK0ala/jev-marshal)**
   (created 2026-09-18T22:42:24Z). Description: "Repository rules for
   pull requests, enforced by Jev." **Empty git repo** this pass
   (default-branch 409). Fold as **Watch / description-only**. Cousin
   of Abide / jev-pref / if-ai (policy-as-judgment on a PR). No
   metrics, no fail polarity, no license to invent.

8. **[`LilDojd/jevons`](https://github.com/LilDojd/jevons)**
   (MIT; TypeScript; created 2026-09-18T22:43:34Z; 0★). Bounded **Pi**
   execution supervisor. README 100% slop badge. **Not a second
   coding agent:** Jev interprets evidence; ordinary code controls
   freshness, limits, and permitted responses. Skill selection (≤3
   or none), failure recovery (actual completed tool outcomes; exact
   repeats in code), review (chunk × rule), optional investigation,
   verification (select among configured commands; never generates
   them). Default recovery **shadow**. Steering (opt-in) delivers
   fixed replan/ask-user guidance, **never generated commands**.
   Optional pre-tool feedback is off by default. Distinguish from
   `phin-tech/pi-jev-approver` (fail-closed remainder) and
   `kevinpita/pi-jev-context` (sieve). Do not copy devenv/bun.

   **Placement.** Agent self-supervision lifecycle
   (`agent-self-assessment.md`) as a bounded supervisor, not a
   planner. Hole: gate / route. **Empirical** as README policy
   (shadow default). **Hypothesis** as improved task completion —
   "small fixture experiments are useful smoke tests, not evidence"
   (theirs). Cards: `agent-self-assessment.md`; `mappings.md` §9;
   `mixed-architecture.md`.

### MED (brief)

- **[`Victor-Casado/if-ai`](https://github.com/Victor-Casado/if-ai)**
  (MIT; created 2026-09-18T22:09:14Z; 0★). Plain-English PR checks:
  one condition, a required `min-confidence`, one GitHub Action.
  Modes `pr-body` / `diff` / `per-file`. Pass only when true **and**
  confidence ≥ threshold. Empty body/diff, timeout, API error →
  **fail** (fail-closed on the Action). Two-option Choice (Noul has
  no native confidence). PR text is data, not a security boundary.
  Cousin of Abide / jev-pref / jev-marshal. Do not copy the Action
  YAML.
- **[`alexsatch/omp-auto-mode`](https://github.com/alexsatch/omp-auto-mode)**
  (MIT; created 2026-09-18T22:05:41Z; 0★). oh-my-pi plugin. README
  is one line: classify tool calls `safe` / `unsafe` / `ask`.
  Pre-action gate cousin. Description-thin.
- **[`jolehuit/jev-downloads-sorter`](https://github.com/jolehuit/jev-downloads-sorter)**
  (MIT; created 2026-09-18T22:25:30Z; 0★). Device-loop Choice:
  launchd `WatchPaths` on `~/Downloads`; one decision per file;
  ~400 ms README examples. Closed folder catalog; never invents
  folders; never overwrites; OpenRouter unreachable → extension-map
  fallback. Do not copy `install.sh`.
- **[`LakshyaChaudhry/jev-label-desk`](https://github.com/LakshyaChaudhry/jev-label-desk)**
  (created 2026-09-18T22:49:49Z; 0★). Description: weekend project
  using Jev to automate trace/data labeling for a provided taxonomy.
  README empty this pass. **Watch / description-only.**
- **[`flaviomartil/herdr-jev`](https://github.com/flaviomartil/herdr-jev)**
  (created 2026-09-18T22:23:53Z; 0★; license not stated this pass).
  Jev triage ~260 ms + triad orchestration (advisor / implementer /
  reviewer). No key → local heuristic, 0 ms. Do not copy
  `install.sh` or the model matrix.
- **jev-gateway siblings.** Product
  [`vinilana/jev-gateway`](https://github.com/vinilana/jev-gateway)
  (fail-open passthrough) + bench above. Claude Code is `hint` mode
  (cannot force `tool_choice` with thinking / cache). Do not copy
  ports.

### Omni / Jev-omni

Not multimodal. Usage: merge-gate / wake / claim-evidence as
text-state decisions **before** a generative turn. Archive +
landscape pointer. Archer still Watch.

## 52. GLiNER2 Ultrafast — encoder backend of observe→score-among-candidates→code-acts (2026-09-18 ~16:56 Boise)

America/Boise ~16:56 = 22:56 UTC. Docs-only fold into open PR #2
(`cursor/augustus-store-envelope-00b4`). Not a competing PR. Archer
27B drop still **WATCH**. Identity lock vs `typesafe-ai` / `tenbin` /
`decision-first` holds. No wrapper, no `uv` / `.env` / Browser Harness
doctor how-to, no copied ports or Hub download scripts. No invented
metrics. **Not Jev. Not GLiNER2.5. Not multimodal.** Do not re-fold
§48 solari-reflex as a new product, §50 compaction as a species
rewrite, §51 CI merge-gate / wake / Harbor on/off, GLiGuard as a
safety clone, or jev-ultrafast's 7.1 s Flights
row as this demo.

Backend-agnostic: this is an **observe → score among observed
candidates → code acts** placement (pointer/selection among a11y/DOM
controls; hybrid local decide + remote fill; `DONE` is loop
termination, not verified success). TypeSafe Jev is one backend for
that *job* (`browser-use/jev-ultrafast`, `hitakshiA/solari-reflex`);
local Fastino GLiNER2 is another. Same instinct as §50 compaction
(Jev Noul/Score vs GLiNER2.5 encoder): Augustus stays family-first.

### HIGH

1. **[`sahibzada-allahyar/gliner2-ultrafast`](https://github.com/sahibzada-allahyar/gliner2-ultrafast)**
   (MIT; Python; created 2026-09-18T19:35:23Z; 12★ at capture). Fork /
   adaptation of [`browser-use/jev-ultrafast`](https://github.com/browser-use/jev-ultrafast)
   that swaps TypeSafe Jev for **local Fastino GLiNER2**
   ([`fastino/gliner2-multi-v1`](https://huggingface.co/fastino/gliner2-multi-v1);
   Apache-2.0 weights, 307M extractor, GLiNER2 not GLiNER2.5). Real
   browser automation. **Work in progress.** **Not a prose planner.
   Not a screenshot VLM. Not a hosted decision-model API.**

   Load-bearing loop (README + `docs/architecture.md`):

   ```text
   goal → local GLiNER2 → requirements
   page → observed controls → local matching + controller → browser action
                            → text helper (API) if typing needed
   ```

   GLiNER extracts requirement spans and **scores observed controls**.
   Candidates come from DOM / accessible labels (`snapshot.js`); the
   model chooses among them. It does **not** use screenshots. It does
   **not** generate selectors or executable JavaScript. Code owns
   requirement order, progress, calendar matching (English month
   names, ISO, US-style numeric), form submit, freshness / visibility
   / disabled / occlusion checks, and execution. Browser mutations
   are not automatically retried after uncertain execution. The
   inspector's scores are **not calibrated probabilities of task
   success**.

   Default hybrid, not fully offline: local GLiNER2 for decide;
   Mercury 2.5 via OpenRouter for typed field text (OpenAI-compatible
   endpoint configurable). Websites and the text-model service need
   the network. The browser uses an owned tab in an existing Chrome
   profile.

   **`DONE` ≠ verified success.** Termination is heuristic. Loop
   `DONE` reports that the agent stopped; applications must
   independently inspect the actual result. Example verifiers run
   *after* the loop and do not choose actions. Same Harbor-style
   honesty as solari-reflex (`notes.md` §48).

   **Demo claims (theirs; not re-run; not a bake-off).** Live Google
   Flights, one-way NYC→SFO on 9 Oct 2026; no ticket selected or
   purchased. README / `docs/demo.md`: **12.20 s** to visible results
   (12.201 s frame); complete action loop **13.785 s**; API usage
   **~$0.0001** ($0.00010623 across three text-helper calls). Clock
   starts after model loading, goal parsing, initial navigation, and
   first page observation. Independent outcome verification is
   *outside* that clock. Local compute and electricity excluded.
   Their measurement doc: a demonstration, not a controlled
   performance comparison or general reliability benchmark. Do not
   invent a vs-Jev-Ultrafast table; do not merge with the atlas
   7.1 s / 9.5 s Flights figures (`notes.md` §49).

   **Four load-bearing mental models (architecture, not a plugin
   catalog):**

   1. **Same job, encoder backend.** Jev Ultrafast scores among
      observed controls with TypeSafe Jev; this repo scores among
      observed controls with local GLiNER2. The *hole* is
      observe → score-among-candidates → code acts. Compaction
      (`notes.md` §50) already taught that keep/drop is
      backend-agnostic (Jev Noul/Score vs GLiNER2.5). Computer-use
      selection is the same lesson on a different hole. Augustus
      does not pick a vendor for the hole.

   2. **Candidates from observation, not generation; not
      screenshot multimodal.** Control set is a11y/DOM-derived.
      Pointer/selection species with
      [solari-reflex](https://github.com/hitakshiA/solari-reflex)
      (structured obs, Jev, no screenshots; `notes.md` §48) and
      [laya-mind2web-browser-agent](https://huggingface.co/ShaunSpark/laya-mind2web-browser-agent)
      (Laya open head; operation + target index over a list of
      interactive DOM elements; author-reported 74.3% on 68
      held-out — small n, not a ranking; Apache-2.0). Contrast
      [blackwood-rlcd](https://huggingface.co/BlackwoodAI/blackwood-rlcd)
      (screenshot + letters code already marked → Choice; CC BY-NC;
      `notes.md` §46). Pixel-free / DOM-as-text is the preferred
      computer-use placement when the environment is already
      structured (`judgment-class.md` vision pattern 1;
      `mental-models.md` §boundary).

   3. **Hybrid local decide + remote fill.** Economics: tiny API
      for TYPE text; local encoder for control scoring. Mixed
      architecture, not dual-process-ai (that product is S1/S2 with
      a confidence τ; routing accuracy unmeasured — `notes.md`
      §49). Here the *split* is where compute lives: judgment on
      the laptop, generation only where a string must be typed.
      Code still owns actuators. A loop with nothing to type stays
      local.

   4. **Composition + independent outcome check.** Perception
      (Browser Harness / DOM snapshot) → decision (GLiNER2) →
      verified act (code). The post-run verifier is not the
      decision policy. Same Harbor instinct as solari / jev-e2e:
      score the *task*, not a self-report.

   **Limits (theirs, README + architecture; experimental).** Common
   HTML and ARIA patterns; behavior varies with page structure and
   goal wording. Date parsing is English-oriented. Not fully
   offline. Optional traces can include page content. No published
   Harbor taskset or calibration of control scores as P(success) —
   do not invent them.

   **Siblings — complementary, do not merge.**

   - **`browser-use/jev-ultrafast`:** same job, Jev backend. Credit
     in their README. Do not treat this demo clock as a head-to-head.
   - **`hitakshiA/solari-reflex`:** same observe → decide → verified
     act; Jev; Harbor-style table vs Codex on Solari (`notes.md` §48).
   - **`m-newhauser/gliner25-compaction`:** Fastino encoder sibling
     *class*, GLiNER2.5 (`fastino/gliner2.5-base-v1`), compaction /
     keep-drop hole — not this checkpoint and not browser CU
     (`notes.md` §50).
   - **GLiGuard:** Fastino encoder sibling (safety-schema classify).
     Not control scoring.
   - **blackwood-rlcd:** screenshot multimodal decide. Different
     input. Not this placement.
   - **`24601/rh-guard`:** light note only — independent outcome
     verification vs trusting `DONE`. Not reward-hack detection.

   **Placement.** Exact-text keep/drop among observed controls
   (`applied-mappings.md` §2) + mixed architecture (code acts; LLM
   writes TYPE only). Pillar: search/control (one substituted
   classifier step) + runtime-assurance sandwich (freshness /
   visibility / no generated selectors in code). Hole: perceive /
   keep-drop / replace-one-classifier-step. Family: GLi\* encoder
   (GLiNER2 local, `gliner2-multi-v1`). Fail-closed on actuation
   (code validates the observed node). Eval path: their Flights
   demonstration + post-run verifier; no class bake-off this pass.
   **Empirical** as README / architecture behavior. **Hypothesis**
   that the same envelope transfers to *your* sites. Cards:
   `judgment-class.md` (primary); `mixed-architecture.md` (primary);
   `applied-mappings.md` §2; `mappings.md` §9 / §12; `faq.md`;
   `mental-models.md`; `validation.md`; `methods-catalog.md`;
   `toolbox-mapping.md`; `agent-self-assessment.md`. No wrapper.

### Omni / Jev-omni

Not multimodal pixels. Strong **composition / open-weights decide**
exemplar for browser computer-use (local encoder + remote fill).
Archive + landscape. Harbor-style independent verify is already in
their framing.
