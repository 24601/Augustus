# Value discovery: instrument ready, discovery blocked on credentials

**Status, 2026-09-27: no inference has run and nothing is graded.** The frozen
[contract](contract.md), the independently authored
[instrument](instrument.md) and the [isolation qualification](isolation.md) are
complete. The first baseline attempt failed before any model turn because the
VibeProxy Claude credential cannot refresh. Reported cost so far: **$0**.

## Why this stage exists

Three earlier campaigns tied at full acceptance. Those tasks supplied the
decisions Augustus is supposed to help with — exact interfaces, complete
manuals, disclosed distributions — and graded implementation. A strong agent
saturates that. The open question is not "can it implement a specification" but
whether Augustus changes decisions, outcomes or cost when the choices are
genuinely unresolved. Saturation, insensitive measurement and an unhelpful skill
are three different explanations, and the earlier results cannot separate them.

## What is ready

Two application briefs with messy synthetic operational records: cold-chain
sleeve dispatch, where the decisive fields arrive after delivery and equipment
changed mid-history, and printshop preflight routing, where a shuffled
multi-revision export retries reprint billing more often than clean invoices.
Both disclose the objective, action costs, serving keys and deployment rule, and
name no model, split, primitive or hazard. The private grader measures continuous
future-cohort dollars, recomputes every reported number from source records read
before candidate execution, enforces serving limits in fresh processes, and marks
historical split independence `unverifiable` rather than trusting ID lists.
Coordinator replay reproduced all forty validation runs.

Request-body capture shows the baseline arm carries no Augustus or sentinel text,
while planted sentinels in disposable synthetic locations do appear, so the
absence is a measurement rather than an assumption.

## The block

Twelve `POST /v1/messages` calls returned HTTP 503 `auth_unavailable`. A separate
offline diagnosis, with no messages request, showed the stored credential failing
to refresh with `invalid_grant: Refresh token not found or invalid`. The model
catalog and model registration succeeded, so this is authentication, not routing
or model availability. The runner recorded the attempt as failed, refused to
retry automatically, and stopped the stage.

The single trace contains no model turn: zero tokens, zero cost, and the only
assistant event is the CLI's own synthetic error. The harness flagged it as a
protocol failure rather than accepting a substitute response. Evidence:
`discovery-blocked.tar.gz`, SHA256
`f8811641608e24f4ecf6cf0284318da2ac461800f123ca9610d7820e11be7ee2`.

This is the disclosed credential-rotation risk: a temporary credential copy can
rotate the upstream refresh token without writing back to the original file.

## To resume

Re-authenticate the VibeProxy Claude credential interactively, then authorize the
runner to clear the failed record and continue. Ceilings are unchanged: baseline
arm only, four attempts, $3, 40 turns, 600 seconds, concurrency one, proxy
restarted per attempt. Discovery observations stay excluded from any later
comparison estimate. If baselines do not fail consequentially on either task,
the honest outcome is a published null, not a harder grader or a weakened model.
The protected transfer packet remains frozen, unopened and outside this
repository.
