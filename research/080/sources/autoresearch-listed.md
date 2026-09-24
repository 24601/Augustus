# Autoresearch tooling: inspection of the maintainer's list

Confidential 0.8.0 lane report. Nothing here was posted, pushed, or filed on
GitHub or anywhere else. Lane: auto-research / autoscience tooling. Date:
2026-09-23. Retrieval window: 2026-09-23T17:01:50Z to 17:12:37Z.

**Method.** I shallow-cloned each repository (`--depth 1`, hooks disabled, LFS
smudge off) into `research/080/tmp/autoresearch-listed/src/` so I could read it.
I also used GitHub REST metadata, the arXiv export API, and one official arXiv
blog page. **Nothing third-party was installed, built, or run.** The only
processing was static: parsing files and XOR-decoding one obfuscated HTML
blob with Python.

**Inspection depth.** Every listed tool got README + key-source depth. Items
pulled from the Awesome list got metadata or README depth, as marked in the
sources table.

**Evidence labels** follow `research/protocol.md`:

- **Contract**: behaviour or interface visible in source or official docs at the recorded SHA. It is not executed behaviour.
- **Reported**: a third-party claim or number.
- **Hypothesis**: my inference or design implication.
- **Unknown**: not established.

Stars, forks, issue counts and commit counts are observations, not quality
evidence. None of these repositories appeared in `research/notes.md` or
`research/sources.json` before today. All nine are first sightings.

## Bottom line

1. **Adopt nothing.** No listed tool closes the scheduler gap in
   `research/maintenance.md`. None supplies a verified recurring job with
   liveness receipts. DARE explicitly hands scheduling to the "host runtime".
   CoAutoResearch loops inside one project with no calendar recurrence. FAROS
   has background jobs only. swarm-factory's "24/7 unattended operation" is
   fabricated. The gap is an owner/host decision, not a tooling purchase.
2. **Two pilots, both local and both needing maintainer approval before any
   third-party code runs:**
   - **mareforma** for the trainer eval harness. It gives computed-not-declared
     grounding receipts and a pre-registered prediction with a computed
     "bearing" (the direction of evidence, computed rather than declared).
   - **Anti-Autoresearch**, found through the list, to audit our own ExoPO
     draft for self-consistency and citation integrity. No public log and no
     upload.
3. **Borrow patterns, not code:**
   - FAROS evaluation discipline: frozen hashed manifests that refuse drift, a
     leakage validator, `precision = null` when gold labels are
     non-exhaustive, bootstrap by source unit, and matched-budget baselines.
     FAROS has **no licence file**, so ideas only.
   - CoAutoResearch's ordered stop-status truth table.
   - DARE v4's runtime-boundary invariants.
   - karpathy/autoresearch's "evaluator outside the agent's write set".
   - scholaraio's closed-world citation states, which need strengthening.
4. **Reject:**
   - **Usaid22/swarm-factory is a malware or scam lure.** It contains no
     source code. Two hourly bot workflows fake activity (2,099 bot commits).
     Its GitHub Pages "download" page is XOR-obfuscated JavaScript that
     auto-redirects to an external domain. Do not visit it.
   - **InternAgent** as a loop design. Its scorer averages relative changes
     without regard to metric direction, and the metrics it scores are written
     by the agent-edited code itself. Keep it only as counterexample fixtures.
5. **Watch:**
   - **ToolUniverse**: a biomedical tool platform. It has an unpinned
     `uvx --refresh` supply chain and a remote-instruction setup.
   - **Awesome-AI-Scientist**: a useful discovery index. It is not evidence
     and it lists its own organisation's system first.
6. **Decide (ExoPO route).** arXiv's CS category now requires review articles
   and position papers to be accepted through peer review before submission
   (official blog, 2025-10-31, retrieved today). A "position paper" on arXiv
   cs.* needs a venue acceptance first, or a different framing or category.

## Fit and stage coverage

Fit targets:

- **(a)** automating the recurring patrol and fold
- **(b)** the 0.8.0 trainer skill's hill-climb and experiment loop
- **(c)** drafting or critiquing the ExoPO paper

Stage columns:

- **Lit**: search and reading
- **Idea**: hypothesis or idea generation
- **Design**: experiment design
- **Exec**: code execution
- **Anal**: analysis
- **Write**: paper writing
- **Rev**: review and critique
- **Prov**: provenance and citation
- **Sched**: scheduling and recurrence

Cell values: Y = implemented; P = partial or prompt-only; – = absent.

| Tool | Lit | Idea | Design | Exec | Anal | Write | Rev | Prov | Sched | Fit | Action |
|---|---|---|---|---|---|---|---|---|---|---|---|
| OpenNSWM-Lab/FAROS | Y | Y | Y | Y (Docker; host fallback) | Y | Y | Y (ReviewX) | Y | P (background jobs) | b, c patterns | borrow-pattern |
| ZimoLiao/scholaraio | Y | – | – | P (scientific tool docs) | P | Y | P | Y (library-bound) | – | c (citations), a (library) | borrow-pattern |
| yogsoth-ai/de-anthropocentric-research-engine | Y (paid/hosted MCP) | Y | Y | – | P | – | P (red-team SOPs) | P | – (delegated to host) | a patterns | borrow-pattern |
| Omni-Scientist/Awesome-AI-Scientist | index | – | – | – | – | – | – | – | – | discovery for a, b, c | watch |
| Usaid22/swarm-factory | none (no code) | – | – | – | – | – | – | – | fake | none | reject |
| YihongT/CoAutoResearch | P | Y | Y | Y (agent CLI) | Y | Y | Y (internal reviewers) | Y (result cards) | P (in-project loop) | a, b patterns | borrow-pattern |
| mims-harvard/ToolUniverse | Y (tools) | – | – | Y (tools) | P | – | – | P (cache hashes) | – | none now | watch |
| InternScience/InternAgent | Y | Y | P | Y (host) | P | – | P | – | – | b (negative) | reject |
| mareforma/mareforma | – | – | P (pre-registration) | – | Y (bearing) | – | P (contest) | Y | – | b pilot, a pattern | pilot |

## Tool cards

### 1. OpenNSWM-Lab/FAROS

**Identity:**

- Node `R_kgDOScPUtg`. HEAD `4e4e96fde842ced39b5bfd805b5666b4ce7cca0e` (2026-09-05). Last push 2026-09-05. Created 2026-05-13.
- **No licence.** There is no LICENSE file and the licence API returns 404, so all rights are reserved.
- Not a fork.
- README badges claim 685 backend and 41 frontend tests passed. The README body says 644 and 35. The mismatch is internal.

