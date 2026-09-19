# Refresh log

## 2026-09-18 ~01:50 UTC — baseline
- Pulled docs index (llms.txt: 16 cookbooks, 4 patterns), primitives,
  confidence, how-to-build, jaggedness, use-case map, Choice, Score,
  quickstart, official skill, awesome-typesafe (45★), jev-trader,
  jev-ultrafast, jev-review/openjev/jevlike (search excerpts), dev.to guide,
  DataCamp, Register, Truescho, X launch posts (web index).
- Oracle review (design-and-falsification companion; 5 mappings + rejections;
  4-file skill; evidence labels) incorporated into skill architecture.
- Gaps: direct Tavily/Exa API calls fail (plugin double-encodes body);
  X/XAI creds absent; no MCTS+Jev artifact found; no independent benchmarks.
- Next pass: re-check awesome-typesafe commits, evals.typesafe.ai, Discord
  #show-and-tell, `jev-1.13` GitHub code search, model alias + price + limits.

## 2026-09-18 02:45 UTC — scheduled refresh
- Gemini Deep Research completed: 1.15M tokens processed, 32 searches, 26k-token cited report (interaction v1_ChduNkdz…9zVFFzQWM, fetchable via GET /v1beta/interactions/{id}).
- GitHub census (gh CLI, created >2026-09-10 + topics jev/typesafe + code search 'jev-1.13'/'api.typesafe.ai'): ~60 Jev-specific repos, framework integrations in LiteLLM, LangChain(+JS), Vercel AI, Mastra, Eliza, Ax, Composio, Laravel AI, instructor-php, agentgateway. All 87 cloned to /home/user/workspace/jev-archive (1.2GB).
- New measured numbers: pi-warden 150 paired runs 6→0 rule breaks, ~$0.00004/0.3s per judgment; GodsBoy router 94.4% vs 70.8% lexical baseline (72 synthetic requests, jev-1.13.0); openjev-sglang smoke incl. 64-answer question + 65 rejected; winnow hides blocks at relevance<=0.22; jev-ultrafast 2402★ (was ~2100).
- New from Gemini report: Archer Hume 6,800-record study — ECE 0.0313 on MMLU sample but 32% accuracy on novel two-step math word problems (recognizes ignorance, cannot reason steps). Mike Taylor/Every — 777 judgments, ~25x faster and ~580x cheaper than Fable 5.1, 6/7 planted defects found. Near Here moderation — 96% acc at 0.59s and $0.043/1k decisions. Pricing confirmed $42/B input tokens, output free, 32k envelope. Doom demo ≈10 calls/s ≈$7/hour, fed structured JSON state (not raw pixels) — criticism to record. Cookbooks gained self-consistency: nouls (15 repeats over one insurance claim).
- Provider status: Tavily 403 (same body bug as 09-17); Exa tweet category removed (HTTP 400); X/XAI creds still absent. X coverage stays via web index + Gemini grounding.

## 2026-09-18 02:46 UTC — scheduled refresh
- awesome-typesafe HEAD: 8b9e8aa3c44f
- https://docs.typesafe.ai/llms.txt -> HTTP 200
- https://evals.typesafe.ai/ -> HTTP 200
- https://openrouter.ai/typesafe/jev-1.13 -> HTTP 200
- action: diff index/cookbook list vs research/sources.json; update notes.md + log.

## 2026-09-18 14:42 UTC — X+GH hourly discourse pass
- Method: provided live scan (USAGE-DIGEST + theme-digest.json +
  github-topic-jev-last-hour.json, window 13:39–14:39 UTC) archived under
  `research/archive/hourly/2026-09-18T14/`. X API still not used; theme
  digest is the X source for this hour. GitHub = `topic:jev` movers (34).
- Live checks: awesome-typesafe HEAD `6eef30ba8c3f` (was `8b9e8aa3c44f`);
  https://docs.typesafe.ai/llms.txt -> HTTP 200;
  https://evals.typesafe.ai/ -> HTTP 200;
  https://openrouter.ai/typesafe/jev-1.13 -> HTTP 200.
- Docs index: cookbook list unchanged vs sources.json (still the same
  primitives/patterns/cookbooks). No API contract edits.
- Discourse: cost/prefilter 48, tool routing 33, agent gate/linter 27,
  mixed architecture 16, skepticism 11. Design signal: mixed architecture
  is the default; "just classification" is answered with placement.
- Novel GH shapes recorded in notes.md §17 and findings.md: git-jev-stage,
  jevprune, llama-index-jev (fail-open rerank / fail-closed select),
  jev-pref, lizard-agent, jevql, OpenSmoke, decision-first, tenbin, Janus,
  LightJev, snifftest/repear/clean-code-review, is-malicious.
- Skill: added `references/mixed-architecture.md`; SKILL.md protocol +
  index + classification non-negotiable; identity lock vs typesafe-ai /
  tenbin / decision-first. Version 0.3.0.
- Next pass: re-check awesome-typesafe since `6eef30ba8c3f`, evals page,
  whether LlamaIndex nDCG numbers get a second dataset, ECE claims on X.

## 2026-09-18 14:55 UTC — Laya open-head note
- Source: https://huggingface.co/convaiinnovations/laya (HF card HTTP
  fetched this pass). Open System-1 head, Choice/Score/Noul, self-hostable,
  text-only, 512 tok/question. Vendor vs-Jev table recorded as **claims**.
- Design implication only: decision-design cards stay backend-agnostic
  (typed judgment provider); TypeSafe Jev remains the documented default;
  open weights transfer calibration/eval duty to the operator.
- Skill: one-liner in SKILL.md + provider slot on the design card +
  mixed-architecture reproduce/open paragraph. No Laya how-to, no copied
  `predict()` contract.
- notes.md §18; sources.json + findings.md updated.

## 2026-09-18 15:10 UTC — class-scope (Jev exemplar, not monopoly)
- Not a new X+GH hour. Last hourly scan remains
  `research/archive/hourly/2026-09-18T14/`. This pass is literature +
  skill identity: Augustus designs for the whole class of fast/cheap
  categorization-classification-scoring models.
- Sources fetched HTTP 200: GLiClass arXiv 2508.07662; Knowledgator
  GLiClass intro; listwise/calibration 2208.06164 and 2211.01494; SigLIP
  HF docs; vision notes 2510.13364 and 2608.19376; Laya HF card already
  in sources.
- Skill: `references/judgment-class.md` (families, listwise vs decision,
  vision patterns, agent-architecture portents); SKILL.md opening,
  description triggers, protocol (family from hole; family-aware fan-out;
  ranking vs decision fail policy), mapping-index row, design-card hole
  + family fields, non-negotiable on affinities. FAQ: "is Jev the only
  model?", GLiClass vs Jev vs cross-encoder, CLIP/SigLIP gating.
  mixed-architecture + applied-mappings intros class-wide. README /
  marketplace / CHANGELOG / ecosystem. Identity lock vs typesafe-ai /
  tenbin / decision-first unchanged. No invented API contracts.
- notes.md §19; sources.json papers appended; findings.md batch #7.

## 2026-09-18 15:20 UTC — formal / semi-formal / crossover card
- Curriculum `FORMAL-METHODS-SYSTEM-ONE.md` not in repo; GitHub code
  search returned 0. Card from the brief + fetched docs.
- HTTP 200: Hillel vibing-specs (2026-03-10), Quint, Antithesis,
  Resonate DST, Alloy, TLA+, P, NuSMV, PRISM, Event-B wiki, Dafny,
  OpenJML, Frama-C, SPARK, NN/g gulfs, NATM Wikipedia, Leveson STAMP
  intro PDF. event-b.org and mitpress book page failed HEAD; cited
  wiki/PDF instead.
- Skill: `references/formal-methods.md` (ownership; model-finders;
  deductive; DST; TOCTOU / soundness theater / vibing specs; NATM /
  snap-fit / Norman / Leveson). SKILL.md protocol + index +
  non-negotiable. FAQ: replace TLA+? / Noul ≈ proof? methods-catalog
  rejected row; composition-algebra #9; toolbox family. No invented
  APIs. Identity lock holds.
- notes.md §20; sources.json appended; findings.md batch #8.

## 2026-09-18 15:25 UTC — cross-domain mental models (not SWE-only)
- Critical scope: Augustus is design judgment across AI, SWE, business,
  knowledge work, and life. Formal methods are one pillar.
- HTTP 200: Elkan rescale.pdf, sklearn cost-sensitive threshold, VOI /
  detection theory / MCDA / expected-utility Wikipedia, NIPS 2008
  reject-option paper.
- Skill: `references/mental-models.md` (EU, abstention, calibration,
  VOI, MCDA, search/control, SDT, Leveson, NATM/snap-fit/Norman, domain
  gallery). SKILL.md mission/description/protocol/design-card
  domain+pillar. FAQ "only for software?". mappings.md Hypothesis
  beyond-SWE examples. boundary-audit TOCTOU/vacuous-spec red flags.
  README/marketplace exposure. Non-negotiable unchanged: exact work in
  code/policy; model owns narrow judgment; never launder Noul as proof.
  No invented APIs.
- notes.md §21; sources.json appended; findings.md batch #9.

