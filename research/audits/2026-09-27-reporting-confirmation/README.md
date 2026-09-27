# Untouched-task comparison: acceptance ties, reporting mechanism not exercised

**Reproduced, 2026-09-27.** All eighteen implementations passed the frozen
private grader. New guidance improved neither acceptance over no Augustus nor
acceptance over the old guidance. This meets neither predeclared benefit rule.
No skill was changed or release published as a result of this experiment.

| Condition | Policy artifact | Distribution serving | Trainer loads | Reported cost | Mean agent wall time |
| --- | ---: | ---: | ---: | ---: | ---: |
| No Augustus | 3/3 | 3/3 | 0/6 | $0.7354604 | 33.39 s |
| Old explicit (0.8.1) | 3/3 | 3/3 | 6/6 | $0.9137690 | 40.21 s |
| New explicit (0.8.2-dev) | 3/3 | 3/3 | 6/6 | $0.9147302 | 41.19 s |

Total new reported cost: **$2.5639596**, within the $10 ceiling. New guidance
cost 24.38% more than no Augustus and 0.11% more than the old guidance in these
runs. These are provider/CLI list-price estimates, not reconciled billing.
Small samples, caching and order effects preclude a general cost-effect claim.
No retries, timeouts, tool denials, protocol failures or missing costs occurred.
Previous campaigns cost $6.3239766; cumulative arithmetic total is $8.8879362.

## What this measures

The [contract](contract.md) and candidate revisions were committed before either
protected archive was opened. Three repetitions per condition per task used
the same requested/reported Opus 5.5 medium through existing VibeProxy on the
Mac, Claude Code 2.1.282, 20-turn/180-second ceilings and concurrency one.
Order was rotated. Both explicit arms received identical load instructions;
baseline omitted only that prefix and the plugin. Upstream model identity is
not independently attested by the routing name. This is not automatic activation
testing; twelve explicit runs loaded the trainer body, none the companion body.

The independently authored tasks specify exact interfaces and policy semantics:
minimax regret over currently allowed modes, and safe distribution alignment with
expected-loss decisions. They exercise deterministic implementation, not choosing
base models, constructing a messy dataset, fitting or hill climbing an application.
The [instrument inspection](instrument.md) records reference and mutation checks.

**No run read or invoked the new policy-receipt helper.** The tasks do not request
population reporting or future-loss claims. Thus this is a useful no-observed-
regression result on two fresh task types, but not an efficacy test of the repaired
reporting mechanism. Saturated acceptance cannot demonstrate equivalence, general
superiority, or that the skill is useless. Repetitions and thousands of checks do
not increase the number of independent application types beyond two.

The next useful measurement should directly require an operational report from
messy, independently authored records and compare correctness of population,
policy direction, uncertainty claims and resulting action. Include cases where
the right answer needs no helper. Freeze its rubric and inputs before running;
do not turn the revealed tasks into a tuning holdout or spend more on identical
saturated coding tasks. This recommendation is not another executed campaign.

## Verification and replay

```sh
python3 research/audits/2026-09-27-reporting-confirmation/replay.py
make check
```

Coordinator replay in the Linux orb verified **551 archived file hashes**, frozen
archive hashes, task inputs, counterbalancing, equal prompts, model/effort/budget
settings, actual skill loads and reported costs, then independently reran all
eighteen grades. Every result matches the Mac. Each policy submission passes
1,484 checks/717 cases; each serving submission passes 229 checks/192 cases.
All eighteen submission sources were read before execution. The 30 old and 31
new snapshot files separately match the frozen Git revisions byte-for-byte.
Repository check: 197 tests, both self-tests and shell syntax pass.

Mac isolation uses scoped tool hooks and Seatbelt for agent Python execution;
six archived offline checks include private-grader read denial. Those OS checks
were not rerun on Linux. Parent grading uses reviewed frozen code, clean process
environment and a 60-second timeout, not an adversarial-code sandbox. No new
inference is part of replay. No credential-shaped values were found by the
parent scan; nonsecret host paths and a dummy local-proxy placeholder remain.

[Raw archive](results.tar.gz), SHA256
`32bd19ed08e45dc8ff020b811023b8cd7efd14c9cc71c26784b7151066e4b1ed`,
contains frozen skills, task packet, harness, traces, solutions, runner grades,
mock-isolation evidence and cost records. [Parent replay](replay-result.json)
retains per-run results. The protected packet is now consumed and published for
replay; it must not be described as an untouched holdout again. Development
remains 0.8.2-dev, published release 0.8.1 unchanged.
