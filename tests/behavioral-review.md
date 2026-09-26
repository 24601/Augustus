# Behavioral skill review

These scenarios test whether instructions help a capable agent make useful
decisions. They are not a model benchmark or deterministic CI assertion.
Do not score by finding exact words or matching expected prose.

Give a fresh agent the candidate skill and only the `id`/`prompt` for a
representative subset of skill_cases.json. Do not show expected notes,
prior failures, or the intended fix. Keep evaluation read-only or use an
isolated temporary directory. The coordinator assesses the returned answers.

For each response, record:

- Did it understand the desired behavior and domain?
- Was skill activation appropriate, including avoiding needless ceremony?
- Did it choose a justified pillar, placement, and family (or no model)?
- Did it separate exact work, semantic judgment, and generation?
- Did it state meaningful output semantics, evidence gaps, and assumptions?
- Did policy retain action authority, with concrete error/abstention handling?
- Was there a useful baseline, falsifier, and evaluation proportional to risk?
- Was the response concise enough to use and free of invented evidence?

Use `pass`, `revise`, or `not_applicable` for each aspect with a reason and
an excerpt/location in the actual output. A finding about authority,
probability semantics, or invented evidence blocks acceptance. A formatting
preference alone does not. Keep the prompts, outputs, reviewer identity,
skill revision or working-tree hash, and observed limitations together in
a dated audit artifact. Do not claim improved outcomes from one smoke pass.
To claim a change improves answers, also answer the affected scenarios with
the last published skill, blind the reviewer to the arm, and report
better/same/worse per scenario; a few scenarios support no significance
claim. Factual or arithmetic corrections need no comparison arm.

## Trainer scenarios and execution evidence

Use the `trainer_*` cases together with the existing `provider_distillation`
case; do not duplicate that terms/provenance scenario. In the latter, assess
whether the proposed data path excludes Jev-derived training targets, not
just whether the answer mentions terms. Renaming or mixing those targets
with human labels does not establish independent provenance. A comparator
must remain distinguishable from training supervision.

The trainer prompts exercise data preparation, constrained method selection,
cost-sensitive and open-set decisions, bounded improvement, a no-training
outcome, and export semantics. They intentionally request advice or plans,
not access to a supplied dataset. Assess concrete decisions and arithmetic;
do not demand a particular model family or reward a checklist of terms.
The copy-editing control must remain a direct rewrite even though it mentions
training and exported weights.

Record scenario construction, prose response review, and executed system
checks separately. Adding these cases or passing `make check` establishes
only offline structure, not trainer activation, successful training, or
semantic acceptance. Run candidate-skill reviews only after that candidate
exists. An execution claim additionally needs actual inputs and commands,
split/group and label provenance, run/configuration identities, observed
metrics, and a fresh-process export/reload comparison where applicable.
Mark absent execution evidence as not run rather than inferring it from a
plausible plan. Use synthetic or authorized redacted data for execution.

The plugin-eval trainer trigger requires the exact `augustus-train` skill,
including namespaced calls; loading only Augustus does not satisfy it. Inspect
the kept trace too, including any routing from Augustus. Its behavioral grader
judges the data plan, not training success. The trainer copy control rejects
activation of either skill.
Keep the existing with/without-arm and spend safeguards in CONTRIBUTING.