## 2026-09-18 15:40 UTC — FM expansion + Hypothesis mapping cards
- Curriculum `FORMAL-METHODS-SYSTEM-ONE.md` still absent (GitHub code
  search 0). Expand `formal-methods.md` in place (no duplicate
  `formal-semi-formal.md`).
- HTTP 200: Apalache, Alloy-vs-model-checkers FAQ, Antithesis DST
  explainer, PufferLib docs, arXiv 2406.12905, Hillel vibing specs,
  Hillel QCon 2026 informal-methods talk, Resonate DST, Antithesis intro.
- Skill: Alloy Analyzer vs Apalache teaching split; DST trio
  (Antithesis / Resonate / PufferLib Ocean); TOCTOU-of-Noul named;
  AI×FM harms (receipt theater, mode laundering). mappings.md §6–§9
  Hypothesis cards (VOI, SDT/ROC, Leveson, search/control).
  boundary-audit stop conditions. FAQ Alloy vs Apalache / PufferLib.
  methods-catalog + toolbox + composition-algebra wiring. SKILL.md
  index + description triggers. Identity lock holds. No invented APIs.
  Promote Hypothesis only with an acceptance test that ran.
- notes.md §22; sources.json appended; findings.md batch #10.

## 2026-09-18 15:50 UTC — fold attached curriculum
- Archived five research docs under `research/archive/curriculum/`.
- Skill: `formal-semi-formal.md` one-screen alias; named rows folded into
  `formal-methods.md` (Amazon TLA+, mCRL2/KeYmaera, Alloy composition
  table, semi-formal artifacts, ITP/PBT, Resonate HQ identity, Cauli,
  Kent/Shirky/Vanderburg/Agans, help/harm checklist). mental-models
  master rule, conformal, OR, epistemology, harms. mappings.md §10–§16
  Hypothesis. boundary-audit checklist. Identity lock holds. No
  invented APIs. Promote Hypothesis only with an acceptance test.
- HTTP 200: Amazon FM PDF, Cauli, Shirky, dreidel, Resonate why/tested,
  mCRL2, KeYmaera X, arXiv 2502.15441, Lamport Agent.
- notes.md §23; sources.json appended; findings.md batch #11.

## 2026-09-18 16:00 UTC — jevals ecosystem pointer
- Source: https://github.com/dayhaysoos/jevals (README HTTP 200 this pass).
  Local MIT workbench: labeled Noul/Choice/Score cases, compare runs,
  WebMCP + agent skill. Not affiliated with TypeSafe.
- Role: empirical acceptance-test *surface* for Hypothesis mapping cards;
  complements `scripts/evaluate_decisions.py`. Workbench existence is
  Empirical; cards stay Hypothesis until *your* labeled cases + test run.
- Skill: one sentence in `references/validation.md` next to the offline
  evaluator. Catalog bullet in `docs/ecosystem.md`. No CLI/env/ports in
  SKILL.md; Augustus is not a jevals how-to.
- notes.md §24; sources.json appended; findings.md batch #12.

## 2026-09-18 16:07 UTC — 10:07 Boise hourly fold
- Window: America/Boise 10:07 = 16:07 UTC. Named X posts + GitHub
  READMEs fetched (all HTTP 200).
- GLiNER promoted from cousin footnote to species-map peer (locate vs
  GLiClass categorize vs Jev decide vs GLiNER2.5 local multi-head).
  36× Browser Use claim labeled tweet/Hypothesis.
- openjev-lm: 92.9% / 6 vCPU teacher-distill; not independent gold.
- mappings.md §17 paraphrase brittleness; §18 allowlist ∩ remainder
  (jevgate + doc-router 1.74× $). FAQ: LLM-as-judge, allowlist-then-judge.
- Pointers: pi-jev-context, jevscope next to jevals. No thin how-tos.
  Domain-general mission unchanged. Identity lock holds.
- notes.md §25; sources.json appended; findings.md batch #13.

## 2026-09-18 16:20 UTC — trolley / dual orchestration / JevLint
- Han Xiao trolley: jina-reranker-v3.5 Jev-style API always pulls the
  lever (1 or 1B). Empirical rejection of listwise-as-decide.
- James Ward: Jev-as-tool vs Jev-as-outer-loop; MCP schemas as state.
- huntedman/JevLint: file-level convention Nouls; jev-pref sibling.
  doc-router already in §25 (judge = 2.5% of OCR bill).
- notes.md §26; no CLI/how-tos. Identity lock holds.

## 2026-09-18 16:45 UTC — Hume architecture reconstruction
- Fetched https://archerhume.com/posts/jevs-architecture-unmasked/ HTTP 200
  (17 Sep 2026, ~28 min). Tweets HTTP 200:
  https://x.com/4rcherhume/status/2100555442061820286 and
  https://x.com/4rcherhume/status/2100848840643612729 (text via X API).
- Recorded as reconstruction from ~10k probes of jev-1.13.0, labeled
  published / observed / inferred. Not a TypeSafe contract. Envelope
  (~32k branch, ~65k request, 255 options) cited as an independent probe
  of the existing notes, not an override.
- Skill: short compute-graph card in judgment-class.md (three holes;
  TypeAR comparison sentence only, no how-to); calibration paragraph in
  mental-models.md; one FAQ; one formal-methods PBT paragraph; one
  validation.md IIA clause. No SGLang snippets, no new script.
- Open-weight drop status: WATCH (tweet: ~65% done). "Smarter than Jev"
  weighed against his own order-sensitivity and calibration warnings.
- notes.md §31; sources.json; findings.md batch #15.

## 2026-09-18 16:45 UTC — effect-oriented loops + GLiNER author

- James Ward image post: "Effect Oriented" is ZIO (his effect-oriented
  client), not Effect.ts. Load-bearing: handler runs ZIO effects while
  Jev stays the outer decision loop. Hypothesis `mappings.md` §19;
  extends dual orchestration. No client signature in SKILL.md.
- urchade (GLiNER author): GLiNER2 multi-task classification "like jev"
  is GLiGuard Figure 3 — schema-conditioned softmax/sigmoid, one pass.
  Confirms categorize beside decide. 36× still a tweet.
- notes.md §28. HTTP 200 on both posts, arXiv, both GitHub URLs.
  `note_tweet` absent on both.

## 2026-09-18 17:05 UTC — GLiGuard README / paper claims

- HTTP 200: `fastino-ai/GLiGuard` README, arXiv abs 2605.07982, HF
  `fastino/gliguard-LLMGuardrails-300M`.
- Recorded only what those sources say: 0.3B GLiNER2 encoder; one
  bidirectional pass; 23–90× vs 7–27B; README 16.2× / 16.6× (abstract
  says 17× latency; table matches README). Not a Jev weight clone.
- README OR / refusal rule left as existing policy-in-code. "like jev"
  stays the §28 tweet (discourse). FAQ one row. No install copy.
- notes.md §30. Ward card already in `mappings.md` §19; not rewritten.


## 2026-09-18 16:55 UTC — TypeAR constrained-AR surface

- README HTTP 200 (blob 43f456ae, repo a49c320). Python, created
  2026-09-17, updated 2026-09-18, no license file. X posts for the
  Archer drop re-fetched (`note_tweet` absent; text complete). Essay
  reconstruction is notes §31.
- TypeAR is a next-token constraint surface, not a sixth decide
  species. Enum ≤16, no abstention primitive. 5.8× is their K=16
  boolean example only. Sequential conditioning compared to Jev
  fan-out and to mappings §19 (already present; not rewritten).
- Archer drop remains WATCH. Hub search found no archerhume /
  4rcherhume weights. rh-guard not confirmed in this tree.
- notes.md §32; judgment-class card; one FAQ row; one formal-methods
  paragraph. No serving-stack snippets in skill cards.

## 2026-09-18 17:02 UTC — ~11:02 Boise hourly fold

- America/Boise ~11:02. Docs-only. Archer drop still **WATCH** (Hub
  authors `archerhume` / `4rcherhume` empty). HTTP 200 on cited HF
  cards, GitHub READMEs, essay, X URLs, SREGym blog.
- Archer clarifications folded (dense 27B one-forward-pass; multimodal
  generalization report; AU healthcare residency; "decision models"
  name). When-to-use table in `judgment-class.md`.
- HF: jev-gate-student-b (148,160-row corpus), jp-sns-jev7-estimator,
  open-jev-deberta-v3-large, mini-jev-runs 27.9k, jev-tree-choice-cap.
- Device/harness: jev-mobile, jev-macos-loop, jev-harness (existing),
  routeKit. HacksonClark SREGym-Lite 20/50→24/50; Coppe placement
  sentence. No wrapper, no install copy.
- notes.md §33; sources.json; findings.md batch #19.
## 2026-09-18 17:20 UTC — marginals, Nimble, djev-spark

- Meijer post HTTP 200, `note_tweet` present. Jev is not probabilistic
  programming; Kleisli qualifications exaggerate; endorsed gloss is
  marginals vs joint. Card in `judgment-class.md`; FAQ row; one
  decision-theory sentence. No category-theory tutorial. Joints stay
  with TLA+/Alloy/contracts. notes.md §34.
