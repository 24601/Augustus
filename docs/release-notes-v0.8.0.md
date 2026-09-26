---
title: "Augustus v0.8.0: build and improve your own task specialist"
description: "Two agent skills for decision-system design and application-specific data assembly, model selection, training, export and bounded improvement."
permalink: /release-notes-v0.8.0.html
---

# Augustus v0.8.0

Released 2026-09-26. Augustus now ships two skills: `augustus` for designing
and evaluating decision systems, and `augustus-train` for building and improving
an application-specific component from data to reloadable inference.

## What you can ask it to do

- Choose decision primitives, feasible base models and training methods under
  your application's error costs, latency, compute and data constraints.
- Assemble data with provenance, adjudicate ambiguous labels, and separate
  development from confirmation without overlooking group or time leakage.
- Fit a task specialist, export it, reload it in a fresh process, and keep
  prediction, abstention and downstream action policy distinct.
- Run bounded improvements to data, models or programs. Compare with the
  incumbent on independent evidence; retain rules or no model when they win.

The trainer includes a runnable CPU classifier recipe. It guides an agent using
your application's tools; it is not a hosted trainer or a pretrained model.
Provider-output training still requires permission under the provider's terms.

## What was executed

Fresh agents completed three journeys, then the coordinator replayed them:

- **Binary classification:** three real CPU fits and bounded policy selection;
  group-weighted cost 0.023857 versus 0.107356 for always-ham on a public SMS
  proxy. All 1,025 fresh-process inference rows matched.
- **Multiclass routing with review:** 150 intents plus out-of-scope examples,
  three fits and 72 policies; cost 0.117966 versus 0.3 for always-review.
  All 5,477 fresh-process rows matched.
- **No training:** exact-rule routing with six correction, failure and
  fresh-process tests, plus seven separately reviewed advisory responses.

See the [replayable acceptance audit](https://github.com/24601/Augustus/tree/v0.8.0/research/audits/2026-09-26-trainer-journeys)
for source identities, dependencies, recipes and limitations. Repository checks
passed 190 tests plus numerical self-tests. Installation checks covered both
skills, not implicit activation in a crowded skill inventory.

These are public-proxy and fixture results, not production effectiveness or
proof that the skill beats an unassisted agent. The multiclass corpus has
near-duplicate and unknown-family dependence; its statistical bound is not clean
population evidence. The binary refit matched behavior, not serialized bytes.
This is not a recipe for reproducing a general instruction-conditioned Jev.

## Upgrade

For Claude Code, remove an older pinned marketplace, then reinstall:

```bash
claude plugin marketplace remove augustus
claude plugin marketplace add 24601/Augustus@v0.8.0
claude plugin install augustus@augustus
```

For Skills CLI agents, install both skills:

```bash
npx skills add https://github.com/24601/Augustus/tree/v0.8.0 --skill augustus augustus-train
```

For manual installs, copy both directories under `.agents/skills/`, including
their references and scripts. The trainer uses helpers from its companion.
No existing entry point was removed. No model download, paid call or deployment
is performed by installation.

Earlier release: [v0.7.2]({{ '/release-notes-v0.7.2.html' | relative_url }}).
