# Recurring research and reassessment

This is the maintainer's operating contract, not evidence of an active scheduler.
The collector scripts do not schedule work or review their own receipts. Use the
[protocol](protocol.md) and [fold prompt](prompts/research-fold.md) for every fold.

## Current operational evidence

Checked 2026-09-22 after the full refresh:

- Git history and `refresh-log.md` contain roughly hourly folds through the
  04:44 UTC scan, merged at 05:14 UTC. Some are substantive revisits. This proves
  historical work, not continuing execution or exhaustive reassessment.
- Live GitHub workflows are Quality, Pages checks/deployment, Scorecard, and
  dependency graph updates. Only Scorecard has a repository cron schedule;
  it is a security check, not a research refresh.
- No Augustus research job was found in the checked local Codex automation
  definitions, user crontab, loaded launchd labels, or user LaunchAgents files.
  This does not rule out a remote scheduler. Its owner, active configuration,
  next run, and recent successful run receipt remain unverified.
- Today's [full refresh](decision-model-review-2026-09-22.md) is an explicit
  user-requested reassessment. It is not proof of unattended maintenance.

Do not report this operating contract as automated until the scheduler owner
provides live configuration and successful research-run evidence. Configuring a
job, a successful availability probe, and completing a substantive review are
three separate states.

## Target cadence

The maintainer owns completion and can adjust these intervals with an explicit
reason and a bounded overdue backlog. These targets are not configured jobs.

| Interval or trigger | Required work | Completion evidence |
| --- | --- | --- |
| Daily; hourly only while launch volume warrants it | Probe official contracts and actively used sources; discover new class-wide work; triage changed identities/revisions, failures, and retractions. | Query/coverage receipt, changed-source queue, failures, and next due time. A no-change probe is a valid result, not a full review. |
| Within one working day of a material change | Inspect the actual API/code/paper/evaluation diff. Prioritize retractions, safety or privacy changes, and changed score semantics used by current guidance. | Old/new claim, exact revision, inspection depth, affected references, disposition, and any immediate qualification of unsupported advice. |
| Weekly | Resolve high-priority revisits; inspect a rotating cohort of older source cards; search beyond Jev across the method families in the protocol. Recheck current guidance against negative results and competing approaches. | Reviewed cohort and selection rationale, unresolved/overdue sources, catch-up versus new work, targeted corrections or justified no-change decisions. |
| Monthly and before a substantive release | Reassess the whole mission and current advice even when source fingerprints are unchanged: assumptions, counterexamples, simpler baselines, human decision processes, research coverage, installed behavior, maintenance cost, and discoverability. | Full coverage ledger, fresh behavioral answers and independent review where guidance changes, accepted/rejected findings, and a bounded next-review plan. |

For a source revisit, trace the implications into all dependent rules, examples,
tests, and public claims; one corrected source card does not repair dependent
advice automatically. Unchanged source bytes do not establish that our previous
interpretation was right. Review interpretations and deployment assumptions too.
Rotate the old-card cohort by risk and age rather than claiming every repository
was audited each week. Preserve unreviewed items and their true review ages.

## Scheduler handoff and liveness checks

The scheduler owner must retain:

```text
Job ID and owner; configured timezone/cadence; enabled state; next due time:
Requested model/effort and permitted tools/costs:
Last attempted run; last successful collection; last completed review:
Run URL or durable receipt; coverage cutoff; reviewed revisions:
Open material changes and overdue reviews; next broad reassessment due:
Failure or missed-run notification destination:
```

On every invocation, compare these states with the target cadence. A run that
fetches successfully but skips review must not advance `last completed review`.
Likewise, metadata-only collection must not reset a source's last-reviewed age.
Report overdue work and failed/incomplete runs explicitly; do not issue a green
"up to date" claim when liveness or review coverage is unknown. A scheduler that
is disabled, repeatedly failing, or missing receipts needs owner attention.

Give a scheduled reviewing agent the fold prompt, prior coverage cutoff and
queue, access to the actual primary artifacts, and enough context to challenge
existing advice. Merely executing `hourly-refresh.sh` cannot do that job. Keep
publication separate: neither cadence nor a terminal instruction grants new
merge, release, outreach, paid-search, or account-setting authority.

Measure resolved uncertainties, corrected design decisions, held-out behavior,
overdue material changes, and time to find useful guidance. Source counts,
timestamps, hourly commits, and unchanged-source fetches are not substitutes.