- Nimble README + HF card + announcement, all HTTP 200. Did not distill
  from Jev. Hard synthetic labels; 2,676 used to train / 324 holdout.
  Table: Nimble 90.12%, Jev 1.13.0 93.21%, untuned Qwen3.8-27B 84.88%,
  base 9B 66.36%. Named receipt, not a ranking. Model card Apache-2.0
  LoRA on Qwen3.5-9B; repo LICENSE 404. Tweet "100ms" and rounded
  percents not promoted. 9B-vs-Jev on your labels is Hypothesis.
  notes.md §35. One `validation.md` sentence. No serving snippets in
  skill cards.
- djev-spark README HTTP 200. DiffusionGemma 26B-A4B NVFP4; Jev-shaped
  API; images are an extension; sequential / think / entropy-triggered
  samples in the README. vLLM PR 57250 HTTP 200, patch not reviewed.
  Empirical as interface; Hypothesis as a win over a decision head.
  Holes table extended; essay not rewritten. License null. notes.md §36.
- tenderizzation "welcome back ResNet-50": one sentence, notes.md §37.
  Classification FAQ not expanded.
- Identity lock holds. No CLI, env, ports, or install in SKILL.md.

## 2026-09-18 17:35 UTC — Atallah entropy buckets

- x.com fetch 403 on both status URLs. `api.fxtwitter.com` code 200
  for both. Later post quotes the earlier one.
- 2026-09-14T14:50:17Z: three buckets (who reviews / review / write a
  PR); frontier models only for the third, his view.
- 2026-09-18T14:59:35Z: "first model ever" for low- and medium-entropy
  tasks. Claim, not Empirical.
- Photos: OpenRouter cost-vs-usage bands (deterministic / semi-variable
  / variable) and a programming overlay (scan / review / write). Not
  transcribed as a dataset. Not a benchmark.
- Card in `judgment-class.md` (composes with Meijer; agent-loop shape;
  load-bearing caveat). When-to-use pointer only. One mental-models
  sentence. One formal-methods sentence. No mappings §20. notes.md §38.
  Hypothesis. No CLI.

## 2026-09-18 17:39 UTC — perception then judgment

- Basit post not found. X search for Basit + Jev/SAM returned Turkish
  "basit," not a handle. No tweet id invented. Card stays Hypothesis.
- SAM 3.1 name verified: Hub HTTP 200 (raw README 401, gated);
  RELEASE_SAM3p1.md HTTP 200; Meta blog HTTP 200. Masks and tracks.
  Object Multiplex. Perceive. No install or API copied.
- Moritz Kremb post fetched (note_tweet present): transcript then Jev.
  Instance of the pattern, not the Basit source. His ~300 ms and
  $0.0002 not promoted.
- Card in `judgment-class.md` beside djev-spark / Watch. Species line:
  SAM and ASR perceive, Jev decides. Information dies at the interface.
  Archer stays Watch (no audio, no Hub weights). djev-spark images
  unchanged (think/sequential reject images).
- One mental-models sentence. One formal-methods contract-surface
  sentence (PBT the schema; Noul is not over raw pixels or raw audio).
  notes.md §39. Entropy allocator §38 not rewritten.
- Identity lock holds. No CLI, env, ports, or install.

## 2026-09-18 17:50 UTC — eval & hill-climb

- Basit post not found (X search empty). No tweet id. HoH, Room driver,
  live Room, and video-as-judge-last labeled "Basit ask, primary post
  not retrieved."
- jevals `af6fecc`: README, PRODUCT.md, DESIGN.md, skills/jevals/SKILL.md.
  `npx jevals` verified as the README entry. No flags, keys, or ports
  in skill cards. Score taught as enabled (later PRODUCT + DESIGN +
  README), not the earlier "Score deferred" sentence. "No built-in
  split" and "no unknown label" are the agent skill; PRODUCT/DESIGN/README
  do not document a split and do not say "unknown."
- Harbor README + task docs HTTP 200. Separate verifier env documented;
  default shares the agent container. No Harbor CLI.
- verifiers v1 blog (2026-07-10, Will Brown et al.): taskset / harness /
  runtime. Harbor is their taskset format, not a second product.
- Canonical section `validation.md` Eval & hill-climb. One composition
  table. notes.md §40. Perception §39 and Atallah §38 not rewritten.
  Identity lock holds.

## 2026-09-18 17:55 UTC — perception-decision pipeline

- Basit post still not retrieved. No tweet id. Card is Hypothesis.
- Ax README re-read: DSPy for TypeScript. Existing sources.json URL
  `https://github.com/ax-llm/ax`. No second URL. No call shape added.
- Pipeline card in `validation.md`. Points at §40 for Harbor /
  Verifiers / jevals hygiene instead of restating it. §39 composition
  card and §38 allocator left in place. Formal-methods contract
  sentence not rewritten; one hill-climb pointer only.
- notes.md §41. Nimble ECE not claimed. openjev-lm spelling kept.
  No CLI.

## 2026-09-18 17:59 UTC — ~11:59 Boise hourly fold

- America/Boise ~11:59. Docs-only. Archer still **WATCH** (Hub empty;
  latest @4rcherhume posts are replies). Local jev-archive path absent;
  READMEs and X fetched live. HTTP 200 on cited URLs.
- Three open paths named on the when-to-use card: encoder / AR
  constrained decode (TypeAR + pcdServer) / trained decision-only.
- HIGH: pcdServer, jevql store-frame, OpenSmoke env vs policy,
  jev-mode, jot, typesafe-jev-tools 149-row.
- MED: openevals, hermes-jev-north-star, TheoOliveira/pi-jev,
  jev-plays-games, joxide, laya-typed-decisions. routeKit already §33.
- X discourse archived in notes §42. No wrapper, no install copy.
- notes.md §42; sources.json; findings.md batch #25.

## 2026-09-18 — second adversarial pass

- Whole skill at `7b3a0c3`. Zero blockers. §27 fixes still held.
- Patched five kept defects (`notes.md` §43): unpublished jevals
  entry removed from `validation.md`; SAM/ASR out of the perceive
  species; two call shapes out of `optimizer-integration.md`;
  $0.042/MTok tagged; GodsBoy 94.4% marked exploratory.
- Dropped: Harbor wording matches the verifiers v1 post; mini-jev-runs
  dual use; translation-invariant claim; SREGym arithmetic.

## 2026-09-18 18:58 UTC — ~12:58 Boise hourly fold

- America/Boise ~12:58. Watch run 185349. Docs-only. Archer still
  **WATCH** (no architecture rewrite; ~65% done is user watch, not a
  retrieved status tweet this pass). Local jev-archive path absent;
  READMEs and X fetched live.
- Novel vs §42: sqlite-jev in-engine store fork; bitrate-advisor hard
  envelope; jev-routing host adapter; jev-claw OpenClaw routing;
  mmalisper JOB planner thread; Higgsfield auto-route claim.
- Frames only (already folded): jev-harness practice, openjev-lm
  receipts, jev-gate as memory sieve, encoder vs decoder replica.
  README stubs: jev-voice-control, JevML. Skip rewrite: jev-pref,
  mini-jev-runs, jev-tree-choice-cap.
- notes.md §44; sources.json; findings.md batch #27. No wrapper.

## 2026-09-18 19:54 UTC — kev (runnable Archer reconstruction)

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`); no
  duplicate PR. Docs-only. Archer 27B drop still **WATCH**.
- Source: [`jaredpalmer/kev`](https://github.com/jaredpalmer/kev)
  README + MODEL_CARD + LICENSE Apache-2.0 + release v0.1.0, all HTTP
  200. 24★. Isolation / ECE / acc / permute / IIA / forgery cited from
  README; not re-run. Not a Jev distill (public gold CE).
- Cards: `judgment-class.md` (family, holes, when-to-use, dedicated
  card); FAQ; `validation.md` bake-off + mechanism tests;
  `mental-models.md`; `mixed-architecture.md`; `formal-methods.md`;
  `optimizer-integration.md`; SKILL.md path + identity lock.
- notes.md §45; sources.json; findings.md batch #28. No wrapper.

## 2026-09-18 20:03 UTC — ~14:03 Boise hourly fold

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`).
  Docs-only. Archer 27B drop still **WATCH** (Hub empty; user watch
  ~2026-09-19).
- HIGH: blackwood-rlcd (open multimodal RLCD, CC BY-NC, Jev-compatible
  shim; web 0.907 vs Jev text-only 0.480; letter-shuffle 0.133 vs
  0.587; ECE 0.037; ~200 ms H100; Jev still leads general text 0.850
  vs 0.786). open-jev-laya-bench (26+9, 11959 items; ECE/NLL/Brier;
  Δ +0.023 / +0.229; LLM-as-judge is not the score). Foodoo1
  decision-token QLoRA (64→95% / 85.2→98.8% at ~234 ms; synthetic).
  jevgate frame (allowlist proves; fail-open). wellposed (missing
  other → confident wrong). jev-reflex-autonomy-lab (S1 keeps control).