**What it is.** A FastAPI + React "Foundation AutoResearch Operating System":

- Idea generation → `PlanPackage` (a typed contract) → code in a sandbox → experiment → LaTeX paper → "ReviewX" claim–evidence–measurement audit → human sign-off.
- A "Blueprint + Capability + Profile + Provider" runtime.
- The README calls it a release candidate for competition validation. It also ships `scripts/start_competition_backend.sh`.

**Mechanism (Contract):**

- **Evidence gate.** Literature search runs over arXiv, Semantic Scholar, OpenAlex, Crossref, DBLP and Wanfang, followed by semantic filtering before ideation.
- **Closed citation set.** The outline prompt requires that references "MUST contain only those evidence papers" from the plan's evidence package (`modules/paper/skills/outline.py`).
- **ReviewX support states:** `supported`, `weakly_supported`, `unsupported`, `contradicted`, `artifact_absent` ("not proof of a false claim") and `needs_human_verification`.
- **Evaluation harness** (`experiments/reviewx_eval`):
  - frozen manifests that hash samples, gold labels, paper artifacts, the method matrix, eval code and git state, and refuse changed inputs or resumes with a different fingerprint;
  - leakage-resistant corruption benchmarks (CEM-Bench v2) that keep labels out of model-visible IDs and metadata, plus a leakage validator;
  - `precision/F1 = null` when gold labels are non-exhaustive;
  - bootstrap resampling by source paper, not by derived variant;
  - blind human-annotation export;
  - PeerQA dev/held-out split, with the held-out split "unseen until the method and alignment threshold are frozen";
  - matched-budget single-prompt and structured-rubric baselines.

**Human gates (Contract, with caveats):**

- The README claims human approval at plan, result-interpretation and final sign-off.
- In the Blueprint runtime, the file-based approval backend treats a decision file with no `status`/`approved` fields as **approved**. This is `data.get('status','approved')` in `faros/providers/external_backend.py`.
- In the sample `faros_hybrid` profile, `HumanProvider` has no external backend configured. It returns `ok=True` with the canned text "Human review checkpoint completed" and `scoreSuggestion: 6` (`faros/providers/human_provider.py`).
- Both are fail-open gate patterns. They are source-read, not executed.

**Evidence:**

- **Reported.** `backend/experiments/reviewx_scifact/RESULTS.md` (run 2026-08-25, 339 SciFact dev pairs, threshold fixed at 0.5):
  - F1 0.7746 against 0.7460 for a lexical baseline;
  - ECE 0.0345 against 0.0819;
  - every 95% paired-bootstrap interval crosses zero;
  - the authors call it a proof of concept, not conclusive;
  - raw data and predictions are not redistributed.
- **Independent evidence: none.**

**Models, APIs and cost:**

- Qwen is recommended (DashScope). Also MiniMax, Moonshot, DeepSeek, Zhipu, OpenAI and Anthropic.
- Docker is needed for the production sandbox. LaTeX with CJK is needed for PDFs.
- Cost: Unknown.

**Safety:**

- **Docker sandbox (Contract):** `--network none`, `--cap-drop ALL`, `--read-only`, `no-new-privileges`, with memory and CPU limits.
- **Host fallback.** When Docker is unavailable it falls back to `create_subprocess_shell` on the host with a denylist. Host execution is allowed by default because `FAROS_EXECUTION_ROLE` defaults to `development`.
- **User identity.** Identity comes from an `X-Faros-User` header, which needs a trusted proxy. This is documented.

**Maintenance (observations):**

- 100 commits between 2026-07-13 and 2026-09-05. 11 contributors; the top author has 61 commits.
- No releases or tags.
- 3,037 stars and 390 forks in about four months.
- 99 of the 100 most recent issues were filed on one day (2026-08-30) by distinct accounts, as generic code-review items. That looks like a bulk campaign.
- One of those issues claims `shell=True`. That string does not appear at HEAD, but `create_subprocess_shell` does.
- Issue counts and stars carry no weight.

**Fit:**

- (b) The evaluation-harness discipline is the best on the list.
- (c) The ReviewX support states make a good self-audit checklist for ExoPO.
- (a) None.

**Action: borrow-pattern.** The patterns are strong and generic. The code is unlicensed, and the runtime has fail-open gate stubs and a host-execution default.

### 2. ZimoLiao/scholaraio

**Identity:**

- Node `R_kgDORimTkw`. HEAD `c3a4b2656b2018fb372ae63a7256c61956e4ea50` (2026-09-20). Last push 2026-09-20. Created 2026-03-09.
- Licence MIT (file present).
- Releases: v2.0.0 on 2026-08-17.

**What it is.** An "academic harness" for coding agents. It is a Python CLI plus 44 agent skills, symlinked for Claude Code, Codex and Qwen. It covers:

- PDF ingest to structured Markdown (MinerU or Docling);
- hybrid keyword and vector search;
- a citation graph;
- workspaces;
- BibTeX/RIS export;
- writing workflows;
- `citation-check`.

`STRATEGY.md` explicitly says it is **not** an autonomous scientist and does not own hypothesis generation or experiment loops.

**Mechanism: citation check (Contract, `services/citation_check.py`).**

- A regex extracts author–year citations only. Numbered and identifier citations are not handled.
- Each citation gets one of three statuses against the local library index:
  - `VERIFIED`: a unique match on first-author surname plus year;
  - `AMBIGUOUS`;
  - `NOT_IN_LIBRARY`.
- **Limit.** `VERIFIED` does not check the title, identifier, or whether the paper supports the claim. A fabricated "Smith (2020)" passes if any Smith 2020 paper is in the library.
- The skill text asks for manual layers afterwards: DOI metadata cross-check, then full-text "content consistency".
- The skill asserts "about 40% of AI-generated citations may be hallucinated" with no source. That number is Reported and unsourced.

**Human gates.** The researcher drives the coding agent. There is no autonomous loop.

**Evidence.** Tests exist (`tests/test_citation_check.py` and others). No outcome evaluation was found. Independent evidence: none.

**Models, APIs and cost:**

- The default LLM is `deepseek-chat` via an OpenAI-compatible API. Anthropic, Google and local models are optional.
- MinerU cloud parsing is optional and uploads PDFs to `mineru.net`.
- Publisher PDF fetch uses the user's own campus or network entitlements.

