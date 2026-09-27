# Application climb 2: acceptance ties, no demonstrated benefit

**Reproduced, 2026-09-27.** Eighteen task-agent implementations were independently
graded on frozen future cases: **18/18 pass**, zero measured safety violations.
All three conditions pass six of six runs. The predeclared benefit criterion
is not met. No skill was modified, no candidate promoted, no release published.
Published **0.8.1 remains unchanged**.

## What ran

Two application problems, three conditions, three repetitions per condition.
The agent chose its own approach, fitting/selection procedure and validation;
prompts specified interfaces, outcomes and operational constraints, not code.

- **Checkout selection:** choose among frozen synthetic score stocks or a
  constant, adapt a decision policy using 1,200 historical orders, account for
  a documented funnel change and 15 ms stock budget. Private future cohort:
  4,000 orders plus ten malformed/unavailable-score cases. Loss is 8 per missed
  fraud and 1 per needless review; acceptance requires mean <= 0.45, valid
  stock latency, safe fallback, and fresh-process artifact serving.
- **Enzyme dispatch:** choose an approach using 480 selectively observed
  historical orders and current operational semantics. Private cohort: 1,215
  dispatch snapshots, including certificate corrections and recovery. Acceptance
  requires zero illegal dispatches, mean realized cost <= 50, and JSON artifact
  reload in a fresh process. The known carrier distribution permits an exact
  expected-cost policy; fitting historical success labels is not required.

Conditions: no Augustus; both skills available automatically; both available
with an explicit trainer-load request. Requested/reported Opus 5.5 medium through
VibeProxy on the Mac, Claude Code 2.1.282. Concurrency one, 20-turn/180-second
ceilings, standard-library Python, no task-agent network. Orders rotate within
each task; each arm occupies each position once. Skills are byte-pinned 0.8.1.

## Results

| Condition | Passes | Trainer body loads | Selection median loss | Dispatch median cost | Reported agent cost |
| --- | ---: | ---: | ---: | ---: | ---: |
| No Augustus | 6/6 | unavailable | 0.20325 | 44.80329 | $1.3423818 |
| Automatic | 6/6 | 0/6 | 0.17625 | 44.80329 | $1.3442966 |
| Explicit | 6/6 | 6/6 | 0.20325 | 44.80329 | $1.8292394 |

All nine checkout implementations selected compact, used the 300 post-change
rows, excluded the slow stock and passed failure-policy checks. All nine
dispatch implementations achieve exactly the reference cohort cost with no
illegal actions. Fresh-process serving succeeds throughout. Actual fit functions
were rerun by the parent, not merely inspected or accepted from agent prose.

Selection losses, repetitions 1/2/3:

- None: 0.20325 / 0.20325 / 0.20325.
- Auto: 0.17625 / 0.16750 / 0.20325.
- Explicit: 0.20325 / 0.20325 / 0.17650.

The lower-loss solutions choose less brittle thresholds using smoothing or a
coarser threshold search; this is an observed implementation difference, not a
validated new general rule. Automatic runs loaded neither body, although skill
descriptions were present. Three repetitions on one fixed selection cohort
cannot distinguish stochastic variation from a description/treatment effect.
Explicit loading has the same median selection loss and costs **36.27% more**
in aggregate than no Augustus. Costs are reported estimates, not reconciled
billing, and cache/order effects remain possible despite counterbalancing.

New reported model cost **$4.5159178**, below the $10 ceiling. Together with the
prior executable campaign: **$6.3239766**. All 18 attempts completed; no retries,
timeouts, missing cost, transport failure or protocol error. Twelve Bash guard
denials and recovery attempts remain in traces; they are not excluded runs.
Raw CLI `num_turns` includes tool-result events; distinct assistant message counts
are 5–15, with the same `--max-turns 20` command in every arm.

## Interpretation and limits

| Hypothesis | Result | Disposition |
| --- | --- | --- |
| Guidance helps choose a feasible stock/policy after drift | All arms make the right stock and data-era choice; primary acceptance ties | No demonstrated incremental benefit |
| Guidance prevents learning from biased dispatch labels | Unaided agents also use admissible expected-cost policy | No demonstrated incremental benefit |
| Automatic availability leads to body use | 0/6 body loads; explicit 6/6 | Discovery/usefulness remain separate |

This improves on the preceding exact-code tasks by leaving implementation and
method choice open. It still has only **two constructed applications**. The
operations manuals provide unusually complete semantics; the no-training task
is solvable from those semantics. Scores are generated synthetic class-conditional
signals, not measured real model stocks. No actual encoder/LLM fitting, text-data
acquisition, label adjudication, provider comparison or production deployment
occurred. Repeated agents do not create new independent application types.
No dedicated nontrigger tasks were included; this is not a false-positive study.

The tasks are again saturated on acceptance for this strong agent. Do not broaden
the product claim, tighten the ceiling after looking, or force a skill change to
create a win. A materially different next experiment would use a real application
and messy source records, where data construction and validation choices are not
already resolved by the supplied manual. That proposal is not executed here.
The earlier independent confirmation packet remains unopened and unconsumed.

## Evidence and offline replay

```sh
python3 research/audits/2026-09-27-application-climb/selection/selftest.py
python3 research/audits/2026-09-27-application-climb/policy/private/validate.py
python3 research/audits/2026-09-27-application-climb/replay.py
make check
```

Python 3.12+ recommended (3.11 with extraction-filter support also works).
Replay checks 490 archive file hashes, the pre-run freeze, public inputs,
counterbalancing, paired prompts, skill inventories/loads, model metadata and
costs, then reruns every outcome grader. Parent replay reproduced all 18 results.
Repository check: 192 tests, both self-tests and shell syntax pass.

The selection instrument passes a reference and rejects seven bad policies;
hand-counted false-positive/false-negative anchors verify cost arithmetic.
The independently authored policy instrument passes eleven hand-derived anchors,
rejects seven bad policies and four artifact/serving violations. Parent reran
both validators before launch. Mac-specific isolation tests are archived runner
evidence, not claimed rerun on Linux. Parent credential-shape scan found no matches.

[Frozen contract](contract.md), [pre-run hashes](frozen-sha256.txt),
[parent replay results](replay-result.json), and `grades/` retain the analysis.
[Raw archive](initial-results.tar.gz), SHA256
`ea599e46d960c8d3353178868be81dff42211b2aa196456283390388ab5da304`,
contains exact solutions, self-tests, traces, configs, release snapshot and runner.
No auth files, private proxy logs or runtime homes; nonsecret absolute paths are
retained. `offline-validation` contains mock API evidence, excluded from inference.
Private task material was withheld from task agents until all runs completed;
it is now published for replay and is no longer an unseen evaluation set.
