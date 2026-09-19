# Changelog

All notable changes to Augustus are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versioning
follows [SemVer](https://semver.org/spec/v2.0.0.html).

Each release notes the [`typesafe-ai/skills`](https://github.com/typesafe-ai/skills)
revision it was written against. That skill owns integration contracts;
Augustus owns design judgment. Re-read live TypeSafe docs before treating a
pin as current API behavior.

## [0.3.0] - 2026-09-18

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12).

### Added

- Mixed-architecture card: default placement is judgment-class model +
  generator + code, not stack replacement. Covers cost-sensitive prefilter
  (fail-open vs fail-closed per action), tool/skill routing, AGENTS.md
  preference lint, a placement gallery from the 2026-09-18 X+GH hour, and
  an explicit answer to "Jev is just classification"
- Protocol branch and mapping-index rows for those four placements
- Non-negotiable: classification is not the product; typed judgment is a
  software primitive placed beside generation
- Hourly research archive for this pass (X theme digest + `topic:jev` movers)
  under `research/archive/hourly/2026-09-18T14/`
- Research note on Laya (`convaiinnovations/laya`): open Choice/Score/Noul
  head as a self-hosted *typed judgment provider*; vendor benches labeled
  claims; TypeSafe remains the default path
- Applied-mapping cards: context sieve, exact-text keep/drop, env/harness
  triage, moderation/ranking, skill/tool routing (`applied-mappings.md`)
- FAQ card for "it's just classification", stack replacement, Jev vs open
  head, and Augustus vs neighbor how-to skills
- Judgment-class card: Augustus covers the whole class of fast/cheap
  categorization-classification-scoring models (Jev is exemplar, not
  monopoly). Families: closed decision API, open System-1 heads (Laya),
  GLiNER/GLiClass encoder family (locate vs categorize vs local
  multi-head), listwise/pairwise rankers, vision scorers.
  Species map in `judgment-class.md`; GLiNER is a peer, not a footnote.
  Fork of listwise discriminative vs decision/proper-scoring objectives;
  four vision scoring patterns; seven portents for agent architecture.
  FAQ rows for family choice, GLiNER vs GLiClass vs Jev vs cross-encoder, and
  CLIP/SigLIP gating. No invented APIs.
- Formal-methods card: judgment vs proof ownership (sensor / constraint /
  searchlight); Alloy Analyzer vs Apalache (model finder ≠ SMT BMC ≠
  inductiveness); TLA+/Quint/P/NuSMV/PRISM/Event-B; Dafny/JML/
  Frama-C/SPARK; DST trio (Antithesis hypervisor, Resonate Lean+oracle+
  SDK, PufferLib env+seed / Ocean trainer contracts); harms
  (TOCTOU-of-Noul, soundness theater, AI×FM / Hillel vibing specs);
  crossover metaphors (NATM, snap-fit, Norman gulfs, Leveson STAMP/STPA).
  Curriculum archived at `research/archive/curriculum/FORMAL-METHODS-SYSTEM-ONE.md`;
  named rows folded here. One-screen alias: `formal-semi-formal.md`.
  Non-negotiable: never launder a Noul as a proof.
- One-screen `references/formal-semi-formal.md` (curriculum 1-pager)
- Hypothesis mapping cards (do not promote without an acceptance test):
  VOI / gather; SDT/ROC; Leveson sensor≠constraint; search/control
  outside SWE; spec property pipeline; Alloy instance loop; runtime
  assurance sandwich; DST multiverse triage; durable agent control;
  assignment hybrid; situated density (`mappings.md` §6–§16)
- Input-brittleness and structural-prove ∩ remainder cards
  (`mappings.md` §17–§18): paraphrase pairs → Chow abstain; allowlist /
  text-layer first, judge leftovers (jevgate / doc-router *shapes*
  Empirical; domain-general reading Hypothesis). FAQ: GLiNER vs Jev,
  LLM-as-judge (Langfuse framing), allowlist-then-judge
- GLiGuard as an Empirical encoder peer (`judgment-class.md`,
  `notes.md` §30): one-pass safety-schema classify on GLiNER2, not a
  Jev weight clone; FAQ "is GLiGuard Jev?"; README OR/refusal
  aggregation left as existing policy-in-code. LLM I/O safety is not
  a coding-agent tool gate
- Hourly 10:07 Boise fold (`research/notes.md` §25–§26): GLiNER2.5 local
  peer; openjev-lm 92.9% / 6 vCPU teacher-distill; jevgate; doc-router
  1.74× $; pi-jev-context; jevscope next to jevals; Han Xiao trolley
  (listwise ≠ decide); James Ward dual orchestration; JevLint
- Constrained-AR surface, not a sixth species (`judgment-class.md`):
  TypeAR puts a typed interface on a pretrained generator (next-token
  constraint ≠ proper-scoring head). Archer Hume's open-weight drop
  stays **Watch** (`research/notes.md` §31, §32)
- Hourly ~11:02 Boise fold (`research/notes.md` §33): Archer
  clarifications still Watch (27B dense one-forward-pass, multimodal
  generalization report, AU healthcare residency not anti-TypeSafe,
  prefers "decision models"); when-to-use table (proprietary Jev vs
  Archer vs TypeAR vs encoder DeBERTa vs LoRA distill); HF novel
  (jev-gate-student-b 148k corpus, jp-sns-jev7 ONNX, open-jev-deberta,
  mini-jev-runs 27.9k logits, jev-tree-choice-cap); device/harness
  (jev-mobile MCP, jev-macos-loop, jev-harness, routeKit); HacksonClark
  SREGym-Lite 20/50→24/50 — rank tests, do not diagnose
- Hourly ~11:59 Boise fold (`research/notes.md` §42): Archer still
  Watch. Three open paths (encoder / AR constrained decode / trained
  decision-only). Native constrained serving
  ([pcdServer](https://github.com/stephanj/pcdServer), TypeAR-class,
  2–256 enums, Apple+Linux GGUF). Meta-VOI hook
  (typesafe-jev-tools 149-row: Haiku more accurate, Jev confidence
  monotonic). jev-mode latency-class split (token ratio durable;
  accuracy is parity). OpenSmoke env-break vs policy-break +
  pre-mortem. jevql store-as-decision-surface. jot topology B with a
  closed catalog. openevals online full-traffic. hermes north-star
  two-layer finish gate. pi-jev (not pi-jev-context). jev-plays-games
  option-order probe. joxide jump-by-description. laya-typed-decisions
  companion packaging. No wrapper.
- Hourly ~12:58 Boise fold (`research/notes.md` §44): Archer still
  Watch (no architecture rewrite). Store-index fork: in-engine
  ([sqlite-jev](https://github.com/mgaitan/sqlite-jev), pg-jev cousin)
  vs CLI rewrite (jevql). Soft judgment inside a hard envelope
  ([bitrate-advisor](https://github.com/affirmitv/bitrate-advisor);
  mmalisper JOB planner +12% geomean, author-reported; join-order
  Choice alone was 2× slower). Distill-to-device as a *memory* gate
  (jev-gate, already §33). Encoder vs decoder open-replica receipts
  (openjev-lm $0/call overnight CPU). jev-harness as Harbor-adjacent
  practice (assert on action). Host adapter
  ([jev-routing](https://github.com/nekowasabi/jev-routing), not MCP);
  OpenClaw typed routing ([jev-claw](https://github.com/trietphan/jev-claw)).
  Voice-control and JevML are README stubs. Higgsfield auto-routing is
  a claim. No wrapper.
- kev (`jaredpalmer/kev`, `research/notes.md` §45): runnable Archer
  reconstruction on the trained decision-only open path next to Laya /
  Nimble / Watch. Qwen2.5-0.5B LoRA + pointer, Apache-2.0, `POST
  /v1/systemone` drop-in. Isolation exact (packed vs separate max Δ
  3.7e-6; secret-in-sibling p=0.03 vs in-state 0.99). Held-out ECE
  0.065 (0.031 after temp scale); acc 0.799 on 1,350 ID questions.
  Permute argmax flips 7.4%; IIA log-odds shift mean 0.13; boundary
  forgery held. Laptop-local System One for development/eval; not a
  knowledge/frontier substitute; not a Jev teacher-copy. Contrast vs
  TypeAR, encoder DeBERTa, proprietary Jev. jevals/Harbor bake-off
  candidate. No serve how-to.
- Hourly ~14:03 Boise fold (`research/notes.md` §46): Archer still
  Watch. Open multimodal RLCD
  ([blackwood-rlcd](https://huggingface.co/BlackwoodAI/blackwood-rlcd),
  CC BY-NC): screenshot + marked candidates → Choice; web acc 0.907 vs
  Jev 1.13 text-only 0.480; letter-shuffle 0.133 vs 0.587; ECE 0.037;
  ~200 ms H100; Jev still leads general text 0.850 vs 0.786. Shared
  bake-off ([open-jev-laya-bench](https://huggingface.co/datasets/pngwn/open-jev-laya-bench)):
  26+9 tasks, 11959 items; ECE/NLL/Brier; macro acc Δ +0.023
  neutral / +0.229 home; LLM-as-judge is not the score. Decision-token
  QLoRA
  ([Foodoo1/Qwen3-14B-RLCD-Decision-LoRA](https://huggingface.co/Foodoo1/Qwen3-14B-RLCD-Decision-LoRA)):
  fraud_risk 64→95%, overall 85.2→98.8% at ~234 ms/4-field broadcast;
  synthetic. jevgate frame: allowlist *proves*, Jev judges only
  unlisted, fail-open. wellposed: missing `other` → confidence 1.00
  wrong; gating cannot catch it (`tenbin` owns the lint skill).
  S1 reflex keeps control (jev-reflex-autonomy-lab). MED:
  jev-decision-layer, jev-e2e, jevpandas. No wrapper.
- Abide (`coldteadotai/abide`, `research/notes.md` §47): productized
  Jev preference lint for Claude Code / Codex / OpenCode. Soft
  AGENTS.md / CLAUDE.md rules → one Score per rule on the diff (never
  the conversation); hard rules stay with the linter (same layering
  family as jevgate). Edit- vs turn-phase observation window; banded
  confidence (≥0.8 repair / 0.5–0.8 note / <0.5 silence — their
  operating point) + fail-open hooks; rubric.json quotes source
  lines; calibrate/tune fix false positives in the question. Replay
  of 93 sessions (1,256 edits / 147 turns) with independent review:
  edit precision ~26%, turn ~73% (author-reported, before tune).
  Fuller productized path of the jev-pref contract. Complementary to
  rh-guard (eval-integrity vs project soft rules). Text/diff only —
  not multimodal. No hook how-to.
- kev delta (`research/notes.md` §45): Hub weights
  [`jaredpalmer/kev-0.5b`](https://huggingface.co/jaredpalmer/kev-0.5b);
  `--run` accepts Hub ids; PEFT `task_type=FEATURE_EXTRACTION` (publish
  patches legacy adapters). HIGH question-design: confront Choice
  `"other"` / none-of-the-above as a wrong alternative too, vary
  wording, dedicated `none_of_the_above` eval (no published rates).
  Cross-link wellposed request-shape lint. No species change. No
  wrapper.
- Hourly ~14:52 Boise fold (`research/notes.md` §48): Archer still
  Watch. Extractive selection + offline `redecide`
  ([testimonial-miner](https://github.com/AppitStudio/testimonial-miner));
  pointer-not-generator
  ([jev-reviewer](https://github.com/choxos/jev-reviewer)). Local
  `/v1/systemone` drop-in ([jev-local](https://github.com/us/jev-local);
  default scorer is a stub until `hf`). Observe→decide→verified-act,
  no screenshots ([solari-reflex](https://github.com/hitakshiA/solari-reflex);
  60.2/194.9, 66/460, 24.2/98.4 s vs Codex on Solari). Dataframe
  accessor sibling ([jevframe](https://github.com/ktaletsk/jevframe);
  note jevpandas). Route ≠ memory (jev-hermes). Advisory sidecar
  (agent-workflow-typesafe-ai). Structure induction (dag-jev experiment).
  Decision-for-control / generator-for-content (jev-agentworld-web-simulator).
  Collab arms + Wilson/McNemar (jev-testbench). AST ∩ semantic (jevscan;
  `tenbin` owns lint). Light Pi gate (pi-jev-approver). Laya ONNX port
  ([laya-onnx](https://huggingface.co/Mattepiu/laya-onnx); do not copy
  vs-Jev table). Spotcheck: SemIf 1551★; jevlike 866★; tracker
  20:12:57Z still lists Laya, not Blackwood. No wrapper.
- Hourly ~15:52 Boise fold (`research/notes.md` §49): Archer still
  Watch. X discourse blocked. Boundary map / extractable-from-state
  ([jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas);
  history suite A wrong@0.90 / B 0.07 / C right@0.97; component node;
  dangerous-high ECE; DOM-as-text + fan-out). Harbor-style bake-off vs
  constrained LLMs
  ([DMB](https://github.com/nibzard/decision-model-benchmark) v2: jev
  banking 76.3% / spam 93.0% / 256+ cap; p50 264–276 ms; $0.07/1k; no
  class wins on quality). Feedstock
  ([jevals-data](https://github.com/Jevals/jevals-data) CC-BY-4.0;
  recompute-from-logs; 2026-09-18 board). Dual-process S1 decide / S2
  generate ([dual-process-ai](https://github.com/taro1985/dual-process-ai);
  routing accuracy unmeasured). Combinatorial ≠ extractive (ARC-AGI
  Direct Jev 4/400). Packed one-forward open LLM
  ([open-alternative-jev](https://github.com/ikermoel/open-alternative-jev)
  RACE-H 92.9% @ 4.55 q/s; not a Jev reproduction). Tiny SAN local
  surface ([von](https://github.com/wfzyx/von) 14 MB; not a replica).
  kev light delta **100★**. Do not merge Banking77 87% / 76.3% /
  79.67%. No wrapper.
- GLiNER2.5 extractive compaction (`research/notes.md` §50,
  [gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction),
  Apache-2.0): architecture notes, not a plugin how-to. Pointer
  keep-drop (character-offset copies) vs generator summarizers;
  family with testimonial-miner / jev-reviewer. Soft retention Choice
  under a hard mutation envelope (mutating tools / shell operators →
  `keep_full`); low-confidence / invalid evidence fail closed to
  `keep_full` — contrast many fail-open Jev gates. Same compaction
  *job* as fast-jev-compaction / pi-jev-compaction; GLiNER encoder
  backend; Fastino/GLiGuard sibling class. `shadowMode` default true.
  Not Jev. Not multimodal. No invented metrics.
- CI merge-gate / fail-open wake VOI / S1 indexer / claim-evidence
  (`research/notes.md` §51): architecture notes, not a plugin how-to.
  [latch](https://github.com/CaseReed/latch) cluster-then-policy
  PASS/BLOCK (pair Harbor + rh-guard).
  [wakegate](https://github.com/shitianfang/wakegate) skip only if
  p(wake)<0.2 (21/21 smoke). s1-graphify-indexer GLiNER extract +
  escalate-S2 (10–50× unfilled).
  [clear-head](https://github.com/VladyslavHontar/clear-head)
  claims vs session evidence.
  reification-labs/foreman description-only Phoenix scaffold (not the
  super-jev loop).
  [jev-gateway-bench](https://github.com/vinilana/jev-gateway-bench)
  Harbor on/off one-run signal.
  jev-marshal Watch/empty; jevons bounded Pi supervisor (shadow
  recovery). MED: if-ai, omp-auto-mode, downloads-sorter, label-desk,
  herdr-jev. Archer still Watch. No invented metrics. No wrapper.
- GLiNER2 Ultrafast observe→score→act (`research/notes.md` §52,
  [gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast),
  MIT): architecture notes, not a browser-agent how-to. Same
  observe→score-among-candidates→code-acts *job* as jev-ultrafast /
  solari-reflex; local GLiNER2 (`fastino/gliner2-multi-v1`) backend,
  not GLiNER2.5. No screenshots; no generated selectors; code owns
  actuators. Hybrid local decide + remote fill (Mercury 2.5 default
  for TYPE). `DONE` ≠ verified success. Contrast blackwood-rlcd
  screenshot multimodal; laya-mind2web is DOM-index Laya (same
  observed-candidate family). Fastino sibling class with
  gliner25-compaction (different hole) and GLiGuard (safety schema).
  Demo (theirs, not re-run): Flights 12.20 s / 13.785 s / ~$0.0001
  API — demonstration, not a bake-off. No invented metrics.
- jev-pruner evidence-preserving Bash stdout prune (`research/notes.md`
  §53, [jev-pruner](https://github.com/tamaratran/jev-pruner), MIT):
  architecture notes, not a plugin how-to. After Bash, Jev Noul-prunes
  stdout chunks before the main LLM sees them — no summary. Hard
  envelope (≤10k estimated tokens / JSON-diff-whole-doc untouched)
  then soft Noul; fail-safe keep original; full archive. Marketplace
  id still `fast-jev-output`. Codex is opt-in wrapper, not automatic
  interception. Same evidence-preserving *family* as
  fast-jev-compaction and gliner25-compaction; different *job*
  (command output vs session memory) and Jev backend vs GLiNER2.5.
  Manual sweep (theirs): needles 24/24; mean reduction 83% on trim
  scenarios. Harbor plugin-eval cannot reach Jev. Terminal-Bench
  paired pilot is integration, not a full bench. No invented metrics.
- Cua-S1 specialist System One computer-use (`research/notes.md` §54,
  [cua-s1](https://github.com/trycua/cua/tree/main/libs/cua-s1),
  parent MIT, ~23.3k★ this pass): architecture notes, not a Driver /
  MCP / `uv` how-to. Form-oriented profile `cua-s1-form-v0`. Byte
  encoder + option-attention head chooses fill/check/click/skip per
  observed element; does not generate values or selectors. Plan ≠
  execute; dry-run default; `execute`/`submit` independent opt-ins;
  fail-closed on unknown checkbox / fill without advertised token
  `set_value`. **Not TypeSafe Jev** — parallel "System One" naming in
  CUA research. Same observe→score-among-candidates→code-acts *job*
  as jev-ultrafast / gliner2-ultrafast / solari-reflex / laya-mind2web;
  specialist form contract, source-only this pass (no weights, no
  checkpoint scores). Offline metric *names* only (accuracy,
  abstention, coverage, wrong actions/targets, unsafe when should
  abstain). Tests exercise implementation, not checkpoint quality.
  Watch for a `cua-s1-form-v0` artifact drop. No invented metrics.
- Hourly ~17:48 Boise fold (`research/notes.md` §55): Archer still
  Watch. X MCP flap; `since_id` not advanced. Architecture notes, not
  a how-to. Local CUDA/PyTorch Choice/Score/Noul replica
  ([jevify](https://github.com/Mintzs/jevify); uncalibrated
  likelihoods ≠ Noul; no LICENSE this pass; independent of
  Distillation). Decision-native RAG
  ([decision-native-rag-skills](https://github.com/emergency-lee/decision-native-rag-skills);
  retrieve wide → decide → evidence set; no bundled harness; no
  universal benchmark). Verbatim session ledger + scored recall
  ([carryforward](https://github.com/Dharundp6/jev-carryforward);
  rules never judged; fail-open dump; 9×3 hint). Judgment as a
  Ruby language primitive ([hunch](https://github.com/carldaws/hunch);
  English-as-config; `rescue nil` fail-open at save). Healthcare
  Harbor-shaped S1+S2
  ([explore-typesafe-ai](https://github.com/si618/explore-typesafe-ai);
  synthetic FHIR; not clinically validated). Pre-registered
  independent eval
  ([jev-baselines-eval](https://github.com/ickma2311/jev-baselines-eval);
  **both AMBIGUOUS**; cascade sign-flip at exact parity;
  confidence=1.0 theater; encoder-with-labels wins; serving-path ≠
  model-speed; same-day errata ×3). Student-b light delta only (HF
  card unchanged). MED: toolgate (pre-exec allow/block/review; Jev
  not authorization), typesafe-screening-mcp (PubMed screening aid),
  databricks-jev-pdf-lab (**honest negative**; no OSS license),
  yannip1234/codex-jev (extractive compression family; equal
  accuracy/lower cost not established), kazuhideoki/jev-search
  (recursive *file* search + fzf; **not** superagents-lab web
  search). No wrapper. No invented metrics.
- Hourly ~18:38 Boise 2026-09-18 / 00:38 UTC 2026-09-19 fold
  (`research/notes.md` §56): Archer still Watch. Architecture
  notes, not a plugin / showcase catalog. Classify-first MCP
  ([jev-sift](https://github.com/kbhuw/jev-sift); batch path/url/text
  → Jev without entering main agent context first; 50 / 60k / 2MB /
  public-IP envelope; mocks ≠ accuracy; no LICENSE this pass;
  topology A MCP, not jev-routing). Living applied-mappings atlas
  ([jevable.com](https://jevable.com/); claimed 342 vs JSON-LD first
  page 36; class patterns — intent columns, score-among-observed,
  VOI gates, generative UI decide, robotics text-state, draft-gate
  silence ≠ safer — not a 342-title hit list). Maker clocks stay
  claims unless already a named receipt. No wrapper. No invented
  metrics.
- Stagehand experimental Jev stack (`research/notes.md` §57,
  [#2955](https://github.com/browserbase/stagehand/pull/2955) 5/5 of
  #2951–#2955, all OPEN draft): architecture notes, not an SDK
  how-to. Major harness productization of
  observe→score-among-candidates→code-acts (cousins jev-ultrafast /
  gliner2-ultrafast / cua-s1 / solari). Jev picks a11y elements;
  code copies text. extract `"off"` | `"judge"` | `"pick"`. Their
  card (gemini-3.8-flash, 25×3): **37/75** no-LLM ~0.5 s vs baseline
  **4.37 s**; 69/75 vs 23/25 (92% both); LLM-off **36/75** — pick is
  a fast path, not a replacement. Screenshot extract always LLM.
  Cache-check errors never block replay. Do not merge clocks. No
  invented metrics.
- Hourly ~18:46 Boise 2026-09-18 / 00:46 UTC 2026-09-19 fold
  (`research/notes.md` §58): Archer still Watch. Architecture
  notes, not a Convex / uv / pnpm catalog. Public judgment wall
  ([ask-jev-ai](https://github.com/waynesutton/ask-jev-ai); 6
  parallel questions; policy-in-code; cost-to-1M from tokens;
  license null). Meaning-search without embeddings
  ([jevgrep](https://github.com/Bentlybro/jevgrep); 79% top-5 vs
  BM25 40% / grep 20% on stripped repos; keyword still wins exact
  strings). PR attention ≠ correctness
  ([egma-ai/jev-reviewer](https://github.com/egma-ai/jev-reviewer);
  **not** choxos pointer-not-generator). Skills→oxlint
  ([jev-oxlint](https://github.com/cephalization/jev-oxlint);
  AST prove ∩ remainder; Phoenix fixtures; not a hard gate;
  `tenbin` owns lint). Session-sticky first-prompt routing
  ([jev-adaptive-thinking](https://github.com/jxu-dev-c/jev-adaptive-thinking);
  fail-closed fallback). Measured RAG rerank
  ([Jev-RAG](https://github.com/Max-sm-yc/Jev-RAG); one-run ≥70%
  cost / 72% latency vs Spark *rerank*; full-context Spark still
  faster). MED: safe-sh, jev-loan-triage, TurboGuo arenas, jevbox;
  hermes/mcp packs not found this pass. No wrapper. No invented
  metrics.
- Hourly ~19:48 Boise 2026-09-18 / 01:48 UTC 2026-09-19 fold
  (`research/notes.md` §59): Archer still Watch. Architecture
  notes, not a pip / venv / Cloudflare catalog. Capability kernel
  ([interlock](https://github.com/somoore/interlock); LLM ring 3 /
  kernel ring 0; secrets never in the agent; Jev SENSOR;
  `policy.py` BLOCK/ASK/ALLOW; type-safe ≠ correct; distinct from
  toolgate). Typed control plane around DSPy
  ([jev-dspy-control-plane](https://github.com/manikanda-kumar/jev-dspy-control-plane);
  DSPy drafts AFTER route+action; OpenJEV / DSPy / JSON Schema
  share ontology; offline heuristic ≠ quality). Native-probability
  calibration arena
  ([jev-arena](https://github.com/meetr1912/jev-arena); live 145
  noul Brier 0.0059 / ECE 0.0620 *theirs*; overconfident in low
  bins; 2-request fan-out) plus sonar (heatmap-as-policy) /
  vickrey (Jev never bids) / bracket (Brier vs Elo; live trailed
  Elo). Engine owns truth / Jev owns judgment
  ([game-coach](https://github.com/JoelLewis/game-coach); Wave 0
  PRD; Stockfish WASM; GPL-3.0; anti-soundness-theater with egma).
  Human-confirmed port cleanup
  ([port-cleanup](https://github.com/epiphany-dynamics/port-cleanup);
  Jev recommends; human is the only kill trigger; identity
  re-check; shields; mapped explanations). MED toolbelt:
  jev-pr-labeler, jevcumber, typedecide, jevon, dsh-jev,
  fast-jev-compaction-pi, jev-tetris-benchmark, modelsystem,
  opencode-system-one, browser-ai, semantic-bookmark. Skip
  jef-mcp (parody) and jevregist (account farming). Star spike:
  SemIf 1491→1606 (this pass 1607); jevlike 851→896 (this pass
  897). No wrapper. No invented metrics.
- Hourly ~20:43 Boise 2026-09-18 / 02:43 UTC 2026-09-19 fold
  (`research/notes.md` §60): Archer still Watch. Architecture
  notes, not a uv / bun / Modal catalog. Domain LoRA specialist
  vs few-shot hosted
  ([Domain-jev-maker](https://github.com/help-er/Domain-jev-maker);
  independent CLINC gold, not a Jev teacher-copy;
  matched-precision KL 0.168 vs 0.580 banking; few-shot
  determinate McNemar n.s.; train when downstream reads p).
  Decide→policy→LLM leftover cascade
  ([jav-email-cascade](https://github.com/skiingfalcon/jav-email-cascade);
  jev vs gen-json vs gen-logprob; Noul 0.5 never rounded;
  license null; mock gen-json flat-confidence is *their mock*).
  ORDER BY ranking family
  ([jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench);
  six gates pass; Score ordinal 0.143 weak link; 53-way 0.99
  tie; calibration ≠ sortable; recodelabs batch-40 fails
  ranking). Wire-compat GLiFormer backend
  ([jeff](https://github.com/logan-markewich/jeff); typesafe-sdk
  drop-in; ~$2.6 vs $15.6 L4 HTTP ~6×; A10G direct ~$0.65 ~24×;
  AG News 75.5% vs 90.5%; CPU more expensive; license null; not
  a Jev replica). MED: loopback gateway
  ([sysone](https://github.com/hraness/sysone); hosted + local
  OpenJev/NanoJev/Mini-Jev; no weights; credential from env).
  No wrapper. No invented metrics.
- Hourly ~21:39 Boise 2026-09-18 / 03:39 UTC 2026-09-19 fold
  (`research/notes.md` §61): Archer still Watch. Architecture
  notes, not a pip / npm / bun catalog. Active-learning triage
  ([jev-triage](https://github.com/ThyFriendlyFox/jev-triage);
  accept / expensive teacher / human; log full distributions;
  **do not distill Jev as teacher of record**, ~68% ceiling).
  Evidence-packet explorer
  ([jev-semantic-explorer](https://github.com/jimmyhealer/jev-semantic-explorer)
  / jevex; index-once ask-many; 1/8→6/8 SWE-bench Verified
  finish n=8 *theirs*; packet HitFile 0.233 diagnostic).
  Meaning-grep
  ([jev-semgrep](https://github.com/uehaj/jev-semgrep); AND/OR/NOT
  line Nouls; JP↔EN; MIT LICENSE / GitHub NOASSERTION; 0.94/0.98
  *theirs*). Closed-vote CU
  ([JevOnly](https://github.com/buluoray/JevOnly); no planner LLM;
  11 steps / 43 calls / ~$0.014 / 17 s *theirs*). Harbor Jev vs
  local MLX PCD vs AR JSON
  ([system-one-benchmark](https://github.com/mallahyari/system-one-benchmark);
  toxic-chat n=50; Jev 84.0% / Brier 0.1096 vs PCD 52% / 0.3884;
  O(1) ≠ calibrated Noul; license null). Host-owned product
  ([waymode](https://github.com/mossburgh/waymode); app retains
  handlers/permissions; 24/26 + 34/36 *theirs*; not a
  self-driving proof). OMP/pi fail-open gates
  ([omp-jev-extensions](https://github.com/luw2007/omp-jev-extensions);
  `jev_acceptance_gate` + `jev_route`; contrast pi-jev-approver
  fail-closed). Skip empty jev-compactor / laya-jolt. No wrapper.
  No invented metrics.
- Hourly ~22:38 Boise 2026-09-18 / 04:38 UTC 2026-09-19 fold
  (`research/notes.md` §62): Archer still Watch. Architecture
  notes, not an `omp plugin` / pip catalog. Watch archive path
  missing on this VM; receipts from live GitHub. Permission vs
  probability
  ([omp-greenlight](https://github.com/SemetricLabs/omp-greenlight);
  1,013 calls / 10 sessions; default **40.9%** prompts removed /
  **0 of 94** unsafe auto-approvals on labelled corpus; operator
  owns thresholds; plugin never self-tunes; not a sandbox; host
  deny stays above). Judgment ≠ permission
  ([skill-broker](https://github.com/adamjralph/skill-broker);
  Hermes pre-agent outline; code owns grants; Jev never grants
  access; **not a production recipe**). Eval integrity /
  instrument-not-score
  ([dinostomp](https://github.com/collapseindex/dinostomp);
  FINDINGS 189 / 99 against itself; `dinostomp jev` if-statement
  hygiene; ECE 0.062 *theirs* on 24 examples; beside jevals, not
  a Harbor taskset). MED: fast-jev-opencode, jev-desktop,
  jev-agent-integration, sift, JevExplore. Census: Awesomejev
  488/21644; SemIf 1641 (+13); jevlike 905 (+4); tracker likes
  41 (+1); Laya yes; Blackwood ABSENT; X MCP flapping
  (`pages_archived` 0). No wrapper. No invented metrics.
- Hourly ~23:40 Boise 2026-09-18 / 05:40 UTC 2026-09-19 fold
  (`research/notes.md` §63): Archer still Watch. Architecture
  notes, not a uvicorn / bun / marketplace catalog. Watch
  archive path missing on this VM; receipts from live GitHub +
  HF. Hunches labeled. Constrained optimizer + S1 features
  ([slo-router](https://github.com/zeeshan8281/slo-router);
  license null; Jev task/exactness/evidence as features, never
  the sole hot-path gate; fail-open local features; same
  routes/accuracy; p95 **77.93 → 490.38 ms** *theirs*; eight-row
  demo is not a benchmark). Privilege ≠ verdict
  ([construct-auto-classifier](https://github.com/godspede/construct-auto-classifier);
  Apache-2.0; effect-based shell gate; fast-allow/deny then Jev
  Choice + independent risk Nouls; fail-closed; Jev **0**
  dangerous / 975; every chat model leaked 16–104; operator-owned
  dials). Attention filter / VOI for human review
  ([jev-lens](https://github.com/rashedInt32/jev-lens) +
  [jev-lens.nvim](https://github.com/rashedInt32/jev-lens.nvim);
  never blocks the agent; never edits; never green unless sure).
  MED: [sysone-help/sysone](https://github.com/sysone-help/sysone)
  (evaluation-model-first TS SDK; **not** hraness/sysone gateway);
  [INSTRUCT_JEV](https://huggingface.co/datasets/ctaxnagomi/INSTRUCT_JEV)
  (119 rows; 47/51/21; jevals seed);
  [swift-jev](https://github.com/ckaik/swift-jev) (LICENSE-only
  this pass; not a CLI product). Census: Awesomejev 488/21644;
  SemIf **1652** (+11); tracker likes **42** (+1); lastModified
  unchanged; Laya yes; Blackwood ABSENT; X MCP flapping. No
  wrapper. No invented metrics.
- Hourly ~00:39 Boise 2026-09-19 / 06:39 UTC fold
  (`research/notes.md` §64): Archer still Watch. Architecture
  notes, not a uvx / pnpm / marketplace catalog. Watch
  archive path missing on this VM; receipts from live GitHub.
  Hunches labeled. Measurement owns endorsement
  ([jev-packs](https://github.com/dtduc-git/jev-packs);
  CC0; nine packs `verified` *theirs* on pinned
  `jev-1.13.0`; accuracy/ECE/cost/latency; `unknown`
  mandatory; named runner jevassert **not released** / 404;
  packs without evidence stay `provisional`). Jev supplies
  evidence, code owns authority
  ([actiongate-jev](https://github.com/omkarghugarkar007/actiongate-jev);
  Apache-2.0; deterministic policy owns ALLOW|REVIEW|BLOCK;
  positive score never overrides a hard security fail;
  fail-closed financial/destructive/credential if Jev is
  down; 500-case is label-baseline, not accuracy). Ranking ≠
  calibration
  ([does-jev-confidence-mean-anything](https://github.com/Adilmp/does-jev-confidence-mean-anything)
  + [jevcal](https://github.com/Adilmp/jevcal); 8,000
  human-annotated judgments; AUC **~0.91**; stated **~75%**
  vs human **~10%**; two-parameter recalibration removes
  **~96% ECE** without changing rank; never hard-threshold
  raw p as a frequency; vendor "calibrated" often means
  rank-correlation). MED:
  [gqgs/laya-onnx](https://github.com/gqgs/laya-onnx)
  (complete Laya→browser int8; distinct from Mattepiu);
  [kunchenguid/local-jev](https://github.com/kunchenguid/local-jev)
  (ModernBERT local approximation — not equivalence). Do
  not re-fold sysone-help/sysone. Census: Awesomejev
  488/21644; SemIf **1660** (+8); jevlike **910** (+5);
  TypeAR 9; tracker likes 42; lastModified unchanged; Laya
  yes; Blackwood ABSENT; X MCP flapping. No wrapper. No
  invented metrics.
- Same-hour remainder ~00:39 Boise 2026-09-19 (`research/notes.md`
  §65): Archer still Watch. Do not re-fold actiongate / jev-packs
  / sysone-help. Hot-click CU
  ([ego-jev](https://github.com/jiangkoumo/ego-jev); MIT; indexed
  viewport table → operation+target; code owns observe/execute/
  `--until`; text model only for type; HN 4.9 s vs 9.7 s / wiki
  5.4 s vs 10.1 s *theirs* n=3, high variance, not a bench).
  Jev judges relevance, code decides structure
  ([jev-compactor](https://github.com/edwardyen724-g/jev-compactor);
  MIT; was empty skip §61; never rewrite; regex floor; compaction
  fail-open if Jev down, safety fail-closed; 64.5% / 366 ms /
  $0.0004 / 0 invented paths / 4 of 4 facts vs Sonnet summary
  96.2% / 1 invented path, one session). Local rules first,
  never auto-train on the model's own hides
  ([x-reply-filter](https://github.com/zhuyansen/x-reply-filter);
  MIT; `rules.js` then batched Nouls; confirm-queue). OpenCode
  port already §62: fast-jev-opencode. Census as §64. No wrapper.
  No invented metrics.
- Hourly ~01:47 Boise 2026-09-19 (`research/notes.md` §66): Archer
  still Watch. Three clusters: **control-plane combinators**
  ([decision-combinators](https://github.com/voidning/decision-combinators);
  Then/Gate/Vote/Cascade/Weighted; not literal AND/OR; not chat
  turns) + **skill VOI**
  ([skillranker](https://github.com/Dicklesworthstone/skillranker);
  52★; two-pass + none-of-these; hook **fail-open** — corrects
  §7 fail-closed); **eval integrity without leaderboard theater**
  ([jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas)
  10★ receipts, type-safe ≠ correct, axis already §49;
  [jev-frontier-100](https://github.com/softpudding/jev-frontier-100)
  Jev 77.0% vs Qwen3.5 4B/2048 96.7% / 4B off 56.0%, exploratory;
  [jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)
  900 tickets ECE 0.107 = 4.4× floor, Choice/Score T~3.3 vs
  boolean T 0.66, unknowable priority mean p 0.74); **gate
  doctrine clone**
  ([turnstile](https://github.com/zyphr-labs/turnstile); Apache-2.0;
  policy first, Jev remainder, replay; missing Jev → Review);
  **MLX one-pass replica economics**
  ([jevmlx](https://github.com/bnsd55/jevmlx); 28★; softmax ≠
  Noul; no local leaderboard yet). MED: invalidate (0 of 157
  false invalidations), jev-intent-review (under construction),
  prune-review (22-run cost 1.18% with 305% outlier). Census not
  re-derived. No wrapper. No invented metrics.
- Hourly ~02:38 Boise 2026-09-19 (`research/notes.md` §67): Archer
  still Watch. Do not re-fold the 01:47 list except sibling
  contrast. **TLA+ compose with judgment**
  ([jev-labs](https://github.com/copyleftdev/jev-labs); MIT;
  never confidently wrong; 1,080 golden 0 wrong *theirs* under
  chaos, escalate 5%→18% severe; TLC 1,049,750 states / 0
  errors; synthetic, not clinical). **Advance/coverage ledger**
  ([seal](https://github.com/Reasonofmoon/seal); MIT; no seal,
  no advance; coverage.path auto|code|human|escalate; mint ≠
  product brain). **skill-broker sibling** (outline already
  §62; grants in code vs turnstile runtime vs skillranker
  advisory). **Sureness**
  ([how-sure-is-jev](https://github.com/adarc8/how-sure-is-jev);
  MIT; Choice confidence = max_prob; 75/25 → 0.5 vs entropy
  0.19). **JevBench v1.1**
  ([jevbench](https://github.com/fstandhartinger/jevbench);
  MIT; unofficial; Main Score 0.6/0.2/0.2; Jev 1.13.0 **87.6**;
  calibration reported not scored). **CI typed gate**
  ([ci-gatekeeper-bot-jev](https://github.com/NemanjaManic/ci-gatekeeper-bot-jev);
  package.json MIT / GitHub SPDX null; 504–629 ms *theirs*).
  **Codex MCP adapter**
  ([jev-in-codex](https://github.com/teempai/jev-in-codex);
  MIT; ranking unbenchmarked; lexical fallback). Census:
  SemIf **1683** (+11); jevlike **923** (+5); tracker likes
  **43** (+1); Awesomejev 488/21644 unchanged. No wrapper. No
  invented metrics.
- Hourly ~03:38 Boise 2026-09-19 (`research/notes.md` §68): Archer
  still Watch. Do not re-fold the 02:38 list except sibling
  contrast. **Judgment as attention redirect, not a merge
  blocker**
  ([jev-preflight](https://github.com/muse0509/jev-preflight);
  Go MIT; eight risk axes; assist=one reinspect; fail-open;
  uncalibrated 0.85; owner-run Claude Code 2.1.267: no-key
  fail-open PASS, key-enabled exactly one continuation).
  **Landed-script trust / headless≠auto-approve**
  ([construct-auto-classifier](https://github.com/godspede/construct-auto-classifier)
  delta; cert still Jev **0** dangerous / 975; $0.047/1k).
  **Jev judges relevance; code decides structure**
  ([jev-compactor](https://github.com/edwardyen724-g/jev-compactor)
  product-arm **73%** / 350 ms / 4 of 4 *theirs*; 30–250×
  cheaper than shipped summarizers; §65 64.5% is vs-Sonnet).
  **Compress-before-first-send**
  ([dizk/jev-lens](https://github.com/dizk/jev-lens); MIT;
  79% fewer tokens / 500 SWE-rebench; post-send prune +17%
  cost; distinct from rashedInt32/jev-lens). **tools≠use**
  ([jev-carryforward](https://github.com/Dharundp6/jev-carryforward)
  0/4 recall; SessionStart > hoping). **Observational
  memory**
  ([pi-observational-memory-jev](https://github.com/willfish/pi-observational-memory-jev);
  keep/kind verbatim; model-free compact). **Independent
  open-Jev class**
  ([openvons](https://github.com/genai-craft/openvons);
  Apache-2.0 LICENSE / GitHub SPDX NOASSERTION; 7★; JevPick
  3.2–4.8×; `/v1/systemone` wire-compat ≠ replica).
  **Physical-world S1**
  ([HA-Jev](https://github.com/AboveColin/HA-Jev); MIT;
  **17★**; sensors from typed answers; not for
  locks/heaters). **Judgment outside the store**
  ([jevql](https://github.com/kylemclaren/jevql); CLI
  judges; vanilla Postgres never sees `jev()`). Short
  consumer bullet: [sift](https://github.com/bohutang/sift)
  ~$0.00003/post. Census: Awesomejev **561** (+73, agent
  tooling 87→107); SemIf **1704**. No wrapper. No invented
  metrics.
- Hourly ~04:39 Boise 2026-09-19 (`research/notes.md` §69): Archer
  still Watch. Do not re-fold the 03:38 list except sibling
  contrast / combinators rename. **Digital-design combinators**
  ([jev-combinators](https://github.com/voidning/jev-combinators)
  is the rename of decision-combinators; extended Router /
  Loop / Retry / Fallback / Memory; metaphor ≠ literal AND/OR).
  **VOI cache admission**
  ([jevcache](https://github.com/kushals256/jevcache); MIT;
  same-intent skip LLM; n=100 *theirs* 0 FP / precision 1 /
  recall 0.38 / fpr 0 vs Jaccard@0.35 fpr 0.48; fail-open).
  **Harbor skill-routing harness**
  ([pi-jev-skill-bench](https://github.com/iamdin/pi-jev-skill-bench)
  + [pi-jev-skill-suggestion](https://github.com/iamdin/pi-jev-skill-suggestion);
  BM25 vs Jev at roster 50–500; 43 gold; no live numbers this
  pass; no-key no-op; tool mode is tools≠use cousin).
  **Zeroshot vs BERT displacement**
  ([jev-zeroshot-vs-bert](https://github.com/zhuyansen/jev-zeroshot-vs-bert);
  +0.05–+0.13 vs DeBERTa-c; contamination 0.901 vs `-c` 0.763;
  ≈230 / >2048 labels; DiD 0.035 vs 0.112 *theirs*).
  **Typed escalate/continue/abort baton**
  ([jev-handoff](https://github.com/shitianfang/jev-handoff);
  MIT; inverted loop; gate never grants; fail-open; Vercel
  drops confidence). **Worth-your-attention VOI**
  ([ThinkyMiner/Winnow](https://github.com/ThinkyMiner/Winnow);
  MIT; 80%/90% *theirs*; **≠** kevinpita/winnow).
  **Jev WHETHER / Python HOW / LLM WHAT**
  ([hermes-jev-router](https://github.com/rsdkrasen/hermes-jev-router);
  license null; community plugin; skip-next needs core patch).
  **Conflict ≠ ignorance**
  ([jev-typed-evaluation-collapse](https://github.com/mleyvaz/jev-typed-evaluation-collapse);
  Noul collapses; named Choice p=1.0; binary red 0.67–0.85
  *theirs*). **Playwright executes, Jev chooses**
  ([browser-jev](https://github.com/DowLucas/browser-jev);
  license null; sample-from-distribution). **Local class**
  ([OpenJev](https://github.com/IamBusy/OpenJev) Apache-2.0
  `/v1/decide` 45/60 *theirs*, not TypeSafe drop-in, ≠
  hraness/sysone runners;
  [semif-serve](https://github.com/dddanielliu/semif-serve)
  1164 vs 178 ms; runoff ≠ softmax; wire-compat ≠ replica).
  Toolbelt notes: jev-security-scan / jev-decisions / TeoMastro
  (summary.md 404 this pass); **rh-guard owns reward-hack**.
  Flywheel:
  [DGUI_HYPERMEM-JEV](https://huggingface.co/datasets/ctaxnagomi/DGUI_HYPERMEM-JEV)
  6-row schema. Census: Awesomejev **flat 561/27007**; tracker
  likes **43→45**; SemIf **1714** (+10); jevlike **926** (+3).
  No wrapper. No invented metrics.
- Hourly ~05:46 Boise 2026-09-19 (`research/notes.md` §70): Archer
  still Watch. Do not re-fold §50–§69 HIGH except sibling
  contrast / jevassert landing / prune-review, intent-review,
  laya-jolt, local-jev deltas. **Record/replay CI LANDED**
  ([jevassert](https://github.com/dtduc-git/jevassert);
  Apache-2.0; accuracy/ECE/Brier/cost/latency offline from
  recordings; exit 0/1/2; McNemar; Action `@v0`).
  **Evidence-gated packs now have a runner**
  ([jev-packs](https://github.com/dtduc-git/jev-packs);
  size 0→458; 2,990-case matrix *theirs*: Jev/Sonnet 5
  accuracy tie Δ≤0.018, Jev better calibrated 7/9, ~250×
  cheaper; sms-spam this-pass 0.953/ECE 0.040).
  **Failure-finding arena**
  ([jevarena](https://github.com/chenmingtang830/jevarena);
  Apache-2.0; **≠** meetr1912/jev-arena; harness not findings).
  **BBQ stereotype/uncertainty/cost**
  ([jev-bbq-experiment](https://github.com/simonmesmith/jev-bbq-experiment);
  license null; 58,492; 97.28%; bias 0.04/0.34; $0.3429 /
  7.75 min *theirs*; not a general bias cert).
  **Decider ≠ executor**
  ([jeffrey](https://github.com/thomasbrueggemann/jeffrey);
  MIT; Jev next-tool/progress/risk/done; LLM fills args;
  pick ≠ fill). **Sentence-as-rule lint**
  ([jevlint](https://github.com/mizchi/jevlint); MIT;
  ast-grep × `ask:`; 13/15 1.00/1.00 *theirs*; **≠**
  huntedman/JevLint). **VOI hunk prune**
  ([prune-review](https://github.com/shubhangi013/prune-review);
  22-run 1.18% with 305% outlier; ~20% target; cost not
  quality). **Whole-repo intent**
  ([jev-intent-review](https://github.com/yottayoshida/jev-intent-review);
  VERIFIED/VIOLATION/UNKNOWN; empty search ≠ proof).
  **GLiNER2 System One spec**
  ([Jev_from_GLiNER2](https://github.com/Eran-BA/Jev_from_GLiNER2);
  spec-only; ≠ jeff). **Open replica substrates**
  ([grande](https://github.com/bokuweb/grande) JGLUE 0.614/
  0.853 + 270M 0.710/0.710 *theirs*;
  [laya-jolt](https://github.com/jlt-commons/laya-jolt)
  byte parity; [JEV-CPU](https://github.com/leesk212/JEV-CPU)
  PoC, Meanblock 404; [local-jev](https://github.com/kunchenguid/local-jev)
  done 30%/shape 57%). **Persist constraints**
  ([pi-heed](https://github.com/Nyarlathoteppppp/pi-heed);
  98.5%/0 false block *theirs*). Toolbelt note:
  actiongate slogan already §64. MED:
  [system-one-responsible-ai](https://github.com/david-j-lustig/system-one-responsible-ai)
  size-0 framing stub. Census not re-derived. No wrapper.
  No invented metrics.
- Hourly ~06:43 Boise 2026-09-19 (`research/notes.md` §71): Archer
  still Watch. Do not re-fold §50–§70 HIGH except sibling
  contrast. **Harbor SGR-judge contract**
  ([jev-judge-bench](https://github.com/slavadubrov/jev-judge-bench);
  README MIT / GitHub SPDX NOASSERTION; frozen SLA-150; Jev vs
  Luna / DeepSeek-flash / glm-5.3-flash; invalid = FN;
  21 offline tests; canaries ≠ quality; **no quality headline
  yet**; **≠** jevarena / jevbench). **Empty skip**
  ([jev-context-pruner](https://github.com/IPECTER/jev-context-pruner);
  409 empty). **Hand no-text steps**
  ([jev-use](https://github.com/shitianfang/jev-use); MIT
  v0.4.1; p50 220 ms; 186 vs 2,672 ms; gate 12/12; Vercel
  drops confidence → margin 0.4; first loop 17/20 then 0/20
  *theirs*; **≠** jev-ultrafast). **Pi System-One control
  plane** ([pi-jev-control](https://github.com/goodruizhan/pi-jev-control);
  license null; v0.3.0 private; GUI never force-click;
  compaction never writes session). **Never free-generates**
  ([jev-gpt](https://github.com/florian-hoenicke/jev-gpt);
  license null; ~400 calls / 75 s / 2¢ *theirs*).
  **OpenRouter recipe atlas**
  ([jev-cookbook](https://github.com/nexibeo/jev-cookbook);
  MIT; 1★; 16–36 samples not benches; 425 calls / $0.015;
  browser 5/6 *theirs*). **Personal-history feed**
  ([jevfeed](https://github.com/fengyiqicoder/jevfeed); MIT;
  no social graph; one request per batch of ten).
  **Competing NAR claim-audit, not endorsement**
  ([openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0);
  README Apache-2.0 / GitHub SPDX NOASSERTION; 77.10%/0.0636/
  0.0144 *theirs* unverified; **open PR #1**: throughput≠
  latency, Laya parity, like-for-like ECE; **≠**
  IamBusy/OpenJev). Census not re-derived. No wrapper. No
  invented metrics.
- Hourly ~07:49 Boise 2026-09-19 (`research/notes.md` §72): Archer
  still Watch. Do not re-fold §50–§71 HIGH except sibling
  contrast. **1-token logprob endpoint ≠ Noul**
  ([chakuho](https://github.com/taku-me/chakuho); MIT;
  coverage ≠ correctness; GUI 336 *theirs* 27B 95%/92%
  vs Jev 89%/82%; `__none__` 97% vs 8B 10%). **Open
  replica engine** ([jevinf](https://github.com/zerodegress/jevinf);
  MIT; 2.57×/2.27× 100% argmax; MPS only). **Unofficial
  Elixir SDK ≠ OTP peer**
  ([typesafe-elixir-sdk](https://github.com/phiat/typesafe-elixir-sdk);
  MIT; 1★; ≠ dannote/jev). **jevex rename + n=16 VOI**
  ([jevex](https://github.com/jimmyhealer/jevex); 160s→69s
  / $8.74→$3.13 / 16/16 *theirs*; keep n=8 1/8→6/8).
  **Commit attention≠verdict**
  ([commitjev](https://github.com/yodablocks/commitjev);
  MIT; middle band never rounded; 0 false on 5 clean
  *theirs*). **Hermes plugin is Agnes not TypeSafe**
  ([hermes-plugin-jev](https://github.com/Mrmimee/hermes-plugin-jev)).
  **Pi compact ≠ compaction**
  ([pi-jev-compact](https://github.com/dev-willbird1936/pi-jev-compact);
  MIT). **Empty skip**
  ([jev-runway](https://github.com/IPECTER/jev-runway);
  LICENSE-only). **Decision-native inbox**
  ([mailordinal](https://github.com/Milo318/mailordinal);
  MIT). **Unofficial jev-cli not ready**
  ([jev-cli](https://github.com/shaharia-lab/jev-cli);
  0.0.0; ≠ jevql). **Laya multilingual**
  ([laya-multilingual](https://huggingface.co/convaiinnovations/laya-multilingual);
  MASSIVE 0.366/0.387; Khmer 0.000@0.952; ships
  uncalibrated). **Schema-scorer Hub** (GitHub 404; v2
  Choice 0.841; peaked ranking). HF 401 this pass on
  open-jev-laya-bench / jev-tree-choice-cap /
  INSTRUCT_JEV; jevlogs 404+401. Census not re-derived.
  No wrapper. No invented metrics.
- User-provided signal ~08:37 Boise 2026-09-19
  (`research/notes.md` §73): **Skip Archer.**
  **Productized System One HTTP**
  ([classifier-dev](https://github.com/mrmps/classifier-dev);
  MIT; **185★**; https://classifier.dev). Label +
  calibrated confidence as the public contract; batch
  `{id,text}[]` ~1000; Jev primary, LLM fallback only.
  400 headlines **650 ms** *theirs*. **Escalate-under-
  threshold:** smart re-asks single-label <0.7;
  multi-label ignores (re-judge worse, 23 s). Emotion
  ≥0.9 → 82% / <0.5 → 29%; gemini-3.8-flash 87.5→90.0 /
  61.8→63.7 *theirs*. Multi-label F1 **0.887** / **230 ms**
  vs cascade **0.799** / 1.5 s (eval 232 ms; AG News
  **87.7%** vs 82.0%). **Measurement-first:** `/benchmark`
  from tracked JSON; read eval/README (n=7 train-on-test;
  ~0.03 coin flip). **Silent FALLBACK:** granite F1
  **0.546** vs advertised ~**0.800** *theirs*; rh-guard
  owns the gate. Life/business (spam/inbox/feedback),
  not SWE-only. Distinct from ask-jev-ai wall. No wrapper.
  No invented metrics.
- User-provided signal ~08:48 Boise 2026-09-19
  (`research/notes.md` §74): **Skip Archer.** **Delta of
  §48.** Pointer-not-generator at evidence-synthesis
  scale
  ([choxos/jev-reviewer](https://github.com/choxos/jev-reviewer);
  MIT; **12★**; https://jevreviewer.xera.ac). **≠**
  [egma-ai/jev-reviewer](https://github.com/egma-ai/jev-reviewer).
  Two-pass Choice (which line) + Noul (does this line
  itself answer); quotes = Noul ≥ 0.5 *theirs*. *Not
  found* / *Unclear* first-class. Human tick is the
  product (checked never overwritten). 18-q template
  **4.6 s / $0.0101** *theirs* (spot check, not a
  validation study). Cochrane / PRISMA / RoB, not
  SWE-only. No wrapper. No invented metrics.
- User-provided signal ~08:56 Boise 2026-09-19
  (`research/notes.md` §75): **Skip Archer.**
  **Wire-compat ≠ logit-equiv**
  ([githubnext/localjev](https://github.com/githubnext/localjev);
  MIT; **261★**; GitHub Next). **≠**
  [kunchenguid/local-jev](https://github.com/kunchenguid/local-jev).
  Bun `POST /v1/systemone` on DiffusionGemma via Chat
  Completions; TypeSafe SDK drop-in. Prompted JSON →
  validate/retry → normalize + entropy confidence — not
  razorback16 structured-read logits. Harbor-shaped
  bake-off *theirs*: 1,200 req; Qwen3.6 short macro
  **76.7%**; Gemma 4 26B-A4B **75.0%**; DiffusionGemma
  **74.2%**; no definitive winner (2/120); do not treat
  as calibrated. LM Studio still cannot load
  DiffusionGemma. Do not copy bun / `.env`. No wrapper.
  No invented metrics.
- User-provided signal ~09:07 Boise 2026-09-19
  (`research/notes.md` §76): **Skip Archer.** **Laya
  packaging, not a new species**
  ([NandhaKishorM/laya](https://github.com/NandhaKishorM/laya);
  Apache-2.0; **710★**). PyPI + `Router` over Hub
  [`laya`](https://huggingface.co/convaiinnovations/laya) /
  [`laya-multilingual`](https://huggingface.co/convaiinnovations/laya-multilingual) /
  [`laya-typed-decisions`](https://huggingface.co/convaiinnovations/laya-typed-decisions).
  **≠** TypeSafe `/v1/systemone`. **≠** githubnext/localjev.
  T4 *theirs*: 1q **32.8 ms** (~7.8× vs Jev p50
  236–276 ms). Post-T ECE **0.081** vs Jev **0.246**;
  raw ECE still trails (0.213 vs 0.144). Banking77
  **0.425** vs Jev **0.870** (77 vs 72; ~3–4 tok/label).
  typed-decisions **0.766** is a fine-tune (base
  0.362/0.342 vs majority 0.461). Soft-acc 0.471 vs
  0.580. Khmer **0.000@0.952** — Router because gating
  cannot catch. 0.85 still soft. Jev rows third-party
  unpublished-here. Do not copy pip / preload. No
  wrapper. No invented metrics.
- User-provided signal ~09:14 Boise 2026-09-19
  (`research/notes.md` §77): **Skip Archer.** **External
  openjev census ≠ scored bake-off**
  ([@airesearch12](https://x.com/airesearch12/status/2101259522933186879);
  Florian S / Benchmark Heaven). Named ~18 (system-one-open,
  openjev-sglang, DeBERTa open-jev, Needle 3,
  open-alternative-jev, Nimble 9B, SemIf, open-jev Dasein /
  JoshuaSP, OpenJev razorback16, mini-jev, system-one,
  system-one-gemma, jevlike, AlexWortega/openjev, GLiNER2,
  Succinct Router 14M, jev-model-router/Director/Loki).
  GLiNER2 + routers are **class-boundary**. Incomplete vs
  Laya / localjev / kev / TypeAR / openvons. Engagement
  **ephemeral** (SIGNAL ~417/9/3; this pass 564/15/5). **≠**
  jevbench v1.1. Watch
  [jev-models](https://benchmarkheaven.com/jev-models); do
  not paste live ranks. Do not copy Stripe. No wrapper. No
  invented metrics.
- User-provided signal ~09:24 Boise 2026-09-19
  (`research/notes.md` §78): **Skip Archer.** **JevBench v1.2
  scored board**
  ([benchmarkheaven.com/jev-models](https://benchmarkheaven.com/jev-models);
  harness [fstandhartinger/jevbench](https://github.com/fstandhartinger/jevbench)
  MIT; 0★; HEAD `27ed3d6c`). Protocol `jevbench::v1.2`; scored
  19 Sept 2026; 534 decisions (hard 220 = 30% of Intelligence).
  Official Score = geometric mean of I/C/S/K at 25% each. Jev
  1.13.0 **75.3**; SemIf (Qwen3.5-4B) **74.6** (−0.7); OpenJev
  DiffusionGemma (razorback16) 67.6 *theirs*. Luna Intelligence
  **96.8** rank **#7** on cost. Calibration **on** the rank
  (delta from v1.1). Weighting is a product design. Option-order
  72%→21%. Self-host latency ×2 is an assumption; many costs
  est. Laya absent (gap, not named-excluded). GLiNER2 mapping
  issues; apps out. Qwen3.8 27B Chutes TEE **≠** Archer. **≠**
  tweet census §77 **≠** v1.1 87.6. Do not copy Stripe / CLI.
  No wrapper. No invented metrics.
- Hourly System One watch ~08:42 Boise 2026-09-19
  (`research/notes.md` §79): **Skip Archer.** Named HIGHs
  **already folded** (§73–§78) — extract **how-to-apply**,
  not a hit list: wire-compat ≠ logit-equiv (prompted JSON
  ≠ structured logit); productize label+p and mark
  `FALLBACK`; packaging ≠ new species / script-before-p /
  0.85 still soft; pointer-not-generator (two-pass; *Not
  found*; human tick); external census ≠ scored bake-off /
  geo-mean weights are a design. **Skip thin noise**
  (JEValuate / jevspeak / fable-jev; jev-semgrep already
  §61). Hard-gating a Noul as a PR/quality gate is
  soundness theater
  ([totally-tim/jev-gate](https://github.com/totally-tim/jev-gate)
  0★ ≠ jev-gateway; [claude-jev-warden](https://github.com/connectedGraph/claude-jev-warden)
  1★).   Qwen3.8 27B ≠ Archer. No wrapper. No invented
  metrics.
- User-provided HIGH ~09:50 Boise 2026-09-19
  (`research/notes.md` §80): **Skip Archer.** Delta of
  §46, not a new species.
  [khordoo/jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab)
  (TypeScript; **7★**; license null; README SHA
  `130987c9`; ARCHITECTURE SHA `48da0769`; HEAD
  `e3297ebe`). S1 never stalls waiting; S2 is one-use
  advisory and never flies. Purple confidence =
  **consumed** S2 (purple bar = arrival; red = fail).
  Local controller is rule-based **≠**
  githubnext/localjev **≠** kunchenguid/local-jev.
  Live API `POST /v1/systemone` `jev-latest`; 20%
  starting gate *theirs* still soft and does not start
  a mission. Seed = geometry ≠ async replay. No pixels
  to either provider; confidence ≠ selected
  probability; S2 never grants. README GLM 5.3 vs
  ARCHITECTURE muse-spark-1.3-contributor — quote both
  *theirs*. Experimental viz, not a flight controller.
  Do not copy npm / `.dev.vars`. No wrapper. No
  invented metrics.
- User-provided HIGH ~09:51 Boise 2026-09-19
  (`research/notes.md` §81): **Skip Archer.** Productized
  observe→score-among-candidates→code-acts on a Mac,
  not a new species.
  [awlevin/typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)
  (Python; MIT; **427★**; README SHA `369f4a6a`; HEAD
  `cc7b5066`). OCR+AX → numbered items → TypeSafe
  Choices (`kind`/`item`/`site`/`offscreen`) →
  deterministic click/type. **Never ships a screenshot
  to frontier for the *decision***; the one-shot
  **answer** writer may receive the capture (reader
  packet, not the Choice). Writer only for free text.
  Overlapping options = false low confidence. AX bonus
  never sole (Spotify 0 *theirs*). Post-type Noul 0.5
  and `--min-confidence` 0.4 still soft. $0.0002 vs
  Opus $0.032 (155×) *theirs* on **one screenshot**,
  not a Harbor taskset. Honest caveat: dates.py rebuilds
  pixel-free reasoning. **≠** jev-ultrafast **≠**
  cua-s1 **≠** jev-macos-loop **≠** camoufox. Do not
  copy `uv sync` / `.env`. No wrapper. No invented
  metrics.
- User-provided HIGH ~10:01 Boise 2026-09-19
  (`research/notes.md` §82): **Skip Archer.** Productized
  ASR observe→score-among-candidates→code-acts in
  headed Chromium, not a new species and not omni.
  [moritzkremb/jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)
  (JavaScript; MIT; **103★**; README SHA `fa033303`;
  HEAD `054db0f3`). Web Speech partials → one 9–11-
  question Jev request (~250–350 ms *theirs*) →
  policy. Pointer-not-generator for spans. Closed-set
  may act on a partial; free-text waits. Spoken
  confirm is convenience, not auth. Numbered overlay,
  no second model. Integration 27/27 / ~$0.0002/call
  *theirs* fixtures, not a Harbor taskset. 0.5 / 0.55
  / 0.6 still soft. **≠** jev-voice-control **≠**
  nikolas-j **≠** Aj1905 **≠** typesafe-computer-use
  OCR. Do not copy `npm` / `.env` / `run.sh`. No
  wrapper. No invented metrics. Expand the §39 tweet;
  do not re-card it.
- User-provided HIGH ~10:20 Boise 2026-09-19
  (`research/notes.md` §83–§84): **Skip Archer.** Two
  signals, one fold.
  [reddpy/AgentGhost](https://github.com/reddpy/AgentGhost)
  (TypeScript; MIT; **2★**; README SHA `44145fa9`;
  HEAD `ac04e4fb`). Intent-aware ALLOW/ASK/DENY
  wrap-as-execution: the wrap *is* the tool function;
  rules first; ASK throws; `failMode: closed`. Judge
  is a slot. Provider-hosted tools out of reach.
  **≠** jwen5419807/agentghost **≠** vventirozos
  **≠** actiongate **≠** toolgate **≠** jev-use.
  rh-guard owns the gate cousin. Do not copy `npm` /
  `.env` / `AUTO_APPROVE`. [@studio_yebisu JP genre
  atlas](https://x.com/studio_yebisu/status/2101065176069886152)
  (2026-09-18T21:45:48Z). Apps by hole, not a scored
  bake-off. Stars research-time (typesafe-computer-use
  203→**427**; jev-voice-browser 40→**103**). Not
  verified evals. Engagement ephemeral (this pass
  131,234 / 1,934 / 192). SAM 3.1 already §39.
  OpenRouter Jev no-waitlist is WATCH, not a recipe.
  **≠** @airesearch12 class census **≠** v1.2 board.
  Do not dump the 30 repos. No wrapper. No invented
  metrics.
- User-provided HIGH ~10:25 Boise 2026-09-19
  (`research/notes.md` §85): **Skip Archer.** External
  pedagogy / how-to-apply, not a new species.
  [@akshay_pachaar “Jev Clearly Explained”](https://x.com/akshay_pachaar/status/2101037514945597645)
  (article https://x.com/i/article/2100940576741093376;
  2026-09-18T19:55:53Z). LLM hammer for bounded
  decisions; code owns branches; parallel questions;
  thresholds in code; **schema-safe ≠ correct**;
  placements = routing / tool-risk / verify with LLM;
  shadow-mode; questions-as-code. **200× / 400×** and
  70–500 ms / $0.042/MTok are TypeSafe **ceiling**
  claims *theirs*, not Harbor. Text-only; not looking
  at the screen. **≠** official docs **≠** Flavio
  Copes **≠** LangChain harness **≠** AgentGhost.
  Engagement ephemeral (this pass 233,495 / 2,280 /
  235). Do not copy the Python samples. No wrapper.
  No invented metrics.
- User-provided HIGH ~10:30 Boise 2026-09-19
  (`research/notes.md` §86): **Skip Archer.** Dedicated
  fold of [uehaj/jev-semgrep](https://github.com/uehaj/jev-semgrep)
  (light-noted §61). Grep by meaning via Jev Noul;
  proposition ≠ embedding; contrast-set (all six
  about a refund; only customer-*asking* pass);
  AND/OR/NOT are boolean ops on *thresholded* bits
  (do not multiply p; ≠ jev-combinators metaphor).
  Cross-lingual; no index; EN safer near threshold.
  Semgrep.dev SAST name collision. **Not a gate**
  (ranking fail-open; rh-guard skip). LICENSE MIT /
  GitHub NOASSERTION. HEAD `21120e9`; README SHA
  `923e6a5`. Stars ephemeral (0 → SIGNAL ★42 → **51**
  this pass). 0.94/0.98 LLM-as-judge 10×51 *theirs*,
  not Harbor. **≠** jevgrep **≠** jev-sift **≠**
  jevex **≠** semgrep.dev. Do not copy npm / `npx` /
  `.env` / marketplace. No wrapper. No invented
  metrics.
- Hourly 1047 HIGH + deferred 0945 backlog
  (`research/notes.md` §87): **Skip Archer.** Docs-only
  off main (PR #2 merged). How-to-apply / mental
  models / architecture / Harbor-jevals — not
  SWE-only. Formal methods compose with scoring; a
  Noul is a SENSOR; hard-gating as test/PR/HA
  write/authorship is soundness theater. Ten
  clusters: decision-validated UI
  ([gram-render](https://github.com/wei-b0/gram-render)
  never authors text;
  [jev2ui](https://github.com/dglazkov/jev2ui) Jev
  decides / Gemini writes);
  decision-as-assert
  ([jevtest](https://github.com/realZachi/jevtest)
  ambiguous band 0.15–0.85; 0.85 still soft);
  hybrid S1
  ([anima3](https://github.com/hulryung-uo/anima3)
  Qwen logprob default; jeff confidently flat; do
  **not** invent Laya);
  pointer search
  ([JevFind](https://github.com/Peu77/JevFind));
  Harbor trio
  ([jev-frontier-bench](https://github.com/manjunathshiva/jev-frontier-bench)
  72.5%/ECE 0.161 vs Fable 84%/0.064 *theirs*;
  ChaosNLI JS worse than uniform; **≠**
  frontier-100;
  [jev-gliclass-bench](https://github.com/JoeSlain/jev-gliclass-bench)
  product bakeoff 78/40/49;
  [job-posting-triage](https://github.com/geckguy/job-posting-triage)
  majority floor 0.947 / tfidf wins / calibration ≠
  discrimination);
  authorship named escape (not evidence);
  non-SWE
  ([ha-switchboard](https://github.com/grayslawson/ha-switchboard)
  HA remains execution **≠** HA-Jev;
  [n8n-nodes-jev](https://github.com/vibe-with-me-tools/n8n-nodes-jev)
  unofficial Low Confidence);
  compaction delta
  ([fast-jev-compaction-pi](https://github.com/zaycruz/fast-jev-compaction-pi)
  **≠** pi-jev-compact **≠** pi-jev-compaction;
  ~50× *theirs*);
  full-distribution optimizer
  ([jevloop](https://huggingface.co/spaces/async-dime/jevloop)
  UCB1+CEM; no LLM in the loop; mock default);
  deferred class
  ([laya-vision](https://huggingface.co/thaitea/laya-vision-smolvlm-256m)
  SmolVLM; `score` untrained; **≠** blackwood **≠**
  Archer;
  [Cerebellum-2B](https://github.com/mkeco/Cerebellum-2B)
  `/v1/decide` ≠ TypeSafe; wire-compat vs
  agent-routing as separate Harbor axes; competing
  NAR **not endorsement**;
  [laya-grounded](https://huggingface.co/Luni/laya-grounded)
  not drop-in; phishing 0.611→0.512; Platt not
  temperature). 0★ HIGHs still get real cards. Do
  not copy npm / `pi install` / n8n / HA add-on /
  `TYPESAFE_API_KEY`. No wrapper. No invented
  metrics.
- Queued user SIGNALs + remaining deferred 0945 HIGH
  (`research/notes.md` §88): **Skip Archer.** Docs-only
  on PR #3. Mental models: open LoRA replica
  ([GestaltLabs/Jeff-1](https://huggingface.co/GestaltLabs/Jeff-1)
  acc **0.8183** ECE **0.0807** vs Jev **0.8283** /
  **0.0932** n=9730 *theirs*; set reused; **≠**
  [logan-markewich/jeff](https://github.com/logan-markewich/jeff));
  Jev-first bounded agent
  ([stanley-code](https://github.com/devagrawal09/stanley-code)
  empty findings ≠ approval; human promote; 0.6/0.55/0.15
  still soft);
  NL memory → beam-search FS
  ([findme](https://github.com/marc2332/findme) **≠**
  JevFind);
  price workers not the conversation
  ([jevsubrouter](https://github.com/leftspace89/jevsubrouter)
  fail-open; counts ≠ dollars). laya-vision +
  Cerebellum already §87 — not re-carded. Soft Noul ≠
  hard safety. Do not copy `uv` / npm / cargo /
  marketplace / `TYPESAFE_API_KEY` / `JEVSUB_API_KEY`.
  No wrapper. No invented metrics.
- Hourly 1144 HIGH (`research/notes.md` §89): **Skip
  Archer.** Docs-only on PR #3. Do **not** re-fold
  1047 / §87 / §88. How-to-apply / mental models /
  architecture / Harbor-jevals — not a thin Jev skill
  dump. Backend-agnostic categorization/scoring/
  decision class. Formal methods compose with scoring;
  a Noul is a SENSOR; hard-gating a default 0.5 bool,
  quoting apa “mathematically fulfilled,” treating A/B
  proxies as token savings, letting Jev send mail, or
  pasting jev-test bars as results is soundness theater.
  Seven clusters: **Typed if**
  ([feelings](https://github.com/BoundaryML/feelings)
  `.feels()` default 0.5 is Noul-0.5-never-rounded;
  exhaustive BAML `match`; **≠** hunch **≠** Probably;
  license null; **0★**);
  **Shadow then honor**
  ([apa-agent-harness](https://github.com/AiPersonacademy/apa-agent-harness)
  **≠** AntonioCoppe/jev-harness; unpublished npm;
  0.85 still soft;
  [apa-persona-engine](https://github.com/AiPersonacademy/apa-persona-engine)
  SM then leftover LLM; <250 ms ≠ microsecond;
  [grok-bot-jev](https://github.com/Bodila51/grok-bot-jev)
  skill honor; A/B proxies ≠ tokens; 13.0× is a
  top-five cap);
  **Human every action**
  ([Essentiel-Jev](https://github.com/JacquesGariepy/Essentiel-Jev)
  never authority; 0.75 provisional; license null);
  **Atom then sense**
  ([enzo-mcp](https://github.com/mahawi1992/enzo-mcp)
  independently falsifiable claims; UNKNOWN useful;
  **≠** jev-sift);
  **File by Choice**
  ([pigeonhole](https://github.com/noripto/pigeonhole)
  OTHER skip; 0.6 still soft; **≠** jev-semgrep;
  client-side playground
  [jev-agent-decision-playground](https://huggingface.co/spaces/bojansandhaus/jev-agent-decision-playground)
  static no-network; **≠** classifier.dev; sibling
  jev-decisions pointer only);
  **Question preflight**
  ([jev-reliability](https://github.com/vcjdeboer/jev-reliability)
  Nothing about accuracy; noul-gate 0.0%/12.5%/3.6%
  *theirs*; **≠** dinostomp;
  [clduab11/jev-test](https://github.com/clduab11/jev-test)
  bars ≠ scores; **≠** realZachi/jevtest;
  [jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark)
  “Jev wins” is not an assumption; **≠** Jev-RAG;
  [dairui1/jev-lab](https://github.com/dairui1/jev-lab)
  urgent 91% vs Haiku 79% *theirs* synthetic; **≠**
  BrendanH18/jev-lab; do not re-card jev-desktop);
  **Inbox read-only vs write**
  ([jevmail](https://github.com/fazlerocks/jevmail)
  `gmail.readonly` ~3¢/1k *theirs*; **3★**;
  [mailjay](https://github.com/secondfret/mailjay)
  archive/trash after review; license null; **≠**
  mailordinal). Soft Noul ≠ hard safety. 0★ HIGHs
  still get real cards. Do not copy unpublished npm
  `@aipersona/…` / `uv` / `baml toolchain` / Gateway
  keys / `TYPESAFE_API_KEY`. No wrapper. No invented
  metrics.
- Hourly 1241 HIGH (`research/notes.md` §90): **Skip
  Archer.** Docs-only on a **fresh PR off main**. Never
  reopen merged #3 / #4 / #5. Do **not** re-fold 1144 /
  §89. How-to-apply / mental models / architecture /
  Harbor-jevals / toolbelt — not a thin Jev skill dump.
  Backend-agnostic categorization/scoring/decision class
  (Jev-like speed/econ). Formal methods compose with
  scoring; a Noul is a SENSOR; hard-gating AUTO_ACT,
  treating ranking logits as frequencies, pasting
  95.2% / 83% plumbing / 36/120 NL2Bash as class
  ceilings, or letting Jev send/delete/close pinned
  tabs is soundness theater. Twelve clusters:
  **Observe→score→act namesake**
  ([ZHUBoer/ego-jev](https://github.com/ZHUBoer/ego-jev)
  reserved `__none__`; runWorkflow completed ≠ success;
  **≠** jiangkoumo/ego-jev; **0★**);
  **Decision-as-ranking**
  ([jsort](https://github.com/keltokhy/jsort) scores are
  relative; Noul not Choice for scale; CommonLit
  r=0.824 / ρ=0.841 *theirs*; **1★**);
  **Native vs schema-guided Harbor**
  ([groundedness-judge-bench](https://github.com/slavadubrov/groundedness-judge-bench)
  native vs schema-guided; implicit_true included
  in yes; Jev 0.6667 vs GLM 0.7661 *theirs*;
  LICENSE MIT / SPDX NOASSERTION; **0★**; **≠**
  jev-judge-bench);
  **0 promotions / authored vs real**
  ([jev_playground](https://github.com/JYeswak/jev_playground)
  0 promotions; routing-backtest 0.0447%; **0★**; **≠**
  HF playground);
  **Offload + classifier-not-generator**
  ([yuyang2230/jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)
  jev-1.13-free; **≠** GodsBoy; **0★**;
  [jev-techstack-classifier](https://github.com/swap-mitra/jev-techstack-classifier)
  stack_config.json only; license null; **0★**);
  **Collapse late**
  ([s1_ruby](https://github.com/innocentdiaz/s1_ruby)
  collapse late; `undecided?` abstain; **≠** hunch **≠**
  feelings; **1★**);
  **Unofficial toolbelt**
  ([2389-research/judgement](https://github.com/2389-research/judgement)
  license null; confidence ≠ winner p; **0★**;
  [typesafeai-sdk-rust-community](https://github.com/community-ports/typesafeai-sdk-rust-community)
  typesafeai-sdk-community not a new species; **0★**);
  **Pointer shell**
  ([tpellet/hunch](https://github.com/tpellet/hunch)
  exit 3; never-execute list; **≠** carldaws/hunch;
  **0★**);
  **Preview-first VOI / rubric rewrite**
  ([jev-file-search](https://github.com/emilwagman/jev-file-search)
  scores not calibrated accuracy; **0★**;
  [jev-linkmap](https://github.com/stas4000/jev-linkmap)
  Jev never sees S2 prose; LICENSE MIT / SPDX
  NOASSERTION; **0★**);
  **Life fail-open covers**
  ([jev-mail](https://github.com/muhammedilyasy/jev-mail)
  metadata only; [tidy](https://github.com/MANISH007700/tidy)
  none-of-folders stay; [tab-bouncer](https://github.com/MANISH007700/tab-bouncer)
  pinned/audio/current never closed;
  [lkclean](https://github.com/stefw/lkclean) Show
  fail-open; [jev-yt-time-saver](https://github.com/jaibhasin/jev-yt-time-saver)
  Show anyway);
  **S1 decide / S2 plan**
  ([ORIGIN-CIVILIZATION](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION)
  pause-if-no-Jev; validResponse sums-to-1; **≠**
  Essentiel-Jev; **1★**);
  **Seed/expand/judge/verify + local daemon ≠ Jev**
  ([jev-crawlers](https://github.com/russfranky/jev-crawlers)
  risk bands never raw boolean; **0★**;
  [jevbrain](https://github.com/Synxneuos/jevbrain)
  AUTO_ACT is not a Noul; license null; **9★**). Soft
  Noul ≠ hard safety. 0★ HIGHs still get real cards.
  Census (user-provided; not re-derived): Archer still
  NOT landed (HF empty; tracker likes 49 lastModified
  2026-09-19T18:37:18Z still promised); Laya yes;
  Blackwood ABSENT; SemIf 1846 (+17); jevlike 962 (+3);
  TypeAR-AI/TypeAR 10 (+1); Awesomejev flat 561/27007.
  Do not copy `TYPESAFE_API_KEY` / `ZEN_API_KEY` /
  `AI_GATEWAY` / `uv` / `cargo` / wrangler / chrome
  unpacked / OAuth client ids / shop URLs / `.env`.
  No wrapper. No invented metrics.
- Hourly 1347 HIGH (`research/notes.md` §91): **Skip
  Archer.** Docs-only on a **fresh PR off main**. Never
  reopen merged #3 / #4 / #5 / #7. Do **not** re-fold
  1241 / §90. How-to-apply / mental models /
  architecture / Harbor-jevals / toolbelt — not a thin
  Jev skill dump. Backend-agnostic
  categorization/scoring/decision class (Jev-like
  speed/econ). Formal methods compose with scoring; a
  Noul is a SENSOR; hard-gating argmax as safety,
  pasting 97.7% n=130 / 0 hallucination / 8,026 tokens
  as class ceilings, or treating a skill named System
  One as a judge is soundness theater. Nine clusters:
  **Judge harness as control API**
  ([judgekit](https://github.com/lexingtonhibiki/judgekit)
  YAML classify/score/route/verify; 97.7% n=130
  *theirs*; **0★**;
  [typed-judge-kit](https://github.com/Ascurse/typed-judge-kit)
  verdict-in-code; MIN_LABELS=20; **0★**);
  **Batch packing VOI**
  ([decide](https://github.com/alsoleg89/decide)
  packing VOI; 0.8 ≠ 80% accuracy; license null;
  **0★**; **≠** jev-sift);
  **Calibration as product**
  ([Jev-Calibration](https://github.com/AnthusAI/Jev-Calibration)
  Platt ECE 0.117→0.052; license null; **0★**;
  [jev-calibration-arena](https://github.com/pmcclelland/jev-calibration-arena)
  never acts; size 0; **0★**; **≠** jev-arena);
  **Decision-as-Plugin**
  ([openrouter-jev-mcp](https://github.com/ctmx/openrouter-jev-mcp);
  [typesafe-mcp](https://github.com/cyrusasco/typesafe-mcp)
  noul deadband 0.35–0.65;
  [FrancoisChastel/jev-code](https://github.com/FrancoisChastel/jev-code)
  ≠ npm jev-code; **1★**;
  [claudecode-jev-marketplace](https://github.com/skylence-org/claudecode-jev-marketplace)
  fail-open not hot path;
  [mcp_jev](https://github.com/pedroknigge/mcp_jev)
  packs not ask_jev;
  [jev-skill](https://github.com/codaaiteam/jev-skill)
  jevtypesafeai.com ≠ TypeSafe);
  **Policy-constrained skill select**
  ([hermes-switchyard](https://github.com/bgrablin/hermes-switchyard)
  ≠ hermes-jev-router ≠ hermes-plugin-jev; **0★**);
  **Tiny local econ pruner**
  ([nanoprune](https://github.com/dmdjr1409/nanoprune)
  2.8MB ECE 2.58%; 0 hallucination theater; **0★**);
  **Observe→score→act cousins**
  ([jev-browser-agent](https://github.com/smartdio/jev-browser-agent)
  ≠ ZHUBoer/ego-jev;
  [omp-jev-web](https://github.com/Dakai/omp-jev-web)
  DONE ≠ proof;
  [hari007sh/jev](https://github.com/hari007sh/jev)
  ≠ dannote/jev; license null);
  **Deterministic verify ≠ System One**
  ([system-one-skills](https://github.com/0thernet/system-one-skills)
  deterministic verify; **0★**);
  **Soft-score vs hard-argmax**
  ([typed-gate](https://github.com/harshpuri84/typed-gate)
  band [0.40,0.60] is refusal;
  [pi-jev-gate](https://github.com/fivethirty/pi-jev-gate)
  fail-closed; choice is the verdict; rh-guard owns). Soft
  Noul ≠ hard safety. 0★ HIGHs still get real cards.
  Census (user-provided; not re-derived): Archer still
  NOT landed. Do not copy `TYPESAFE_API_KEY` /
  `OPENROUTER_API_KEY` / `JEV_API_KEY` / `uv` / `npx`
  / plugin-marketplace install / `.env`. No wrapper.
  No invented metrics.
- Hourly 1441 HIGH (`research/notes.md` §92): **Skip
  Archer.** Docs-only on a **fresh PR off main**. Never
  reopen merged #3 / #4 / #5 / #7 / **#8**. Do **not**
  re-fold 1347 / §91. How-to-apply / mental models /
  architecture / Harbor-jevals / toolbelt — not a thin
  Jev skill dump. Backend-agnostic
  categorization/scoring/decision class (Jev-like
  speed/econ). rh-guard owns the gate cousins;
  Augustus owns placement. Formal methods compose with
  scoring; a Noul is a SENSOR; pasting Foq 100%/ECE
  0.2% / Reranker 0.1667 / 400 ms / akpsahan vs-Jev as
  class ceilings, or treating Qwen3.8-27B as Archer, is
  soundness theater. Nine clusters:
  **Self-hosted econ**
  ([Foq](https://github.com/yohanargentina-oss/Foq)
  ~25ms/2.2GB local; **1★**;
  [rev](https://github.com/jaswanthsanjay88/rev)
  prefill-only + HF jev-0.5b; **0★**;
  [robfrase/jev](https://github.com/robfrase/jev)
  planning memo);
  **Soft-judgment gate integrity**
  ([typesafe_agent_gates](https://github.com/ThiagaoBR/typesafe_agent_gates)
  27/27 / 31/31; [safe-sh](https://github.com/EpicEric/safe-sh)
  static remainder; **1★**;
  [jev-pastepilot](https://github.com/buberlo/jev-pastepilot)
  Confirm before act; rh-guard owns);
  **Retrieval as calibrated decision space**
  ([Jev-Reranker](https://github.com/uspraveen/Jev-Reranker)
  live Jev not yet measured;
  [sessionwise](https://github.com/Nasrallah-AL/sessionwise)
  opt-in relevance;
  [jev-search](https://github.com/savka777/jev-search)
  pointer sieve; **≠** kazuhideoki/jev-search
  **≠** superagents-lab/jev-search);
  **Enterprise reflexes**
  ([400ms-agentic-sf](https://github.com/furuCRM-Inc/400ms-agentic-sf)
  Salesforce WebMCP;
  [typesafe-scheduler-diagnostics](https://github.com/thevilledev/typesafe-scheduler-diagnostics)
  advisory);
  **Screenshot-free / CU**
  ([droidjev](https://github.com/mkruglikov/droidjev)
  screenshot-free;
  [jevcu](https://github.com/Tewoto1/Computer-use-and-control-with-Jev)
  planner still writes);
  **Hybrid S1/S2**
  ([ha-conversation-jev](https://github.com/luxus/ha-conversation-jev)
  Jev→Grok; **1★**;
  [dsh-jev](https://github.com/buberlo/dsh-jev)
  can only gate; **2★**);
  **Harbor-jevals / SRE**
  ([jev-classification-benchmark](https://github.com/rachit-srivastava-devx/jev-classification-benchmark)
  specified not run;
  [jev-luna-pagerduty-trigger](https://huggingface.co/datasets/reachjalil/jev-luna-pagerduty-trigger)
  p≥0.50);
  **Laya densifies**
  ([meldecision](https://github.com/meldltd/meldecision)
  laya-go ONNX;
  [laya-doom](https://github.com/shantanugoel/laya-doom)
  never pixels;
  [laya-api](https://github.com/logixism/laya-api)
  empty README;
  [akpsahan/laya](https://huggingface.co/akpsahan/laya)
  ≠ Archer);
  **Demos / unofficial toolbelt**
  ([jevchess](https://github.com/choxos/jevchess)
  engine owns truth; **1★**;
  [jev-drive](https://github.com/vedssharma/jev-drive)
  sim not AV;
  [story-arc](https://github.com/amali-s/story-arc)
  Jev never authors;
  [jev-hs-assistant](https://github.com/newbie1668/jev-hs-assistant)
  HS6;
  [jev-plays-starcraft-2](https://github.com/golergka/jev-plays-starcraft-2)
  UI-verified ≠ API Victory; **1★**;
  [awesome-jev-use-cases](https://github.com/walidboulanouar/awesome-jev-use-cases)
  catalog; **2★**;
  [typesafe-go](https://github.com/Nibir1/typesafe-go)
  ≠ official). Soft Noul ≠ hard safety. 0★ HIGHs
  still get real cards. Census (user-provided; not
  re-derived): Archer still NOT landed; tracker likes
  **50** lastModified UNCHANGED
  2026-09-19T18:37:18Z; SemIf 1873 (+7); jevlike 969
  (+2); TypeAR 10 flat; Awesomejev 561/27007 flat.
  Do not copy `TYPESAFE_API_KEY` / OAuth `client_id` /
  `uv` / `npx` / `.env`. No wrapper. No invented
  metrics.
- Hourly 1541 HIGH (`research/notes.md` §93): **Skip
  Archer.** Docs-only on a **fresh PR off main**. Never
  reopen merged #7 / **#8** / **#9**. Do **not** push
  onto unmerged SIGNAL fold #10. Do **not** re-fold
  1441 / §92. How-to-apply / mental models /
  architecture / Harbor-jevals / toolbelt — not a thin
  Jev skill dump. Backend-agnostic
  categorization/scoring/decision class (Jev-like
  speed/econ). rh-guard owns the injection-firewall /
  CI-gate cousins; Augustus owns placement. Formal
  methods compose with scoring; a Noul is a SENSOR;
  pasting orchestrator 0.95 / skip_below 0.05 /
  OpenRoboto $ as class ceilings, inventing
  one-dollar-tahoe ASR/FPR, or treating numbered-choice
  softmax as a Noul is soundness theater. Six clusters:
  **Decision-as-plugin for SWE**
  ([jev-orchestrator](https://github.com/petercr/jev-orchestrator)
  difficulty + policy thresholds + JSONL trace; **0★**;
  [jev-codex-pilot](https://github.com/Charlyhno-eng/jev-codex-pilot)
  model + reasoning depth; **0★**;
  [jev-replacement](https://github.com/SunnyKikiHK/jev-replacement)
  keep/shadow/hybrid/reject; license null; **0★**);
  **Evidence projection**
  ([quarry](https://github.com/jackboykin/quarry)
  quarry evidence projection; Go MIT; **0★**; **master**);
  **Soft judgment integrity**
  ([jevguard](https://github.com/seb4ez/jevguard)
  calibrator/cache/escape; **0★**;
  [jev-ci-selector](https://github.com/guilhem/jev-ci-selector)
  CI shadow mode; license null; **0★**; rh-guard owns);
  **Physical/control first-class domain**
  ([awesome-jev](https://github.com/Frank-ZY-Dou/awesome-jev)
  Frank-ZY-Dou/awesome-jev robotics/3D/control; license
  null; **0★**; text-state, not pixels);
  **Harbor-jevals / injection-firewall**
  ([one-dollar-tahoe](https://github.com/PavitarSinghArneja/one-dollar-tahoe)
  TypeSafe Jev defense eval; **0★**; ~74 demo; README
  has no ASR/FPR; rh-guard owns);
  **llama.cpp replica**
  ([llama-jev](https://github.com/webNeat/llama-jev)
  llama.cpp replica; license null; **0★**; softmax ≠
  Noul). Soft Noul ≠ hard safety. 0★ HIGHs still get
  real cards. Census **not provided this hour** (not
  re-derived). Archer still NOT landed. Do not copy
  `TYPESAFE_API_KEY` / `AI_GATEWAY_API_KEY` /
  `EXA_API_KEY` / `GROQ_API_KEY` / `uv` / `npx` /
  `go install` / `.env` / `attacks.json`. No wrapper.
  No invented metrics.
- Effect-oriented loops (`notes.md` §28, `mappings.md` §19): Ward's
  ZIO client keeps Jev as the outer Choice and the handler as the
  effect. Not Effect.ts. GLiNER author: GLiNER2 "like jev" is GLiGuard
  schema-conditioned categorize, not a Noul.
- Boundary-audit stop conditions for TOCTOU-of-Noul and vacuous specs;
  FAQ rows for Alloy vs Apalache and PufferLib-as-DST-trio
- Research pointer to [dayhaysoos/jevals](https://github.com/dayhaysoos/jevals):
  local MIT workbench for Jev questions vs labeled Noul/Choice/Score cases
  (compare runs, WebMCP + agent skill). Empirical acceptance-test surface
  for Hypothesis mapping cards; complements `evaluate_decisions.py`. Not a
  jevals how-to (`research/notes.md` §24; one sentence in `validation.md`)
- Mental-models card: Augustus is design judgment across AI, SWE,
  business, knowledge work, and life — not SWE-only. Pillars: expected
  utility / selective classification, calibration and cost-sensitive
  thresholds, VOI, MCDA, search/control substitutions, signal detection,
  Leveson org/safety, NATM/snap-fit/Norman/Kent/Shirky as general
  intuition. Domain gallery labeled Hypothesis except launch-week
  Empirical SWE rows.
- Archer Hume architecture reconstruction (17 Sep 2026 essay, ~10k
  probes of `jev-1.13.0`): direct readout vs generated confidence,
  isolated questions, listwise IIA and order sensitivity, confidence as
  arithmetic on the distribution. Independent envelope probe; does not
  override live TypeSafe docs. Announced open-weight drop is **WATCH**
  (27B dense, AU healthcare residency, prefers "decision models"; still
  no Hub weights). `research/notes.md` §31, §33; `judgment-class.md`
  when-to-use table; FAQ confidence / surfaces questions.
- Entropy as allocator (**Hypothesis**, `judgment-class.md`): Atallah's
  low / medium / high buckets place System One on typed decisions and a
  frontier decoder on high-entropy synthesis — same axis as marginals
  vs joint and as VOI. "Review this PR" as medium is still partly
  generative; "first model ever" is a claim. `research/notes.md` §38
- Marginals, not a probabilistic program (`judgment-class.md`, FAQ):
  Erik Meijer — Jev is a cool API and not a PPL; Kleisli qualifications
  exaggerate; "Jev gives you the marginals; a decoder gives you the
  joint." Joints and invariants stay with TLA+ / Alloy / contracts.
  `research/notes.md` §34
- Bespoke Nimble: open contrastive recipe, not a Jev distill. Model
  card Apache-2.0 LoRA on Qwen3.5-9B (repo license absent). Their
  324-example holdout is a named receipt (Nimble 90.12%, Jev 1.13.0
  93.21%), not a ranking. 9B-vs-Jev on your labels stays Hypothesis.
  `research/notes.md` §35; one sentence in `validation.md`
- djev-spark: third compute graph (diffusion structured reads,
  Jev-shaped I/O, image-in). Empirical as the public interface;
  Hypothesis that it beats a decision head on your task. Archer's
  multimodal drop stays WATCH. `research/notes.md` §36
- Perception specialist then judgment specialist vs shared multimodal
  System One (**Hypothesis**): SAM 3.1 (masks and tracks) or an ASR
  transcript, then typed decisions on that state, is an application
  pattern, not native omni. Information dies at the interface. Prefer
  a shared multimodal decision model when the joint matters (Archer
  Watch, not Empirical; djev-spark images; future audio). Basit ask,
  primary post not retrieved. `research/notes.md` §39
- Perception→decision pipeline, measure, and hill-climb
  (**Hypothesis**, `validation.md`): stages with a versioned state
  contract; stage metrics plus a frozen taskset; HoH changes one stage
  or one interface. DSPy/Ax only on LM-program knobs; jevals and
  calibration for the decision slice; Harbor names product
  end-to-end, not a tutorial. `research/notes.md` §41
- Eval & hill-climb (`validation.md`): jevals decision-stage hygiene
  (independent keys, correctness is not confidence, held-out, immutable
  runs) and Harbor as the product taskset substrate; one composition
  table. `research/notes.md` §40

### Changed

- Skill description rewritten as trigger conditions (mixed architecture,
  prefilter, routing, preference lint, classification skepticism, family
  choice including GLiNER/GLiClass/listwise/vision) plus an explicit `not_for`
  against the official `typesafe-ai` skill
- Identity lock vs neighbor skills (`typesafe-ai`, `tenbin`, `decision-first`)
  so Augustus stays the design-judgment layer — class-wide, not TypeSafe-only
- Design cards name hole, family, and typed judgment provider (Jev default;
  other family only with self-eval)
- Protocol fan-out step is family-aware (Jev batch, GLiClass one-pass,
  dual-encoder prompt scoring); ranking vs decision fail policy is a
  non-negotiable
- Protocol and FAQ branch for "formally verify with Jev"; methods-catalog
  and composition-algebra verifier position point at the ownership split
- Skill mission and description are domain-general (AI / SWE / business /
  knowledge work / life); FAQ "is this only for software?"; mappings.md
  beyond-SWE examples labeled Hypothesis; boundary-audit red flags for
  TOCTOU-of-Noul and vacuous specs; formal-methods expanded with Alloy vs
  Apalache and the DST trio including PufferLib; GLiNER promoted from
  cousin footnote to species-map peer

### Fixed

Adversarial review of the whole skill against its own non-negotiables
(findings in `research/notes.md` §27).

- Gate fail policy is per action, not universally open
  (`composition-algebra.md` position 3, `agent-self-assessment.md`):
  advisory guards fail open *because* an interlock sits underneath;
  selection and authorization gates fail closed
- Dual-orchestration topology A selects from a closed catalog instead of
  "planning" MCP calls, which contradicted the standing planner rejection
- Species map applied to the skill's own advice: GLiClass (categorize) is
  the large-catalog substitute for a 255-option Choice; GLiNER spans are
  not (`SKILL.md`, `judgment-class.md`, `applied-mappings.md`)
- Han Xiao trolley relabeled an Empirical **rejection** (one tweet, no
  repo), not a recipe
- openjev-lm caveat moved to the figure it belongs to: 92.9% is against 70
  hand-labelled gold, 98.1% is teacher *agreement*
- Contract surface removed from design cards: the Ax constructor call and
  the `instructions` key enumeration point at live docs instead
  (`optimizer-integration.md`, `question-design.md`)
- `mappings.md` preamble no longer claims uniform Hypothesis where card
  bodies say Contract/Empirical; §17 forbids reusing jevgate's ≤0.18 as a
  constant; all Hypothesis-range references aligned to §6–§19
- Ownership split labeled Contract in `toolbox-mapping.md`, matching
  `mappings.md` §8; done-check splits structure from the Noul

Second pass on `7b3a0c3` (`research/notes.md` §43). Zero blockers.
Dropped the unpublished `npx jevals` line; SAM and ASR are upstream
producers, not the perceive species; removed two call shapes from
`optimizer-integration.md`; tagged the $0.042/MTok cell as a vendor
figure; marked GodsBoy 94.4% exploratory.
- Skill description gained trigger terms for boundary audit, question
  diagnosis, agent self-supervision, and optimizer placement

## [0.2.0] - 2026-09-18

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12).

### Added

- Boundary-audit card for existing systems: three-way split (exact /
  bounded judgment / generation), code-smell catalog, fit test, opportunity
  map, smallest-viable-boundary rule, Jev-around-LLM sandwich, centralized
  policy + raw-judgment retention, red flags, completion questions
- Protocol branch: audit a codebase/PR before inventing mappings; per-action
  risk gates; keep questions/thresholds in one reviewable module
- Skill description trigger terms for brittle parsers, prompt-to-JSON
  classifiers, and agent loops that are really bounded decisions

## [0.1.0] - 2026-09-18

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12) — the only tagged revision of the official skill at
Augustus launch.

### Added

- Skill protocol, decision-design card, and evidence labels (Contract /
  Empirical recipe / Hypothesis)
- Classical-method mappings: features/utility, selective decisions, decision
  circuits, bounded rerank, hierarchy/beam search
- Agent self-assessment, optimizer coupling (Ax, DSPy, ProgramAsWeights)
- Toolbox sweep, named-methods catalog, 11-position composition algebra,
  question-design diagnosis
- Validation gates and `scripts/evaluate_decisions.py`
- Launch-week evidence archive (187 repos) and public ecosystem index
- Claude Code marketplace manifest; public GitHub mirror at
  [`24601/Augustus`](https://github.com/24601/Augustus)

### Research log (pre-tag)

The dated passes below are how 0.1.0 was assembled.

### 2026-09-18 (refresh pass 2)
- Research: Gemini Deep Research report retrieved and archived (interaction ID
  saved in jev-archive/state); GitHub census doubled to ~60 Jev repos +
  framework integrations (LiteLLM, LangChain, Vercel AI, Mastra, Eliza, Ax,
  Composio); all 87 repos cloned to /home/user/workspace/jev-archive for
  hourly refresh.
- New measured recipes added to notes.md: foreman supervision loop, pi-jev
  gate thresholds, pi-warden 6→0 paired-run result, winnow relevance sieve,
  fast-jev-compaction two-noul rule, skill-router gates (0.30/0.40, shortlist
  3, 94.4% vs 70.8%), calibration ECE 0.0313 vs 32% OOD collapse (Archer
  Hume), Every 777-judgment eval, Near Here moderation numbers.
- Skill: added references/agent-self-assessment.md (agent self-supervision
  lifecycle, grounding/citation checks, skill callability testing) and two
  mapping-index rows; validation.md dogfooding section still canonical.

### 2026-09-17/18 (initial)
- Baseline research archive (sources.json, notes.md), augustus skill with
  mappings + validation references, evaluator script, hourly refresh script,
  Claude plugin marketplace manifest.

### 2026-09-18 (topic-index pass 3)
- Fixed census method: exact GitHub search paginated (700 repos created since
  09-14 captured; 700-result cap noted) + topics/jev crawl → ~80 additional
  repos; archive now 184 clones. Miss-cause documented: earlier star-sorted
  limit-40 search cut the low-star tail (incl. both MCTS repos).
- Skill: MCTS mapping promoted experimental → empirical recipe (grounded vs
  speculative fidelity in types; probes-only concession; measured 24/24 vs
  1/24 greedy); agent-self-assessment.md gains the judge-variance recipe
  (Jev judge 224-279x more consistent than LLM judge over 100 reps).

### 2026-09-18 (pass 4 — optimizers + official skills + clone audit)
- ax Jev support documented from source (native adapter details, trueThreshold
  semantics, fail-closed mapping validation); new reference
  optimizer-integration.md covering Ax + DSPy typesafeify + jev-dspy-lab.
- typesafeainate/dspy-typesafeify cloned; official typesafe-ai/skills already
  archived and layered-on (never duplicated).
- Clone audit: repos.txt deduped (185 unique), 0 missing on disk, no failures.

### 2026-09-18 (pass 5 — toolbox sweep meta-method)
- New references/toolbox-mapping.md: the how-to-find-approaches-and-
  applications procedure (judgment-shaped-hole substitution, newly-feasible
  classification via economics inversion, standing rejections list); wired
  into SKILL.md central model + index row.

### 2026-09-18 (pass 6 — named-methods + operators/theorems tier)
- references/methods-catalog.md: ~20 named algorithms (CatBoost row is
  Empirical via autoresearch cookbook) + operators/theorems tier with
  precondition-carrying rule; wired into SKILL.md index and toolbox sweep.

### 2026-09-18 (pass 7 — composition algebra as application generator)
- references/composition-algebra.md: 11-position grammar of Jev-vs-construct
  relations, logical-operator combination rules, and the position×construct
  traversal as the systematic application generator; wired into SKILL.md
  index + toolbox sweep.
