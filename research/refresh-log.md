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

## 2026-09-19 ~14:48 UTC — user-provided choxos/jev-reviewer (~08:48 Boise)
- Docs-only **delta of §48** into PR #2. `notes.md` §74.
  Skip Archer. Hunches labeled. No wrapper. No invented
  metrics. Always **choxos/jev-reviewer** or
  “systematic-review Jev Reviewer.” **≠** egma-ai.
- Receipts: user SIGNAL + live README `d0220a1` ~14:48
  UTC. MIT; **12★**; https://jevreviewer.xera.ac.
- Folded: pointer-not-generator at evidence-synthesis
  scale; two-pass Choice+Noul (quotes ≥ 0.5 *theirs*);
  *Not found* / *Unclear*; speculative fan-out; 18-q
  **4.6 s / $0.0101** *theirs* (spot check); human tick
  never overwritten; Cochrane/PRISMA/RoB, not SWE-only.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, applied-mappings §2, mixed-architecture,
  faq, mental-models, methods-catalog, toolbox, validation,
  composition-algebra, question-design, agent-self-assessment,
  ecosystem, CHANGELOG, README.
-   notes.md §74; sources.json (438 sources, 435 unique URLs,
  retrieved 2026-09-19T14:48Z); findings.md batch #58.
  No wrapper.

## 2026-09-19 ~14:56 UTC — user-provided githubnext/localjev (~08:56 Boise)
- Docs-only into PR #2. `notes.md` §75. Skip Archer.
  Hunches labeled. No wrapper. No invented metrics.
  Always **githubnext/localjev**. **≠** kunchenguid/local-jev.
- Receipts: user SIGNAL + live README `39939e6` / eval
  `418cae7` ~14:56 UTC. MIT; **261★**; GitHub Next.
- Folded: wire-compat ≠ logit-equiv (prompted JSON +
  entropy confidence vs razorback16 structured-read);
  TypeSafe SDK drop-in; 1,200-req bake-off *theirs*
  (Qwen3.6 76.7% / Gemma 26B 75.0% / DiffusionGemma
  74.2% short; no winner; not calibrated); LM Studio
  runner gap; institutional interchange.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, judgment-class, mixed-architecture,
  faq, mental-models, validation, methods-catalog,
  toolbox, composition-algebra, question-design,
  mappings §7, ecosystem, CHANGELOG, README.
- notes.md §75; sources.json (440 sources, 437 unique URLs,
  retrieved 2026-09-19T14:56Z); findings.md batch #59.
  No wrapper.
## 2026-09-19 ~15:07 UTC — user-provided NandhaKishorM/laya (~09:07 Boise)
- Docs-only into PR #2. `notes.md` §76. Skip Archer.
  Hunches labeled. No wrapper. No invented metrics.
  Always **NandhaKishorM/laya**. Packaging of Hub Laya,
  not a new species. **≠** TypeSafe `/v1/systemone`.
  **≠** githubnext/localjev.
- Receipts: user SIGNAL + live README `f12882b` ~15:07
  UTC. Apache-2.0; **710★** (user 687; hourly 691);
  62 forks; 7 issues; Python.
- Folded: Router script-before-p (Khmer 0.000@0.952);
  where Jev leads (Banking77 0.425 vs 0.870; soft-acc
  0.471 vs 0.580; raw ECE 0.213 vs 0.144); where Laya
  leads (T4 32.8 ms; post-T ECE 0.081 vs 0.246);
  0.766 is fine-tune not zero-shot; 0.85 still soft;
  vs-Jev unpublished-here. Do not copy pip / preload.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, judgment-class, mixed-architecture,
  faq, mental-models, validation, methods-catalog,
  toolbox, composition-algebra, question-design,
  mappings §7, applied-mappings §4/§8, ecosystem,
  CHANGELOG, README.
- notes.md §76; sources.json (443 sources, 440 unique URLs,
  retrieved 2026-09-19T15:07Z); findings.md batch #60.
  No wrapper.
## 2026-09-19 ~15:14 UTC — user-provided @airesearch12 census (~09:14 Boise)
- Docs-only into PR #2. `notes.md` §77. Skip Archer.
  Hunches labeled. No wrapper. No invented metrics.
  Quote tweet; mark likes ephemeral. **≠** jevbench
  v1.1. Do not paste live board ranks. Do not copy
  Stripe.
- Receipts: user SIGNAL_4b0c (~08:41 Boise) + live X
  MCP get_posts_by_id this pass (564 impressions / 15
  likes / 5 replies / 1 quote / 11 bookmarks — ephemeral).
- Folded: external census ≠ scored bake-off; GLiNER2 +
  routers class-boundary; incomplete vs Laya / localjev /
  kev / TypeAR / openvons; Harbor honesty watch
  (calibration, cost, latency, silent fallback).
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, judgment-class, mixed-architecture,
  faq, mental-models, validation, methods-catalog,
  toolbox, composition-algebra, question-design,
  mappings §7, ecosystem, CHANGELOG, README.
- notes.md §77; sources.json (447 sources, 444 unique URLs,
  retrieved 2026-09-19T15:14Z); findings.md batch #61.
  No wrapper.
## 2026-09-19 ~15:24 UTC — user-provided JevBench v1.2 board (~09:24 Boise)
- Docs-only into PR #2. `notes.md` §78. Skip Archer.
  Hunches labeled. No wrapper. No invented metrics.
  Quote board *theirs*. **≠** tweet census §77 **≠**
  jevbench v1.1 87.6. Do not copy Stripe / CLI.
- Receipts: user SIGNAL_988e (~08:44 Boise) + live
  board fetch this pass + GitHub README SHA `bf1e79ba`
  + RESULTS-v1.2.md SHA `fdfab1a2` + HEAD `27ed3d6c`
  (pushed 2026-09-19T13:27:30Z; MIT; 0★).
- Folded: geo-mean I/C/S/K product; cal ON rank;
  weight sensitivity; option-order 72→21; instruction
  models class-boundary; ×2/est. Harbor honesty; Laya
  absent as gap; GLiNER2 mapping exclusion; Qwen3.8
  27B ≠ Archer.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, judgment-class, mixed-architecture,
  faq, mental-models, validation, methods-catalog,
  toolbox, composition-algebra, question-design,
  mappings §7/§17, ecosystem, CHANGELOG, README.
- notes.md §78; sources.json (449 sources, 446 unique URLs,
  retrieved 2026-09-19T15:24Z); findings.md batch #62.
  No wrapper.
## 2026-09-19 ~15:37 UTC — hourly 0842 already-folded watch (~08:42 Boise)
- Docs-only into PR #2. `notes.md` §79. Skip Archer.
  Hunches labeled. No wrapper. No invented metrics.
  Named HIGHs already §73–§78 — apply, don’t re-card.
  Skip thin noise. Do not copy action.yml / bun / pip.
- Receipts: user SIGNAL 0842 + live GitHub search this
  pass (~15:37 UTC) for leftover thin (0–1★).
- Folded: wire-compat ≠ logit-equiv; product+FALLBACK;
  packaging honesty / script-before-p; pointer-not-
  generator; census ≠ scored bake-off / geo-mean VOI.
  Skip jev-semgrep (already §61). Soundness-theater
  skip for totally-tim/jev-gate (0★) and
  claude-jev-warden (1★). Qwen3.8 27B ≠ Archer.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, mixed-architecture, faq,
  mental-models, validation, toolbox,
  composition-algebra item 19, question-design,
  ecosystem, CHANGELOG, README.
- notes.md §79; sources.json (455 sources, 452 unique URLs,
  retrieved 2026-09-19T15:37Z); findings.md batch #63.
  No wrapper.
## 2026-09-19 ~15:50 UTC — user-provided khordoo/jev-reflex-autonomy-lab delta (~09:50 Boise)
- Docs-only into PR #2. `notes.md` §80. Skip Archer.
  Hunches labeled. No wrapper. No invented metrics.
  Quote README. Delta of §46, not a new species.
  Do not copy npm / `.dev.vars` / keys.
- Receipts: user SIGNAL_2f18 (~08:48 Boise; ★6) +
  uploaded README_f001 + live GitHub this pass
  (**7★** / 1 fork; license null; README SHA
  `130987c9`; ARCHITECTURE SHA `48da0769`; HEAD
  `e3297ebe`; pushed 2026-09-19T15:11:21Z). Demo
  https://khordoo.github.io/jev-reflex-autonomy-lab/watch-demo.html.
- Folded: S1 never stalls / S2 one-use advisory;
  purple = consumed not arrived; Local controller ≠
  githubnext/localjev ≠ kunchenguid/local-jev; 20%
  starting gate still soft; seed = geometry ≠ async
  replay; no pixels; confidence ≠ selected
  probability; S2 never grants. README GLM 5.3 vs
  ARCHITECTURE muse-spark — quote both *theirs*.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, mixed-architecture, faq,
  mental-models, agent-self-assessment, validation,
  toolbox, composition-algebra item 20,
  question-design, mappings §6/§9, applied-mappings
  §9, judgment-class portent 5, methods-catalog,
  ecosystem, CHANGELOG, README.
- notes.md §80; sources.json (457 sources, 454 unique URLs,
  retrieved 2026-09-19T15:50Z); findings.md batch #64.
  No wrapper.
## 2026-09-19 ~16:05 UTC — user-provided typesafe-computer-use HIGH (~10:05 Boise)
- Docs-only into PR #2. `notes.md` §81. Skip Archer.
  Hunches labeled. No wrapper. No invented metrics.
  Quote README. Expand the census one-liner; do not
  re-card it. Do not copy `uv sync` / `.env` / keys /
  Screen Recording how-to.
- Receipts: user SIGNAL_0e9d (~08:49 Boise; MIT; ★419)
  + uploaded README_45d1 + live GitHub this pass
  (**427★** / 24 forks / 7 issues; README SHA
  `369f4a6a`; HEAD `cc7b5066`; pushed
  2026-09-18T23:33:50Z).
- Folded: productized OCR+AX observe→score→act
  (hosted Jev); exclusive action set; split
  kind/item/site/offscreen; perception rebuilds
  pixel-free reasoning; writer/decider + post-type
  Noul still soft; 155× *theirs* one screenshot ≠
  Harbor taskset; decision ≠ answer-reader capture;
  AX never sole; `done` ≠ success. **≠** jev-ultrafast
  **≠** cua-s1 **≠** jev-macos-loop **≠** camoufox.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, mixed-architecture, faq,
  mental-models, agent-self-assessment, validation,
  toolbox, composition-algebra item 21,
  question-design, mappings §6/§9, applied-mappings
  §2/§9, judgment-class portent 4, methods-catalog,
  ecosystem, CHANGELOG, README.
- notes.md §81; sources.json (457 sources, 454 unique URLs,
  retrieved 2026-09-19T16:05Z); findings.md batch #65.
  No wrapper.
## 2026-09-19 ~16:10 UTC — user-provided jev-voice-browser HIGH (~10:10 Boise)
- Docs-only into PR #2. `notes.md` §82. Skip Archer.
  Hunches labeled. No wrapper. No invented metrics.
  Quote README. Expand the §39 tweet; do not re-card
  it. Do not copy `npm` / `.env` / `run.sh` / keys.
- Receipts: user SIGNAL_89ca (~08:50 Boise; MIT;
  ★100) + uploaded README_0987 + live GitHub this
  pass (**103★** / 12 forks / 0 issues; README SHA
  `fa033303`; HEAD `054db0f3`; pushed
  2026-09-17T22:40:26Z).
- Folded: productized ASR observe→score→act
  (hosted Jev); partial-speech VOI (closed-set may
  fire; free-text waits); 9–11-question fan-out;
  pointer spans; spoken confirm ≠ auth; numbered
  overlay, no second model; 27/27 / ~300 ms /
  ~$0.0002 *theirs* fixtures ≠ Harbor; 0.5 / 0.55 /
  0.6 still soft. **≠** jev-voice-control **≠**
  nikolas-j **≠** Aj1905 **≠** typesafe-computer-use
  OCR. Compose with §81; never waveform-to-Jev.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, mixed-architecture, faq,
  mental-models, agent-self-assessment, validation,
  toolbox, composition-algebra item 22,
  question-design, mappings §6/§8/§9,
  applied-mappings §2/§7/§9, judgment-class
  portent 4, methods-catalog, ecosystem, CHANGELOG,
  README.
- notes.md §82; sources.json (458 sources, 455 unique URLs,
  retrieved 2026-09-19T16:10Z); findings.md batch #66.
  No wrapper.
## 2026-09-19 ~16:20 UTC — user-provided AgentGhost + JP genre atlas HIGH (~10:20 Boise)
- Docs-only into PR #2. `notes.md` §83–§84. Skip Archer.
  Hunches labeled. No wrapper. No invented metrics.
  Quote README and tweet. Dual-signal turn. Do not
  copy `npm` / `.env` / `AUTO_APPROVE`. Do not dump
  the 30 atlas repos.
- Receipts: user SIGNAL_7c0f (~08:50 Boise; MIT; ★2)
  + live GitHub this pass (**2★** / 0 forks / 0 issues;
  README SHA `44145fa9`; HEAD `ac04e4fb`; pushed
  2026-09-18T21:59:40Z). User SIGNAL_a92b (~08:50
  Boise; ~120k views) + live X this pass (131,234 /
  1,934 / 192; created 2026-09-18T21:45:48Z).
- Folded: wrap-as-execution ALLOW/ASK/DENY (wrap
  *is* the tool function; rules first; ASK throws;
  fail-closed; judge swappable). **≠** jwen5419807
  **≠** vventirozos **≠** actiongate **≠** toolgate
  **≠** jev-use. rh-guard owns the gate cousin.
  JP genre atlas (apps by hole; stars research-time
  203→427 / 40→103; not verified evals; OpenRouter
  Jev WATCH). **≠** class census §77 **≠** v1.2.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, mixed-architecture, faq,
  mental-models, agent-self-assessment, validation,
  toolbox, composition-algebra items 23–24,
  question-design, mappings §8/§18, applied-mappings
  §7, judgment-class, methods-catalog, ecosystem,
  CHANGELOG, README.
- notes.md §83–§84; sources.json (460 sources, 457 unique URLs,
  retrieved 2026-09-19T16:20Z); findings.md batch #67.
  No wrapper.
## 2026-09-19 ~16:25 UTC — user-provided Akshay pedagogy HIGH (~10:25 Boise)
- Docs-only into PR #2. `notes.md` §85. Skip Archer.
  Hunches labeled. No wrapper. No invented metrics.
  Quote ARTICLE.md. Do not copy Python samples. Do
  not paste 200×/400× as Harbor. Do not steal
  jev-semgrep / Flavio Copes.
