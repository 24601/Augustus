---
title: "Augustus v0.7.1: sharper uncertainty routing and verified patrol findings"
description: "A patch release that corrects uncertainty-routing guidance, promotes five decision-changing patrol findings, consolidates duplicated references, and adds release-surface checks."
permalink: /release-notes-v0.7.1.html
---

# Augustus v0.7.1

Released 2026-09-23. This patch refines existing guidance; it adds no provider
integration, model, or new workflow capability. TypeSafe Jev remains the
default hosted exemplar, and exact rules, classical models, and human processes
remain valid alternatives. Nothing here claims a measured deployment gain.

## What changed in the skill

- **Uncertainty routing and deferral.** The judgment-class section now uses
  one three-option menu to show that entropy and top-option mass can rank the
  same cases differently: (0.5, 0.5, 0) has 1 bit, while (0.6, 0.2, 0.2) has
  more top mass and about 1.371 bits. The old example compared two menu sizes,
  and normalization erased its reversal. Deferral is stated as theory under
  calibrated mass: defer when 1 − top mass exceeds the handler's expected loss
  on the case, query cost included. Chow's rule is the constant-loss case. A
  rejector fit to representative handler outcomes is allowed. The handler
  decides deferred cases and policy authorizes the act; the earlier wording let
  a model handler "own" it. Dominance is now convention-free: "if one act never
  costs less, always take the other."
- **Five promotions from the 2026-09-23 patrol**, each kept because it changes a
  design decision:
  - Preflight rejects one-option or one-level questions. Their confidence is
    1.0 by construction.
  - The diagnosis table now covers name bias, not only position bias.
  - Done-checks need evidence the judged system cannot forge. A deterministic
    check is not independent if the agent can edit what it reads.
  - Post-deployment error needs outcomes on every case or a known-probability
    audit sample, not review queues or complaints alone. Reviewer accuracy is
    measured under the deployed display.
  - Labels from an automated check are not independent gold. A router's
    quality gain is bounded by the per-case best route.
- **Task-routed entry point.** The reference table is organized by what the
  user is doing and names the two offline scripts. One-off choices use weight
  sensitivity, missing criteria, dominated options, and value of information
  instead of a held-out population.
- **Consolidation.** `references/formal-semi-formal.md` is removed; its rules
  live in `formal-methods.md`, `mappings.md` §12, and `mental-models.md`.
  Repeated exemplar disclaimers and duplicated lists now appear once. Runtime
  references drop from 179,929 to 172,817 bytes. Two independent verifier
  lenses checked every cut against its owning passage.
- **Smaller fixes.** `evaluate_decisions.py --help` documents its input rows.
  Script paths use `<skill-dir>`. The example selective band follows from its
  own costs. The FAQ no longer implies a Noul confidence field. TypeAR links to
  its new name, TypeLLM.

The skill description and activation examples are unchanged.

## Upgrade notes

Reinstall from the `v0.7.1` tag with your existing method; avoid duplicate
installations. A Claude Code marketplace pinned to `@v0.7.0` stays there: run
`claude plugin marketplace remove augustus`, then add
`24601/Augustus@v0.7.1` and install again. Anything that linked
`references/formal-semi-formal.md` should link `references/formal-methods.md`.
The bundled scripts keep their valid-input interfaces; only
`evaluate_decisions.py` help text changed. The skill needs no API key.

## Repository changes

`make check` now enforces release-surface parity: CITATION, a dated changelog
heading, a pinned README install, and linked release notes must match a
non-prerelease version. It also rejects frontmatter keys outside the Agent
Skills spec, angle brackets in the description, and non-string metadata. The
release smoke installs from a `git archive` export. An opt-in, paid
`claude plugin eval` suite measures implicit activation with and without the
plugin, and an offline test keeps it honest. Eight new behavioral scenarios
cover the promoted rules and two non-trigger controls.

## Evidence and limits

Two independent verifier lenses, evidence fidelity and a doctrine skeptic,
checked every proposed edit. An independent Codex `gpt-6-astra` review
(reasoning effort `max`) found two P1s and one P2. All three were fixed, and a
second pass accepted the fixes.

Fresh agents answered all 38 behavioral scenarios using only the candidate
skill. Fable 5.1 graded the answers and reported no blocking finding: 271
aspect passes and two non-blocking notes on answer wording. A blind comparison
with 0.7.0 on the seven affected scenarios found the candidate better on two,
the same on four, and 0.7.0 slightly better on one (portfolio). That result led
to a wording fix, which a rerun confirmed. These are qualitative smoke
results, not a measured outcome improvement.

A pre-registered activation A/B (20 queries, 3 runs each, isolated) kept the
current description. A proposed rewrite fixed two missed triggers but falsely
triggered on a generic BLEU/ROUGE request.

Read the [patrol and 0.7.1 review evidence](https://github.com/24601/Augustus/blob/v0.7.1/research/patrol-2026-09-23.md)
and the [0.7.1 acceptance record](https://github.com/24601/Augustus/blob/v0.7.1/research/audits/2026-09-23-release-071.md).
Every third-party number remains Reported. No provider inference ran and no
third-party benchmark was reproduced. Requested model routing is recorded
separately from observed identity and is not backend attestation. Historical
TypeSafe skill provenance remains v0.5.7 (`65a39f3`), rechecked on 2026-09-23
as that repository's latest tag and HEAD.

Earlier release: [v0.7.0]({{ '/release-notes-v0.7.0.html' | relative_url }}).
