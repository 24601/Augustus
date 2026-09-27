# Executable climb 1: bounded research contract

Owner authorization: “climb away”, after the VibeProxy advice pilot. Incumbent is
Augustus v0.8.1 at commit 4ba9d2111d29ea03247c22b3de90bfa8dde1b261.
Goal: improve actual application artifacts, separating automatic discovery from
usefulness once loaded. Synthetic contract fixtures, not production outcomes.

## Fixed experiment

- Three development tasks: safe first-message dataset preparation, feasible
  grouped learning-curve planning and cost selection, soft-target fit/export/serve.
- Three arms: no Augustus skills; both available automatically; both available
  with an explicit request to load the trainer. Otherwise identical prompts,
  inputs, model, tools, time and turn ceilings. Counterbalance arm order by task.
- Requested agent: `claude-opus-5-5` through existing VibeProxy. No paid judge;
  independent executable checks own acceptance. Preserve reported identities,
  tool calls, artifacts, latency, estimated costs and transport failures.
- Up to two guidance candidates, each addressing an observed development
  failure. No edits to frozen tasks, evaluator, budgets or success criteria.
  A demonstrated evaluator defect invalidates affected comparisons; correct it
  openly and rerun all affected artifacts, never only the preferred candidate.
- Maximum 27 agent runs, concurrency one, 20 turns / 180 seconds each, $15
  reported-cost stop checked between runs (one in-flight run can exceed it).
  No extra training service, paid search, network access by task agents, or
  release publication. Local Python standard library execution only.
- Development is descriptive. One initial run/task/arm, then at most six runs
  per candidate across automatic and explicit arms. If a candidate improves,
  reserve six runs for confirmation before spending on another candidate.

## Protected confirmation and promotion

An independent thread owns two fresh task contracts and their graders in its
separate workspace. It supplies hashes only until finalists are frozen. Parent
and development agents do not receive confirmation content during tuning. Task
agents never receive grader/reference files. This is workflow isolation, not a
claim that a privileged coordinator cannot request access.

Primary measurement: complete task-contract pass, plus prespecified invariant
checks for diagnosis. Timeouts/errors/missing artifacts fail, not exclusions.
Activation is a separate trace measure; a baseline need not call any skill.
Manual prose quality is diagnostic only. Record all attempts, not best runs.

Choose a candidate only if it repairs at least one failed development contract
without a new contract failure and without more than 50% aggregate reported
agent-cost growth versus the corresponding release arms. Confirm it against
the incumbent and no-skill baseline on both protected tasks (six runs); require
no new task failure and at least one strict contract gain over the incumbent.
These are engineering gates, not statistical significance or broad superiority.
If initial development is saturated, stop changing guidance and report that the
instrument cannot identify benefit; do not create gratuitous changes. If no
candidate earns confirmation within budget, retain 0.8.1.

Permitted promotion: checked development guidance on main as 0.8.2-dev, with
versions synchronized, only after the gates above. Published 0.8.1 is immutable;
new release publication needs separate authorization. Archive rejected patches
and hypotheses. Stop on two non-improving candidates, budget, infrastructure
failure without a bounded remedy, or completed confirmation. Never reuse a
revealed confirmation outcome for another candidate in this climb.
