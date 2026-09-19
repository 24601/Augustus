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
  unofficial-local-as-Jev, Nemotron “not calibrated
  replacement”, and Laya confidence-without-
  competence; Augustus owns placement. Archive
  tarball SIGNAL.md for three clusters (fetched
  ~15:32–15:35 Boise). No 1541 fold PR was open
  (`gh pr list --state open` had #11 modernbert-only
  extending §93; this PR is the requested three-
  cluster §94 fold with SIGNAL name locks).
- Folded how-to-apply clusters: Compile-time System
  One / questions-as-index (byenzyme/enzyme;
  guidance ≠ hook; catalysts ≠ summaries;
  compile-time System One); unofficial JA ModernBERT
  cross-encoder (argos1111/modernbert-ja-310m-jev;
  unofficial ≠ TypeSafe; format_version
  modernbert-jev/1; Argos1111/jev_local ≠
  us/jev-local ≠ kunchenguid/local-jev); NAR class
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
