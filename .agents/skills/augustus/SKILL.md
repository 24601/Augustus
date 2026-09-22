---
name: augustus
description: "Use when placing the decision-model class (classifiers, encoders and decoders, specialized AR and constrained heads, vision and listwise scorers, and what TypeSafe calls System One). TypeSafe Jev (Choice, Score, Noul) is the dominant exemplar most users will call. Peers such as Laya, kev, OpenJev, and GLiNER are in the class and are not equal in adoption. Ranking is not calibration. A soft score is not a hard gate. Formal methods are one pillar. Not a TypeSafe product; load the typesafe-ai skill for live Jev contracts. Trigger phrases: references/activation-triggers.md."
license: MIT
metadata:
  version: 0.5.1
  typesafe_skill: v0.5.7
  typesafe_skill_commit: 65a39f3
  tribute: "Named for Augustus De Morgan (1806-1871), mentor of William Stanley Jevons."
---

# Augustus

Design-judgment skill for the **decision-model class**: classifiers,
encoders and decoders, specialized AR and constrained heads, vision and
listwise scorers, and what TypeSafe calls System One. Uses mathematical,
logical, and algorithmic mental models across **AI, software, business,
knowledge work, and life**. Not limited to software engineering. Formal
methods are one pillar (`references/formal-methods.md`); the portable frames
are `references/mental-models.md`.

TypeSafe Jev (typed Choice / Score / Noul) is the **dominant** product
most users will actually call, and the default recommended path. Peers
are in the class; they are not equal in adoption. This skill owns **where
judgment belongs**; the official `typesafe-ai` skill plus the live docs own
Jev integration contracts. Read them before writing Jev API code. Neighbor
skills `tenbin` (lint/measure) and `decision-first` (try-Jev-first habit)
own their jobs. Do not collapse into a TypeSafe how-to, a Laya install, a
kev serve, a blackwood vLLM how-to, a jev-local Docker install, or a
GLiClass or GLiNER tutorial.

Pick the **pillar** from the hole (expected utility, VOI, MCDA, signal
detection, search/control, org/safety, formal methods), then the
**family** (`references/judgment-class.md`), then the vendor. Default
placement is **mixed architecture**: exact work in code/policy, narrow
judgment on a decision-model, generation only where something
must be written.

Central model: **evidence → semantic judgments → explicit policy → checked
action → observed outcome.** Every design must name what the judgment
model estimates, what remains exact, what (if anything) is still
generated, and what experiment could prove the idea wrong.

For genuinely new problem shapes, use the toolbox sweep
(`references/toolbox-mapping.md`): find the judgment-shaped component of a
classical method you already trust, substitute it, classify the win
(marginal / newly-feasible / invalid), and falsify.

Trigger phrases that should activate this skill live in
`references/activation-triggers.md`. The YAML description stays
short so a registry can show the skill. Load that file for the
phrase list. It does not add a recipe.

## Protocol

1. If the request is "replace the LLM/stack with Jev", "isn't this just
   classification?", "is Jev probabilistic programming?" (marginals vs
   joint — not a PPL), "low vs high entropy / frontier model for
   this?", "is Jev the only model?", "is this only for
   software?", "formally verify with Jev / replace TLA+ / Dafny /
   DST", "Alloy vs Apalache", "GLiNER vs Jev", "LLM-as-judge",
   "paraphrase brittleness", "allowlist then judge", "TOCTOU-of-Noul",
   "Jev inside the database / sqlite-jev", "Jev picks bitrate / join
   order / the model", "wait for Archer", "lint the request / missing
   other", or another phrase in `references/activation-triggers.md`,
   then `references/mental-models.md`, then
   `references/mixed-architecture.md`, then
   `references/judgment-class.md` before any mapping. Proof,
   model-checking, contracts, DST, and judgment-vs-proof ownership: also
   read `references/formal-methods.md` (Alloy vs Apalache; DST trio
   Antithesis / Resonate HQ / PufferLib; TOCTOU-of-Noul). One-screen
   alias: `references/formal-semi-formal.md`. Answer with a **placement**
   (sieve / keep-drop / triage / rank / route / gate / perceive /
   abstain / gather / replace-one-classifier-step) and a **pillar +
   family**, not a rewrite, a vendor tutorial, or a Noul-as-proof. If it
   is an existing system, PR, workflow, or practice: also run the
   boundary audit (`references/boundary-audit.md`). Classify each step
   as exact / bounded judgment / generation; recommend the smallest
   insertion, not a redesign. Greenfield with no replacement framing:
   start at step 2.
2. Start from the desired behavior: what the software, person, or
   organization shows, selects, changes, or hands off. Work backward to
   the judgments it needs. Name the domain and the pillar
   (`references/mental-models.md`), then pick the family whose
   *objective* matches the action's fail policy
   (`references/judgment-class.md`). Do not start from a logo.
3. Keep exact work in code, policy, checklists, ledgers, law, and
   recipes: arithmetic, counting, dates, lookups, authorization, safety
   interlocks, control flow, side effects, money. Keep open-ended
   writing, explanation, and code generation on a generative model or a
   person; a judgment-class model may gate, route, or verify around that
   call. Proof, model-checking, contracts, and DST stay with their
   tools — a Noul is a sensor, not a discharged proof obligation
   (`references/formal-methods.md`). A capability kernel keeps
   secrets out of the agent and leaves BLOCK/ASK/ALLOW in policy;
   type-safe is not the same as correct.
4. Give the provider one narrow judgment per question (a knowledgeable
   person could answer in a second given the state). Split multi-factor
   judgments; fuse in code with visible weights. Jev's option/envelope
   limits are Jev's, not the class's — large or changing label sets may
   prefer a GLiClass one-pass (categorize). GLiNER (locate) substitutes
   only where the answer *is* a span in the text
   (`judgment-class.md` species map).
5. Exploit the family's cheap fan-out: batch independent questions in
   one request when the provider supports it (measurement economics:
   200 calibration questions in 2 requests; ~100 Battleship noul/turn); encode text + all labels
   once for GLi\* heads; score many prompts against one
   embedding for dual-encoder vision. Sequence a second call only when
   its state or options depend on an earlier answer.
6. Route on uncertainty with per-action thresholds tuned on your own
   data. Ranking scores **order** (fail open); decision scores
   **authorize** (fail closed). Do not threshold a listwise or affinity
   number as if it were P(permit). The same judgment can authorize a
   reversible path and must not authorize an irreversible one.
7. Ship a decision-design card (below) and the smallest falsifying
   experiment. Name the eval path. A card without one is incomplete
   (`references/validation.md#eval--hill-climb`). Record family, model,
   rubric, candidate-source, and policy versions. Keep questions,
   criteria, and thresholds in one reviewable module; store raw
   judgments separately from derived actions.
8. Already-catalogued sources are not done. When fingerprints move,
   densify the prior card. Treat **revisit HIGH** like **novel HIGH**.
   Star-noise is not a fold. See **REVISIT / since last look**.

## REVISIT / since last look

Basit standing order (2026-09-20): Augustus revisits already-catalogued
repos when they change since last look, not only first sightings.
Things change a lot.

Hourly fold prompts must treat **revisit HIGH** like **novel HIGH**
for Augustus. Skip is for star-noise and name collisions, not for "we
already have a card."

Never append uniqueness locks or hourly HIGH digests to `README.md`.
The human-facing README stops at License. Locks live in
`research/notes.md`, fold overlays, and uniqueness_gate fixtures.

Revisit / since-last-look lock: catalogued repos are not done; store fingerprints default_sha, pushed_at, description_hash, release_tag; material change is README/API/release/calibration claim/serving port/bench rewrite; star-noise is stars/likes/forks alone; densify the prior notes section, do not mint a sibling first sighting; do not invent equivalence; SHA move is not a replica; treat revisit HIGH like novel HIGH for Augustus; notes.md §122

**Fingerprints to store** (hourly diffs these): `default_sha`
(full HEAD, not a 12-char prefix), `pushed_at` (GitHub push
clock), `description_hash` (sha256[:12] of the GitHub / Space
description, or null if unquoted; not README SHA),
`release_tag`. Helper:
`research/revisit_fingerprints.py`. Checklist:
`research/revisit-checklist.md`.

**Material change** (revisit HIGH): README rewrite, API / primitive
surface, release tag, calibration claim, serving port or bottle,
bench rewrite. **Star-noise** (pulse only): stars, watchers, forks,
Hub likes, likes-only jitter with `lastModified UNCHANGED`.

**Densify, do not invent a second census.** Keep the original
`notes.md` section id. Append a dated since-last-look card. Quote the
new README *theirs*. Keep the prior quotes. Do not mint a sibling
first-sighting section. Do not invent equivalence: SHA move is not a
replica; wire-compat is not a calibrated Noul; a new bench number is
not Harbor. Namesake locks stay. Prior uniqueness locks stay one
substring. Do not reopen or amend PR #23–#44. Does not bump 0.5.0.
Merged #44 owns §121. This protocol is §122.

## Mapping index

