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
option-order shuffle; **irrelevant-option / IIA** (append an option that
should not move odds among the rest — Hume's reconstruction,
`research/notes.md` §31, not a new invariance the API promises);
public cousin for the read-the-letter graph:
[`Mikhail/mini-jev-runs`](https://huggingface.co/datasets/Mikhail/mini-jev-runs)
`read_letters_rotated_options` (scores not calibrated; `notes.md` §33);
**paraphrase pairs** (semantically equivalent
wording — does p swing enough to change the *act*? `mappings.md` §17);
irrelevant distractor injection in state; no-match and
empty-evidence cases; policy-boundary cases just above/below thresholds;
contradictory-output handling (operation says X, target says Y).

## Offline eval: selective binary decisions

Run `scripts/evaluate_decisions.py` on application-exported JSONL
(`{id, p, y, group}` + optional baseline `p_base`, costs). It reports Brier
score, reliability bins with counts, and coverage/FP/FN/cost across
thresholds. Rules: select thresholds on split A, report final numbers on
split B; no universal pass mark; missing labels/costs → stated limitation,
never invented defaults. Ranking/search metrics stay checklist-level until a
real application justifies executable support. A complementary labeled-case
workbench for running Jev questions (Noul / Choice / Score) and comparing
runs is [dayhaysoos/jevals](https://github.com/dayhaysoos/jevals) (MIT,
local; WebMCP + agent skill; not affiliated with TypeSafe) — the empirical
acceptance-test *surface* for Hypothesis mapping cards; this script remains
the offline Brier / reliability / cost evaluator. Pointer only
(`research/notes.md` §24); Augustus is not a jevals how-to. Same
acceptance-test *surface*, different UI:
[jeiel85/jevscope](https://github.com/jeiel85/jevscope) (local-first
visual debugger + JSONL regression; policy buckets are JevScope-derived,
not Jev answers). Pointer only; do not copy ports or env into skill cards.

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

## Threshold non-transfer (Empirical, FirasSX914/calibre)

Calibration and routing thresholds measured on one dataset do **not** transfer to
another — and neither does routing's ROI. calibre: Banking77 Jev→DeepSeek route @0.67
gives 80.2% at $0.103 vs Jev alone 77.8%@$0.051; on Web of Science the same routing
ties Jev alone (52.8% both) for 46% more money. The optimal threshold, the sign of
the model gap, and whether routing pays at all all flipped. Rule: every gate/threshold
is a per-dataset measurement, not a constant. Re-measure on your data before shipping
and re-measure when the distribution shifts; treat any borrowed threshold as a prior,
never a setting.

## Shadow mode before gating

Adoption pattern (AntonioCoppe/jev-harness): run the Jev judgment in parallel with
the live system and only **log what you would have done** (policy + gate applied)
until behavioral evals over replayed fixtures pass; then flip to enforcement. Assert
on the *action* (block/warn/pass), not on free text. This is the safe path for any
confidence gate added to an existing pipeline.

## Frontmatter (by agents and by Jev rankers)

- `name`: gerund, hyphenated, matches directory; specific over clever.
- `description`: third person, what + when, with the trigger terms users
  and rankers actually emit (e.g. name the primitives: Choice, Score, Noul;
  name the jobs: routing, reranking, verification, decomposition).
- Write descriptions like Choice criteria: `what` it covers, `not_for` its
  neighbor, examples of triggering requests. Distinct descriptions are a
  retrieval feature — the skill_suggestion cookbook shows lookalike
  descriptions are the top failure source.