- Receipts: user SIGNAL_55e5 (~08:51 Boise; ~183k
  views / 2095 likes / 220 RTs) + live X this pass
  (233,495 / 2,280 / 235 / 3,652; created
  2026-09-18T19:55:53Z; article
  https://x.com/i/article/2100940576741093376).
- Folded: LLM hammer; code owns branches; parallel
  questions; thresholds in code; schema-safe ≠
  correct; routing / tool-risk / verify with LLM;
  shadow-mode; questions-as-code. 200×/400× TypeSafe
  ceiling *theirs*. Text-only. **≠** official docs
  **≠** Flavio **≠** LangChain harness **≠**
  AgentGhost.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, mixed-architecture, faq,
  mental-models, agent-self-assessment, validation,
  toolbox, composition-algebra item 25,
  question-design, mappings §2/§18, methods-catalog,
  ecosystem, CHANGELOG, README.
- notes.md §85; sources.json (462 sources, 459 unique URLs,
  retrieved 2026-09-19T16:25Z); findings.md batch #68.
  No wrapper.

## 2026-09-19 ~16:30 UTC — user-provided jev-semgrep dedicated HIGH (~10:30 Boise)
- Docs-only into PR #2. `notes.md` §86. Skip Archer.
  Hunches labeled. No wrapper. No invented metrics.
  Quote README. Do not copy npm / `npx` / `.env` /
  marketplace. Do not dump CLI flags. Not a gate.
- Receipts: user SIGNAL_9afa (~08:54 Boise; ★42) +
  live GitHub this pass (**51★** ephemeral; 2 forks /
  0 issues; created 2026-09-19T03:18:28Z; pushed
  2026-09-19T14:51:00Z). HEAD `21120e9`; README SHA
  `923e6a5`. LICENSE MIT / GitHub NOASSERTION.
- Folded: proposition ≠ embedding; contrast-set
  refund; boolean AND/OR/NOT after threshold (do
  not multiply p); no-index economics; Semgrep.dev
  collision; not a gate. 0.94/0.98 *theirs* 10×51,
  not Harbor. **≠** jevgrep **≠** jev-combinators
  **≠** semgrep.dev.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, mixed-architecture, faq,
  mental-models, agent-self-assessment, applied-mappings
  §4, mappings §4, validation, toolbox,
  composition-algebra item 26, question-design,
  methods-catalog, ecosystem, CHANGELOG, README.
- notes.md §86; sources.json (464 sources, 461 unique URLs,
  retrieved 2026-09-19T16:30Z); findings.md batch #69.
  No wrapper.

## 2026-09-19 ~16:52 UTC — hourly 1047 HIGH + deferred 0945 (~10:47 Boise)
- Docs-only off main (PR #2 merged). `notes.md` §87.
  Skip Archer. Hunches labeled. No wrapper. No invented
  metrics. Quote READMEs / Hub cards. 0★ HIGHs still
  get real cards. Not a hit list.
- Folded how-to-apply clusters: decision-validated UI
  (gram-render never authors text; jev2ui leftover
  writer); decision-as-assert (jevtest ambiguous band;
  0.85 still soft); hybrid S1 (anima3 Qwen logprob;
  jeff confidently flat; do not invent Laya); pointer
  search (JevFind); Harbor trio (frontier-bench ≠
  frontier-100; GLiClass product bakeoff; four engines /
  majority floor / calibration ≠ discrimination);
  authorship named escape; non-SWE (ha-switchboard ≠
  HA-Jev; n8n Low Confidence); compaction-pi namesake
  lock (~50× *theirs*); jevloop full-distribution
  optimizer (mock default); deferred class (laya-vision
  SmolVLM `score` untrained; Cerebellum `/v1/decide` ≠
  TypeSafe — wire-compat vs agent-routing as separate
  Harbor axes, competing NAR not endorsement;
  laya-grounded not drop-in / Platt not temperature).
- Formal compose: Telegram/HA/test/verb-menu/n8n/compaction
  envelopes. Hard-gating a Noul as test/PR/HA/authorship
  is soundness theater.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 27–36, question-design,
  methods-catalog, formal-methods, agent-self-assessment,
  optimizer-integration, ecosystem, CHANGELOG, README.
- notes.md §87; sources.json (485 sources, 482 unique URLs,
  retrieved 2026-09-19T16:52Z); findings.md batch #70.
  No wrapper.

## 2026-09-19 ~17:25 UTC — queued user SIGNALs + remaining deferred 0945 HIGH (~11:25 Boise)
- Docs-only on PR #3. `notes.md` §88. Skip Archer.
  Hunches labeled. No wrapper. No invented metrics.
  Quote READMEs / Hub cards. Soft Noul ≠ hard safety.
- Folded how-to-apply clusters: open LoRA replica
  (GestaltLabs/Jeff-1 acc **0.8183** ECE **0.0807** vs
  Jev **0.8283** / **0.0932** n=9730 *theirs*; set reused;
  **≠** logan-markewich/jeff GLiFormer; Hub GestaltLabs ≠
  GitHub Gestalt-Lab); Jev-first bounded agent
  (stanley-code empty findings ≠ approval; human
  `--promote-candidate`; 0.6/0.55/0.15 still soft;
  0.1.0 not on npm); NL memory → beam-search FS
  (findme **≠** JevFind; license null); price workers
  not the conversation (jevsubrouter fail-open; counts
  ≠ dollars). laya-vision + Cerebellum already §87 —
  not re-carded. jevsubrouter is the remaining deferred
  0945 HIGH.
- Formal compose: gitignore/symlink listing; `test.skip`
  / deleted assertions; pinned Agent model + prompt-cache.
  Empty findings as approval / auto-promote / unmeasured $
  / Jeff-1 as logan jeff are soundness theater.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 37–40, question-design,
  methods-catalog, formal-methods, agent-self-assessment,
  ecosystem, CHANGELOG, README.
- notes.md §88; sources.json (490 sources, 487 unique URLs,
  retrieved 2026-09-19T17:25Z); findings.md batch #71.
  No wrapper.

## 2026-09-19 ~17:55 UTC — hourly 1144 HIGH (~11:49 Boise)
- Docs-only on PR #3. `notes.md` §89. Skip Archer.
  Do **not** re-fold 1047 / §87 / §88. Hunches labeled.
  No wrapper. No invented metrics. Quote READMEs.
  Soft Noul ≠ hard safety. 0★ HIGHs still get real
  cards. Not a Jev skill dump.
- Folded how-to-apply clusters: Typed if (feelings
  `.feels()` default 0.5 is Noul-0.5-never-rounded;
  exhaustive BAML `match`; **≠** hunch **≠** Probably);
  Shadow then honor (apa-agent-harness **≠**
  AntonioCoppe/jev-harness; unpublished npm; grok-bot-jev
  skill honor; A/B proxies ≠ tokens; 13.0× is a top-five
  cap; apa-persona-engine SM then leftover LLM);
  Human every action (Essentiel-Jev never authority;
  0.75 provisional);
  Atom then sense (enzo-mcp independently falsifiable
  claims; UNKNOWN useful; **≠** jev-sift);
  File by Choice (pigeonhole OTHER skip; 0.6 still
  soft; HF playground static no-network; **≠**
  classifier.dev; sibling jev-decisions pointer only);
  Question preflight (jev-reliability Nothing about
  accuracy; noul-gate 0.0%/12.5%/3.6% *theirs*;
  clduab11/jev-test bars ≠ scores; jev-rag-benchmark
  “Jev wins” is not an assumption; dairui1/jev-lab
  91% vs 79% *theirs* synthetic; **≠** BrendanH18;
  do not re-card jev-desktop);
  Inbox read-only vs write (jevmail `gmail.readonly`
  ~3¢/1k *theirs*; mailjay archive/trash after review;
  **≠** mailordinal).
- Formal compose: BAML exhaustive `match`; kill switch
  + skill honor; human approve + read-back;
  deterministic evidence + `allow_external_jev`;
  `OTHER` skip; static no-network; `gmail.readonly`;
  Trash not delete. Soft Noul ≠ hard safety:
  `.feels()` 0.5, apa 0.85, Essentiel 0.75, pigeonhole
  0.6, jev-lab 0.65/0.70. Hard-gating a default 0.5
  bool / quoting “mathematically fulfilled” / treating
  A/B as token savings / letting Jev send / pasting
  bars as results is soundness theater.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 41–48, question-design,
  methods-catalog, formal-methods, agent-self-assessment,
  ecosystem, CHANGELOG, README.
- notes.md §89; sources.json (504 sources, 501 unique URLs,
  retrieved 2026-09-19T17:55Z); findings.md batch #72.
  No wrapper.

## 2026-09-19 ~18:41 UTC — hourly 1241 HIGH (~12:41 Boise)
- Docs-only on a **fresh PR off main**. Never reopen
  merged #3 / #4 / #5. `notes.md` §90. Skip Archer.
  Do **not** re-fold 1144 / §89. Hunches labeled.
  No wrapper. No invented metrics. Quote READMEs.
  Soft Noul ≠ hard safety. 0★ HIGHs still get real
  cards. Not a Jev skill dump. Backend-agnostic
  categorization/scoring/decision class.
- Folded how-to-apply clusters: Observe→score→act
  namesake (ZHUBoer/ego-jev reserved `__none__`;
  runWorkflow completed ≠ success; **≠** jiangkoumo);
  Decision-as-ranking (jsort scores are relative; Noul
  not Choice for scale);
  Native vs schema-guided Harbor
  (groundedness-judge-bench native vs schema-guided;
  implicit_true included in yes; **≠** jev-judge-bench);
  0 promotions / authored vs real (jev_playground 0
  promotions; routing-backtest 0.0447%);
  Offload + classifier-not-generator
  (yuyang2230/jev-agent-skill jev-1.13-free;
  jev-techstack-classifier stack_config.json);
  Collapse late (s1_ruby collapse late; `undecided?`
  abstain; **≠** hunch **≠** feelings);
  Unofficial toolbelt (2389-research/judgement license
  null; confidence ≠ winner p; typesafeai-sdk-community
  not a new species);
  Pointer shell (tpellet/hunch exit 3; never-execute
  list; **≠** carldaws/hunch);
  Preview-first VOI / rubric rewrite (jev-file-search
  scores not calibrated accuracy; jev-linkmap Jev never
  sees S2 prose);
  Life fail-open covers (muhammedilyasy/jev-mail
  metadata only; tidy none-of-folders stay; tab-bouncer
  pinned/audio/current never closed; lkclean Show
  fail-open; jev-yt-time-saver Show anyway);
  S1 decide / S2 plan (ORIGIN pause-if-no-Jev;
  validResponse sums-to-1; **≠** Essentiel-Jev);
  Seed/expand/judge/verify + local daemon ≠ Jev
  (jev-crawlers risk bands never raw boolean; jevbrain
  AUTO_ACT is not a Noul).
- Formal compose: Ego Lite locators / `__none__` /
  completed≠success; jsort scores relative;
  groundedness 0.5 label on Noul; playground 0
  promotions; s1_ruby `?` vs `undecided?`; hunch exit 3
  + never-execute; tidy 0.8 + none stay; tab
  pinned/audio; lkclean Show; YT Show anyway; ORIGIN
  pause-if-no-Jev + validResponse; crawlers verify
  grounding not exec; jevbrain AUTO_ACT is not a Noul.
  Soft Noul ≠ hard safety. Hard-gating AUTO_ACT /
  ranking-as-frequency / 95.2% / 83% plumbing / 36/120
  as class ceilings is soundness theater.
- Census not re-derived. Archer still NOT landed (HF
  empty; tracker likes 49 lastModified
  2026-09-19T18:37:18Z still promised). Laya yes.
  Blackwood ABSENT. SemIf 1846 (+17). jevlike 962 (+3).
  TypeAR-AI/TypeAR 10 (+1). Awesomejev flat 561/27007.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 49–61, question-design,
  methods-catalog, formal-methods, agent-self-assessment,
  ecosystem, CHANGELOG, README.
- notes.md §90; sources.json (524 sources, 521 unique URLs,
  retrieved 2026-09-19T18:41Z); findings.md batch #73.
  No wrapper.

## 2026-09-19 ~19:47 UTC — hourly 1347 HIGH (~13:47 Boise)
- Docs-only on a **fresh PR off main**. Never reopen
  merged #3 / #4 / #5 / #7. `notes.md` §91. Skip Archer.
  Do **not** re-fold 1241 / §90. Hunches labeled.
  No wrapper. No invented metrics. Quote READMEs.
  Soft Noul ≠ hard safety. 0★ HIGHs still get real
  cards. Not a Jev skill dump. Backend-agnostic
  categorization/scoring/decision class.
- Folded how-to-apply clusters: Judge harness as
  control API (judgekit YAML classify/score/route/verify;
  typed-judge-kit verdict-in-code);
  Batch packing VOI (alsoleg89/decide packing VOI;
  0.8 ≠ 80% accuracy; **≠** jev-sift);
  Calibration as product (Jev-Calibration Platt ECE
  0.117→0.052; jev-calibration-arena never acts);
  Decision-as-Plugin (ctmx/openrouter-jev-mcp
  Decision-as-Plugin; FrancoisChastel/jev-code ≠ npm
  jev-code; claudecode-jev-marketplace fail-open not
  hot path; pedroknigge/mcp_jev packs not ask_jev;
  cyrusasco/typesafe-mcp noul deadband 0.35–0.65;
  codaaiteam/jev-skill jevtypesafeai.com ≠ TypeSafe);
  Policy-constrained skill select (hermes-switchyard ≠
  hermes-jev-router ≠ hermes-plugin-jev);
  Tiny local econ pruner (nanoprune 2.8MB ECE 2.58%);
  Observe→score→act cousins (smartdio/jev-browser-agent
  ≠ ZHUBoer/ego-jev; Dakai/omp-jev-web DONE ≠ proof;
  hari007sh/jev ≠ dannote/jev);
  Deterministic verify ≠ System One
  (0thernet/system-one-skills deterministic verify);
  Soft-score vs hard-argmax (typed-gate band
  [0.40,0.60] is refusal; pi-jev-gate fail-closed; choice is the verdict;
  rh-guard owns).
- Formal compose: YAML/recipe as control API; packing
  VOI; arena never acts; Decision-as-Plugin fail-open
  missing key / not-hot-path; Switchyard advisory never
  loads skills; nanoprune 0-hallucination theater;
  DONE ≠ proof; system-one-verify is deterministic;
  mid-band is refusal. Soft Noul ≠ hard safety.
  Hard-gating argmax as safety / 97.7% n=130 / 8,026
  tokens as class ceilings is soundness theater.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 62–70, question-design,
  methods-catalog, formal-methods, agent-self-assessment,
  ecosystem, CHANGELOG, README.
- notes.md §91; sources.json (543 sources, 540 unique URLs,
  retrieved 2026-09-19T19:47Z); findings.md batch #74.
  No wrapper.

## 2026-09-19 ~20:41 UTC — hourly 1441 HIGH (~14:41 Boise)
- Docs-only on a **fresh PR off main**. Never reopen
  merged #3 / #4 / #5 / #7 / **#8**. `notes.md` §92.
  Skip Archer. Do **not** re-fold 1347 / §91. Hunches
  labeled. No wrapper. No invented metrics. Quote
  READMEs. Soft Noul ≠ hard safety. 0★ HIGHs still
  get real cards. Not a Jev skill dump.
  Backend-agnostic categorization/scoring/decision
  class. rh-guard owns the gate cousins; Augustus
  owns placement.
- Folded how-to-apply clusters: Self-hosted econ
  (Foq ~25ms/2.2GB local; rev prefill-only + HF
  jev-0.5b; robfrase/jev planning memo);
  Soft-judgment gate integrity
  (typesafe_agent_gates 27/27 / 31/31;
  EpicEric/safe-sh static remainder; pastepilot
  Confirm before act; rh-guard owns);
  Retrieval as calibrated decision space
  (Jev-Reranker live Jev not yet measured;
  sessionwise opt-in relevance; jev-search pointer
  sieve);
  Enterprise reflexes (400ms Salesforce WebMCP;
  typesafe-scheduler-diagnostics advisory);
  Screenshot-free / CU (droidjev screenshot-free;
  Tewoto1 jevcu planner still writes);
  Hybrid S1/S2 (ha-conversation-jev Jev→Grok;
  dsh-jev can only gate);
  Harbor-jevals / SRE
  (jev-classification-benchmark specified not run;
  jev-luna-pagerduty p≥0.50);
  Laya densifies (meldltd/meldecision laya-go ONNX;
  laya-doom never pixels; logixism/laya-api empty
  README; akpsahan/laya ≠ Archer);
  Demos / unofficial toolbelt (choxos/jevchess
  engine owns truth; jev-drive sim not AV;
  story-arc Jev never authors; jev-hs-assistant HS6;
  golergka/jev-plays-starcraft-2 UI-verified ≠ API
  Victory; awesome-jev-use-cases catalog;
  Nibir1/typesafe-go ≠ official).
- Formal compose: local class-backend economics;
  remainder after exact rules; retrieve then decide;
  advisory diagnoses never place Pods; screenshot-free
  observe→score→act; S1 decide / S2 leftover;
  Harbor-jevals for ops; packaging ≠ new species;
  engine owns truth. Soft Noul ≠ hard safety.
  Pasting Foq 100%/ECE 0.2% / Reranker 0.1667 /
  400 ms / akpsahan vs-Jev as class ceilings, or
  treating Qwen3.8-27B as Archer, is soundness
  theater.
- Census not re-derived. Archer still NOT landed;
  tracker likes **50** lastModified UNCHANGED
  2026-09-19T18:37:18Z; SemIf 1873 (+7); jevlike
  969 (+2); TypeAR 10 flat; Awesomejev 561/27007
  flat.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 71–79, question-design,
  methods-catalog, formal-methods, agent-self-assessment,
  ecosystem, CHANGELOG, README.
- notes.md §92; sources.json (570 sources, 567 unique URLs,
  retrieved 2026-09-19T20:41Z); findings.md batch #75.
  No wrapper.

## 2026-09-19 ~21:23 UTC — SIGNAL jevcache + jev-align (~15:23 Boise)
- Docs-only on a **fresh PR off main** after #9 merge
  `059f3670`. Never reopen merged #3 / #4 / #5 / #7 /
  #8 / **#9**. `notes.md` §93. Skip Archer. Do **not**
  re-fold 1441 / §92. Hunches labeled. No wrapper.
  No invented metrics. Quote READMEs. Soft Noul ≠
  hard safety. Not a Jev skill dump. Backend-agnostic
  categorization/scoring/decision class. rh-guard
  owns HIT-as-truth and training-score auto-accept;
  Augustus owns placement. Archive tarball SIGNAL.md
  for both (fetched ~15:13 Boise).
- Folded how-to-apply clusters: Decision ledger /
  memoization (hyperspaceai/jevcache; fingerprint
  after redact; recall vs decide; publish
  fingerprints+answers; CI replay as Harbor cousin;
  Cache hit ≠ correctness; hyperspaceai/jevcache ≠
  kushals256/jevcache; memoize typed decisions; VOI
  of cache hit); GEPA alignment loop
  (sutro-sh/jev-align; human labels only; score never
  auto-accepts; production capture flywheel;
  sutro-sh/jev-align ≠ caiovicentino/jev-align;
  GEPA + System One).
- Formal compose: a HIT is a sensor not a proof; a
  training score is a sensor not an accept. Soft
  Noul ≠ hard safety.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 80–81, question-design,
  methods-catalog, formal-methods, optimizer-integration,
  agent-self-assessment, ecosystem, CHANGELOG, README.
- notes.md §93; sources.json (572 sources, 569 unique
  URLs, retrieved 2026-09-19T21:23Z); findings.md
  batch #76. No wrapper.

## 2026-09-19 ~21:35 UTC — SIGNAL enzyme + JA ModernBERT + Gemma/Nemotron/djev-dev/Laya essay (~15:32–15:35 Boise)
- Docs-only on a **fresh PR off main** after #10 merge
  `30438eff`. Never reopen merged #3 / #4 / #5 / #7 /
  #8 / #9 / **#10**. `notes.md` §94. Skip Archer. Do
  **not** re-fold jevcache/jev-align / §93. Hunches
  labeled. No wrapper. No invented metrics. Quote
  READMEs. Soft Noul ≠ hard safety. Not a Jev skill
  dump. Backend-agnostic categorization/scoring/
  decision class. rh-guard owns guidance-as-hook,
  unofficial-local-as-Jev, hosted-bootstrap silent
  FALLBACK, LFM-default-as-JA-softmax, Nemotron “not
  calibrated replacement”, and Laya confidence-without-
  competence; Augustus owns placement. Archive
  tarball SIGNAL.md for three clusters (fetched
  ~15:32–15:35 Boise). No 1541 fold PR was open
  (`gh pr list --state open` had #11 modernbert-only
  extending §93; this PR is the requested three-
  cluster §94 fold with SIGNAL name locks).
- Folded how-to-apply clusters: Compile-time System
  One / questions-as-index (byenzyme/enzyme;
  guidance ≠ hook; catalysts ≠ summaries;
  compile-time System One; hosted bootstrap ≠
  silent TypeSafe); unofficial JA ModernBERT
  cross-encoder (argos1111/modernbert-ja-310m-jev;
  unofficial ≠ TypeSafe; format_version
  modernbert-jev/1; Argos1111/jev_local ≠
  us/jev-local ≠ kunchenguid/local-jev; LFM
  default ≠ ModernBERT backend); NAR class
  legitimacy / multimodal / Router-OOD (@googlegemma;
  pst2154/Nemotron_Jev; Nemotron ≠ TypeSafe Jev;
  not a calibrated replacement; Davipar/djev-dev;
  djev-dev complements djev-spark; images as Choice
  options; Laya essay numbers *theirs*; Router/OOD
  confidence).
- Formal compose: `when asked`, unofficial local p,
  Nemotron p, and Laya 0.85 are sensors. Soft Noul ≠
  hard safety.
- Census not re-derived. Archer still NOT landed.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 82–84, question-design,
  methods-catalog, formal-methods,
  agent-self-assessment, ecosystem, CHANGELOG, README.
- notes.md §94; sources.json (581 sources, 578 unique
  URLs, retrieved 2026-09-19T21:35Z); findings.md
  batch #77. No wrapper.
## 2026-09-19 ~21:41 UTC — hourly 1541 HIGH (~15:41 Boise)
- Docs-only on a **fresh PR off main**. Never reopen
  merged #7 / **#8** / **#9** / **#10** / **#12**.
  Do **not** re-fold §93 / §94. `notes.md` §95.
  Skip Archer. Do **not** re-fold 1441 / §92. Hunches
  labeled. No wrapper. No invented metrics. Quote
  READMEs. Soft Noul ≠ hard safety. 0★ HIGHs still
  get real cards. Not a Jev skill dump.
  Backend-agnostic categorization/scoring/decision
  class. rh-guard owns the injection-firewall /
  CI-gate cousins; Augustus owns placement.
- Folded how-to-apply clusters: Decision-as-plugin
  for SWE (difficulty + policy thresholds + JSONL
  trace; jev-codex-pilot model + reasoning depth;
  keep/shadow/hybrid/reject);
  Evidence projection vs LLM summary
  (quarry evidence projection);
  Soft judgment integrity (jevguard
  calibrator/cache/escape; jev-ci-selector CI
  shadow mode; rh-guard owns);
  Physical/control first-class domain
  (Frank-ZY-Dou/awesome-jev robotics/3D/control);
  Harbor-jevals / injection-firewall
  (one-dollar-tahoe TypeSafe Jev defense eval;
  rh-guard owns);
  llama.cpp replica (llama-jev llama.cpp replica;
  softmax ≠ Noul).
- Formal compose: next-act Choice + policy in code;
  pointer never paraphrase; remainder after exact
  rules; shadow then honor; text-state not pixels;
  measurement owns endorsement; replica honesty.
  Soft Noul ≠ hard safety. Pasting 0.95 FINISH /
  skip_below 0.05 / OpenRoboto $ as class ceilings,
  inventing ASR/FPR, or treating softmax as a Noul
  is soundness theater.
- Census not provided this hour (not re-derived).
  Archer still NOT landed. Last pin from §92:
  tracker likes **50** lastModified UNCHANGED
  2026-09-19T18:37:18Z; SemIf 1873; jevlike 969;
  TypeAR 10; Awesomejev 561/27007.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 85–90, question-design,
  methods-catalog, formal-methods, agent-self-assessment,
  ecosystem, CHANGELOG, README.
- notes.md §95; sources.json (590 sources, 587 unique URLs,
  retrieved 2026-09-19T21:41Z); findings.md batch #78.
  No wrapper.

## 2026-09-19 ~22:39 UTC — hourly 1639 HIGH (~16:39 Boise)
- Docs-only on a **fresh PR off main**. Never reopen
  merged #7 / **#8** / **#9** / **#10** / **#12** /
  **#13**. Do **not** re-fold §93 / §94 / §95.
  `notes.md` §96. Skip Archer. Do **not** re-fold
  1441 / §92. Hunches labeled. No wrapper. No invented
  metrics. Quote READMEs. Soft Noul ≠ hard safety.
  0★ HIGH still gets a real card. Not a Jev skill
  dump. Backend-agnostic categorization/scoring/
  decision class. Augustus owns placement (stdout
  prune is not a rh-guard gate).
- Folded how-to-apply: OpenCode host-port of
  evidence-preserving stdout prune
  (indiejoseph/opencode-jev-pruner; observe→score-
  candidates→prune; jev-zen / jev-1.13-free;
  zen-chat ≠ Noul; fail-open original; keepScore
  >0.1 floor). MEDIUM watch: jev-webagent-bench
  empty stub; Kiln-AI/jev_jsonschema noul_threshold
  0.5; NSStudent/JevSwiftSDK unofficial.
- Formal compose: a Noul is a SENSOR. Hard-gating
  prune as proof of irrelevance, or treating
  zen-chat as calibrated Jev, is soundness theater.
  Soft Noul ≠ hard safety.
- Census not provided this hour (not re-derived).
  Archer still NOT landed. Last pin from §92:
  tracker likes **50** lastModified UNCHANGED
  2026-09-19T18:37:18Z; SemIf 1873; jevlike 969;
  TypeAR 10; Awesomejev 561/27007.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 91–92, question-design,
  methods-catalog, formal-methods, agent-self-assessment,
  ecosystem, CHANGELOG, README.
- notes.md §96; sources.json (594 sources, 591 unique URLs,
  retrieved 2026-09-19T22:39Z); findings.md batch #79.
  No wrapper.

## 2026-09-19 ~23:17 UTC — SIGNAL gliner-native-runtime (~17:17 Boise)
- Docs-only on a **fresh PR off main**. Never reopen
  merged #7 / **#8** / **#9** / **#10** / **#12** /
  **#13** / **#14**. Do **not** re-fold §93 / §94 / §95 /
  §96. `notes.md` §97. Skip Archer. Do **not** re-fold
  1441 / §92. Hunches labeled. No wrapper. No invented
  metrics. Quote READMEs. Soft Noul ≠ hard safety.
  User-linked SIGNAL (pushed 2026-08-26). Not a Jev
  skill dump. Backend-agnostic categorization/scoring/
  decision class. Augustus owns placement (rh-guard
  skips).
- Folded how-to-apply: GLiNER2 native Apple path
  (shershah1024/gliner-native-runtime; unofficial
  Swift/Core ML GLiNER 2.5-small; entity spans +
  confidence; not Choice/Score/Noul; not TypeSafe;
  label descriptions as schema; on-device ANE
  economics; honesty locks; ≠ Fastino ≠
  gliner25-compaction ≠ gliner2-ultrafast ≠
  Eran-BA/Jev_from_GLiNER2 ≠ NSStudent/JevSwiftSDK ≠
  jevmlx; default threshold 0.1 still soft).
- Formal compose: a span confidence is a SENSOR.
  Hard-gating 0.1 as NER quality, treating this as
  TypeSafe `/v1/systemone`, or inventing ANE Harbor
  is soundness theater. Soft Noul ≠ hard safety.
- Census not provided this hour (not re-derived).
  Archer still NOT landed. Last pin from §92:
  tracker likes **50** lastModified UNCHANGED
  2026-09-19T18:37:18Z; SemIf 1873; jevlike 969;
  TypeAR 10; Awesomejev 561/27007.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra item 93, question-design,
  methods-catalog, formal-methods, agent-self-assessment,
  ecosystem, CHANGELOG, README.
- notes.md §97; sources.json (596 sources, 593 unique URLs,
  retrieved 2026-09-19T23:17Z); findings.md batch #80.
  No wrapper.

## 2026-09-19 ~23:40 UTC — hourly 1740 HIGH (~17:40 Boise)
- Docs-only on a **fresh PR off main**. Never reopen
  merged #7 / **#8** / **#9** / **#10** / **#12** /
  **#13** / **#14** / **#15**. Do **not** re-fold §93 /
  §94 / §95 / §96 / §97. `notes.md` §98. Skip Archer
  rewrite. Do **not** re-fold 1639 / gliner-native-runtime
  / 1541. Hunches labeled. No wrapper. No invented
  metrics. Quote READMEs. Soft Noul ≠ hard safety.
  0★ HIGH still gets a real card. Not a Jev skill
  dump. Backend-agnostic categorization/scoring/
  decision class. Augustus owns placement (rh-guard
  does not own protocol envelope / meaning-search
  ranking / replica honesty).
- Folded how-to-apply: Decision Graph Protocol
  (numerous-com/dgp; Decision Graph Protocol
  frame→assess→commit; app retains permissions/effects;
  Jev-first assessor-neutral; guarded commit /
  receipt/next frame; assessment batching; hard-gating
  DGP as safety theater; numerous-com/dgp ≠ TypeSafe
  official). Calibrated meaning-grep (can1357/jegrep;
  jegrep calibrated path+range Nouls; no
  embeddings/index/daemon; ~$0.01–0.03 typical; agent
  --json; can1357/jegrep ≠ Bentlybro/jevgrep ≠
  uehaj/jev-semgrep). Archer-arch fidelity + measured
  calibration gap (jaredpalmer/kev family; Archer-arch
  fidelity; kev family OOD 0.76–0.77 vs Jev 0.86;
  block-causal isolation; pointer/readout CE-trained;
  /v1/systemone drop-in; replica honesty; do not
  rewrite §45).
- Formal compose: a Noul is a SENSOR. Hard-gating DGP
  as safety theater, hard-gating a miss as “the concept
  is absent,” treating OpenRouter/TypeSafe auto-failover
  as one Noul (silent FALLBACK), or pasting OOD acc as
  “close enough to ship as Jev” is soundness theater.
  Soft Noul ≠ hard safety.
- Census not provided this hour except Archer tracker
  likes **51** (+1 vs last pin **50**); lastModified
  UNCHANGED 2026-09-19T18:37:18Z; Hub
  archerhume/4rcherhume HTTP **401**. Archer still NOT
  landed. Last remaining pin from §92: SemIf 1873;
  jevlike 969; TypeAR 10; Awesomejev 561/27007.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 94–96, question-design,
  methods-catalog, formal-methods, agent-self-assessment,
  ecosystem, CHANGELOG, README.
-   notes.md §98; sources.json (607 sources, 604 unique URLs,
  retrieved 2026-09-19T23:40Z); findings.md batch #81.
  No wrapper.

## 2026-09-20T00:43:33Z — hourly 1843 HIGH (Boise ~18:43 MDT)

- Docs-only fold on a **fresh PR off main**. Never reopen
  merged #7–**#16**. Prior fold agent
  `bc-37d98185-7b64-5345-8327-1414294cc9aa` finished;
  Augustus #16 MERGED. Do **not** re-fold 1740 / §98 /
  1639 / §96 / gliner-native-runtime / §97 / 1541 / §95.
  Skip Archer rewrite. Quote READMEs. Hunches labeled.
  No wrappers / keys / install recipes. Do not dump
  source / SDK / weights / training corpora.
  `invented_signal: false`.
- Five HIGH: Kungie/gut (PRIMARY; **0★**; cost-derived
  YES/NO/UNSURE overlay); Illusion47586/judge (**0★**;
  typed-callback twin); zwliJay/jev-forge (**1★**;
  variable-N option scoring as the trainable object;
  not a sixth species); wfzyx/von late-catch (**43★**;
  NAR local drop-in; Needle snapshot ≠ 395M table);
  ishaannk/llm-vs-jev (**0★**; typed vs chat judges
  cross-note; rh-guard owns steerability).
- gut/judge are **control-flow / decision-theory
  overlays, not new class-table species**. Formal
  methods compose with scoring; a Noul is a SENSOR.
  Hard-gating 0.038, merging Needle 52.6% with n=78
  93%, “guaranteeing” calibration, or pasting “Jev
  wins guardrailing” is soundness theater.
- Pulse (do not invent): Archer still NOT landed. Hub
  archerhume/4rcherhume HTTP **401**. Qwen3.8-27B ≠
  Archer. Tracker likes **51** flat; lastModified
  UNCHANGED 2026-09-19T18:37:18Z. Laya yes. Blackwood
  ABSENT from tracker (Hub still 200). Awesomejev
  561/27007 flat (user-provided; ≠ AnotiaWang 83★).
  Live REST: SemIf **1936★**; jevlike **983★** (watch
  claimed 984); TypeAR **11★** flat. X MCP since_id
  held `2100958005663568282`; pages_archived 0; no
  invented tweets.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models Apply 1843, judgment-class
  von late-catch + jev-forge class-architecture,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 97–101, question-design,
  methods-catalog, formal-methods, agent-self-assessment,
  ecosystem, CHANGELOG, README.
- notes.md §99; sources.json; findings.md batch #82.
  No wrapper. Do **not** merge from this review.
- Adversarial review honesty locks: live SKILL/README
  class index no longer presents von as current tiny
  SAN (Needle §49 snapshot ≠ this-pass 395M / n=78);
  `on_unsure="raise"` named as app policy, not a
  System One hard gate; gut license quoted as GitHub
  Apache-2.0 / LICENSE MIT / pyproject Apache-2.0
  *theirs* (same split honesty as jev-forge).

## 2026-09-20T01:43Z — hourly 1943 HIGH (Boise ~19:43 MDT)

- Fresh PR off main after merged #17 (`b844cb6` / §99).
  Never reopen merged #7–**#17**. Branch
  `cursor/hourly-1943-probably-jev-align-0408`.
  Prior 1843 fold agent
  `bc-562b8004-e121-5379-a560-cc1082f67e93` is FINISHED.
  Skip Archer rewrite. Quote READMEs. Mark *theirs*.
  No wrappers / keys / install recipes. Do not dump
  source / SDK / weights / training corpora.
  `invented_signal: false`.
- Nine HIGH: southpolesteve/probably (PRIMARY; **3★**;
  Jev IS the if-statement); sutro-sh/jev-align (**133★**
  live-star / framing delta of §93; HEAD/README SHA
  unchanged); samdotmak/jev-recall (**6★**; retrieve by
  relevance not resemblance); chopratejas/invalidate
  (**11★** HIGH upgrade; memory leases ended by new
  evidence); mizchi/jev-lint (**13★**; jevlint rename);
  Kiln-AI/jev_jsonschema (**5★** HIGH upgrade; JSON
  Schema question compiler); mizorewww/laya-coreml
  (**0★**; on-device Laya CoreML ANE); Micha0827/snapjudge
  (**3★**; softmax ≠ Noul); direwolfiy/JevPi (**0★**;
  Jev-first Pi agent loop).
- probably is a **language**, not a library overlay.
  Formal methods compose with scoring; a Noul is a SENSOR.
  Hard-gating `feels`, pasting 17/18 as Harbor, hard-gating
  0 of 157, treating boolean @ 0.5 as a proof, claiming
  10×, treating softmax as a Noul, or treating 62 tests as
  quality is soundness theater.
- Pulse (do not invent): Archer still NOT landed last pin
  from §99. Hub archerhume/4rcherhume HTTP **401**. Tracker
  likes **51** flat; lastModified UNCHANGED
  2026-09-19T18:37:18Z. Live REST: SemIf **1954★**; jevlike
  **989★**; TypeAR **11★** flat. AnotiaWang/awesome-jev
  **83★** ≠ Awesomejev 561/27007. X MCP not used; no
  invented tweets.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models Apply 1943, judgment-class
  language/replica notes, validation, applied-mappings,
  mappings, toolbox, composition-algebra items 102–110,
  question-design, methods-catalog, formal-methods,
  optimizer-integration jev-align 133★ delta,
  agent-self-assessment, ecosystem, CHANGELOG, README.
- notes.md §100; sources.json; findings.md batch #83.
  No wrapper. Do **not** merge from this review.
- Adversarial review honesty locks: jev-lint **is**
  jevlint (GitHub rename, not a second product); jev-align
  HEAD/README SHA unchanged vs §93 (stars 60→133);
  invalidate / jev_jsonschema are HIGH upgrades not new
  mechanisms; GitHub homepage null for invalidate /
  jev-recall despite attached JSON (quote README demos);
  JevPi GitHub size 0 with contents (same honesty as gut);
  0★ HIGH still got a real card.
## 2026-09-20T06:42Z — hourly 0042 HIGH (Boise ~00:42 MDT)

- Fresh PR off main after merged #22 (`98ded82` / §104).
  Never reopen merged #7–**#22**. Do **not** merge from
  merged **#22** (hourly 2340 / §104). Branch
  `cursor/hourly-0042-augustus-fold-3529`.
  Skip Archer rewrite. Quote READMEs. Mark *theirs*.
  No wrappers / keys / install recipes. Do not dump
  source / SDK / weights / eval logs.
  `invented_signal: false`.
- Twelve HIGH: Arohtea/jev-readout (PRIMARY; **0★**;
  structured probability readouts); gulagala001/jevify
  (**0★**; ordinary-model Jev-shape; ≠ Mintzs/jevify);
  mourad-ghafiri/laya-rlcd-benchmark (**0★**; 40.3% below
  constant-answer); SupremeDreamZ/jev-fastloop (**0★**;
  cheap fail-open semantic edge); TheWebDevel/jev-fanout
  (**0★**; asking more questions in one call);
  harneet2512/reflexrl (**0★**; VLM+Jev RL teacher);
  yibie/laya-jev-lab (**0★**; independent Jev API vs Laya);
  umstek/zero-shot-ie-bench (**0★**; GLiNER vs GLiFormer
  vs Laya vs Jev); angelgalvisc/snake-arena-jev-vs-llms
  (**0★**; decisions-per-minute & cost);
  sathariels/jevcheck (**0★**; behavioral contracts);
  GaneshVG18/upgrade-radar (**0★**; HEAD `e438f9bd` live
  rewrite vs prior-agent `d7cfc80c`); lirantal/discoprint
  (**0★**; discography theme/mood/complexity).
- Formal methods compose with scoring; a Noul is a SENSOR.
  Treating displayed p as proof, schema-valid JSON as a
  calibrated Noul, collapsing gulagala001 into Mintzs,
  quoting 40.3% without the constant-answer, hard-gating
  fastloop confidence as safety, treating 0.0000 sd as
  universal determinism, treating 2.95× as Harbor,
  hard-gating cascade 0.60, collapsing locate into decide,
  treating snake points as intelligence, treating jevcheck
  as a correctness proof, treating `no_direct_evidence` as
  merge-safe, or treating theme Choice as a music-theory
  certificate is soundness theater. Hard-gating a soft
  Noul as safety is the anti-pattern.
- Pulse (do not invent; superseded by post-PR relock
  below): first-fold pin SemIf **2047★** / jevlike
  **1018★** / AnotiaWang **91★** / Laya **672**. Tracker
  likes **56**; lastModified **UNCHANGED** vs §104.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models Apply 0042, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 149–160, question-design,
  methods-catalog, formal-methods, agent-self-assessment,
  ecosystem, CHANGELOG, README.
- notes.md §105; sources.json; findings.md batch #88.
  No wrapper. Do **not** merge from this review.
- Adversarial review honesty locks: GitHub size 0 with
  contents (jev-readout / gulagala001/jevify /
  laya-rlcd-benchmark / jev-fastloop / jev-fanout /
  reflexrl / upgrade-radar / discoprint);
  laya-jev-lab size **49** (relock; was **0** with contents);
  zero-shot-ie-bench size **50** (relock; was **33**); snake-arena size **194**;
  jevcheck size **117**; license null (Arohtea README MIT;
  mourad); gulagala001 SPDX MIT this pass; upgrade-radar
  HEAD `d7cfc80c`→`e438f9bd` / README `d1094805`→`c32f7d18`;
  0★ HIGH still got a real card (all twelve **0★**).
  Name locks: gulagala001/jevify ≠ Mintzs/jevify;
  mourad ≠ yibie/laya-jev-lab; jev-fastloop ≠ jev-ultrafast;
  reflexrl ≠ khordoo; yibie/laya-jev-lab ≠ dairui1 ≠
  BrendanH18; snake-arena ≠ jev-plays-games; jevcheck ≠
  jevals ≠ SivletLabs/jev-eval; upgrade-radar ≠
  paper-radar-jev.

## 2026-09-20T07:20Z — hourly 0042 live REST relock after first PR (#23)

- Independent live REST after `be7f95b` (PR #23). Design
  claims unchanged. Unique consecutive fragments unchanged.
  Skip Archer rewrite. `invented_signal: false`.
- HIGH HEAD/README **moved** (relock): Arohtea/jev-readout
  HEAD `03734993`→`6f1e5900`, README `76a99fe5`→`67ee1e96`
  (still distribution > argmax / Noul 0.5 / Score as
  expectation / bare HTTP); GaneshVG18/upgrade-radar HEAD
  `1e91eb03`→`e438f9bd`, README `b7603c01`→`c32f7d18`
  (still Jev never generates filenames /
  `no_direct_evidence` ≠ merge-safe / Action `@v0.1.3`);
  lirantal/discoprint HEAD `c2a3d47e`→`a9d3294f`, README
  `392efd29`→`9a64f473` (still theme/mood/complexity /
  five atomic questions one call). Size still **0** with
  contents on those three.
- HIGH HEAD/README **unchanged**: gulagala001/jevify,
  mourad-ghafiri/laya-rlcd-benchmark, jev-fastloop,
  jev-fanout, reflexrl, yibie/laya-jev-lab, umstek,
  snake-arena, jevcheck. GitHub size lag: yibie/laya-jev-lab
  **49** (was **0** with contents); umstek **50** (was
  **33**). snake-arena **194**; jevcheck **117**.
- Pulse vs first-fold / §104: SemIf **2057★** (+10 vs
  **2047**); jevlike **1021★** (+3 vs **1018**); TypeAR
  **12★** **flat**; AnotiaWang/awesome-jev **92★** (+1 vs
  **91**); yibie/awesome-jev **442★** (was **430**). Laya
  Hub likes **686** (+14 vs **672**). Qwen3.8-27B likes
  **15793** (was **15787**) ≠ Archer. Tracker likes **56**
  / lastModified `2026-09-20T04:29:16Z` **UNCHANGED**.
  Blackwood likes **2** gated manual — census **absent**.
  Archer Hub HTTP **401**. All twelve HIGH still **0★**.
  Do **not** merge from this review.

## 2026-09-20T07:26Z — hourly 0042 independent adversarial relock after `92577f5` (PR #23)

- Independent review of claimed live-REST pin `92577f5` (relock
  after first fold `be7f95b`). HIGH HEAD/README **unchanged**.
  GitHub pushed timestamps moved without commit: Arohtea
  `07:01:17Z`; upgrade-radar `07:09:10Z`; discoprint
  `07:00:03Z`; umstek `07:25:24Z` (HEAD/README still
  `8770b16b` / `d69dc96a`). Named pulse drifted vs `92577f5`:
  SemIf **2059★** (was **2057★**; +12 vs §104 **2047**).
  jevlike **1022★** (was **1021★**; +4 vs §104 **1018**).
  TypeAR **12★** **flat**. AnotiaWang **92★** **flat**.
  yibie/awesome-jev **443★** (was **442★**). Laya Hub likes
  **690** (was **686**). Qwen3.8-27B likes **15794** (was
  **15793**) ≠ Archer. Tracker likes **56** / lastModified
  `2026-09-20T04:29:16.000Z` **UNCHANGED**. Blackwood likes
  **2** gated manual — census **absent**. Archer Hub HTTP
  **401**. findings.md batch #88 still said `notes.md` §104 /
  open PR #22 and umstek size 33 — corrected to §105 / merged
  #22 / size 50. All twelve HIGH still **0★**. Design claims
  unchanged. Unique consecutive fragments unchanged. Skip
  Archer rewrite. `invented_signal: false`. Do **not** merge
  from this review.

## 2026-09-20T07:37Z — hourly 0042 independent adversarial relock after `0558f7d` (PR #23)

- Independent review of claimed live-REST pin `0558f7d`.
  HIGH HEAD/README **unchanged**. All twelve still **0★**.
  GitHub size lag (HEAD/README unchanged):
  SupremeDreamZ/jev-fastloop **12**; TheWebDevel/jev-fanout
  **206**; harneet2512/reflexrl **749**;
  GaneshVG18/upgrade-radar **908**; gulagala001/jevify
  **145**; mourad-ghafiri/laya-rlcd-benchmark **164**;
  lirantal/discoprint **239**; Arohtea **44** (all were **0**
  with contents). No remaining size-0 HIGH.
  yibie/laya-jev-lab **49**; umstek
  **50**; snake-arena **194**; jevcheck **117**.
- Named pulse vs `0558f7d`: SemIf **2069★** (was **2059★**;
  +22 vs §104 **2047**). jevlike **1022★** **flat**.
  TypeAR **12★** **flat**. AnotiaWang **92★** **flat**.
  yibie/awesome-jev **450★** (was **443★** at `0558f7d`).
  Laya Hub likes **705** (was **690** at `0558f7d`).
  Qwen3.8-27B likes **15796** (was **15794**) ≠ Archer.
  Tracker likes **59** (+3 vs §104 **56**) / lastModified
  `2026-09-20T04:29:16.000Z` **UNCHANGED**. Arohtea GitHub
  size **44** (was **0** with contents; HEAD/README
  unchanged). No remaining size-0 HIGH. Blackwood likes
  **2** gated manual — census **absent**. Archer Hub HTTP
  **401**. Design claims unchanged. Unique consecutive
  fragments unchanged. Skip Archer rewrite.
  `invented_signal: false`. Do **not** merge from this
  review.

## 2026-09-20T06:42Z — hourly 2340 independent adversarial relock after `babb111` (PR #22)

- Independent review of `babb111` (prior PASS claimed live REST).
  HIGH HEAD/README pins still unchanged. Named pulse drifted:
  SemIf **2047★** (was **2041★**; +28 vs §103 **2019**).
  jevlike **1018★** (was **1011★**; +12 vs §103 **1006**).
  TypeAR **12★** **flat**. AnotiaWang **91★** (was **88★**).
  yibie **430★** (was **423★**). cobanov **224★** (was **221★**).
  simple-jev **318★** (was **314★**). logicrw **136★** (size **7677**, was **7136**; HEAD/README unchanged) /
  openjev-sglang **205★** / OpenJevPro size **64** unchanged.
  Tracker `multimodalart/jev-reproductions-tracker` likes **56** /
  lastModified `2026-09-20T04:29:16.000Z` unchanged.
  Hub `archerhume/4rcherhume` HTTP **401**. `Tonic/4rcher-tracker`
  HTTP **401** (not the reproductions tracker). Qwen likes **15787**.
  Qwen3.8-27B ≠ Archer.
- README quotes re-checked *theirs* at locked HEAD/README SHAs.
  `invented_signal: false`. Do **not** merge from this
  review — parent merges after CLEAN.

## 2026-09-20T07:45Z — hourly 0145 HIGH (Boise ~01:45 MDT)

- Fresh PR off main after merged #23 (`44e6b9ac` / §105).
  **HARD RULE:** do not reopen or amend PR #23.
  Never reopen merged #7–**#23**. Branch
  `cursor/hourly-0145-augustus-fold-78c6`.
  Skip Archer rewrite. Quote READMEs. Mark *theirs*.
  No wrappers / keys / install recipes. Do not dump
  source. 0★ HIGH still gets a real card. Quote live
  REST over watch. `invented_signal: false`.
- Architecture probes PRIMARY (train-or-local recipes,
  not TypeSafe drop-in): uspraveen/Jevify (**0★**;
  description-only stub / size 0; HEAD `0f29d783`;
  README SHA `32608473`); Ruivalim/exu-base (**1★**;
  Exu is a toolkit, not a method); Colvin0315/MiniSystemOne
  (**0★**; HEAD `d7f9f803` / README SHA `a5b0d2fd`
  changed vs §104; 90.5 seconds / 29.2% pipeline
  evidence); scienthoon/luce (**1★**; 91.1 % / ECE 0.022
  *theirs*); RichardoMrMu/jev-mini (**0★**; 46x speedup /
  accuracy identical; ECE 0.624 sentiment catastrophe);
  tapsin/jev-local (**0★**; JSON parse of generated text ≠ Noul).
- Measurement densifies: goya4140/jev-reward-model-evaluation
  (**0★**; RewardBench v1 92.58%; Precise IF 50.63%);
  SarathChandraBellam/jev-vs-llm-ticket-router (**0★**;
  Scaffolding in progress); Shilin237/jev-vs-llm-cost
  (**0★**; TypeSafe's own published benchmark);
  fstandhartinger/jevbench (**6★**; HEAD `c7ab99f5`;
  do not re-fold §78 v1.2 board as new; Laya (421M) 70.1
  now on board; classifier.dev fast tier 84.8 is Jev
  behind its own API); AIGNLAI/ReflexRoute (**1★**;
  hard budget filter before Jev); priyankark/jev-state
  (**0★**; Jev judges the next state, XState enforces
  transitions); hfspace mjyoke1111/jev-consistency-benchmark
  (This Space contains no benchmark result yet).
- Catalog gravity: v-modal/awesome-jev-tools (**339★**
  live REST; watch said 337; curation is not endorsement);
  RadRebelSam/awesome-jev (**0★**; crawler-maintained
  directory; Daily GitHub + npm sweep, human-merged).
- HF class ports: rdxtremity/jev-reranking (likes **0**;
  query-side encoders, not a Jev replica);
  onnx-community/system-one-qwen3.5-4b-scorer-ONNX
  (CC-BY-NC-4.0; temperature 1.75; transformers.js
  AutoModel cannot load this graph).
- Formal methods compose with scoring; a Noul is a SENSOR.
  Treating a Jevify two-liner as a checkpoint, pasting
  Colvin as hyusi, treating JSON parse as a Noul, quoting
  46x / 91.1% / 92.58% / 84.8 as class ceilings, treating
  classifier.dev #1 as a better model, re-folding §78 as
  new, letting Jev do budget arithmetic, treating XState
  as Jev, pasting catalog ★ as eval, treating SPLADE as
  TypeSafe Jev, or treating an empty consistency Space as
  a win is soundness theater. Jevify stub and
  JSON-parse-as-Noul are the anti-patterns.
- Pulse (do not invent): Archer still NOT landed. Hub
  archerhume/4rcherhume HTTP **401**. Tracker likes **59**;
  lastModified `2026-09-20T04:29:16.000Z` **UNCHANGED**.
  Live REST: SemIf **2074★** (+27 vs §104 2047);
  jevlike **1022★** (+4 vs §104 1018); TypeAR **12★**
  **flat**. AnotiaWang/awesome-jev **92★** ≠ Awesomejev
  561/27007 ≠ logicrw **146★** ≠ v-modal **339★**.
  yibie **450★**; cobanov **228★**. Qwen3.8-27B ≠ Archer
  (likes **15796**; lastModified UNCHANGED). Laya Hub
  likes **704**. typesafe-ai/skills still v0.5.7 HEAD
  `65a39f3`. X MCP not used; no invented tweets.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models Apply 0145, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 161–177, question-design,
  methods-catalog, formal-methods, agent-self-assessment,
  ecosystem, CHANGELOG, README.
- notes.md §106; sources.json; findings.md batch #89.
  No wrapper. Do **not** merge from this review.
- Adversarial review honesty locks: Jevify size **0**
  HEAD `0f29d783` README SHA `32608473`; Colvin HEAD
  `d7f9f803` README SHA `a5b0d2fd` (was §104 `ac5a0eea` /
  `f8c47847`); awesome-jev-tools **339★** (watch 337)
  HEAD `f117e0c3`; jevbench **6★** HEAD `c7ab99f5`
  README SHA `8fe07c41` (was `27ed3d6c` / `bf1e79ba`);
  logicrw **146★** HEAD `8dce5fa8` (was **136★** /
  `97057cc1`); SemIf **2074★** (was §104 **2047★**);
  tracker likes **59** lastModified unchanged;
  size **0** with contents (Jevify, jev-mini, tapsin,
  goya, ticket-router, cost, ReflexRoute, jev-state);
  0★ HIGH still get real cards (v-modal 339★; jevbench
  6★; exu/luce/ReflexRoute 1★). YAML frontmatter must
  still parse. do not reopen or amend PR #23.

## 2026-09-20T06:17Z — hourly 2340 independent adversarial relock (PR #22)

- Independent review of first-review `3255a57` (claimed live REST
  relock after FAIL). HIGH HEAD/README pins still unchanged.
  Pulse stars and OpenJevPro GitHub size had drifted: logicrw
  **135★** (was **134★**; HEAD `97057cc1` / README SHA `25a19b31`
  unchanged — auto GitHub sync). SemIf **2041★** (was **2031★**;
  +22 vs §103 **2019**). jevlike **1011★** (was **1010★**). TypeAR **12★**
  **flat**. AnotiaWang **88★** (was **87★**). yibie **423★** (was
  **417★**). cobanov **221★** **flat**. OpenJevPro size **64** (was
  **62**; HEAD `94d77bcb` / README SHA `50c77ace` unchanged).
  simple-jev **314★** (was **311★**). openjev-sglang **204★** (was
  **202★**). Tracker likes **56** / lastModified
  `2026-09-20T04:29:16.000Z` unchanged. Archer Hub still HTTP **401**.
  Qwen likes **15787** unchanged. Qwen3.8-27B ≠ Archer.
- README quotes re-checked *theirs* at locked HEAD/README SHAs
  (ESCI 0.242/0.255; jevbetter 0.916/0.873; RLCD 0.5052/0.2872/0.0055;
  OpenJevPro pastes openjev-sglang 95.5%; hyusi two-line stub size 5).
  `invented_signal: false`. Do **not** merge from this
  review — parent merges after CLEAN.

## 2026-09-20T06:09Z — hourly 2340 adversarial relock (PR #22)

- Live REST vs first pin: HIGH HEAD/README unchanged.
  logicrw/awesome-jev-projects **134★** (was **132★**;
  HEAD `97057cc1` / README SHA `25a19b31` unchanged —
  auto GitHub sync). SemIf **2031★** (was **2025★**).
  jevlike **1010★** (was **1009★**). TypeAR **12★** still
  **flat**. AnotiaWang **87★** still **flat**. Tracker
  likes **56** / lastModified `2026-09-20T04:29:16.000Z`
  unchanged. Archer Hub still HTTP **401**. Qwen likes
  **15787** unchanged. Qwen3.8-27B ≠ Archer.
- GitHub size lag: patelvishwa112/jev-system-one-rlcd
  **1513** (was **0** with contents; HEAD `62b103b3`
  README SHA `55994d69` unchanged). Colvin0315/MiniSystemOne
  **814** (was **0** with contents; HEAD `ac5a0eea`
  README SHA `f8c47847` unchanged). Do not paste Colvin
  as hyusi.
- Namesake stars: yibie/awesome-jev **417★** (was **412★**);
  cobanov/awesome-jev **221★** (was **217★**). Still
  different objects from logicrw **134★**.
- `invented_signal: false`. Do **not** merge from this
  review — parent merges after CLEAN.

## 2026-09-20T05:40Z — hourly 2340 HIGH (Boise ~23:40 MDT)

- Fresh PR off main after merged #21 (`d3f8da7` / §103).
  Never reopen merged #7–**#21**. Branch
  `cursor/hourly-2340-minisystemone-8b98`.
  Skip Archer rewrite. Quote READMEs. Mark *theirs*.
  No wrappers / keys / install recipes. Do not dump
  source / SDK / weights / eval logs.
  `invented_signal: false`.
- Eleven HIGH: hyusi2003/MiniSystemOne (PRIMARY; **0★**;
  from-scratch calibrated decision model; description-only stub);
  yodablocks/jev-orderby-bench (**0★**; ESCI hard-probe upgrade);
  karanb192/jev-architect (**0★**; find/design/evaluate decision loops);
  Jairik/jev-distiller (**0★**; distill-Jev UI stub);
  licensedsaucer9-web/jev-opportunities (**0★**; scored opportunity map);
  gavinHuang/jevinize (**0★**; Jev-inize → simple-jev);
  VihaanAgarwal/jev-diff (**0★**; saved-decision regression);
  zhangcy122/OpenJevPro (**0★**; constrained-logprob API);
  patelvishwa112/jev-system-one-rlcd (**0★**; SmolLM RLCD);
  logicrw/awesome-jev-projects (**134★**; source-backed Awesome radar);
  olanotolu/jevbetter (**12★**; rival-aware one-pass scorer).
- Formal methods compose with scoring; a Noul is a SENSOR.
  Treating a description-only stub as a checkpoint, re-folding
  six-gates as new, distilling Jev as teacher of record, pasting
  openjev-sglang as OpenJevPro, treating constrained logprob as
  a Noul, quoting an untrained-looking demo as Jev identity,
  pasting a radar's listed numbers, or quoting 0.916 as a class
  ceiling is soundness theater. Distill-Jev UI stub and
  constrained-logprob-as-Noul are the anti-patterns.
- Pulse (do not invent): Archer still NOT landed. Hub
  archerhume/4rcherhume HTTP **401**. Tracker likes **56**;
  lastModified `2026-09-20T04:29:16.000Z` (not re-fetched as
  a rewrite). Live REST: SemIf **2031★** (+12 vs §103 2019);
  jevlike **1010★** (+4 vs §103 1006); TypeAR **12★**
  **flat**. AnotiaWang/awesome-jev **87★** **flat** ≠ Awesomejev
  561/27007 ≠ logicrw **134★**. Qwen3.8-27B ≠ Archer (likes
  **15787**). X MCP not used; no invented tweets.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models Apply 2340, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 138–148, question-design,
  methods-catalog, formal-methods, agent-self-assessment,
  ecosystem, CHANGELOG, README.
- notes.md §104; sources.json; findings.md batch #87.
  No wrapper. Do **not** merge from this review.
- Adversarial review honesty locks: MiniSystemOne size **5**
  HEAD `4385335b` README SHA `83016bf8`; orderby size **309**
  (relock; was **281**) HEAD `52397954`; awesome-jev-projects
  HEAD `97057cc1` (relock; was `45bab8c4`; README SHA `25a19b31`
  unchanged — auto GitHub sync); jevbetter **12★**; GitHub size
  **1513** (relock; was **0** with contents) (RLCD); OpenJevPro
  PolyForm NC LICENSE SHA `5aa42b53`; RLCD no LICENSE file.

## 2026-09-20T04:46Z — hourly 2246 HIGH (Boise ~22:46 MDT)

- Fresh PR off main after merged #20 (`b3e3ad2` / §102).
  Never reopen merged #7–**#20**. Branch
  `cursor/hourly-2246-system-one-bench-ceb0`.
  Skip Archer rewrite. Quote READMEs. Mark *theirs*.
  No wrappers / keys / install recipes. Do not dump
  source / SDK / weights / eval logs.
  `invented_signal: false`.
- Nine HIGH: reachjalil/system-one-bench (PRIMARY; **0★**;
  independent System One evidence catalog);
  SivletLabs/jev-eval (**0★**; typed eval freeze);
  nafisazizir/hev (**0★**; option-isolated replica);
  yuki-oshio/mini-jev (**0★**; frozen-LLM logits);
  erik-dunteman/ChatJev (**1★**; AR next-token
  anti-pattern);
  wufuju2023-cell/jev-alpha-proof-analysis (**0★**;
  scoring × proof-search);
  zzzzzec/jevsort (**1★**; parallel rank vs serial);
  rupeshpoojary9/awesome-open-system-one (**0★**;
  curated open System One ecosystem catalog);
  LYchoon/paper-radar-jev (**0★**; size **73**;
  knowledge-work paper radar).
- Formal methods compose with scoring; a Noul is a SENSOR.
  Treating a catalog row as a bake-off win, treating
  constructed scenes as production logs, pasting Hev
  80.00% as Jev identity, quoting mini-jev 93.25% as
  family-disjoint, putting Jev in an AR next-token loop,
  laundering a Noul as a Lean step, treating parallel
  rank-k as a sort proof, pasting a curated list’s von
  sub-15ms as an Augustus fact, or hard-thresholding
  paper-radar 0.5 as frequency is soundness theater.
  ChatJev-style soundness theater is the anti-pattern.
- Pulse (do not invent): Archer still NOT landed. Hub
  archerhume/4rcherhume HTTP **401**. Tracker likes **54**;
  lastModified `2026-09-20T02:59:13Z` (not re-fetched as
  a rewrite). Live REST (review relock): SemIf **2019★**;
  jevlike **1006★** (+4 vs §102 1002); TypeAR **12★**
  **flat**. AnotiaWang/awesome-jev **87★** (+1 vs §102 **86**) ≠ Awesomejev
  561/27007. Qwen3.8-27B ≠ Archer. X MCP not used; no
  invented tweets.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models Apply 2246, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 129–137, question-design,
  methods-catalog, formal-methods, agent-self-assessment,
  ecosystem, CHANGELOG, README.
- notes.md §103; sources.json; findings.md batch #86.
  No wrapper. Do **not** merge from this review.
- Adversarial review honesty locks: system-one-bench size
  **90** HEAD `ceb17269` README SHA `d9e0c7b7` (live
  rewrite after pin `4a83bae6` / `3e7109bf`; 19 reviewed
  records); hev size **2318**; GitHub size 0 with
  contents (jev-eval / ChatJev / alpha-proof);
  mini-jev size **38370**; awesome-open-system-one size **4**;
  paper-radar size **73** default **master**; license null
  (ChatJev / alpha-proof / jevsort); CC0 SPDX NOASSERTION
  (awesome-open-system-one); Hub OWNER not published (hev);
  0★ HIGH still got a real card (jevsort **1★**).
  **Review FAIL then lock:** reachjalil/system-one-bench ≠
  mallahyari/system-one-benchmark; SivletLabs/jev-eval ≠
  willkelly/jev-evaluation ≠ 4esv/jev-eval; ChatJev ≠
  jev-gpt; live REST SemIf **2019★** / jevlike **1006★** /
  TypeAR **12★**.
  **PR #21 adversarial FAIL then lock:** PRIMARY HEAD
  `4a83bae6`→`ceb17269` / README `3e7109bf`→`d9e0c7b7` /
  12→19 reviewed records; jevsort HEAD `2d960ab9`→`57067b90`
  / README `cbe5e6bf`→`85044740`; SemIf **2012★**→**2019★**
  (+19 vs §102 **2000**); ChatJev **0★**→**1★**; mini-jev
  size **0**→**38370**; awesome-open-system-one size **0**→**4**.
  TokenTrim 62.4% still *theirs* in `records/routing-ablation.md`.
  PRIMARY HEAD continued `6ff27aa8`→`ceb17269` (recipe-smoke
  commits; README SHA unchanged `d9e0c7b7`; 19 records).
  Do not dump smoke JSON / invent Harbor numbers.
  AnotiaWang/awesome-jev **86★**→**87★**.

## 2026-09-20T03:45Z — hourly 2145 HIGH (Boise ~21:45 MDT)

- Fresh PR off main after merged #19 (`320aff9` / §101).
  Never reopen merged #7–**#19**. Branch
  `cursor/hourly-2145-fold-282d`.
  Skip Archer rewrite. Quote READMEs. Mark *theirs*.
  No wrappers / keys / install recipes. Do not dump
  source / SDK / weights / eval logs.
  `invented_signal: false`.
- Nine HIGH: yodablocks/jevq (PRIMARY; **0★**;
  question-linting of Jev questions themselves);
  ChristianAlexander/laya_ex (**0★**; open Laya binding);
  humandebri/IC-Laya (**0★**; on-chain/edge);
  agilabs-ai/jev48 (**0★**; auditable weekend replica);
  copyleftdev/ember (**0★**; dual-judge / framing);
  PIXELZX0/XERON (**0★**; Laya specialist FT, GPU-pending)
  + daliborsb/laya (Hub replica drop);
  MagaBitmex/jev-4b-distill-data (student corpus;
  student checkpoint missing);
  lewislululu/jevon (non-LLM VIN; likes **3**);
  WaynezProg/jev-kit (**0★**; source-bound evidence).
- Formal methods compose with scoring; a Noul is a SENSOR.
  Treating a clean jevq run as measured separation,
  treating 62 IC-Laya tests as Laya parity, letting a
  Score grant Tx, pasting AUROC as a phishing win,
  injecting priors as help, treating v4 as a controller,
  distilling Jev as teacher of record, pasting maze 1.00
  as a general System One, or treating exit 0 as claim
  truth is soundness theater.
- Pulse (do not invent): Archer still NOT landed. Hub
  archerhume/4rcherhume HTTP **401**. Tracker likes **54**;
  lastModified `2026-09-20T02:59:13Z` (not re-fetched as
  a rewrite). Live REST (review relock): SemIf **2000★**;
  jevlike **1002★** flat; TypeAR **12★** (+1 vs §101 11).
  AnotiaWang/awesome-jev **86★** ≠ Awesomejev 561/27007.
  Qwen3.8-27B ≠ Archer. X MCP not used; no invented tweets.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models Apply 2145, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 120–128, question-design,
  methods-catalog, formal-methods, agent-self-assessment,
  ecosystem, CHANGELOG, README.
- notes.md §102; sources.json; findings.md batch #85.
  No wrapper. Do **not** merge from this review.
- Adversarial review honesty locks: GitHub size 0 with
  contents (jevq / laya_ex / IC-Laya / jev-kit); jev48
  size **1439**; ember size **479**; XERON size **52**;
  license null (XERON; README Apache-2.0); MagaBitmex/jev-4b-distill
  model NOT FOUND; daliborsb copied vs-Jev is §76;
  IC-Laya parity_verified false / MASK 50284 vs PAD 50283;
  0★ HIGH still got a real card (jevon likes **3**).
  **Review FAIL then lock:** WaynezProg/jev-kit ≠
  jonathanavis96/jev-kit (Airlock); ember SCALING.md at
  locked HEAD `c02f622b` is **7/24 → 1/24 → 0/24**
  (SPECTRAL 11/40 is later, not this pin); live REST
  SemIf **2000★** / TypeAR **12★**.

## 2026-09-20T02:41Z — hourly 2041 HIGH (Boise ~20:41 MDT)

- Fresh PR off main after merged #18 (`7ef9613` / §100).
  Never reopen merged #7–**#18**. Branch
  `cursor/hourly-2041-bias-bench-jev-eval-bca1`.
  Skip Archer rewrite. Quote READMEs. Mark *theirs*.
  No wrappers / keys / install recipes. Do not dump
  source / SDK / weights / eval logs.
  `invented_signal: false`.
- Nine HIGH: natemoo-re/bias-bench (PRIMARY; **0★**;
  resume-screening bias audit methodology);
  austindixson/planalyzer (**0★**; code-owned
  pass|review|block); cannacre8ive/switchboard-ai
  (**1★**; cost-aware routing; package 0.4.0);
  elcronos/jev-vs-open-decision-models (**0★**;
  frozen-protocol bake-off); cvsgireesh/jevusher
  (**0★**; VOI admission); MokiMeow/jev-fabric
  (**0★**; typed control plane); jose-troche/live-rubric
  (**0★**; scoring economics); willkelly/jev-evaluation
  (**0★**; pre-registered science); nshkrdotcom/system_one_sdk
  (**0★**; class infrastructure).
- Formal methods compose with scoring; a Noul is a SENSOR.
  Treating a zero binary name gap as a fairness
  certificate, letting Jev emit the verdict string,
  pasting PrismNLI's lead without the contamination
  caveat, treating J7 pass as safe to obey, treating a
  receipt as authorization, or hard-gating confidence
  ≥0.95 is soundness theater. rh-guard owns injection.
- Pulse (do not invent): Archer still NOT landed. Hub
  archerhume/4rcherhume HTTP **401**. Tracker likes **54**
  (+3 vs §100 pin **51**); lastModified **CHANGED**
  2026-09-20T02:59:13Z (was §100 2026-09-19T18:37:18Z).
  Live REST: SemIf **1984★**; jevlike **1002★**; TypeAR
  **11★** flat. AnotiaWang/awesome-jev **84★** ≠
  Awesomejev 561/27007. X MCP not used; no invented tweets.
- Cards: SKILL.md, mixed-architecture fail table +
  gallery, faq, mental-models Apply 2041, judgment-class,
  validation, applied-mappings, mappings, toolbox,
  composition-algebra items 111–119, question-design,
  methods-catalog, formal-methods, agent-self-assessment,
  ecosystem, CHANGELOG, README.
- notes.md §101; sources.json; findings.md batch #84.
  No wrapper. Do **not** merge from this review.
- Adversarial review honesty locks: GitHub size 0 with
  contents (bias-bench / planalyzer / switchboard /
  elcronos / system_one_sdk); jevusher size **81**;
  license null
  (bias-bench / elcronos / live-rubric); switchboard
  README V0.4 / package 0.4.0 / M4–M5 functional as
  logical plans+DAG; MCP adapters / learned economics
  not done; live-rubric ~$0.000004 desc / ~$0.000006
  README Costs; system_one_sdk GitHub desc provider-neutral
  / README opening TypeSafe-first; jev-fabric historical-v0
  zero retained cases; 0★ HIGH still got a real card
  (switchboard now **1★** live REST).


## 2026-09-20T08:43Z — hourly 0243 HIGH (Boise ~02:43 MDT)

- Fresh PR off main after merged #24 (`4d9dcd1` / §106).
  **HARD RULE:** do not reopen or amend PR #23 or #24.
  Never reopen merged #7–**#24**. Branch
  `cursor/hourly-0243-augustus-fold-d3c8`.
  Skip Archer rewrite. Quote READMEs. Mark *theirs*.
  No wrappers / keys / install recipes. Do not dump
  source. 0★ HIGH still gets a real card. Quote live
  REST over watch. `invented_signal: false`.
- Measurement densifies PRIMARY: erendikmenn/jev-llm-router-benchmark
  (**0★**; HEAD `f44ef450`; README SHA `df3687e5`; size **0**
  with contents; Sol 94.2 / Luna 83.9 / Jev path 89.7;
  19.2% Sol / 62.3% cost save / 4.5pp miss of 2pp
  non-inferiority; p50 latency worse than Sol due to
  routing overhead; cheap alone is not success);
  aesaganda/jev-ticket-router (**0★**; license null; Express +
  node:sqlite; previous_ticket_count >= 3 is code;
  MIN_CONFIDENCE 0.6 still soft; ≠ Sarath);
  hoangngochuong24947-gif/jev-figure-router (**1★**;
  confidence ≥ 0.85 hard-gate is theater; generative AI
  banned from scientific plots);
  hfdataset Praveenrajus/jev-bench (likes **0**; sha `c9c3032c`;
  166,054 rows / 22 configs; ≠ fstandhartinger/jevbench).
- Open reproduction class ports: hf NicolaiMTLassen/open-bonzi-jev
  (likes **0**; sha `09240156`; Hub does not ship weights;
  100/100 easy T/F is not Harbor; label_mass ≠ correctness;
  ≠ NicolaiLassen; GH companion **0★** HEAD `1c2508fd`);
  onnx-community/open-jev-deberta-v3-large-ONNX (likes **0**;
  sha `3bc2553b`; temperature 1.05; AutoModel from_pretrained
  works; ≠ system-one-qwen3.5-4b-scorer-ONNX);
  Heman10x-NGU/openJev-verdict-2.0 (**107★** densify; HEAD
  `a458733c`; GH 151M vs README 149.6M; PR #1 now closed
  unmerged; do not re-fold §71 claim-audit as a beat).
- Study densification: wjdjdakf17/jev-study (**0★**; HEAD
  `24b5d7d7`; typed decisions, RLCD, confidence-gated
  routing; structured ≠ correct; mock not live API; 26
  tests; ≠ baekenough/jev-study).
- Formal methods compose with scoring; a Noul is a SENSOR.
  Treating a 0.85 figure FAST_PATH as a proof, 100/100
  easy T/F as Harbor, label_mass as correctness, 77.10%
  as beating Jev, collapsing ticket-router into Sarath,
  collapsing jev-bench into jevbench, collapsing DeBERTa
  ONNX into the Qwen scorer ONNX, treating 151M vs 149.6M
  as two models, quoting 62.3% without the 4.5pp miss,
  treating mock keyword as production, hard-gating ticket
  0.6 as safety, treating a study mock as a live API,
  treating stock llama.cpp Q2_0 as working, or re-folding
  §71 as a beat is soundness theater. Figure-router 0.85
  hard-gate and 100/100 easy T/F as Harbor are the
  anti-patterns.
- Pulse (do not invent): Archer still NOT landed. Hub
  archerhume/4rcherhume HTTP **401**. Tracker likes **59**;
  lastModified `2026-09-20T04:29:16.000Z` **UNCHANGED**.
  Live REST: SemIf **2094★** (+20 vs §106 2074);
  jevlike **1023★** (+1 vs §106 1022); TypeAR **12★**
  **flat**. AnotiaWang/awesome-jev **93★** ≠ Awesomejev
  561/27007. Hub Laya likes **729**. Qwen3.8-27B ≠ Archer.
  X MCP not used. `invented_signal: false`.
- Folded into SKILL.md (description + protocol +
  mapping-index), mental-models Apply 0243, faq,
  mixed-architecture fail table + gallery, applied-mappings,
  validation, judgment-class, composition-algebra items
  178–185, toolbox-mapping, methods-catalog, formal-methods,
  question-design, agent-self-assessment, mappings,
  CHANGELOG, README, docs/ecosystem, findings batch #90,
  sources.json. Hunches labeled. No wrapper.


## 2026-09-20T09:45Z — hourly 0345 HIGH (Boise ~03:45 MDT)

- Fresh PR off main after merged #25 (`6fbd019` / §107).
  **HARD RULE:** do not reopen or amend PR #23 or #24 or #25.
  Never reopen merged #7–**#25**. Branch
  `cursor/hourly-0345-augustus-fold-7a07`.
  Skip Archer rewrite. Quote READMEs. Mark *theirs*.
  No wrappers / keys / install recipes. Do not dump
  source. 0★ HIGH still gets a real card. Size **0**
  WITH CONTENTS still gets a real card. Quote live
  REST over watch. `invented_signal: false`.
- Open reproduction densifies: hf NicolaiMTLassen/bonzi-27b-v2-jev
  (likes **0**; sha `c4d21b74`; Hub still does not ship weights;
  WANLI-256 74.6% *theirs*; ternary still needs PrismML fork);
  bonzi-8b-ternary-v1-jev (sha `47b66187`; WANLI-256 65.2%);
  bonzi-27b-v1-jev (sha `2fb8061a`; Bonsai 1 27B Q1_0 runs on
  stock llama.cpp; WANLI-256 71.1%); mizchi/laya-multilingual-onnx
  (sha `b6314ec9`; ships 646.9MB; 63/63 / 5.1e-4 CPU / 1.2e-2 WebGPU);
  IamBusy/OpenJev-Vision (sha `8cf6cbd3`; CLEVR-4 held-out joint 0%);
  heman10x/openJev-verdict-2.0 (likes **5**; sha `794d5e0d`;
  twin tokenizer-only); IamBusy/OpenJev-Vision-Research-v0.1
  (sha `43e49184`; 12,832; 294,912 derived targets not independent
  samples); UpHash-Network/mini-jev (**0★**; HEAD `52fbae12`;
  yuki-oshio transfer; residual-head decreased 73/96→67/96).
- Measurement densifies PRIMARY: ASEVlad/jev-injection-bench
  (**0★**; HEAD `c0d0f25d`; size **107**; 11,900;
  Jev best ranking / Haiku better ECE 0.021 vs 0.058;
  0.5–0.9 band is where Jev's numbers do not mean what they say;
  Prompt wording moves panic 28%); manojlds/jev-dspy-bench
  (**0★**; HEAD `d8c68d72`; Jev agreement is similarity, never
  ground truth; no aggregate quality grade or merge gate);
  sshariqali/jev-abstentionbench (**0★**; HEAD `f5c0c068`;
  rank 1 of 20 vs 2025 field; question-asymmetry;
  forward-looking 0.465 never extreme); misakaikato/openkev
  (**0★**; HEAD `babcab1c`; calibration layer not a runtime;
  select_threshold returns inf); goodrahstar/pdf-race
  (**0★**; HEAD `1c687fc6`; parser owns the wall clock;
  12/12 tie is a tie; titles selected not generated);
  ZeroX-01/jev-atlas (**0★**; license null; HEAD `bc94bf50`;
  catalog not endorsement); samyakjain0606/jev-is-here
  (**0★**; license null; HEAD `eb0de0ba`; flopcheck 16
  calibrated tweet judgments; mechanical tells in code);
  hfspace BunsDev/laya-calibration-lab (likes **0**; sha
  `a3fc13ba`; T never changes argmax; confidence ≠ top-label p;
  40–48 rows too small to ship T).
- Formal methods compose with scoring; a Noul is a SENSOR.
  Treating WANLI-256 as Harbor, label_mass as correctness,
  Hub family cards as shipping weights, collapsing stock Q1_0
  into §107 Q2_0 gibberish, treating the HF twin as a weights
  drop, quoting 93.25% as family-disjoint, hard-gating injection
  ECE 0.058 as “Jev is calibrated”, quoting rank 1 without
  question-asymmetry / 2025 field, treating dspy-bench as a
  quality claim, hard-gating pdf-race 12/12 as pipeline
  equality, treating atlas listed counts as eval, hard-gating
  flopcheck composite as truth, treating calibration-lab 40-row
  T as production, treating CLEVR joint 0% as “vision Jev
  works”, treating ONNX 63/63 as ECE, treating openkev T as
  transferable, or treating select_threshold inf as a bug is
  soundness theater. Injection ECE 0.058 as a hard gate and
  40-row T as production are the anti-patterns.
- Pulse (do not invent): Archer still NOT landed. Hub
  archerhume/4rcherhume HTTP **401**. Tracker likes **60**;
  lastModified `2026-09-20T04:29:16.000Z` **UNCHANGED**.
  Live REST: SemIf **2128★** (+34 vs §107 2094);
  jevlike **1026★** (+3 vs §107 1023); TypeAR **12★**
  **flat**. AnotiaWang/awesome-jev **94★** ≠ Awesomejev
  561/27007. Hub Laya likes **765**. Qwen3.8-27B ≠ Archer.
  X MCP not used. `invented_signal: false`.
- Folded into SKILL.md (description + protocol +
  mapping-index), mental-models Apply 0345, faq,
  mixed-architecture fail table + gallery, applied-mappings,
  validation, judgment-class, composition-algebra items
  186–201, toolbox-mapping, methods-catalog, formal-methods,
  question-design, agent-self-assessment, mappings,
  CHANGELOG, README, docs/ecosystem, findings batch #91,
  sources.json. Hunches labeled. No wrapper.

## 2026-09-20T13:43Z — hourly 0743 HIGH (Boise ~07:43 MDT)

- Fresh PR off main after merged #29 (`a9c8b61` / §111).
  **HARD RULE:** do not reopen or amend PR #23 or #24 or #25 or #26 or #27 or #28 or #29 or #30 or #32.
  Never reopen merged #7–**#29** / merged **#30**. Branch
  `cursor/fold-hourly-0743-high-794b`.
  Skip Archer rewrite. Quote READMEs. Mark *theirs*.
  No wrappers / keys / install recipes. Do not dump
  source. 0★ HIGH still gets a real card. Size **0**
  WITH CONTENTS still gets a real card. Quote live
  REST over watch. `invented_signal: false`.
- Measurement densifies PRIMARY: ywchiu/jev_benchmark
  (**1★**; HEAD `4322c350`; size **173**;
  Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%;
  restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask;
  They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%);
  siren2345/jev-single-decode-transformers (**0★**; HEAD `2aa5fea7`;
  siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode;
  Split Transformers experiment from llama.cpp runtime);
  tanayvasishtha/jev-lab (**0★**; HEAD `96c90cdd`;
  Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling;
  second pass must be $0.00 from cache; The pages never call Jev);
  plus dataset/Space densifies (Praveenrajus sha a39eba3f; pngwn README 404;
  jevlogs HDFS 0.9933; BunsDev sha eda59e0a; mini-jev-runs 27 900).
- Open-weight / RLCD: Verdict-open-jev (**33★**; HEAD `30f15564`;
  TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%);
  Mintzs densify 26.1× / 90.0% / 167 ms; rlcd-lite Finding 1 trap;
  distill-corpus Student B MAE 0.148 / Pearson 0.836 / 86.0%;
  altryne/jevify Find where Jev belongs. Design the questions. Measure the difference.
- Skills / DecisionOps: ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome;
  Jev-Skill local path does not claim replica; simplosophy current-llm.
- Anti-patterns: 77.0% as Harbor, 0.85 as 85%, TF-IDF ECE as beating Jev,
  softmax A/B/C as a Noul, ACT as a provider proof.
- Pulse (do not invent): Archer still promised_not_landed. Hub
  archerhume/4rcherhume HTTP **401**. Tracker likes **66**;
  lastModified `2026-09-20T04:29:16.000Z` **UNCHANGED**.
  Laya present (likes **843**); Blackwood ABSENT. Live REST:
  SemIf **2225★** (+17 vs §111 2207); jevlike **1046★**
  (+1 vs §111 1043); TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM **16★**.
  AnotiaWang/awesome-jev **98★** ≠ yibie/awesome-jev **516★**.
  Qwen3.8-27B ≠ Archer.
  X MCP not used. `invented_signal: false`.
- Folded into SKILL.md (description + protocol +
  mapping-index), mental-models Apply 0743, faq,
  mixed-architecture fail table + gallery, applied-mappings,
  validation, judgment-class, composition-algebra items
  273–288, toolbox-mapping, methods-catalog, formal-methods,
  question-design, agent-self-assessment, mappings,
  CHANGELOG, README, docs/ecosystem, findings batch #96,
  sources.json. Hunches labeled. No wrapper.
  Hourly 0743 uniqueness lock: Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%; abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%; 0.85 coverage 84.60% selective risk 1.18%; 26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled; Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084; reliability 0.007 but resolution 0.000; 27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624; 22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f; Student B MAE 0.148 / Pearson 0.836 / 86.0%; pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2; HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000; 2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated; E2 recomputes from saved probabilities; Space sha eda59e0a; MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T; T never changes argmax; siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling; second pass must be $0.00 from cache; The pages never call Jev; Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%; restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask; They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%; ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench; ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome; confidence is descriptive provider output, not a substitute for probability; Quality denominators include only valid scored answers; an exact halfway tie chooses the lower level; aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills; The local path does not claim to turn a smaller checkpoint into Jev; Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION; current-llm; 结构兼容，不是 Jev 模型能力; altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; Find where Jev belongs. Design the questions. Measure the difference; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★; SemIf 2241★ (+34 vs §111 2207); jevlike 1051★ (+8 vs 1043); AnotiaWang 98★ (+1 vs 97); yibie/awesome-jev 525★ (+19 vs 506); Laya likes 864 (was 822); tracker likes 67 (+3 vs 64); lastModified UNCHANGED `2026-09-20T04:29:16.000Z`; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32/#33; notes.md §113

## 2026-09-20T12:46Z — hourly 0646 HIGH (Boise ~06:46 MDT)

- Fresh PR off main after merged #28 (`c7c0300` / §110).
  **HARD RULE:** do not reopen or amend PR #23 or #24 or #25 or #26 or #27 or #28.
  Never reopen merged #7–**#28**. Branch
  `cursor/fold-hourly-0646-high-795b`.
  Skip Archer rewrite. Quote READMEs. Mark *theirs*.
  No wrappers / keys / install recipes. Do not dump
  source. 0★ HIGH still gets a real card. Size **0**
  WITH CONTENTS still gets a real card. Quote live
  REST over watch. `invented_signal: false`.
- Measurement densifies PRIMARY: alakise/calibration-is-not-alpha
  (**0★**; HEAD `064b75f5`; size **268**;
  Calibration is not alpha; NO CURRENT ALPHA CANDIDATE;
  ΔR² approximately +0.00084; Brier 0.2131387; ECE 0.0421875;
  Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05);
  OrMizL/jev-compaction-bench (**0★**; HEAD `92fd33e6`;
  default 0.5 keeps zero non pinned; keepResult median 0.14 to 0.17;
  keepCall median 0.28 to 0.35; usable range is about 0.10 to 0.25;
  7.8% to 57.9%; judges results it never sees; task-finish eval not built yet;
  $0.002 per compaction);
  slavadubrov/sgr-judge-bench (**0★**; HEAD `5e142707`;
  slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench;
  Jev 108/120 $0.083 0.34 s; Luna SGR 114/120;
  paired Jev accuracy-difference intervals include zero; not evidence of equivalence;
  GLM SGR 26/120 93 format failures; Terra-planned Jev hybrid 55/120);
  elyashium/atlas-replay-lab (**0★**; HEAD `9856ab9b`; empty README;
  rule-based by default, optionally Jev-backed;
  missing key cannot break the experience);
  siren2345/jev-single-decode (**0★**; HEAD `65df86a3`;
  prefill plus exactly one decode; softmax over A/B/C ≠ Noul;
  BBQ 9,053/10,000 (90.53%); ECE 0.0890; Mean confidence 0.9943;
  overconfident; score and noul not implemented).
- Datasets/Spaces: DGUI 12 rows (was 6); INSTRUCT 119 rows likes 2;
  pngwn/open-jev encode the state once, decide everything in parallel;
  0.740 accuracy against a 0.508 majority; ECE 0.047;
  fine-tune's advantage ends where its 384-token training data does;
  jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd;
  Space does not call Jev; recomputes routing from saved probabilities.
- Applied/skills/economics: 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22;
  synthetic repository benchmark; Jev evaluations are advisory;
  YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep;
  default threshold 0.8 still soft; 40-line windows cannot prove whole function;
  token-native sequential start/end Choice; Gemini/Haiku stubs not configured yet;
  handful of hand-written examples, not a benchmark; Jev judged exactly what it was given;
  laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills;
  contract_passed is not a claim of guaranteed factual truth;
  Wilson lower bound 0.85 floor; fixture mode no savings claim.
- Formal methods compose with scoring; a Noul is a SENSOR.
  Treating ECE as alpha, 0.5 compaction as safety, 0.8 as 80%,
  Wilson 0.85 as a proof, or contract_passed as truth is
  soundness theater. Calibration is not alpha; ranking ≠
  calibration theater are the anti-patterns.
- Pulse (do not invent): Archer still promised_not_landed. Hub
  archerhume/4rcherhume HTTP **401**. Tracker likes **64**;
  lastModified `2026-09-20T04:29:16.000Z` **UNCHANGED**.
  Laya present (likes **822**); Blackwood ABSENT. Live REST:
  SemIf **2207★** (+21 vs §110 2186); jevlike **1043★**
  (+5 vs §110 1038); TypeAR **15★** (+1 vs §110 14).
  AnotiaWang/awesome-jev **97★** ≠ yibie/awesome-jev **506★**.
  Qwen3.8-27B ≠ Archer.
  X MCP not used. `invented_signal: false`.
- Folded into SKILL.md (description + protocol +
  mapping-index), mental-models Apply 0646, faq,
  mixed-architecture fail table + gallery, applied-mappings,
  validation, judgment-class, composition-algebra items
  248–267, toolbox-mapping, methods-catalog, formal-methods,
  question-design, agent-self-assessment, mappings,
  CHANGELOG, README, docs/ecosystem, findings batch #94,
  sources.json. Hunches labeled. No wrapper.
  Hourly 0646 uniqueness lock: Calibration is not alpha; NO CURRENT ALPHA CANDIDATE; ΔR² approximately +0.00084; Brier 0.2131387; ECE 0.0421875; Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05; default 0.5 keeps zero non pinned; keepResult median 0.14 to 0.17; keepCall median 0.28 to 0.35; usable range is about 0.10 to 0.25; 7.8% to 57.9%; judges results it never sees; task-finish eval not built yet; $0.002 per compaction; slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench; Jev 108/120 $0.083 0.34 s; Luna SGR 114/120; paired Jev accuracy-difference intervals include zero; not evidence of equivalence; GLM SGR 26/120 93 format failures; Terra-planned Jev hybrid 55/120; rule-based by default, optionally Jev-backed; empty README; missing key cannot break the experience; prefill plus exactly one decode; softmax over A/B/C ≠ Noul; BBQ 9,053/10,000 (90.53%); ECE 0.0890; Mean confidence 0.9943; overconfident; score and noul not implemented; DGUI 12 rows (was 6); INSTRUCT 119 rows likes 2; encode the state once, decide everything in parallel; 0.740 accuracy against a 0.508 majority; ECE 0.047; fine-tune's advantage ends where its 384-token training data does; jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd; Space does not call Jev; recomputes routing from saved probabilities; 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22; synthetic repository benchmark; Jev evaluations are advisory; YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; default threshold 0.8 still soft; 40-line windows cannot prove whole function; token-native sequential start/end Choice; Gemini/Haiku stubs not configured yet; handful of hand-written examples, not a benchmark; Jev judged exactly what it was given; laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills; contract_passed is not a claim of guaranteed factual truth; Wilson lower bound 0.85 floor; fixture mode no savings claim; SemIf 2207★ (+21 vs §110 2186); jevlike 1043★ (+5 vs 1038); TypeAR 15★ (+1 vs 14); AnotiaWang 97★ (+1 vs 96); yibie/awesome-jev 506★ (+16 vs 490); Laya likes 822 (was 802); tracker likes 64 flat, lastModified UNCHANGED; do not reopen or amend PR #23/#24/#25/#26/#27/#28.

## 2026-09-20T11:41Z — hourly 0541 HIGH (Boise ~05:41 MDT)

- Fresh PR off main after merged #27 (`39d6520` / §109).
  **HARD RULE:** do not reopen or amend PR #23 or #24 or #25 or #26 or #27.
  Never reopen merged #7–**#27**. Branch
  `cursor/hourly-0541-augustus-fold-9585`.
  Skip Archer rewrite. Quote READMEs. Mark *theirs*.
  No wrappers / keys / install recipes. Do not dump
  source. 0★ HIGH still gets a real card. Size **0**
  WITH CONTENTS still gets a real card. Quote live
  REST over watch. `invented_signal: false`.
- Open-weight / RLCD / Blackwood watch: hf BlackwoodAI/blackwood-rlcd
  (likes **2**; gated **manual**; sha `3b9e29df`; Blackwood tracker ABSENT);
  anthonym21/qwen3-0.6b-rlcd-decision (sha `b327ec5e`; r = c - p_a;
  ECE 0.021; acc 0.807 vs warmup 0.746);
  larkooo/gemma-e2b-rlcd (sha `e099c730`; Independent primitive;
  11.57s vs 54.10s · 4.67× · 120/128 *theirs*;
  default path is pretrained Gemma probs not trained RLCD head);
  Meanblock/JEV-CPU (sha `759fa606`; GH Meanblock 404; lock leesk212/JEV-CPU;
  softmax over letter slots ≠ Noul);
  impacte/mimir-lfm-openjev (sha `5f9173bb`; WANLI 0.741 vs openjev v2 0.77 *theirs*;
  3-way NLI ≠ Noul);
  shreyanbr/system-one-distilled/gold/zeroshot
  (priority 0.464 = majority floor; banking77 contaminated;
  raw margins not probabilities;
  do not distill Jev as teacher of record (they distilled Haiku)).
- Measurement densifies PRIMARY: Running-Dolphins/jev-bench
  (**0★**; HEAD `67d2ee42`; size **1070**;
  “0.9 is not one number”; ranking ≠ calibration;
  banking77 0.8–0.9 stated 0.86 actual 0.73 over-confident *theirs*);
  WallerChen/jev-measured (**0★**; HEAD `4a12dfb3`;
  $0.0000153–$0.0000226 vs circulating $0.0004 (~20×);
  Score is 0..n-1 expectation not 0–1; Noul has no confidence field;
  TCP floor 198.8 ms; type reliability is not a reason to choose Jev (json_schema 5/5);
  gateway tax not one number);
  RadRebelSam/jev-decision-lab (**0★**; HEAD `e6d6d42d`; size **128**;
  Function-only 5/8 vs hybrid 8/8; 8 designed cases not conversion lift);
  jackojacko05/compare-jev-bigquery-ai-functions (**0★**; HEAD `cb9ef56b`;
  200-row pilot Jev 86.5% 173/200 vs Gemini Flash-Lite 86.0% 172/200 vs Pro 87.0% 174/200 *theirs*;
  not a ranking).
- Applied/theory: questionator (Client-side quiz; pointer from held docs; scanned-PDF warn);
  grill-jev (Jev judges / agent reasons / user decides);
  jev-lsp (pattern exact, judgement must clear floor);
  jev-spec (treating 0.85 as 85% / minProbability hard-gate as Harbor);
  Jev-LLM (VERIFY acquires discriminating evidence, never same-pool confidence-only rescoring;
  Solar writes, Jev chooses NEXT ACTION).
- Formal methods compose with scoring; a Noul is a SENSOR.
  Treating 0.9 as one number, 8/8 as conversion lift, 200-row as
  ranking, 0.85 as 85%, Score as 0–1, Noul.confidence as existing,
  json_schema gap as typed-model win, circulating $0.0004 as
  measured, 64× Space as Harbor, or minProbability 0.85 as Harbor
  is soundness theater. treating 0.85 as 85% / minProbability
  hard-gate as Harbor, 0.9 as one number, and 8/8 as conversion
  lift are the anti-patterns.
- Pulse (do not invent): Archer still promised_not_landed. Hub
  archerhume/4rcherhume HTTP **401**. Tracker likes **64**;
  lastModified `2026-09-20T04:29:16.000Z` **UNCHANGED**.
  Laya present (likes **793**); Blackwood ABSENT. Live REST:
  SemIf **2186★** (+20 vs §109 2166); jevlike **1038★**
  (+1 vs §109 1031); TypeAR **14★** flat vs §109.
  AnotiaWang/awesome-jev **96★** ≠ yibie/awesome-jev **490★**.
  Qwen3.8-27B ≠ Archer.
  X MCP not used. `invented_signal: false`.
- Folded into SKILL.md (description + protocol +
  mapping-index), mental-models Apply 0541, faq,
  mixed-architecture fail table + gallery, applied-mappings,
  validation, judgment-class, composition-algebra items
  226–247, toolbox-mapping, methods-catalog, formal-methods,
  question-design, agent-self-assessment, mappings,
  CHANGELOG, README, docs/ecosystem, findings batch #93,
  sources.json. Hunches labeled. No wrapper.

## 2026-09-20T10:39Z — hourly 0439 HIGH (Boise ~04:39 MDT)

- Fresh PR off main after merged #26 (`58a05ab` / §108).
  **HARD RULE:** do not reopen or amend PR #23 or #24 or #25 or #26.
  Never reopen merged #7–**#26**. Branch
  `cursor/hourly-0439-augustus-fold-7118`.
  Skip Archer rewrite. Quote READMEs. Mark *theirs*.
  No wrappers / keys / install recipes. Do not dump
  source. 0★ HIGH still gets a real card. Size **0**
  WITH CONTENTS still gets a real card. Quote live
  REST over watch. `invented_signal: false`.
- Open reproduction densifies: hf kushalpatil/jevify-gemma4-26b-a4b
  (likes **0**; sha `d4c0d1d4`; Hub jevify merged LoRA ships weights;
  PAWS 0.580/ece 0.288 is the weak cell; GH kushalpatil07/jevify 404);
  26b-a4b-lora (sha `ec4a3d22`; LoRA adapter twin not independent eval);
  e4b (sha `a6b5a716`; smaller E4B slightly better OOD ECE than 26B-A4B);
  e4b-lora (sha `cca1f55e`; E4B LoRA stub card);
  NicolaiMTLassen/bonzi-8b-v1-jev (sha `588bc44e`; WANLI-256 64.5%; rank #4 of 6);
  bonzi-1.7b-v1-jev (sha `48148bf9`; WANLI-256 52.0%; rank #6 of 6);
  bonzi-4b-v1-jev (sha `d5545084`; WANLI-256 60.2%; rank #5 of 6);
  roadius2/ultra_laya (**0★**; HEAD `0dff5bd2`; roadus2 watch misspelling;
  ultra_laya REVIEW defects; default branch claude/laya-jev-review-gg5ppo).
- Measurement densifies PRIMARY: AHTOOOXA/jev-cyrillic-audit
  (**0★**; HEAD `7167894a`; size **1302**;
  XNLI EN 88.3% ECE 0.032 → RU 77.3% ECE 0.096;
  Δ −11.0 pp [−14.2,−7.8]; ECE +0.063;
  MASSIVE no detectable difference at n=600;
  confidence is function of p_max (r=1.000));
  JulesHuisman/jev-eval (**0★**; HEAD `96c2a110`;
  JulesHuisman/jev-eval scaffolding / README SHA c356a584 (was empty e69de29b));
  tunahansahin897/what-is-jev (**0★**; HEAD `71d53be2`;
  947 repos scored; A 273 / B 302 / C 372; LLM rubric ≠ benches);
  Mishkun/judge-jev (**0★**; HEAD `1bf495d3`; judge-jev 0.5 still soft).
- Applied class placements: LiuHao-1443/jev-table-tennis (**1★**;
  7 bands 6/10 vs 40 bands 0/10); laguagu/jev-evidence-lab
  (32/32 synthetic is smoke not production); hemanth/hfjev;
  akash-kamat/jev-llm (pointer-not-generator 400 human-authored responses);
  chenmingtang830/jevgraph (proposed ≠ authorized;
  gated 100% (95/95) coverage 59.375%); Towow-ai/jpp
  (J++ composable semantic computation language);
  whyashthakker/awesome-jev-use-cases (No benchmark winner is claimed);
  dog-last/awesome-jev (phishing 5-atomic + LR 95.0% *theirs*);
  shinshin86/jev-aituber-tension-sample (AITuber tension ±15);
  shinpr/jev-reranker (README npm global; repo is Rust);
  AHTOOOXA/git-confess (httpx exhibit 11% (13/119) *theirs*);
  waterme7on/jev-paper-trader (90d trend +12.40% vs random +12.75% vs BH +41.71%;
  5m win rate 25%).
- Formal methods compose with scoring; a Noul is a SENSOR.
  Treating WANLI-256 as Harbor, LoRA stubs as independent eval,
  jevify n=307 ECE as a hard gate, 32/32 as production, 0.8
  evidence as proof, 40-band 0/10 without 7-band, /judge 0.5
  as truth, git-confess 11% as a person verdict, paper-trader
  +12.40% as edge, Awesomejev 656/38160 as eval, tracker likes
  as Archer landing, roadus2 spelling, or jevgraph 100% gated
  as production is soundness theater. jevify ECE 0.061 as a
  hard gate, 0.8 evidence as proof, and paper-trader fills as
  edge are the anti-patterns.
- Pulse (do not invent): Archer still promised_not_landed. Hub
  archerhume/4rcherhume HTTP **401**. Tracker likes **64**;
  lastModified `2026-09-20T04:29:16.000Z` **UNCHANGED**.
  Laya present (likes **783**); Blackwood ABSENT. Live REST:
  SemIf **2166★** (+38 vs §108 2128); jevlike **1031★**
  (+5 vs §108 1026); TypeAR **14★** (+2 vs §108 12).
  AnotiaWang/awesome-jev **95★** ≠ Awesomejev 656 entries /
  38,160 stars (was 561/27007). Qwen3.8-27B ≠ Archer.
  X MCP not used. `invented_signal: false`.
- Folded into SKILL.md (description + protocol +
  mapping-index), mental-models Apply 0439, faq,
  mixed-architecture fail table + gallery, applied-mappings,
  validation, judgment-class, composition-algebra items
  202–225, toolbox-mapping, methods-catalog, formal-methods,
  question-design, agent-self-assessment, mappings,
  CHANGELOG, README, docs/ecosystem, findings batch #92,
  sources.json. Hunches labeled. No wrapper.

## 2026-09-20 ~14:10 UTC — user-provided HIGH Merve Noyan ZS classifier lineage
- Docs-only on a **fresh PR off main** (`cursor/merve-zeroshot-classifier-signal-f943`).
  After merged #29 (`a9c8b61`, hourly 0646 / `notes.md` §111).
  **HARD RULE:** do not reopen or amend PR #23 or #24 or #25
  or #26 or #27 or #28 or #29.
- X MCP **WAS** used. Parent 2101463303734067592: likes **421** /
  impressions **35498** / RTs 23 / bookmarks 89 / replies 30 /
  quotes 3; created 2026-09-20T00:07:49Z; note_tweet full text.
  Follow-up 2101592535835529527: likes **189** / impressions **9613**
  / RTs 22 / bookmarks 138; created 2026-09-20T08:41:20Z.
  Author @mervenoyann merve 92246 followers. Maziyar quoted
  2101158867455320127 likes 446 / impressions 87625.
- Hub likes locked where cited: MoritzLaurer/deberta-v3-large-zeroshot-v2.0
  **139**; MoritzLaurer/ModernBERT-large-zeroshot-v2.0 **72**.
  facebook/bart-large-mnli **1616** is Hub widget default, **not**
  Merve’s pick (not cited as recommendation). answerdotai/ModernBERT-large
  **487** is MLM backbone.
- Folded into `notes.md` §112, SKILL.md (description uniqueness +
  protocol triggers + mapping index), mental-models Apply 0806, faq,
  mixed-architecture fail table + gallery, applied-mappings,
  validation, judgment-class, composition-algebra items 268–272,
  toolbox-mapping, methods-catalog, formal-methods, question-design,
  agent-self-assessment, mappings, CHANGELOG, README, docs/ecosystem,
  findings batch #95, sources.json. Hunches labeled. No wrapper.
- Quote *theirs*. Do not invent accuracy numbers.
  `invented_signal: false`. Do **not** merge from this review.
- Review REST relock (adversarial gate, live X still moving): parent likes **421** /
  impressions **35498** / RTs 23 / bookmarks 89 / replies 30 / quotes 3;
  follow-up likes **189** / impressions **9613** / RTs 22 / bookmarks 138;
  Maziyar likes **446** / impressions **87625**. Hub likes **139** / **72**
  unchanged. bart-large-mnli **1616** unchanged. Uniqueness fragments
  likes 421 / 189; impressions 35498 / 9613.
- User-provided 0806 uniqueness lock: people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 421 / 189; impressions 35498 / 9613; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29.

## 2026-09-20 ~14:43 UTC — hourly 0843 HIGH measurement / judgment
- Docs + evaluator on a **fresh PR off main** (`cursor/hourly-0843-augustus-fold-220d`).
  Rebased onto latest `main` after merged #31 (0743, `notes.md` §113 /
  items 273–288 / batch #96), #32 (`486e93e`, Release v0.4.0), #33
  (README map), and #34 (Pages layout). **HARD RULE:** do not reopen or amend PR
  #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34.
  Do **not** reply into the finished 0743 agent. Do **not** reopen or
  amend merged #31. Merged #31 owns `notes.md` §113 / items 273–288 /
  batch #96 — leave it alone. This fold: `notes.md` §114 / items 289–302 /
  batch #97.
- PRIMARY: VladUZH/jev-calibration (instruct-tuning honesty collapse; No Jev API was called;
  Qwen2.5 ≠ Archer); rlaope/jeval (equal-width vs quantile ECE 0.113 vs 0.076; drift M2 not
  implemented); dnakhoa/jev-deferred-crispification (calibration does not compose; hop-ECE
  permutation-invariant; 25–60× headline withdrawn; Deferred Crispification; Qwen 3.8 sparring ≠ Archer).
- Rename densify: g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev (same GitHub id 1378007307).
- Evaluator: equal-width vs quantile ECE, ranking≠calibration (AUC=1 ECE>0.2), hysteresis enter/exit,
  hop-ECE permutation invariance, cost-optimal threshold. uniqueness_gate.py.
- Pulse: SemIf 2237★ (+30 vs §111 2207); jevlike 1049★ (+6 vs 1043); TypeLLM/TypeLLM 16★;
  AnotiaWang 98★; yibie/awesome-jev 520★ (+14 vs 506); Laya likes 861 (was 822);
  tracker likes 66 (+2 vs 64) lastModified UNCHANGED; Blackwood likes 2 gated manual;
  Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401.
- Folded into `notes.md` §114, SKILL.md (description uniqueness + protocol triggers +
  mapping index), mental-models Apply 0843, faq, mixed-architecture fail table,
  applied-mappings, validation, judgment-class, composition-algebra items 289–302,
  toolbox-mapping, methods-catalog, formal-methods, formal-semi-formal, question-design,
  agent-self-assessment, mappings, CHANGELOG Unreleased, changelog-hourly, README,
  docs/ecosystem, findings batch #97, sources.json. Hunches labeled. No wrapper.
- Quote *theirs*. Do not invent accuracy numbers. `invented_signal: false`.
  Do **not** merge from this fold agent.


Hourly 0843 uniqueness lock: A hunch is a probability with a policy attached; { enter: 0.8, exit: 0.6 } is hysteresis; replay a policy change without inference; Decision models are providers, not the product; huncho ≠ Kungie/gut ≠ carldaws/hunch ≠ tpellet/hunch; pretrained Qwen2.5 base ECE 0.030 (0.5B) / 0.040 (7B); instruct 0.302 / 0.269; 70.9% → 70.0% mean conf 74.1% → 96.7%; temperature scaling still matches it in-distribution; No Jev API was called; Qwen2.5 ≠ Archer; Qwen/Qwen3.8-27B ≠ Archer; 学習済みモデル v0.1 は準備中です; bool AUROC 0.523; 先頭だと0件、末尾だと250件; 温度を渡さない場合、確率は較正されていません; このリポジトリには Jev を呼ぶコードが存在しません; g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev (same GitHub id 1378007307); 947 repos scored; A 273 · B 302 · C 372; LLM rubric ≠ benches; Data as of 2026-09-20; HEAD 895b9498; README SHA 3ae98c56; 13 focused checks and one mutually exclusive outcome; Probabilities are advisory, not calibrated guarantees; omni-/ask-jev ≠ pedroknigge/mcp_jev; pd.cut bins by equal width while jeval bins by quantile; ECE 0.113 and ECE 0.076; jeval drift is not implemented yet; rlaope/jeval ≠ dayhaysoos/jevals; calibration does not compose; ECE has exactly zero statistical power to detect the failure mode that kills trajectories; 25–60× headline withdrawn; P(all-correct): 0.0071 vs 0.0001; TCE / AMS; Qwen 3.8 sparring ≠ Archer; Deferred Crispification; light_cutoff_applied_to_combination 0; recorded run, kinematic animation; BANKING77 Accuracy BERT-Base 93.02 Jev 79.90; Analyse jev calibration (NLL, ECE) backlog; BERT figures are published supervised references, not zero-shot; 档位措辞效应 分数极差中位 0.50、最大 1.32; 修好后对照组是 0.01; 不是 benchmark; 概率没做 calibration; ~1,430 API calls, about $0.15; xiaohuaxi/jev-study ≠ wjdjdakf17/jev-study ≠ baekenough/jev-study; AND: product (independence assumed and recorded in the trace); chat model's stated confidence is not calibrated; circuit-vl-4b ≠ Archer; Bring your own API key; vamsikrishna2421/jev-usecases ≠ whyashthakker/awesome-jev-use-cases; catalog ≠ endorsement; SemIf 2237★ (+30 vs §111 2207); jevlike 1049★ (+6 vs 1043); TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 520★ (+14 vs 506); Laya likes 861 (was 822); tracker likes 66 (+2 vs 64) lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34; notes.md §114
