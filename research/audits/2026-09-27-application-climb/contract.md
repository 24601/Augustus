# Application climb 2: frozen measurement contract

Authorization: user “ok, so do it” after proposing less-prescriptive application
tasks, independently fixed outcomes, and repeated three-condition measurements.
This is a new experiment, not relabeling or rerunning the saturated code tasks.

## Question and treatment

Does released Augustus help an agent choose and implement an appropriate
application decision system when requirements specify outcomes and interfaces,
but do not prescribe the model, primitive, data split or optimization method?

Two synthetic development applications, each with local data and domain docs:
one stock/policy selection problem and one policy/no-training opportunity.
The application requirements disclose action costs, serving constraints and
acceptable outcomes. Private future outcomes and evaluators are fixed before
task-agent execution. Public input and private grader hashes are recorded.
Known-good implementations and plausible wrong ones validate the instrument.
Coordinator can inspect development graders; task agents cannot. The previous
independent confirmation packet remains unopened and unused.

Three arms: no Augustus; both 0.8.1 skills automatically available; both available
with the sole prefix “Before implementing, load augustus-train and apply its
relevant guidance.” Same requested/reported Opus 5.5 medium, Mac VibeProxy,
tool isolation, 20-turn/180-second ceilings, standard-library Python and no
task-agent network. Three repetitions per task/arm, 18 runs total. Arm order
cycles none/auto/explicit, auto/explicit/none, explicit/none/auto; second task
starts one position later. Record order, caching and cost; no seed-control claim.

## Measures, bounds and decision

Primary: application acceptance, consisting of disclosed outcome-loss threshold,
hard safety/serving constraints and JSON artifact roundtrip/fresh-process use.
Errors, malformed artifacts and timeouts fail, not exclusions. Report all
per-run losses and failures; activation is separate. No LLM outcome judge.
Secondary: per-task median loss, pass count, loading, latency and reported cost.
Do not pool incomparable task loss units or treat repetitions as new task types.

Hypothesis: loaded guidance reduces harmful selection/validation errors relative
to unaided implementation. Falsifier: equal/worse acceptance or loss, or a safety
regression. A descriptive benefit signal requires at least two additional passes
out of six versus baseline and no task with fewer passes; it is not significance
or a release claim. Saturation is again a valid null result, not permission to
change frozen outcomes. Any grader defect requires a documented correction and
regrading all arms; no selectively repaired submissions.

Budget: 18 inference attempts, concurrency one, at most $10 new reported cost
checked before launches with one possible in-flight overshoot. Prior campaign
spent $1.8080588, retained in accounting. No automatic retries on unknown outcomes;
stop and reconcile. No guidance optimization or release is authorized by this
measurement protocol. If there is a useful failure, record a specific next
hypothesis rather than modifying skills against revealed confirmation outcomes.
Stop on completed 18 runs, cost ceiling, or unresolved infrastructure failure.

Only synthetic data; no claim about customer deployment, model training quality
at scale, or replacing a general Jev. Publish replayable research evidence after
runs complete; no new release or change to published 0.8.1.