**Safety:**

- The plugin manifest's SessionStart hook runs `scripts/check-deps.sh`.
- Cloud LLM and parsing endpoints receive full text. That is a confidentiality concern for 0.8.0 material.
- Publisher fetch raises licensing and terms-of-service questions.

**Maintenance (observations):**

- 7 contributors: ZimoLiao 460, "claude" 147.
- Cadence 2026-05 to 2026-09, slowing in September (2 commits).
- Frequent releases.

**Fit:**

- (c) The three-state closed-world citation check is a good minimal shape. For ExoPO it must be strengthened: resolve by identifier (arXiv ID or DOI), match the title, and read for claim support.
- (a) A local paper library could hold the patrol's primary PDFs, but it adds an ingest stack we don't need.

**Action: borrow-pattern.** It shows the right shape, but the `VERIFIED` label is too strong for what it checks.

### 3. yogsoth-ai/de-anthropocentric-research-engine (DARE)

**Identity:**

- Node `R_kgDORMuzGQ`. HEAD `cbc38aa2466d209a592710b0e09304bbdef98696` (2026-09-23). Last push 2026-09-23. Created 2026-02-10.
- Licence Apache-2.0.
- Latest release v3.2.2 (2026-06-21).
- **README/HEAD drift.** The README describes "v3.2.2" and "900+ skills" in 9 or 10 packages; the repo description and README disagree on the package count. HEAD commits say "replace v3 sources with the v4 graph". v4 has 267 nodes (tactics and SOPs, the atomic single-step procedures), with 474 edges, and `skills/` is byte-identical to `v4/skills/`.
- **Contributor observations.** "Tavily PR Agent" and a Keenable-affiliated account each contributed once, alongside MCP integrations for their products.

**What it is.** Pure-Markdown skills for Claude Code that orchestrate "autonomous" research: direction → literature → gap → hypothesis → ideation → stress test → experiment design → an executable "Research Spec". The philosophy is explicitly anti-human-in-the-loop: "without asking for permission". The human's role is "oracle" and "guardian".

**Mechanism (Contract, `v4/docs/runtime-boundary.md`, `architecture.md`):**

- Two executable node types (tactic, SOP). Each returns a fixed eight-field `ResearchStateDelta`: findings, evidence_updates, hypothesis_updates, assumption_updates, uncertainties, decisions, open_questions, recommended_jumps.
- Checkpoints are **append-only**. The spec is a deterministic projection of the checkpoint event stream.
- **Invariant 5:** "a stage completes only when its completion criteria are verifiable; the runtime may not substitute timeout, budget exhaustion or an empty agent result for completion".
- Relative gates must declare formula, numerator, denominator, baseline checkpoint, direction and threshold.
- Saturation must compare the current batch with a comparable previous batch.

**Human gates.** Spec approval only. After that the agent works autonomously within "±10% deviation bounds". Sampled v4 SOPs (`update-confidence-from-evidence`, `verify-evidence-independence`) are procedure text for the LLM. There is no arithmetic in code, and "confidence" has no defined semantics.

**Hallucinated citations.** No v4 skill references DOI, Semantic Scholar or paper-ID verification (0 files). Independence is handled as prose ("no record is counted as independent without a documented lineage break").

**Evidence.** No evaluation. `validate_graph.py` checks structure only. Independent evidence: none.

**Models, APIs and cost:**

- Claude Code or Codex as the executor.
- `mcp.example.json` includes:
  - **paid or keyed** search: Brave, Tavily, Apify, Semantic Scholar key;
  - **hosted keyless** endpoints: alphaXiv, Keenable, you.com;
  - servers launched with `npx -y …@latest`, which is unpinned.

**Safety:**

- Autonomous by design.
- Unpinned MCP packages.
- Hosted search MCPs receive every query. That leaks the research agenda to vendors, which conflicts with 0.8.0 confidentiality and our no-paid-search rule.

**Maintenance (observations):** 614 commits by one author; 100 commits in September alone; 7 contributors.

**Fit:**

- (a) The runtime-boundary invariants map directly onto `maintenance.md`: "collection success must not advance last completed review".
- (b) and (c): none.

**Action: borrow-pattern** (the invariants and the delta schema). Reject the runtime posture.

### 4. Omni-Scientist/Awesome-AI-Scientist (list; triage below)

**Identity:**

- Node `R_kgDOUCwsyA`. HEAD `bad5e3cd71a502433bd53a16b05e2a6976923232` (2026-09-09). Created 2026-08-24.
- Licence CC-BY-4.0. The GitHub API reports NOASSERTION.
- 19 commits (18 by one account), 2 contributors.

**What it is.** A curated list of 497 entries. It has a site build, a link checker and a taxonomy script.

**Quality notes (observations):**

- The owning organisation's own **OmniScientist** is the first entry in two sections (self-listing).
- The list requires "a real license" for Workbenches but includes karpathy/autoresearch, which has no licence (API 404, no LICENSE file).
- Its "license traps" claims match the GitHub API for all three I checked: HKUDS/AI-Researcher and UniPat-AI/UniScientist have no licence; gomesgroup/coscientist is NOASSERTION.
- Only 2 of our 9 listed tools appear in it: ToolUniverse and InternAgent.

**Action: watch.** Use it as a discovery index for the patrol. Appearing on it, or in correlated lists, is not evidence.

### 5. Usaid22/swarm-factory

**Identity:**

- Node `R_kgDOS7EfgA`. HEAD `3f310cffb90811023a8e2783d5c207e07905a7e8` (2026-09-23T16:32Z). Created 2026-06-15.
- No licence file, although the README claims MIT.
- The repo name "swarm-factory" does not match the README product "LabRat".
- The decoded page title is "archive / ecore-project.zip". That looks like a lure template, not a project identity.

**What it is (Contract, static reading):**

- Six files: README.md, index.html, two random-named `.github/*` stamp files, and two workflows.
- **No source code.**
- Both workflows run hourly (`cron: '0 * * * *'`). They append a timestamp to a stamp file and commit it with random messages such as "optimize load #8588". That produces 2,099 github-actions[bot] commits.
- `index.html` is an XOR-encoded blob (`atob` key and data, then `document.write`). Decoded statically, it is a fake "Secure Download" progress page. It auto-redirects after about 10 seconds to an external domain, which I did not visit. The README's "Get Release" badge links to this Pages site.

**Research-loop stages.** None. The README's multi-agent "market allocation" and "24/7 unattended operation" describe nothing in the repository.