- MED: jev-decision-layer, jev-e2e, jevpandas.
- Cards: judgment-class, validation, question-design, mappings §18/§4,
  mixed-architecture, faq, agent-self-assessment, mental-models,
  formal-methods, applied-mappings, methods-catalog, toolbox.
- notes.md §46; sources.json; findings.md batch #29. No wrapper.

## 2026-09-18 20:34 UTC — Abide soft-rule preference lint

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`).
  Docs-only. Not a competing PR. Archer 27B drop still **WATCH**.
- HIGH: [`coldteadotai/abide`](https://github.com/coldteadotai/abide)
  (MIT, created 2026-09-18). Productized Jev preference lint for
  Claude Code / Codex / OpenCode. Soft AGENTS.md / CLAUDE.md rules →
  one Score per rule on the diff (never the conversation); hard rules
  stay with the linter (jevgate-family layering). Edit- vs turn-phase
  observation window; banded confidence + fail-open; rubric as
  artifact (calibrate/tune). Replay 93 sessions / 1,256 edits / 147
  turns; independent-reviewer precision edit ~26% / turn ~73%
  (author-reported, before tune). Fuller path of jev-pref;
  complementary to rh-guard. Text/diff only — not multimodal.
- Cards: mixed-architecture, question-design, validation, mappings
  §2 / §18, faq, agent-self-assessment, toolbox, methods-catalog,
  mental-models, formal-methods, composition-algebra, SKILL.md.
- notes.md §47; sources.json; findings.md batch #30. No wrapper.

## 2026-09-18 20:43 UTC — kev delta (Hub weights, NOTA training)

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`).
  Docs-only. Not a rewrite of §45. No species change.
- Hub: [`jaredpalmer/kev-0.5b`](https://huggingface.co/jaredpalmer/kev-0.5b)
  HTTP 200; `--run` accepts Hub ids; GitHub release tarball remains.
  PEFT `task_type=FEATURE_EXTRACTION`; publish patches null task_type.
  GitHub 61★ this pass.
- HIGH question-design: none-of-the-above must appear as a wrong
  alternative too, varied wording; dedicated `none_of_the_above` eval
  (no published rates). Cross-link wellposed / Choice `"other"`.
- Cards: question-design, faq, judgment-class, validation, ecosystem.
- notes.md §45 delta; sources.json; findings.md batch #31. No wrapper.

## 2026-09-18 20:52 UTC — extractive / local surface / speed layer (~14:52 Boise)

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`).
  Docs-only. Not a competing PR. Archer 27B drop still **WATCH**.
- HIGH: testimonial-miner (extractive + `redecide`); jev-reviewer
  (pointer-not-generator); jev-local (`/v1/systemone`; stub until hf);
  solari-reflex (observe→act, no screenshots; 60.2/194.9, 66/460,
  24.2/98.4 s); jevframe (pandas/Polars accessor; sibling of jevpandas).
- MED: jev-hermes (route ≠ memory); agent-workflow-typesafe-ai
  (advisory sidecar); dag-jev (structure induction, experiment);
  jev-agentworld-web-simulator; jev-testbench (collab arms);
  jevscan (AST ∩ semantic); pi-jev-approver (light); laya-onnx
  (do not copy vs-Jev table).
- Spotcheck: SemIf 1551★; jevlike 866★; tracker 20:12:57Z lists Laya,
  not Blackwood. Awesomejev 488/21644 not re-derived.
- Cards: SKILL.md, applied-mappings §2/§5, mappings §1/§4/§9/§18,
  mixed-architecture, mental-models, validation, faq, judgment-class,
  methods-catalog, toolbox, agent-self-assessment, question-design,
  ecosystem, CHANGELOG, README.
- notes.md §48; sources.json; findings.md batch #32. No wrapper.

## 2026-09-18 21:52 UTC — boundary map / Harbor bake-off / dual-process (~15:52 Boise)

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`).
  Docs-only. Not a competing PR. Archer 27B drop still **WATCH**.
  X MCP flap blocked discourse this hour — no tweets invented.
- HIGH: jev-capability-atlas (extractable-from-state axis; history
  suite A/B/C table; component node; dangerous-high ECE; DOM-as-text);
  DMB v2 (frozen protocol vs constrained LLMs; 76.3/93.0/256+;
  264–276 ms; $0.07/1k); jevals-data CC-BY-4.0 feedstock;
  dual-process-ai (S1 decide / S2 generate; routing accuracy
  unmeasured).
- MED: ARC-AGI Direct Jev 4/400; open-alternative-jev RACE-H 92.9%
  @ 4.55 q/s (not a reproduction); von 14 MB SAN (not a replica);
  kev 100★ light delta.
- Do not merge Banking77 87% / 76.3% / 79.67%. Do not copy vs-Jev
  tables or uv/von-serve how-tos.
- Cards: SKILL.md, mental-models (primary boundary map),
  judgment-class (vs constrained LLM; von; open-alternative-jev),
  validation (DMB + jevals-data + ARC), mixed-architecture
  (dual-process; component node; DOM-as-text), faq, mappings
  §2/§3/§6/§9, applied-mappings, question-design, methods-catalog,
  toolbox, agent-self-assessment, ecosystem, CHANGELOG, README.
- notes.md §49; sources.json; findings.md batch #33. No wrapper.

## 2026-09-18 22:22 UTC — GLiNER2.5 extractive compaction (~16:22 Boise)

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`).
  Docs-only. Not a competing PR. Archer 27B drop still **WATCH**.
  **Not Jev. Not multimodal.** No invented metrics.
- HIGH: [m-newhauser/gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction)
  (Apache-2.0, created 2026-09-18). GLiNER2.5
  `fastino/gliner2.5-base-v1` retention Choice + exact char-offset
  copies. Mutating tools / shell operators → `keep_full`. Fail-closed
  to `keep_full`. `shadowMode` default true. Same *job* as
  fast-jev-compaction / pi-jev-compaction; encoder backend.
  Fastino/GLiGuard sibling class. Pointer family with
  testimonial-miner / jev-reviewer.
- Limits (theirs): experimental; characters not tokens; conservative
  shell over-retains; completed pairs only. No published
  retention-quality rates.
- Cards: SKILL.md, judgment-class (primary), applied-mappings §1–§2,
  mappings §12/§18, mixed-architecture, faq, mental-models,
  methods-catalog, toolbox, agent-self-assessment, ecosystem,
  CHANGELOG, README.
- notes.md §50; sources.json; findings.md batch #34. No wrapper.

## 2026-09-18 22:48 UTC — CI merge-gate / fail-open wake / S1 indexer / claim-evidence (~16:48 Boise)

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`).
  Docs-only. Not a competing PR. Archer 27B drop still **WATCH**.
  No invented metrics. No wrapper.
