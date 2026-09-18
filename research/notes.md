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

- No independent reproduction of speed/cost/quality claims; no MCTS+Jev
  project found yet (closest: beam-search cookbook, jev-trader per-step
  decisions, StarCraft run). The user's MCTS example is direction, not yet
  an observed artifact — treat MCTS-as-value-function as EXPERIMENTAL.
- 255-option Choice at scale (>255 candidates) has no canonical public
  recipe; tournament-bracket decomposition is UNPROVEN (see skill warnings).
- Score cross-question comparability and calibration on deployment
  populations: unmeasured. Thresholds from cookbooks are examples, not rules.
- Prices/limits/aliases will move; evals page (evals.typesafe.ai) and
  Discord #show-and-tell are the fastest-moving sources — check every pass.