**Safety.** It is a probable malware or scam distribution lure. Do not visit the Pages URL or download anything.

**Action: reject.** It is on the maintainer's list, so it was closed with this disposition. Reporting it to GitHub would be an external action and needs the maintainer's authority.

### 6. YihongT/CoAutoResearch

**Identity:**

- Node `R_kgDOS7557Q`. HEAD `ecbdf464f9140ebd199c69250a7df3050ee42a6c` (2026-09-12). Created 2026-06-16.
- `pushed_at` is 2026-09-19, but the only branch (main) is at 2026-09-12. That is unexplained.
- Licence Apache-2.0. Release v2.0.0 (2026-09-11).
- 5 contributors, mostly the author's aliases.

**What it is.** A local dashboard (Node + Python) that drives the user's authenticated Codex CLI or Claude Code through bounded "Trials". It stages result cards, runs internal reviewers, merges authorised decisions, and generates a paper from a **frozen evidence snapshot** without running new experiments. The disclaimers are candid:

- "Internal review is not external peer review or proof of a scientific claim."
- The example papers are "developer-operated research drafts with human intervention".

**Mechanism (Contract, `templates/default/ui/v2_gate.py`, `requirements/GATE_TRUTH_TABLE.yaml`).** An ordered goal gate: `killed_by_human > pass > needs_human > paused_budget > blocked > continue > no_viable_line`.

- `needs_human` requires exactly one concrete question, `blocking=true` and `can_continue_meanwhile=false`.
- `blocked` requires a concrete non-human recovery condition, and is invalid while an independent valuable move exists.
- `pass` requires every key claim to map to accepted or qualified result cards, negative evidence to be visible, final reviewers to pass strictly, and a Human Brief stating what was proved and what was not.
- Plan approval is bound by `plan_sha256`.
- **Caveat (Contract).** The gate code "does not trust agent-recommended status fields". But its input signals (`budget_reached`, `viable_path`, `expected_value`, …) are read from a staged `GATE_EVIDENCE.json` written by the agent's stage. Only final readiness (a projection over cards and reviews) and the kill authority are service-derived. A deterministic combiner over agent-attested booleans is not an independent gate.

**Hallucinated citations.** Paper generation uses citation skills on the frozen snapshot. I did not audit it beyond that. Unknown.

**Evidence.** Two example papers (Digits and Ising, CPU-bounded), self-described as developer-operated. Independent evidence: none.

**Models, APIs and cost:**

- The user's Codex or Claude Code subscription or API.
- Z.ai GLM gateway presets exist.
- Paper PDF needs Python 3.12, LaTeX and Poppler.
- Cost is bounded by configured trial, time and token limits. Actual cost: Unknown.

**Safety:**

- The defaults are Codex `workspace-write` + `on-request` and Claude `manual`.
- `full-access` / `danger-full-access` and `bypassPermissions` presets are available.
- Remote server mode needs an authenticated network boundary (documented).

**Maintenance (observations):** 100 commits between 2026-06-26 and 2026-09-12. 10 README translations.

**Fit:**

- (a) The ordered run-status vocabulary fits scheduled fold receipts.
- (b) The stop statuses map to the trainer's "don't train / stop" exits.
- (c) The "paper from frozen evidence snapshot" rule is a good rule for any results section in ExoPO.

**Action: borrow-pattern.** A full platform is more than we need, and its gate inputs are agent-attested.

### 7. mims-harvard/ToolUniverse

**Identity:**

- Node `R_kgDOOCnxVw`. HEAD `c0b9b71c843df285865eb96c283a5e06eb3ea58e` (2026-09-23). Created 2025-03-03 (older than 2026).
- Licence Apache-2.0. Release v1.5.1 (2026-09-22).
- Paper arXiv 2509.23426 v3 (updated 2026-08-07).
- 32 contributors.

**What it is.** An "AI-Tool Interaction Protocol" and MCP server exposing more than 1,000 tools (Reported), mostly biomedical, plus 68 agent skills. It has a `tu` CLI and a "compact mode" that reduces the exposed tools to 4 or 5 discovery tools. Literature tools cover arXiv, Semantic Scholar, OpenAlex, Crossref, PubMed and Europe PMC.

**Mechanism (Contract):**

- The tool cache key includes `sha256(STATIC_CACHE_VERSION + class source + parameter schema)[:16]` (`base_tool.py`). A changed tool implementation therefore invalidates its cache.
- The default cache TTL is `None` (no expiry). A cached literature search can be served stale unless the TTL is configured.

**Human gates.** None at the platform level. The platform is a tool layer.

**Hallucinated citations.** Not addressed. It retrieves; it does not verify claims.

**Evidence.** The paper and downstream agents (TxAgent, Medea) are Reported. Independent evidence: none.

**Models, APIs and cost:** Any LLM. Many tools need their own API keys.

**Safety:**

- The recommended MCP config runs `uvx --refresh tooluniverse`, which fetches and executes the newest PyPI release on every launch.
- The "AI agent" install path is "Read https://aiscientist.tools/setup.md and set up ToolUniverse for me". That is remote instructions executed by an agent.
- A large tool surface means a large injection surface.

**Maintenance (observations):** Very active: 100 commits in September, weekly releases.

**Fit.** None today. We already reach arXiv, Crossref and OpenAlex through direct public APIs with explicit receipts. The cache-version hash is a small reusable idea.

**Action: watch.**

### 8. InternScience/InternAgent

**Identity:**

- Node `R_kgDOOrCg_Q`. HEAD `fa8c3eedfa9751d3752ea6eb49220b303ac2397d` (2026-07-29). Last push 2026-07-29. Created 2025-05-16 (older than 2026).
- The licence file is Apache-2.0 with a prepended copyright line; the API reports NOASSERTION/"Other".
- **Rename verified.** `Alpha-Innovator/NovelSeek` and `Alpha-Innovator/InternAgent` both redirect to this repository with the same node ID. The README's "NovelSeek renamed to InternAgent (2025-07-10)" is supported by that join.
- Papers: arXiv 2505.16938 v3 (InternAgent 1.0) and 2602.08990 v1 (InternAgent 1.5).
- **Copied code.** 386 of the 492 files under `internagent/mas` are a vendored CAMEL 0.2.47 copy.

**What it is.** Closed-loop "autonomous discovery". It generates ideas, then runs experiments via a Claude Code or iFlow backend that edits `experiment.py`, then runs `launcher.sh`. It scores against `run_0`, supports MCTS variants, has a memory module, and has deep-research QA.

