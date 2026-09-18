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
