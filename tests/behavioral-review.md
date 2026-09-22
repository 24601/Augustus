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