**Mechanism: scoring (Contract, `internagent/stage.py::_calculate_experiment_performance`).**

- `overall_improvement_rate` is the **unweighted mean of per-metric `(current−baseline)/|baseline|·100`**. It ignores metric direction and uses one run with no repeats.
- For a lower-is-better metric (RMSE, MAE), a worse result counts as positive "improvement".
- The metrics come from `final_info.json`, which is written by the `experiment.py` that the agent just edited. The evaluator sits inside the agent's write set.
- `tasks/metric_config.json` does declare directions, but only the MCTS/iFlow path reads it. It also marks `"Test Top 20 DE MSE": true`, meaning higher-is-better for an MSE.
- The result feeds the memory used to steer later ideas.

**Human gates.** None found in `stage.py`.

**Hallucinated citations:**

- No verification code outside the vendored CAMEL benchmarks.
- **Live example of a citation error.** The README BibTeX gives both FlowSearch and AutoMLGen the ID `arXiv:2510.08521`. The arXiv API returns 2510.08521v2 = FlowSearch (Hu et al.), so the AutoMLGen entry has a wrong ID. An author–year check such as scholaraio's would not catch this.

**Evidence.** Reported only:

- "#1 on MLE-bench" for the separate MLEvolve repository;
- "leading on GAIA/HLE/GPQA/FrontierScience".

**Models, APIs and cost:** OpenAI (embeddings and memory), OpenRouter, Anthropic (Claude Code backend). GPU tasks. Cost: Unknown.

**Safety:**

- `claude --permission-mode acceptEdits` runs in the experiment directory.
- `bash launcher.sh` runs on the host with a copy of the full `os.environ` (API keys included) and no sandbox.

**Maintenance (observations):** 49 commits since 2025-05. Bursty (24 in 2026-02). 9 contributors. No GitHub releases; tags up to v1.5.0.

**Fit.**

- (b) Negative only: it supplies test fixtures for what the trainer loop must reject.
- (a) and (c): none.

**Action: reject.** Keep the scorer, direction and self-report defects as counterexamples.

### 9. mareforma/mareforma

**Identity:**

- Node `R_kgDORwZcfA`. HEAD `e7ae9c718adc8bde0ddd824a620d3ded4dcf5756` (2026-09-10). Created 2026-03-25.
- Licence MIT. Release v0.4.0 (2026-09-10). Pre-1.0.
- PyPI releases via Trusted Publishing, according to SECURITY.md (Reported). Typosquat names are reserved.

**What it is.** A local-first Python library in which AI-scientist findings become **signed claims in a graph**, with trust *read from the graph, not declared*. The pieces:

- **Observer.** `mareforma diagnose -- python run.py` and `observe(cites=...)` wrap the `requests`, `httpx`, `aiohttp`, `io.open`, `pandas` and `polars` seams. They compute `GROUNDED` (the cited data was actually read), `UNGROUNDED`, or `OPAQUE`. The observer returns `OPAQUE` when a subprocess, thread or unobserved-I/O seam hides the read. Unknown receipt states also degrade to `OPAQUE`.
- **Trust layer.** A content-addressed `Proposition` bound to a **pre-registered prediction**. A computed **bearing** (supports, refutes or neutral) comes from an `EffectEstimate` whose inconsistent CIs or p-values are refused. A `Status` counts independent lines, where independence means a distinct signer and a distinct `data_id`. The doc names cross-model error correlation as an unmodelled residual.
- **Signing.** Ed25519 signing. Sigstore-Rekor public log is optional.
- **MCP server.** Read and verify only.

**Human gates.** The library records, and the humans are the signers and validators. The first key on a fresh project auto-enrols irrevocably as root validator.

**Hallucinated citations.** It targets exactly this case. Its README shows an empty corpus, with the model answering from memory and inventing a citation: that run is recorded as `UNGROUNDED` with `reads: 0`. **Limit:** `GROUNDED` means the file was read, not that its content supports the finding.

**Evidence.** Examples and tests exist. Grounding prevalence pilots are mentioned. Independent evidence: none.

**Models, APIs and cost:** Six light dependencies. Local SQLite. Network only for the optional Rekor or ClawInstitute adapters.

**Safety:**

- The signing key sits at `~/.config/mareforma/key`.
- The optional public log is a **publication**. It must stay off for 0.8.0.
- By its own statement it is a library, not a sandbox.

**Maintenance (observations):**

- 4 contributors: felipeyanez 351, "claude" 69. A single-maintainer bus factor.
- 15 stars.
- 100 commits between 2026-08-10 and 2026-09-10.

**Fit:**

- (b) Strongest. The trainer's eval harness is a Python process, so the observer can show that the confirmation split was actually read and not a stale or fallback file. The pre-registered prediction and computed bearing mirror incumbent–challenger acceptance.
- (a) Limited. Patrol reading happens through agent tools (WebFetch, `gh`), outside any Python observer, so it would record `OPAQUE`. Only scripted collectors such as `refresh.py` could be observed.

**Action: pilot.** Run it locally on a synthetic trainer fixture, with no public log, after maintainer approval.

## Awesome-AI-Scientist triage

497 entries were parsed from the README at `bad5e3c`, in `research/080/tmp/autoresearch-listed/awesome_entries.tsv`. The section counts match the README badges.