| Familiar method | Judgment shape | Detail |
|---|---|---|
| Mental models across domains (not SWE-only) | EU, abstention, VOI, MCDA, SDT, search/control, Leveson, NATM/Norman/snap-fit; **extractable-from-state boundary map** (self-contained vs needs outside knowledge). **Apply queued 1047 follow-ons** (`notes.md` §88): **Replica honesty** / **Empty ≠ approve** / **Beam as control** / **Cache is the exact envelope**. Apply 1144 (`notes.md` §89): **Typed if** / **Shadow then honor** / **Human every action** / **Atom then sense** / **File by Choice** / **Question preflight** / **Inbox read-only vs write**. See `references/activation-triggers.md` for the rest of this row.
| Judgment-model class (Jev is exemplar, not monopoly) | Species: decide / locate (GLiNER) / categorize (GLiClass) / rank / perceive; open heads include encoder DeBERTa, LoRA distill, **domain specialist LoRA on independent gold**, openjev-lm, kev. Compaction job is backend-agnostic (Jev Score/Noul vs GLiNER2.5 encoder). Indexer cousin: GLiNER extract + escalate-S2 (10–50× unfilled). Computer-use observe→score-among-candidates→code-acts is backend-agnostic (Jev Ultrafast ↔ GLiNER2 Ultrafast ↔ Cua-S1 specialist ↔ Stagehand experimental Jev stack; **OCR+AX desktop:** typesafe-computer-use hosted Jev, never ships a screenshot for the *decision*; Cua-S1 is not TypeSafe Jev; See `references/activation-triggers.md` for the rest of this row.
| Open weights vs constrained decoding vs proprietary API | Three open paths: encoder open-jev / AR constrained decode (TypeAR + pcdServer; decision-token LoRA; packed one-forward logprob on open LLMs; **CUDA/PyTorch local replica** jevify — uncalibrated likelihoods ≠ Noul) / trained decision-only (Laya + ONNX port, Nimble, kev, **blackwood-rlcd** multimodal now, Archer Watch still Watch). **Domain LoRA specialist on independent gold** (not a Jev teacher-copy): train when downstream reads p; few-shot hosted when only argmax. Local `/v1/systemone` surfaces: jev-local (stub until `hf`), kev (trained pointer), von (§49 Needle SAN snapshot ≠ this-pass 395M / n=78; **Hourly 1851:** MLX von port ≠ that n=78 table; logprob or early-exit readout ≠ trained head; residual plus LoRA is one seed; Qwen3.5 ≠ Archer; `notes.md` §158). See `references/activation-triggers.md` for the rest of this row.
| Formal / semi-formal (proof vs judgment) | Sensor vs constraint vs searchlight; Alloy vs Apalache; DST trio; TOCTOU-of-Noul, AI×FM. Skills→oxlint: AST/precheck compose with remainder judgment without hard-gating a Noul as a proof. PR attention ≠ correctness (anti-soundness-theater). Engine owns truth / Jev owns judgment (Stockfish+Jev chess coach). Capability kernel: type-safe ≠ correct; irreversible behind threshold AND human. Eval integrity: check the instrument, not just the score (`dinostomp jev` tests a question like an if-statement). Effect contracts, not surface tokens (construct-auto-classifier; privilege ≠ verdict). **Jev supplies evidence, code owns authority** (actiongate-jev; See `references/activation-triggers.md` for the rest of this row.
| Mixed architecture (judgment model + LLM) | Provider judges, LLM writes, code owns control; not a stack replacement. Advisory sidecar never changes host routing. Dual-process: S1 decides, S2 generates (routing accuracy unmeasured); **Harbor-shaped cousin:** decide→policy→LLM leftover (shared Answer schema; jev vs gen-json vs gen-logprob; Noul 0.5 never rounded). **Closed-vote CU:** no planner LLM; code builds options, Jev only picks (JevOnly). **Host-owned product:** app retains handlers/permissions; Jev over live typed actions (waymode). S1 specialists + S2 coordinator is the same split (description-only greenfield). Internals ≠ FSM; See `references/activation-triggers.md` for the rest of this row.
| Context sieve | Relevance Noul per block; always-keep set in code; stub + recall key. Encoder cousin: GLiNER2.5 retention Choice + char-offset spans (gliner25-compaction); fail-closed keep_full; shadowMode default. Stdout cousin: jev-pruner (Jev Noul after hard ≤10k/JSON-diff envelope; fail-safe original; archive). Session-ledger cousin: carryforward (verbatim facts; Jev scores recall; rules never judged; fail-open dump). Classify-first MCP cousin: jev-sift (batch path/url/text → Jev without entering main agent context; uncertain/errors/truncation ≠ irrelevant). **Capability-tree lookup:** NiazMorshed2007/jcr one tool; returns context; See `references/activation-triggers.md` for the rest of this row.
| Exact-text keep / drop | Choice include/exclude/mixed over candidates code already holds. Extractive quotes / pointer-not-generator (model never writes the excerpt; char-offset compaction same species). Observed a11y/DOM controls: score among them; code clicks (Jev or GLiNER2 or Cua-S1 option-attention). Harness productization: Stagehand extract pick-and-copy (Jev picks; code copies; schema/gate else LLM). **Closed-vote CU:** code builds options, Jev only picks, no planner LLM (JevOnly); host-owned handlers/permissions (waymode). **Hot-click CU:** indexed element table → operation+target in one request; code owns observe/execute/verify; text model only for type (ego-jev; See `references/activation-triggers.md` for the rest of this row.
| Environment / harness triage | Scan every step for env failure; LLM autopsy only on flags. Merge-gate cousin: cluster in code, judge labels cause, policy owns PASS/BLOCK (latch; judge never says ignore alone). **Pre-review typed gate:** should_review/risk/route/touches_secrets → auto-approve|human-review|block (ci-gatekeeper; cheap before expensive LLM/human; operator-owned thresholds). **Stop-hook attention redirect:** eight risk axes, assist=one reinspect, fail-open, uncalibrated 0.85 (jev-preflight; not a merge blocker). **VOI hunk prune:** Jev scores PR hunks before expensive generative review (prune-review; 22-run 1.18% with 305% outlier *theirs*; ~20% target). **Whole-repo intent:** VERIFIED/VIOLATION/UNKNOWN beyond the diff (jev-intent-review). **Commit pre-review:** message vs diff / cohesion / omitted change; middle band is review not a verdict; regex proves literals (commitjev). **Hourly 1241:** jev-crawlers risk bands never raw boolean. **Hourly 1347:** alsoleg89/decide packing VOI; 0.8 ≠ 80% accuracy; 0thernet/system-one-skills deterministic verify | `references/applied-mappings.md#3-environment--harness-triage` |
| Moderation and ranking | Hold-before-publish vs graded rerank; fail policy per action. Meaning-search without embeddings (jevgrep packed parallel; 79% top-5 on stripped repos; keyword still wins exact strings). **Meaning-grep** AND/OR/NOT over *thresholded* line Nouls; proposition≠embedding; Semgrep.dev collision; not a gate (jev-semgrep §86). **Evidence-packet explorer:** index-once ask-many, citable source_of_truth/tests/callers (jevex). Measured RAG rerank vs generative rerank (Jev-RAG one-run ≥70% cost / 72% latency vs Spark rerank; See `references/activation-triggers.md` for the rest of this row.
| Skill / tool routing | Choice over a closed catalog + whether-anything-fits; code dispatches. Route ≠ memory: cheap intent gate skips memory tours on easy routes. Session-sticky first-prompt classification (lock for the session; fail-closed to a declared fallback). OMP/pi: `jev_route` topology/tier + `jev_acceptance_gate` before done (**fail-open**; contrast pi-jev-approver fail-closed). OMP prompt suppression: Jev grades gated calls; operator owns the bar; plugin never self-tunes (omp-greenlight; not a sandbox). **Outline only:** Hermes pre-agent skill broker — code owns grants; Jev never grants access (skill-broker; See `references/activation-triggers.md` for the rest of this row.
| Expensive observation router | Structural prove (text layer) ∩ remainder Noul (needs OCR?) | `references/applied-mappings.md#6-expensive-observation-router` |
| Capability kernel / human-confirmed gate | Secrets never in the agent; closed action space; Jev SENSOR; policy BLOCK/ASK/ALLOW. Distinct from pre-exec toolgate. Human is the only kill trigger; identity re-check; shields override; mapped explanations not raw model prose. **Permission vs probability:** operator owns auto-approve thresholds; plugin never self-tunes the safety bar; host deny stays above (omp-greenlight; not a sandbox). **Spoken confirm ≠ auth:** jev-voice-browser `destructive` spoken "confirm" is convenience not a guarantee (control-port reach is the grant; rh-guard owns the gate cousin). **Privilege ≠ verdict:** effect-based shell gate; See `references/activation-triggers.md` for the rest of this row.
| Decide → policy → LLM leftover | Typed decide backends share one Answer schema; policy in code routes auto/review/llm; generator writes leftover text only. Noul 0.5 = cannot-tell, never rounded. Score conf 0.0 = flat, never acted on. Hard flags always review. **Inbox cousin:** mailordinal (typed signals → deterministic priority; no leftover LLM required). **Public decide-backend:** classifier.dev (HTTP classification API; leftover LLM is fallback when Jev is down). **Open NAR cousin:** NandhaKishorM/laya (self-hosted Choice/Score/Noul; Router picks ckpt; policy still in the caller). **Compile leftover:** byenzyme/enzyme (Decisions uses Jev; catalyst generation uses a separate LLM; See `references/activation-triggers.md` for the rest of this row.
| Closed-vote computer-use | Code builds every option from observation/goal/facts; decision model only picks; code acts/verifies/undoes. No planner LLM. Host-owned product cousin: app retains handlers/permissions; Jev over live typed actions. **Hot-click cousin:** indexed viewport table → operation+target; code owns the loop; generator only for type (ego-jev). **Adversarial cousin:** Playwright executes, Jev chooses explore/continue (browser-jev; sample not argmax). **Decider≠executor cousin:** Jev picks next-tool/progress/risk/done; LLM only fills args (jeffrey; risk≥0.5 pause; stuck ladder). **Hand no-text steps:** jev-use (plugin; writing stays with the LLM). **Never free-generates:** jev-gpt (WordNet tree of Choices; architecture demo). **OCR+AX productized cousin:** typesafe-computer-use (macOS; exclusive kinds; split questions; post-type Noul still soft; 155× *theirs* one screenshot). **ASR voice-browser cousin:** jev-voice-browser (Playwright; partial-speech wait; spoken confirm ≠ auth). **CU source-study pointer:** dairui1/jev-lab; do not re-card jev-desktop. | `references/applied-mappings.md#9-closed-vote-computer-use` |
| Agent preference lint / semantic gates | Soft project rules as criteria; linter owns hard rules; one Score per rule on the diff; bands + fail-open; name the observation window (edit vs turn). Named Choice escape when conflict ≠ ignorance (typed-evaluation-collapse). Sentence-as-rule cousin: ast-grep `rule:` × Jev `ask:` (mizchi/jev-lint is mizchi/jevlint rename; ~1 in 5 findings wrong *this README*; 13/15 1.00/1.00 older corpus; fail-open no-verdict). Independent of huntedman/JevLint | `references/mixed-architecture.md#preference-lint-and-gates` |
| Dual orchestration (Jev ∩ LLM ∩ MCP) | Jev-as-tool vs Jev-as-outer-loop; schemas are exact state | `references/mixed-architecture.md#dual-orchestration-jev--llm--mcp` |
| "It's just classification" / "not probabilistic programming" / stack-replacement FAQ | Typed judgment is a software primitive, not a new task; marginals are not a joint; Jev is not the only model. **Public pedagogy:** Akshay “Jev Clearly Explained” — LLM hammer; schema-safe ≠ correct; 200×/400× TypeSafe ceiling. **Meaning-grep:** jev-semgrep ≠ semgrep.dev; proposition≠embedding; not a gate. **Hourly 1047:** Jev never authors UI text; jevtest 0.85 still soft / ambiguous band; product bakeoff ≠ architecture duel; majority floor; HA remains execution; compaction-pi ≠ compact ≠ compaction; jevloop mock ≠ quality; Cerebellum `/v1/decide` ≠ TypeSafe; See `references/activation-triggers.md` for the rest of this row.
| Feature engineering / multi-criteria analysis | Nouls + Score distributions as named features, weights in code | `references/mappings.md#1-semantic-judgments--features-and-explicit-utility` |
| Selective classification / decision theory | Thresholds from action costs, abstention paths. Train a domain specialist when downstream code **reads the probability**; few-shot hosted API when only **argmax** matters (calibration/VOI, not an accuracy bake-off). **Active-learning triage:** high conf accept / middling expensive teacher / low-or-boundary human; log full distributions. **Do not distill Jev as teacher of record** (~68% ceiling compounds errors; real outcomes stay the targets). **SIGNAL §93:** human labels only; production capture flywheel; score never auto-accepts | `references/mappings.md#2-probabilistic-judgments--cost-sensitive-decisions` |
| Decision tables / circuits / state machines | Judgment predicates, code owns transitions. Language primitive: Ruby `chance`/`pick`/`rate` as control flow (hunch; English-as-config; fail polarity per action). feelings `.feels()` default 0.5 is Noul-0.5-never-rounded; exhaustive BAML `match`; **≠** hunch **≠** southpolesteve/probably (language primitive, not a `.feels()` overlay). apa-persona-engine SM then leftover LLM. **Hourly 1241:** s1_ruby collapse late; `undecided?` abstain; tpellet/hunch exit 3. **Hourly 1347:** typed-judge-kit verdict-in-code; judgekit YAML classify/score/route/verify | `references/mappings.md#3-semantic-predicates--decision-circuits` |
| Retrieve + expensive relevance fn | Bounded rerank of a retrieved shortlist. Decision-native RAG: retrieve wide → decide explicitly → evidence set → conflict resolve → reason only over kept evidence (embeddings stay candidate generators; no universal benchmark). **Capability tree:** NiazMorshed2007/jcr applies the same sandwich to documented commands (`notes.md` §116). Classify-first MCP: same sandwich on agent I/O (path/url/text → judge; main LLM opens survivors). Meaning-search without embeddings (packed parallel relevance; two-stage outline→zoom). **Meaning-grep** AND/OR/NOT over *thresholded* line Nouls; proposition≠embedding; See `references/activation-triggers.md` for the rest of this row.
| Store as semantic index (SQL / SQLite / zoxide / dataframe) | Cheap exact predicates first; typed questions on the remainder. In-engine extension (sqlite-jev / pg-jev) vs **judgment outside the store** (jevql CLI; vanilla Postgres never sees `jev()`) vs path index (joxide) vs dataframe columns (jevpandas / jevframe). **ORDER BY over probs is a ranking job:** calibration ≠ sortable; measure pairwise inversion / Score ordinality / two-decimal ties (jev-orderby-bench). **2340 upgrade:** ESCI hard probe fails four of six; jev_bool ECE 0.242 inversion 0.255; do not re-fold §60 six-gates as new (`notes.md` §104) | `references/mappings.md#4-retrieval--bounded-semantic-reranking` |
| Soft judgment inside a hard envelope | Model may only match the deterministic policy or be more conservative (bitrate ABR; query-planner override-when-confident; compaction mutations/shell operators → keep_full; stdout prune: ≤10k/JSON-diff-whole-doc untouched, then Noul; Cua-S1: plan≠execute, dry-run, fail-closed checkbox/fill; Stagehand extract: schema/completion-gate/screenshot-always-LLM then pick, else LLM; skills→oxlint: AST/precheck prove, guidance whole-file in state, remainder Noul — not a hard gate; pre-exec toolgate: allow/block/review — Jev is not authorization; guard error/timeout stops; See `references/activation-triggers.md` for the rest of this row.
| Value of information / gather as an act | Pay for another observation only if EV(decision) improves more than cost; abstain from calling *any* model when a regex already answers (meta-VOI). Fail-open wake/resume: skip the LLM turn only if the judge answers and p(wake) is low (Horvitz). Selective memory: verbatim ledger + scored recall (carryforward; rules never judged; 9×3 is a hint). Classify-first read: pay for a full agent open iff relevance (or typed question) says it might change the act (jev-sift; errors/truncation ≠ irrelevant). **Training-data VOI:** spend expensive teacher/human labels only where confidence says they change the outcome (jev-triage); See `references/activation-triggers.md` for the rest of this row.
| Signal detection / ROC | Criterion and operating point from costs and base rate, not accuracy. Operator owns the criterion; a plugin must not self-tune the safety bar (omp-greenlight 40.9% / 0 of 94 *theirs*). Exactness raises a quality floor — it must not override capability/context (slo-router). Privilege ≠ verdict (construct; `sudo status` can be safe). **Ranking ≠ calibration:** never hard-threshold raw p as a frequency (does-jev-confidence; AUC ~0.91, stated ~75% vs human ~10%). **Hourly 1347:** Jev-Calibration Platt ECE 0.117→0.052; typed-gate band [0.40,0.60] is refusal; 0.8 ≠ 80% accuracy. **OOD / AUC ≠ ECE:** sign of miscalibration flips by type (jev-ood-calibration; **Hourly 1851:** 0.5 is not a boundary; plumbline is not a leaderboard; `notes.md` §158). See `references/activation-triggers.md` for the rest of this row.
| Org / safety control structure | Sensor ≠ constraint (Leveson); STPA if the sensor lies. Capability kernel: Jev SENSOR, policy.py constraint; secrets never in agent (interlock). Host deny fires ahead of Jev prompt-suppression (omp-greenlight). Judgment ≠ permission: Jev never grants skill access (skill-broker outline). Contracts on effects, not tokens (construct). Attention filter ≠ permission gate (jev-lens). **Jev supplies evidence, code owns authority** (actiongate-jev; positive score never overrides a deterministic failure). **SEAL coverage ledger** (exception queue visible; mint ≠ product brain). **Never confidently wrong** (jev-labs; See `references/activation-triggers.md` for the rest of this row.
| Search / control loops (any domain) | Algorithm stays yours; judgment substitutes one classifier step. **Decider≠executor:** Jev picks next-tool/progress/risk/done; LLM only fills args (jeffrey; pick ≠ fill; still not a planner-writer). **Tree-of-Choices writer:** jev-gpt never free-generates (one question per word). **Pick≠write plugin:** jev-use. **1-token selector:** chakuho reads next-token mass over declared labels (not a writer). Robotics text-state (geometry-as-text, not pixels); khordoo: no graphical input; S1 flies, S2 advises without stalling; physics owns collisions; do not replace A* / a solver with a Noul. **OCR+AX desktop CU:** typesafe-computer-use (hosted Jev; See `references/activation-triggers.md` for the rest of this row.
| Spec property pipeline | Rank candidate props; checker owns validity | `references/mappings.md#10-spec-property-pipeline-hypothesis` (**Hypothesis**) |
| Alloy instance loop | Cluster CEXs; Analyzer owns in-scope truth | `references/mappings.md#11-alloy-instance-loop-hypothesis` (**Hypothesis**) |
| Runtime assurance sandwich | Abstain → RV/monitor → act | `references/mappings.md#12-runtime-assurance-sandwich-hypothesis` (**Hypothesis**) |
| DST multiverse triage | Cluster failing seeds/timelines; regress on the same seed | `references/mappings.md#13-dst-multiverse-triage-hypothesis` (**Hypothesis**) |
| Durable agent control | Resonate protocol settles promises; Jev gates inside a step | `references/mappings.md#14-durable-agent-control-hypothesis` (**Hypothesis**) |
| Assignment hybrid | Soft affinity + hard solver. **Empirical as shape:** slo-router constrained min-cost s.t. quality+SLO floors; Jev features, not the sole gate (p95 77.93→490.38 same routes *theirs*) | `references/mappings.md#15-assignment-hybrid--soft-affinity--hard-solver-hypothesis` (**Hypothesis**; slo-router Empirical as *shape*) |
| Situated density (Shirky) | Aggressive soft loops only inside a named community | `references/mappings.md#16-situated-density-shirky-hypothesis` (**Hypothesis**) |
| Input brittleness / paraphrase stability | Synonymous wording that swings p → abstain or rewrite. **Preregistered framing measurement** (jev-reliability) | `references/mappings.md#17-input-brittleness--sensitivity-calibration-selective-abstention-hypothesis` (**Hypothesis**) |
| Structural prove ∩ soft remainder | Allowlist *proves* the easy verbs; judge only unlisted leftovers; fail-open (cannot block). Effect-based cousin: fast-allow/deny <1ms then Jev remainder, **fail-closed** on execution (construct-auto-classifier). **Wrap cousin:** rules first then Jev remainder, ASK throws, **fail-closed** on execution (AgentGhost) | `references/mappings.md#18-structural-prove--soft-remainder-hypothesis-as-domain-general-empirical-as-named-shapes` (**Hypothesis**; jevgate/OCR shapes Empirical; construct Empirical as certification; AgentGhost Empirical as README wrap) |
| Effect-oriented state-machine loops | Soft predicates on transitions; code owns the transition | `references/mappings.md#19-effect-oriented-state-machine-loops-hypothesis` (**Hypothesis**; ZIO client, not Effect.ts) |
| Agent self-supervision / on-track detection | Pre-gate → output judge → done-check → supervisor nouls. S1 reflex keeps control; optional S2 is one-use advice (khordoo delta: never stall; log consumption; Local ≠ localjev; 20% still soft). **OCR+AX desktop CU:** typesafe-computer-use (never screenshot-to-frontier for the decision; `done` ≠ success; 0.4/0.5 still soft). **ASR voice-browser:** jev-voice-browser (never waveform-to-Jev; spoken confirm ≠ auth). Claim/evidence Stop (anti-hallucinated-done); See `references/activation-triggers.md` for the rest of this row.
| Optimizer/program frameworks (Ax, DSPy) | Typed fields → one provider request; judge metrics; threshold discipline. Ax and DSPy climb LM-program knobs only. Typed control plane sits *around* DSPy (ontology/security/confidence/state/allow-list); DSPy drafts AFTER route+action. **Full-distribution critic (no LM):** jevloop UCB1+CEM over edit ops in code; mock mode default (control-loop demo, not a Jev quality headline). **GEPA alignment loop:** human labels only; score never auto-accepts; production capture flywheel; sutro-sh/jev-align ≠ caiovicentino/jev-align; GEPA + System One | `references/optimizer-integration.md` |
| Perception → decision pipeline / measure / hill-climb | Stages with a versioned state contract; frozen taskset; DSPy/Ax only on the LM-program slice. Specialist composition stays **Hypothesis**; open multimodal decide (blackwood-rlcd) is a named receipt. Structured observe→decide→verified-act (no screenshots) is a computer-use speed-layer receipt (Jev or GLiNER2 or Cua-S1 specialist; Cua-S1 source-only, not TypeSafe Jev). Stagehand experimental Jev is the same job inside a major harness (pick-and-copy extract; 37/75 no-LLM ~0.5s vs 4.37s is *their* card; pick ≠ replacement). **OCR+AX desktop:** typesafe-computer-use (MIT **427★**; hosted Jev; $0.0002/155× *theirs* one screenshot, not a taskset). **ASR voice-browser:** jev-voice-browser (MIT **103★**; 27/27 fixtures *theirs*). **Laya-class vision:** thaitea/laya-vision-smolvlm-256m (SmolVLM; `score` untrained; CC-BY-NC-SA; **≠** blackwood **≠** Archer). **Frozen-VLM logit harness:** yoheinakajima/glance (Apache-2.0; local Qwen3-VL-4B readout; harness not weights; soft scores ≠ hard gates; `notes.md` §147). Same section as the row below | `references/validation.md#eval--hill-climb` |
| Eval & hill-climb | Decision-stage jevals hygiene; Harbor taskset × harness × runtime; one score-composition table. Shared bake-off exemplar: open-jev-laya-bench (ECE/NLL/Brier; LLM-as-judge is not the score). Harbor-style frozen protocol vs constrained LLMs: DMB (accuracy/calibration/latency/cost; See `references/activation-triggers.md` for the rest of this row.
| (meta) Finding new mappings & applications | Toolbox sweep: judgment-shaped component of a known method, substituted + falsified. **Hourly 1241:** groundedness-judge-bench native vs schema-guided; jev_playground 0 promotions; jsort scores are relative; jevbrain AUTO_ACT is not a Noul. **SIGNAL §94:** compile-time catalysts ≠ summaries; unofficial JA JGLUE *theirs*; NAR/multimodal *theirs*. **Hourly 1541:** difficulty + policy thresholds + JSONL trace; quarry evidence projection; one-dollar-tahoe TypeSafe Jev defense eval; llama-jev llama.cpp replica. **Hourly 1740:** Decision Graph Protocol frame→assess→commit; jegrep calibrated path+range Nouls; no embeddings/index/daemon; See `references/activation-triggers.md` for the rest of this row.
| Named methods / operators / theorems | Substitution tiers: operand-judgments, preconditioned theorems, non-substitutable. **Hourly 1241:** ZHUBoer/ego-jev reserved `__none__`; jsort scores are relative; groundedness-judge-bench native vs schema-guided; jev_playground 0 promotions | `references/methods-catalog.md` |
| (meta) Where a judgment model sits relative to any construct | 11 positions + logical-operator rules + position×construct traversal as the application generator. **Hourly 1241 items 49–61** (`notes.md` §90). **SIGNAL §93 items 80–81** (`notes.md` §93): Decision ledger / memoization; GEPA alignment loop. **SIGNAL §94 items 82–84** (`notes.md` §94): Compile-time System One / questions-as-index; unofficial JA ModernBERT; See `references/activation-triggers.md` for the rest of this row.
| Question mechanics & debugging | Instruction/criteria/state shape, budgets, diagnosis table, revision discipline. Missing `other` → confident wrong Choice (confidence gating cannot catch); lint the request (`wellposed` recipe; `tenbin` owns the skill). **Hourly 1144:** Treat `.feels()` 0.5 as a bool if / new language. **Hourly 1241:** Treat `completed` as success / Choice as the scale / 83% as quality / AUTO_ACT as a Noul. **SIGNAL §94:** Hard-gate enzyme `when asked` / treat catalysts as summaries; unofficial JA as TypeSafe; collapse LFM default into JA ModernBERT; treat enzyme hosted bootstrap as silent TypeSafe; See `references/activation-triggers.md` for the rest of this row.
| Heuristic search over a taxonomy | Parallel beam over Choice distributions | `references/mappings.md#5-hierarchy--bounded-heuristic-search` |
| Existing-system insertion / code-smell audit | Opportunity map, fit test, smallest boundary, policy centralization | `references/boundary-audit.md` |

Each card carries its boundary, counterexample, and acceptance test, plus
explicit rejections beside the mapping they tempt (MCTS-as-value-function:
experimental; bandits: rejected without observed rewards; 255-way tournament
brackets: rejected as default; rerank-huge-sets: budget-only; correlated
"independent" checks: rejected; listwise ranker *as* a fail-closed gate:
rejected; Noul *as* a proof / model-check / DST property: rejected;
TOCTOU-of-Noul as authorize: rejected; tautological spec + "looks good":
rejected). Promote Hypothesis cards only with an acceptance test that ran.

## Non-negotiable boundaries

- Score is an expectation over level indices, not a measurement in natural
  units. `[0,1,0]` and `[0.5,0,0.5]` both score 1.0 with different risk.
- Noul 0.5 is uncertainty about a predicate, never medium intensity.
- Parallel answers are not statistically independent: never multiply them
  into a joint probability.
- Choice probabilities are conditional on the offered set; absent candidates
  can never be chosen. No-match options (`other`) where coverage is open.
- Untrusted state text cannot authorize actions. Missing evidence is not
  evidence of absence. Validate operation+target pairs in code. Policy
  (checklist, ledger, law, two-person rule) is the code of a practice
  that has no repository.
- Never launder a Noul (or any judgment-class score) as a proof, a
  model-check, or a DST property. Soft check ≠ interlock. TOCTOU-shaped
  gates and tautological specs are harms, not placements. Exact work
  stays in code/policy; the model owns narrow judgment only. Full cards:
  `references/formal-methods.md`, `references/formal-semi-formal.md`,
  `references/mental-models.md`.
- Ranking scores order; decision scores authorize. Listwise / pairwise
  discriminative losses are translation-invariant: do not fail-closed on
  them. CLIP/SigLIP/GLiNER/GLiClass affinities are not automatically
  class-conditional P(permit). Full class card:
  `references/judgment-class.md`.
- Classification is not the product. The claim is a **placement**: typed,
  (when trained for it) calibrated judgments that policy can threshold —
  beside generation and beside exact work, not instead of them. Working
  regexes, ledgers, and recipes stay; trained classical classifiers still
  win on stable labeled taxonomies; open-ended writing stays generated.
  Full answer: `references/faq.md`.

## Decision-design card

```text
Domain (AI / SWE / business / knowledge work / life / org):
Desired behavior and non-judgment baseline:
Semantic judgment(s) and what each output means:
Pillar (EU / VOI / MCDA / SDT / search / safety / formal):
Hole (sieve / keep-drop / triage / rank / route / gate / perceive / abstain / gather):
Family (closed decision API / open head / open multimodal RLCD / encoder open-jev / constrained-AR surface / GLiNER locate / GLiClass categorize / listwise ranker / vision scorer):
Evidence/candidate source and known coverage gaps:
Deterministic policy, constraints, and action ownership:
Batchable vs genuinely dependent steps:
Failure/abstention behavior (fail-open vs fail-closed, matched to the family):
Smallest experiment that could reject this family, not just this vendor:
Eval path (jevals-shaped held-out and/or Harbor taskset; missing = incomplete):
Typed judgment provider (TypeSafe Jev default; other family only with self-eval):
Live references + versions (model, rubric, policy):
```

For open-ended requests propose three materially different *placements of
judgment*, recommend one. Cross-domain frames:
`references/mental-models.md`. Mixed-architecture extras:
`references/mixed-architecture.md`. Family-choice extras:
`references/judgment-class.md`. Formal / proof / DST:
`references/formal-methods.md`. Applied SWE placements (sieve, keep/drop,
env triage, moderation/ranking, skill routing):
`references/applied-mappings.md`. Hypothesis cards (VOI, SDT, Leveson,
search/control, spec pipeline, Alloy loop, RV sandwich, DST triage,
durable agents, assignment, situated density, paraphrase stability,
structural-prove ∩ remainder, effect-oriented state-machine loops)
stay labeled until an acceptance test
runs: `references/mappings.md` §6–§19. For concrete
requests skip the brainstorm and build.

## Evidence labels

- **Contract**: current documented behavior — refresh from live docs.
- **Empirical recipe**: worked on a stated dataset/model/version — retest.
- **Hypothesis**: plausible, unestablished — label and test before relying.

Hourly 0843 uniqueness lock: A hunch is a probability with a policy attached; { enter: 0.8, exit: 0.6 } is hysteresis; replay a policy change without inference; Decision models are providers, not the product; huncho ≠ Kungie/gut ≠ carldaws/hunch ≠ tpellet/hunch; pretrained Qwen2.5 base ECE 0.030 (0.5B) / 0.040 (7B); instruct 0.302 / 0.269; 70.9% → 70.0% mean conf 74.1% → 96.7%; temperature scaling still matches it in-distribution; No Jev API was called; Qwen2.5 ≠ Archer; Qwen/Qwen3.8-27B ≠ Archer; 学習済みモデル v0.1 は準備中です; bool AUROC 0.523; 先頭だと0件、末尾だと250件; 温度を渡さない場合、確率は較正されていません; このリポジトリには Jev を呼ぶコードが存在しません; g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev (same GitHub id 1378007307); 947 repos scored; A 273 · B 302 · C 372; LLM rubric ≠ benches; Data as of 2026-09-20; HEAD 895b9498; README SHA 3ae98c56; 13 focused checks and one mutually exclusive outcome; Probabilities are advisory, not calibrated guarantees; omni-/ask-jev ≠ pedroknigge/mcp_jev; pd.cut bins by equal width while jeval bins by quantile; ECE 0.113 and ECE 0.076; jeval drift is not implemented yet; rlaope/jeval ≠ dayhaysoos/jevals; calibration does not compose; ECE has exactly zero statistical power to detect the failure mode that kills trajectories; 25–60× headline withdrawn; P(all-correct): 0.0071 vs 0.0001; TCE / AMS; Qwen 3.8 sparring ≠ Archer; Deferred Crispification; light_cutoff_applied_to_combination 0; recorded run, kinematic animation; BANKING77 Accuracy BERT-Base 93.02 Jev 79.90; Analyse jev calibration (NLL, ECE) backlog; BERT figures are published supervised references, not zero-shot; 档位措辞效应 分数极差中位 0.50、最大 1.32; 修好后对照组是 0.01; 不是 benchmark; 概率没做 calibration; ~1,430 API calls, about $0.15; xiaohuaxi/jev-study ≠ wjdjdakf17/jev-study ≠ baekenough/jev-study; AND: product (independence assumed and recorded in the trace); chat model's stated confidence is not calibrated; circuit-vl-4b ≠ Archer; Bring your own API key; vamsikrishna2421/jev-usecases ≠ whyashthakker/awesome-jev-use-cases; catalog ≠ endorsement; SemIf 2237★ (+30 vs §111 2207); jevlike 1049★ (+6 vs 1043); TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 520★ (+14 vs 506); Laya likes 861 (was 822); tracker likes 66 (+2 vs 64) lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §114

## NanoJev unified-games-v1 densify (`notes.md` §115)

User-provided HIGH 0915 (Boise). TianyuCodings/NanoJev is an
open replica / specialist gameplay S1 — **not TypeSafe Jev**.
A 0.6B parallel decision model: states and questions in,
complete probability distributions out. Zero output-token
decoding. One model, four games. Game success ≠ calibrated
Noul. local type boolean ≠ TypeSafe noul. caijinchun/nanojev-arena
≠ liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠ NanoJev.
Do not copy `pip` / `snapshot_download` / `serve_decisions`.
Do not reopen or amend PR #31/#32/#33/#35. Merged #35 owns
§114. This fold stays §115. Skip Archer. `invented_signal: false`.
Protocol: quote *theirs*; mixed-architecture fail polarity
per act; judgment-class replica honesty.

User-provided 0915 uniqueness lock: TianyuCodings/NanoJev unified-games-v1 densify; A 0.6B parallel decision model: states and questions in, complete probability distributions out. Zero output-token decoding.; One model, four games; ViZDoom Basic 128/128 vs Jev 56/128; Predict Position 27/128 vs Jev 11/128; Maze 225 attempts vs Jev 2738; Snake 30 food / 256 steps; held-out Maze 4/10 Snake 8/8 Basic 128/128 Predict 27/128; Untuned Qwen3-0.6B baseline; 18,760 questions per variant; 16,333 ViZDoom; 896 Predict Position expert episodes; hard_lr1e5; mix weights 1/3, 1/3, 1/6, 1/6; Hub C-Tianyu/NanoJev revision unified-games-v1 likes 58; dataset C-Tianyu/NanoJev-Data likes 5; HEAD 618cea6d906d54e128360786d12f703fff2b1245; 1289★ / 158 forks / size 64035; README SHA 4190093c64ee75b26e9726daa3b00cbcf6d3157a; MIT; caijinchun/nanojev-arena ≠ liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠ NanoJev; not TypeSafe Jev; open replica / specialist gameplay S1; soft scores ≠ hard gates; Game success ≠ calibrated Noul; local type boolean ≠ TypeSafe noul; invented_signal false; do not reopen or amend PR #31/#32/#33/#35; notes.md §115


User-provided 0920 jcr uniqueness lock: NiazMorshed2007/jcr MIT; site https://jcr.niazmorshed.dev; topics ai-agents,jev,mcp; **4★**; HEAD `138b3832`; README SHA `2a49dbc1`; LICENSE SHA `46231303`; size **14850**; Jev Capability Resolver; one tool to find documented deterministic commands in a nested capability tree; returns context; **does not execute**; skills = workflow+judgment; capabilities = individual operations; format independent of Jev; proposed open standard exploration; classify (Jev) → optional OpenAI decompose compound → beam search geometric mean of routing probs; keep up to 3 paths ≥60% of best (JCR_BAND_RATIO 0.6); ambiguity / no-match / depth-limit explicit; soft scores ≠ hard gates; 0.6 band is application policy; routing ≠ permission; docs ≠ authority to run; sol-vs-opus5-20 *theirs*: 20 scenarios × 4 variants = 80 runs; lookup+explain only, no execution; Claude Opus 5: agent input 108,585→15,819 (−85%), cost $0.3700→$0.1222 (−67%), wall 105.5s→77.7s; Codex GPT-5.6-Sol: 61,952→47,669 (−23%), $0.1377→$0.1151 (−16%), wall 25.3s→62.4s (Sol slower with JCR in 19/20); One Sol outlier 372.6s / 193 Jev calls; n=1 per cell; Not Harbor task-execution; Claude/Codex harnesses; compare mode; 50 scenarios bundled; 11 groups, 960 nodes, 11,360 items; 16 routing rounds per step; NiazMorshed2007/jcr ≠ skill-broker ≠ skillranker ≠ jev-sift ≠ jev-lens ≠ jevusher ≠ jev_select_capability; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34; notes.md §116
User-provided 0922 uniqueness lock: SemIf was formerly OpenJev; independent; not affiliated with Jev or TypeSafe; homepage openjev.com; default master; MIT; HEAD ca3ba65f1429; Tolerate float roundoff in MLX evidence verification; pushed 2026-09-19; live REST 2282★ / 140 forks; size 9177; README SHA 74ab7f7f; LICENSE SHA ca562883; interface pattern reproduction with open models; does not reproduce Jev undisclosed model/training; Direct option logits; 0 output tokens; shared-state parallel; MLX backend for Apple Silicon (`--backend mlx`); Qwen3.5-4B 3090 direct 1.023s vs AR JSON 5.332s (**5.21×**); argmax agree 18/21; systems comparison ≠ semantic equivalence; Parallel suffixes 20.03 dec/s on 777 decisions; Browser ladder Qwen3.5-4B authored BA 0.813, pert 0.766, TypeSafe subset agreement 0.845 vs Published Jev 0.883 (102 across 20 cases); Softmax over options ≠ calibrated Noul; typed output does not guarantee semantic correctness; wire/agreement ≠ replica of TypeSafe; SemIf ≠ kw2828/OpenJev playground ≠ zhihz/openjev ≠ apiplant/semif-rs port ≠ dddanielliu/semif-serve; rename is densify not a second census; JevBench 74.6 is §78 not this ladder; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#38; do not push onto open #39/#40; notes.md §117
User-provided 0940 uniqueness lock: Turn decision-shaped LLM prompts into proposed Jev primitives; This is a conversion assistant, not an automatic guarantee of equivalent behavior; The compiler uses deterministic heuristics, not an LLM or evaluation model; It understands a deliberately small set of common prompt patterns; Generated instructions and criteria must be reviewed before production use; Score ranges such as 0 to 1 are translated into ordered Jev criteria; Prompts requiring open-ended prose are not a fit; suitability strong/partial/not_a_fit; compatibility full/partial/none; Writing new text stays with an LLM; Review the generated Score rubric; Jev scores ordered criteria, not an arbitrary 0-to-1 range; Everything runs locally in the browser; There is no framework, database, account, API, or server-side prompt processing; The key is read from the process environment and is never stored or printed; connect-src 'none'; alexwestco/llm-to-jev ≠ altryne/jevify ≠ ryana/jevify ≠ fidecastro/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; HEAD 234058ab372d; README SHA 43cd94fb; LICENSE SHA 5f334006; compiler SHA fdf235d0; 2★; MIT; JavaScript; size 29; Pages https://alexwestco.github.io/llm-to-jev/; invented_signal false; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §118
## Hourly 0947 HIGH (`notes.md` §119)

jev-as-judge / OneForward readout / catalogs / replay /
RLCD heads. judge ≠ actuator. softmax over A–H ≠ Noul.
candidate_mass. Qwen3.5-2B ≠ Archer. Qwen3.5-4B ≠ Archer.
catalog ≠ endorsement. Status: no model yet. Exit 1 is
not a proof. Do not copy keys. Rebased onto `fb15455`
(merged #42 v0.5.0) after `38e4e92` (#39 hygiene). Do not
reopen or amend PR #23–#40. Does not bump 0.5.0.
Skip Archer. `invented_signal: false`.


## Hourly 1049 HIGH (`notes.md` §120)

ggmlc GGUF is not llama.cpp. serving substrate ≠ calibrated replica.
Qwen3.5-9B ≠ Archer. planner writes JEV selects. pick_by_id vs pick_second.
Soft scores ≠ hard gates. catalog ≠ endorsement.
Do not copy keys. Rebased onto `8f446c4` (merged #41) after
`fb15455` (merged #42 v0.5.0). Do not reopen or amend PR #23–#42.
Does not bump 0.5.0. Skip Archer. `invented_signal: false`.



## Hourly 1143 HIGH (`notes.md` §121)

open recreation ≠ calibrated replica. semantic lint is a sensor not a proof.
cutoff 0.8 still soft. paired bootstrap CIs *theirs*.
Same accuracy, 35x faster *theirs*. systems comparison ≠ semantic equivalence.
wire-compat ≠ replica. permission ≠ confidence. catalog ≠ endorsement.
Qwen3.5-4B ≠ Archer. Do not copy keys. Fresh PR off `a61372f` (merged #43).
Do not reopen or amend PR #23–#43. Does not bump 0.5.0. Skip Archer.
`invented_signal: false`.

Hourly 0947 uniqueness lock: Fast and cheap agent evals. jev as judge.; 18,041 skills from the 200 most-starred repos; Not a security scanner; 最简 Jev 调用演示器; confidence 不是正确率; q93304989-bit/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; 75% cheaper and 18% faster withdrawn; jev @0.15 100% recall 87% savings; 33Audits/jev-auto ≠ gargpratyush/jev-router; no Typesafe key, no PI_API_BASE, zero deps; tool-emitted Score/Noul ≠ calibrated Noul; semantic_compatibility: false; candidate_mass; Qwen3.5-2B ≠ Archer; Jev evaluates decisions; it cannot run a coding-agent session; Status: no model yet; S1LV3RJ1NX/openjev ≠ TheoLeeCJ/openjev; 28 accepted decisions; 3 targets; score 800; health 100; arcade game not a flight trainer; A successful live TypeSafe call has not been verified for v0.1.0; abhibansal60/tidy ≠ MANISH007700/tidy; No model, Jev included, predicted which channels its owner keeps; seed 1 selected on a held-out 400-item validation split; Brier 0.342 → 0.378; more accurate and more overconfident; Qwen3.5-4B ≠ Archer; static quants of kushalpatil/jevify-gemma4-26b-a4b; The labels were corrected, and one earlier result was retracted; zero of 23,869 eligible rows; Do not compare cost without checking task success; Exit 1 is not a proof; kisshan13/typesafe-ai-go ≠ Nibir1/typesafe-go ≠ official; 38 tests that cannot fail in a 356-model warehouse; if a parser can answer it, Jev is never asked; 359 of them; Games & Simulation 82; Education & Learning 1; Ratings are heuristics; syedabbasshaheer-art/jev-atlas ≠ ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas; anandi1989/awesome-jev-usecases ≠ whyashthakker/awesome-jev-use-cases ≠ walidboulanouar/awesome-jev-use-cases ≠ vamsikrishna2421/jev-usecases; Every headline result above is self-reported; Archer Hume 84.6% MMLU-Pro is a third-party probe not landed Archer; catalog ≠ endorsement; judge ≠ actuator; softmax over A–H ≠ Noul; SemIf 2270★; jevlike 1054★; TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 538★; Laya likes 889; tracker likes 68 lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#35/#36/#37/#38/#40; do not push onto open #39; notes.md §119
Hourly 1049 uniqueness lock: ggmlc GGUF is not llama.cpp; Loading them in llama.cpp will fail; one encoder pass; hf:mys/laya-GGUF sha 713ae6f6e39f likes 0 apache-2.0; hf:mys/laya-multilingual-GGUF sha 3b645ae54281; hf:mys/laya-typed-decisions-GGUF sha 1e9e8ba1f527; hf:tozp/laya-onnx sha 0862aeba1e65 Opset 14 FP32 and INT8; tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; docker-laya MIT HEAD 1b8239a51ddd README SHA 9cb7bdc3; laya.cpp RTX ggml CUDA HEAD 8590937c79a2 README SHA cdd429b9; serving substrate ≠ calibrated replica; Softmax over options ≠ calibrated Noul; Qwen3.5-4B ≠ Archer; Qwen3.5-9B ≠ Archer; jev-position-test n=6 HEAD 7a56ca1c2698 README SHA 23f194c9; jevmlx slots 5 of 6; hosted Jev 0 of 6; prior_correction made it worse; jevSweeper mean Spearman ρ −0.274; picked exact-optimal 1/25 (4%); 31 of 36 still logically decidable; 86% of the time we should not have been asking; game success ≠ calibrated Noul; LLM2Jev 64★ Apache-2.0 HEAD 924618721277 README SHA da35fe61; not affiliated with or endorsed by Jev or TypeSafe; No answer tokens are generated; OpenSourceJev llama.cpp Qwen3-1.7B HEAD 3c41fba3681d; JEV-MLX Qwen3.5-9B HEAD dec24cd929ea; decision-head-rlcd Qwen3.5-4B 4.9M LoRA; AUTO_ACT is not a Noul; closed-set fail-open stdlib-only; verified=False; soft scores ≠ hard gates; 22 to 40% cheaper *theirs*; first version 70% more expensive; 111-case benchmark *theirs*; CDC 5,000 Jev 72.2% AUC 0.7725 *theirs*; accuracy is a trap; 9.0% base rate always-no 91.0%; catalog ≠ endorsement; jev-skill 109★ 90 scenarios HEAD 4f6e899a24d4; awesome-jev-live 673 entries 4★; minecraft-agent 214★ 131 JEV decisions 35 Astra calls; nether-final-08 8 minutes 43.300 seconds; planner writes JEV selects; RoboJEV structured simulator state not images; ashare-trader 策略未通过自己的回测门槛; 36 组参数全部净期望为负; no positive expectation under real costs; typed_evals NOT an official TypeSafe AI product; jev-as-judge is a sensor; third-person-audit 40% & 60% watermarks still soft; The included experience uses a handwritten demo provider; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42; notes.md §120


**Hourly 1143 HIGH (`notes.md` §121).** open recreation ≠ calibrated replica. semantic lint is a sensor not a proof. cutoff 0.8 still soft. paired bootstrap CIs *theirs*. Same accuracy, 35x faster *theirs*. systems comparison ≠ semantic equivalence. serving substrate ≠ calibrated replica. catalog ≠ endorsement. permission ≠ confidence. Do not reopen or amend PR #23–#43. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1143 uniqueness lock: open recreation ≠ calibrated replica; Qwen3.5-4B ≠ Archer; It is an open re-creation of Jev; less calibrated; perch 164★ MIT HEAD ba775a9940b6 README SHA 7ad0403b; semantic lint is a sensor not a proof; oxlint-plugin-jev cutoff 0.8 still soft; nassim-arifette/jevgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; patdown fuzzy linter; PanAchy/jevvy ≠ Atominac/jevvy; No orders, no advice; SmartMoney-Cub 25★ HEAD d93cf493853d; paired bootstrap CIs *theirs*; emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; +0.82 pts XQuAD-EN 95% CI +0.35 to +1.31; +7.62 pts SciFact CI +4.88 to +10.38; Same accuracy, 35x faster *theirs*; systems comparison ≠ semantic equivalence; BANKING77 500 Jev 81.0% GPT-OSS 82.8% Mercury 73.2% Gemini 85.4% *theirs*; frozen cascade missed its evaluation accuracy target 430/500 vs GPT-5 432/500; This is not demonstrated equal-quality savings; 24 invented tickets; Routing errors caught by the gate 0 of 3; sample too small to establish calibration; This is not TypeSafe Jev; No real API requests were made; wire-compat ≠ replica; KonghaYao/laya-jev 按官方接口写的客户端只改一个 base URL; gqgs/laya-onnx densify 496.8 MiB; tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; serving substrate ≠ calibrated replica; BeatAPI/awesome-jev ≠ 99hansling/awesome-jev ≠ Vishnurr2k01/awesome-jev ≠ robokrunch/awesome-jev ≠ rudy2steiner/awesome-jev-hub; All 125 projects; catalog ≠ endorsement; Pasblinn/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab ≠ q93304989-bit/jev-lab; Independent project. Not affiliated with TypeSafe; Kevthetech143/super-jev densify experimental V0.2.0; permission ≠ confidence; allay-team/openjev ≠ piyush-infocusp/openjev ≠ TheoLeeCJ/openjev; 2022 Mineflayer Jevalent collision; kushalpatil/jevify-gemma4-e4b GGUF densify; static quants; This dataset and model are independent research artifacts, not reproductions of Jev or RLCD; pngwn demo accuracy 0.705 ECE 0.046 ~112 ms *theirs*; cutoff 0.8 still soft; soft scores ≠ hard gates; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43; notes.md §121

**Hourly 1248 HIGH (`notes.md` §123).** decide is not generate. tryDecide returns typed calibrated judgments not a token stream. GLiNER/GLiClass ports are class members not Jev replicas. 93.5% *theirs* not Harbor. 74.9 *theirs* not Harbor. 8.7x *theirs* not Harbor. wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#45. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1248 uniqueness lock: decide is not generate; tryDecide returns typed calibrated judgments not a token stream; juspay/neurolink 133★ MIT HEAD 268b0fe83130 README SHA e709cadfa6b6 tag v12.19.0; GLiNER/GLiClass ports are class members not Jev replicas; MacPaw/Gliner2Swift ≠ Knowledgator/GLiClass.c ≠ fbilhaut/gliclass-rs ≠ Knowledgator/GLiClass.js ≠ gravitee-io/GLiNER4j ≠ apiplant/gliner-rs ≠ codesoda/gliner2-rs; 8.7x faster 4.4x fewer prompts *theirs*; 153 was a reporting error; corrected 156-case 9.8x faster 4.2x fewer prompts *theirs*; independent v0.2.1 1.24x vs Mini *theirs*; Approvals only; anpicasso/hermes-jev-approvals ≠ hermes-switchyard; scx-router GLiClass ranks candidate LLMs in one non-generative pass; typesafeai-dotnet-sdk Not affiliated with TypeSafe AI; hyperspaceai/jevcache ≠ kushals256/jevcache; ST-jeved measures each reply; 400 plain-text for unaskable question; razorback16/openjev:0.2.1 Docker densify HEAD 794a81b87131; wire-compat ≠ logit-equiv; Option-Marker joint attention 93.5% macro *theirs*; 93.6% micro *theirs*; n=78; T = 1.0367 vs T = 1.1692 two temperatures; guaranteeing is soundness theater; wfzyx/von densify HEAD bed7e7337791; Benchmark Heaven leaderboard #2 74.9 *theirs*; NLL calibration assets; 77.10% still §71 claim-audit; do not re-fold as a beat; Heman10x-NGU/openJev-verdict-2.0 densify HEAD bff28567cff4; kev-family weight tarballs; PLAN_Qwen35 proposal for review; deadline 0.53→0.82 at 9B *theirs*; Qwen3.5-9B ≠ Archer; isolation would fail by construction on DeltaNet; jaredpalmer/kev densify; JevBench v1.2.2 jeff 66.9 (#9) jev 75.3 (#2) *theirs*; logan-markewich/jeff densify HEAD 34b32f99a727; thinking=True/False per-field budget; type safety does not guarantee factual accuracy; TypeLLM/TypeLLM densify HEAD c4b03ba9e792; us/jev-local stub until hf; Eran-BA/Jev_from_GLiNER2 spec ≠ replica; lsu-ub-uu/systemone ≠ TypeSafe System One; Layan/Laya HF spaces name-match; catalog ≠ endorsement; decide ≠ generate ≠ stream; 93.5% *theirs* not Harbor; 74.9 *theirs* not Harbor; 8.7x *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45; notes.md §123

## Hourly 1248 HIGH (`notes.md` §123)

decide is not generate. tryDecide returns typed calibrated judgments not a token stream.
GLiNER/GLiClass ports are class members not Jev replicas.
93.5% *theirs* not Harbor. 74.9 *theirs* not Harbor. 8.7x *theirs* not Harbor.
wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement.
Qwen3.5-9B ≠ Archer. Do not copy keys. Fresh PR off `1c9c367` (merged #45).
Do not reopen or amend PR #23–#45. Does not bump 0.5.0. Skip Archer.
`invented_signal: false`.

**Hourly 1248 HIGH (`notes.md` §123).** decide is not generate. tryDecide returns typed calibrated judgments not a token stream. GLiNER/GLiClass ports are class members not Jev replicas. 93.5% *theirs* not Harbor. 74.9 *theirs* not Harbor. 8.7x *theirs* not Harbor. wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#45. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1248 uniqueness lock: decide is not generate; tryDecide returns typed calibrated judgments not a token stream; juspay/neurolink 133★ MIT HEAD 268b0fe83130 README SHA e709cadfa6b6 tag v12.19.0; GLiNER/GLiClass ports are class members not Jev replicas; MacPaw/Gliner2Swift ≠ Knowledgator/GLiClass.c ≠ fbilhaut/gliclass-rs ≠ Knowledgator/GLiClass.js ≠ gravitee-io/GLiNER4j ≠ apiplant/gliner-rs ≠ codesoda/gliner2-rs; 8.7x faster 4.4x fewer prompts *theirs*; 153 was a reporting error; corrected 156-case 9.8x faster 4.2x fewer prompts *theirs*; independent v0.2.1 1.24x vs Mini *theirs*; Approvals only; anpicasso/hermes-jev-approvals ≠ hermes-switchyard; scx-router GLiClass ranks candidate LLMs in one non-generative pass; typesafeai-dotnet-sdk Not affiliated with TypeSafe AI; hyperspaceai/jevcache ≠ kushals256/jevcache; ST-jeved measures each reply; 400 plain-text for unaskable question; razorback16/openjev:0.2.1 Docker densify HEAD 794a81b87131; wire-compat ≠ logit-equiv; Option-Marker joint attention 93.5% macro *theirs*; 93.6% micro *theirs*; n=78; T = 1.0367 vs T = 1.1692 two temperatures; guaranteeing is soundness theater; wfzyx/von densify HEAD bed7e7337791; Benchmark Heaven leaderboard #2 74.9 *theirs*; NLL calibration assets; 77.10% still §71 claim-audit; do not re-fold as a beat; Heman10x-NGU/openJev-verdict-2.0 densify HEAD bff28567cff4; kev-family weight tarballs; PLAN_Qwen35 proposal for review; deadline 0.53→0.82 at 9B *theirs*; Qwen3.5-9B ≠ Archer; isolation would fail by construction on DeltaNet; jaredpalmer/kev densify; JevBench v1.2.2 jeff 66.9 (#9) jev 75.3 (#2) *theirs*; logan-markewich/jeff densify HEAD 34b32f99a727; thinking=True/False per-field budget; type safety does not guarantee factual accuracy; TypeLLM/TypeLLM densify HEAD c4b03ba9e792; us/jev-local stub until hf; Eran-BA/Jev_from_GLiNER2 spec ≠ replica; lsu-ub-uu/systemone ≠ TypeSafe System One; Layan/Laya HF spaces name-match; catalog ≠ endorsement; decide ≠ generate ≠ stream; 93.5% *theirs* not Harbor; 74.9 *theirs* not Harbor; 8.7x *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45; notes.md §123

## Hourly 1340 HIGH (`notes.md` §124)

typesafe-sdk 0.7 Pydantic response models. msgspec dropped.
The server's output is unchanged and was never wrong.
MLX backend 400 plain-text error contract.
SchemaError is 400 plain-string detail not 422 list.
Pydantic response models ≠ logit-equiv. msgspec dropped is not a replica.
Error contract is not a Noul. PLAN_Qwen35 densify.
coverage-at-error-budget *theirs* not Harbor.
GLiNER locate ports are class members not Jev replicas. Locate ≠ decide.
Jev-Vision skip 0.936 effect 0.967 done 0.896 157 ms *theirs*.
~160 ms *theirs* not Harbor. 0.971 F1 *theirs* not Harbor.
hf:fr0stbit3/laya-gguf serving substrate ≠ calibrated replica.
jkcdarunday/SystemOne-Next ≠ TypeSafe System One.
wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement.
Qwen3.5-9B ≠ Archer. Do not copy keys. Fresh PR off `2d67227` (merged #46).
Do not reopen or amend PR #23–#46. Does not bump 0.5.0. Skip Archer.
`invented_signal: false`.

**Hourly 1340 HIGH (`notes.md` §124).** typesafe-sdk 0.7 Pydantic response models. msgspec dropped. MLX backend 400 plain-text error contract. Pydantic response models ≠ logit-equiv. msgspec dropped is not a replica. Error contract is not a Noul. PLAN_Qwen35 densify. coverage-at-error-budget *theirs* not Harbor. GLiNER locate ports are class members not Jev replicas. Locate ≠ decide. ~160 ms *theirs* not Harbor. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#46. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1340 uniqueness lock: typesafe-sdk 0.7 Pydantic response models; msgspec dropped; The server's output is unchanged and was never wrong; MLX backend 400 plain-text error contract; SchemaError is 400 plain-string detail not 422 list; razorback16/openjev densify HEAD 6e91dfc031bc README SHA cbdcc8de0304; Pydantic response models ≠ logit-equiv; msgspec dropped is not a replica; Error contract is not a Noul; wire-compat ≠ logit-equiv; PLAN_Qwen35 densify; corrected Qwen3.5 LoRA target names verified; in_proj_qkv in_proj_z in_proj_a in_proj_b out_proj; peft 0.21 existence proof; OOD-calibration study; coverage-at-error-budget metric in Phase 0; PLAN_Qwen35 still proposal for review; deadline 0.53→0.82 at 9B *theirs*; isolation would fail by construction on DeltaNet; Qwen3.5-9B ≠ Archer; jaredpalmer/kev densify HEAD 75cc15ddb8e2 PLAN SHA eca543246f50; GLiNER locate ports are class members not Jev replicas; urchade/GLiNER ≠ fbilhaut/gline-rs ≠ lmoe/gliner-onnx.js ≠ shershah1024/gliner-native-runtime; Locate ≠ decide; Jev-Vision skip 0.936 effect 0.967 done 0.896 157 ms *theirs*; ~160 ms *theirs* not Harbor; 0.971 F1 *theirs* not Harbor; coverage-at-error-budget *theirs* not Harbor; hf:fr0stbit3/laya-gguf serving substrate ≠ calibrated replica; jkcdarunday/SystemOne-Next ≠ TypeSafe System One; catalog ≠ endorsement; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46; notes.md §124

## Hourly 1746 HIGH (`notes.md` §128)

TypeLLM/TypeLLM densify HEAD 702e6a287f3c README SHA 08180db0450b.
truncated thinking then constrained decode.
typellm_runtime.py typellm_sglang.py. evals/qwen35_small.
0.8B thinking On 0/18 *theirs*. forced closure 20/20 type-valid *theirs*.
Constrained AR ≠ calibrated Noul. type safety does not guarantee factual accuracy.
Qwen/Qwen3.8-27B ≠ Archer.
jaredpalmer/kev densify live HEAD 8465c4c4c294 watch 38087aa0301d README SHA 19664b9ae546.
Kev-0.8B completes family. Kev-0.8B 4B 9B Qwen3.5.
4B new-source 0.794/0.832 *theirs*. 9B new-source 0.812/0.837 *theirs*.
transfer-v9 Kev-9B 5% Jev 9% Kev-8B 26% *theirs*.
SemIf Kev-9B 0.917 Jev 0.965 *theirs*. scienthoon 0.952/0.911 vs 0.897/0.914 *theirs*.
transformers >= 5.17. Qwen3.5 ≠ Archer.
notque/vexjoy-agent 421★ /d routes /do fallback.
tamaratran/jev-pruner densify HEAD 47d017c34eab.
qkal/Canny Facts go to code. Judgments go to Jev. Only facts can block.
Jev never blocks.
jqueryscript/awesome-jev 231 entries catalog ≠ endorsement.
jqueryscript/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev.
jamescazzetta/five-lines threshold 0.80 still soft.
eugeniughelbur/jev-engineering 371ms $0.0000189 300-call *theirs*.
tpellet/jevify ≠ altryne/jevify. seb4ez/jevguard-mcp ≠ seb4ez/jevguard.
resumocast/jev-mcp ≠ jkudish/jev-mcp. dtduc-git/jev-table first sighting.
Adrian-Ernesto/jevsort ≠ zzzzzec/jevsort.
MidasMulli/kev-ane 155/155 argmax *theirs*. MidasMulli/kev-ane ≠ jaredpalmer/kev.
serving substrate ≠ calibrated replica. empty repo skip-thin.
loktar00/llm-lan-party empty repo. rh-guard owns primary gates.
wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement.
Archer still promised_not_landed. Hub archerhume/4rcherhume HTTP 401.
Do not copy keys. Fresh PR off `0f8279e` (merged #50).
Do not reopen or amend PR #23–#50. Does not bump 0.5.0. Skip Archer.
`invented_signal: false`.

## Hourly 1643 HIGH (`notes.md` §127)

razorback16/openjev densify HEAD febf02e88989 README SHA 242a737dba01.
release 0.3.0. re-pin vLLM PR #57250 restructured head.
VLLM_COMMIT baa8338. pyproject and __init__ agree 0.3.0.
MODEL_VERSION stays openjev-0.1. uv.lock hygiene.
restructured vLLM head ≠ logit-equiv.
dual serving is not generate. Hosted Codiv ≠ TypeSafe.
wire-compat ≠ logit-equiv. SHA move is not a replica.
Error contract is not a Noul.
frostney/clean-code-review 7★ typed judgments not opinions.
documentation is read not judged. Luna writes from Jev findings.
morcoan/JMP Joint Model Participation.
Models participate. Real tools execute.
Jev routes actions generators supply arguments. not a swarm.
zkjoie/jevbus Thresholds are policy not model.
Drop < Review < Deliver. FanOut or Exclusive.
Kelbie/hunch ≠ carldaws/hunch ≠ tpellet/hunch ≠ huncho.
Agent Skills semantic review.
SupratikB23/JevCanvas Jev never generates prose JSX or code.
Diffusion never decides structure. json-render is the only renderer.
skcache/jevtrafficsim Fixed Adaptive Jev. game success ≠ calibrated Noul.
Shalimov04/open-jev ≠ razorback16/openjev ≠ TheoLeeCJ/openjev ≠ Zefan-Cai/Open-Jev.
MstyAI/laya-onnx empty repo ≠ tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx.
SherifAshraf2003/jev-use ≠ shitianfang/jev-use.
aniruddh-krovvidi/switchboard ≠ cannacre8ive/switchboard-ai.
Visorian/TidyUp ≠ abhibansal60/tidy. isiomaC/jevkit ≠ WaynezProg/jev-kit.
lee-lou2/jev-tree ≠ reachjalil/jev-tree. Royhu1/jev-poker-trainer empty repo.
JoacoMarc/jev-harness-router ≠ jackbarunz/jev-tool-router.
rh-guard owns primary gates.
hf:Praveenrajus/jev-bench HTTP 200 was 401.
hf:ZefanCai/Open-Jev densify dataset. LoRA ≠ RLCD replica.
hf:emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark.
hf:ctaxnagomi/DGUI_HYPERMEM-JEV densify sha ab3d3529.
hf:hugging-apps/open-jev-deberta-v3-large-demo encoder class member not Jev replica.
serving substrate ≠ calibrated replica. catalog ≠ endorsement.
Archer still promised_not_landed. Hub archerhume/4rcherhume HTTP 401.
Do not copy keys. Fresh PR off `6672fbf` (merged #49).
Do not reopen or amend PR #23–#49. Does not bump 0.5.0. Skip Archer.
`invented_signal: false`.

## Hourly 1542 HIGH (`notes.md` §126)

TypeLLM/TypeLLM densify HEAD 6a48f9f1e623 README SHA dbdc1f193537.
README densify 3k→12k B. thinking=True/False per-field budget.
type safety does not guarantee factual accuracy.
Batch 5.8x *theirs*. Constrained AR ≠ calibrated Noul.
Qwen/Qwen3.8-27B ≠ Archer.
jaredpalmer/kev densify HEAD b339f446a0ef README SHA 86b0a19909f3.
Kev-0.6B 4B 8B family. 4B new-source 0.790/0.806 *theirs*.
8B new-source 0.796/0.780 *theirs*. Jev hosted 0.857 *theirs*.
Questions share the input text but cannot read each other.
No Jev outputs were used for training.
8.2% ≥0.9 on wrong *theirs*. option order can change an answer.
Qwen3 ≠ Archer.
TheoOliveira/pi-jev 21★ fail-closed routing.
JEV_THRESHOLD 0.65 still soft. routing ≠ permission.
harshwasan/jev-sentinel fail closed never auto-allows.
harshwasan/jev-sentinel ≠ leepokai/jev-guard.
jackbarunz/jev-tool-router ≠ esinocchi/jev-tool-router.
threshold 0.90 still soft.
76/81 vs 77/81 *theirs*. 0.419s vs 2.459s *theirs*.
$0.00486 vs $0.03673 *theirs*.
does not execute. not a security boundary.
baronunread/leanest fail-open uncertainty means RUN.
classifier.dev default Jev/Laya pluggable.
openlayer-ai/jevals ≠ dayhaysoos/jevals.
estimates not Harbor. classifier ≠ authorizer.
MrJev/awesome-jev 118 entries catalog ≠ endorsement.
MrJev/awesome-jev ≠ yibie/awesome-jev.
Koushik890/jev-firewall fail closed ask_below 0.7 still soft.
CompleteTech-LLC-AI-Research/jev-codex-approval experimental native not compiled.
confidence is not a measured probability. rh-guard owns primary gates.
hf:rAVEUK/open-jev-deberta-v3-large encoder class member not Jev replica.
hf:p-yan/laya-quanto serving substrate ≠ calibrated replica.
hf:Gtrkrsk/laya serving substrate ≠ calibrated replica.
wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement.
Archer still promised_not_landed. Hub archerhume/4rcherhume HTTP 401.
Do not copy keys. Fresh PR off `f40139c` (merged #48).
Do not reopen or amend PR #23–#48. Does not bump 0.5.0. Skip Archer.
`invented_signal: false`.


## Hourly 1441 HIGH (`notes.md` §125)

vLLM NVIDIA + MLX Apple Silicon. Codiv hosted free endpoint.
dual /v1/systemone + /v1/chat/completions. chat 501 on MLX.
dual serving is not generate. Hosted Codiv ≠ TypeSafe.
STE README rewrite. serving-port densify.
hr98w/jev-visual 167★ Apple Silicon visual candidate scoring.
37.30s → 2.40s at 64 decisions *theirs*.
Breakout 9 bricks 6 returns 2 lives *theirs*.
candidate probabilities are relative not correctness.
jkudish/jev-mcp 156★ ten MCP tools.
recommendation is advisory. the server never blocks on its own.
TypeSafe CLERC 5% to 18% *theirs*.
jkudish/jev-mcp ≠ burnigtm/jev-mcp.
zhengxuyu/litjev off-the-shelf Qwen decision layer.
Probabilities are not calibrated by default. Qwen/Qwen3.8-27B ≠ Archer.
zhengxuyu/litjev ≠ alexwestco/llm-to-jev.
Zefan-Cai/Open-Jev LoRA + scalar head.
2B 94.71% 9B 97.54% hard test *theirs*.
2B OOD 86.02% 9B OOD 91.97% *theirs*.
80,816 training rows. 27B still in progress. LoRA ≠ RLCD replica.
Zefan-Cai/Open-Jev ≠ TheoLeeCJ/openjev ≠ razorback16/openjev.
cristianoliveira/jeq intelligence you can pipe.
pass-min 0.8 still soft. JEQ does not own actions.
AndyInQtr/laya-coreai CoreML serving substrate ≠ calibrated replica.
AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml.
wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement.
Error contract is not a Noul. Archer still promised_not_landed.
Hub archerhume/4rcherhume HTTP 401.
Do not copy keys. Fresh PR off `fea7c0b` (merged #47).
Do not reopen or amend PR #23–#47. Does not bump 0.5.0. Skip Archer.
`invented_signal: false`.

## Open-Jev densify (`notes.md` §125)

DENSIFY the original 1441 card. Do not mint a sibling first sighting.
HEAD 4933ee84951f README SHA ce1a587219e4. pushed 2026-09-21T01:34Z.
Astra TREC commit 1dd56990be7e. live 3★ (star-noise is not the fold).
LoRA adapters plus a trained scalar decision head and calibration
temperature. not merged base models. Independent of TypeSafe.
no RLCD/parity claims. LoRA ≠ RLCD replica.
customer-service P50 local HTTP 85.03 ms vs Jev HTTPS 295.26 ms *theirs*.
1024 tokens/32 candidates Open-Jev slower 1015.90 vs 301.37 *theirs*.
prefix caching experimental/off by default.
systems latency ≠ semantic equivalence.
GPT Luna P50 918.13 ms Astra 1938.39 ms *theirs*.
TREC-DL Jev/Luna/Astra completed. Open-Jev TREC pending.
80,816 training rows. 2B 94.71% / OOD 86.02%. 9B 97.54% / 91.97% *theirs* not Harbor.
hard acc ≠ calibrated Noul. type-valid ≠ exact.
Qwen/Qwen3.8-27B ≠ Archer.
website https://zefan-cai.github.io/open-jev/.
SHA move is not a replica. Do not copy train flags.
Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer.
`invented_signal: false`.


**Hourly 1441 HIGH (`notes.md` §125).** vLLM NVIDIA + MLX Apple Silicon. Codiv hosted free endpoint. dual /v1/systemone + /v1/chat/completions. chat 501 on MLX. dual serving is not generate. Hosted Codiv ≠ TypeSafe. candidate probabilities are relative not correctness. recommendation is advisory. the server never blocks on its own. LoRA ≠ RLCD replica. pass-min 0.8 still soft. 37.30s → 2.40s at 64 decisions *theirs*. 2B 94.71% 9B 97.54% hard test *theirs*. wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#47. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1441 uniqueness lock: vLLM NVIDIA + MLX Apple Silicon; Codiv hosted free endpoint; dual /v1/systemone + /v1/chat/completions; razorback16/openjev densify HEAD cddbd962c88a README SHA a5943415cb92; STE README rewrite; serving-port densify; chat 501 on MLX; dual serving is not generate; Hosted Codiv ≠ TypeSafe; wire-compat ≠ logit-equiv; SHA move is not a replica; Error contract is not a Noul; hr98w/jev-visual 167★ Apple Silicon visual candidate scoring; 37.30s → 2.40s at 64 decisions *theirs*; Breakout 9 bricks 6 returns 2 lives *theirs*; candidate probabilities are relative not correctness; jkudish/jev-mcp 156★ ten MCP tools; recommendation is advisory; the server never blocks on its own; TypeSafe CLERC 5% to 18% *theirs*; jkudish/jev-mcp ≠ burnigtm/jev-mcp; zhengxuyu/litjev off-the-shelf Qwen decision layer; Probabilities are not calibrated by default; Qwen/Qwen3.8-27B ≠ Archer; zhengxuyu/litjev ≠ alexwestco/llm-to-jev; Zefan-Cai/Open-Jev LoRA + scalar head; 2B 94.71% 9B 97.54% hard test *theirs*; 2B OOD 86.02% 9B OOD 91.97% *theirs*; 80,816 training rows; 27B still in progress; LoRA ≠ RLCD replica; Zefan-Cai/Open-Jev ≠ TheoLeeCJ/openjev ≠ razorback16/openjev; cristianoliveira/jeq intelligence you can pipe; pass-min 0.8 still soft; JEQ does not own actions; AndyInQtr/laya-coreai CoreML serving substrate ≠ calibrated replica; AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47; notes.md §125


**Hourly 1542 HIGH (`notes.md` §126).** TypeLLM README densify 3k→12k B. Batch 5.8x *theirs*. Constrained AR ≠ calibrated Noul. kev family densify. 4B new-source 0.790/0.806 *theirs*. 8.2% ≥0.9 on wrong *theirs*. option order can change an answer. fail-closed routing vs fail-open test selection. classifier ≠ authorizer. estimates not Harbor. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#48. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1542 uniqueness lock: TypeLLM/TypeLLM densify HEAD 6a48f9f1e623 README SHA dbdc1f193537; README densify 3k→12k B; thinking=True/False per-field budget; type safety does not guarantee factual accuracy; Batch 5.8x *theirs*; Constrained AR ≠ calibrated Noul; Qwen/Qwen3.8-27B ≠ Archer; jaredpalmer/kev densify HEAD b339f446a0ef README SHA 86b0a19909f3; Kev-0.6B 4B 8B family; 4B new-source 0.790/0.806 *theirs*; 8B new-source 0.796/0.780 *theirs*; Jev hosted 0.857 *theirs*; Questions share the input text but cannot read each other; No Jev outputs were used for training; 8.2% ≥0.9 on wrong *theirs*; option order can change an answer; Qwen3 ≠ Archer; wire-compat ≠ logit-equiv; SHA move is not a replica; TheoOliveira/pi-jev 21★ fail-closed routing; JEV_THRESHOLD 0.65 still soft; routing ≠ permission; harshwasan/jev-sentinel fail closed never auto-allows; harshwasan/jev-sentinel ≠ leepokai/jev-guard; jackbarunz/jev-tool-router ≠ esinocchi/jev-tool-router; threshold 0.90 still soft; 76/81 vs 77/81 *theirs*; 0.419s vs 2.459s *theirs*; $0.00486 vs $0.03673 *theirs*; does not execute; not a security boundary; baronunread/leanest fail-open uncertainty means RUN; classifier.dev default Jev/Laya pluggable; openlayer-ai/jevals ≠ dayhaysoos/jevals; estimates not Harbor; classifier ≠ authorizer; MrJev/awesome-jev 118 entries catalog ≠ endorsement; MrJev/awesome-jev ≠ yibie/awesome-jev; Koushik890/jev-firewall fail closed ask_below 0.7 still soft; CompleteTech-LLC-AI-Research/jev-codex-approval experimental native not compiled; confidence is not a measured probability; rh-guard owns primary gates; hf:rAVEUK/open-jev-deberta-v3-large encoder class member not Jev replica; hf:p-yan/laya-quanto serving substrate ≠ calibrated replica; hf:Gtrkrsk/laya serving substrate ≠ calibrated replica; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48; notes.md §126
**Hourly 1643 HIGH (`notes.md` §127).** openjev release 0.3.0 densify. re-pin vLLM PR #57250 restructured head. restructured vLLM head ≠ logit-equiv. MODEL_VERSION stays openjev-0.1. dual serving is not generate. Hosted Codiv ≠ TypeSafe. typed judgments not opinions. Thresholds are policy not model. Jev never generates prose JSX or code. game success ≠ calibrated Noul. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#49. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1643 uniqueness lock: razorback16/openjev densify HEAD febf02e88989 README SHA 242a737dba01; release 0.3.0; re-pin vLLM PR #57250 restructured head; VLLM_COMMIT baa8338; pyproject and __init__ agree 0.3.0; MODEL_VERSION stays openjev-0.1; uv.lock hygiene; dual serving is not generate; Hosted Codiv ≠ TypeSafe; restructured vLLM head ≠ logit-equiv; wire-compat ≠ logit-equiv; SHA move is not a replica; Error contract is not a Noul; frostney/clean-code-review 7★ typed judgments not opinions; documentation is read not judged; Luna writes from Jev findings; morcoan/JMP Joint Model Participation; Models participate. Real tools execute.; Jev routes actions generators supply arguments; not a swarm; zkjoie/jevbus Thresholds are policy not model; Drop < Review < Deliver; FanOut or Exclusive; Kelbie/hunch ≠ carldaws/hunch ≠ tpellet/hunch ≠ huncho; Agent Skills semantic review; SupratikB23/JevCanvas Jev never generates prose JSX or code; Diffusion never decides structure; json-render is the only renderer; skcache/jevtrafficsim Fixed Adaptive Jev; game success ≠ calibrated Noul; Shalimov04/open-jev ≠ razorback16/openjev ≠ TheoLeeCJ/openjev ≠ Zefan-Cai/Open-Jev; MstyAI/laya-onnx empty repo ≠ tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; SherifAshraf2003/jev-use ≠ shitianfang/jev-use; aniruddh-krovvidi/switchboard ≠ cannacre8ive/switchboard-ai; Visorian/TidyUp ≠ abhibansal60/tidy; isiomaC/jevkit ≠ WaynezProg/jev-kit; lee-lou2/jev-tree ≠ reachjalil/jev-tree; Royhu1/jev-poker-trainer empty repo; JoacoMarc/jev-harness-router ≠ jackbarunz/jev-tool-router; rh-guard owns primary gates; hf:Praveenrajus/jev-bench HTTP 200 was 401; hf:ZefanCai/Open-Jev densify dataset; LoRA ≠ RLCD replica; hf:emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; hf:ctaxnagomi/DGUI_HYPERMEM-JEV densify sha ab3d3529; hf:hugging-apps/open-jev-deberta-v3-large-demo encoder class member not Jev replica; serving substrate ≠ calibrated replica; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49; notes.md §127

**Hourly 1746 HIGH (`notes.md` §128).** TypeLLM truncated thinking densify. 0.8B thinking On 0/18 *theirs*. forced closure 20/20 type-valid *theirs*. Constrained AR ≠ calibrated Noul. Kev-0.8B completes family. 4B new-source 0.794/0.832 *theirs*. 9B new-source 0.812/0.837 *theirs*. transfer-v9 5%/9%/26% *theirs*. Facts go to code. Judgments go to Jev. Only facts can block. Jev never blocks. five-lines threshold 0.80 still soft. 155/155 argmax *theirs*. Qwen3.5 ≠ Archer. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#50. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1746 uniqueness lock: TypeLLM/TypeLLM densify HEAD 702e6a287f3c README SHA 08180db0450b; truncated thinking then constrained decode; typellm_runtime.py typellm_sglang.py; evals/qwen35_small; 0.8B thinking On 0/18 *theirs*; forced closure 20/20 type-valid *theirs*; Constrained AR ≠ calibrated Noul; type safety does not guarantee factual accuracy; Qwen/Qwen3.8-27B ≠ Archer; jaredpalmer/kev densify live HEAD 8465c4c4c294 watch 38087aa0301d README SHA 19664b9ae546; Kev-0.8B completes family; Kev-0.8B 4B 9B Qwen3.5; 4B new-source 0.794/0.832 *theirs*; 9B new-source 0.812/0.837 *theirs*; transfer-v9 Kev-9B 5% Jev 9% Kev-8B 26% *theirs*; SemIf Kev-9B 0.917 Jev 0.965 *theirs*; scienthoon 0.952/0.911 vs 0.897/0.914 *theirs*; transformers >= 5.17; Qwen3.5 ≠ Archer; wire-compat ≠ logit-equiv; SHA move is not a replica; notque/vexjoy-agent 421★ /d routes /do fallback; tamaratran/jev-pruner densify HEAD 47d017c34eab; qkal/Canny Facts go to code. Judgments go to Jev. Only facts can block.; Jev never blocks; jqueryscript/awesome-jev 231 entries catalog ≠ endorsement; jqueryscript/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev; jamescazzetta/five-lines threshold 0.80 still soft; eugeniughelbur/jev-engineering 371ms $0.0000189 300-call *theirs*; tpellet/jevify ≠ altryne/jevify; seb4ez/jevguard-mcp ≠ seb4ez/jevguard; resumocast/jev-mcp ≠ jkudish/jev-mcp; dtduc-git/jev-table first sighting; Adrian-Ernesto/jevsort ≠ zzzzzec/jevsort; MidasMulli/kev-ane 155/155 argmax *theirs*; MidasMulli/kev-ane ≠ jaredpalmer/kev; serving substrate ≠ calibrated replica; empty repo skip-thin; loktar00/llm-lan-party empty repo; rh-guard owns primary gates; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50; notes.md §128

**Hourly 1843 HIGH (`notes.md` §129).** kev own-data JSONL densify. --init_from warm-start LoRA/head PR #9. from-scratch ≠ warm-start. JSONL labels ≠ Harbor. 4B new-source 0.794/0.832 *theirs*. 9B new-source 0.812/0.837 *theirs*. 0.33 vs 0.84 vs 0.83/0.88 *theirs*. reconstruction ≠ replica. assay-001 split verdict. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#51. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1843 uniqueness lock: jaredpalmer/kev densify HEAD bd058057ad0a README SHA 84b872488915; Fine-tuning on your own data; --data JSONL; --init_from warm-start LoRA/head PR #9; Kev-0.8B 4B 9B Qwen3.5 family; 4B new-source 0.794/0.832 *theirs*; 9B new-source 0.812/0.837 *theirs*; 0.33 vs 0.84 vs 0.83/0.88 *theirs*; from-scratch ≠ warm-start; JSONL labels ≠ Harbor; Kev-0.5B card Qwen3.5 family pointer; No Jev outputs were used for training; option order can change an answer; 8.2% ≥0.9 on wrong *theirs*; Kev-9B 7.5% ≥0.9 on wrong *theirs*; dabit3/jev-experiments densify 340★; simota/tenbin densify neighbor skill; Promethe-us/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev; kyegomez/open-jev reconstruction ≠ replica; unofficial research implementation with random weights; kyegomez/open-jev ≠ razorback16/openjev ≠ TheoLeeCJ/openjev ≠ Zefan-Cai/Open-Jev ≠ Shalimov04/open-jev; jourdanlabs/assay-001 split verdict; CLINC150 ECE 0.0204 *theirs*; Banking77 ECE 0.0936 *theirs*; 8,576 responses zero type errors *theirs*; brnyxx/jev-ra 3-5x / ~300 ms *theirs*; 8.50× Wikipedia *theirs*; ThePFMind/jev-mcp ≠ jkudish/jev-mcp ≠ burnigtm/jev-mcp; namenu/pi-jev-effort ≠ TheoOliveira/pi-jev; samatv256/mini-Jev ≠ r-ms/mini-jev; comoc/jev-minesweeper ≠ EnesYilmazcode/JevMinesweeper; game success ≠ calibrated Noul; Nutlope/jev-fraud Kimi K3; jeffloo886/jev-notion; hf:akhilaaa3/openjev-v1-allmix-r512-merged ≠ hf:akhilaaa3/openjev-r512-handoff-demo; serving substrate ≠ calibrated replica; catalog ≠ endorsement; SHA move is not a replica; wire-compat ≠ logit-equiv; Qwen3.5 ≠ Archer; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51; notes.md §129


## User-provided 1936 (`notes.md` §130)

sgoedecke/system-one 20★ HEAD ebde2a2db706. SystemOne.from_pretrained.
TypeSafe-compatible ≠ TypeSafe replica. Batched single-token choice inference.
mithalouni/system-one-open 18★ MIT HEAD 77f1f7cccf8a.
76.7% vs Jev 86.9% strict common subset *theirs*. 97 ms H100 *theirs*.
74.8% held-out *theirs*. replica ≠ TypeSafe.
kotoba-lang/typed-decisions 1★ Apache-2.0 HEAD 10d7834d3b99.
DeBERTa-v3-large 0.855 / 42 ms *theirs*. ModernBERT-base 0.717 / 68 ms *theirs*.
LLaDA-MoE 0.835 / 676 ms *theirs*.
kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions.
encoder class member not Jev replica.
aisearchio 15-link census catalog ≠ endorsement.
12 already carded 3 gaps this fold. soft scores ≠ hard gates.
user-provided 1936 / notes.md §130.
Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer.
`invented_signal: false`.

**User-provided 1936 HIGH (`notes.md` §130).** sgoedecke/system-one first-sighting. SystemOne.from_pretrained. TypeSafe-compatible ≠ TypeSafe replica. mithalouni/system-one-open first-sighting. 76.7% vs Jev 86.9% *theirs*. replica ≠ TypeSafe. kotoba-lang/typed-decisions first-sighting. DeBERTa-v3-large 0.855 / 42 ms *theirs*. kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions. aisearchio 15-link census catalog ≠ endorsement. soft scores ≠ hard gates. SHA move is not a replica. Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
User-provided 1936 uniqueness lock: sgoedecke/system-one 20★ HEAD ebde2a2db706 README SHA d331b567e2c3; SystemOne.from_pretrained; Batched single-token choice inference; TypeSafe-compatible; cache_prefix=True; LICENSE absent; sgoedecke/system-one ≠ mithalouni/system-one-open ≠ KathanModh259/system-one ≠ babybear-labs/system-one; TypeSafe-compatible ≠ TypeSafe replica; mithalouni/system-one-open 18★ MIT HEAD 77f1f7cccf8a README SHA 535f33028a68 LICENSE SHA 2f6f2cf1064e; Gemma 4 E2B / Gemma 3 270M Modal; 76.7% vs Jev 86.9% strict common subset *theirs*; 97 ms H100 *theirs*; 74.8% held-out *theirs*; replica ≠ TypeSafe; HF upload pending; kotoba-lang/typed-decisions 1★ Apache-2.0 HEAD 10d7834d3b99 README SHA 4d6bbf4c4e44 LICENSE SHA 513bb5e3cb4c; ModernBERT / DeBERTa / LLaDA-MoE; DeBERTa-v3-large 0.855 / 42 ms *theirs*; ModernBERT-base 0.717 / 68 ms *theirs*; LLaDA-MoE 0.835 / 676 ms *theirs*; kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions; encoder class member not Jev replica; aisearchio 15-link census catalog ≠ endorsement; 12 already carded 3 gaps this fold; soft scores ≠ hard gates; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §130
**Open-Jev densify (`notes.md` §125).** DENSIFY the original 1441 card, not a sibling first sighting. HEAD 4933ee84951f README SHA ce1a587219e4. LoRA + scalar head + calibration temperature. not merged base models. customer-service P50 85.03 vs Jev 295.26 *theirs*. 1024/32 slower 1015.90 vs 301.37 *theirs*. systems latency ≠ semantic equivalence. Open-Jev TREC pending. hard acc ≠ calibrated Noul. type-valid ≠ exact. LoRA ≠ RLCD replica. Qwen/Qwen3.8-27B ≠ Archer. SHA move is not a replica. Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
User-provided Open-Jev densify uniqueness lock: Zefan-Cai/Open-Jev densify HEAD 4933ee84951f README SHA ce1a587219e4; pushed 2026-09-21T01:34Z; Astra TREC commit 1dd56990be7e pushed 2026-09-21T01:17Z; live 3★ (was 0★; star-noise is not the fold); LoRA adapters plus trained scalar decision head and calibration temperature; not merged base models; dataset ZefanCai/Open-Jev rev c67699e13d0a; Open-Jev-2B rev 0c7aa498b162; Open-Jev-9B rev 47e966881e48; 27B still in progress; Independent of TypeSafe; no RLCD/parity claims; LoRA ≠ RLCD replica; customer-service P50 local HTTP 85.03 ms vs Jev HTTPS 295.26 ms *theirs*; 1024 tokens/32 candidates Open-Jev slower 1015.90 vs 301.37 *theirs*; prefix caching experimental/off by default; CUDA prefix caching exceeded tolerance on 9/11 workloads; systems latency ≠ semantic equivalence; GPT Luna P50 918.13 ms Astra 1938.39 ms *theirs*; TREC-DL Jev/Luna/Astra completed; Open-Jev TREC pending; 80,816 training rows; 2B 94.71% / OOD 86.02%; 9B 97.54% / 91.97% *theirs* not Harbor; hard acc ≠ calibrated Noul; type-valid ≠ exact; Qwen/Qwen3.8-27B ≠ Archer; website https://zefan-cai.github.io/open-jev/; launch X thread https://x.com/Zefan_Cai/status/2101782158658695388 https://x.com/Zefan_Cai/status/2101786019607740436 https://x.com/Zefan_Cai/status/2101789698947793231; densify §125 not a sibling first sighting; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §125

**Hourly 1946 HIGH (`notes.md` §131).** X-sentiment does not execute trades. heyjunpenn/awesome-jev 485 catalog ≠ endorsement. jev-arena 62.69% vs 67.26% *theirs* not gold. 203.2s $0.84 vs 823.5s $1.50 *theirs*. one seed-0 trial *theirs*. Jev $0.018825 vs Astra $5.93 *theirs*. 10.59× *theirs*. 6 class flips. agreement ≠ accuracy. probabilities uncalibrated. Qwen3.8 ≠ Archer. Spanish −6.4 pp XNLI *theirs*. ECE 0.057→0.101 *theirs*. 72.2% vs 63.4% p_max≥0.9 coverage *theirs*. llm-to-jev description rewrite Convert LLM prompts to Jev prompts. SHA unchanged 234058ab372d. 3★. heuristic conversion ≠ calibrated Noul. skip Zefan-Cai/Open-Jev densify open #53. skip #54 three. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1946 uniqueness lock: brainstormity/Jev-X-Sentiment-Analysis 136★ HEAD 5c932f941a92 README SHA bf4134b44cda; platform does not execute trades; heyjunpenn/awesome-jev 485 catalog ≠ endorsement; heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ MrJev/awesome-jev ≠ Promethe-us/awesome-jev ≠ ckaraca/awesome-jev ≠ yzfly/awesome-jev-zh ≠ shirenchuang/awsomejev ≠ andyrewlee/awesome-system-one; NanmiCoder/jev-arena 10k comments 62.69% vs 67.26% *theirs* not gold; 203.2s $0.84 vs 823.5s $1.50 *theirs*; AI-reviewed labels ≠ gold; openroboto-ai/jev-robot-control one seed-0 trial *theirs*; Jev $0.018825 vs Astra $5.93 *theirs*; one-trial robot ≠ Harbor; endman100/research-Qwen3.8-JevLike 10.59× *theirs*; 6 class flips; agreement ≠ accuracy; probabilities uncalibrated; Qwen3.8 ≠ Archer; 10.59× systems ≠ ECE; marcosmartinez/jev-acento Spanish −6.4 pp XNLI *theirs*; ECE 0.057→0.101 *theirs*; 72.2% vs 63.4% p_max≥0.9 coverage *theirs*; alexwestco/llm-to-jev description rewrite Convert LLM prompts to Jev prompts; SHA unchanged 234058ab372d; 3★; heuristic conversion ≠ calibrated Noul; desc rewrite ≠ SHA/behavior change; skip Zefan-Cai/Open-Jev densify open #53; skip sgoedecke/system-one mithalouni/system-one-open kotoba-lang/typed-decisions open #54; ikermoel/open-alternative-jev already §49; nrdz-labs/fast-jev-opencode already §62; mallahyari/system-one-benchmark already §61; does not execute; catalog ≠ endorsement; *theirs* not Harbor; SHA move is not a replica; local_only ≠ Jev; rule-table ≠ model; replica ≠ TypeSafe; arunav25/jev-mcp ≠ jkudish/jev-mcp ≠ ThePFMind/jev-mcp ≠ burnigtm/jev-mcp; luckberonne/mini-jev ≠ r-ms/mini-jev ≠ samatv256/mini-Jev; Kwwwww74/OpenJev ≠ razorback16/openjev ≠ kyegomez/open-jev ≠ Zefan-Cai/Open-Jev; peach-zhang/typesafe-go ≠ kisshan13/typesafe-ai-go ≠ Nibir1/typesafe-go; laidick/system-one-benchmark ≠ mallahyari/system-one-benchmark; sahasrarjn/system-one ≠ sgoedecke/system-one; aboisvert/jevvy ≠ PanAchy/jevvy; andrest04/jev-lab ≠ javsanesq/jevlab; twilwa/pi-typesafe ≠ TheoOliveira/pi-jev; RuipuCui/jev-harness ≠ ismaelsoilet/jev-harness ≠ AntonioCoppe/jev-harness; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §131

**Hourly 2049 HIGH (`notes.md` §132).** kev night-2 densify HEAD c096660c8da2. PLAN SHA 8d77dd271c66. README SHA unchanged 84b872488915. KEV_TEMPERATURE T≈2.0. Brier 0.291→0.267 ECE 0.105→0.039 *theirs*. 7.5%→3.2% *theirs*. grouped T rejected. Qwen3.6-35B-A3B smoke 0.812 *theirs*. Hub --revision night2-du. MMLU-Pro 1000 Kev-9B 0.511 Jev 0.829 *theirs*. Qwen3.6 ≠ Archer. temperature scaling ≠ ECE unless measured. Hub --revision is a pin not a replica. kotoba OpenJev runtime densify HEAD ff7f84e74d04. generated_text: False. trained runtime ≠ TypeSafe. OpenJev.from_pretrained. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#55. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 2049 uniqueness lock: jaredpalmer/kev densify HEAD c096660c8da2 PLAN SHA 8d77dd271c66 README SHA unchanged 84b872488915; night-2 dates/unknowable/assertion; KEV_TEMPERATURE T≈2.0; Brier 0.291→0.267 ECE 0.105→0.039 *theirs*; 7.5%→3.2% *theirs*; grouped T rejected; Qwen3.6-35B-A3B smoke 0.812 *theirs*; 21M LoRA experts frozen; Hub --revision night2-du; MMLU-Pro 1000 Kev-9B 0.511 Jev 0.829 *theirs*; Qwen3.6 ≠ Archer; temperature scaling ≠ ECE unless measured; kotoba-lang/typed-decisions densify HEAD ff7f84e74d04 README SHA unchanged 4d6bbf4c4e44; feat expose trained OpenJev decision runtime; open_jev.py; tests/test_open_jev.py; generated_text: False; trained runtime ≠ TypeSafe; OpenJev.from_pretrained; decide_request kind typed-decisions/open-jev-v1; daftAI2026/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ MrJev/awesome-jev ≠ Promethe-us/awesome-jev; danielamitay/swev CoreML; serving substrate ≠ calibrated replica; smlayero/jev-debtgate CI gate cutoff still soft; Octalab-Inc/jqv stock Qwen3 decision API; franckverrot/lev ≠ jaredpalmer/kev; neko233-com/laya-go ≠ convaiinnovations/laya; tryAGI/TypeSafeAI ≠ official; abgregs/jev-experiments ≠ nak1b/jev-experiments ≠ dabit3/jev-experiments; jaanavit/gliner2-skill Locate ≠ decide; prasanthj/duckdb-jev SQL predicates; hf:Nebulaw1 legal LoRA ≠ RLCD replica; Qwen3.5 ≠ Archer; catalog ≠ endorsement; *theirs* not Harbor; SHA move is not a replica; skip-thin KadePrice123/jev-state-tracking hideri777/jev-application-sample; Hub --revision is a pin not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55; notes.md §132

**Hourly 2146 HIGH (`notes.md` §133).** Open-Jev provider quality densify HEAD a00559ea0ab2. README SHA unchanged ce1a587219e4. provider pipeline ≠ completed Open-Jev quality. CPU tests ≠ GPU scores. 65/76 72/76 66/76 60/76 71/76 *theirs*. Open-Jev TREC pending. cartpole Kev flip HEAD 922cc61490a0. fine-tuned Kev ≠ TypeSafe Jev. one record of 64. 81.25% 52/64 *theirs*. softmax ≠ calibrated Noul. ashare rewrite HEAD 26c7e95e6828. QMT mock/dry default no orders. AUC 0.532 *theirs*. does not execute. kevin Playwright + Onyx first card. 3.69ms *theirs* not Harbor. metask-jev-4b 79.6% / 80.1% *theirs*. cutoff 95% still soft. option order can change an answer. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#56. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 2146 uniqueness lock: Zefan-Cai/Open-Jev densify HEAD a00559ea0ab2 README SHA unchanged ce1a587219e4; Publish prepared Open-Jev provider quality evaluation pipeline; 808 requests 1841 labelled decisions per model; Open-Jev GPU inference has not started; 48 CPU tests pass; Open-Jev TREC pending; 65/76 72/76 66/76 60/76 71/76 *theirs*; 117/140 109/140 135/140 *theirs*; JF100 232/300 227/300 300/300 *theirs*; FizzBuzz 299/300 300/300 300/300 *theirs*; mailroom 908/921 900/921 913/921 *theirs*; Jev TREC DL19/DL20 nDCG@10 0.275836/0.190667 strict *theirs*; Luna 0.729911/0.702082 *theirs*; Astra 0.736610/0.714484 *theirs*; provider pipeline ≠ completed Open-Jev quality; CPU tests ≠ GPU scores; tinmanlab/cartpole-jev densify HEAD 922cc61490a0 README SHA 0860958714f3; Active model Kev Not TypeSafe Jev; 81.25% 52/64 *theirs*; one record of 64; fine-tuned Kev ≠ TypeSafe Jev; softmax ≠ calibrated Noul; xuboboo/ashare-trader densify HEAD 26c7e95e6828 README SHA 7a860bdfa97b; premarket + intradaily; local probability model; QMT sidecar mock/dry default no orders; AUC 0.532 *theirs*; 36 组参数全部净期望为负; does not execute; gauravsaini/kevin first card Playwright + Onyx; Laya/Kev friends *theirs*; 3.69ms *theirs* not Harbor; metask-jev-4b 79.6% / 80.1% *theirs*; Bespoke Nimble-9B 74.8% / 63.5; Jev 76.0% / 75.3; lumen mixture-of-LoRA conformal; ardada2468/typedecide ≠ shkumbinhasani/typedecide; 87 of 144 order-unstable *theirs*; bonsai 192/231 ECE 0.037 *theirs*; 8GB; vercel-labs 95% Luna fallback; cutoff 95% still soft; tinmanlab/jev-qwen3.8-27b Qwen3.8 ≠ Archer; train-your-first-jev Qwen2.5-0.5B LoRA; sankaku-tech/jev-kit ≠ WaynezProg/jev-kit ≠ isiomaC/jevkit; jevfish DecisionScore 78.24 *theirs*; Typed Decision Bench 5387; reflex-gate CoT GBNF ≠ Noul; skip-thin IOCArena laya-mirror empty SHA; snsk JP 97.6 vs 36.9 *theirs*; yunhe-dev/awesomejev catalog ≠ endorsement; yunhe-dev/awesomejev ≠ heyjunpenn/awesome-jev ≠ daftAI2026/awesome-jev; wayfind/metask-jev ≠ metask-ai/metask-jev; mjyoke1111/jev-lab already §106; mizchi/jev-playground 19★; KaLM-Jev reranker ≠ Jev replica; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56; notes.md §133
**Hourly 2246 HIGH (`notes.md` §134).** Open-Jev TREC densify HEAD 48346d0630f1. README SHA unchanged ce1a587219e4. TREC prep ≠ completed Open-Jev TREC. context proof ≠ nDCG. CPU tests ≠ GPU scores. 79 CPU tests *theirs*. Open-Jev TREC pending. TypeLLM PyPI densify HEAD 8a8b4aefd443. typellm 0.1.1. PyPI packaging ≠ calibrated Noul. Constrained AR ≠ calibrated Noul. simple-jev 408★ first card. logits are not calibrated probabilities of correctness. wire-compat ≠ logit-equiv. jev-directory catalog ≠ endorsement. Jev-Mem 11.0% 6.6× 36.7% *theirs* not Harbor. FogMoe/necro abandoned LoRA retrospective. serving substrate ≠ calibrated replica. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#57. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 2246 uniqueness lock: Zefan-Cai/Open-Jev densify HEAD 48346d0630f1 README SHA unchanged ce1a587219e4; Publish strict Open-Jev TREC evaluation preparation and context proof; Actual Open-Jev TREC model inference is pending; All 79 combined CPU tests pass; 97 queries 43 DL19 54 DL20; at most 873 requests per model; No GPU or model inference was used; TREC prep ≠ completed Open-Jev TREC; context proof ≠ nDCG; CPU tests ≠ GPU scores; Open-Jev TREC pending; TypeLLM/TypeLLM densify HEAD 8a8b4aefd443 README SHA 9f6dea3a4c8c; Add PyPI packaging and publish workflow; typellm 0.1.1; Drop fixed banner height so it scales on PyPI; Constrained AR ≠ calibrated Noul; PyPI packaging ≠ calibrated Noul; type safety does not guarantee factual accuracy; featherless-ai/simple-jev 408★ HEAD b02aa81c915a README SHA 4c5be59e9738; logits are not calibrated probabilities of correctness; does not reproduce TypeSafe; /v1/systemone alias of /v1/classifier; wire-compat ≠ logit-equiv; everyai-com/jev-directory 13★ 50 runnable evals 1300+ builds catalog ≠ endorsement; Jev-Mem 11.0% 6.6× 36.7% *theirs* not Harbor; Nyarlathoteppppp/pi-jev-context ≠ kevinpita/pi-jev-context; FogMoe/necro abandoned LoRA retrospective; LoRA ≠ RLCD replica; Qwen3.5-0.8B ≠ Archer; clarity-judge independent community project; hearim Jev-compatible Go gateway; yijunyu/jev-rs any LLM one prefill; alongL/openJev ≠ Zefan-Cai/Open-Jev; huaizuo2022/jev-ultrafast ≠ browser-use/jev-ultrafast; FluidInference/laya-coreml ≠ AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml; serving substrate ≠ calibrated replica; wayfind/metask-jev-4b-policy-mix ≠ metask-ai/metask-jev; majiayu000/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev; rajasekharponakala/jev-mcp ≠ thedv91/jev-mcp ≠ jkudish/jev-mcp; skip-thin jev-droid 404 mach empty SHA; game success ≠ calibrated Noul; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57; notes.md §134
**Hourly 2347 HIGH (`notes.md` §135).** openjev MLX densify HEAD 2050fdb8280d. README SHA d5322e16e565. MLX backend steps>1/think/text gen + image Qs. dual serving is not generate. Hosted Codiv ≠ TypeSafe. wire-compat ≠ logit-equiv. TypeLLM Release v0.1.1 densify HEAD 8a8b4aefd443. README SHA unchanged 9f6dea3a4c8c. GitHub Release v0.1.1. Constrained AR ≠ calibrated Noul. PyPI packaging ≠ calibrated Noul. JevLoop 6★ independent not affiliated. WANLI-256 74.6% *theirs*. option order 0.188 or 0.542 *theirs*. jevtok 0 mismatches *theirs* not Harbor. ockev 35ms 95.8% TomatoEggBench *theirs* not Harbor. n=8 is not Harbor. serving substrate ≠ calibrated replica. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#58. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 2347 uniqueness lock: razorback16/openjev densify HEAD 2050fdb8280d README SHA d5322e16e565; MLX backend steps>1/think/text gen + image Qs; dual serving is not generate; Hosted Codiv ≠ TypeSafe; wire-compat ≠ logit-equiv; SHA move is not a replica; TypeLLM/TypeLLM densify HEAD 8a8b4aefd443 README SHA unchanged 9f6dea3a4c8c; GitHub Release v0.1.1; Drop fixed banner height so it scales on PyPI; Constrained AR ≠ calibrated Noul; PyPI packaging ≠ calibrated Noul; type safety does not guarantee factual accuracy; zjunlp/JevLoop 6★ independent not affiliated; NicolaiLassen/open-bonsai-jev ≠ NicolaiMTLassen/open-bonzi-jev; WANLI-256 74.6% *theirs*; danielhirt/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ mjyoke1111/jev-lab; option order 0.188 or 0.542 *theirs*; novaleolin/jev-evolve; option order can change an answer; LabGuy94/jevtok 0 mismatches *theirs* not Harbor; ockev 35ms 95.8% TomatoEggBench *theirs* not Harbor; structured-decision-bench n=8 *theirs*; n=8 is not Harbor; Yang-SS-stack/jev-computer-use ≠ Mrchen116/jev-computer-use; amoreX/jevvy ≠ PanAchy/jevvy ≠ aboisvert/jevvy; smile-magic/laya-mlx-ddz ≠ smile-magic/laya-mlx-wzq; sriramkasyap/laya-api wire-compat ≠ logit-equiv; hf:space:Yuki131/KaLM-Jev ≠ KaLM-Embedding/KaLM-Jev; KaLM-Jev reranker ≠ Jev replica; hf:soyelmismo/laya-multilingual-onnx serving substrate ≠ calibrated replica; ranking before lossless condensation; llm-routing-jiv does not execute; jev-page-checker advisory does not block; 1deat0r/Jcua Cua-S1 ≠ TypeSafe; Jev-Register-Tool catalog only; nexibeo/jev-cookbook already carded; leesk212/JEV-CPU already carded; kazuhideoki/jev-search already carded; skip-thin layacm empty SHA; game success ≠ calibrated Noul; does not execute; catalog ≠ endorsement; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58; notes.md §135
**Hourly 0049 HIGH (`notes.md` §136).** Open-Jev JevBench public-subset densify HEAD f46ff604f794. README SHA e32c4bbd519c. public-subset ≠ Harbor. 231 ≠ 534. kev night-2 35B densify HEAD e0bcf50153f1. README SHA unchanged 84b872488915. PLAN correct 35B MMLU-Pro (0.550). evaluate.load honour weights_dtype=bf16. 5-10× *theirs* not Harbor. fail-open routing ≠ permission. ordered routing ≠ end-to-end. softmax next-token ≠ calibrated Noul. potential_match ≠ hiring decision. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#59. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 0049 uniqueness lock: Zefan-Cai/Open-Jev densify HEAD f46ff604f794 via afb5226982c7 README SHA e32c4bbd519c was ce1a587219e4; Publish audited JevBench public-subset baselines; community benchmark plan; diverse hard-data pipeline New model gains have not been measured; 231 public tasks 72 original 48 easy 111 hard; full 534 303 private unavailable; do not report full-534; 2B 150/231 64.94% 9B 179/231 77.49% Jev 200/231 86.58% Luna 206/231 89.18% Astra 231/231 100.00% *theirs*; Brier 0.4751 0.3219 0.1811 0.2074 0.0085 *theirs*; ECE 0.1274 0.0858 0.0318 0.0932 0.0149 *theirs*; P50 138.0 189.2 291.3 953.8 2206.4 ms *theirs*; candidate order 119 of 139 Choice; native vs verbalized; public-subset ≠ Harbor; 231 ≠ 534; Open-Jev TREC pending; 27B training not complete; LoRA ≠ RLCD replica; Qwen3.5-2B ≠ Archer; Qwen3.5-9B ≠ Archer; densify §125 not a sibling first sighting; jaredpalmer/kev densify HEAD e0bcf50153f1 README SHA unchanged 84b872488915; PLAN correct 35B MMLU-Pro (0.550); evaluate.load honour weights_dtype=bf16; Kev Qwen3.6-35B-A3B MMLU-Pro 0.550 Kev-9B 0.545 Jev 0.840 *theirs*; Not shipped; Qwen3.6 ≠ Archer; Hub --revision is a pin not a replica; wy-coliney/jev-browser-use 282★ 5-10× *theirs* not Harbor; Jev clicks Codex thinks and verifies; wy-coliney/jev-browser-use ≠ browser-use/jev-ultrafast ≠ Mrlyk/jev-browser ≠ akras14/jevbro; gargpratyush/jev-router 270★ first card fail-open routing ≠ permission; 33Audits/jev-auto ≠ gargpratyush/jev-router; BillionsBobby/JevRouter 124★ 38% 44% vs 24% *theirs* not Harbor; ordered routing ≠ end-to-end; BillionsBobby/JevRouter ≠ gargpratyush/jev-router; daseinlabs/open-jev 75★ Gemma 3 4B MLX; softmax next-token ≠ calibrated Noul; head 0.970 ECE 0.027 *theirs*; shuffled-context 0.258; daseinlabs/open-jev ≠ Zefan-Cai/Open-Jev ≠ razorback16/openjev ≠ zhlei07/openjev; skeptrunedev/jev-recruiter potential_match ≠ hiring decision; abhixhek/jevcal threshold on held-out; simulator not a Jev bench; fail-closed without fallback; AntonioCoppe/jev-harness already carded; akash-kamat/system-one-gemma 64.4% ECE 0.047 *theirs*; 200x *theirs* not Harbor; Premo-Cloud/typesafe-sdk-java unofficial; AgentBuff/awesome-jev catalog ≠ endorsement; AgentBuff/awesome-jev ≠ yibie/awesome-jev ≠ heyjunpenn/awesome-jev; Alpha-Harper-Franklin/jev-drive ≠ VennIntelligence/jev-drive; skip-thin zhlei07/openjev empty SHA khmuhtadin/n8n-nodes-jev-classification empty SHA; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59; notes.md §136
**Hourly 0151 HIGH (`notes.md` §137).** Open-Jev v3 densify HEAD ed45657bf726. README SHA 12e0f581e15d. v3 data prepared ≠ retrained released models. held-out protocol ≠ Harbor. 1,280-row panel ≠ Harbor. finite training loss ≠ quality improvement. website redesign ≠ calibration. jev-wide naive throws away 83% *theirs*. certo KL 0.008 *theirs*. first-instinct 63.3%→78.1% *theirs* not Harbor. Jev is a gate not a generator. community port ≠ TypeSafe. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#60. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 0151 uniqueness lock: Zefan-Cai/Open-Jev densify HEAD ed45657bf726 via 748ae3024294 README SHA 12e0f581e15d was e32c4bbd519c; Publish audited v3 community data and held-out evaluation protocol; Redesign readable project site and consolidate benchmark results; 129,288 decision rows 74,921 training; frozen mixture 96,849 training; 1,280-row / 840-group comparison panel; v3 data prepared ≠ retrained released models; held-out protocol ≠ Harbor; 1,280-row panel ≠ Harbor; finite training loss ≠ quality improvement; website redesign ≠ calibration; 27B step 616 pending; Open-Jev TREC pending; LoRA ≠ RLCD replica; Qwen3.5-2B ≠ Archer; Qwen3.5-9B ≠ Archer; densify §125 not a sibling first sighting; chy4pro/jev-for-chrome 12★ community port ≠ TypeSafe; chy4pro/jev-for-chrome ≠ browser-use/jev-ultrafast; PsiACE/dohnuts 4★ small multimodal direct decisions; joint RLCD *theirs*; Dohnuts ≠ TypeSafe; catoenm/first-instinct 9B 63.3%→78.1% *theirs* not Harbor; 371,278 prepared ≠ consumed; RL did not reliably improve held-out; independent educational not a recovered Jev recipe; 123Satyajeet123/jev-wide naive throws away 83% *theirs*; 255 documented ~32,768 tokens real; two-decimal 95.8% floored *theirs*; IIA fails +0.31 ... +0.50 *theirs*; AltSlate-Labs/certo KL 0.008 acc 0.844 ECE 0.004 *theirs*; research preview independent not affiliated; endomorphosis/JevOps Jev is a gate not a generator; Lake remains admission; Jev never writes Lean; gbesse/question-forge held-out before winner; demo accuracy is synthetic not a Jev benchmark; flyryan/ai-news-aggregator 26★ does not execute; Akashdb5/jev-router ≠ gargpratyush/jev-router ≠ daviddl9/jev-router; kiuckhuang/laya-jev ≠ KonghaYao/laya-jev; tegersdorfer-collab/jevkit ≠ isiomaC/jevkit ≠ WaynezProg/jev-kit; buluoray/JevOnly already carded; yottayoshida/jev-intent-review already carded; skip-thin Iskandeur/system1-system2 zhlei07/open-system-one Hand-In/openjev-multimodal gwxcsny53/jev-watchtower empty SHA; serving substrate ≠ calibrated replica; game success ≠ calibrated Noul; does not execute; catalog ≠ endorsement; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60; notes.md §137


## User-provided jimothy (`notes.md` §159)

TypeSafe Jev stays the default recommended path.
AndrewPrifer/jimothy is a distill and local-serving path inside the
decision-model class. It is not a replacement for hosted Jev.
A distilled local classifier is not a calibrated replica.
Teacher labeling uses hosted Jev when configured. Training itself is local.
A null threshold means no recommendation. The application applies the cutoff.
MiniLM probabilities can differ across Node, browser, WASM, and WebGPU.
Validate cutoffs in the deployment environment.
BANKING77 and the email table stay *theirs*, not Harbor.
Wire-compat is not logit-equiv. Catalog is not endorsement.
hourly 1851 §158 are on main. This fold is §159 only.
Do not reopen or amend PR #23 through #84. Do not reclaim §147 through §158.
Does not bump 0.5.0 or 0.5.1. Skip Archer.
`invented_signal: false`.
The uniqueness lock lives in `research/notes.md` and the uniqueness gate fixture only.

## Hourly 1851 HIGH (`notes.md` §158)

TypeSafe Jev stays the default recommended path.
An MLX port of von is not the §49 n=78 table.
Logprobs and early exit are not a trained head. 15 to 88 times on
AG News is *theirs*, not Harbor.
One seed is not a species win. About 0.05 across seeds is their noise band.
Port 8000 is wire-compat, not logit-equiv. Qwen3.5 is not Archer.
0.5 is not a decision boundary. A collapsed question does not return
by rebalancing.
A republished Laya card is not a new measurement.
Abstention over a causal LM is not new weights.
Measure on your labels. plumbline is not a leaderboard. Do not import
a winner from a report with no score table.
kev probes moved into `modal_app.py`. A file move is not a new bench.
A description rewrite is not a product. Densify §45, §157, and §150.
Do not mint a sibling first sighting.
hourly 1751 §157 are on main. This fold is §158 only.
Do not reopen or amend PR #23 through #83. Do not reclaim §147 through §157.
Does not bump 0.5.0 or 0.5.1. Skip Archer.
`invented_signal: false`.
The uniqueness lock lives in `research/notes.md` and the uniqueness gate fixture only.

## Hourly 1751 HIGH (`notes.md` §157)

TypeSafe Jev stays the default recommended path.
nokia-applied-research/AnyJev is MorrisZJ/AnyJev, same GitHub id.
Densify §151, not a sibling first sighting. L0 is not calibration.
hunch 153 ms and 24/24 are *theirs*, not Harbor. min-conf 0.75 still soft.
Code verifies the click. Confidence below 0.7 still escalates, and 0.7 stays soft.
Jev answers bounded questions. Jev is not the writer.
Held-out ECE on 2,493 questions is *theirs*. Labels are not human.
Accuracy is not calibration. A temperature republish is not a calibrated replica.
Picks never change the outcome. Tree cuts 0.65 / 0.40 / 0.30 stay soft.
A ranker is not a detector. 101/101 is ceiling-effect evidence.
Shadow discards the answer. The provider call is never skipped.
Game success is not a calibrated Noul. DiffusionGemma is not Archer.
Densify §151, §153, and §127. Do not mint a sibling first sighting.
hourly 1653 §156 are on main. This fold is §157 only.
Do not reopen or amend PR #23 through #82. Do not reclaim §147 through §156.
Does not bump 0.5.0 or 0.5.1. Skip Archer.
`invented_signal: false`.
The uniqueness lock lives in `research/notes.md` and the uniqueness gate fixture only.

## Hourly 1653 HIGH (`notes.md` §156)

TypeSafe Jev stays the default recommended path.
Category and split are judgments. Page bytes stay exact.
docjev 40/40 and 7/8 exact packets are *theirs*, not Harbor.
A local wire is not a replica. Sarashina is not Archer.
A bounded file rank is not calibration. Offline fallback sends nothing.
A merged Gemma 4 head is not Archer. An ONNX export is not a calibrated replica.
About 33 ms on Apple Silicon is *theirs*. 0.80 and 0.5 stay soft.
A controller proposes. The host grants. Game success is not a calibrated Noul.
Densify §94, §143, §148, §153, §154, and the §46 wellposed card.
Do not mint a sibling first sighting.
hourly 1556 §154 and rawwerks/one-system §155 are on main. This fold is §156 only.
Do not reopen or amend PR #23 through #81. Do not reclaim §147 through §155.
Does not bump 0.5.0 or 0.5.1. Skip Archer.
`invented_signal: false`.
The uniqueness lock lives in `research/notes.md` and the uniqueness gate fixture only.

## User-provided rawwerks/one-system (`notes.md` §155)

TypeSafe Jev stays the default recommended path.
rawwerks/one-system is a gateway in front of compatible System One servers.
POST /v1/systemone only. There is no chat-completions endpoint.
Privacy Demo classifies task domain. It is not a privacy filter.
A single eligible backend skips model-based selection, even if hosted.
Threshold 0.5 is a soft example, not a safety envelope.
Declared capabilities fail closed. Questions are not dropped.
Laya is a class peer local option, not equal in adoption.
A gateway is not a calibrated replica. Routing selection is not permission.
Soft judgment never sole veto.
hourly 1556 §154 are on main. This fold is §155 only.
Do not reopen or amend PR #23 through #80. Do not reclaim §147 through §154.
Does not bump 0.5.0 or 0.5.1. Skip Archer.
`invented_signal: false`.
The uniqueness lock lives in `research/notes.md` and the uniqueness gate fixture only.

## Hourly 1556 HIGH (`notes.md` §154)

TypeSafe Jev stays the default path.
Metric value is a judgment. Retention is policy. Annotate preserves metrics.
A 300-item labelled table is *theirs*, not Harbor. open-jev is not TypeSafe.
A router does not place orders. Synthetic-demo profiles are not strategies.
A file review is not a merge gate. 0.60 and 0.75 are still soft.
Fail open is not an interlock. A mock UI is not inference.
A catalog is not endorsement. A serving substrate is not a calibrated replica.
Qwen3-VL-2B is not Archer. Qwen2.5 is not Archer.
Densify §145, §146, §150, and §153. Do not mint a sibling first sighting.
heyaozh/system-one is the rename of heyaozh/jev-rust-crate, same HEAD.
The traffic experiment closed without a demonstrated advantage. That result is *theirs*.
Soft judgment never sole veto.
hourly 1454 §153 are on main. This fold is §154 only.
Do not reopen or amend PR #23 through #79. Do not reclaim §147 through §153.
Does not bump 0.5.1. Skip Archer.
`invented_signal: false`.
The uniqueness lock lives in `research/notes.md` and the uniqueness gate fixture only.

## Hourly 1454 HIGH (`notes.md` §153)

TypeSafe Jev stays the default path.
Jev chooses concrete actions. Code acts. A person reviews the write.
A model score is not a guarantee of success.
0.25 is still a soft keep threshold.
Nothing sends itself. P near 0.5 is NULL.
Same answers is their claim. Export parity is not Harbor.
Codiv OpenJev is not TypeSafe. Ranking is not calibration.
An open recreation is not a calibrated replica. Qwen3-4B is not Archer.
The prior swev card was CoreML. The live port is MLX.
84.0% and 88.58% are *theirs*. One Mind2Web shard. n=40 is not Harbor.
Soft judgment never sole veto.
Densify §132, §145, and §151. Do not mint a sibling first sighting.
ryana/jevify §152 are on main. This fold is §153 only.
Do not reopen or amend PR #23 through #78. Do not reclaim §147 through §152.
Does not bump 0.5.1. Skip Archer.
`invented_signal: false`.
The uniqueness lock lives in `research/notes.md` and the uniqueness gate fixture only.

## Hourly 1352 HIGH (`notes.md` §151)

TypeSafe Jev stays the default path.
Jev decides generator writes code owns irreversible.
never classifies.
L0 is not calibration.
0.227 to 0.077 *theirs*.
L1 ECE 0.100 *theirs*.
answers nothing itself.
never summarizes.
noul carries no confidence.
63.9% to 81.8% *theirs*.
0.75 still soft.
legal UCI.
quick_eval acc 0.6234 *theirs*.
do not quote 0.7518.
first card revisit tag no prior notes card.
Soft judgment never sole veto.
catalog ≠ endorsement. *theirs* not Harbor.
hourly 1352 / notes.md §151
Parent merges only after ADV_PASS.
glance §147, hourly 1203 §148, lev §149, and hourly 1256 §150 are on main. This fold is §151 only.
Do not reopen or amend PR #23 through #76. Do not reclaim §147–§150.
Does not bump 0.5.1. Skip Archer.
`invented_signal: false`.
The uniqueness lock lives in `research/notes.md` and the uniqueness gate fixture only.

## Hourly 1203 HIGH (`notes.md` §148)

Swift 6 bridge into Apple Foundation Models.
40 to 150 ms *theirs*.
Never embed API keys.
bridge is not an on-device replica.
Jev remains the decision model.
false alarms 24.8% to 65.2% to 47.2% *theirs*.
67,890 decisions *theirs* not Harbor.
No Jev outputs were used.
detection gain is not a license to auto-block.
Soft judgment never sole veto.
$0.000851 in 23.6s *theirs*.
measured $0.000143 *theirs*.
exit code 2 is code.
noul p=0.02 is not a merge.
one crawl is not Harbor.
playground is not a bench.
PyPI 0.6.0 pending.
0.612 against 0.740 *theirs*.
AUROC 0.899 *theirs*.
HTTP 200 was 401.
verified:false.
sha 024a68eade83 was 7d433994fbde.
Qwen3-0.6B ≠ Archer.
Gemma 4 ≠ Archer.
densify §145 not a sibling first sighting.
densify §146 not a sibling first sighting.
densify §131 not a sibling first sighting.
densify §129 not a sibling first sighting.
Models propose. Application keeps policy.
first card revisit tag no prior notes card.
code enumerates model picks code gates.
shadow mode proceeds anyway.
n=10 is not Harbor.
skip-thin empty SHA HTTP 409.
catalog ≠ endorsement. *theirs* not Harbor.
hourly 1203 / notes.md §148
Parent merges only after ADV_PASS.
Do not reopen or amend PR #23-#72. Does not bump 0.5.1. Skip Archer.
`invented_signal: false`.

Hourly 1203 uniqueness lock: peterfriese/jev-foundation-models Swift 6 bridge into Apple Foundation Models; peterfriese/jev-foundation-models 1★ Apache-2.0 Swift HEAD 27963995965d README SHA b40b836f4396; 40 to 150 ms *theirs*; zero hallucinations is a README claim *theirs*; Never embed API keys; bridge is not an on-device replica; Apple Foundation Models host the call shape; Jev remains the decision model; Alexander-Ollman/laya-ft signal detection; Alexander-Ollman/laya-ft 0★ NOASSERTION Py HEAD 41f8247c3969 README SHA e97e314c88d5; Aegis prompts F1 60.6% 81.5% 83.7% *theirs*; Aegis responses 37.4% 69.5% 77.0% *theirs*; ToxicChat 36.4% 50.5% 53.3% *theirs*; WildGuard prompts 48.7% 59.4% 65.7% *theirs*; WildGuard responses 20.8% 53.3% 51.6% *theirs*; BeaverTails 6.0% 34.1% 59.4% *theirs*; false alarms 24.8% to 65.2% to 47.2% *theirs*; XSTest 250 harmless prompts *theirs*; 67,890 decisions *theirs* not Harbor; No Jev outputs were used; not a dependable general-purpose safety filter *theirs*; detection gain is not a license to auto-block; Soft judgment never sole veto; Ejokey/lightjev $0.000851 in 23.6s *theirs*; Ejokey/lightjev 0★ MIT Py HEAD 921fffb588b9 README SHA 30fa74b9f711; six pages four hits 3/3 *theirs*; about $0.0001 per decision *theirs*; STOP always available; one crawl is not Harbor; code owns the queue; ruslanlap/jev-gate measured $0.000143 *theirs*; ruslanlap/jev-gate 0★ MIT Py HEAD 300014a1bdea README SHA 96e31d8dc5d8; exit code 2 is code; noul p=0.02 is not a merge; five typed questions; probabilities must sum to 1 within 0.02 *theirs*; ruslanlap/jev-gate ≠ hf:SargeDev/jev-gate-student-b-merged; Renwang-Huang/arbitype independent not an official TypeSafe product; Renwang-Huang/arbitype 0★ MIT Py HEAD 454cf2c4a345 README SHA ffa11f281a52; PyPI 0.6.0 pending; Renwang-Huang/arbitype ≠ Renwang-Huang/typesafe-mcp; Codercise/jev-in-practice key stays in the Node process; Codercise/jev-in-practice 0★ MIT TS HEAD 02be666a30ad README SHA 3f0c47161028; playground is not a bench; fraud sales patent presets; emlama/jev-mcp saved tool is inputs context questions docs; emlama/jev-mcp 0★ MIT Py HEAD 4c7da93a21be README SHA a258eb52829c; emlama/jev-mcp ≠ burnigtm/jev-mcp ≠ jkudish/jev-mcp ≠ resumocast/jev-mcp ≠ tphakala/jev-mcp; single SQLite volume; hf:clduab11/jev-calibration-statistics HTTP 200 was 401; hf:clduab11/jev-calibration-statistics 0 likes sha 9bbe055ee875 mit; sha 9bbe055ee875 was 13f4fa48f2f2; 0.612 against 0.740 *theirs*; missed its main pre-registered bar *theirs*; AUROC 0.899 *theirs*; 9,075 passages 349 questions *theirs*; jev-1.13.0; Gemma 4 ≠ Archer; densify §145 not a sibling first sighting; hf:aimeigaoshou/agent-jev sha 024a68eade83 was 7d433994fbde; hf:aimeigaoshou/agent-jev 0 likes sha 024a68eade83 apache-2.0; verified:false; accuracy 0.7925 ECE 0.1687 Brier 0.0448 *theirs*; same numbers as §146 not a new Harbor; Qwen3-0.6B ≠ Archer; malevrigns/agent-jev ≠ hf:aimeigaoshou/agent-jev; densify §146 not a sibling first sighting; AkashPriyadarshii/jev-seo densify HEAD f42455ac951a was f8cb7c55c356; AkashPriyadarshii/jev-seo 27★ MIT Rust HEAD f42455ac951a README SHA 677171501c8e; README SHA 677171501c8e was e3290fd15add; 27★ was 21★; densify §131 not a sibling first sighting; catalog ≠ endorsement; dtduc-git/jevnav densify HEAD b7a12d2f54ce was 96f5438bea96; dtduc-git/jevnav 1★ Apache-2.0 Py HEAD b7a12d2f54ce README SHA 61ea35cc8f32; page truth not pixels; replay exits 1 with no model call *theirs*; densify §129 not a sibling first sighting; star 0 to 1 is star-noise; dtduc-git/jevnav ≠ pstong216/jevnav-demo; SoundBlaster/SwiftDecision first card revisit tag no prior notes card; SoundBlaster/SwiftDecision 0★ Apache-2.0 Swift HEAD 7af9416e1ac4 README SHA 54ad5d8e4886; Models propose. Application keeps policy; SoundBlaster/SwiftDecision ≠ peterfriese/jev-foundation-models ≠ SoundBlaster/SwiftDecision-Examples; Tongyun1/Jev-in-the-Loop densify HEAD 039c2117f4e3 was a60444c0c268; Tongyun1/Jev-in-the-Loop 0★ MIT Py HEAD 039c2117f4e3 README SHA ffe54ee54576; README SHA ffe54ee54576 was e4ebd224d5f8; Codex prepares inputs Jev picks the next action; operating a browser is not a calibrated Noul; hfnissum-byte/jevmerge code enumerates model picks code gates; hfnissum-byte/jevmerge 1★ NOASSERTION JS HEAD 2b472ca7304b README SHA b32e85e4909c; prakash5284 n=10 is not Harbor; $0.0019 *theirs*; theglitcharchitect/muse-skills shadow mode proceeds anyway; skip-thin Elue-dev/jev_elixir Shoaib-Asghar/jev-probe lvzhaobo/-jev-assayer empty SHA HTTP 409; ravinarayanan89/JevForce HTTP 404; jevonj05/jevonj05 name collision not a decision model; sunmont/pi-jev-dsk-agi acronym expansion is not TypeSafe Jev; hf:opg13/laya about 33 ms *theirs* not Harbor; hf:marcmagn1/jev-alt-systemone-trackio ≠ hf:marcmagn1/jev-alt-systemone-eval; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; wire-compat ≠ logit-equiv; serving substrate ≠ calibrated replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70/#71/#72; notes.md §148; peterfriese/jev-foundation-models 1★ Apache-2.0 Swift HEAD 27963995965d README SHA b40b836f4396; AbdelStark/abdelstark.github.io 0★ NOASSERTION HTML HEAD bd54fa76189c README SHA 8f7523bcaf57; Alexander-Ollman/laya-ft 0★ NOASSERTION Py HEAD 41f8247c3969 README SHA e97e314c88d5; AustinDKB/grass-optimizer 0★ NOASSERTION Py HEAD 6a0616ab83e1 README SHA e7ee8271da7e; BipinRajC/Jev-api-experiments 0★ NOASSERTION Py HEAD e57a266df0ea README SHA cee6481e2e5b; Codercise/jev-in-practice 0★ MIT TS HEAD 02be666a30ad README SHA 3f0c47161028; DevvGwardo/ghost-route 0★ MIT TS HEAD ca4e40fd94b4 README SHA b4be5c1f6893; Ejokey/lightjev 0★ MIT Py HEAD 921fffb588b9 README SHA 30fa74b9f711; Elue-dev/jev_elixir empty SHA HTTP 409; Georgy-hook/laya-rimworld-director 0★ GPL-3.0 Py HEAD fb82dbf34562 README SHA f25b95e16247; Jorgediamanto/jev-playground 0★ NOASSERTION Py HEAD b3b3d2d8f8db README SHA 7b9972acca45; Lavenir7/Jev2048 0★ NOASSERTION JS HEAD 9e8785ba82e1 README SHA aabbb986b729; Makia9879/pi-jev-router 0★ NOASSERTION TS HEAD 2f6aed131dc8 README SHA 81b43e3994fd; NikHeck/jev-benchmark 0★ NOASSERTION Py HEAD 4997038a2902 README SHA 9e6d3a30ef4b; Renwang-Huang/arbitype 0★ MIT Py HEAD 454cf2c4a345 README SHA ffa11f281a52; Shoaib-Asghar/jev-probe empty SHA HTTP 409; SoundBlaster/SwiftDecision-Examples 0★ MIT HEAD 378c8bc4564f README SHA 05e313ca7b00; Sy3058/jev-evaluate 0★ NOASSERTION Py HEAD 4e6424305b27 README SHA 9a4f7fc26e43; UtpalJayNadiger/find 0★ ISC TS HEAD 44247083ac90 README SHA 670a74958a92; ahtcfg24/codex-speculator 0★ MIT TS HEAD 8496757f0c86 README SHA 6caece2fcb2e; allebee/jevgrep 0★ MIT Py HEAD e7ec44aa801d README SHA 96102d2f6a22; allebee/pytest-jev 0★ MIT Py HEAD b24310cccf43 README SHA 7ab5e2e57a5a; babanomania/linkedin-bullshit-filter 0★ MIT TS HEAD 2838b3c6dc76 README SHA 408ff8140090; bangxiao0927/decidespeak 0★ Apache-2.0 Py HEAD 6558e1a9b157 README SHA d1b95ca6b74b; bitofant/laya 0★ NOASSERTION HEAD f9335cb99e9b README SHA 1a26983aef62; coreywoo27/Jev-Empowered-Qwen-mlx 0★ MIT Py HEAD a14c9b924351 README SHA 2131d40716fc; cornelflorea/jev-test 0★ NOASSERTION TS HEAD 42cadf15cc79 README SHA 35db91381f38; dannyowelch/jev-abstention-checker 0★ NOASSERTION TS HEAD fb2a0afa6220 README SHA acf5b81da07f; dante01yoon/laya-jev-arena 0★ NOASSERTION JS HEAD 4a723c55d31c README SHA a1280d76ddcd; datamonsterr/jev_auto_select_skills 0★ NOASSERTION TS HEAD ffa748ef2cab README SHA 37cd6e7ca9c4; diluteoxygen/JevName 0★ NOASSERTION JS HEAD 08f239452851 README SHA 4598ba81b321; edrache/jevworms 0★ NOASSERTION JS HEAD e79d677c7714 README SHA 098a1d2d3af3; emerson-buoy/jev-ticket-classifier 0★ NOASSERTION TS HEAD a51bd3faf388 README SHA 6a2f242d2409; emlama/jev-mcp 0★ MIT Py HEAD 4c7da93a21be README SHA a258eb52829c; fblissjr/typesafe-experiments 0★ MIT TS HEAD 0d21b21d3c0e README SHA 81d2df816c34; frahlg/laya-ems-test 0★ Apache-2.0 Py HEAD a7f72577dc0e README SHA 35993b958438; hazlema/jev-connect4 0★ MIT TS HEAD be4f9757a820 README SHA bcef5ccd0859; hf:marcmagn1/jev-alt-systemone-trackio 0 likes sha e8fe2df8f29c NOASSERTION; hf:opg13/laya 0 likes sha 99175af5d679 apache-2.0; hfnissum-byte/jevmerge 1★ NOASSERTION JS HEAD 2b472ca7304b README SHA b32e85e4909c; ishantanu/jevtraces 0★ Apache-2.0 Go HEAD 7053acccc254 README SHA f83ca85d1641; jayozer/jevzero 0★ MIT Py HEAD 601228d24a8a README SHA 1a6c376f01ef; jeonck/clinic-checklist 0★ NOASSERTION Py HEAD b693bfa56d42 README SHA e2bb49fe9f2a; jevonj05/jevonj05 0★ NOASSERTION Py HEAD eaf07387d305 README SHA 3743fe2fb819; jordilopez/pi-smart-router 0★ NOASSERTION TS HEAD 2cd38cc56af1 README SHA 89c03c160a85; karanb192/jev-skill-scout 0★ MIT JS HEAD a10b1a1fe71b README SHA 638dd7042894; ljbuturovic/jevgram 0★ NOASSERTION Py HEAD 73185b0df270 README SHA 2af501753734; luisrapalino/jev-smart-bets 0★ MIT TS HEAD a606f2b45195 README SHA 0f3714226f74; lvzhaobo/-jev-assayer empty SHA HTTP 409; lvzhaobo/jev-assayer 1★ NOASSERTION Py HEAD 795031c93e71 README SHA 7fe614bdf174; makiisthenes/JevAIExperimentation 0★ NOASSERTION Py HEAD dae1c2f867d0 README SHA e69de29bb2d1; moelahmady/shunt-jev 0★ MIT TS HEAD 47285110cf2a README SHA 2332516baf23; naiersaidane/jev-demos 0★ NOASSERTION TS HEAD dd8d6fe03da6 README SHA 6a41ac881196; olivere/systemone 0★ MIT Go HEAD fe90e12af0a0 README SHA ede6fced042e; p2kalita/Building-a-Harness-with-Jev-LangChain 0★ NOASSERTION Py HEAD 7c7318ebe703 README SHA 38bc6d9acddc; pavlealeksic/jev-hermes 0★ NOASSERTION Py HEAD ff858e957322 README SHA 2444a463e79c; perezjohn0/jevpav 0★ NOASSERTION HEAD 3185ac2bc377 README SHA ad253f8dfe83; piyushsonawane07/trueKeep 0★ NOASSERTION TS HEAD a072d99e6034 README SHA a217f090c99d; prakash5284/jev-vs-llm-resume-jd-eval 0★ NOASSERTION Py HEAD d9a80a8a00f4 README SHA 06b2104f5b63; pratik-codechef/jev-model 0★ NOASSERTION TS HEAD 5b3a8fb21b50 no README; punitarani/jeve 0★ NOASSERTION Py HEAD c12c66b809da README SHA 631ba86611e4; ravinarayanan89/JevForce HTTP 404; rishhavv/tabjev 0★ MIT JS HEAD 9b4abd1ee7d6 README SHA 15cbe787df05; ruslanlap/jev-gate 0★ MIT Py HEAD 300014a1bdea README SHA 96e31d8dc5d8; sathwikkuncham/laya-snake-arena 0★ Apache-2.0 Py HEAD e7227d789501 README SHA 6947e635bc72; shivpratapsinghpanwar/edgefront 0★ MIT Py HEAD 3b3771d69949 README SHA 7342f40028e9; singhdevhub-lovepreet/firstlight 0★ NOASSERTION TS HEAD 43378a949bce README SHA 5efe948df249; sliday/jev-chess-algo 0★ MIT TS HEAD 4462ace0895b README SHA 24e42556378c; sunmont/pi-jev-dsk-agi 0★ NOASSERTION TS HEAD 2aa1f06e5da6 README SHA b25ef30d534b; theglitcharchitect/muse-skills 0★ MIT Py HEAD f0cc9cc9cea6 README SHA a14927d3b12f; uibuckets/ai-decision-lab 0★ MIT Py HEAD bd237978608f README SHA bc88b74a1ba6; uibuckets/laya-local-service 0★ MIT Py HEAD 7b340cb7ab25 README SHA fbc8e3ca521a; wuxie888/jev-yaba-wechat 0★ MIT Py HEAD b29bd3c42cec README SHA 0744b3dd6268; AkashPriyadarshii/jev-seo 27★ MIT Rust HEAD f42455ac951a README SHA 677171501c8e; dtduc-git/jevnav 1★ Apache-2.0 Py HEAD b7a12d2f54ce README SHA 61ea35cc8f32; SoundBlaster/SwiftDecision 0★ Apache-2.0 Swift HEAD 7af9416e1ac4 README SHA 54ad5d8e4886; Tongyun1/Jev-in-the-Loop 0★ MIT Py HEAD 039c2117f4e3 README SHA ffe54ee54576; hf:aimeigaoshou/agent-jev 0 likes sha 024a68eade83 apache-2.0; hf:clduab11/jev-calibration-statistics 0 likes sha 9bbe055ee875 mit

## Hourly 1110 HIGH (`notes.md` §146)

same-species serving not an 18th scoring row.
act head untrained do not gate on it.
page to typed fields.
11 of 11 *theirs* not Harbor.
JSON chat ≠ calibrated Noul.
softmax over letter slots ≠ calibrated Noul.
independent project built only from the public post.
schema-valid is not the same as correct.
README is a kev tree copy.
copied kev numbers are not a musubi bench.
musubi-labs/musubi-jev ≠ jaredpalmer/kev.
wire-compat ≠ logit-equiv.
serving substrate ≠ calibrated replica.
ranking ≠ calibration.
decision act/review/abstain is code.
act_above 0.8 still soft.
Soft is not a sole veto.
densify §142 not a sibling first sighting.
densify §143 not a sibling first sighting.
densify §139 not a sibling first sighting.
densify §145 not a sibling first sighting.
64/64 and 63/64 *theirs* not Harbor.
star 0 to 1 is star-noise.
cloudbtl/JevRAG ≠ emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark.
0xagentlabs/jev-xiangqi ≠ Zafer-Liu/jev-xiangqi.
s3rli/jevips name collision not a decision model.
skip-thin Alpha-Harper-Franklin/astra-jev empty SHA HTTP 409.
hf:marcmagn1/jev-alt-systemone-eval README 404 models HTTP 401 *theirs*.
catalog ≠ endorsement. *theirs* not Harbor.
hourly 1110 / notes.md §146
Do not copy keys. Fresh PR off `6be01e0429ed` (merged #70).
Do not reopen or amend PR #23-#70. Does not bump 0.5.0. Skip Archer.
`invented_signal: false`.

Hourly 1110 uniqueness lock: hf:thaitea/laya-vision 13 likes sha a2653db2831b cc-by-nc-sa-4.0; SmolVLM-256M vision typed choice/score/noul; same-species serving not an 18th scoring row; independent not affiliated; A-OKVQA 63.1% ECE 0.266 to 0.094 *theirs*; ScienceQA 89.0% ECE 0.080 to 0.034 *theirs*; VQAv2 noul 73.2% ECE 0.085 to 0.042 *theirs*; All n=8235 75.9% ECE 0.035 *theirs* not Harbor; VQAv2 re-split not comparable to published VQAv2; about 71 ms *theirs*; option order varies 1.2 points *theirs*; act head untrained do not gate on it; not a drop-in replacement for Laya text checkpoint; usage loads thaitea/laya-vision-smolvlm-256m already §87; hf:thaitea/laya-vision ≠ thaitea/laya-vision-smolvlm-256m card id; AntonG87/codearia-sieve 1★ MIT TS HEAD 64ecd4151726 README SHA b03a3d29ab22; page to typed fields; 6 of 6 *theirs*; 11 of 11 *theirs* not Harbor; robots-disallowed did not fetch; no model required for the parse; 7Zenox/gemma-jev 0★ NOASSERTION Py HEAD 2eed119e03ff README SHA c3b58d6a15a9; generation-free letter slots; 144 authored decisions *theirs*; Gemma 3 270M 0.293 below chance 0.333 *theirs*; Gemma 4 E2B-it JSON chat 0.807 *theirs*; Qwen3.5-4B JSON chat 0.813 *theirs*; JSON chat ≠ calibrated Noul; softmax over letter slots ≠ calibrated Noul; bf16 vs fp32 argmax-agreement check not run; Gemma ≠ Archer; Qwen3.5 ≠ Archer; Pdbz199/local-decision-model 0★ MIT Py HEAD ddceb5829849 README SHA 80659ec966f5; independent project built only from the public post; one pass no generation; schema-valid is not the same as correct; musubi-labs/musubi-jev 0★ Apache-2.0 HEAD e943f21e4057 README SHA 8ffd43564204; README is a kev tree copy; copied kev numbers are not a musubi bench; musubi-labs/musubi-jev ≠ jaredpalmer/kev; quaeast/vllm2jev 0★ NOASSERTION Py HEAD 8a51f94961ea README SHA be92356f1176; does not reproduce Jev calibration; wire-compat ≠ logit-equiv; IAmJSD/pg-laya 0★ Apache-2.0 Rust HEAD 1bc66a4d6a7f README SHA 03476be41744; SQL choice score noul; serving substrate ≠ calibrated replica; IAmJSD/pg-laya ≠ realZachi/pg-jev ≠ giuliosmall/pg_typesafe; gbesse/jev-rerank-server 0★ MIT JS HEAD b28cef5e34a6 README SHA 91167c66c29c; SciFact n=25 nDCG@10 0.616377 to 0.718260 *theirs*; Recall@10 0.84 unchanged *theirs*; ranking ≠ calibration; MarkChu-git/typesafe-mcp 0★ MIT HEAD a064b14207c0 README SHA ae27210cc5af; decision act/review/abstain is code; act_above 0.8 still soft; MarkChu-git/typesafe-mcp ≠ itsmostafa/typesafe-mcp ≠ cyrusasco/typesafe-mcp ≠ Renwang-Huang/typesafe-mcp; pythongiant/laya-drift densify 4★ TS HEAD d33db6736ed8 README SHA 7af1781c28c5 was 334953e5cb8f / 6662121ba0f3; monitor agent drift; densify §142 not a sibling first sighting; Adkid-Zephyr/chinese-workflow-decision-bench densify 1★ MIT Py HEAD b694dc6dbcba README SHA 9ef2b7d76a37 was 6d0a7c2af303 / 4ed71a36cd51; 64/64 and 63/64 *theirs* not Harbor; synthetic not a group-chat dump; densify §145 not a sibling first sighting; turenlabs/jast densify 1★ MIT Rust HEAD c6588285208f README SHA d9214ca31f92 unchanged; star 0 to 1 is star-noise; densify §145 not a sibling first sighting; JabbaKadabra/SystemOneDotNet densify MIT C# HEAD 5120ffb84cc5 README SHA 0809f98d4c93 was 5bff3394281c / 76a9188c180a; unofficial .NET client; wire-compat ≠ logit-equiv; densify §143 not a sibling first sighting; arnavm-codes/JevFence densify HEAD 7e277474ff5e README SHA 2bbb684757de was 6fe62ca7b10c / 5441aaeaace0; soft scores ≠ hard gates; densify §145 not a sibling first sighting; cloudbtl/JevRAG 0★ Apache-2.0 Py HEAD 307ab19ee9cf README SHA 9b814bb6624b; first card revisit tag no prior notes card; cloudbtl/JevRAG ≠ emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; gbesse/decision-workbench densify MIT JS HEAD 877d1a9add5b README SHA 24cce8900d67 was 8889cf3750a3 / 14a3bf79da7a; human review separate from model output; demo scores are not accuracy measurements; densify §139 not a sibling first sighting; 0xagentlabs/jev-xiangqi ≠ Zafer-Liu/jev-xiangqi; RyanNg1403/jev-cli ≠ gnapse/jev-cli ≠ sunchojack/jev-cli; KennethAshley/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev; malevrigns/agent-jev ≠ hf:aimeigaoshou/agent-jev; 79.25% 1585/2000 ECE 0.1687 *theirs* not Harbor; kidzik/jiffy probabilities are uncalibrated; s3rli/jevips name collision not a decision model; skip-thin Alpha-Harper-Franklin/astra-jev jonas050210/Laya_Playground pietrushka/jev-youtube-filter empty SHA HTTP 409; skip-thin THANK-YOU-FOR-YOUR-ORDER-ASDF123/repo-laya4qxd Ylr9933/JevForAgent empty README; hf:marcmagn1/jev-alt-systemone-eval dataset sha 95f679e8455b README 404 models HTTP 401 *theirs*; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70; notes.md §146

## Hourly 1019 HIGH (`notes.md` §145)

schema-valid is not the same as correct.
API confidence is not P(correct).
GEPA revises Choice instructions/criteria with weights fixed.
jev-1.13.0 weights fixed.
Brier 0.1357→0.0747 *theirs*.
F1 69.1%→79.7% *theirs*.
FN 4→6.
review-queue policy is not F1.
Soft is not gate.
Not an 18th scoring-table species.
Every claim is labeled and sourced.
catalog ≠ endorsement.
发送永远手动.
About 180 ms.
routing ≠ permission.
$0.00241 *theirs*.
Not a screenshot agent.
game success ≠ calibrated Noul.
pi-follow-through threshold 0.8 still soft.
wire-compat ≠ logit-equiv.
densify §144 not a sibling first sighting.
pi-jev-context densify §134 not a sibling first sighting.
aliaihub/awesome-jev-usecases ≠ anandi1989/awesome-jev-usecases ≠ whyashthakker/awesome-jev-use-cases.
rezoch340/jev-chat-JARVIS-windows ≠ Finderchangchang/jev-chat-JARVIS.
aakgna/jevcal ≠ abhixhek/jevcal.
007M7/jev-chat ≠ w3cj/jev-chat ≠ Manta-Boardgame/jev-chat.
fstandhartinger/jev-router ≠ gargpratyush/jev-router.
prakash7474/Jev_guard ≠ leepokai/jev-guard.
rdutra/laya-mcp ≠ PerryLink/laya-mcp ≠ wsargent/laya-mcp.
Kourin1996/jev-playground ≠ wustep/jev-playground.
ai-ecoverse/cua-s1.js Cua-S1 ≠ TypeSafe.
skip-thin Unnati-23/jev-typesafe-guide antoniofaical/digital-twin-classifier-jev leonezhu/agent-kits empty README.
skip-thin wjw66/deepseek-harness-jev-pre-compaction ziwon/jev-actor empty SHA HTTP 409.
hf:chanoian/openjev-mlx-demo HTTP 401 *theirs*.
hf:clduab11/jev-calibration-statistics HTTP 401 *theirs*.
hf:yasserrmd/laya-lab HTTP 401 *theirs*.
catalog ≠ endorsement. *theirs* not Harbor.
hourly 1019 / notes.md §145
Do not copy keys. Fresh PR off `c801b1a185c6` (merged #69).
Do not reopen or amend PR #23–#69. Does not bump 0.5.0. Skip Archer.
`invented_signal: false`.

Hourly 1019 uniqueness lock: praneeth16/adapting-jev-with-gepa ADE Corpus V2 GEPA; schema-valid is not the same as correct; API confidence is not P(correct); GEPA revises Choice instructions/criteria with weights fixed; jev-1.13.0 weights fixed; Brier 0.1357→0.0747 *theirs*; F1 69.1%→79.7% *theirs*; FN 4→6; review-queue policy is not F1; Soft is not gate; Not an 18th scoring-table species; aliaihub/awesome-jev-usecases 15★ NOASSERTION HEAD 6cbde6bd3569 README SHA 7ea135c6345d; Every claim is labeled and sourced; catalog ≠ endorsement; aliaihub/awesome-jev-usecases ≠ anandi1989/awesome-jev-usecases ≠ whyashthakker/awesome-jev-use-cases; rezoch340/jev-chat-JARVIS-windows 6★ MIT Py HEAD 26b686301437 README SHA 0714736b68c3; 发送永远手动; rezoch340/jev-chat-JARVIS-windows ≠ Finderchangchang/jev-chat-JARVIS; iamvatsalpatel/tiershift 3★ MIT TS HEAD 16a0826b9f62 README SHA 46fcb1cb191b; About 180 ms; routing ≠ permission; Bring-AI/jev-rl 2★ MIT Py HEAD 36f89cec85a2 README SHA 6283da6011b7; $0.00241 *theirs*; daniel4x/JevEmon 2★ GPL-3.0 HEAD 572454c69bf7 README SHA 8fc00d12848d; Not a screenshot agent; game success ≠ calibrated Noul; spoonnotfound/soupbase 2★ MIT TS HEAD 3e874e83e710 README SHA 3106bc96d6ab; Nabsku/pi-follow-through 1★ MIT TS HEAD c62ef28ff4ac README SHA 64000451b79e; pi-follow-through threshold 0.8 still soft; dashbi1/jev-sim 1★ MIT Py HEAD 753c7397d73c README SHA 05fd960799d2; wire-compat ≠ logit-equiv; jev-jarvis/jev-jarvis densify 8★ MIT Py HEAD a94e3b967ef5 README SHA e441335b1df0 was be68dd7993f0 / efe7e47a6fe8; densify §144 not a sibling first sighting; Nyarlathoteppppp/pi-jev-context densify 5★ MIT TS HEAD 96371e2bf144 README SHA d4276222a436 was f0128a86478f; pi-jev-context densify §134 not a sibling first sighting; Nyarlathoteppppp/pi-jev-context ≠ kevinpita/pi-jev-context; fly88oj/jebii 0★ MIT JS HEAD 5cbe527ed791 README SHA b4a76b8aba9d; generallymatthew/factlabel 0★ Apache-2.0 Py HEAD b3d3bceee044 README SHA b1cda6c4646e; aakgna/jevcal ≠ abhixhek/jevcal; 007M7/jev-chat ≠ w3cj/jev-chat ≠ Manta-Boardgame/jev-chat; fstandhartinger/jev-router ≠ gargpratyush/jev-router; prakash7474/Jev_guard ≠ leepokai/jev-guard; rdutra/laya-mcp ≠ PerryLink/laya-mcp ≠ wsargent/laya-mcp; Kourin1996/jev-playground ≠ wustep/jev-playground; ai-ecoverse/cua-s1.js Cua-S1 ≠ TypeSafe; skip-thin Unnati-23/jev-typesafe-guide antoniofaical/digital-twin-classifier-jev leonezhu/agent-kits empty README; skip-thin wjw66/deepseek-harness-jev-pre-compaction ziwon/jev-actor empty SHA HTTP 409; hf:chanoian/openjev-mlx-demo HTTP 401 *theirs*; hf:clduab11/jev-calibration-statistics HTTP 401 *theirs*; hf:yasserrmd/laya-lab HTTP 401 *theirs*; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69; notes.md §145

## Hourly 0923 HIGH (`notes.md` §144)

intellyweave GLiNER OSINT.
Locate ≠ decide.
finite choices + none.
4B frozen+head 0.916 vs 27B zs 0.875 *theirs*.
8 questions 22.6 ms *theirs*.
softmax ≠ calibrated Noul.
AgentBeam local security layer.
soft scores ≠ hard gates.
unofficial not affiliated.
wire-compat ≠ logit-equiv.
chips virtual.
game success ≠ calibrated Noul.
densify §121 not a sibling first sighting.
densify §139 not a sibling first sighting.
densify §141 not a sibling first sighting.
Runs every rule against every line in parallel. No skimming.
heuristic conversion ≠ calibrated Noul.
Median 275 ms.
trolley 0.99 vs 0.78.
11/11/7 match/differ/undecided of 29 *theirs*.
retired name reservation is not a replica.
PerryLink/laya-mcp ≠ wsargent/laya-mcp.
DreamBlooms/dohnuts.cpp ≠ PsiACE/dohnuts.
ClemensSchartmueller/jev-guard ≠ leepokai/jev-guard ≠ seb4ez/jevguard.
AABBAASS1/jev-router ≠ gargpratyush/jev-router ≠ Akashdb5/jev-router ≠ daviddl9/jev-router.
atharvamhaske/typesafe-sdk-go ≠ kisshan13/typesafe-ai-go ≠ stacklok/typesafe-go ≠ Nibir1/typesafe-go ≠ peach-zhang/typesafe-go ≠ draganm/go-jev ≠ kataras/jev ≠ robertjndw/gosys1 ≠ Stumble/jev-go.
skip-thin gnapse/jev-cli HTTP 404.
hf:Skylarcc/Laya-Online HTTP 401 *theirs*.
hf:piratehack009/laya-cn-flash-triage HTTP 404 *theirs*.
catalog ≠ endorsement. *theirs* not Harbor.
hourly 0923 / notes.md §144
Do not copy keys. Fresh PR off `89a26925295e` (merged #67).
Do not reopen or amend PR #23–#67. Does not bump 0.5.0. Skip Archer.
`invented_signal: false`.

Hourly 0923 uniqueness lock: vericle/intellyweave 76★ BSD-3-Clause Py HEAD ff4152ce9d20 README SHA 3afa702012e8; GLiNER OSINT; Locate ≠ decide; genai-craft/openvons 13★ NOASSERTION Py HEAD c2683c4539a7 README SHA 85164d409725; finite choices + none; 4B frozen+head 0.916 vs 27B zs 0.875 *theirs*; 8 questions 22.6 ms *theirs*; softmax ≠ calibrated Noul; whyashthakker/beam-cli 11★ AGPL-3.0 TS HEAD 5162ec66179a README SHA d55847ca5681; AgentBeam local security layer; soft scores ≠ hard gates; atharvamhaske/typesafe-sdk-go 8★ MIT Go HEAD 6ea04182d356 README SHA 8d90abda1f58; unofficial not affiliated; wire-compat ≠ logit-equiv; atharvamhaske/typesafe-sdk-go ≠ kisshan13/typesafe-ai-go ≠ stacklok/typesafe-go ≠ Nibir1/typesafe-go ≠ peach-zhang/typesafe-go ≠ draganm/go-jev ≠ kataras/jev ≠ robertjndw/gosys1 ≠ Stumble/jev-go; Prophetlab/JevPokerBench 7★ MIT Py HEAD 9c9816688a3c README SHA 0fcd6807b9c3; chips virtual; game success ≠ calibrated Noul; *theirs* not Harbor; tyler-dot-earth/patdown densify 11★ NOASSERTION TS HEAD 8b2b2b591470 README SHA 1052b6da2c25 was ae0e277fdd64 / 275f4b9c; Block/steer/fuzzy lint; judge swappable; default TypeSafe/Jev; provider-neutral; densify §121 not a sibling first sighting; evoke-build/evoke densify 8★ Apache-2.0 Rust HEAD 50c9637ef11f README SHA 72ec0e65c432 was ca8a311743fe / fcce876e2cab; Jev is the first adapter; the design is bound to no engine; densify §139 not a sibling first sighting; lukstei/slop-grader 5★ MIT TS HEAD b60332684ff8 README SHA bbc1604754d3; Runs every rule against every line in parallel. No skimming; sumleo/prompt2jev densify 2★ MIT Py HEAD f3b6bc763b74 README SHA 3d58e8c10075 was bd9cd8a471a6 / afc36885861e; heuristic conversion ≠ calibrated Noul; densify §141 not a sibling first sighting; Andymulb/jev_the_philosopher 0★ MIT TeX HEAD 334e3f9b83e5 README SHA 8db05448b75f; Median 275 ms; trolley 0.99 vs 0.78; 11/11/7 match/differ/undecided of 29 *theirs*; PerryLink/layacore 0★ Apache HEAD 12afe3af5edc README SHA f78b73d21cf7; retired name reservation; the project is now PerryLink/laya-mcp; retired name reservation is not a replica; PerryLink/layacore-mcp HEAD b006cc7c3f87 README SHA 1177f286f3f8; PerryLink/laya-mcp-npm launcher not implementation HEAD 426e965b4c48 README SHA 98ed0d448b09; PerryLink/laya-mcp ≠ wsargent/laya-mcp; DreamBlooms/dohnuts.cpp ≠ PsiACE/dohnuts; ClemensSchartmueller/jev-guard ≠ leepokai/jev-guard ≠ seb4ez/jevguard; AABBAASS1/jev-router ≠ gargpratyush/jev-router ≠ Akashdb5/jev-router ≠ daviddl9/jev-router; wustep/jev-playground ≠ AbnormalPilot/jev-playground ≠ mizchi/jev-playground; Li-Evan/awesome-jev ≠ Omrigotlieb/awesome-jev ≠ youzizzz1028/Awesome-Jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev; sunchojack/jev-cli ≠ gnapse/jev-cli; Alistair77/openjev ≠ Zefan-Cai/Open-Jev ≠ razorback16/openjev; jev-jarvis/jev-jarvis ≠ eatmoreduck/jev-jarvis; Renwang-Huang/typesafe-mcp ≠ itsmostafa/typesafe-mcp; inematds/laya ≠ convaiinnovations/laya ≠ NandhaKishorM/laya; kataras/jev ≠ okooo5km/jev ≠ sebastianbugal/jev ≠ dannote/jev; ai-ecoverse/kev.js ≠ jaredpalmer/kev; skip-thin gnapse/jev-cli HTTP 404 fr4j4/system-one-arena nothingmn/Jev.Sdk youniszhang/jev-local Vaibhaav-Tiwari/fly-doom-jev fengliner/jev-tank-battle ngouard5/jeveuxaider-design empty SHA; hf:Skylarcc/Laya-Online HTTP 401 *theirs*; hf:piratehack009/laya-cn-flash-triage HTTP 404 *theirs*; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67; notes.md §144

## Hourly 0823 HIGH (`notes.md` §143)

dohnuts densify MODEL_CARD / JevBench 65.80% vs Jev 86.58%.
Laya multi 47.62%.
78.21% macro accuracy *theirs*.
180,031 decisions *theirs*.
same-species serving not an 18th scoring row.
densify §137 not a sibling first sighting.
field→value match among supplied options not free text.
Cua-S1 ≠ TypeSafe.
FluidInference/FluidUse ≠ FluidInference/laya-coreml ≠ AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml.
Screenshots aren't uploaded.
Jev is the only model.
not fully offline.
JSON 0.909 letters 0.907 *theirs*.
13 600 / 13 600 *theirs*.
softmax over letters ≠ calibrated Noul.
model=jev-auto.
AG News 0.910 *theirs*.
Banking77 0.870 *theirs*.
DAIR Emotion 0.480 *theirs*.
Fastest and cheapest web agent *theirs*.
densify description rewrite.
TypeSafeAI/typesafe-playground ≠ kavehmz/typesafe-playground ≠ nickthompson480/typesafe-ai-playground.
No generative fallback.
Unofficial research repo. Not affiliated with TypeSafe AI.
skip-thin GokhanCalkap/LayaCode fredzhaozonghui/LAYA1 empty SHA.
Abhi895/Laya ≠ convaiinnovations/laya.
mjdileep/OpenJev ≠ Zefan-Cai/Open-Jev.
Abhi001vj/system-one-open ≠ mithalouni/system-one-open ≠ sgoedecke/system-one.
ZulfiFazhar/system-one ≠ sgoedecke/system-one.
Futureppo/typesafe_register key-farming skip.
catalog ≠ endorsement. *theirs* not Harbor.
hourly 0823 / notes.md §143
Do not copy keys. Fresh PR off `41fa40c` (merged #66).
Do not reopen or amend PR #23–#66. Does not bump 0.5.0. Skip Archer.
`invented_signal: false`.

Hourly 0823 uniqueness lock: PsiACE/dohnuts densify 11★ Apache-2.0 HEAD 253766e5fcb7 README SHA 4b5b019deba9 was a5049834489c / e1b448c440b5; MODEL_CARD + training dataset refs; JevBench 65.80% vs Jev 86.58% / Laya multi 47.62% *theirs*; 152 / 231 *theirs*; 78.21% macro accuracy *theirs*; 180,031 decisions *theirs*; Qwen3.5-0.8B; Joint RLCD *theirs*; Dohnuts ≠ TypeSafe; densify §137 not a sibling first sighting; same-species serving not an 18th scoring row; SHA move is not a replica; FluidInference/FluidUse 3★ Apache-2.0 Swift HEAD c18071d791eb README SHA f1cba4a244bb; on-device Mac form CU; Accessibility API; CUA-S1-FORMS CoreML ~706K params ~1ms Neural Engine; field→value match among supplied options not free text; Cua-S1 ≠ TypeSafe; FluidInference/FluidUse ≠ FluidInference/laya-coreml ≠ AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml; serving substrate ≠ calibrated replica; shhivv/third-hand 274★ MIT Swift HEAD 430394b35dbb README SHA b615d7c3fd19; Screenshots aren't uploaded; Jev is the only model; not fully offline; typesafe-ai/system-one-adapter-python 226★ MIT HEAD adffc2eab300 README SHA d01afbf0499e; Drop-in TypeSafeClient replacement backed by LLM APIs; wire-compat ≠ logit-equiv; typesafe-ai/typesafe-sdk-js 203★ MIT HEAD 66880ccded6c README SHA 7e834076c14e; typesafe-ai/typesafe-sdk-python 175★ MIT HEAD 2ce5c65f1364 README SHA 361a3bc13e19; catalog ≠ endorsement; r-ms/mini-jev 40★ MIT HEAD ca612198bfb6 README SHA 565b70c4cf4d; read the option letter's logits instead of generating JSON; yuki-oshio/mini-jev ≠ r-ms/mini-jev; JSON 0.909 letters 0.907 *theirs*; 13 600 / 13 600 *theirs*; softmax over letters ≠ calibrated Noul; Das-rebel/a3m-router 16★ MIT HEAD 62caefe59315 README SHA c19e802d5cf2; model=jev-auto; routing ≠ permission; AbdelStark/jev-benchmarks 13★ Apache-2.0 HEAD 0d610cc53e79 README SHA 5fd3627f7de4; AG News 0.910 *theirs*; Banking77 0.870 *theirs*; DAIR Emotion 0.480 *theirs*; *theirs* not Harbor; browser-use/jev-ultrafast densify 14622★ MIT HEAD 1231850a0bf1 README SHA fa7d079f9192; Fastest and cheapest web agent *theirs*; densify description rewrite; pythongiant/laya-drift densify 4★ HEAD 334953e5cb8f README SHA 6662121ba0f3 was fc94b71cf7dd / 55ef2343ee5d; opencode plugin to calculate agentic drift over time *theirs*; densify §142 not a sibling first sighting; BlinkWrite/pii-masker densify 1★ MIT HEAD 6ad202ab4443 README SHA 27931758af6c; On-device reversible PII masking *theirs*; Locate ≠ decide; TypeSafeAI/typesafe-playground ≠ kavehmz/typesafe-playground ≠ nickthompson480/typesafe-ai-playground; siliconkernel/vllm-jev-decison 8★ MIT HEAD a9362d52b9a8; No generative fallback; Stumble/jev-go 3★ MIT HEAD a475dc925ba6; Twister915/typesafe-ai 11★ Apache-2.0 Rust HEAD d4455efb1d06; rorshopping/jev-on-a-laptop 23★ HEAD 5821d9106103; Unofficial research repo. Not affiliated with TypeSafe AI; Qwen2.5 ≠ Archer; skip-thin GokhanCalkap/LayaCode fredzhaozonghui/LAYA1 empty SHA; Abhi895/Laya ≠ convaiinnovations/laya; mjdileep/OpenJev ≠ Zefan-Cai/Open-Jev; Abhi001vj/system-one-open ≠ mithalouni/system-one-open ≠ sgoedecke/system-one; ZulfiFazhar/system-one ≠ sgoedecke/system-one; Futureppo/typesafe_register key-farming skip; soft scores ≠ hard gates; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66; notes.md §143

## Hourly 0707 HIGH (`notes.md` §142)

Jev-cu text-only CU / 只传文字，不传截图.
Text only no screenshots. Codex CU executes.
100% of our tax document corpus at $0.001 per page.
TaxCalcBench 0 strict errors *theirs*.
blank IRS 38 strict errors 5.05% *theirs*.
100% of corpus *theirs* not Harbor.
The model does not receive screenshots.
game success ≠ calibrated Noul.
21 seconds for 9 actions *theirs*.
A completed booking is not demonstrated.
droidrun/mobile-jev ≠ Friedjof/jev-mobile.
giuliosmall/pg_typesafe ≠ realZachi/pg-jev.
itsmostafa/typesafe-mcp ≠ cyrusasco/typesafe-mcp ≠ burnigtm/jev-mcp.
The field guide to typed decisions.
densify §141 not a sibling first sighting.
hf:Praveenrajus/jev-bench HTTP 401 was 200.
densify §107/§125 remainder.
densify §134 not a sibling first sighting.
ENEM 2025 *theirs* not Harbor.
Ying-Kai-Liao/jev-browser ≠ wy-coliney/jev-browser-use.
w3cj/jev-chat ≠ Manta-Boardgame/jev-chat.
snellingio/system-one ≠ sgoedecke/system-one ≠ Luke458/system-one ≠ developerekene/System-One.
stoleas/typesafe-computer-use ≠ awlevin/typesafe-computer-use.
holotwist/laya ≠ NandhaKishorM/laya.
RafalWilinski/vibecheck ≠ psyb0t/vibecheck.
dannote/jev ≠ okooo5km/jev ≠ sebastianbugal/jev.
skip-thin developerekene/System-One holotwist/laya wuzhiping/jev-laya empty SHA.
hf:s1lv3rj1nx/openjev-healthcare-router HTTP 401 *theirs*.
catalog ≠ endorsement. *theirs* not Harbor.
hourly 0707 / notes.md §142
Do not copy keys. Fresh PR off `34edba4` (merged #65).
Do not reopen or amend PR #23–#65. Does not bump 0.5.0. Skip Archer.
`invented_signal: false`.

Hourly 0707 uniqueness lock: Sac-Y/Jev-cu 524★ HEAD e2cc92d731fa README SHA 3deeafbc870f; 只传文字，不传截图; Text only no screenshots; Codex CU executes; local policy gates; kyotofin/tax-doc-classifier 322★ Apache-2.0 HEAD 3e95a77f763c README SHA 72c4f74b542e; 100% of our tax document corpus at $0.001 per page; TaxCalcBench 0 strict errors *theirs*; blank IRS 38 strict errors 5.05% *theirs*; 34× cheaper and 6× faster *theirs*; 261 IRS forms; 100% of corpus *theirs* not Harbor; fhshaik/typesafe-mario 319★ HEAD ca22449ed187 README SHA c489f9350414; The model does not receive screenshots; game success ≠ calibrated Noul; droidrun/mobile-jev 307★ MIT HEAD 395fc222beac README SHA d257fed2c5f7; 21 seconds for 9 actions *theirs*; A completed booking is not demonstrated; droidrun/mobile-jev ≠ Friedjof/jev-mobile; realZachi/pg-jev 269★ HEAD afd11fa856d7 README SHA e8735928b57d; giuliosmall/pg_typesafe ≠ realZachi/pg-jev; kitze/skillbox 220★ MIT HEAD cda64ad3310a README SHA dedcb6be3c39; itsmostafa/typesafe-mcp 181★ MIT HEAD d4c110c7edd8 README SHA 2bd68aff4299; itsmostafa/typesafe-mcp ≠ cyrusasco/typesafe-mcp ≠ burnigtm/jev-mcp; kitze/unclutter 157★ MIT HEAD 9ef9beccc1e5 README SHA 5ad63c67fd02; standardagents/jevpilot 147★ HEAD e1beeb13b9a9 README SHA ec386a81e12c; AbdelStark/awesome-typesafe-jev densify 417★ MIT HEAD d6ea2a0d6cf4 README SHA 234ae59a0b16 was a6a68b57888a / e47993484e3a; The field guide to typed decisions; Independent community project; densify §141 not a sibling first sighting; SHA move is not a replica; hf:Praveenrajus/jev-bench HTTP 401 was 200; densify §107/§125 remainder; *theirs* not Harbor; hf:wayfind/metask-jev-4b-policy-mix densify sha 5ecdd272ab4a README SHA c534ee82b141; densify §134 not a sibling first sighting; wayfind/metask-jev-4b-policy-mix ≠ metask-ai/metask-jev; patryckalves/jev-no-enem HEAD 7f85f787e3d1 README SHA 237b308df062; ENEM 2025 *theirs* not Harbor; 56.6% (103/182) *theirs*; ECE 0.078 *theirs*; Ying-Kai-Liao/jev-browser ≠ wy-coliney/jev-browser-use; w3cj/jev-chat ≠ Manta-Boardgame/jev-chat; snellingio/system-one ≠ sgoedecke/system-one ≠ Luke458/system-one ≠ developerekene/System-One; stoleas/typesafe-computer-use ≠ awlevin/typesafe-computer-use; holotwist/laya ≠ NandhaKishorM/laya; RafalWilinski/vibecheck ≠ psyb0t/vibecheck; dannote/jev ≠ okooo5km/jev ≠ sebastianbugal/jev; skip-thin developerekene/System-One holotwist/laya wuzhiping/jev-laya empty SHA; hf:s1lv3rj1nx/openjev-healthcare-router HTTP 401 *theirs*; hf:s1lv3rj1nx/openjev-heldout HTTP 401 *theirs*; hf:s1lv3rj1nx/openjev-mixture HTTP 401 *theirs*; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65; notes.md §142

## Hourly 0551 HIGH (`notes.md` §141)

kev Night-2 densify / densify §45 not a sibling first sighting.
locked OOD 0.684/0.837/0.852 *theirs*. Night-2 sign-off.
did not distill from Jev. densify §35 not a sibling first sighting.
APUS-OpenJev 9B 85.0% vs Jev API 82.5% *theirs* not Harbor.
Frozen80 n=80. Candidate probabilities are not calibrated confidence.
Jev is the first adapter the design is bound to no engine.
Zero Hallucinations marketing. Locate ≠ decide.
kylemclaren/jevsearch ≠ kylemclaren/jev-search.
stacklok/typesafe-go ≠ kisshan13/typesafe-ai-go.
DevMortimer/pi-typesafe ≠ twilwa/pi-typesafe.
hf:SeanLiu/Jev-Vision ≠ sseanliu/Jev-Vision.
sontakey/awesome-jev ≠ heyjunpenn/awesome-jev.
Giustino98/system-one-bench ≠ mallahyari/system-one-benchmark.
AbdelStark/awesome-typesafe-jev IS AbdelStark/awesome-typesafe.
Independent community project. skip-thin eatmoreduck/jev-jarvis.
densify §139 not a sibling first sighting.
catalog ≠ endorsement. *theirs* not Harbor.
hourly 0551 / notes.md §141
Do not copy keys. Fresh PR off `524c2d2` (merged #64).
Do not reopen or amend PR #23–#64. Does not bump 0.5.0. Skip Archer.
`invented_signal: false`.

Hourly 0551 uniqueness lock: jaredpalmer/kev densify HEAD 4f8110a3f862 README SHA d497d4b89427 was e0bcf50153f1 / 84b872488915; Night-2 sign-off; dates+unknowable deltas promoted for 0.8B/4B/9B; v7-base tags; PLAN SHA 5e6d2fca508e; locked OOD 0.684/0.837/0.852 *theirs*; test Kev-9B 0.837→0.852 *theirs*; Kev-4B 0.832→0.837 *theirs*; Kev-0.8B 0.668→0.684 *theirs*; T≈2.0 Brier 0.291→0.267 ECE 0.105→0.039 *theirs*; 7.5%→3.2% *theirs*; grouped T rejected; date_facts deadline 9B 0.72→0.80 raw→0.90 preprocessor; unknowable ≥0.9 → 0.00; 35B Not shipped MMLU-Pro 0.550 *theirs*; coverage@5% 0.62 from 0.66 at 9B *theirs*; not a controlled architecture comparison; Qwen3.5 ≠ Archer; Qwen3.6 ≠ Archer; temperature scaling ≠ ECE unless measured; Hub --revision is a pin not a replica; densify §45 not a sibling first sighting; SHA move is not a replica; bespokelabsai/nimble densify HEAD f136b3f75721 README SHA b3a04a310f1e; Publish original 2676 training examples and frozen 324 holdout; 90.1% vs Jev 93.2% vs base 66.4% *theirs*; did not distill from Jev; densify §35 not a sibling first sighting; AbdelStark/awesome-typesafe-jev 416★ MIT HEAD a6a68b57888a README SHA e47993484e3a github_id 1374058281; Independent community project; catalog ≠ endorsement; AbdelStark/awesome-typesafe-jev IS AbdelStark/awesome-typesafe (same GitHub id 1374058281); cookiespiggy/agentic-rl 103★ MIT HEAD 072bdd8c69de README SHA f2cc68b4e214; ch.25 Jev vs RL; RL ≠ calibrated Noul; DevMortimer/pi-typesafe 27★ MIT HEAD 8dcaa887e22c README SHA 6a11fb9df8b9; DevMortimer/pi-typesafe ≠ twilwa/pi-typesafe ≠ TheoOliveira/pi-jev; hf:gump2049/APUS-OpenJev-v1 sha e7e3cc0b9c82; APUS-OpenJev 9B 85.0% vs Jev API 82.5% *theirs* not Harbor; Frozen80 n=80; Candidate probabilities are not calibrated confidence; Qwen3.5-4B ≠ Archer; Qwen3.5-9B ≠ Archer; hf:SeanLiu/Jev-Vision sha 9b77fa5fdcd0 apache-2.0; POPE 0.907 MME 0.927 NLVR2 0.930 *theirs*; yes/no ECE 0.034 to 0.047 *theirs*; JevBench hard 52% at 91% mean confidence *theirs*; Qwen3-VL-8B ≠ Archer; LoRA ≠ RLCD replica; wire-compat ≠ logit-equiv; hf:SeanLiu/Jev-Vision ≠ sseanliu/Jev-Vision; evoke-build/evoke densify 6★ HEAD ca8a311743fe README SHA fcce876e2cab was 310840b56f1d / 02b91962cef4; Jev is the first adapter the design is bound to no engine; densify §139 not a sibling first sighting; 47thtechcorner/RayCodes_GLiNER_V1_Multi densify HEAD 485cf8045f73 README SHA 035b339c3789; Zero Hallucinations marketing; Locate ≠ decide; kylemclaren/jevsearch ≠ kylemclaren/jev-search ≠ kazuhideoki/jev-search; stacklok/typesafe-go ≠ kisshan13/typesafe-ai-go ≠ peach-zhang/typesafe-go ≠ Nibir1/typesafe-go; sontakey/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ AbdelStark/awesome-typesafe-jev; Giustino98/system-one-bench ≠ mallahyari/system-one-benchmark; skip-thin eatmoreduck/jev-jarvis githubMJ/Laya4j hawkymisc/typed-decision-bert jayanthbagare/laya_examples mohamedAtoui/Jev-project petrixh/laya-test sidhasadhak/jev-perfume-advisor wendaoheri/jev-browser zohaibtanwir/jev-samsho2 empty SHA; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64; notes.md §141

## Hourly 0445 HIGH (`notes.md` §140)

lcc keep-all / Token reduction alone is not cost reduction.
keeps essentially every block 0.0%/−0.5% *theirs*.
Chat 1282.3 ms vs gateway 232.1 ms ~1/5.5 *theirs*.
acc 0.796 ECE 0.027 *theirs*. How you ask mattered more.
Calibration is not yet measured. NanoJev densify JevHarness §115.
Awesomejev 691→802. serving substrate ≠ calibrated replica.
catalog ≠ endorsement. *theirs* not Harbor.
not a digital twin. Score fan-out ≠ chess engine. Jev cannot waive a failing check.
umgbhalla/jevx ≠ hawkyre/jevx. ryanzen9/XFlow ≠ hawkyre/jevx.
Tsagaanbayr1/jev-tetris ≠ planstack-ai/jev-tetris-benchmark.
wizicer/jev_info_site ≠ JingHao-Leon/awesome-jev-apps.
Do not copy keys. Fresh PR off `777546f` (merged #63).
Do not reopen or amend PR #23–#63. Does not bump 0.5.0. Skip Archer.
`invented_signal: false`.

Hourly 0445 uniqueness lock: lucasmartins-ai/lcc 7★ MIT HEAD a7e86fb60997 README SHA 877831764be9; keeps essentially every block 0.0%/−0.5% *theirs*; mechanical −70.0% Jev −52.1% *theirs*; mock Laya = Jev −22.6% on XL withdrawn; Token reduction alone is not cost reduction; N=18 pilot not Harbor; David-Lolly/Jev-Compatible 3★ HEAD e52e963d8539 README SHA 6e5ff22d40a6; Chat 1282.3 ms vs gateway 232.1 ms ~1/5.5 *theirs*; 3/3 n=3; Softmax over candidate logprobs; Qwen3.8-27B ≠ Archer; wire-compat ≠ logit-equiv; hwfengcs/any2jev 2★ Apache-2.0 HEAD 719b0eb9eefe README SHA 27e0af212cd5; independent not affiliated; acc 0.796 ECE 0.027 *theirs*; 42 ms vs JSON 778 ms *theirs*; Snake acc 0.953 ECE 0.034 *theirs*; Qwen3-0.6B ≠ Archer; /v1/systemone wire-compat ≠ logit-equiv; TianyuCodings/NanoJev densify HEAD 76fdfc9ecdca README SHA a8f8afeb7e44 was 618cea6d / 4190093c64ee; Add JevHarness project link to READMEs; densify §115 not a sibling first sighting; SHA move is not a replica; jjd-lab/jev-synthetic-survey MIT HEAD 9ca8c4ab94bb README SHA ec1664288d50; How you ask mattered more; Noul TVD 0.1530 vs GPT 0.1789 *theirs*; ECE 0.1472 *theirs* not Harbor; missed 0.05 bar; 67.28% vs 64.78% *theirs*; $4.02 vs ~$136 *theirs*; independent work; CankatSarac/jev-arcade MIT HEAD b2e45ed3c1c6 README SHA 1f06af0f4c74; snake 70/80 *theirs*; tetris 167 vs heuristic 2333 *theirs*; 74% conf <0.5 *theirs*; Calibration is not yet measured; three seeds not Harbor; game success ≠ calibrated Noul; sszxt/rlcd HEAD 66ca01664d6b README SHA 3da08d46758d; ECE 0.490→0.423 Brier 0.487→0.409 *theirs*; Yang 2023 contrastive ≠ TypeSafe RLCD; Qwen2.5 ≠ Archer; still overconfident; hf:AXERA-TECH/Laya sha 51a586cd14e2 apache; AX650 NPU 69.991/27.722/69.990 ms *theirs*; seq 256 up to 4 options; serving substrate ≠ calibrated replica; base convaiinnovations/laya; hf:openjev/openjev-MLX-4bit sha c59bf1eed7d8 cc-by-nc-4.0; ~15 GB 4-bit affine; independent not affiliated; hf:openjev/openjev-MLX-4bit ≠ razorback16/openjev; hf:GeekyAbs/laya sha b65d05b4d9eb; GeekyAbs/laya ≠ convaiinnovations/laya; hf:alfred361/laya-web sha 33f171161da5; 100% argmax *theirs*; multilingual-int8 93.8% / worst shift 16.9 pts *theirs*; 50bbx/laya-needle Apache HEAD 01961bade52f README SHA ecaff4dfd271; threshold 0.58 still soft; local Laya ≠ hosted Jev; yunhai-dev/laya2typesafeapi HEAD 4aeb89be286b README SHA d2e5d114fcd8; TypeSafe-compatible ≠ TypeSafe replica; iamdgarcia/openJev MIT HEAD 62bbc30eece2 README SHA 55614ad8caab; independent educational; not local inference; iamdgarcia/openJev ≠ alongL/openJev ≠ Zefan-Cai/Open-Jev; chrisns/homebrew-laya-mac-serve MIT HEAD 1b3c4c0bdb70 README SHA 5e58082b7e9b; tap for chrisns/laya-mac-serve §139; serving substrate ≠ calibrated replica; nk412/judgements MIT HEAD 6624e53c86cc README SHA 86fe465f7887; pydantic wrapper; threshold 0.5 still soft; JingHao-Leon/awesome-jev-apps MIT HEAD d3ef0254c4b2 README SHA fd38a3c4ff2e; catalog ≠ endorsement; JingHao-Leon/awesome-jev-apps ≠ heyjunpenn/awesome-jev; Manta-Boardgame/jev-chat HEAD 44721bae8c2e README SHA 03272e4b9a9f; unofficial; 98% confidence *theirs*; ximing/jev-snake-game HEAD 1e80283f458e README SHA 0a54b74eb095; 用 TypeSafe Jev 驱动的自动贪吃蛇; hf:dataset:syvai/danish-dynaword-laya gated HTTP 401; size_categories 10K<n<100K; devbackend/jevgo ≠ kisshan13/typesafe-ai-go ≠ peach-zhang/typesafe-go; qiudingkai-crypto/jevai and Strernd/beer-jev share README SHA e215bc4ccf13 template collision; skip-thin Adrian-lzr/jev-spire-brain Dililianxice/jev-robotic-arm-benchmark baltzparra/jev-study lzero07/jev-laya-statement qq150078158-lab/TDM-demo empty SHA; Awesomejev 691→802 (+111) / 38194→52151 stars quote watch not re-derive; tracker likes 81 lastModified UNCHANGED; Softmax over options ≠ calibrated Noul; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63; notes.md §140

## Hourly 0348 HIGH (`notes.md` §139)

open-cricket BYOM / wire-compat ≠ logit-equiv. Qwen2.5 ≠ Archer.
Greedy 0.90 vs Oracle 0.82 *theirs*. confidence ≠ P(correct).
seed 42 n=1 is not Harbor. 8,400 calls $0.39 *theirs*.
Noul 0.7 true 44% *theirs*. JevBench 81.65 *theirs* not Harbor.
0-byte Mandelbrot is not a replica. training not complete.
Compose meaning like state. A clean report is not proof.
does not sandbox. serving substrate ≠ calibrated replica.
catalog ≠ endorsement. *theirs* not Harbor.
Do not copy keys. Fresh PR off `04c8a44` (merged #62).
Do not reopen or amend PR #23–#62. Does not bump 0.5.0. Skip Archer.
`invented_signal: false`.

Hourly 0248 uniqueness lock: hf:knowledgator/gliclass-instruct-large-v1.0 43 likes sha 825e5478c1bf apache-2.0; Efficient zero-shot and few-shot multi-task model via sequence classification; GLiClass knowledgator Hub family class-peer catalog not Jev equivalent; Knowledgator/GLiClass.c already §123; Hub models first card as class-peer entries; GLiNER/GLiClass ports are class members not Jev replicas; hf:space:mayafree/typed-decision-leaderboard 33 likes sha f4fc44077818; typed-decision-leaderboard *theirs* not Harbor; JEV 0.7350 ZTC 27B 0.7289 ZTC 397B 0.7272 *theirs* not Harbor; 2,018 items same labels; three-way tie; tacticocc/Jevbridge 33★ MIT HEAD da443ea453ac README SHA 2178333c4c3b; Jevbridge ACP and MCP adapter; does not generate text; Any LLM as System One; wire-compat ≠ logit-equiv; tshmieldev/sharp 29★ MIT HEAD 17cbd8d9cc9e README SHA 783a5cde519c; Cut the slop; Filter your X timeline; kavehmz/typesafe-playground 11★ HEAD 733991a2924a README SHA 04c0b1f6e7da; real API calls not polished benchmarks; himomohi/aside-jev 7★ MIT HEAD e570db43b0e1 README SHA 288e7c91c307; Jev picks the next action from your defined candidates; Not a Cua binding; Jev is the model Aside is the browser runtime; nico-martin/open-jev 6★ MIT HEAD 52667199e8a5 README SHA 81c0485d5833; open reproductions of the shape; Nothing is generated; nico-martin/open-jev ≠ razorback16/openjev ≠ Zefan-Cai/Open-Jev ≠ meijustory123/openjev; hf:chaoliangUNSW/Jev-Style-Qwen3.5-2B-Decision-GGUF 82.3% ECE 0.017 *theirs*; Same decision as bf16 94.4% *theirs*; Qwen3.5-2B ≠ Archer; serving substrate ≠ calibrated replica; hf:pngwn/nanodiff-350m-typed-decisions ECE 0.065 → 0.036 *theirs*; hf:litert-community/laya-LiteRT 144/144 *theirs*; gargpratyush/journey-evals A page that says Success is never accepted as proof; mpnikhil/dev-0.4b Banking77 91.33% BoolQ 85.20% *theirs*; encoder class member not Jev replica; n4ze3m/typed-decisions-synth 7,414 cases 25,859 questions; Nobody checked it; Zaious/jev-capability-atlas already carded; LocalLLaMA/typed-decisions already carded; fengyiqicoder/jevfeed already carded; Zhao-Tian-yi/awesome-jev ≠ Gerry9000/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev; kaustav1996/reflex ≠ vuckuola619/reflex; tphakala/jev-mcp ≠ jkudish/jev-mcp; ninthspace/hunch ≠ carldaws/hunch ≠ tpellet/hunch; ruban-24/switchboard ≠ cannacre8ive/switchboard-ai; hf:openjev/openjev ≠ razorback16/openjev; catalog ≠ endorsement; skip-thin Fibonaccirabbit/Jev-VLN imanshu03/jev-browser-use luca-saggese/laya.c empty SHA; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61; notes.md §138
Hourly 0348 uniqueness lock: JonathanHHenson/open-cricket MIT HEAD d75af22125ed README SHA 7d288a741089; Local structured decisions using causal language models; default Qwen/Qwen2.5-1.5B-Instruct; independent of TypeSafe; API follows Jev's general call shapes but model predictions and confidence calibration differ; wire-compat ≠ logit-equiv; Qwen2.5 ≠ Archer; replica ≠ TypeSafe; virtualman333/jev-decision-arena MIT HEAD cf6ae4ed31e8 README SHA 037f75d9610d; Greedy 0.90 vs Oracle 0.82 *theirs*; Random conf 0.00 still 20.5% *theirs*; ECE 0.180 / 0.106 / 0.205 *theirs*; confidence ≠ P(correct); game success ≠ calibrated Noul; seed 42 n=1 is not Harbor; dopeCape/typesafe-ai-test HEAD ed2adb7740d7 README SHA 183f91c36471; 8,400 calls $0.39 *theirs*; Noul 0.7 true 44% *theirs*; ≥0.9 conf 91.7% AG News *theirs*; versioned model ids rejected; *theirs* not Harbor; pCwOrM/werr 2★ MIT HEAD 2526cae98891 README SHA b29476734a09; JevBench 81.65 *theirs* not Harbor; WindTunnel 49/49 *theirs* not Harbor; 0-byte Mandelbrot is not a replica; meijustory123/OpenJev-Kit HEAD c53125982f80 README SHA a4e72c61a973; training not complete; no accuracy; Qwen3.5-0.8B ≠ Archer; meijustory123/OpenJev-Kit IS meijustory123/openjev (same GitHub id 1379187719); meijustory123/OpenJev-Kit ≠ Zefan-Cai/Open-Jev; microchipgnu/jev-hooks HEAD cbf40e64d7b2 README SHA af25fb0aaf70; Compose meaning like state; rashedInt32/jury.nvim 1★ MIT HEAD bf31e9509e7e README SHA a2b088dd0787; Code enumerates the candidates; evoke-build/evoke 1★ Apache-2.0 HEAD 310840b56f1d README SHA 02b91962cef4; Jev is the first classifier the design is bound to none; moritzkremb/jev-voice-browser densify HEAD 198a0764395a README SHA 816309fc22e6 was fa033303; context is the conversation so far; densify §82 not a sibling first sighting; luantak/is-malicious densify 18★ MIT HEAD faf6ba61d7e1 README SHA 4ae098b4b7ae; A clean report is not proof; does not sandbox; skillseedorg/ChatJEVs MIT HEAD 346e7347cf90 README SHA 6ff81d54040f; ChatJEVs ≠ erik-dunteman/ChatJev; generation from Choice is not a language model replica; chrisns/laya-mac-serve MIT HEAD f294500821b6 README SHA 00e39a7d04e2; serving substrate ≠ calibrated replica; rimusz/localjev-mlx HEAD 297836a0d95e README SHA 2d96d20e0b80; rimusz/localjev-mlx ≠ githubnext/localjev; luhayes/jev-agent-router 1★ MIT HEAD bba795a4dc4e README SHA 17a2f44993d1; does not execute; cutoff 0.8 still soft; gbesse/decision-workbench MIT HEAD 8889cf3750a3 README SHA 14a3bf79da7a; demo scores are not accuracy measurements; zhuyansen/x-reply-filter already carded; kylemclaren/jev-search ≠ kazuhideoki/jev-search; xinwang-nwpu/jev-mobile ≠ Friedjof/jev-mobile; kcd-dev/jev-skill ≠ raphael-liu/jev-skill; yanmad27/ask-jev ≠ kuhung/ask-jev; hf:s1lv3rj1nx/openjev-router-healthcare encoder class member not Jev replica; hf:akhilaaa3/openjev-v1-40705-nimble-r512-merged ≠ hf:akhilaaa3/openjev-v1-allmix-r512-merged; jevai spaces catalog ≠ endorsement; skip-thin Fibonaccirabbit/Jev-GalGame MadhavBahl/jev-guide advance-lion/dsh-jev-hooks amithgc/local-jev hiro1202/jev-review-gate-poc inlight37-design/decision-model_lab kuhung/ask-jev mmiguez314/jev-lab pomodorozhong/exp-jev vanthiet1/JevGuarAgent empty SHA; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62; notes.md §139
Hourly 0445 uniqueness lock: lucasmartins-ai/lcc 7★ MIT HEAD a7e86fb60997 README SHA 877831764be9; keeps essentially every block 0.0%/−0.5% *theirs*; mechanical −70.0% Jev −52.1% *theirs*; mock Laya = Jev −22.6% on XL withdrawn; Token reduction alone is not cost reduction; N=18 pilot not Harbor; David-Lolly/Jev-Compatible 3★ HEAD e52e963d8539 README SHA 6e5ff22d40a6; Chat 1282.3 ms vs gateway 232.1 ms ~1/5.5 *theirs*; 3/3 n=3; Softmax over candidate logprobs; Qwen3.8-27B ≠ Archer; wire-compat ≠ logit-equiv; hwfengcs/any2jev 2★ Apache-2.0 HEAD 719b0eb9eefe README SHA 27e0af212cd5; independent not affiliated; acc 0.796 ECE 0.027 *theirs*; 42 ms vs JSON 778 ms *theirs*; Snake acc 0.953 ECE 0.034 *theirs*; Qwen3-0.6B ≠ Archer; /v1/systemone wire-compat ≠ logit-equiv; TianyuCodings/NanoJev densify HEAD 76fdfc9ecdca README SHA a8f8afeb7e44 was 618cea6d / 4190093c64ee; Add JevHarness project link to READMEs; densify §115 not a sibling first sighting; SHA move is not a replica; jjd-lab/jev-synthetic-survey MIT HEAD 9ca8c4ab94bb README SHA ec1664288d50; How you ask mattered more; Noul TVD 0.1530 vs GPT 0.1789 *theirs*; ECE 0.1472 *theirs* not Harbor; missed 0.05 bar; 67.28% vs 64.78% *theirs*; $4.02 vs ~$136 *theirs*; independent work; CankatSarac/jev-arcade MIT HEAD b2e45ed3c1c6 README SHA 1f06af0f4c74; snake 70/80 *theirs*; tetris 167 vs heuristic 2333 *theirs*; 74% conf <0.5 *theirs*; Calibration is not yet measured; three seeds not Harbor; game success ≠ calibrated Noul; sszxt/rlcd HEAD 66ca01664d6b README SHA 3da08d46758d; ECE 0.490→0.423 Brier 0.487→0.409 *theirs*; Yang 2023 contrastive ≠ TypeSafe RLCD; Qwen2.5 ≠ Archer; still overconfident; hf:AXERA-TECH/Laya sha 51a586cd14e2 apache; AX650 NPU 69.991/27.722/69.990 ms *theirs*; seq 256 up to 4 options; serving substrate ≠ calibrated replica; base convaiinnovations/laya; hf:openjev/openjev-MLX-4bit sha c59bf1eed7d8 cc-by-nc-4.0; ~15 GB 4-bit affine; independent not affiliated; hf:openjev/openjev-MLX-4bit ≠ razorback16/openjev; hf:GeekyAbs/laya sha b65d05b4d9eb; GeekyAbs/laya ≠ convaiinnovations/laya; hf:alfred361/laya-web sha 33f171161da5; 100% argmax *theirs*; multilingual-int8 93.8% / worst shift 16.9 pts *theirs*; 50bbx/laya-needle Apache HEAD 01961bade52f README SHA ecaff4dfd271; threshold 0.58 still soft; local Laya ≠ hosted Jev; yunhai-dev/laya2typesafeapi HEAD 4aeb89be286b README SHA d2e5d114fcd8; TypeSafe-compatible ≠ TypeSafe replica; iamdgarcia/openJev MIT HEAD 62bbc30eece2 README SHA 55614ad8caab; independent educational; not local inference; iamdgarcia/openJev ≠ alongL/openJev ≠ Zefan-Cai/Open-Jev; chrisns/homebrew-laya-mac-serve MIT HEAD 1b3c4c0bdb70 README SHA 5e58082b7e9b; tap for chrisns/laya-mac-serve §139; serving substrate ≠ calibrated replica; nk412/judgements MIT HEAD 6624e53c86cc README SHA 86fe465f7887; pydantic wrapper; threshold 0.5 still soft; JingHao-Leon/awesome-jev-apps MIT HEAD d3ef0254c4b2 README SHA fd38a3c4ff2e; catalog ≠ endorsement; JingHao-Leon/awesome-jev-apps ≠ heyjunpenn/awesome-jev; Manta-Boardgame/jev-chat HEAD 44721bae8c2e README SHA 03272e4b9a9f; unofficial; 98% confidence *theirs*; ximing/jev-snake-game HEAD 1e80283f458e README SHA 0a54b74eb095; 用 TypeSafe Jev 驱动的自动贪吃蛇; hf:dataset:syvai/danish-dynaword-laya gated HTTP 401; size_categories 10K<n<100K; devbackend/jevgo ≠ kisshan13/typesafe-ai-go ≠ peach-zhang/typesafe-go; qiudingkai-crypto/jevai and Strernd/beer-jev share README SHA e215bc4ccf13 template collision; skip-thin Adrian-lzr/jev-spire-brain Dililianxice/jev-robotic-arm-benchmark baltzparra/jev-study lzero07/jev-laya-statement qq150078158-lab/TDM-demo empty SHA; Awesomejev 691→802 (+111) / 38194→52151 stars quote watch not re-derive; tracker likes 81 lastModified UNCHANGED; Softmax over options ≠ calibrated Noul; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63; notes.md §140

User-provided glance uniqueness lock: yoheinakajima/glance Apache-2.0 Py HEAD 8f36e063bffb README SHA b57280394bc1 LICENSE SHA d645695673349e; 4★; 1 fork; star-noise is not the fold; size 51490; pushed 2026-09-21T17:37:40Z; created 2026-09-21T06:51:38Z; PyPI glance-vlm 0.3.1; tag v0.3.1; site https://glance.yohei.me; topics calibration, image-classification, vision-language-model, vlm, zero-shot; Ask an open vision-language model typed questions about an image and get probabilities back, on your own machine; frozen open VLM default Qwen3-VL-4B Apache-2.0; yes/no pick-one and default unfitted rating read from answer-token logits in one forward pass; default unfitted rating is jsondigits (1 pass, exact 0.669); labeled glance fit uses ens4d (4 passes); four-pass zero-shot rating 0.570 behind write JSON 0.672; glance fit --unlabeled uses jsondigits; fast2 (2 passes) and digits (1 pass) remain available; Glance is a calibration and measurement harness around that readout. It is not a model; trains no weights; images never leave the machine; local server binds 127.0.0.1; noul yes/no choice pick-one score ordered rating; POST /v1/decide; zero-shot table only yes/no 0.939 pick-one 0.933 rating exact 0.669 *theirs*; Gemini 3.1 Flash-Lite yes/no 0.961 pick-one 0.933 rating 0.763 *theirs*; fitted readout marked fitted do not say zero-shot or no training: unlabeled image-quality 0.67 to 0.76 exact (README; CLAIMS one-pass 0.758 at 16 unlabeled images) *theirs*; labeled about 32 images 0.86 exact ECE about 0.03 per rubric does not transfer *theirs*; Glance is not an image-quality metric; on KADID-10k it misses their own targets; do not quote interim KADID numbers; Q-SiT-mini 0.9B trained for image quality is level under the same 32-label fit; hand-built features beat it on low-level artifacts when labels are plentiful; non-image-quality rubrics 0.55 exact with 300 labels *theirs*; tilt 0.33 *theirs*; geometric probes diagonals 0.30 largest of four shapes 0.52 eight objects 0.56 *theirs*; stripe direction hidden-state linear probe 0.99 *theirs*; raw yes/no ECE 0.111 and 0.179 *theirs*; pooled two-number Platt map on those suites ECE 0.061 and 0.053 *theirs*; transfer to a new yes/no task untested; glance fit is a per-rubric rating map not that Platt map; explicit other held-out breeds 7.7% *theirs*; claims ledger: faster or cheaper than Jev do not claim; shares inference object with featherless-ai/simple-jev hr98w/jev-visual zhengxuyu/litjev; request and response shapes follow TypeSafe Jev hosted text; yoheinakajima/glance ≠ TypeSafe Jev; POST /v1/decide ≠ TypeSafe /v1/systemone ≠ IamBusy/OpenJev /v1/decide is a wire lock not OpenJev v2 identity; OpenJev v2 is Hub AlexWortega/openjev trained 4B multimodal claim scorer census §77 do not mint a sibling card; OpenJev v2 ≠ Zefan-Cai/Open-Jev ≠ razorback16/openjev ≠ IamBusy/OpenJev-Vision; Zefan-Cai/Open-Jev §125 is a separate trained-head namesake; trains no weights unlike YOFO and unlike hf:thaitea/laya-vision §146 and unlike OpenJev v2 and unlike IamBusy/OpenJev-Vision; harness not weights; soft probs for threshold abstain rank; soft scores ≠ hard gates; logits are not calibrated probabilities of correctness; *theirs* not Harbor; catalog ≠ endorsement; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70/#71/#72; notes.md §147

## Hourly 1256 (notes.md §150)

Decision-model class fold. TypeSafe Jev (Choice, Score, Noul) is the dominant exemplar, named early, and not the whole mandate. A typed client is not a replica. Soft judgment is not a sole veto. schema-valid is not the same as correct. game success ≠ calibrated Noul. routing ≠ permission. densify §48 and §134, not sibling first sightings. Merged #74 owns §148. Merged #76 owns §149. This fold is §150.

Hourly 1256 uniqueness lock: AboveColin/jevclient 2★ MIT Py HEAD a225eadd6eb0 README SHA 5e102cbaa555; typed client is not a replica; wire-compat ≠ logit-equiv; revsmoke/promptrejectormcp 2★ ISC TS HEAD 752217d26fe9 README SHA dab9c144b5f2; screen is a sensor; application must act; soft judgment is not a sole veto; GodModeAI2025/JevCoreML 0★ Apache-2.0 Swift HEAD cb5c261a1412 README SHA f61f018eee8f; CoreML serving substrate ≠ calibrated replica; kev ≠ TypeSafe; Neoo-Blue/vibecheck 0★ Kotlin HEAD cfd6c46899f8 README SHA 718ab09e0442; Jev never writes the reply; RavenValentin/TypeSafe.Jev 0★ MIT C# HEAD 5868475507e5 README SHA 6a4cf10feb67; unofficial .NET client; pin jev-1.13.0; adorosario/jev-rag-claim-verification 0★ MIT Py HEAD 2bdb4d9f3935 README SHA 9b6547d48a39; Jev 1.13.0 balanced acc 73.3 CI [68.5, 77.9] false-verification 23.2% *theirs*; Astra task-optimised 73.8 *theirs*; difference -0.6 points; 187× *theirs* not Harbor; bytelabs-oss/clash-jev 1★ MIT Py HEAD 04d420669966 README SHA 31f93aa3c8d7; no trained policy; fallback never logged as Jev; game success ≠ calibrated Noul; krisitown/jev-router HEAD e2809e09f497 README SHA fa27068d3876; routing ≠ permission; allebee/jevgrep revisit 0★ MIT Py HEAD 5cebf4c046ac README SHA e30654352e5f; first card revisit tag no prior notes card; default threshold 0.5 still soft; meaning-grep is not a gate; allebee/jevgrep ≠ Bentlybro/jevgrep ≠ nassim-arifette/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; harlanljones/jev-roster-shapes densify HEAD 1d94f9e07fe8 README SHA 4653c58a6459; missing data stays missing; geometry never creates value; 8.8 ms is UI latency not a Jev bench; densify §134 not a sibling first sighting; ktaletsk/jevframe densify HEAD 16bd3eae69b7 README SHA 6e0a9ef1ba79; no result thresholded or silently renormalized; densify §48 not a sibling first sighting; hfnissum-byte/Hunkpick 77% *theirs* not Harbor; code enumerates model picks code gates; breejesh/gen1 schema-valid is not the same as correct; 100% schema is not calibrated Noul; hf:Cruzex/laya-typed-decisions-smoketest smoke accuracy 0.460 *theirs* not Harbor; reference 0.727 is not comparable; hf:abidlabs/jev-typed-decisions-causal-0.6b quick_eval acc 0.6234 NLL 1.2755 n=640 *theirs*; unre-run report 0.7518 ECE 0.0154 was not re-run; hf:s1lv3rj1nx/openjev-general-lora Banking77 0.728 vs TypeSafe Jev 0.820 *theirs*; hf:libingzheren/Jev-Mem 0.777 LLM-as-a-Judge *theirs* not Harbor; LLM-as-a-Judge ≠ gold; not the §134 11.0% figure; smartaces/jev-plays-streetfighter-2 6★ text state not video; catalog ≠ endorsement; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70/#71/#72/#73/#74; notes.md §150
