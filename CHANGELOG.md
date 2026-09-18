# Changelog

## 2026-09-18 (refresh pass 2)
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

## 2026-09-17/18 (initial)
- Baseline research archive (sources.json, notes.md), augustus skill with
  mappings + validation references, evaluator script, hourly refresh script,
  Claude plugin marketplace manifest.

## 2026-09-18 (topic-index pass 3)
- Fixed census method: exact GitHub search paginated (700 repos created since
  09-14 captured; 700-result cap noted) + topics/jev crawl → ~80 additional
  repos; archive now 184 clones. Miss-cause documented: earlier star-sorted
  limit-40 search cut the low-star tail (incl. both MCTS repos).
- Skill: MCTS mapping promoted experimental → empirical recipe (grounded vs
  speculative fidelity in types; probes-only concession; measured 24/24 vs
  1/24 greedy); agent-self-assessment.md gains the judge-variance recipe
  (Jev judge 224-279x more consistent than LLM judge over 100 reps).

## 2026-09-18 (pass 4 — optimizers + official skills + clone audit)
- ax Jev support documented from source (native adapter details, trueThreshold
  semantics, fail-closed mapping validation); new reference
  optimizer-integration.md covering Ax + DSPy typesafeify + jev-dspy-lab.
- typesafeainate/dspy-typesafeify cloned; official typesafe-ai/skills already
  archived and layered-on (never duplicated).
- Clone audit: repos.txt deduped (185 unique), 0 missing on disk, no failures.

## 2026-09-18 (pass 5 — toolbox sweep meta-method)
- New references/toolbox-mapping.md: the how-to-find-approaches-and-
  applications procedure (judgment-shaped-hole substitution, newly-feasible
  classification via economics inversion, standing rejections list); wired
  into SKILL.md central model + index row.

## 2026-09-18 (pass 6 — named-methods + operators/theorems tier)
- references/methods-catalog.md: ~20 named algorithms (CatBoost row is
  Empirical via autoresearch cookbook) + operators/theorems tier with
  precondition-carrying rule; wired into SKILL.md index and toolbox sweep.