| Category (count) | Relevance to us | Pulled out |
|---|---|---|
| End-to-End AI Scientists (35) | (b) loop designs; mostly ML-engineering search | AIDE `WecoAI/aideml` (MIT); AIRA-dojo `facebookresearch/aira-dojo`; MLGym. Search operators for the trainer loop: watch. |
| Co-Scientists & Research Agents (27) | (c) literature QA | PaperQA2 `Future-House/paper-qa` (Apache-2.0, active 2026-09-22): watch for ExoPO related-work QA. |
| Open-Source Workbenches (64) | (a), (b) | karpathy/autoresearch (evaluator outside the write set; see below). ARIS `wanshuiyin/Auto-claude-code-research-in-sleep` (MIT; cross-model reviewer loops). AutoSOTA `tsinghua-fib-lab/AutoSOTA` ("papers included only when the internal ledger marks optimization successful", Reported): watch. |
| Surveys & Position Papers (38) | (c) ExoPO related work and counter-positions | 2502.02649v3, 2509.08713v2, 2601.03315v1, 2605.27905v2, 2506.20803v1, 2607.27191v2, 2608.14667v1, 2608.05179v1 (metadata verified; not read) |
| Research Stages: peer review & verification (15), writing (15), literature (12), experimentation (8), ideation (19), knowledge (3) | (c) critique | BadScientist 2510.18003v2; SPOT 2505.11855v1; "Do LMs know when they're hallucinating references?" 2305.18248v3; AAAI-26 AI review pilot 2604.13940v1; "Gaming AI-assisted peer reviews" 2606.10159v1; PaperOrchestra 2604.05018v1 |
| Benchmarks: research automation (16), coding (11), reproducibility (8), literature (14), ideation (4); plus 9 general and 23 domain | (b) evaluation design; (c) citation | CiteME 2407.12861v2; FLAWS 2511.21843v1; CoCoReviewBench 2605.07905v2. Reproducibility benches as trainer-eval references only. |
| Leaderboards (5) | none | Note: Papers With Code is listed as shut down (Reported). |
| Domains (60), Foundation models (14), Datasets (55) | none now | none |
| Safety, Ethics & Policy (20) | (c) venue and route | **arXiv CS review/position-paper policy (official blog 2025-10-31; body fetched)**; REFORMS; "Leakage and the Reproducibility Crisis" 2207.07048 (older). |
| Tutorials/Blogs (19), Related lists (3) | none | none |

**Pulled items at README depth.**

- **karpathy/autoresearch.** Node `R_kgDORgZXsw`, HEAD `228791fb` (2026-03-26), **no licence**. 96,651 stars (observation only).
  - **Contract (README, program.md).** `prepare.py` holds the data prep and evaluation and is "not modified". The agent edits only `train.py`. Each run gets a fixed 5-minute budget, one metric (`val_bpb`), and a `results.tsv` log with keep, discard or crash.
  - **Defect: keep rule.** A run is kept "if val_bpb improved (lower)" by any margin, on the same validation set every time, with no noise margin and no confirmation split. That is search, not confirmation.
  - **Defect: permissions.** The README says to run the agent with "all permissions disabled".
- **Anti-Autoresearch** (`wanshuiyin/Anti-Autoresearch`). Node `R_kgDOTFlgyg`, HEAD `f3ed7577` (2026-09-09), MIT. It is linked from ARIS, not listed directly.
  - Reviewer-side integrity forensics:
    - a span-anchored, hashed evidence ledger;
    - LLM auditors that only *propose* findings;
    - a rules-only reporter;
    - 46 integrity patterns, including numeric self-consistency, baseline integrity, citation integrity, and eval-design validity (leakage, LLM-judge validity, selective reporting);
    - AI-style impressions quarantined at zero verdict weight;
    - "criticals must state ruled-out innocent explanations".
  - All of this is Reported design, with no independent evaluation.
  - The quickstart needs `codex mcp-server`. The ARIS README says codex-cli 0.154.0 removed that entry point, so the setup may be stale. Verify before a pilot.

## Cross-cutting mechanisms

Good patterns to borrow. Each has a mechanism and a falsifier.

1. **Keep the evaluator outside the agent's write set.**
   - Sources: karpathy `prepare.py`; FAROS manifest hashes of the eval code. InternAgent is the counterexample.
   - Mechanism: a candidate cannot improve its score by changing how the score is computed.
   - Falsifier: a candidate diff that touches the eval or split files still gets scored.
2. **Freeze the manifest and refuse on drift.**
   - Sources: FAROS `freeze_experiment.py`; CoAutoResearch `plan_sha256` binding.
   - Hash the data splits, eval code, config and git state. A resume against a changed fingerprint fails closed.
3. **Denominator honesty.**
   - Source: FAROS reports precision as `null` when gold labels are non-exhaustive, instead of treating unlabelled findings as correct.
   - This directly suits the trainer skill's synthetic-label audits.
4. **Resample by the real independent unit.**
   - Source: FAROS bootstraps by source paper.
   - This matches existing Augustus doctrine ("cluster repeats by their real independent unit"). It confirms the doctrine; it is not new.
5. **Ordered stop statuses with a one-question human escalation.**
   - Source: CoAutoResearch.
   - `paused_budget` and `blocked(recovery_condition)` are distinct from `no_viable_line`, and `needs_human` carries exactly one question.
6. **Completion is not substitutable.**
   - Source: DARE v4 invariant 5.
   - Timeout, budget exhaustion or an empty agent result never completes a stage.
   - This is the same rule as `maintenance.md`'s "fetch success must not advance last completed review", stated as a runtime invariant.
7. **Computed, not declared; unknown degrades to OPAQUE.**
   - Source: mareforma.
   - The verdict is derived from observed reads, or from a pre-registered rule plus the estimate. Absence is trusted only where the observer can see.
8. **Closed-world citations.**
   - Sources: FAROS outline prompt; scholaraio's three states.
   - This must be strengthened: resolve every reference by identifier, match the title, and check claim support separately. The InternAgent BibTeX ID collision is the concrete failure an author–year check misses.
9. **Proposers are not deciders.**
   - Source: Anti-Autoresearch (Reported design); ARIS uses cross-model reviewers.
   - LLMs propose findings and a rules-only step adjudicates. "Effective independence" means a same-model reviewer counts as one line of evidence, not two (mareforma states the same).

Bad patterns to avoid.

