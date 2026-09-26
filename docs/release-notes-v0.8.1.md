---
title: "Augustus v0.8.1: verify that training and serving do what you intend"
description: "A trainer-validation patch covering optimizer ownership, soft targets, calibration export and attainable thresholds, with executed repair QA."
permalink: /release-notes-v0.8.1.html
---

# Augustus v0.8.1

Released 2026-09-26. A backward-compatible guidance patch for both Augustus
skills. No new model backend, pretrained weights, or training service.

## What changed

- Check that the optimizer owns the intended parameters and actual updates
  happen before paying for a long fit. Probe custom objectives against known
  targets instead of treating a decreasing loss as sufficient evidence.
- Preserve required calibration through export and fresh-process inference.
  Unchanged argmax does not imply unchanged thresholds, abstention or expected
  rubric scores; top-label ECE does not certify the whole soft distribution.
- Select thresholds over complete tied-score groups and allow empirical risk
  to be nonmonotone. Keep development selection distinct from confirmation.
- Preserve exact rules and no-training solutions when a model adds no value.

The website also includes the updated 3:05 film featuring Augustus Train.
Historical TypeSafe integration provenance remains v0.5.7 (`65a39f3`);
consult live provider documentation for current contracts.

## What was tested

The candidate passed 192 repository tests and both self-tests. Two fresh agents
used clean installations to repair five injected defect categories. The
coordinator replayed real CPU fitting, soft-target convergence, fresh-process
serving, missing-calibration refusal, threshold selection and routing recovery.
Both installed packages matched all 30 candidate skill files.

Eight valid independent acceptance checks passed. The ninth originally required
an allegedly correct serving fixture to remain unchanged; the agent discovered
an actual overflow defect in it. The original failure is preserved and the repair
was independently checked using high-precision arithmetic. Two genuinely correct
controls remained unchanged.

See the [executed QA and replay commands](https://github.com/24601/Augustus/tree/main/research/audits/2026-09-26-trainer-081-qa)
for exact revisions, test outputs and limitations. These are bounded application
fixtures, not proof of production quality, automatic skill activation, or an
advantage over an agent without Augustus. Those measurements are separate.

## Install or upgrade

Both skills ship together. A previously pinned install remains on its old tag.
For an existing Claude marketplace, remove `augustus` first, then reinstall:

```bash
claude plugin marketplace add 24601/Augustus@v0.8.1
claude plugin install augustus@augustus
```

```bash
npx skills add https://github.com/24601/Augustus/tree/v0.8.1 --skill augustus augustus-train
```

No application API migration is required. Revisit existing training and serving
checks where the failure modes above apply; this release does not require a new
fit or calibrator for an already valid artifact.
