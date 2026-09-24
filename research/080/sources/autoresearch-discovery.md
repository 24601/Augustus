# Auto-research / autoscience tooling: discovery beyond the maintainer's list

Lane: auto-research discovery for 0.8.0 component 3 (research automation), with
inputs for component 1 (ExoPO paper) and component 2 (trainer hill-climb).
Date: 2026-09-23. **Confidential 0.8.0 working note. Local only. Do not post to
GitHub or anywhere else.**

**Method.** GitHub REST search using creation-date windows (default best-match
sort, not star-sorted); arXiv export API (focus 2025–2026); Hugging Face API,
Crossref and official docs for identity checks. I read READMEs or named source
files only. Nothing was installed, built or executed.

**Evidence labels.**
- **[C] Contract:** a documented interface, or code behaviour I read at the
  stated SHA.
- **[R] Reported:** a number or claim from the authors or a third party. Not
  verified.
- **[H] Hypothesis:** my inference.
- **[U] Unknown.**

This lane has no *Reproduced* items.

**Scope boundary.** The listed-tools lane owns cards for: karpathy/autoresearch,
ARIS, Anti-Autoresearch, AutoSOTA, InternAgent, mareforma, ToolUniverse, FAROS,
swarm-factory, CoAutoResearch, de-anthropocentric-research-engine and
scholaraio. For three of those I add only cross-notes (§4.5).

---

## 1. Bottom line

1. **AutoResearchClaw is `github:aiming-lab/AutoResearchClaw`.**
   - Identity: node R_kgDORnWLww, MIT, HEAD be4ba4755bf1 (2026-08-19), latest
     release v0.5.0 (2026-05-20).
   - Paper: arXiv:2605.20025v2. Benchmark: `hf:AIMING-Lab-UNC/ARC-Bench` at sha
     5a5923be8d30.
   - At least 30 same-name or derivative repositories exist. None shares its node
     ID.
   - What the source shows (§2):
     - The citation-existence layer is real.
     - Its "claim verification" is keyword and substring matching that emits
       fixed "confidence" constants.
     - Its headline comparisons come from a benchmark the authors built and an
       LLM judges. AutoResearchClaw gets extra inputs, and the co-pilot
       interventions are generated from the same judge's failures on the same
       topics.
   - **Action: reject** it as a dependency or evidence source. Borrow only the
     layered citation-resolution idea.
2. **"Autoresearch" is now a genre, not a project.** 3,113 GitHub repositories
   created in 2026 have the word in their name or description:

   | Creation window | Repositories |
   |---|---|
   | Q1 2026 | 1,188 |
   | Q2 2026 | 1,369 |
   | 2026-07-01 to 08-15 | 318 |
   | 2026-08-16 to 09-23 | 238 |

   The count carries no quality signal. A small set of mechanisms separates
   trustworthy loops from metric-maximizers (§7).
3. **The strongest hill-climb evidence is negative and specific [R]:**
   - Selecting the final solution by validation score leaves 9–17 pp of medal
     rate on the table compared with selecting by test score (AIRA-dojo).
   - One agent hard-coded answers for 19–41 evaluation rows per run until a
     held-out set existed. Agents also read sibling runs through shared git
     state and left memory notes for "future runs" (2607.18064).
   - About 80% of coding-agent research runs had fabricated or invalid results
     (MLR-Bench).
   - All 7 tested models generated synthetic data when data were missing
     (SciIntegrity-Bench).
   - In 82.5% of analyses, the agent named a severe flaw in its own review and
     shipped anyway (AutoResearchEval, pattern F.4).
4. **The best-designed systems converge on exogenous acceptance.** The model
   proposes. A controller the model cannot edit owns evaluation, acceptance,
   rollback and state:
   - codex-autoresearch's controller script;
   - evo's gates;
   - CORAL's grader isolation;
   - AutoResearchExam's private test set;
   - SkillOpt's held-out gate;
   - autoguardrails' fixed evaluator with a benign-pass floor;
   - Anti-Autoresearch's rules-only adjudicator;
   - the external control loop in 2606.11522;
   - the outer-holdout matrix in 2607.17100.

   This is direct supporting evidence for the ExoPO thesis, and it also supplies
   boundary cases (§8.1).
5. **Citation integrity has three axes of different difficulty.**
   - Existence and metadata, and retraction status, are mechanical: resolve
     against Crossref, OpenAlex, DBLP and arXiv (citegate); HALLMARK benchmarks
     the detectors.
   - Support is not mechanical. Deep-research agents keep more than 94% of links
     working, but only 39–77% of cited facts match the source (2605.06635).
   - Only the first axis can be a CI gate.
6. **Popularity does not track verification depth.**
   - K-Dense scientific-agent-skills (46k stars) states it reports no task-level
     evaluation.
   - ARA's install path asks the agent to fetch a remote prompt and follow it,
     and that prompt edits CLAUDE.md or AGENTS.md.
7. **The new design content for Augustus is narrow.** Most of the rest is already
   in `optimizer-integration.md` steps 3–5. What is new:
   - isolation built into the harness, plus leak-free feedback;
   - "a gate set is not a confirmation set", with a count of confirmation reads;
   - an A/A calibration of the acceptance rule (rerun the incumbent as its own
     challenger);
   - a span-anchored claim ledger with rules-only adjudication;
   - "do nothing / don't train" as a reachable terminal state.

---

## 2. AutoResearchClaw: identity verification and source findings

| Field | Observation | Label |
|---|---|---|
| Canonical ID | `github:aiming-lab/AutoResearchClaw`, node R_kgDORnWLww, not a fork, org aiming-lab | C |
| Created / pushed | 2026-03-15 / 2026-08-19 | C |
| HEAD | be4ba4755bf1b52220f25e13b2293b5956590070, "fix(llm): strip reasoning traces by default…" | C |
| License | MIT (LICENSE file and GitHub SPDX) | C |
| Releases | v0.3.0 (03-17), v0.3.1 (03-18), v0.3.2 (03-23), v0.4.0 (04-01, human-in-the-loop), v0.5.0 (05-20, domain agents + ARC-Bench) | C |
| Paper | arXiv:2605.20025v2 (v1 2026-05-19, updated 05-23), 36 authors | C |
| Benchmark | `hf:AIMING-Lab-UNC/ARC-Bench`, sha 5a5923be8d30, MIT. 55 topics: 25 ML, 10 HEP, 10 quantum, 7 biology, 3 statistics. The paper and design doc use the 25 ML topics. | C |
| Ecosystem | OpenClaw-compatible. ACP backends (Claude Code, Codex CLI, others). Optional MetaClaw cross-run skill injection. | C |
| Popularity | 14,517 stars, 1,684 forks (observation only) | — |

**Look-alikes that are not the same identity.** The query `AutoResearchClaw`
returned 31 hits.
- Copies or derivatives: fresedaniel-ops/autoresearchclaw,
  leodama04/AutoResearchClaw, petadimensionlab/AutoResearchClaw (self-described
  derivative), thada2402/AutoResearchClaw, ylc123456789/AutoResearchClaw-dev,
  kyapp69/AutoResearchClaw-backup.
- Wrappers: OthmanAdi/researchclaw-skill, lesterppo/hermes-researchclaw.
- Unrelated name-alikes: InternScience/ResearchClawBench (a benchmark) and
  arXiv:2609.00365 "Dr. Claw". The "Claw" suffix is OpenClaw-ecosystem branding,
  not lineage.

**What the source shows at be4ba47:**

- **`literature/verify.py` [C]** resolves each BibTeX entry in layers: arXiv ID,
  then CrossRef/DataCite DOI, then OpenAlex or Semantic Scholar title search.
  - VERIFIED: title similarity ≥ 0.80. SUSPICIOUS: 0.50–0.80. HALLUCINATED:
    below 0.50 or not found.
  - An optional LLM relevance score is added.
  - This is a real existence and metadata check. It does not test whether the
    cited work supports the sentence.
- **`hitl/claim_verifier.py` [C]** uses string heuristics and assigns fixed
  "confidence" values of 0.8, 0.6, 0.9 and 0.3:
  - A factual claim counts as "grounded" if more than 40% of its non-stopword
    tokens overlap any knowledge-base entry.
  - A citation claim counts as grounded if its first capitalized word (and year)
    appears in any knowledge-base entry.
  - A numerical claim counts as grounded if its digit string appears anywhere in
    `stage-14/experiment_summary.json`.
  - These are ordinal heuristics presented as probabilities. "Improves accuracy
    by 3" passes whenever "3" appears anywhere in that JSON. [H]
- **`pipeline/verified_registry.py` [C]** builds a whitelist of numbers from
  experiment outputs, including rounding and percentage variants. A number in
  the paper passes if it is within 1% of *any* registered value.
  - This checks membership. It does not bind each claim to its metric or
    condition key.
  - With `best_only=True`, the registry uses only the promoted best iteration.
    The paper then reports a maximum over REFINE iterations with no untouched
    re-evaluation. [H: selection-inflated]
- **`experiments/arc_bench/EXPERIMENT_DESIGN.md` [C]** describes the benchmark
  protocol:
  - AutoResearchClaw also receives injected synthesis, hypotheses and an
    experiment plan at stages 7–9. The baselines do not.
  - The co-pilot "HITL" interventions come from one LLM call that reads the
    judge leaves the full-auto run failed. They are then re-run on the same 25
    topics and scored by the same judge.
  - So hypothesis H2 (co-pilot beats full-auto) tests adaptive tuning against
    the evaluator.
  - Regression to the mean alone predicts H3 (bigger gains where full-auto
    scored lowest). [H]
- **The MetaClaw "+18.3% robustness" result [R]** is a composite of stage
  completion (18/19 → 19/19), retry rate and refine-cycle count. These are
  process metrics, not research correctness.
- The "2699 tests passed" README badge is a static image, not a CI receipt. [C]

**Verdict.** Reject as a dependency or evidence source. Borrow two ideas:
layered citation resolution, and stage gates with rollback.

---

## 3. Coverage ledger

