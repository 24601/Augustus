# Decision-model research

Research supports Augustus's design guidance across the whole decision-model
class. TypeSafe Jev is the default hosted exemplar, not the limit of inquiry.
Use [protocol.md](protocol.md) and the [research update prompt](prompts/research-fold.md).

## Current review

The [2026-09-21 decision-model review](decision-model-review-2026-09-21.md)
covers primary sources, current model families, calibration, selective
prediction, conformal risk, decision-focused learning, and evaluation.
Claims, hypotheses, and experiments not run are distinguished there.

The [integration review](audits/2026-09-22-integration-review.md) records
mission/history findings, changes, behavioral evidence, actual checks, and
release boundaries. The [discoverability audit](audits/2026-09-21-discoverability.md)
separates local packaging/onboarding improvements from public growth work.

## Historical evidence

- [notes.md](notes.md): source cards and dated claim changes. Search by
  canonical source ID; do not load the whole file for an ordinary skill task.
- [sources.json](sources.json): discovery URLs and notes. Historic top-level
  retrieval dates are not freshness guarantees for every record.
- [revisit_fingerprints.json](revisit_fingerprints.json): last-look identities
  and four source fingerprints; see [the revisit checklist](revisit-checklist.md).
- [refresh-log.md](refresh-log.md) and [changelog-hourly.md](changelog-hourly.md):
  historical scan logs and legacy uniqueness passages, not runtime policy.
- [archive/](archive/): original scan packets, curriculum, findings, and receipts.
- [Pre-review manifest](archive/pre-review-2026-09-21.json): exact Git revision,
  hashes, and retrieval URLs for the prior installed skill and scripts.

Existing historical locks are retained as evidence. Their old instructions
to duplicate passages across files are superseded by the research protocol.
The runtime skill contains the distilled rules; the archive contains the
evidence and its limits.

## Collect a review receipt

```bash
scripts/refresh-jev-research.sh
scripts/refresh-jev-research.sh --source github:typesafe-ai/skills
scripts/hourly-refresh.sh --source github:typesafe-ai/skills
```

Without a source, collection probes official documentation/evaluation
availability. Named GitHub sources produce fingerprint receipts. The hourly
wrapper first runs offline checks; the scheduler owns timing. Use `--help`
for explicit output-file options. No collector changes the tracked baseline,
clones third-party code, stages files, commits, or pushes.

These probes are not a full ecosystem discovery pass. Review a receipt
against the prior card, inspect material diffs, and decide whether anything
changes the guidance. An unavailable source stays unknown.