1. **A deterministic gate over agent-attested booleans** (CoAutoResearch `GATE_EVIDENCE.json`). `budget_reached` should come from a meter, not from the agent.
2. **Fail-open human gates** (FAROS). A missing approval `status` counts as approved, and a baseline "human" provider returns canned success.
3. **Direction-agnostic averaging of relative changes, self-reported metrics, and single-run acceptance** (InternAgent). There is also a config marking an MSE as higher-is-better.
4. **Strict-improvement keep on a reused validation set** (karpathy/autoresearch). Selection noise and winner's curse; there is no confirmation split.
5. **Overstated verification labels** (scholaraio `VERIFIED` means author plus year).
6. **Unpinned supply chain and remote-instruction installs** (ToolUniverse `uvx --refresh` and `setup.md`; DARE `npx @latest`).
7. **Silent host-execution fallback** (FAROS subprocess backend, on by default in the "development" role).
8. **Hosted search leaks the research agenda** (DARE's MCP set). For 0.8.0, any hosted-search autoresearch tool is a confidentiality leak.
9. **Gameable activity signals.** swarm-factory's bot commits and FAROS's 99-issue day show that commit cadence, issue counts and stars can be manufactured.

## Implications by target

### (a) Patrol and fold automation

**Scheduler gap.**

- Unchanged by this review. No tool here provides owner, next-due, last-successful-collection or last-completed-review receipts (see `maintenance.md`).
- A host scheduler plus a named owner is still required. Examples: a Claude Code scheduled routine, launchd, or cron.
- GitHub Actions is ruled out while 0.8.0 stays off GitHub.

**Borrowable, all Hypothesis:**

- Give every scheduled run a status drawn from `{completed_review, no_change_probe, paused_budget, blocked(recovery_condition), needs_human(one question), failed}`. A metered budget sets `paused_budget`; the agent does not declare it.
- Make receipts append-only.
- Emit fold output as a fixed delta: findings, evidence_updates, uncertainties, decisions, open_questions. This mirrors DARE's `ResearchStateDelta` and fits `protocol.md`'s per-finding template.
- **Falsifier:** status-bearing receipts still get summarised as "up to date" while the review is missing.

**Where observers stop.** mareforma-style grounding can receipt only Python collectors (`refresh.py`). Agent WebFetch or `gh` reading would be `OPAQUE`. Do not claim "grounded fold".

### (b) Trainer skill loop

These add to the current `optimizer-integration.md` loop; they do not replace it. That loop already separates search from confirmation and bundles `compare_workflows.py` with a Hoeffding/union bound.

- Put the evaluator, the splits and the metric-direction table outside the candidate's write set. Hash them into a frozen manifest and refuse on drift.
- Log every trial as keep, discard, crash or `no_viable` in a results ledger, and preserve failed trials.
- Declare metric direction per metric, and test it.
- Never average relative changes across metrics. Acceptance is the pre-registered paired rule on untouched confirmation units.
- Make "don't train" and `no_viable_line` / `paused_budget` first-class terminal statuses with recorded reasons.
- **Counterexample tests to write** (fixtures, not doctrine):
  - a lower-is-better metric that rises must score as a regression;
  - a candidate that edits the eval code or split files must be rejected;
  - a strict-improvement keep on the reused search set must be labelled search, not confirmation;
  - an approval record with no status must fail closed.
- **Sandbox reference.** Use FAROS's Docker flags (`--network none`, `--cap-drop ALL`, `--read-only`, `no-new-privileges`, resource limits), with no silent host fallback.

### (c) ExoPO paper

**Critique:**

- Pilot Anti-Autoresearch locally on our own draft, after checking the codex bridge.
- Use FAROS's six ReviewX support states as the claim-audit vocabulary.
- Resolve every reference by identifier through the arXiv API or DOI.

**Case-study idea (Hypothesis).** Autoresearch systems are acting agents whose keep, stop and publish decisions are exactly the policy ExoPO asks about. On this list:

- the better designs keep that policy exogenous: a fixed evaluator, a truth-table gate, computed bearing;
- the weaker ones let the model author its own metric or approval (InternAgent, FAROS stubs, the CoAutoResearch signal inputs).

This could supply a concrete test domain for the paper's "when should policy be exogenous" criterion. It would need a controlled comparison, not these anecdotes.

**Route.** The arXiv CS policy (Contract, official blog, retrieved today) requires peer-review acceptance documentation for position papers. It is a 2025 post, so recheck the live policy page before choosing a venue, framing or category.

## Open questions for the maintainer

1. Who owns the patrol scheduler, and on what host, while 0.8.0 is off GitHub? That means a Claude Code routine, launchd, cron, or something else. Which receipt fields will it emit?
2. May I run local pilots of mareforma (synthetic trainer fixture, no Rekor or public log) and Anti-Autoresearch (our draft only)? Both mean running third-party code. Which sandbox?
3. ExoPO route under the arXiv CS rule: venue acceptance first, a research-paper framing with experiments, or another category?
4. Should swarm-factory be reported to GitHub abuse? That is an external action needing your authority.
5. Confirm there are no hosted or paid search MCPs for 0.8.0 autoresearch tooling. I recommend none, on confidentiality grounds.
6. Is borrowing *ideas* from unlicensed FAROS and karpathy/autoresearch acceptable, provided no code is copied?

## Not covered

- Nothing was executed or reproduced. All behaviour claims are source-read at the recorded SHAs.
- Reported benchmark numbers were not verified: FAROS SciFact, InternAgent/MLEvolve, AutoSOTA, ToolUniverse tool counts.
- Full source was not audited in several places:
  - CoAutoResearch `server.py` (about 23k lines) was grepped only;
  - the FAROS frontend and most backend services were not read;
  - DARE was sampled at 3 of 267 skills;
  - ToolUniverse's 1,000+ tools were not audited;
  - scholaraio's ingest and fetch stack was not read.
- The Awesome list was triaged by title and category. About 20 entries were checked at metadata depth and 3 at README depth. The paper full texts were not read: arXiv API metadata only.
- PyPI provenance attestations (mareforma, ToolUniverse) were not checked.
- The swarm-factory Pages site and its redirect target were not visited. The redirect domain appears only in the local decoded file.
- The CoAutoResearch `pushed_at` versus HEAD date gap is unexplained.
- arXiv metadata anomaly: 2608.05179v1 shows `published` 2026-06-29, before its ID month. Unverified.
- I did not coordinate with the other 0.8.0 lanes. The arXiv position-paper policy may duplicate a paper-lane finding.

## Raw packet

All under `research/080/tmp/autoresearch-listed/`:

- `meta_*.json`, `commits_*.json`, `contrib_*.json`, `rel_*.json`, `tags_*.json`: GitHub REST metadata.
- `src/<owner>_<repo>/`: shallow clones, read only.
- `awesome_entries.tsv`: the parsed list.
- `swarm_index_decoded.txt`: the statically decoded lure page.
- `karpathy_*.md`, `README_*.md`: README-depth fetches.
- `arxiv_batch.xml` (sha256 prefix `f79c8a322dcee543`).
- `arxiv_blog_position.html` (sha256 prefix `78d261bced41d3a4`).

## Sources

| # | Canonical ID | URL | Revision | Retrieved (UTC) | Depth |
|---|---|---|---|---|---|
| 1 | github:OpenNSWM-Lab/FAROS (R_kgDOScPUtg) | https://github.com/OpenNSWM-Lab/FAROS | 4e4e96fde842ced39b5bfd805b5666b4ce7cca0e | 2026-09-23T17:02:41Z | README + key source (runtime providers, sandbox, reviewx_eval, SciFact results); issues page 1 |
| 2 | github:ZimoLiao/scholaraio (R_kgDORimTkw) | https://github.com/ZimoLiao/scholaraio | c3a4b2656b2018fb372ae63a7256c61956e4ea50 | 2026-09-23T17:02:45Z | README, STRATEGY, config, hooks, citation_check source + skill |
| 3 | github:yogsoth-ai/de-anthropocentric-research-engine (R_kgDORMuzGQ) | https://github.com/yogsoth-ai/de-anthropocentric-research-engine | cbc38aa2466d209a592710b0e09304bbdef98696 | 2026-09-23T17:02:47Z | README, v4 architecture + runtime-boundary docs, mcp.example.json, 3 SOPs |
| 4 | github:Omni-Scientist/Awesome-AI-Scientist (R_kgDOUCwsyA) | https://github.com/Omni-Scientist/Awesome-AI-Scientist | bad5e3cd71a502433bd53a16b05e2a6976923232 | 2026-09-23T17:02:48Z | Full README parse (497 entries), CONTRIBUTING, LICENSE |
| 5 | github:Usaid22/swarm-factory (R_kgDOS7EfgA) | https://github.com/Usaid22/swarm-factory | 3f310cffb90811023a8e2783d5c207e07905a7e8 | 2026-09-23T17:02:49Z | All 6 files; index.html statically decoded; Pages site not visited |
| 6 | github:YihongT/CoAutoResearch (R_kgDOS7557Q) | https://github.com/YihongT/CoAutoResearch | ecbdf464f9140ebd199c69250a7df3050ee42a6c | 2026-09-23T17:02:53Z | README, gate docs + truth table, v2_gate.py, runtime gate signals, permission presets |
| 7 | github:mims-harvard/ToolUniverse (R_kgDOOCnxVw) | https://github.com/mims-harvard/ToolUniverse | c0b9b71c843df285865eb96c283a5e06eb3ea58e | 2026-09-23T17:02:58Z | README, base_tool cache versioning, cache backend, arXiv tool spec |
| 8 | github:InternScience/InternAgent (R_kgDOOrCg_Q); aliases Alpha-Innovator/NovelSeek, Alpha-Innovator/InternAgent | https://github.com/InternScience/InternAgent | fa8c3eedfa9751d3752ea6eb49220b303ac2397d | 2026-09-23T17:03:02Z | README, stage.py scoring, experiments_utils_claude.py, metric_config.json, vendored-code count |
| 9 | github:mareforma/mareforma (R_kgDORwZcfA) | https://github.com/mareforma/mareforma | e7ae9c718adc8bde0ddd824a620d3ded4dcf5756 | 2026-09-23T17:03:03Z | README, SECURITY, concepts (grounding, findings), observe/_verdict.py, pyproject |
| 10 | github:karpathy/autoresearch (R_kgDORgZXsw) | https://github.com/karpathy/autoresearch | 228791fb499afffb54b46200aca536f79142f117 | 2026-09-23T17:10:35Z | README + program.md; licence endpoint 404 |
| 11 | github:wanshuiyin/Anti-Autoresearch (R_kgDOTFlgyg) | https://github.com/wanshuiyin/Anti-Autoresearch | f3ed7577beaff9c44280f8fcddcfce0e51a6292d | 2026-09-23T17:11:08Z | README (first ~90 lines) |
| 12 | github:wanshuiyin/Auto-claude-code-research-in-sleep (R_kgDORjDgTA) | https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep | 341f914024d270dc5c8fa51337d1ad38829273aa | 2026-09-23T17:10:53Z | README grep (release notes, reviewer bridge) |
| 13 | github:tsinghua-fib-lab/AutoSOTA (R_kgDORxpYdg) | https://github.com/tsinghua-fib-lab/AutoSOTA | d39ac9e03cf999589be196f06a26cc8449bb3031 | 2026-09-23T17:10:54Z | README grep (ledger claim; Reported numbers) |
| 14 | Metadata only: WecoAI/aideml (R_kgDOLpUc1w), facebookresearch/aira-dojo (R_kgDOO8m36w), facebookresearch/MLGym (R_kgDON7rjyw), Future-House/paper-qa (R_kgDOI55lCg), bethgelab/CiteME (R_kgDOMH94Gw), guijinSON/SPOT (R_kgDOObnKRQ), Omni-Scientist/OmniScientist (R_kgDOT6KSJA), ai4s-research/open-science (R_kgDOTMbi4g), K-Dense-AI/scientific-agent-skills (R_kgDOQFcxuA), SakanaAI/AI-Scientist-v2 (R_kgDOOV2Kmw), allenai/asta-bench (R_kgDOOMoxmA), InternScience/MLEvolve (R_kgDORQT4cQ), HKUDS/AI-Researcher, UniPat-AI/UniScientist, gomesgroup/coscientist | https://github.com/<id> | default-branch metadata (pushed_at, licence) | 2026-09-23T17:05–17:13Z | metadata |
| 15 | arXiv (API batch, sha256 prefix f79c8a32): 2509.23426v3, 2505.16938v3, 2602.08990v1, 2510.08521v2, 2608.05179v1, 2509.08713v2, 2510.18003v2, 2605.27905v2, 2601.03315v1, 2506.20803v1, 2407.12861v2, 2305.18248v3, 2505.11855v1, 2511.21843v1, 2605.07905v2, 2502.02649v3, 2502.13138v1, 2507.02554v2, 2604.13940v1, 2606.10159v1, 2608.14667v1, 2605.20025v2, 2608.13558v1, 2607.27191v2, 2502.14499v1, 2604.05018v1 | https://export.arxiv.org/api/query?id_list=… | versions as listed | 2026-09-23T17:12:18Z (first two attempts: empty body, then HTTP 429) | metadata (title, authors, dates, category) |
| 16 | arXiv blog: "Attention Authors: Updated Practice for Review Articles and Position Papers in arXiv CS Category" (Kat Boboris, 2025-10-31) | https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category/ | mutable page; sha256 prefix 78d261bced41d3a4 | 2026-09-23T17:12:37Z | body text (first ~3.5k chars) |
| 17 | Augustus repo evidence reused | research/protocol.md, research/maintenance.md, research/prompts/research-fold.md, .agents/skills/augustus/references/optimizer-integration.md, research/sources.json, research/notes.md (grep); scratchpad wf1-patrol-*.json summaries | working tree at 4236a60 | 2026-09-23T17:00–17:14Z | read / grep |
