# 0.8.1 activation and advice-quality pilot

Frozen before inference, 2026-09-26. Release under test:
[4ba9d2111d29ea03247c22b3de90bfa8dde1b261](https://github.com/24601/Augustus/commit/4ba9d2111d29ea03247c22b3de90bfa8dde1b261).
Two arms: both installed skills versus neither; same agent model, one run per
case/arm, concurrency one. This pilot checks measurement integrity and estimates
paired advice outcomes; it cannot establish general superiority.

Execution: Claude Code 2.1.283, requested agent `claude-opus-5-5`, requested judge
`claude-haiku-4-5-20251001`, explicit `--ablation with-without`, `--runs 1`,
`--max-cost-usd 3`, `--keep-temp --no-publish --no-scaffold --mocks record
--trust-plugin`. Existing OAuth credential in orb; no credential transfer.
Mac preflight found no authenticated Claude account there. No real MCP servers,
shell/write/network grants, training jobs, or automatic retries. Cost stop is
checked between launches and can overshoot by one run; report censoring.

The release has **seven**, not five, existing cases. Add the four Mac-prepared
cases unchanged, making **eleven cases / 22 agent runs**, plus graders if budget
allows. Preserve suite hashes before launching. Do not tune cases after results.

## Predeclared interpretation

- Unambiguous positive prompts: `fit_budget`, `no_match`, `ranker_gate`,
  `refund_router`, `trainer_application_data`. Exact trainer recall is measured
  on `fit_budget` and `trainer_application_data`; main-skill positives separately.
- Negative prompts: `plain_rewrite`, `provider_setup`, `train_word_nontrigger`,
  `trainer_copy_control`, `training_arithmetic_nontrigger`. Recompute both
  trainer-only and either-skill false positives from actual trace calls.
- `fit_economics` is **ambiguous activation**, excluded from positive recall:
  it asks for model comparison but supplies arithmetic that needs no judgment.
  The prepared trigger grader remains unchanged but is not authority for this
  interpretation. Its arithmetic outcome counts in paired advice quality.
- Parse successful Skill tool results, not text mentions or attempts alone.
  Require actual trainer name; distinguish direct loading from companion routing.
  Verify both arms' model identity, plugin/skill inventory and tool restrictions.
- Outcome scores exclude activation graders. Pair by task, not random seed.
  Report both succeed / with-only / without-only / neither and missing outcomes.
  The original nontrigger cases without semantic graders cannot supply an
  outcome-quality score just by avoiding a skill call.
- Review actual answers against identical task criteria; retain raw answers,
  judge findings, cost, latency and failures. Independently check economics:
  per 1,000 costs 320/175/190; at 5,000, 1600/1075/950 including fitting;
  fitted strictly cheaper than zero-shot at integer future volume 13,334.
- No population recall, training-quality, production-benefit, crowded-skill
  selection or trainer-only causal claim. Published fixture tests are regression
  evidence, not held-out evidence. A broader repeated study needs a separately
  bounded design after this pilot, not a favorable re-run of these prompts.
