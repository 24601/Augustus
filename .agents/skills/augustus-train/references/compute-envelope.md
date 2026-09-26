# Budget the actual fit and serving path

Use this card before a costly fit or runtime optimization. Its assumption is that
you can measure a representative small batch; if input length, device or backend
differs from deployment, report that limitation rather than extrapolating a guarantee.
CPU methods and no-fit programs often avoid a GPU entirely. No rental or paid call
is authorized by this guidance.

## Preflight with an explicit stop

Record task/input and option counts, length distribution, precision, trainable
parameters, batch and accumulation, optimizer, device/runtime versions and data
residency. Check model/license access, disk, RAM, accelerator memory and artifact
export before a long run. Execute one real batch and save/reload a checkpoint.

Measure startup separately from steady-state fit and inference, then project the
declared workload with headroom and uncertainty. Set a wall-clock/spend/memory
stop. Include labeling/teacher calls, evaluation, failed trials, storage and
fallback—not just the final training job. Check expensive cases such as longest
inputs and largest candidate lists, not only median examples.

On an accelerator, use backend-appropriate placement/profiling evidence and
process-attributable device memory/work. A capability flag, package installation
or device-init line does not prove the forward/backward work uses the GPU.
llama.cpp layer-assignment logs are useful for that backend; they are not a
universal requirement for every trainer. Synchronize accelerator timing where
needed. Preserve logs without credentials or private inputs.

## Change the bottleneck, then test equivalence to the required tolerance

Batching, replicas, caching, precision, adapter merging and runtime changes can
reduce cost. None is automatically behavior-preserving. Before relying on the
speedup, declare acceptable numerical drift, action changes, loss and constraint
regressions relative to the unoptimized path. Probe ordinary and threshold-boundary
inputs under the realistic batch/length mix. Use exact equality only where the
contract needs it. A small average score drift can hide a costly action change.

Gradient accumulation can preserve nominal effective batch while changing floating
point order, dropout, batch-dependent layers or optimizer scheduling. Check example
counts, update counts and the resulting candidate; do not call it identical merely
because micro-batch × accumulation stayed constant. Reducing examples, steps,
context or options, changing base weights or precision, and changing sampling
are recorded recipe/runtime revisions, not invisible rescue operations.

**Falsifier:** if the measured end-to-end gain disappears with startup/fallback
included, or exceeds an agreed regression tolerance, reject that optimization.
An optimization error comparable to the improvement being claimed can invalidate
the comparison even if average accuracy appears unchanged.

## Historical measurements are starting hypotheses, not requirements

**Reported**, not reproduced here: the
[M5 receipt](https://github.com/24601/Augustus/blob/cd6b904f6af412adb643bdcf6281bfcccb33952b/research/080/receipts/m5-grading-2026-09-25.md)
and [PAW run notes](https://github.com/24601/Augustus/blob/cd6b904f6af412adb643bdcf6281bfcccb33952b/research/080/sources/paw-rap-2026-09-23.md)
describe configurations that changed resource cost markedly:

- A LoRA fit at batch 48 used about 69 GiB despite a 38 GiB preflight estimate.
  Micro-batch 12 with accumulation 4 reduced reported use to 24,457 MiB.
  That is a measured configuration, not a universal 24 GiB requirement.
- [imajev run notes](https://github.com/24601/Augustus/blob/cd6b904f6af412adb643bdcf6281bfcccb33952b/research/080/sources/imajev-anyjev-2026-09-25.md)
  report roughly 328 ms per single request on both L4 and A100, whereas three
  replicas reached about 8.2 rows/s. This suggests concurrency/launch overhead as
  a bottleneck for that workload; it does not imply larger GPUs never help.
- AnyJev's 77-option task required four subquestions and 81 prefills per row,
  around 0.63 rows/s, versus 37–61 rows/s on its binary tasks. Option count and
  decomposition changed the work. Cyclic shifts gave zero observed flips on the
  binary probe, not universal invariance on the partitioned multiclass task.

These examples motivate measuring fit and serve separately. They do not predict
your task's memory, speed, winner or minimum data requirement. Compare candidate
forms under the same product contract and declared budgets, allowing different
appropriate methods rather than demanding identical training recipes.

## Recover without silently changing the experiment

Use the host's supported service/job supervision. Persist checkpoints, RNG and
optimizer state when needed, selected artifact and versioned partial results to
an approved durable location. Save expensive synthesized data as soon as it exists.
Resume by run/candidate/input identity, verifying hashes and configuration before
skipping completed work. Never append new predictions under an old artifact ID.

Write progress and errors incrementally, deduplicate retries, verify expected IDs
and count omissions at completion. Record interrupted segments in timing receipts;
segment throughput is not whole-job wall clock. Test one interruption/reload path
before relying on it for a long run. Retain the incumbent when compute is exhausted
before independent acceptance; an unfinished fit is not a trained deployment.