- HIGH: [CaseReed/latch](https://github.com/CaseReed/latch) (MIT) —
  cluster in code, Jev labels, policy PASS/BLOCK; pair Harbor +
  rh-guard. [shitianfang/wakegate](https://github.com/shitianfang/wakegate)
  (MIT) — fail-open VOI wake; 21/21 smoke.
  [s1-graphify-indexer](https://github.com/GreyssonEnterprises/s1-graphify-indexer)
  (+ s1-indexer) — GLiNER extract + escalate-S2; 10–50× unfilled.
  [clear-head](https://github.com/VladyslavHontar/clear-head) (MIT,
  1★) — claims vs session evidence.
  [reification-labs/foreman](https://github.com/reification-labs/foreman)
  — description-only Phoenix scaffold.
  [jev-gateway-bench](https://github.com/vinilana/jev-gateway-bench)
  (MIT) — Harbor on/off one-run signal.
  [jev-marshal](https://github.com/LightningK0ala/jev-marshal) —
  empty / Watch. [jevons](https://github.com/LilDojd/jevons) (MIT)
  — bounded Pi supervisor, shadow recovery.
- MED: if-ai, omp-auto-mode, jev-downloads-sorter, jev-label-desk,
  herdr-jev, jev-gateway sibling.
- Cards: SKILL.md, applied-mappings §3, mappings §3/§6/§9/§18,
  mixed-architecture, validation, faq, judgment-class, mental-models,
  methods-catalog, toolbox, agent-self-assessment, composition-algebra,
  ecosystem, CHANGELOG, README.
- notes.md §51; sources.json; findings.md batch #35. No wrapper.

## 2026-09-18 22:56 UTC — GLiNER2 Ultrafast observe→score→act (~16:56 Boise)

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`).
  Docs-only. Not a competing PR. Archer 27B drop still **WATCH**.
  **Not Jev. Not GLiNER2.5. Not multimodal.** No invented metrics.
- HIGH: [sahibzada-allahyar/gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast)
  (MIT, created 2026-09-18). Local GLiNER2
  `fastino/gliner2-multi-v1` scores observed a11y/DOM controls.
  No screenshots; no generated selectors; code owns actuators.
  Hybrid local decide + remote Mercury 2.5 fill. `DONE` ≠ verified
  success. Same *job* as jev-ultrafast / solari-reflex; encoder
  backend. Fastino sibling class with gliner25-compaction (different
  hole, GLiNER2.5) and GLiGuard (safety schema). Contrast
  blackwood-rlcd screenshot→Choice; laya-mind2web is DOM-index Laya
  (same observed-candidate family).
- Demo (theirs, not re-run): Flights 12.20 s visible / 13.785 s loop /
  ~$0.0001 API. Not a bake-off. Do not merge with atlas 7.1 s.
- Cards: SKILL.md, judgment-class (primary), mixed-architecture
  (primary), applied-mappings §2, mappings §9/§12, faq,
  mental-models, validation, methods-catalog, toolbox,
  agent-self-assessment, composition-algebra, ecosystem, CHANGELOG,
  README.
- notes.md §52; sources.json; findings.md batch #36. No wrapper.

## 2026-09-18 23:15 UTC — jev-pruner evidence-preserving Bash stdout prune (~17:15 Boise)

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`).
  Docs-only. Not a competing PR. Archer 27B drop still **WATCH**.
  **Not a summarizer. Not session compaction. Not GLiNER.** No
  invented metrics. No wrapper.
- HIGH: [tamaratran/jev-pruner](https://github.com/tamaratran/jev-pruner)
  (MIT, created 2026-09-18). After Bash, Jev Noul-prunes stdout
  chunks before the main LLM sees them. Hard ≤10k / JSON-diff
  envelope then soft Noul. Fail-safe keep original. Full archive.
  Marketplace id still `fast-jev-output`. Codex opt-in wrapper.
  Same *family* as fast-jev-compaction / gliner25-compaction;
  different *job*. Manual sweep (theirs): needles 24/24; mean
  reduction 83% on trim scenarios. Harbor plugin-eval cannot reach
  Jev. Terminal-Bench paired pilot is integration, not a full bench.
- Cards: SKILL.md, applied-mappings §1 (primary), mixed-architecture,
  mappings §12/§18, faq, validation, judgment-class, mental-models,
  methods-catalog, toolbox, agent-self-assessment, composition-algebra,
  ecosystem, CHANGELOG, README.
- notes.md §53; sources.json; findings.md batch #37. No wrapper.

## 2026-09-18 23:21 UTC — Cua-S1 specialist form System One (~17:21 Boise)

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`).
  Docs-only. Not a competing PR. Archer 27B drop still **WATCH**.
  **Not TypeSafe Jev. Not GLiNER. Not a general CUA. Not multimodal
  pixels-in.** Source-only — no weights, no checkpoint scores. No
  invented metrics. No wrapper. No `uv` / MCP / Driver how-to.
- HIGH: [trycua/cua `libs/cua-s1`](https://github.com/trycua/cua/tree/main/libs/cua-s1)
  (parent MIT; ~23.3k★ this pass). Specialist computer-use research.
  Profile `cua-s1-form-v0`. Byte encoder + option-attention:
  fill/check/click/skip per observed element. Fill values selected
  from extracted `Label: value` pairs. Plan ≠ execute; dry-run
  default; fail-closed checkbox/fill. Parallel "System One" naming
  in CUA, not a TypeSafe contract. Same observe→score→act *job* as
  jev-ultrafast / gliner2-ultrafast / solari-reflex / laya-mind2web.
  Offline metric *names* only. Watch for `cua-s1-form-v0` artifact.
- Cards: SKILL.md, judgment-class (primary), mixed-architecture
  (primary), applied-mappings §2, mappings §9/§12, faq,
  mental-models, validation, methods-catalog, toolbox,
  agent-self-assessment, composition-algebra, ecosystem, CHANGELOG,
  README.
- notes.md §54; sources.json; findings.md batch #38. No wrapper.

## 2026-09-18 23:54 UTC — CUDA replica / decision-native RAG / verbatim recall / Ruby primitive / FHIR Harbor / AMBIGUOUS baselines (~17:48 Boise)

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`).
  Docs-only. Not a competing PR. Archer 27B drop still **WATCH**.
  X MCP namespace flap; `since_id` **not** advanced. Archive
  `/workspace/jev-archive/2026-09-18/234740` not present locally.
  No invented metrics. No wrapper. Do not re-fold §50–§54.
- HIGH: [Mintzs/jevify](https://github.com/Mintzs/jevify) CUDA/PyTorch
  Choice/Score/Noul *shape* on Qwen2.5-1.5B; uncalibrated likelihoods
  ≠ Noul; no LICENSE. [decision-native-rag-skills](https://github.com/emergency-lee/decision-native-rag-skills)
  retrieve-wide → decide → evidence set; no harness; no universal
  benchmark. [jev-carryforward](https://github.com/Dharundp6/jev-carryforward)
  verbatim ledger + scored recall; rules never judged; 9×3 hint.
  [hunch](https://github.com/carldaws/hunch) Ruby language primitive.
  [explore-typesafe-ai](https://github.com/si618/explore-typesafe-ai)
  synthetic FHIR Harbor-shaped; not clinically validated.
  [jev-baselines-eval](https://github.com/ickma2311/jev-baselines-eval)
  **both AMBIGUOUS**; cascade sign-flip; confidence=1.0 theater;
  encoder-with-labels; serving-path ≠ model-speed; errata ×3.
  Student-b light delta only (HF card unchanged).
- MED: toolgate, typesafe-screening-mcp, databricks-jev-pdf-lab
  (honest negative, no OSS license), yannip1234/codex-jev,
  kazuhideoki/jev-search (**not** superagents-lab web search).
- Cards: SKILL.md, judgment-class, applied-mappings §1/§4,
  mappings §3/§4/§6/§18, mixed-architecture, validation, faq,
  mental-models, methods-catalog, toolbox, agent-self-assessment,
  ecosystem, CHANGELOG, README.
- notes.md §55; sources.json; findings.md batch #39. No wrapper.

## 2026-09-19 00:38 UTC — classify-first MCP + living applied-mappings atlas (~18:38 Boise 2026-09-18)

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`).
  Docs-only. Not a competing PR. Archer 27B drop still **WATCH**.
  No invented metrics. No wrapper. Do not re-fold §50–§55.
- HIGH: [kbhuw/jev-sift](https://github.com/kbhuw/jev-sift)
  classify-first MCP/plugin; batch path/url/text → Jev; content
  without entering main agent context first; 50 / 60k / 2MB /
  public-IP envelope; mocks ≠ accuracy; no LICENSE. Same family as
  decision-native-rag-skills. Topology A MCP, not jev-routing.
  [jevable.com](https://jevable.com/) living applied-mappings atlas:
  claimed 342 vs JSON-LD first page 36; class patterns (intent
  columns, score-among-observed, VOI gates, generative UI decide,
  robotics text-state, draft-gate silence ≠ safer). Not a hit list.
  Maker clocks stay claims unless already a named receipt.
- Cards: SKILL.md, applied-mappings §1/§2/§4, mappings §1/§4/§6/§9,
  mixed-architecture (topology A; prefilter polarity; gallery),
  faq, mental-models, methods-catalog, toolbox,
  agent-self-assessment, question-design, ecosystem, CHANGELOG,
  README.
- notes.md §56; sources.json; findings.md batch #40. No wrapper.

## 2026-09-19 00:48 UTC — Stagehand experimental Jev pick-and-copy (~18:48 Boise 2026-09-18)

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`).
  Docs-only. Not a competing PR. Archer 27B drop still **WATCH**.
  No invented metrics. No wrapper. Do not re-fold §50–§56.
- HIGH: [browserbase/stagehand #2955](https://github.com/browserbase/stagehand/pull/2955)
  (5/5 of #2951–#2955, all OPEN draft). Extract completion judge +
  pick-and-copy. Jev picks; code copies. extract off|judge|pick.
  Their card (gemini-3.8-flash, 25×3): 37/75 no-LLM ~0.5 s vs
  baseline 4.37 s; 69/75 vs 23/25 (92% both); LLM-off 36/75 — pick
  is a fast path, not a replacement. Same observe→score-among-
  candidates→code-acts job as jev-ultrafast / gliner2-ultrafast /
  cua-s1 / solari, inside a major harness. Screenshot extract
  always LLM. Cache-check errors never block replay.
- Cards: SKILL.md, applied-mappings §2, mappings §9/§12/§18,
  mixed-architecture, judgment-class, faq, mental-models,
  validation, methods-catalog, toolbox, agent-self-assessment,
  question-design, ecosystem, CHANGELOG, README.
- notes.md §57; sources.json; findings.md batch #41. No wrapper.

## 2026-09-19 00:46 UTC — public wall, meaning-search, attention≠correctness, skills→oxlint, session-sticky route, measured RAG rerank (~18:46 Boise 2026-09-18)

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`).
  Docs-only. Not a competing PR. Archer 27B drop still **WATCH**.
  No invented metrics. No wrapper. Do not re-fold §50–§57.
- HIGH: [waynesutton/ask-jev-ai](https://github.com/waynesutton/ask-jev-ai)
  public judgment wall; 6 parallel questions; policy-in-code;
  cost-to-1M from tokens; license null.
  [Bentlybro/jevgrep](https://github.com/Bentlybro/jevgrep) meaning-
  search without embeddings; 79% top-5 vs BM25 40% / grep 20% on
  stripped repos; keyword still wins exact strings.
  [egma-ai/jev-reviewer](https://github.com/egma-ai/jev-reviewer)
  attention P0/P1/P2 ≠ correctness; **not** choxos.
  [cephalization/jev-oxlint](https://github.com/cephalization/jev-oxlint)
  skills→oxlint AST∩remainder; Phoenix fixtures; not a hard gate.
  [jxu-dev-c/jev-adaptive-thinking](https://github.com/jxu-dev-c/jev-adaptive-thinking)
  session-sticky first-prompt; fail-closed fallback.
  [Max-sm-yc/Jev-RAG](https://github.com/Max-sm-yc/Jev-RAG) one-run
  ≥70% cost / 72% latency vs Spark *rerank*; full-context Spark
  still faster.
- MED: safe-sh, jev-loan-triage, TurboGuo jev-fedspeech/jev-dating,
  jevbox. hermes/mcp packs not found this pass.
- Cards: SKILL.md, applied-mappings §4/§5, mappings §4/§18,
  mixed-architecture (fail table + gallery), validation, faq,
  mental-models, methods-catalog, toolbox, agent-self-assessment,
  formal-methods, ecosystem, CHANGELOG, README.
- notes.md §58; sources.json; findings.md batch #42. No wrapper.

## 2026-09-19 01:48 UTC — capability kernel, typed DSPy control plane, calibration arena, engine-owns-truth, human-confirmed kill (~19:48 Boise 2026-09-18)

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`).
  Docs-only. Not a competing PR. Archer 27B drop still **WATCH**.
  No invented metrics. No wrapper. Do not re-fold §50–§58.
  Skip jef-mcp (parody) and jevregist (account farming).
- HIGH: [somoore/interlock](https://github.com/somoore/interlock)
  capability kernel; secrets never in agent; Jev SENSOR;
  policy.py BLOCK/ASK/ALLOW; type-safe ≠ correct; distinct from
  toolgate.
  [manikanda-kumar/jev-dspy-control-plane](https://github.com/manikanda-kumar/jev-dspy-control-plane)
  typed control plane around DSPy; drafts AFTER route+action;
  offline heuristic ≠ quality.
  [meetr1912/jev-arena](https://github.com/meetr1912/jev-arena)
  native Brier 0.0059 / ECE 0.0620 on 145 noul *theirs*;
  overconfident in low bins; fan-out 2 requests. Siblings
  sonar / vickrey / bracket.
  [JoelLewis/game-coach](https://github.com/JoelLewis/game-coach)
  Wave 0 PRD; Stockfish truth / Jev judgment; GPL-3.0.
  [epiphany-dynamics/port-cleanup](https://github.com/epiphany-dynamics/port-cleanup)
  human-only kill; identity re-check; mapped explanations.
- MED: jev-pr-labeler, jevcumber, typedecide, jevon, dsh-jev,
  fast-jev-compaction-pi, jev-tetris-benchmark, modelsystem,
  opencode-system-one, browser-ai, semantic-bookmark.
  Star spike: SemIf 1491→1606 (this pass 1607); jevlike 851→896
  (this pass 897).
- Cards: SKILL.md, applied-mappings §2/§5/§7, mappings §8/§18,
  mixed-architecture (fail table + gallery), validation, faq,
  optimizer-integration, formal-methods, mental-models,
  methods-catalog, toolbox, agent-self-assessment, ecosystem,
  CHANGELOG, README.
- notes.md §59; sources.json; findings.md batch #43. No wrapper.

## 2026-09-19 02:43 UTC — domain specialist vs few-shot hosted, decide→policy leftover cascade, ORDER BY calibration≠sortable, GLiFormer wire-compat backend (~20:43 Boise 2026-09-18)

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`).
  Docs-only. Not a competing PR. Archer 27B drop still **WATCH**.
  No invented metrics. No wrapper. Do not re-fold §50–§59.
- HIGH: [help-er/Domain-jev-maker](https://github.com/help-er/Domain-jev-maker)
  independent CLINC gold; KL 0.168 vs 0.580; train when
  downstream reads p.
  [skiingfalcon/jav-email-cascade](https://github.com/skiingfalcon/jav-email-cascade)
  decide→policy→LLM leftover; Noul 0.5 never rounded; license
  null; mock gen-json is *their mock*.
  [yodablocks/jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)
  six gates; Score 0.143 weak link; 53-way 0.99 tie;
  calibration ≠ sortable.
  [logan-markewich/jeff](https://github.com/logan-markewich/jeff)
  GLiFormer `/v1/systemone`; ~6× L4 HTTP / ~24× A10G direct;
  AG News 75.5% vs 90.5%; license null; not a Jev replica.
- MED: [hraness/sysone](https://github.com/hraness/sysone)
  loopback gateway; no weights.
- Cards: SKILL.md, applied-mappings §8, mappings §2/§4,
  mixed-architecture (fail table + gallery), validation, faq,
  judgment-class, mental-models, methods-catalog, toolbox,
  agent-self-assessment, optimizer-integration, ecosystem,
  CHANGELOG, README.
- notes.md §60; sources.json; findings.md batch #44. No wrapper.

## 2026-09-19 03:39 UTC — active-learning triage / don't distill Jev as teacher, evidence-packet explorer, meaning-grep, closed-vote CU, Jev vs MLX PCD Harbor, host-owned waymode, OMP/pi fail-open gates (~21:39 Boise 2026-09-18)

- Folded into open PR #2 (`cursor/augustus-store-envelope-00b4`).
  Docs-only. Not a competing PR. Archer 27B drop still **WATCH**.
  No invented metrics. No wrapper. Do not re-fold §50–§60.
- HIGH: [ThyFriendlyFox/jev-triage](https://github.com/ThyFriendlyFox/jev-triage)
  accept / teacher / human; do not distill Jev as teacher (~68%
  ceiling).
  [jimmyhealer/jev-semantic-explorer](https://github.com/jimmyhealer/jev-semantic-explorer)
  jevex; 1/8→6/8 n=8; packet HitFile diagnostic.
  [uehaj/jev-semgrep](https://github.com/uehaj/jev-semgrep)
  AND/OR/NOT line Nouls; JP↔EN; 0.94/0.98 *theirs*.
  [buluoray/JevOnly](https://github.com/buluoray/JevOnly)
  closed-vote; no planner LLM.
  [mallahyari/system-one-benchmark](https://github.com/mallahyari/system-one-benchmark)
  Jev 84.0% / Brier 0.1096 vs PCD 52% / 0.3884 n=50; license null.
  [mossburgh/waymode](https://github.com/mossburgh/waymode)
  host-owned handlers; 24/26 + 34/36 *theirs*.
  [luw2007/omp-jev-extensions](https://github.com/luw2007/omp-jev-extensions)
  fail-open acceptance + route.
- Skip empty: edwardyen724-g/jev-compactor, jlt-commons/laya-jolt.
- Cards: SKILL.md, applied-mappings §2/§4/§5/§9, mappings §2/§4/§6,
  mixed-architecture (fail table + gallery), validation, faq,
  judgment-class, mental-models, methods-catalog, toolbox,
  agent-self-assessment, optimizer-integration, ecosystem,
  CHANGELOG, README.
- notes.md §61; sources.json; findings.md batch #45. No wrapper.

## 2026-09-19 ~04:45 UTC — hourly ~22:38 Boise 2026-09-18 fold (§62)
- Docs-only into PR #2. Archer still Watch. Archive path
  `/workspace/jev-archive/2026-09-18/223856` absent; live GitHub
  READMEs + `gh api`.
- HIGH: [SemetricLabs/omp-greenlight](https://github.com/SemetricLabs/omp-greenlight)
  1,013/10; default 40.9% / 0 of 94; operator owns bar; not a sandbox.
  [adamjralph/skill-broker](https://github.com/adamjralph/skill-broker)
  outline; Jev never grants access; not a production recipe.
  [collapseindex/dinostomp](https://github.com/collapseindex/dinostomp)
  instrument-not-score; `dinostomp jev` ECE 0.062 *theirs* on 24;
  FINDINGS 189 / 99 against itself.
- MED: nrdz-labs/fast-jev-opencode, yikangy873-gif/jev-desktop,
  MrDiamondBallz/jev-agent-integration, bohutang/sift,
  CorieW/JevExplore.
- Census: Awesomejev 488/21644; SemIf 1641 (+13); jevlike 905 (+4);
  tracker likes 41 (+1); lastModified unchanged; Laya yes;
  Blackwood ABSENT; X MCP flapping (`pages_archived` 0).
- Cards: SKILL.md, applied-mappings §5/§7, mappings §7/§8/§18,
  mixed-architecture (fail table + gallery), validation, faq,
  mental-models, methods-catalog, toolbox, agent-self-assessment,
  formal-methods, ecosystem, CHANGELOG, README.
- notes.md §62; sources.json; findings.md batch #46. No wrapper.

## 2026-09-19 ~05:50 UTC — hourly ~23:40 Boise 2026-09-18 fold (§63)
- Docs-only into PR #2. Archer still Watch. Archive path
  `/workspace/jev-archive/2026-09-18/234027` absent; live GitHub
  READMEs + `gh api` + HF card. Hunches labeled.
- HIGH: [zeeshan8281/slo-router](https://github.com/zeeshan8281/slo-router)
  constrained optimizer + S1 features; same routes; p95 77.93→490.38 ms;
  fail-open local; eight-row demo not a benchmark.
  [godspede/construct-auto-classifier](https://github.com/godspede/construct-auto-classifier)
  privilege ≠ verdict; Jev 0 dangerous / 975; chat leaked; fail-closed.
  [rashedInt32/jev-lens](https://github.com/rashedInt32/jev-lens) +
  [jev-lens.nvim](https://github.com/rashedInt32/jev-lens.nvim)
  attention filter / VOI; never blocks; never green unless sure.
- MED: sysone-help/sysone (not hraness/sysone), INSTRUCT_JEV 119-row
  seed, swift-jev LICENSE-only.
- Census: Awesomejev 488/21644; SemIf 1652 (+11); tracker likes 42
  (+1); lastModified unchanged; Laya yes; Blackwood ABSENT; X MCP
  flapping.
- Cards: SKILL.md, applied-mappings §5/§7, mappings §6/§7/§8/§15/§18,
  mixed-architecture (fail table + gallery), validation, faq,
  mental-models, methods-catalog, toolbox, agent-self-assessment,
  formal-methods, judgment-class, ecosystem, CHANGELOG, README.
- notes.md §63; sources.json (352 sources, 349 unique URLs,
  retrieved 2026-09-19T05:50Z); findings.md batch #47. No wrapper.

## 2026-09-19 ~06:45 UTC — hourly ~00:39 Boise 2026-09-19 fold (§64)
- Docs-only into PR #2. Archer still Watch. Archive path
  `/workspace/jev-archive/2026-09-19/0039` absent; live GitHub
  READMEs + `gh api`. Hunches labeled.
- HIGH: [dtduc-git/jev-packs](https://github.com/dtduc-git/jev-packs)
  evidence-gated packs; nine verified *theirs*; jevassert 404 /
  unreleased; measurement owns endorsement.
  [omkarghugarkar007/actiongate-jev](https://github.com/omkarghugarkar007/actiongate-jev)
  Jev supplies evidence, code owns authority; positive p never
  overrides a hard fail.
  [Adilmp/does-jev-confidence-mean-anything](https://github.com/Adilmp/does-jev-confidence-mean-anything)
  + [jevcal](https://github.com/Adilmp/jevcal) ranking ≠
  calibration; 8,000 judgments; AUC ~0.91; stated ~75% vs
  human ~10%; ~96% ECE removed.
- MED: gqgs/laya-onnx (complete Laya browser int8; distinct
  from Mattepiu), kunchenguid/local-jev (not equivalence).
  Do not re-fold sysone-help/sysone.
- Census: Awesomejev 488/21644; SemIf 1660 (+8); jevlike 910
  (+5); TypeAR 9; tracker likes 42; lastModified unchanged;
  Laya yes; Blackwood ABSENT; X MCP flapping.
- Cards: SKILL.md, applied-mappings §7, mappings §7/§8,
  mixed-architecture (fail table + gallery), validation, faq,
  mental-models, methods-catalog, toolbox, agent-self-assessment,
  formal-methods, judgment-class, ecosystem, CHANGELOG, README.
- notes.md §64; sources.json (358 sources, 355 unique URLs,
  retrieved 2026-09-19T06:45Z); findings.md batch #48. No wrapper.

## 2026-09-19 ~06:55 UTC — hourly ~00:39 Boise remainder fold (§65)
- Docs-only into PR #2. Same hour as §64. Archer still Watch.
  Live GitHub READMEs + `gh api`. Hunches labeled.
- HIGH: [jiangkoumo/ego-jev](https://github.com/jiangkoumo/ego-jev)
  hot-click CU; indexed table; ~2× n=3 medians, not a bench.
  [edwardyen724-g/jev-compactor](https://github.com/edwardyen724-g/jev-compactor)
  was empty skip §61; Jev judges relevance, code decides
  structure; 64.5%/366ms/0 invented paths one session.
  [zhuyansen/x-reply-filter](https://github.com/zhuyansen/x-reply-filter)
  local rules first; never auto-train on own hides.
- Skip re-fold: actiongate, jev-packs, sysone-help. fast-jev-opencode
  already §62 MED.
- Census: as §64 (SemIf 1660 / jevlike 910 / Awesomejev 488/21644).
- Cards: SKILL.md, applied-mappings §1/§2/§4/§9, mappings §18,
  mixed-architecture, validation, faq, mental-models,
  methods-catalog, toolbox, agent-self-assessment, formal-methods,
  ecosystem, CHANGELOG, README.
- notes.md §65; sources.json (361 sources, 358 unique URLs,
  retrieved 2026-09-19T06:55Z); findings.md batch #49. No wrapper.

## 2026-09-19 ~07:55 UTC — hourly ~01:47 Boise fold (§66)
- Docs-only into PR #2. Archer still Watch. Live GitHub
  READMEs + `gh api`. Hunches labeled.
- HIGH: decision-combinators (control-plane Then/Gate/Vote/
  Cascade/Weighted); jev-capability-atlas 10★ receipts-not-
  leaderboard (axis already §49); skillranker 52★ VOI /
  hook fail-open (corrects §7); jev-ood-calibration 900
  tickets ECE 0.107 = 4.4× floor, sign flips by type;
  jev-frontier-100 Jev 77.0% vs 4B/2048 96.7% (exploratory);
  turnstile evidence≠authority + replay; jevmlx 28★ one-pass
  softmax ≠ Noul.
- MED: invalidate, jev-intent-review (under construction),
  prune-review (cost outlier).
- Census: not re-derived (last SemIf 1660 / jevlike 910 /
  Awesomejev 488/21644).
- Cards: SKILL.md, applied-mappings §5/§7, mappings §3/§6/§7/§8,
  mixed-architecture, validation, faq, judgment-class,
  mental-models, methods-catalog, toolbox, composition-algebra,
  agent-self-assessment, formal-methods, ecosystem, CHANGELOG,
  README.
- notes.md §66; sources.json (370 sources, 367 unique URLs,
  retrieved 2026-09-19T07:55Z); findings.md batch #50. No wrapper.

## 2026-09-19 ~08:50 UTC — hourly ~02:38 Boise fold (§67)
- Docs-only into PR #2. Archer still Watch. Live GitHub
  READMEs + `gh api`. Hunches labeled. Do not re-fold §66
  HIGH except sibling contrast.
- HIGH: jev-labs (TLA+ compose; never confidently wrong;
  1,080 golden 0 wrong *theirs*); seal (no seal, no
  advance; coverage ledger; mint ≠ product brain);
  skill-broker sibling delta (outline already §62);
  how-sure-is-jev (Choice confidence = max_prob);
  jevbench v1.1 (Main Score; calibration not scored);
  ci-gatekeeper-bot-jev (pre-review typed gate);
  jev-in-codex (Codex MCP; ranking unbenchmarked).
- Census this hour: SemIf 1683 (+11); jevlike 923 (+5);
  tracker likes 43 (+1); Awesomejev 488/21644 unchanged.
- Cards: SKILL.md, applied-mappings §3/§5/§7, mappings
  §3/§7/§8, mixed-architecture, validation, faq,
  mental-models, methods-catalog, toolbox, composition-algebra,
  agent-self-assessment, formal-methods, ecosystem, CHANGELOG,
  README.
- notes.md §67; sources.json (377 sources, 374 unique URLs,
  retrieved 2026-09-19T08:50Z); findings.md batch #51. No wrapper.

## 2026-09-19 ~09:55 UTC — hourly ~03:38 Boise fold (§68)
- Docs-only into PR #2. Archer still Watch. Live GitHub
  READMEs + `gh api`. Hunches labeled. Do not re-fold §67
  HIGH except sibling contrast.
- HIGH: jev-preflight (Stop-hook attention redirect;
  fail-open; eight axes; uncalibrated 0.85; 2.1.267 one
  continuation); construct delta (landed-script;
  headless≠auto-approve; 0/975 stands); jev-compactor
  product-arm 73%/350ms/4 of 4 (64.5% is vs-Sonnet);
  dizk/jev-lens (79%/500 trajectories; +17% post-send;
  distinct from rashedInt32); carryforward 0/4 tools≠use;
  pi-observational-memory-jev (keep/kind verbatim);
  openvons (independent open-Jev class; JevPick 3.2–4.8×;
  wire-compat ≠ replica); HA-Jev 17★ (not for locks);
  jevql outside-the-store; sift ~$0.00003/post short
  bullet.
- Census this hour: Awesomejev 488→561 (+73, agent
  tooling 87→107); SemIf 1683→1704. Archer still NOT
  landed.
- Cards: SKILL.md, applied-mappings §1/§3/§4/§7, mappings
  §4/§6/§7/§8, mixed-architecture, validation, faq,
  judgment-class, mental-models, methods-catalog, toolbox,
  agent-self-assessment, ecosystem, CHANGELOG, README.
- notes.md §68; sources.json (382 sources, 379 unique URLs,
  retrieved 2026-09-19T09:55Z); findings.md batch #52. No wrapper.

## 2026-09-19 ~10:55 UTC — hourly ~04:39 Boise fold (§69)
- Docs-only into PR #2. Archer still Watch. Live GitHub
  READMEs + `gh api` + Hugging Face. Hunches labeled. Do
  not re-fold §68 HIGH except sibling contrast /
  combinators rename.
- HIGH: jev-combinators (rename + Router/Loop/Retry/
  Fallback/Memory; digital-design metaphor ≠ literal
  AND/OR); jevcache (0 FP/100; fail-open); pi-jev-skill-bench
  + suggestion (roster 50–500; 43 gold; no live numbers);
  jev-zeroshot-vs-bert (+0.05–+0.13 / DiD *theirs*);
  jev-handoff (typed baton; gate never grants); ThinkyMiner/
  Winnow (80%/90%; ≠ kevinpita/winnow); hermes-jev-router
  (WHETHER/HOW/WHAT; license null); jev-typed-evaluation-
  collapse (conflict ≠ ignorance); browser-jev (sample-from-
  distribution); IamBusy/OpenJev 45/60 `/v1/decide` ≠ drop-in;
  semif-serve 1164 vs 178 ms; toolbelt notes (rh-guard owns
  reward-hack); DGUI_HYPERMEM-JEV 6-row flywheel.
- Census this hour: Awesomejev flat 561/27007; tracker likes
  43→45; SemIf 1714 (+10); jevlike 926 (+3). Archer still
  NOT landed.
- Cards: SKILL.md, applied-mappings §1/§2/§4/§5/§7/§9,
  mappings §3/§6/§7, mixed-architecture, validation, faq,
  judgment-class, mental-models, methods-catalog, toolbox,
  composition-algebra, agent-self-assessment, question-design,
  ecosystem, CHANGELOG, README.
- notes.md §69; sources.json (399 sources, 396 unique URLs,
  retrieved 2026-09-19T10:55Z); findings.md batch #53. No
  wrapper.

## 2026-09-19 ~11:55 UTC — hourly ~05:46 Boise fold (§70)
- Docs-only into PR #2. Archer still Watch. Live GitHub
  READMEs + `gh api`. Hunches labeled. Do not re-fold
  §50–§69 HIGH except sibling contrast / jevassert landing /
  prune-review, intent-review, laya-jolt, local-jev deltas.
- HIGH: jevassert LANDED (record/replay CI Apache-2.0;
  accuracy/ECE/Brier/cost/latency; exit 0/1/2; McNemar);
  jev-packs pairing + 2,990-case matrix (Jev/Sonnet 5
  accuracy tie, Jev better calibrated 7/9, ~250× cheaper;
  sms-spam 0.953/0.040); jevarena ≠ jev-arena
  (failure-finding, not findings); jev-bbq-experiment
  97.28%/0.04/0.34/$0.3429 *theirs* (not a bias cert);
  jeffrey (decider≠executor; pick ≠ fill); mizchi/jevlint
  13/15 1.00/1.00 *theirs* (≠ huntedman/JevLint);
  prune-review VOI hunk (1.18% with 305% outlier);
  jev-intent-review VERIFIED/VIOLATION/UNKNOWN; Eran-BA
  GLiNER2 spec-only ≠ jeff; grande JGLUE 0.614/0.853 +
  270M 0.710/0.710 *theirs* (license null); laya-jolt
  byte parity; leesk212/JEV-CPU PoC (Meanblock 404);
  local-jev done 30%/shape 57%; pi-heed 98.5%/0 false
  block. MED: lustig size-0 framing stub. Toolbelt:
  actiongate slogan already §64.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, applied-mappings §3/§7/§9, mappings
  §6/§7/§8/§9, mixed-architecture, validation, faq,
  judgment-class, mental-models, methods-catalog, toolbox,
  composition-algebra, agent-self-assessment,
  question-design, ecosystem, CHANGELOG, README.
- notes.md §70; sources.json (411 sources, 408 unique URLs,
  retrieved 2026-09-19T11:55Z); findings.md batch #54. No
  wrapper.

## 2026-09-19 ~12:50 UTC — hourly ~06:43 Boise (SGR-judge contract, control planes, never-generates, recipes+feed, NAR claim-audit)
- Docs-only fold into PR #2. `notes.md` §71. Archer still
  Watch. Do not re-fold §50–§70 HIGH except sibling
  contrast. Hunches labeled. No wrapper. No invented
  metrics.
- Live receipts: GitHub READMEs + `gh api` ~12:50 UTC.
  IPECTER/jev-context-pruner **409 empty**.
- Folded: jev-judge-bench SLA-150 (21 offline tests;
  canaries ≠ quality; no headline yet; ≠ jevarena/jevbench);
  jev-use 220 ms p50 / 12/12 / Vercel 0.4 *theirs*
  (≠ jev-ultrafast); pi-jev-control license null (GUI never
  force-click); jev-gpt ~400 calls / 75 s / 2¢; jev-cookbook
  425/$0.015 samples not benches; jevfeed no social graph;
  openJev-verdict-2.0 77.10%/0.0636/0.0144 *theirs*
  unverified + PR #1 (throughput≠latency; Laya parity;
  like-for-like ECE; ≠ IamBusy/OpenJev).
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, applied-mappings §1/§4/§5/§7/§9,
  mappings §6/§7/§8/§9, mixed-architecture, validation,
  faq, judgment-class, mental-models, methods-catalog,
  toolbox, composition-algebra, agent-self-assessment,
  question-design, ecosystem, CHANGELOG, README.
- notes.md §71; sources.json (421 sources, 418 unique URLs,
  retrieved 2026-09-19T12:50Z); findings.md batch #55.
  No wrapper.

## 2026-09-19 ~13:52 UTC — hourly ~07:49 Boise (1-token logprob ≠ Noul, replica engine, Elixir SDK, commit/jevex VOI, inbox, laya-multilingual)
- Docs-only fold into PR #2. `notes.md` §72. Archer still
  Watch. Do not re-fold §50–§71 HIGH except sibling
  contrast. Hunches labeled. No wrapper. No invented
  metrics. Local archive
  `/workspace/jev-archive/2026-09-19/0747/` missing.
- Live receipts: GitHub READMEs + trees + HF cards
  ~13:52–13:55 UTC. IPECTER/jev-runway **LICENSE-only**.
  GitHub `size: 0` lag on several full trees.
- Folded: chakuho GUI 336 27B 95%/92% vs Jev 89%/82%
  *theirs* (coverage ≠ correctness); jevinf 2.57×/2.27×
  100% argmax; typesafe-elixir-sdk ≠ dannote/jev; jevex
  n=16 160s→69s; commitjev middle band; hermes-plugin-jev
  is Agnes; pi-jev-compact ≠ pi-jev-compaction;
  mailordinal inbox; jev-samples toolbelt; jev-cli not
  ready ≠ jevql; laya-multilingual MASSIVE 0.366/0.387
  (Khmer 0.000@0.952); schema-scorer Hub v2 0.841
  (GitHub 404). Skip: jev-routing Cursor/Devin delta;
  HF 401 open-jev-laya-bench / jev-tree-choice-cap /
  INSTRUCT_JEV; jevlogs 404+401.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, applied-mappings §1/§3/§4/§5/§7/§8,
  mappings §6/§7/§8/§9, mixed-architecture, validation,
  faq, judgment-class, mental-models, methods-catalog,
  toolbox, composition-algebra, agent-self-assessment,
  question-design, ecosystem, CHANGELOG, README.
- notes.md §72; sources.json (435 sources, 432 unique URLs,
  retrieved 2026-09-19T13:52Z); findings.md batch #56.
  No wrapper.

## 2026-09-19 ~14:37 UTC — user-provided classifier.dev (~08:37 Boise)
- Docs-only fold into PR #2. `notes.md` §73. Skip Archer.
  Hunches labeled. No wrapper. No invented metrics.
  Not a thin Jev skill. Life/business (spam/inbox/feedback).
- Receipts: user SIGNAL + live GitHub README `6ae8bda` /
  eval/README `2009d1f` ~14:37 UTC. MIT; **185★**.
- Folded: productized System One HTTP (label+calibrated p;
  batch `{id,text}[]` ~1000; Jev primary / LLM fallback);
  400 headlines 650 ms *theirs*; escalate-under-threshold
  (smart single-label <0.7; multi-label ignores);
  emotion ≥0.9→82% / <0.5→29%; gemini-3.8-flash
  87.5→90.0 / 61.8→63.7; F1 0.887 / 230 ms vs cascade
  0.799 / 1.5 s (eval 232 ms; AG News 87.7% vs 82.0%);
  vs_jev tracked JSON; read eval/README (n=7 train-on-test);
  silent FALLBACK granite 0.546 vs advertised ~0.800;
  rh-guard owns the gate. Distinct from ask-jev-ai.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, applied-mappings §4/§8, mappings
  §6/§7/§8, mixed-architecture, validation, faq,
  judgment-class, mental-models, methods-catalog,
  toolbox, composition-algebra, question-design,
  ecosystem, CHANGELOG, README.
- notes.md §73; sources.json (437 sources, 434 unique URLs,
  retrieved 2026-09-19T14:37Z); findings.md batch #57.
  No wrapper.
