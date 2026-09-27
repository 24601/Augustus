# First executable climb: retain 0.8.1

**Reproduced, 2026-09-27.** All nine submitted implementations passed the frozen
development checker. No guidance candidate was created or promoted. The
predeclared saturation stop applies; protected confirmation remains unopened.
This is a measurement result, **not evidence that Augustus improves outcomes**.

## Results

| Arm | Task passes | Named checks passed | Trainer loaded | Reported cost |
| --- | ---: | ---: | ---: | ---: |
| No Augustus | 3/3 | 10/10 | unavailable | $0.6097026 |
| Automatic availability | 3/3 | 10/10 | 0/3 | $0.5825572 |
| Explicit trainer request | 3/3 | 10/10 | 3/3 | $0.6157990 |

Tasks cover first-message data preparation with transitive leakage groups,
feasible grouped learning curves and future-cost selection, and soft-target
logistic fitting with calibrated export/fresh-process serving. These are synthetic
component contracts, not real application or production outcomes. Ten named
checks contain multiple fixtures/boundaries; they do not exhaust every possible
input covered by the prose contracts.

One run per task/arm, nine attempts, no timeouts or protocol failures. Total
reported cost **$1.8080588** against the $15 stop. No further inference was
authorized after grading. No model judge. Requested/reported model
`claude-opus-5-5`, medium effort, Claude Code 2.1.282 through a temporary VibeProxy
backend on the Mac. Retry/fallback disabled. Response names are routing evidence,
not independent upstream attestation; costs are reported estimates, not billing.

Both skill descriptions were available in automatic and explicit arms. None of
the automatic runs loaded either body; all explicit runs loaded the trainer.
Parent verified inventories, calls, delivered trainer text, identical automatic/
baseline prompts, the exact explicit prefix, artifact hashes and result costs.

## What changed our understanding

| Hypothesis | Test | Result / disposition |
| --- | --- | --- |
| Prior advice failures expose executable component weaknesses | Three frozen tasks, independent arithmetic and behavioral checks | Baseline passes all; no repair target in this set |
| Availability leads to useful automatic loading | Actual Skill calls and delivered content | 0/3 automatic loads; descriptive only |
| Explicit guidance improves correctness over baseline | Same artifact checker for all arms | 3/3 versus 3/3; no demonstrated incremental benefit |

The checker was tested before any solution was inspected: its reference passes
all ten checks and seven plausible wrong implementations fail assertions. This
rules out several vacuous-test mistakes, but **does not establish that the task
set measures the product's distinctive value**. These prompts specify the
correct split, optimizer, policy and cost formula. They test implementing a
decision already made more than discovering the right decision. A strong model
can follow those contracts without Augustus. Automatic nonactivation on these
exact implementation requests is not by itself proof of a general trigger defect.

The next useful research hypothesis is application-level value: can guidance
help choose the primitive, admissible data, stock, baseline, evaluation and
stopping rule when the task does not supply those decisions? A future experiment
should freeze independent application outcomes while leaving those decisions to
the agent, include no-training and nontrigger cases, and repeat matched runs.
That is a proposed **new** experiment, not permission to move this one's goalposts
or reinterpret its ties as wins. No stronger release claim follows from this run.

## Replay and custody

From the repository root, with Python 3.12+ (3.11 with tar extraction-filter
support also works), without credentials or model access:

```sh
python3 research/audits/2026-09-27-executable-climb/selftest.py
python3 research/audits/2026-09-27-executable-climb/replay.py
make check
```

Parent replay verified 325 archived file hashes and regraded all nine solutions;
30/30 named checks pass. `make check`: 192 unit tests, both self-tests, repository
checker and shell syntax pass. Mac-specific harness isolation tests are retained
as runner evidence, not claimed rerun on Linux. Parent additionally scanned the
export for credential shapes without printing any candidate values; none found.

- [Contract](contract.md) and [frozen hashes](frozen-sha256.txt) were fixed before
  execution; the grader fingerprint was sent to the runner before launch.
- [Self-test results](instrument-selftest.json), [parent replay](replay-result.json)
  and `grades/` retain executable evidence. Grader/reference now publish only
  after development agents completed; these tasks are no longer future holdouts.
- [Initial archive](initial-results.tar.gz), SHA256
  `ff68b00f5553102341e5aaca83d63128abc1d302584e92549e39d22ad59b8950`,
  retains exact task-agent code, self-checks, traces, configs, manifests, release
  snapshot, instrument and offline isolation-test history. Offline mock failures
  are retained separately from the nine inference attempts. No auth files,
  private proxy logs or CLI runtime homes are included. Absolute nonsecret paths
  remain for provenance. See its `climb1-instrument/README.md` for Mac replay limits.
- [Holdout custody](holdout-custody.md): the independent author's two task/grader
  archives were not transferred to this coordinator or task agents. No finalist
  passed development selection, so no confirmation was spent or claimed.

The product and published tag remain **0.8.1**. Only research code/evidence changes.
