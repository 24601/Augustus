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




