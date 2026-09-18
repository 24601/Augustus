# Validation: the design gate, eval recipes, and Jev-for-skills

## The gate (run before building)

1. Exact computation, semantic judgment, or both? Exact parts stay in code.
2. Can the right answer be represented? (candidate present? level exists?
   `other` option where coverage is open?)
3. Missing / contradictory / malicious / stale evidence — what happens?
4. Which constraints must code enforce regardless of model output?
5. What does each number mean — and which reading would be invalid?
6. Baseline + labeled cases + held-out split defined before tuning?
7. Rubric design, threshold selection, and final evaluation on separate data?
8. What triggers reevaluation? (model, rubric, source, or policy change.)

## Behavioral tests (measure; Jev promises no invariances)

Candidate removal (drop the winner — does probability spread sensibly?);
option-order shuffle; irrelevant distractor injection in state; no-match and
empty-evidence cases; policy-boundary cases just above/below thresholds;
contradictory-output handling (operation says X, target says Y).

## Offline eval: selective binary decisions

Run `scripts/evaluate_decisions.py` on application-exported JSONL
(`{id, p, y, group}` + optional baseline `p_base`, costs). It reports Brier
score, reliability bins with counts, and coverage/FP/FN/cost across
thresholds. Rules: select thresholds on split A, report final numbers on
split B; no universal pass mark; missing labels/costs → stated limitation,
never invented defaults. Ranking/search metrics stay checklist-level until a
real application justifies executable support.

## Jev for agents and skills (dogfooding)

- **Skill routing**: for large rosters, copy the skill_suggestion shape — one
  request ranks all skills (Choice over index descriptions) plus gate nouls
  for whether any skill fits; a second request reranks the top-3 with full
  descriptions and per-candidate fits-nouls that may reject all. Suggest at
  most one skill; keep the suggestion overridable so prefix caching holds.
- **Self-monitoring tool calls**: after an agent acts, ask decomposed Nouls
  over {request, tool schema, trace}: right tool? arguments match schema?
  result matches call? units/dates verified in code? Escalate on low
  confidence, never auto-retry blindly.
- **Grounding/citation checks**: one Choice (supports / contradicts /
  unrelated) per claim-evidence pair plus a confidence review flag; verify
  against source documents, never against another model's prose.
- **Testing a skill**: define the skill's decision surface (which judgments,
  which policies), build labeled cases per judgment, run the gate's
  behavioral tests, and score with the evaluator script. A skill passes when
  its card's falsifying experiment fails to reject it — not when a demo
  looks clever.
- **Modularity**: one skill per decision-design responsibility; share
  reference files instead of forking near-duplicate skills; prefer a thin
  router (rank-then-verify) over hundreds of micro-skills AND over one fat
  skill. Merge two skills when their design cards are identical except nouns.

## Frontmatter that gets chosen (by agents and by Jev rankers)

- `name`: gerund, hyphenated, matches directory; specific over clever.
- `description`: third person, what + when, with the trigger terms users
  and rankers actually emit (e.g. name the primitives: Choice, Score, Noul;
  name the jobs: routing, reranking, verification, decomposition).
- Write descriptions like Choice criteria: `what` it covers, `not_for` its
  neighbor, examples of triggering requests. Distinct descriptions are a
  retrieval feature — the skill_suggestion cookbook shows lookalike
  descriptions are the top failure source.
