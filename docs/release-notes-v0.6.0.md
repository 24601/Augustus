---
title: "Augustus v0.6.0: focused decision guidance and reliable checks"
description: "A smaller decision-model skill, stronger evaluation, safer research maintenance, verified packaging, and clearer onboarding."
permalink: /release-notes-v0.6.0.html
---

# Augustus v0.6.0

Released 2026-09-22. This release restores the skill's core workflow:
**evidence → bounded judgment → explicit policy → checked action → observed outcome**.
TypeSafe Jev remains the default hosted exemplar; the method applies across
model families and software, business, organizational, and everyday decisions.

## Highlights

- **Focused guidance.** The entry point shrank from approximately 192 KB
  to 9 KB, with 17 task-routed references. Historical research is preserved
  by exact Git revision and a verified 30-file hash manifest.
- **More precise decision design.** Clear boundaries distinguish ranking,
  probability, confidence, calibration, abstention, causal interventions,
  optimization, and authority. Current research is attributed and bounded
  by its assumptions; unrun experiments remain explicitly unrun.
- **Meaningful verification.** Structural lint, content budgets, 53 regression
  tests, numerical self-tests, independent behavioral review, and CI replace
  repeated-prose locks and tautological assertions. Twelve realistic skill
  scenarios include no-model and non-trigger cases.
- **Safer research maintenance.** New promotion guidance requires a changed
  design decision. Refresh collection is bounded and read-only; it never
  stages, commits, pushes, clones projects, or overwrites a receipt.
- **Better installation and onboarding.** Fixed Claude marketplace metadata,
  Codex skill presentation, six canonical placements, two worked examples,
  feedback intake, social previews, sitemap, and mobile layout checks.

These checks establish repository and installation behavior, not measured
model superiority, real-world decision improvement, search rank, or growth.

## Upgrade notes

Reinstall or update Augustus through your existing installation method;
avoid installing duplicate copies through multiple methods. Claude Code
uses `/augustus:augustus`; Codex uses `$augustus`. The skill itself needs
no API key. Hosted model calls remain an optional, separately configured
integration.

If you use the offline helpers directly:

- Pass `--cost-fp` and `--cost-fn` explicitly for cost reports; add
  `--cost-abstain` for selective-policy cost. Use `--lower-threshold` and
  `--upper-threshold` for an abstention band. Fit thresholds on calibration
  data and evaluate the frozen policy on a separate split.
- Complete binary predictions use `action_rate`; selective coverage is a
  different measure. All-abstain selective error is undefined, not zero.
  Impossible observed probabilities have infinite log loss. Duplicate IDs,
  invalid probabilities, and incomplete paired baselines are rejected.
- Refresh wrappers now emit JSON receipts to standard output. Use
  `--output` for a new receipt file; existing files are never overwritten.
  Update any scheduler expecting appended logs or automatic Git writes.
- Run `make check` from a source checkout for the complete check suite.
  The old uniqueness-gate entry point runs only the structural checker;
  historical repeated research passages are no longer required.

## Evidence and earlier releases

Read the [integration review](https://github.com/24601/Augustus/blob/v0.6.0/research/audits/2026-09-22-integration-review.md),
[primary-source research](https://github.com/24601/Augustus/blob/v0.6.0/research/decision-model-review-2026-09-21.md),
and [discoverability audit](https://github.com/24601/Augustus/blob/v0.6.0/research/audits/2026-09-21-discoverability.md).
These are dated pre-release evidence; their descriptions of unperformed
publication or deployment refer to the audit time, not the current release.
Native-host implicit activation and real-user outcome/growth measurements
remain follow-up work.

Earlier release: [v0.5.1]({{ '/release-notes-v0.5.1.html' | relative_url }}).
