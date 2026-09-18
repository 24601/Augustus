# Changelog

All notable changes to Augustus are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versioning
follows [SemVer](https://semver.org/spec/v2.0.0.html).

Each release notes the [`typesafe-ai/skills`](https://github.com/typesafe-ai/skills)
revision it was written against. That skill owns integration contracts;
Augustus owns design judgment. Re-read live TypeSafe docs before treating a
pin as current API behavior.

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
