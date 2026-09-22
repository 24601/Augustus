# Augustus

Find, build, evaluate, and improve systems with decision models.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/24601/Augustus)](https://github.com/24601/Augustus/releases)
[![Quality](https://github.com/24601/Augustus/actions/workflows/quality.yml/badge.svg)](https://github.com/24601/Augustus/actions/workflows/quality.yml)
[![Docs](https://img.shields.io/badge/docs-24601.github.io-blue.svg)](https://24601.github.io/Augustus/)

Augustus equips agents to **find useful placements, build decision-driven
systems, create evaluations, and hill-climb them against real outcomes**.
It combines decision
theory, value of information, multi-criteria analysis, signal detection,
search/control, and formal-methods boundaries. It applies to software,
business, organizations, research, and everyday decisions.

[TypeSafe Jev](https://docs.typesafe.ai/) (Choice, Score, Noul) is the
default hosted exemplar. The skill also covers classical classifiers,
encoders, open decision heads, constrained readouts, rankers, and vision
scorers. Choose the family by the task, then test it against the baseline.
Sometimes the best result is a formula, a checklist, or no new model.

The working model is:

**evidence → bounded judgment → explicit policy → checked action → observed outcome**

Augustus is independent of TypeSafe. The
[official TypeSafe skill](https://github.com/typesafe-ai/skills) and current
provider docs own API contracts; Augustus supplies composition, implementation,
evaluation, and improvement methods. Named for
Augustus De Morgan, mentor of William Stanley Jevons.

## Try it

After installation, ask your agent:

> Use Augustus to audit our refund-email workflow. Find the smallest
> useful classifier insertion, keep eligibility and payments in code,
> and propose an evaluation that could reject the change.

> Use Augustus to compare ways our library could choose three programs
> under a fixed budget. Make the values, evidence gaps, and tradeoffs explicit.

> Use Augustus to review this confidence threshold. Explain what the score
> means, when to abstain, and what we should measure on held-out cases.

> Use Augustus to build a decision-model router and its evaluation harness.
> Keep our incumbent runnable, test complete episode outcomes, and set up a
> bounded improvement loop with untouched confirmation data and rollback.

Advice produces a concise design card and falsifier. Build requests produce
working adapters, policy and evals; improvement requests produce a bounded
incumbent–challenger loop. The agent reads only relevant references. Source
popularity and proxy-score gains do not establish improvement.

## Examples

| Problem | Placement | Evaluate |
| --- | --- | --- |
| Expensive generated-JSON email routing | Bounded intent classifier before existing handlers | Action errors, review coverage, total cost |
| Search results need ordering | Retrieve candidates, then rank relevance | Recall, nDCG, final task success |
| Many plausible projects under a budget | Explicit utility/MCDA with exact constraints | Sensitivity, feasibility, stakeholder outcomes |
| Agent claims it is finished | Judge evidence gaps; verify artifacts and effects | False completion and recovery on real tasks |
| Need a decision under uncertainty | Compare act, defer, and gather-more-evidence | Expected loss and value of information |
| Model appears to approve a risky action | Treat judgment as evidence inside host policy | Unauthorized effects, failure paths, drift |

A typed response is not proof of truth. Ranking scores, probability,
confidence, calibration, and action success have different meanings.
See [the working skill](.agents/skills/augustus/SKILL.md).

## Install

For agents supporting the Skills CLI:

```bash
npx skills add 24601/Augustus --skill augustus
```

This follows the repository's current default branch, which may contain
unreleased work. For a reproducible source checkout of the last release:

```bash
git clone --branch v0.7.0 --depth 1 https://github.com/24601/Augustus.git
```

The skill directory is `.agents/skills/augustus/`. Use your agent's local
skill installation mechanism to install that directory. Keep its references
and scripts together. Merely cloning a repository does not install it into
every agent.

The skill needs no API key to provide design guidance. Calling Jev or another
hosted provider is a separate, optional integration with its own credentials
and costs. Review installed instructions before granting any agent access.

Claude Code marketplace:

```bash
claude plugin marketplace add 24601/Augustus
claude plugin install augustus@augustus
```

In Claude Code, invoke `/augustus:augustus`; in Codex, use `$augustus`.
If it is not visible, reload your agent's skills/plugins and check its installed
version. See [worked examples](https://24601.github.io/Augustus/examples.html)
for the kind of result to expect. Avoid installing the same skill by multiple
methods in one agent.

## Project and evidence

- [Skill and reference index](.agents/skills/augustus/SKILL.md): runtime guidance.
- [Research archive](research/README.md): primary sources, historical claims,
  revisits, and the current decision-model review.
- [Contributing](CONTRIBUTING.md): content boundaries, tests, behavioral review.
- [Changelog](CHANGELOG.md): product changes, separate from research observations.
- [Website](https://24601.github.io/Augustus/): examples and ecosystem orientation.
- [Feedback](https://github.com/24601/Augustus/issues/new/choose): installation
  problems, mistaken activation, and sanitized real-world failures.

For local development, install `requirements-dev.txt` and run `make check`.
The offline helpers evaluate labeled binary predictions and paired workflow
outcomes; neither calls a model. The
[composition calculus](.agents/skills/augustus/references/composition-algebra.md)
and [build/improvement workflow](.agents/skills/augustus/references/optimizer-integration.md)
connect methods to implementation and evidence. Tests and structural lint do
not establish model quality or deployment benefit.

## Versioning

Current release: **0.7.0**. See the
[release notes](docs/release-notes-v0.7.0.md) for changes and migration details.

Historical TypeSafe skill provenance: v0.5.7 (`65a39f3`). Read live provider
docs before writing integration code; that pin is not a current API guarantee.
Install from the `v0.7.0` tag when you need an exact source revision;
default-branch installation may include later unreleased work.

## License

MIT. See [LICENSE](LICENSE). Security reports: [SECURITY.md](SECURITY.md).
Contributions: [CONTRIBUTING.md](CONTRIBUTING.md).