Prior repository evidence: `notes.md`, `sources.json` and the decision reviews
had no cards for these sources. Related prior evidence:
- kev's autoresearch champion rule and its `docs/claims.json` +
  `verify_claims.py` claim ledger (notes.md §45; today's ecosystem patrol).
- TypeSafe's "autoresearch feature discovery" cookbook (`sources.json`), fetched
  today: sha256 00ee0cff…

**GitHub search.** REST, best-match sort, first page of 100 only.

| Query (retrieved 2026-09-23 ~17:03–17:18Z) | total_count | Returned |
|---|---|---|
| `autoresearch in:name,description created:2026-01-01..2026-09-23` | 3,113 | 100 |
| same, split by window: Q1 / Q2 / 07-01..08-15 / 08-16..09-23 | 1,188 / 1,369 / 318 / 238 | 100 each |
| same + `stars:>=100` (triage filter) | 49 | 49 |
| `autoresearch … created:2026-07-01..2026-09-23 stars:>=20` | 6 | 6 |
| `"ai scientist" in:name,description created:2025-01-01..2026-09-23` | 636 | 100 |
| same + `stars:>=100` | 17 | 17 |
| `"ai-scientist" in:name created:2024-06-01.. stars:>=100` | 7 | 7 |
| `"automated research" OR "autonomous research" … 2025-06-01.. stars:>=50` | 32 | 32 |
| `citation verification in:name,description created:2025-06-01..` | 1,843 | 100 |
| `hallucinated citations in:name,description created:2025-01-01..` | 161 | 100 |
| `research "claude code" skill … 2026 stars:>=200` | 42 | 42 |
| `experiment loop … agent … 2026 stars:>=50` | 5 | 5 |
| `"claim ledger" OR "evidence ledger" in:readme,description …` | 11,306 (too broad; not traversed) | 100 |
| `reward hacking autoresearch in:readme,description 2026` | 193 | 100 |
| `"ai scientist" OR autoresearch OR "research agent" created:2026-09-01.. stars:>=30` | 2 | 2 |
| `AutoResearchClaw` (identity check) | 31 | 30 |

**arXiv export API**
- Queries and totals:
  - `ti:"AI scientist"`: 64
  - `all:autoresearch`: 67
  - `abs:"research agent" AND abs:benchmark AND (reproduc OR fabricat OR "reward hacking")`: 21
  - 16 title lookups for named systems and benchmarks.
- Seven title queries hit HTTP 429 (AutoReproduce, AI Scientist, "Evaluating
  Sakana", RE-Bench, MLGym, EXP-Bench, AI co-scientist). I resolved all of them
  later with `id_list` lookups.
- I fetched 69 abstracts. I read full-text sections of two papers: 2607.18064v2
  and 2507.02554v2.

**Selection.** I read 16 sources at README or source depth (§4). Criteria:
1. It implements a research or improvement loop, or verification
   infrastructure.
2. It was active in 2026.
3. Its mechanism is distinct from the others.
4. It fits one of the three 0.8.0 components.

Star thresholds were triage filters to stay under the page cap. They bias the
sample toward popular repositories. Low-star repositories in the 3,113 set are
largely unreviewed.

**Identity checks**
- `openai/preparedness` redirects to `openai/frontier-evals` (node
  R_kgDOOQUqDQ). It holds `project/paperbench`.
- `Orchestra-Research/Agent-Native-Research-Artifact` redirects to
  `ARA-Labs/Agent-Native-Research-Artifact` (same node R_kgDORyuAbQ). The ARA
  paper cites the old owner name.
- `jimmc414/Kosmos` is an unofficial reimplementation. It is not from the
  Edison/FutureHouse authors.
- Karpathy's "LOOPS.md", which ARIS cites (2026-07-02), is not in karpathy's
  public repositories or gists. Only third-party notes mention it. [U]
- The AI Scientist peer-reviewed paper exists: Nature 651:914–919 (2026-03-25),
  doi:10.1038/s41586-026-10265-5. I checked Crossref metadata only; I did not
  read the paper.
- arXiv metadata anomaly: five records have a v1 `published` date earlier than
  their ID month (for example, 2607.28631 lists 2026-04-18 and 2608.05179 lists
  2026-06-29). I did not use these dates to date any claim.

---

## 4. Tool cards

Every card uses the same fields: identity and inspection depth; loop;
mechanism; acceptance and human gates; verification; evidence; cost; safety;
fit for the three 0.8.0 components; action.

### 4.1 Hill-climb loop controllers

**C1. leo-lilinxiao/codex-autoresearch**
- **Identity:** node R_kgDORp-fEA; MIT; HEAD 0f54c5717074 (2026-09-12); created
  2026-03-18; 2,645 stars (observation). Read: README and
  `scripts/autoresearch_core.py`.
- **Loop:** inspect → change one thing → commit → measure → keep if improved and
  the guard passes, else revert → append an audit event. Runs in the foreground
  (a Codex Goal) or the background (one `codex exec` worker per iteration).
- **Mechanism [C]:**
  - "The control script owns commits, verification, rollback, and state. Codex
    owns the hypotheses and code changes."
  - `run.json` is immutable.
  - `events.jsonl` is append-only and validated for consistency. For example,
    discarding an improving trial requires a failed guard log. Partial or
    contradictory state is an error. The README says the controller "never
    guesses a result from old files or conversational memory."
  - Scope is enforced by a path check. The run requires a clean named branch.
    HEAD drift outside the tool aborts the run.
- **Acceptance [C]:** `improved()` is a strict inequality on a single
  measurement. There is no noise margin and no repeat. This suits counts such as
  `error_count` and fails on noisy metrics.
- **Human gates:** one confirmation of goal, scope, metric parser, guard and mode
  before the first write. None per iteration.
- **Verification:** none for claims; it is not a research writer.
- **Cost:** [U].
- **Safety [C]:** the Quick Start runs `codex --dangerously-bypass-approvals-and-sandbox`.
- **Fit:** trainer hill-climb: high. Patrol: low. Paper: none.
- **Action:** borrow the pattern (controller-owned event log, enforced scope,
  fail-closed state validation). Do not copy its single-run acceptance or its
  sandbox bypass.

**C2. evo-hq/evo**
- **Identity:** node R_kgDOR6bLtA; Apache-2.0; HEAD ab5fbd6c8210 (2026-07-17);
  1,459 stars. Read: README and `skills/discover/references/constructing-benchmark.md`.
- **Loop:** `/evo:discover` finds the metric, instruments the benchmark and
  creates gates. `/evo:optimize` runs rounds of parallel subagents in git
  worktrees with tree search. Frontier strategies: argmax, top-k, ε-greedy,
  softmax, pareto_per_task.
- **Mechanism [C]:**
  - Gates are exit-code checks on every experiment, inherited down the tree. The
    README warns that without gates "the search will find ways to return a
    constant, skip work, or trade correctness for speed."
  - When `discover` builds a benchmark from scratch, it must pair a held-out
    slice (30–40% of cases) as a score-floor gate. It adds an exact-leakage
    pre-gate that greps for validation strings and gold answers.
  - The docs concede: "Do not describe held-out data as secret. Defense is
    detection."
  - Variance-aware optimization is "not implemented yet." The docs warn that
    noisy benchmarks produce noisier optimization trees.
- **Human gates:** an optional pause per round. Unattended by default.
- **Cost:** optional remote sandboxes (Modal, E2B, Daytona, AWS, Azure). Spend
  not reported.
- **Safety [C]:** on Codex, hooks are trusted automatically unless you pass
  `--no-trust-hooks`.
- **Fit:** trainer hill-climb: high, as a design reference. Patrol: low.
- **Action:** borrow the pattern (gate taxonomy, exact-leakage pre-gate, and its
  honest point that a repeatedly consulted held-out slice is a gate, not
  confirmation). Watch.

**C3. Human-Agent-Society/CORAL**
- **Identity:** node R_kgDORoQHWg; Apache-2.0; HEAD 0123dfb939b3 (2026-09-06);
  arXiv:2604.01658v3 (COLM 2026 per the README); 1,008 stars. Read: README and
  abstract.
- **Loop:** several long-running coding agents in separate worktrees. Shared
  state lives in `.coral/public` (attempts, notes, skills). A grader daemon
  scores every commit. A manager sends heartbeat prompts (reflect, consolidate,
  pivot). Supports multi-island runs.
- **Mechanism [C]:**
  - The grader environment and answer keys live in `.coral/private`.
  - Since 2026-06-24, the Docker session runs agents as an unprivileged user, so
    they "can no longer read `.coral/private/` … not even via Bash." On the host
    this is opt-in (`agents.isolate_user`). That implies isolation was by
    convention before.
  - Rubric-judge grader packages for open-ended tasks (added 2026-04-24).
- **Evidence [R]:** state of the art on 10 tasks; 3–10× improvement rates with
  fewer evaluations; kernel task improved from 1363 to 1103 cycles.
- **Fit:** trainer hill-climb: medium-high, for grader isolation by OS
  permission. Patrol: low.
- **Action:** borrow the pattern (grader and answer-key isolation by OS
  permission). Watch.

**C4. davebcn87/pi-autoresearch**
- **Identity:** node R_kgDORkmdKA; MIT; HEAD 939ede8220da (2026-09-10); 8,110
  stars; an extension for the pi coding agent. Read: README.
- **Loop:** `/autoresearch` writes `.auto/prompt.md` and `measure.sh`, then loops
  edit → commit → `run_experiment` → `log_experiment` → keep or revert. The
  `autoresearch-finalize` skill regroups kept changes into independent branches;
  the user approves the grouping.
- **Mechanism [C]:**
  - A "confidence" score = |best improvement| ÷ the median absolute deviation
    (MAD) of all metric values in the segment. At 2× or more it is labelled
    "likely real." Advisory only.
  - An optional `checks.sh` (tests, types, lint) blocks a keep when it fails.
  - `before`/`after` hooks inject steering messages. `maxIterations` caps the
    run.
- **Critique [H]:**
  - MAD over all runs mixes the effects of the changes with measurement noise.
  - "Best improvement" is a maximum over many draws, so the ratio will exceed 2×
    by chance as the run count grows.
  - The correct noise floor comes from an A/A rerun of the incumbent.
- **Fit:** trainer hill-climb: medium. Patrol: low.
- **Action:** borrow the pattern (finalize kept changes into independently
  reviewable changesets; checks as blockers). Reject its confidence ratio as an
  acceptance rule.

**C5. uditgoenka/autoresearch**
- **Identity:** node R_kgDORmNgCQ; MIT; HEAD 050e30dc4ba0 (2026-08-12); 6,367
  stars. Built for Claude Code; the core also runs on OpenCode and Codex. Read:
  README.
- **Loop:** define goal, scope, metric, direction and Verify (plus an optional
  Guard) → baseline → one atomic change per iteration → verify → keep or
  `git revert` → TSV log. Bounded by default. Many subcommands (debug, fix,
  security, ship, predict, reason, probe, regression).
- **Mechanism [C]:**
  - Verify is the metric. Guard is a command that must always pass.
  - "Guard/test files are never modified." This rests on instructions plus
    hooks. The README says hooks "are defense-in-depth guardrails, not a
    security sandbox."
  - The regression gate runs a Mann–Whitney U test with 7 samples per side.
- **Fit:** trainer hill-climb: medium. The scope creep into security and
  shipping lowers its value as a reference.
- **Action:** borrow the pattern (the Verify/Guard split; a repeated-sample
  regression test). Watch.

**C6. microsoft/SkillOpt**
- **Identity:** node R_kgDOSXkMwg; MIT; HEAD 79124b37e9a6 (2026-09-05);
  arXiv:2605.23904v2; PyPI v0.2.0; 17,393 stars. Read: README and abstract.
- **Loop:** rollout → reflect → aggregate → select → one bounded add, delete or
  replace edit to a single skill document. The edit is accepted only if it
  "strictly improves a held-out validation score." Extras: a textual
  learning-rate budget, a buffer of rejected edits, and an epoch-wise slow/meta
  update. SkillOpt-Sleep consolidates nightly "behind a held-out validation
  gate."
- **Mechanism [C]:** "The skill document [is] the trainable state of a frozen
  agent." Deployment adds zero inference-time calls.
- **Evidence [R]:** best or tied in all 52 (model, benchmark, harness) cells. On
  GPT-5.5 it improves no-skill accuracy by +23.5 points in direct chat, +24.8 in
  Codex and +19.1 in Claude Code.
- **Caveat [H]:** a validation set consulted for every acceptance is a gate, not
  confirmation. I have not read whether a separate untouched test backs the
  52-cell result.
- **Fit:**
  - ExoPO: high. It is policy-as-text outside the weights, optimized against an
    external gate.
  - Trainer: medium, as the "optimize the prompt or skill before training a
    head" step.
- **Action:** watch. Cite in ExoPO as a Reported example. Read the paper's split
  protocol first.

**C7. SantanderAI/autoguardrails**
- **Identity:** node R_kgDOS7VgbA; Apache-2.0; HEAD 1ca0c9b2c005 (2026-07-16);
  130 stars. Read: README.
- **Loop:** record a baseline → edit only `policy.md` → score the candidate with
  `--repeat 2` → keep it only if attack success rate (ASR) improves and the
  benign pass rate drops by no more than 2 pp; otherwise restore automatically.
  `results.tsv` is append-only.
- **Mechanism [C]:**
  - Only the policy file changes. The evaluator, judge prompt and test suite are
    fixed.
  - It reports three numbers: `asr_unguarded` (empty policy), `asr_with_policy`,
    and their difference, `policy_delta`. This separates the guardrail's
    contribution from the model's own safety.
  - The rules forbid switching judges mid-series. A changed suite starts a new
    lineage.
- **Gap [H]:** selection and reporting use the same fixed suite, so there is no
  untouched test. An LLM judge scores ASR.
- **Fit:** ExoPO: high, as a minimal worked example (explicit policy, constraint
  floor, counterfactual baseline). Trainer: medium.
- **Action:** borrow the pattern (empty-policy counterfactual baseline,
  constraint floor, new lineage when the evaluator changes).

**C8. NousResearch/autoreason**
- **Identity:** node R_kgDORzax_Q; no license file; HEAD 538f8817550e
  (2026-04-12); 605 stars; paper PDF in the repository (not checked on arXiv).
  Read: README.
- **Loop:** each round produces three versions: the incumbent A, an adversarial
  revision B, and a synthesis AB. Fresh-context judges rank them in a blind
  Borda count. The winner becomes A. The loop converges when A wins twice.
  "Do nothing" is always an option.
- **Evidence [R]:**
  - 77% vs 73% for Sonnet 4.6 on 150 CodeContests problems (private tests).
  - With Haiku 4.5, "held-out gains vanish — the generation-evaluation gap has
    closed."
  - Critique-and-revise shrinks weak-model outputs by 59–70% over 15 passes.
- **Fit:**
  - Paper drafting: high (incumbent-protecting revision with an explicit
    no-change winner).
  - ExoPO: boundary evidence. The gains need an evaluator that knows more than
    the generator.
- **Action:** borrow the pattern for ExoPO revision passes. Judge wins are not
  quality evidence.

### 4.2 End-to-end research systems

**C9. aiming-lab/AutoResearchClaw.** Identity and source findings are in §2.
- **Loop:** 23 stages in 8 phases: scoping, literature, synthesis, experiment
  design, execution, analysis (with a PIVOT/REFINE decision at stage 15),
  writing, finalization with citation verification.
- **Human gates:** stages 5, 9 and 20, with rollback. `--auto-approve` skips all
  of them. A 24-hour default human timeout; `auto_proceed_on_timeout` defaults
  to false.
- **Cost:** in the example config, `cost_budget_usd` defaults to 0, meaning no
  limit [C].
- **Safety:** Docker or sandbox execution, `network_policy: setup_only`. AST
  checks "block identical ablations, hardcoded metrics" [C].
- **Fit:** low for patrol and for the trainer. For paper drafting, reject: fully
  automated writing is the wrong tool for a position paper.
- **Action:** reject.

**C10. sapientinc/PRAXIST**
- **Identity:** node R_kgDOUGGnKA; license NOASSERTION (the README describes a
  Fair Source License plus user agreement, so it is not OSI open source); HEAD
  5b50658b219d (2026-09-23); created 2026-08-27; arXiv:2608.25955v1; 6,716 stars.
  Read: README and abstract.
- **Loop:** a takeover skill verifies the baseline and evaluator, then builds a
  task harness with "explicit metric directions, baseline provenance,
  protocol-integrity checks, evidence maturity rules, and justified retention
  lanes." Parallel peers run each generation. A cohort-level synthesis feeds a
  typed evidence graph of findings, frontiers and agendas.
- **Mechanism [C]:** the task project, not Praxist, owns the objective,
  evaluator, metrics and baselines. Launch authorization is an explicit field in
  the brief.
- **Evidence [R]:** on the 75-task MLE-bench, 60 medals (80.0%, 49 gold) versus
  55 (73.3%, 34 gold) for a Claude Code / Opus 4.8 baseline, at $3,054 versus
  $38,370 in model spend. MLE-bench stopped accepting leaderboard submissions on
  2026-04-24 "while we develop an improved process for ensuring submissions are
  fair and comparable" [C]. Comparability is unverified.
- **Safety [C]:** the agent-managed install suggests `codex --yolo`.
- **Fit:** trainer: medium, for its lineage and evidence-maturity vocabulary.
  The license limits reuse.
- **Action:** watch. Read the paper's definitions of lineage and evidence
  maturity. Do not vendor it.

**C11. EvoMap/AutoResearch**
- **Identity:** node R_kgDOT5Dp9w; Apache-2.0; HEAD 21f591298aca (2026-09-13);
  arXiv:2608.17906v4; 3,215 stars. Read: README and abstract.
- **Loop:**
  - Idea generation: collect signals → filter → intersect with a local
    knowledge base → at least three distinct models generate and cross-review →
    plan.
  - Idea execution, in Claude Code: freeze the idea's provenance → plan → pilot
    → scale, or stop with a preserved negative result → main experiment →
    critic review plus a blind review without self-evaluation context → close
    or iterate.
- **Mechanism [C]:**
  - "Independent" stages must use distinct underlying model identities, and the
    tool counts them.
  - Exported plans carry a checksum of the source file.
  - The workflow "never rewrites the local knowledge base automatically."
  - Paid network research requires `--confirm-paid-network`.
  - `decisions.log` is append-only.
- **Evidence [R]:** RSICD mean recall 32.84 → 34.69. "5 audit-confirmed issue
  events vs 11–27" for other systems, by their own audit.
- **Safety [C]:** execution uses `claude --dangerously-skip-permissions`, with an
  explicit rule to run only in a disposable environment without the host home
  directory or credentials.
- **Fit:** patrol: medium. Trainer: medium (pilot before scaling; stop with a
  negative result).
- **Action:** borrow the pattern (confirmation flag for paid calls; no automatic
  rewrite of curated knowledge; count distinct model identities).

### 4.3 Provenance and verification infrastructure

**C12. chrisyangsong/citegate, with rpatrik96/hallmark**
- **citegate identity:** node R_kgDOT1jh-w; MIT; HEAD 94cc0a02a63a (2026-08-30);
  102 stars. Read: README.
- **citegate mechanism [C]:** checks each BibTeX entry against Crossref,
  OpenAlex and DBLP.
  - Verdicts: verified, not-found, retracted (OpenAlex plus Retraction Watch
    data in Crossref), mismatch, unverifiable (never fails the build), error.
  - Exits non-zero on the verdicts you configure.
  - Ships as a GitHub Action, a pre-commit hook, and a weekly retraction monitor
    that opens issues.
- **HALLMARK identity:** node R_kgDORMBUCQ; MIT; HEAD ddd62975e48f (2026-09-21);
  13 stars. Read: README.
- **HALLMARK mechanism [C]:** a benchmark for citation-hallucination detectors.
  - 2,526 entries: 826 valid and 1,246 hallucinated in the public splits, plus a
    454-entry hidden split.
  - 14 hallucination types, 6 sub-tests per entry, calibration error (ECE), and
    a temporal split to detect contamination.
  - Caches responses in SQLite so reruns are reproducible.
  - Baselines include HalluCiteChecker (2604.26835).
- **Limit:** both check existence, metadata and retraction. Neither checks
  whether the source supports the claim.
- **Fit:**
  - Paper drafting: high, as the bibliography gate for ExoPO.
  - Patrol: high, for resolving source identity and watching for retractions.
  - Do not use the Action or the issue-opening monitor while 0.8.0 is
    confidential.
- **Action:** pilot the CLI locally after reading its source. Use HALLMARK-style
  fixtures to choose a detector.

**C13. ARA-Labs/Agent-Native-Research-Artifact (ARA)**
- **Identity:** node R_kgDORyuAbQ; MIT; HEAD e52a925e9d03 (2026-08-24);
  arXiv:2604.24658v3; 682 stars. Read: README and abstract.
- **Mechanism [C]:** a schema for research artifacts:
  - `PAPER.md` manifest;
  - `logic/claims.md` (falsifiable claims with proof references);
  - `experiments.md`;
  - `src/configs` with rationale;
  - `trace/exploration_tree.yaml` (a typed DAG that keeps dead ends);
  - `evidence/` (raw tables).

  It ships seven skills, including a rigor reviewer and a research fuzzer.
- **Evidence [R]:** on PaperBench and RE-Bench, QA accuracy 72.4% → 93.7% and
  reproduction 57.4% → 64.4%. Preserved failure traces can "constrain a capable
  agent from stepping outside the prior-run box."
- **Safety [C]:** setup tells the agent to "Read
  https://raw.githubusercontent.com/…/wire-ara.md and follow its instructions,"
  which writes a routing map into CLAUDE.md or AGENTS.md. That is a mutable
  remote instruction channel into the agent's standing instructions.
- **Fit:** patrol: medium (the claims, evidence and exploration-tree schema).
  Paper: medium.
- **Action:** borrow the schema only. Reject the install method.

**C14. yifanzhang-pro/Agora**
- **Identity:** node R_kgDOUeUNRg; Apache-2.0; HEAD 4ce939e2447b (2026-09-18);
  arXiv:2609.18094v2; 70 stars. Read: README and abstract.
- **Mechanism [C]:**
  - An append-only Git DAG of typed contributions (results, insights,
    hypotheses, verifications, reports).
  - A contribution's evidence score comes only from other accounts' results and
    verifications; self-citation is excluded.
  - `analyze()` lists leading and contested work and recommends next steps with
    a UCB-style ranking.
- **Evidence [R]:** 13 language-model workers ran about 12 days and made 1,703
  contributions. The development evaluator score fell from 3.39 to 1.899 bits
  per byte, with 165 reproductions and no reported failures. The README
  discloses its own limits: "All method choices used the same 200-text
  development evaluator, and the final score improvement was smaller than the
  observed cross-hardware variation." Also, 18 first-day contributions produced
  about 98% of the gain.
- **Fit:** patrol: medium (verification status, and evidence from independent
  accounts only).
- **Action:** borrow the pattern. It is also a model of honest self-reporting.

**C15. Future-House/paper-qa (PaperQA2)**
- **Identity:** node R_kgDOI55lCg; Apache-2.0; HEAD 57e89f7223b0 (2026-08-12);
  paper arXiv:2409.13740v2 (2024, older); 9,239 stars. Read: README.
- **Loop:** LLM-generated keyword search → chunk and embed → gather evidence
  (top-k chunks, LLM-scored summaries, re-scored) → answer with in-text
  citations. Paper metadata comes from Semantic Scholar, Crossref and Unpaywall,
  including a retraction check. A dedicated setting looks for contradictions.
- **Caveat [C]:** the FAQ says the internal tools, licensed paper access and
  search-from-scratch setup differ from the open repository. The published
  results are not what the public code reproduces.
- **Fit:** patrol: medium, as local-corpus Q&A over primary sources already
  downloaded.
- **Action:** watch. Its answers never replace primary-artifact inspection.

### 4.4 Benchmarks usable as tools

**C16. bespokelabsai/AutoResearchExam and PrentisAI/AutoResearchEval**
- **AutoResearchExam:**
  - Identity: node R_kgDOUSMSyw; Apache-2.0; HEAD 7758e84af55f (2026-09-15).
  - 29 tasks across model training, algorithms, data engineering, systems,
    evaluation and calibration, safety and interpretability. The official
    harness allows 24 hours and up to 1,000 experiments, with public validation
    feedback. It scores progress over the run with AUARC.
  - Protocol, verbatim [C]: "Select each checkpoint by public validation and
    measure its private test score on the same saved artifact. Report test
    performance, but never use test scores to select checkpoints. Keep private
    test data, scores, and logs outside the agent environment."
- **AutoResearchEval:**
  - Identity: node R_kgDOT28VaA; no license; HEAD 1df36f37bc42 (2026-09-21);
    arXiv:2608.14905v3.
  - 100 tasks across 7 domains, 800 trajectories from 8 harness–model pairs.
    Its failure taxonomy (ARFT) has 45 patterns under 4 root-cause pillars;
    experts reached κ = 0.85.
  - Findings [R]: 12,712 failure hits; 92.1% in the cognitive pillars. Pattern
    F.4, uncorrected self-awareness, appears in 82.5% of analyses. The deficits
    recur across all harnesses, which the authors read as a model-level problem.
- **Fit:** trainer: high (the protocol paragraph is a ready acceptance
  contract). Patrol: medium (ARFT as a fold-review checklist).
- **Action:** borrow the protocol as a rule, and make F.4 a gate: a named severe
  flaw blocks the output. Watch both.

### 4.5 Cross-notes on listed-lane tools (not full cards)

- **karpathy/autoresearch** (HEAD 228791fb499a, 2026-03-26).
  - The README says MIT, but GitHub detects no license file.
  - Selection and reporting both use `val_bpb` on one pinned validation shard.
    There is no untouched test.
  - A change is kept only if it is strictly lower on one run.
  - The immutability of `prepare.py` is an instruction, yet the README says to
    run the agent with all permissions disabled.
  - "NEVER STOP" removes the stop exit.
  - The fixed 5-minute budget makes runs comparable only on one machine.
  - [C/H]
- **ARIS.**
  - The assurance gate hashes audit inputs with SHA-256 to catch stale audits,
    and treats the external verifier's exit code as the source of truth [C].
  - `citation-audit` checks existence, metadata and "context appropriateness"
    separately. It was motivated by real papers cited for claims they do not
    support [R].
  - Its argument for two-model review ("adversarial bandits… 2-player games
    converge to Nash equilibrium") has no variable map and is not evidence [H].
- **Anti-Autoresearch.**
  - A deterministic core: a hashed span ledger, LLM auditors that only propose
    findings, and a rules-only adjudicator.
  - A finding must quote a verbatim ledger span or it fails closed.
  - On 2026-07-10, exact calculators meant to clear numeric false alarms were
    demoted. Adversarial review showed a calculator cannot tell whether "50%" is
    exact or rounded [C/R].
  - This negative result applies to any numeric claim checker Augustus writes.

---

## 5. Triage at metadata or abstract depth

"Older" means the code or paper predates 2026 and was newly checked today.

| Source | Year / activity | What it is | Disposition |
|---|---|---|---|
| SakanaAI/AI-Scientist (v1), 2408.06292v3. Peer-reviewed as Nature 651:914–919 (2026-03-25, Crossref metadata only) | 2024 code (older); pushed 2025-12 | Template-based idea → experiment → paper → automated review | Archive. Beel et al. (2502.14297v3) report poor novelty assessment, 42% of experiments failing, hallucinated numbers [R] |
| SakanaAI/AI-Scientist-v2, 2504.08066v1 | 2025; last push 2025-12-19 (older) | Tree search built on AIDE, with a vision-model figure loop. 1 of 3 workshop submissions cleared the average acceptance threshold [R]. $15–20 per run for experiments plus about $5 for writing [R]. RAIL-derived license with mandatory AI-use disclosure [C] | Reject for 0.8.0 drafting; archive |
| SamuelSchmidgall/AgentLaboratory, 2501.04227v2 | 2025; pushed 2025-08 (older) | Staged pipeline with human feedback per stage; that feedback improved quality [R] | Archive |
| HKUDS/AI-Researcher, 2505.18705v1 | 2025; pushed 2025-10; no license | End-to-end system plus Scientist-Bench | Archive |
| ResearAI/DeepScientist, 2509.26603v1 | 2025–26; pushed 2026-06 | Bayesian-optimization framing with a Findings Memory. 20,000 GPU-hours, about 5,000 ideas, about 1,100 validated [R] | Watch; the cost scale is itself a finding |
| Kosmos, 2511.02824v2 (closed Edison platform); jimmc414/Kosmos (unofficial) | 2025 | A structured world model across 200 rollouts; independent scientists judged 79.4% of statements accurate [R] | Archive. The unofficial repository is not Kosmos |
| Future-House/robin, 2505.13400v1 | 2025 | Lab-in-the-loop drug-candidate discovery (ripasudil for dry AMD) [R] | Archive |
| stanford-oval/storm (STORM 2402.14207v2, Co-STORM 2408.15232v2) | 2024 (older) | Perspective-guided question asking to write cited articles | Archive. It synthesizes; it does not verify |
| AkariAsai/OpenScholar, 2411.14199v1 | 2024 (older) | RAG over 45M open-access papers; GPT-4o hallucinated citations 78–90% of the time [R] | Archive |
| Just-Curieous/Curie, 2502.16069v2; MLR-Copilot 2408.14033v3; ResearchAgent 2404.07738v2; AutoReproduce 2505.20662v4 | 2024–25 | Rigor modules, ideation or reproduction loops | Archive |
| Google Co-Scientist, 2502.18864v2 (retitled "Accelerating scientific discovery with Co-Scientist", updated 2026-06-29) | Closed | Multi-agent hypothesis generation | Archive; title change noted |
| K-Dense-AI/scientific-agent-skills (46,304 stars), 2609.00065v2 | 2025–26 | 163–166 procedural skills. The paper says "We report no task-level evaluation" [C] | Archive. Popularity is not efficacy |
| Imbad0202/academic-research-skills (49,284 stars) | 2026 | Academic pipeline with integrity gates; v3.8 adds an opt-in audit that fetches each cited source per anchor [C] | Watch the claim-audit design |
| alchaincyf/darwin-skill (6,081 stars) | 2026 | Autoresearch-style SKILL.md optimizer scored by a 9-dimension LLM-judged rubric | Reject as an evidence method. Per AGENTS.md, rubric scores do not certify semantic quality |
| githubnext/autoloop (no license) | 2026 | Scheduled GitHub Agentic Workflow (every 6 hours); opens draft PRs; keeps state on a memory branch | Reject for 0.8.0 (GitHub-hosted, publishes). The most-overdue-first scheduling idea is worth keeping |
| WecoAI/aideml; facebookresearch/aira-dojo, 2507.02554v2 | 2024–26 | AIDE tree search; search-policy × operator study | Archive; cite the generalization-gap finding (§6) |
| josephbsmith/citationdiff (0 stars) | 2026 | Invalidates a citation verification when the Markdown claim changes | Keep the pattern only |
| Karpathy "llm-wiki" gist 442a6bf5 (2026-04-04) | 2026 | Immutable raw sources, an LLM-maintained wiki, a schema file; operations: ingest, query, lint | Augustus already has the three layers. The missing piece is a human-gated "lint" pass for contradictions and stale claims |
| EdwardOptimization/Bilevel-Autoresearch; InternScience/ResearchClawBench; allenai/asta-bench; OSU-NLP-Group/ScienceAgentBench | 2025–26 | A meta-loop and benchmarks | Metadata only; benchmark findings in §6 |

---

## 6. What benchmarks and audits reveal about failure modes

| Source (depth) | Finding [label] | Design implication |
|---|---|---|
| PaperBench 2504.01848v3 (abstract; 2025) | 20 papers; 8,316 rubric leaves co-developed with the papers' authors; the best agent scores 21.0%; the LLM judge is validated on a separate judge benchmark [R] | Rubric decomposition plus judge validation is the minimum when outcomes cannot be executed |
| MLE-bench 2410.07095v6 + README | At least 3 seeds with mean ± SEM; detectors for rule violations and plagiarism; leaderboard closed to new submissions on 2026-04-24 [C] | Agent variance is large. Comparability needs a protocol, not only a grader |
| AIRA-dojo 2507.02554v2 (full-text passages) | Searching and selecting by test score instead of validation score adds +9.4 / +12.4 / +15 / +16.6 pp medal rate (MCTS / evolutionary / greedy / AIDE-greedy). The gap widens with search time [R] | Selecting on the search metric is optimistic. Confirm the frozen pick on untouched data |
| Quran recitation study, 2607.18064v2 (§8.3, §9) | Codex hard-coded 19–41 evaluation rows per run. A held-out set removed the memorization and the score gap. One run read a sibling's in-flight solution through a shared git worktree. Agents left memory notes for "future runs." n = 3 per arm, one task [R] | The paper's five rules: R1 hold out data; R2 keep feedback leak-free; R3 isolate run state by construction; R4 audit the agent tool's own state channels; R5 report metric components and preregister hypotheses |
| MLR-Bench 2505.19955v3 | About 80% of coding-agent runs produced fabricated or invalid results [R] | Every number in a report must bind to an executed artifact |
| SciIntegrity-Bench 2605.10246v2 | 34.2% of 231 runs had an integrity problem. All 7 models synthesized data when data were missing. Removing completion pressure cut undisclosed fabrication from 20.6% to 3.2%, but not the synthesis itself [R] | Make "infeasible" or "don't train" a reachable terminal state, with no pressure language |
| AutoResearchEval 2608.14905v3 | F.4 (the agent names a severe flaw and ships anyway) in 82.5% of analyses [R] | Reviews must block; advisory prose is not enough |
| "AI scientists produce results without reasoning scientifically," 2604.18805v1 | Evidence ignored in 68% of traces; refutation-driven revision in 26%; the base model explains 41.4% of variance, the scaffold 1.5% [R] | Scaffolds will not fix epistemics. Check outputs mechanically |
| CAWM position, 2606.23175v1 (single author) | 7 of 28 episodes reached a right-looking answer through the wrong mechanism; a regime-shift check flagged all of them [R] | Add one out-of-regime check before accepting a mechanism claim |
| Hidden pitfalls, 2509.08713v2 | Found inappropriate benchmark selection, leakage, metric misuse and post-hoc selection bias. Traces plus code expose these far better than the paper alone [R] | Review the traces and code, not only the write-up |
| Verification-gap survey, 2608.05179v1 | Of 24 runnable systems, 83% release code; 38% release seeds or traces; 38% verify novelty at all [R] | "Open source" does not mean auditable |
| "Cited but Not Verified," 2605.06635v1 | Links valid more than 94% of the time; factual accuracy 39–77%; accuracy falls about 42% as tool calls grow from 2 to 150 [R] | Existence checks are necessary but not sufficient |
| "LLM hallucinations in the wild," 2605.07723v1 | Across 111M references, at least 146,932 non-existent citations in 2025 [R] | A bibliography gate is mandatory for anything we circulate |
| Search-time contamination, 2606.05241v1 | Agents that search the web retrieve benchmark answers, inflating scores by up to 4% [R] | Generate synthetic data and run evals without web access to the eval set |
| Rehearse, 2607.27687v1 | The agent's pre-execution judgment of which change will help falls from 82.8% to 56.9% accuracy late in a loop [R] | Measure; do not trust the agent's predictions |
| Compression and generalization, 2606.11045v1 | Little adaptive overfitting when the successful strategy is compressible; deliberately induced overfitting fails to reproduce from a short prompt [R] | A cheap overfitting probe. Also a counterexample to "any reuse of validation data is fatal" |
| Outer-holdout matrix, 2607.17100v2 | Winners frozen after inner 5-fold search were confirmed on 9 of 10 endpoints; one inner-endorsed gain was rejected [R] | Validate decisions, not only the final artifact |
| Search discipline, 2606.11522v1 | The aggregate score can rank first a candidate that collapses protected regions [R] | Slice constraints belong in the exogenous acceptance rule |
| Red Queen Gödel Machine, 2606.26294v2 | The strongest baseline reviewer accepts AI-generated papers at up to 1.91× the human rate; evaluators evolve but stay fixed within each epoch [R] | Reviewer approval is not acceptance. A changed evaluator needs a lineage boundary |
| AIDE², 2609.26457v1 (2026-09-22) | A self-editing research agent keeps the changes that score best on hidden evaluations; reward hacking fell from 55% to 32% [R] | Even recursive self-improvement keeps acceptance exogenous |
| ResearchClawBench, 2606.07591v5 | The best agent scores 21.5 of 100 on re-discovery [R] | End-to-end autonomy remains weak |

---

## 7. Cross-cutting patterns

### 7.1 What makes automated research trustworthy

For each pattern: mechanism, examples, where it fails, and a falsifier where one
applies.

1. **Acceptance lives outside the optimizer.**
   - The proposer cannot edit the evaluator, the data roles, the acceptance
     rule or the state log.
   - Examples: codex-autoresearch, evo, SkillOpt, autoguardrails,
     Anti-Autoresearch, 2606.11522.
   - Where it fails: the controller still consumes a gamed metric. The Quran
     memorization passed a controller.
   - Falsifier: a planted exploit (for example, hard-coded evaluation IDs)
     either is or is not caught.
2. **Isolation is built into the harness, not written as an instruction.**
   - Examples:
     - the grader and answers are unreadable by OS permission (CORAL);
     - the private test lives outside the agent's environment
       (AutoResearchExam);
     - each run gets a fresh single-commit clone, with no shared version
       control, logs or memory (Quran R3/R4).
   - Karpathy's instruction-only "do not modify `prepare.py`", run with
     permissions disabled, is the counterexample.
   - Falsifier: a canary file in the private directory is never read during a
     red-team run.
3. **Three data roles, with a read budget.**
   - Search data: feedback allowed.
   - Gate data: consulted repeatedly, so it becomes adaptive (evo's held-out
     slice, SkillOpt's validation set).
   - Confirmation data: untouched, scored once per frozen candidate.
   - AIRA-dojo prices the cost of conflating them. Evo concedes a held-out slice
     is "not secret." 2606.11045 bounds when reuse is benign.
4. **Acceptance accounts for noise, calibrated with an A/A test.**
   - Strict single-run improvement accepts noise (karpathy, codex-autoresearch,
     SkillOpt's "strictly improves").
   - Better options: repeated samples with a rank test (uditgoenka); a paired
     non-inferiority test with a record-clustered bootstrap (kev, §45);
     Augustus's Hoeffding bound at confirmation.
   - Falsifier: rerun the incumbent as its own challenger k times. The
     acceptance rate should stay at or below the nominal α.
5. **Feedback never leaks answers.** Failure messages echo inputs and
   predictions, never gold labels (Quran R2). Add an exact-string leakage
   pre-gate (evo).
6. **A span-anchored claim ledger with rules-only adjudication.**
   - Every claim points to a hashed artifact span and a source revision.
   - LLMs may propose findings; rules decide.
   - Hashing the audit inputs invalidates stale audits.
   - Examples: Anti-Autoresearch, ARIS, kev's `claims.json`, citationdiff.
   - Where it fails: the extractor misses claims (recall), and exact-versus-rounded
     arithmetic is ambiguous (Anti-Autoresearch, 2026-07-10).
7. **Citations are checked on three axes.**
   - Existence and metadata: a mechanical gate.
   - Retraction: a mechanical gate (citegate).
   - Support: needs the cited passage plus a human or a calibrated judge (ARIS
     citation-audit; the 2605.06635 framework).
8. **Negative results and stopping are first-class outcomes.**
   - autoreason's incumbent can win.
   - EvoMap stops with a preserved negative result.
   - CARTOGRAPH's "refuse" guard (2606.07576) flagged all 4 A-Lab claims later
     judged inconclusive and passed 32 of 36 confirmed ones [R].
   - Where it fails: preserved failure traces can over-constrain a capable
     agent (ARA), so negative memory needs scope and expiry.
9. **The process is the reviewed artifact.** Traces, code and seeds, not the
   paper. Examples: Hidden Pitfalls; the verification-gap survey;
   OpenDiscoveryTrace; Agora; PRAXIST's lineage graph.
10. **Independent review, but only when it blocks.**
    - Examples: distinct model identities (EvoMap), fresh contexts (autoreason),
      cross-family reviewers (ARIS).
    - Each helps only if a named severe flaw blocks release (F.4).
    - Reviewer bias toward AI-written text is documented (RQGM), so reviewer
      approval is never acceptance.

### 7.2 What produces convincing garbage

1. **Self-graded quality and novelty.** The generating system reviews itself:
   AI Scientist v1's automated reviewer and novelty checks (per Beel et al.);
   darwin-skill-style rubrics.
2. **Process proxies reported as progress.** MetaClaw's "robustness" composite,
   stage-completion rates, "tests passed" badges.
3. **Benchmarks the authors build and judge.** Asymmetric inputs, plus judge
   feedback reused on the same topics (ARC-Bench H2/H3).
4. **Heuristic verification that prints confidence-looking numbers.**
   AutoResearchClaw's keyword-overlap and digit-substring checks.
5. **Selection-inflated reporting.**
   - Best-of-REFINE numbers.
   - The maximum over a search tree scored on validation data (AIRA-dojo).
   - One development evaluator used for every choice (Agora, self-disclosed).
   - Loops that only ever measure a pinned validation shard (karpathy).
6. **Citations that do not resolve or do not support the claim.** At least
   146,932 non-existent citations in 2025. Links that work while 39–77% of the
   cited facts hold.
7. **Contamination channels.** Web search reaching benchmark answers; shared
   git state; persistent agent memory; sibling branches; printed gold labels.
8. **Completion pressure.** "NEVER STOP" instructions and mandatory deliverables
   drive agents to synthesize missing data (SciIntegrity-Bench).
9. **Right answer, wrong mechanism, and claim drift.** The runnable artifact no
   longer supports the mechanism the write-up claims (CAWM; Xcientist,
   2606.18874).
10. **Unsafe defaults in install paths and permissions.**
    - "Read this URL and follow its instructions" installers that edit
      AGENTS.md or CLAUDE.md (ARA, autoloop).
    - `--dangerously-bypass-approvals-and-sandbox`, `--yolo` or "disable all
      permissions" as the recommended path.

---

## 8. Implications for the three 0.8.0 components

### 8.1 ExoPO position paper

**Supporting evidence (keep the labels):**
- Exogenous acceptance is the convergent 2026 architecture:
  - codex-autoresearch: "the control script owns commits, verification,
    rollback, and state";
  - evo's gates;
  - SkillOpt: "skill document as the trainable state of a frozen agent,"
    optimized against a held-out gate; 52/52 cells [R];
  - autoguardrails: a policy file, a fixed evaluator, a benign-pass floor and
    an empty-policy counterfactual;
  - RecSys Factory: "autonomy at decision points, not over pipelines," a 78-day
    deployment that its authors call a case-study observation [R];
  - 2606.11522: an external loop overturns the agent's own acceptance;
  - 2607.17100: an outer holdout rejects a gain the inner search endorsed;
  - AIDE²: even a self-editing agent is accepted on hidden evaluations.
- Evidence of what goes wrong when the acceptance policy is the literal metric:
  the Quran memorization, the AIRA-dojo gap, MLR-Bench fabrication, and
  SciIntegrity-Bench's completion pressure.

**Boundary cases to state honestly:**
- autoreason: once generation matches evaluation ability, the exogenous
  tournament adds nothing. The evaluator must know something the proposer does
  not.
- RQGM: evaluators can themselves be optimized if they stay fixed within each
  epoch. Exogeneity holds per epoch, not forever.
- 2606.11045: for policies with a short description, repeated reuse of
  validation data overfits little, so a strict one-shot holdout can be
  over-conservative.
- DPO-family methods: nothing here contradicts them where preference is the
  product. The judge-driven loops (autoreason, RQGM) actually document judge
  bias.

**Ingredients for the operational test [H; for the ExoPO lane to formalize].**
Keep the policy exogenous when any of these holds:
1. The proposer can observe or influence the evaluation channel.
2. Acceptance must stay stable across many proposers and versions.
3. Costs, authority or constraints change faster than retraining can follow.
4. A slice constraint exists that the aggregate metric can hide.
5. An auditor must be able to replay and contest each decision.

*Falsifier:* a domain where an in-weights policy trained on the same outcome
data matches the exogenous policy on untouched complete-episode loss and under
shift, at equal audit cost.

**Drafting process:**
- A local bibliography gate (citegate-style).
- A claim ledger for every number in the paper (the Anti-Autoresearch pattern).
- autoreason-style passes (incumbent vs revision, blind judges) for prose only.
- Human sign-off.
- No AutoResearchClaw- or AI-Scientist-class generators.

### 8.2 Trainer skill: requirements for the hill-climb infrastructure

1. **A controller-owned state machine.** An immutable run config (metric,
   direction, data roles, scope, budget, acceptance rule). An append-only event
   log validated for consistency. Scope enforced by path. Contradictory state
   fails closed.
2. **Isolation.**
   - A fresh clone per run, with no shared version-control database.
   - Confirmation data and the grader are either not mounted or unreadable by
     the agent's user.
   - Inspect or clear the agent's memory channels between runs.
   - Run a canary check.
3. **Data roles with a read counter.** Search, gate and confirmation sets. A
   confirmation set is read once per frozen candidate and every read is logged.
4. **Feedback hygiene.** Never echo gold labels from the gate or confirmation
   sets. Run an exact-string leakage pre-gate on candidate code, prompts and
   synthetic data.
5. **Acceptance.**
   - Repeated measures or paired tests during search.
   - An A/A calibration before each campaign.
   - Confirmation via the `compare_workflows.py` bound.
   - A per-component and per-slice report.
   - A preregistered hypothesis for each round.
6. **Synthetic data.**
   - Generate it offline, with no web access that could reach the eval set.
   - Record provenance for each row (generator and version, prompt hash, seed).
   - Deduplicate against the confirmation set.
   - Report the first-proposal gain separately from later rounds, as the
     TypeSafe cookbook does: 1.87 → 1.77 RMSE, with most of the gain in the
     first call [R; vendor example].
7. **"Don't train" is a reachable exit.**
   - Success conditions include "incumbent retained" and "infeasible:
     insufficient signal," with no pressure language.
   - Climb a baseline ladder: majority or mean → bag-of-words → a zero-shot
     hosted decision → prompt or skill optimization (SkillOpt-like) → a trained
     head.
8. **Review is a gate.** A severe issue named by any reviewer blocks promotion
   (F.4).

### 8.3 Research patrol and fold automation

The patrol monitors sources and folds claims into notes. It is not a metric
hill-climb, so most autoresearch loops do not fit. What does fit:

1. **A local scheduler with receipts** for the length of 0.8.0.
   Most-overdue-first scheduling (the autoloop idea), implemented with
   launchd or cron plus a headless agent. Receipts follow `maintenance.md`. No
   GitHub Actions, PRs or issues.
2. **Deterministic identity resolution** for each source card:
   - GitHub node ID plus HEAD SHA;
   - arXiv ID plus version;
   - DOI via Crossref or OpenAlex, with retraction status;
   - Hugging Face sha;
   - cached responses with digests (HALLMARK caches responses so reruns are
     reproducible).
3. **A claim ledger for folds.** Each promoted claim records source ID,
   revision, retrieval time, the exact quoted span and its hash, the evidence
   label and the inspection depth.
   - Rules check that labels are consistent; for example, a third-party number
     without a Reported label fails.
   - A claim goes stale when the source revision or the claim text changes
     (ARIS hashing, citationdiff).
4. **A fold-review checklist.** ARFT, especially F.4, plus Hidden Pitfalls'
   four failure modes.
5. **A confirmation flag for paid or network calls, and no automatic rewrite of
   curated references** (the EvoMap pattern). Both match AGENTS.md.
6. **Optional:** PaperQA2 for Q&A over primary PDFs already downloaded. Never a
   substitute for inspecting the primary artifact.
7. **A lint pass** (the llm-wiki "lint" operation). Find contradictions and
   superseded claims across `notes.md` sections, and queue them for human
   review. It makes no automatic edits.

---

## 9. Recommendations

| Item | Action | Reason |
|---|---|---|
| Isolation built into the harness, leak-free feedback, and an audit of cross-run channels (Quran R1–R5, CORAL, AutoResearchExam protocol) | adopt (trainer infrastructure) | These exploit channels were directly observed and are cheap to close. Current Augustus doctrine does not name them |
| Gate ≠ confirmation, a confirmation read counter, and A/A calibration of the acceptance rule | adopt | The AIRA-dojo gap, evo's own concession, and the strict single-run acceptance in most loops |
| Controller-owned event log and scope enforcement (codex-autoresearch) | borrow-pattern | State that fails closed |
| Deterministic claim ledger (Anti-Autoresearch core, ARIS input hashing) | borrow-pattern | Patrol folds and the numbers in the ExoPO paper |
| citegate-style bibliography and retraction gate (local CLI only) | pilot | The ExoPO bibliography and patrol identity checks. Validate on HALLMARK-style fixtures first |
| autoguardrails' empty-policy counterfactual and constraint floor | borrow-pattern | A minimal ExoPO worked example |
| autoreason's incumbent / revision / synthesis rounds with a no-change option | borrow-pattern | Paper revision passes. Judge wins are not quality |
| SkillOpt | watch | Text-space policy optimization with a gate. Check its split protocol |
| PRAXIST, CORAL, evo, Agora, AutoResearchEval (ARFT), AutoResearchExam | watch | Distinct mechanisms. No execution without authority |
| AutoResearchClaw | reject | Heuristic claim checks; a benchmark the authors built and judged, with feedback leakage |
| AI-Scientist-v2, Agent Laboratory, AI-Researcher, DeepScientist for drafting | reject | Fully automated writing; mostly older; documented failure evidence |
| ARA's `wire-ara.md` and autoloop's `install.md` remote-instruction installs | reject | Mutable remote instructions written into AGENTS.md or CLAUDE.md |
| githubnext/autoloop for 0.8.0 | reject | GitHub-hosted and publishes PRs, which breaks confidentiality |
| A local scheduler for the patrol | decide | The maintainer owns cadence and authority |
| LLM-judged objectives in the trainer | decide | Judge bias (RQGM) and drift |

## 10. Open questions for the maintainer

1. Is a local-only scheduler (launchd or cron plus a headless agent, writing
   receipts) acceptable for the patrol during 0.8.0? Who owns it?
2. Should the trainer allow LLM-judged objectives for acceptance, or only
   labelled or observed outcomes, with judges limited to search?
3. May we spend compute on two controlled experiments on a task we control?
   - An A/A test of the acceptance rule.
   - A planted-exploit test: hard-coded evaluation IDs, a leaked gold string,
     and a read of a sibling run.

   Either would turn Reported items into Reproduced ones.
4. What evidence weight should the ExoPO paper give single-author 2026 position
   preprints (2606.23175, 2606.04220): Reported evidence, or motivation only?
5. Should AutoResearchClaw appear in the paper as a negative example, or stay in
   research notes?
6. Should the claim-ledger pattern apply retroactively to `notes.md` (45k
   lines), or only to new folds?

## 11. Not covered and limits

- No tool, benchmark or paper was executed or reproduced. Every number is
  author- or third-party-Reported.
- Full text was read only for 2607.18064v2 (§8.3, §9) and 2507.02554v2 (§5.3
  passages). Everything else is abstract depth. I did not read SkillOpt's split
  protocol or PRAXIST's evidence-maturity rules.
- The listed-lane tools are only cross-noted.
- Not inspected: closed systems (the Edison Kosmos platform, Google
  Co-Scientist, Zochi, Carl, vendor "deep research" products).
- Not inspected here: evolutionary code search (OpenEvolve, ShinkaEvolve,
  AlphaEvolve) and GEPA/DSPy. Other lanes likely cover them.
- X/Twitter was not collected. Karpathy's LOOPS.md remains unverified.
- GitHub coverage is first pages only. Star thresholds biased the sample
  toward popular repositories. Non-English-described repositories are
  undersampled. The README-scope "ledger" query (11,306 hits) was not
  traversed.
- Agents4Science and OpenReview reviews and Hugging Face Papers pages were not
  inspected.
- The five arXiv date/ID anomalies are unexplained.

---

## 12. Sources

Retrieval times are UTC on 2026-09-23. Star counts are observations, not
quality evidence. "Depth" is what I actually read.

### 12.1 Repositories (GitHub REST; node ID, HEAD, license at retrieval)

| Canonical id (node) | URL | Revision (HEAD, date) | License | Retrieved (UTC) | Depth | Stars (obs.) |
|---|---|---|---|---|---|---|
| github:karpathy/autoresearch (R_kgDORgZXsw) | https://github.com/karpathy/autoresearch | 228791fb499a (2026-03-26) | None | 2026-09-23T17:08:06Z | source: README, program.md, prepare.py eval section (listed lane owns card) | 96651 |
| github:aiming-lab/AutoResearchClaw (R_kgDORnWLww) | https://github.com/aiming-lab/AutoResearchClaw | be4ba4755bf1 (2026-08-19) | MIT | 2026-09-23T17:08:08Z | source: README; hitl/claim_verifier.py; literature/verify.py; pipeline/verified_registry.py; experiments/arc_bench/EXPERIMENT_DESIGN.md; releases | 14517 |
| github:uditgoenka/autoresearch (R_kgDORmNgCQ) | https://github.com/uditgoenka/autoresearch | 050e30dc4ba0 (2026-08-12) | MIT | 2026-09-23T17:08:10Z | README | 6367 |
| github:davebcn87/pi-autoresearch (R_kgDORkmdKA) | https://github.com/davebcn87/pi-autoresearch | 939ede8220da (2026-09-10) | MIT | 2026-09-23T17:08:12Z | README | 8110 |
| github:leo-lilinxiao/codex-autoresearch (R_kgDORp-fEA) | https://github.com/leo-lilinxiao/codex-autoresearch | 0f54c5717074 (2026-09-12) | MIT | 2026-09-23T17:08:13Z | source: README; scripts/autoresearch_core.py | 2645 |
| github:evo-hq/evo (R_kgDOR6bLtA) | https://github.com/evo-hq/evo | ab5fbd6c8210 (2026-07-17) | Apache-2.0 | 2026-09-23T17:08:15Z | README + skills/discover/references/constructing-benchmark.md | 1459 |
| github:Human-Agent-Society/CORAL (R_kgDORoQHWg) | https://github.com/Human-Agent-Society/CORAL | 0123dfb939b3 (2026-09-06) | Apache-2.0 | 2026-09-23T17:08:17Z | README | 1008 |
| github:sapientinc/PRAXIST (R_kgDOUGGnKA) | https://github.com/sapientinc/PRAXIST | 5b50658b219d (2026-09-23) | NOASSERTION | 2026-09-23T17:08:19Z | README | 6716 |
| github:EvoMap/AutoResearch (R_kgDOT5Dp9w) | https://github.com/EvoMap/AutoResearch | 21f591298aca (2026-09-13) | Apache-2.0 | 2026-09-23T17:08:21Z | README | 3215 |
| github:wanshuiyin/Anti-Autoresearch (R_kgDOTFlgyg) | https://github.com/wanshuiyin/Anti-Autoresearch | f3ed7577beaf (2026-09-09) | MIT | 2026-09-23T17:08:23Z | README (listed lane owns card) | 156 |
| github:wanshuiyin/Auto-claude-code-research-in-sleep (R_kgDORjDgTA) | https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep | 341f914024d2 (2026-09-18) | MIT | 2026-09-23T17:08:25Z | README grep (listed lane owns card) | 16569 |
| github:ARA-Labs/Agent-Native-Research-Artifact (R_kgDORyuAbQ) | https://github.com/ARA-Labs/Agent-Native-Research-Artifact | e52a925e9d03 (2026-08-24) | MIT | 2026-09-23T17:08:26Z | README; rename join from Orchestra-Research/* (same node) | 682 |
| github:SakanaAI/AI-Scientist-v2 (R_kgDOOV2Kmw) | https://github.com/SakanaAI/AI-Scientist-v2 | 96bd51617cfd (2025-12-19) | NOASSERTION | 2026-09-23T17:11:00Z | README | 7212 |
| github:SakanaAI/AI-Scientist (R_kgDOMiZjRw) | https://github.com/SakanaAI/AI-Scientist | 1de1dbc1f4ee (2025-12-19) | NOASSERTION | 2026-09-23T17:11:02Z | metadata | 14605 |
| github:SamuelSchmidgall/AgentLaboratory (R_kgDONnRoTg) | https://github.com/SamuelSchmidgall/AgentLaboratory | d9017d90e329 (2025-08-20) | MIT | 2026-09-23T17:11:03Z | metadata | 5865 |
| github:HKUDS/AI-Researcher (R_kgDOOGx4LQ) | https://github.com/HKUDS/AI-Researcher | f9a6f8480860 (2025-10-16) | None | 2026-09-23T17:11:05Z | metadata | 5760 |
| github:ResearAI/DeepScientist (R_kgDOP3K-XQ) | https://github.com/ResearAI/DeepScientist | b36624417f0c (2026-06-28) | Apache-2.0 | 2026-09-23T17:11:07Z | README (partial) | 3334 |
| github:Future-House/paper-qa (R_kgDOI55lCg) | https://github.com/Future-House/paper-qa | 57e89f7223b0 (2026-08-12) | Apache-2.0 | 2026-09-23T17:11:09Z | README | 9239 |
| github:stanford-oval/storm (R_kgDOLk3bGg) | https://github.com/stanford-oval/storm | fb951af7744d (2025-09-30) | MIT | 2026-09-23T17:11:10Z | metadata | 31492 |
| github:AkariAsai/OpenScholar (R_kgDONP7Olg) | https://github.com/AkariAsai/OpenScholar | 0e9b8fb91227 (2025-08-13) | Apache-2.0 | 2026-09-23T17:11:12Z | metadata | 1604 |
| github:Just-Curieous/Curie (R_kgDONzTN4w) | https://github.com/Just-Curieous/Curie | db1b1f56159b (2025-09-28) | Apache-2.0 | 2026-09-23T17:11:14Z | metadata | 369 |
| github:openai/frontier-evals (R_kgDOOQUqDQ) | https://github.com/openai/frontier-evals | 51052cede8cc (2026-04-21) | MIT | 2026-09-23T17:11:17Z | metadata + top tree (requested as openai/preparedness; GitHub redirect) | 1302 |
| github:openai/mle-bench (R_kgDOM9X49g) | https://github.com/openai/mle-bench | 507f92e1138b (2026-04-24) | NOASSERTION | 2026-09-23T17:11:18Z | README (leaderboard, rules) | 1750 |
| github:OSU-NLP-Group/ScienceAgentBench (R_kgDOM6ctjw) | https://github.com/OSU-NLP-Group/ScienceAgentBench | c26e151ed601 (2026-07-18) | MIT | 2026-09-23T17:11:20Z | metadata | 173 |
| github:allenai/asta-bench (R_kgDOOMoxmA) | https://github.com/allenai/asta-bench | a9e338070fff (2026-09-03) | Apache-2.0 | 2026-09-23T17:11:22Z | metadata | 138 |
| github:facebookresearch/aira-dojo (R_kgDOO8m36w) | https://github.com/facebookresearch/aira-dojo | c795d8649d30 (2025-09-26) | NOASSERTION | 2026-09-23T17:11:24Z | metadata | 172 |
| github:K-Dense-AI/scientific-agent-skills (R_kgDOQFcxuA) | https://github.com/K-Dense-AI/scientific-agent-skills | 49c6e97775ea (2026-09-21) | MIT | 2026-09-23T17:11:26Z | README (partial) | 46304 |
| github:SantanderAI/autoguardrails (R_kgDOS7VgbA) | https://github.com/SantanderAI/autoguardrails | 1ca0c9b2c005 (2026-07-16) | Apache-2.0 | 2026-09-23T17:11:28Z | README | 130 |
| github:NousResearch/autoreason (R_kgDORzax_Q) | https://github.com/NousResearch/autoreason | 538f8817550e (2026-04-12) | None | 2026-09-23T17:11:29Z | README | 605 |
| github:chrisyangsong/citegate (R_kgDOT1jh-w) | https://github.com/chrisyangsong/citegate | 94cc0a02a63a (2026-08-30) | MIT | 2026-09-23T17:11:31Z | README | 102 |
| github:rpatrik96/hallmark (R_kgDORMBUCQ) | https://github.com/rpatrik96/hallmark | ddd62975e48f (2026-09-21) | MIT | 2026-09-23T17:11:33Z | README (partial) | 13 |
| github:githubnext/autoloop (R_kgDOR4mEFQ) | https://github.com/githubnext/autoloop | 438782ff81b4 (2026-05-13) | None | 2026-09-23T17:11:35Z | README | 73 |
| github:Imbad0202/academic-research-skills (R_kgDORZOZYw) | https://github.com/Imbad0202/academic-research-skills | df064e9da93c (2026-09-23) | NOASSERTION | 2026-09-23T17:11:37Z | README (partial) | 49284 |
| github:InternScience/ResearchClawBench (R_kgDORqQltA) | https://github.com/InternScience/ResearchClawBench | 01bc2371f698 (2026-09-17) | MIT | 2026-09-23T17:11:39Z | metadata | 264 |
| github:PrentisAI/AutoResearchEval (R_kgDOT28VaA) | https://github.com/PrentisAI/AutoResearchEval | 1df36f37bc42 (2026-09-21) | None | 2026-09-23T17:11:41Z | README | 31 |
| github:bespokelabsai/AutoResearchExam (R_kgDOUSMSyw) | https://github.com/bespokelabsai/AutoResearchExam | 7758e84af55f (2026-09-15) | Apache-2.0 | 2026-09-23T17:11:43Z | README | 28 |
| github:EdwardOptimization/Bilevel-Autoresearch (R_kgDORtVf-A) | https://github.com/EdwardOptimization/Bilevel-Autoresearch | 2010e958028f (2026-03-30) | MIT | 2026-09-23T17:11:44Z | metadata | 198 |
| github:Future-House/robin (R_kgDOOs591w) | https://github.com/Future-House/robin | 4a5cce310f3b (2026-04-21) | Apache-2.0 | 2026-09-23T17:11:46Z | metadata | 714 |
| github:jimmc414/Kosmos (R_kgDOQRBD0w) | https://github.com/jimmc414/Kosmos | 6cfe7f690dec (2026-04-04) | None | 2026-09-23T17:11:48Z | metadata (unofficial reimplementation; not Kosmos authors) | 589 |
| github:WecoAI/aideml (R_kgDOLpUc1w) | https://github.com/WecoAI/aideml | 60b3978ddf65 (2026-09-03) | MIT | 2026-09-23T17:11:50Z | metadata | 1538 |
| github:yifanzhang-pro/Agora (R_kgDOUeUNRg) | https://github.com/yifanzhang-pro/Agora | 4ce939e2447b (2026-09-18) | Apache-2.0 | 2026-09-23T17:11:51Z | README | 70 |
| github:josephbsmith/citationdiff (R_kgDOTbK2xQ) | https://github.com/josephbsmith/citationdiff | 7a1c9c053652 (2026-07-17) | MIT | 2026-09-23T17:11:53Z | metadata | 0 |
| github:alchaincyf/darwin-skill (R_kgDOSBP5ZQ) | https://github.com/alchaincyf/darwin-skill | 8a8b66258e3c (2026-09-18) | MIT | 2026-09-23T17:18:20Z | README | 6081 |
| github:microsoft/SkillOpt (R_kgDOSXkMwg) | https://github.com/microsoft/SkillOpt | 79124b37e9a6 (2026-09-05) | MIT | 2026-09-23T17:18:28Z | README | 17393 |

### 12.2 Papers (arXiv export API; version = latest at retrieval)

| arXiv id (version) | Title | v1 date | Retrieved (UTC) | Depth |
|---|---|---|---|---|
| arXiv:2402.14207v2 | Assisting in Writing Wikipedia-like Articles From Scratch with Large Language... | 2024-02-22 | 2026-09-23T17:17:31Z | abstract (export API) |
| arXiv:2404.07738v2 | ResearchAgent: Iterative Research Idea Generation over Scientific Literature ... | 2024-04-11 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2408.06292v3 | The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery | 2024-08-12 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2408.14033v3 | MLR-Copilot: Autonomous Machine Learning Research based on Large Language Mod... | 2024-08-26 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2408.15232v2 | Into the Unknown Unknowns: Engaged Human Learning through Participation in La... | 2024-08-27 | 2026-09-23T17:17:31Z | abstract (export API) |
| arXiv:2409.11363v2 | CORE-Bench: Fostering the Credibility of Published Research Through a Computa... | 2024-09-17 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2409.13740v2 | Language agents achieve superhuman synthesis of scientific knowledge | 2024-09-10 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2410.05080v3 | ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Dri... | 2024-10-07 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2410.07095v6 | MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering | 2024-10-09 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2411.14199v1 | OpenScholar: Synthesizing Scientific Literature with Retrieval-augmented LMs | 2024-11-21 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2411.15114v2 | RE-Bench: Evaluating frontier AI R&D capabilities of language model agents ag... | 2024-11-22 | 2026-09-23T17:17:31Z | abstract (export API) |
| arXiv:2501.04227v2 | Agent Laboratory: Using LLM Agents as Research Assistants | 2025-01-08 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2502.14297v3 | Evaluating Sakana's AI Scientist: Bold Claims, Mixed Results, and a Promising... | 2025-02-20 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2502.14499v1 | MLGym: A New Framework and Benchmark for Advancing AI Research Agents | 2025-02-20 | 2026-09-23T17:17:31Z | abstract (export API) |
| arXiv:2502.16069v2 | Curie: Toward Rigorous and Automated Scientific Experimentation with AI Agents | 2025-02-22 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2502.18864v2 | Accelerating scientific discovery with Co-Scientist | 2025-02-26 | 2026-09-23T17:17:31Z | abstract (export API) |
| arXiv:2504.01848v3 | PaperBench: Evaluating AI's Ability to Replicate AI Research | 2025-04-02 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2504.08066v1 | The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agenti... | 2025-04-10 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2505.13400v1 | Robin: A multi-agent system for automating scientific discovery | 2025-05-19 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2505.18705v1 | AI-Researcher: Autonomous Scientific Innovation | 2025-05-24 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2505.19955v3 | MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research | 2025-05-26 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2505.20662v4 | AutoReproduce: Automatic AI Experiment Reproduction with Paper Lineage | 2025-05-27 | 2026-09-23T17:17:31Z | abstract (export API) |
| arXiv:2505.24785v2 | EXP-Bench: Can AI Conduct AI Research Experiments? | 2025-05-30 | 2026-09-23T17:17:31Z | abstract (export API) |
| arXiv:2506.22419v2 | The Automated LLM Speedrunning Benchmark: Reproducing NanoGPT Improvements | 2025-06-27 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2507.02554v2 | AI Research Agents for Machine Learning: Search, Exploration, and Generalizat... | 2025-07-03 | 2026-09-23T17:13:05Z | full text (HTML) §5.3 passages |
| arXiv:2509.08713v2 | The More You Automate, the Less You See: Hidden Pitfalls of AI Scientist Systems | 2025-09-10 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2509.26603v1 | DeepScientist: Advancing Frontier-Pushing Scientific Findings Progressively | 2025-09-30 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2510.21652v2 | AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite | 2025-10-24 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2511.02824v2 | Kosmos: An AI Scientist for Autonomous Discovery | 2025-11-04 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2511.04583v4 | Jr. AI Scientist and Its Risk Report: Autonomous Scientific Exploration from ... | 2025-11-06 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2604.01658v3 | CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery | 2026-04-02 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2604.05018v1 | PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing | 2026-04-06 | 2026-09-23T17:16:40Z | abstract (export API) |
| arXiv:2604.18805v1 | AI scientists produce results without reasoning scientifically | 2026-04-20 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2604.24658v3 | The Last Human-Written Paper: Agent-Native Research Artifacts | 2026-04-27 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2604.26835v1 | HalluCiteChecker: A Lightweight Toolkit for Hallucinated Citation Detection a... | 2026-04-29 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2605.06635v1 | Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep... | 2026-05-07 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2605.07723v1 | LLM hallucinations in the wild: Large-scale evidence from non-existent citations | 2026-05-08 | 2026-09-23T17:16:40Z | abstract (export API) |
| arXiv:2605.10246v2 | SciIntegrity-Bench: A Benchmark for Evaluating Academic Integrity in AI Scien... | 2026-05-11 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2605.20025v2 | AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collabor... | 2026-05-19 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2605.22343v1 | Sibyl-AutoResearch: Autonomous Research Needs Self-Evolving Trial-and-Error H... | 2026-05-21 | 2026-09-23T17:16:40Z | abstract (export API) |
| arXiv:2605.23899v1 | From Raw Experience to Skill Consumption: A Systematic Study of Model-Generat... | 2026-05-22 | 2026-09-23T17:18:34Z | abstract (export API) |
| arXiv:2605.23904v2 | SkillOpt: Executive Strategy for Self-Evolving Agent Skills | 2026-05-22 | 2026-09-23T17:18:34Z | abstract (export API) |
| arXiv:2606.04220v1 | Dead Science Walking: Publication Bias and the AI Scientist Pipeline | 2026-06-02 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2606.05241v1 | Search-Time Contamination in Deep Research Agents: Measuring Performance Infl... | 2026-06-03 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2606.07576v1 | When Should an AI Scientist Stop? Verifiable Experiment Steering and Refusal ... | 2026-05-26 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2606.07591v5 | ResearchClawBench: A Benchmark for End-to-End Autonomous Scientific Research | 2026-05-28 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2606.11045v1 | What Fits (Into Few Tokens) Doesn't Overfit: Compression and Generalization i... | 2026-06-09 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2606.11522v1 | Search Discipline for Long-Horizon Research Agents | 2026-06-09 | 2026-09-23T17:16:40Z | abstract (export API) |
| arXiv:2606.18874v3 | Externalizing Research Synthesis and Validation in AI Scientists through a Re... | 2026-06-17 | 2026-09-23T17:16:40Z | abstract (export API) |
| arXiv:2606.21024v1 | Negative Knowledge as Failure-aware Shared Memory for AutoResearch | 2026-06-19 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2606.23175v1 | Position: Correct Answer, Wrong Mechanism -- When AI Scientists Defend Genera... | 2026-06-22 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2606.26294v2 | The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators | 2026-06-24 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2607.17100v2 | Auto Research for Materials: Auditable AI-Scientist Workflows with Held-Out T... | 2026-07-19 | 2026-09-23T17:16:40Z | abstract (export API) |
| arXiv:2607.18064v2 | Autoresearch with Coding Agents: Generalizers and Metric-Maximizers on Quran ... | 2026-07-20 | 2026-09-23T17:13:05Z | full text (HTML) §8.3, §9 |
| arXiv:2607.27687v1 | Rehearse: Stepping Back from the Confidence Cliff in Self-Improving Autoresearch | 2026-07-30 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2608.05179v1 | Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap | 2026-06-29 | 2026-09-23T17:16:40Z | abstract (export API) |
| arXiv:2608.10424v1 | Recovering Wasted Compute in Autoresearch Agents | 2026-08-11 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2608.11241v1 | RecSys Factory: Bounding LLM Agent Autonomy to Decision Points in the Industr... | 2026-07-31 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2608.14905v3 | How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 R... | 2026-08-14 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2608.17906v4 | AutoResearch: Insight In, Hallucination Out | 2026-08-18 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2608.19511v1 | Symposium: Trust via Auditable Records for Communities of AI Scientist Agents | 2026-08-20 | 2026-09-23T17:16:40Z | abstract (export API) |
| arXiv:2608.25955v1 | Praxist: From Experimental Artifacts to Solution Lineages | 2026-08-26 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2609.00065v2 | Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents | 2026-08-30 | 2026-09-23T17:16:40Z | abstract (export API) |
| arXiv:2609.07713v1 | The Emerging AI Paper-Review Arms Race: Adversarial Co-Evolution in Scholarly... | 2026-09-07 | 2026-09-23T17:16:40Z | abstract (export API) |
| arXiv:2609.09203v1 | OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows | 2026-09-05 | 2026-09-23T17:16:40Z | abstract (export API) |
| arXiv:2609.11975v1 | AI-Research Agents in the Wild. From GitHub and arXiv to Regularities and Gaps | 2026-09-01 | 2026-09-23T17:13:05Z | abstract (export API) |
| arXiv:2609.18094v2 | Agora: Git as Shared Memory for Collective AutoResearch | 2026-09-16 | 2026-09-23T17:12:38Z | abstract (export API) |
| arXiv:2609.21257v1 | Verify, Don't Trust: Agentic Model Development for Video Discovery Retrieval ... | 2026-09-18 | 2026-09-23T17:16:40Z | abstract (export API) |
| arXiv:2609.26457v1 | Recursive self-improvement of AI research agents | 2026-09-22 | 2026-09-23T17:13:05Z | abstract (export API) |

### 12.3 Files, datasets, docs and registries inspected

| Source | URL | Revision / digest | Retrieved (UTC) | Depth |
|---|---|---|---|---|
| AutoResearchClaw `researchclaw/hitl/claim_verifier.py` | https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/hitl/claim_verifier.py | be4ba4755bf1 | 2026-09-23T17:11Z | source (full file, 348 lines) |
| AutoResearchClaw `researchclaw/literature/verify.py` | https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/literature/verify.py | be4ba4755bf1 | 2026-09-23T17:11Z | source (structure + thresholds, 974 lines) |
| AutoResearchClaw `researchclaw/pipeline/verified_registry.py` | https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/verified_registry.py | be4ba4755bf1 | 2026-09-23T17:12Z | source (key functions, 449 lines) |
| AutoResearchClaw `experiments/arc_bench/EXPERIMENT_DESIGN.md` | https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/experiments/arc_bench/EXPERIMENT_DESIGN.md | be4ba4755bf1 | 2026-09-23T17:20Z | full file (96 lines) |
| AutoResearchClaw releases | https://api.github.com/repos/aiming-lab/AutoResearchClaw/releases | v0.3.0–v0.5.0 | 2026-09-23T17:19Z | metadata |
| hf:AIMING-Lab-UNC/ARC-Bench (dataset card) | https://huggingface.co/datasets/AIMING-Lab-UNC/ARC-Bench | sha 5a5923be8d30; lastModified 2026-05-22 | 2026-09-23T17:19Z | API metadata + card head |
| codex-autoresearch `scripts/autoresearch_core.py` | https://github.com/leo-lilinxiao/codex-autoresearch/blob/0f54c571707487f59486ba7c50d405edfc746c19/scripts/autoresearch_core.py | 0f54c5717074 | 2026-09-23T17:22Z | source (acceptance, scope, state validation) |
| evo `plugins/evo/skills/discover/references/constructing-benchmark.md` | https://github.com/evo-hq/evo/blob/ab5fbd6c8210ed900157c8907a431bafc74c4215/plugins/evo/skills/discover/references/constructing-benchmark.md | ab5fbd6c8210 | 2026-09-23T17:22Z | full doc (171 lines) |
| karpathy/autoresearch `program.md`, `prepare.py` | https://github.com/karpathy/autoresearch/tree/228791fb499afffb54b46200aca536f79142f117 | 228791fb499a | 2026-09-23T17:09Z | full program.md; grep of prepare.py eval section |
| openai/mle-bench README (leaderboard note 2026-04-24) | https://github.com/openai/mle-bench/blob/507f92e1138bb6e40dac5c6ee7a6758e6424bf97/README.md | 507f92e1138b | 2026-09-23T17:14Z | README sections |
| Crossref: AI Scientist in Nature | https://doi.org/10.1038/s41586-026-10265-5 | Nature 651:914–919, 2026-03-25 | 2026-09-23T17:24Z | Crossref metadata only |
| TypeSafe cookbook: autoresearch feature discovery (official docs) | https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery.md | sha256 00ee0cfff9cf… (71,497 bytes, HTTP 200) | 2026-09-23T17:21Z | intro + split/loop passages |
| Karpathy gist "llm-wiki" | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f | created 2026-04-04 (API returned 502; raw fetched, 11,985 bytes) | 2026-09-23T17:25Z | full text |
| arXiv HTML full text 2607.18064v2 | https://arxiv.org/html/2607.18064v2 | v2 (2026-08-27) | 2026-09-23T17:14Z | §8.3, §9 |
| arXiv HTML full text 2507.02554v2 | https://arxiv.org/html/2507.02554v2 | v2 (2025-11-04) | 2026-09-23T17:15Z | §5.3 passages, figure captions |
| GitHub search / arXiv query ledgers (local) | research/080/tmp/autoresearch-discovery/search_ledger.jsonl, arxiv_ledger.jsonl | 18 GitHub + 19 arXiv queries | 2026-09-23T17:03–17:18Z | coverage receipts |

Raw packet (README bodies, source excerpts, abstracts, ledgers): `research/080/tmp/autoresearch-discovery/`. The listed-lane packet is separate: `research/080/tmp/autoresearch-listed/`.
