---
title: "Augustus v0.7.0: build, evaluate, and improve decision systems"
description: "A compositional decision calculus, an executable outcome evaluator, a bounded improvement workflow, and a full primary-source refresh."
permalink: /release-notes-v0.7.0.html
---

# Augustus v0.7.0

Released 2026-09-22. This minor release equips agents to find, build, evaluate,
and improve decision-model systems, with new paired-outcome tooling and a more
explicit composition calculus. It adds no provider integration or model and makes no claim of
measured model superiority. TypeSafe Jev remains the default hosted exemplar;
exact rules, classical models, and human processes remain valid alternatives.

## The important shift

Augustus is a skill and working method for agents to **discover useful decision
models, implement compositions, build evals, and hill-climb decision-driven or
Software 3.0 systems**. Research is input to that work, not its finished output.
The goal is to derive and test the best-supported method for the actual task,
not reproduce a consensus survey or chase a fashionable benchmark.

That capability is now named directly in the skill's activation description,
Codex UI, Claude marketplace, README, and website. Discoverability should match
what users want to accomplish: build and improve working systems with outcomes
and explicit constraints—not merely read about model placement.

## What changed

- **Composition-to-implementation loop.** Typed evidence contracts, conditional
  cascade and branch risk, dependence-safe budgets, decision-regret bounds,
  information substitution limits, and trajectory-level evaluation. Cross-field
  analogies must supply their assumptions and a falsifier.
- **Executable outcome comparison.** A standalone paired-workflow evaluator
  separates descriptive search from fixed-sample confirmation, flags observed
  constraint violations, and keeps unknown costs explicit. Fixtures and proxy
  results are not promoted to outcome evidence; the helper never deploys a policy.
- **Bounded improvement.** Agents retain a runnable incumbent, build evals before
  hill climbing, protect confirmation data, preserve rejected trials, and use
  authorized rollout and rollback. Research informs mechanisms, not a median survey.
- **Primary-source refresh.** Reviewed Jev-Omni, decision-model-testing, pijev,
  official contracts, selected ecosystem changes, and recent decision research.
  Traversed all 400 tracked Jevusers entries and 1,299 app rows. Directory
  traversal and GitHub/Hub metadata discovery are not code audits.
- **Precise score and evidence boundaries.** Version wrapper and aggregation
  semantics; distinguish convex-loss averaging from calibration; measure actual
  media coverage, accepted-case support, injection controls, and complete
  workflow cost and latency.
- **Independent re-derivation.** Earlier delegated scopes were redone with
  requested GPT-6 Astra/xhigh agents. Corrected unnecessary training/filtering
  requirements, a blanket calibration prerequisite, post-action enforcement
  claims, Alloy temporal limits, and distillation overstatements.
- **Regression protection.** The offline suite grows from 53 to 96 tests.
  Skill scenarios grow from 12 to 31, with fresh answers reviewed by the
  coordinator. Structural checks and behavioral smoke tests are distinct.
  Adversarial review additionally caught maximum-float overflow, subnormal
  aggregation errors and log-loss cancellation; exact arithmetic oracles,
  randomized boundary probes and fixed-sample null checks now cover those paths.
- **Discoverability checks.** Corrected About metadata, verified current directory
  presence and page layout, fixed encoded fragments, and added `noindex` checks.
  Audited existing awesome-list entries and drafted targeted positioning updates;
  no third-party PRs, issues or corrections were submitted by that audit.
  Installation, implicit activation, indexing, and real benefit remain separate
  claims; listings alone do not establish growth.

## Upgrade notes

Update through your existing installation method; avoid duplicate installations.
The skill needs no API key. No provider benchmark or paid inference was run.

The existing offline helpers now reject duplicate JSON keys, conflicting known
repository node IDs, and invalid schema-version types. Oversized numbers,
decoder nesting failures, and interrupted HTTP reads produce explicit input or
receipt errors. Large finite policy costs are averaged without multiplying
counts into an avoidable overflow. Valid-input interfaces remain unchanged;
partial baselines still carry no comparative claim.

Run `make check` from a source checkout. Runtime references must stay within the
installed skill, including nested cards; budgets, links, and SemVer are checked.
Rendered-site validation checks asset existence, not image decoding or CSS URLs.
Use the explicit GitHub Pages gem activation in CONTRIBUTING for a matched build.

## Evidence and limits

Read the [refresh and source dispositions](https://github.com/24601/Augustus/blob/v0.7.0/research/decision-model-review-2026-09-22.md),
[replacement ledger and integration evidence](https://github.com/24601/Augustus/blob/v0.7.0/research/audits/2026-09-22-refresh-acceptance.md),
[adversarial findings and corrections](https://github.com/24601/Augustus/blob/v0.7.0/research/audits/2026-09-22-adversarial-070.md),
[discoverability audit](https://github.com/24601/Augustus/blob/v0.7.0/research/audits/2026-09-22-astra-redo-discoverability.md),
[existing-listing update queue](https://github.com/24601/Augustus/blob/v0.7.0/research/audits/2026-09-22-listing-positioning.md),
and [maintainer guidance](https://github.com/24601/Augustus/blob/v0.7.0/research/prompts/maintainer.md).
These dated artifacts preserve what was verified at each stage; final publication
and deployment are recorded on the release PR. Requested model routing is not
independent backend attestation. Public projections are not private benchmark
replay; no source result was upgraded to Reproduced without a local run.

Earlier release: [v0.6.0]({{ '/release-notes-v0.6.0.html' | relative_url }}).
