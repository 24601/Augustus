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





