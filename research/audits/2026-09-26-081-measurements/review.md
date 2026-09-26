# VibeProxy pilot: coordinator acceptance

The owner requested VibeProxy after the initial OAuth failure. The existing
[Mac worker](https://ampcode.com/threads/T-01a0e004-e968-756f-aa39-f8779789998d)
completed the unchanged eleven-case pilot: **22 agent runs, $1.3384598 reported
cost, no censoring**. No additional inference was authorized or run afterward.
The [worker receipt](vibeproxy/README.md) contains full methods and limitations.

## Independent checks

The coordinator downloaded the archive with SHA-256
`0f04e68fc62266be372f1799646230b0f764c8cd2e0f599715f6cd91d9ea6a32`,
verified its complete manifest, compared every archived release skill file with
the tagged Git object, and checked all 30 suite hashes against the pre-run
committed inventory. Parsed all 22 traces independently: one completed run per
arm/case, no final error, no MCP server, same reported agent model, and exactly
the two Augustus skills added to the with-plugin inventory. Successful Skill
results match call IDs; the trainer-positive trace contains the loaded body and
the data-and-splits reference read. No baseline made a Skill call.

Recomputed semantic outcomes excluding tool/activation graders: **eight pairs
pass in both arms**, none pass only in one arm, and three pairs lack semantic
graders. Recomputed costs from original `costUsd` fields: $0.7612742 with skills,
$0.5771856 without. Those fields already include judge costs; adding
`judgeCostUsd` again would double count. The 31.9% difference is descriptive,
cache/order-confounded, and based on list-price estimates, not a reconciled bill.

| Predeclared activation subset | Successful loads |
| --- | ---: |
| Exact trainer positives | 1/2 |
| Main-skill positives | 2/3 |
| Either skill on negative prompts | 0/5 |

`fit_budget` loaded Augustus, not Augustus Train. `ranker_gate` loaded neither.
`fit_economics` remains excluded from activation recall because its interpretation
was marked ambiguous before inference. These small fixed-case counts are not
population recall or false-positive-rate estimates.

## Green grading is not acceptance of the answers

Directly checked the disputed answer passages and independent arithmetic:

- The with-plugin fit plan requests **24 examples per class inside held-out
  five-fold CV**, although only 24 exist in total. Its learning-curve endpoint
  is infeasible. Both arms also falsely treat reviewer agreement as a universal
  accuracy ceiling. A decreasing or flat empirical learning curve does not prove
  that more data or another model cannot help.
- Both economics answers get the requested costs and integer break-even right.
  The with-plugin answer adds a wrong cost-ratio crossover. With FP cost 1 and
  FN cost c, fitted minus zero-shot error cost is **5c − 55 per 1,000**; the
  crossover is 11, not 5.5, and fitted is cheaper below it. Exact rational checks
  confirm the original 5,000-decision winner and both sides of 13,334. Neither
  answer loaded a skill here, so this is not a demonstrated skill-content effect.
- The baseline employee-training rewrite adds two commentary sentences despite
  the one-sentence request. All three judge votes still passed it.
- The trainer-loaded data answer has useful provenance/confirmation details.
  The baseline's suggested forbidden-feature probe is not a valid test that
  those features leaked into the actual deployed pipeline. This one pair is a
  useful hypothesis, not proof of overall improvement.

The graders were too broad or permissive to detect these failures. We retain
their original results rather than retroactively changing scores or prompts.
Worker and coordinator review were **not blinded**, contrary to the original
plan's blind-pair review step; these observations are therefore diagnostic and
not a new unbiased better/same/worse endpoint. No comparative quality win is
accepted from this run.

## Execution deviations and next decision

Mac Claude Code was **2.1.282**, versus the plan's orb **2.1.283**. This is an
explicit host-version deviation, not an exact harness replication. VibeProxy's
normal fallback settings were not changed; a disposable instance reused its
existing server-side auth with retries and preview/project fallback disabled.
That instance was stopped after the run. Normal configuration was preserved.
All agent responses reported the requested model, but proxy names are not
independent backend attestation. Raw judge identity was not separately observed.

**Conclusion:** activation works selectively; no overall advice-quality benefit
has been demonstrated. Do not strengthen the release claims or rerun these same
easy graders until a positive result appears. The next useful measurement is a
new, frozen set of executable data/fit/serve tasks with independent arithmetic,
feasibility and policy checks, matched no-skill baselines, counterbalanced order,
and protected task families. Investigate the trainer-routing miss separately;
any instruction change belongs to a new development version, not the published
0.8.1 tag. More repetitions of the current permissive rubric would not fix its
measurement weakness.

The `vibeproxy/` directory preserves the sanitized archive unchanged, including
raw answer/trace evidence, original grades, routing metadata, frozen inputs and
hashes. No credentials, auth directories or unsanitized proxy logs are included.
