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
