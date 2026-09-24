# Pre-registration locks

Two locks per experiment, hashed and dated here, with read-only copies under `/srv/aug/ctl` on
tabputer-1. The grader refuses to score confirmation data unless the analysis-lock hash matches.

| Lock | When | What it fixes |
| --- | --- | --- |
| **Design** | Before any experiment-dataset download or any read of dataset text or labels. Provisioning artifacts — wheels, the base image, the §4.4 acceptance weights — are not experiment data | Estimands, arms, controls, margin rules, family and m, α = 0.05, power 0.8, **the bound R on each loss**, the method, **the mode and its direction**, seeds, split proportions, the n rule, **`true_delta` per contrast**, caps, and the outcome rows |
| **Analysis** | After fitting, calibration and pilots; before any confirmation read | Split-manifest hashes, σ̂ per contrast, the numeric margins, the required n, the powered set, the allocation of n, the hashes of the frozen arms, and any prespecified narrowing. **It never re-chooses `true_delta` or a margin** |

## Status

**The four design locks are written and hashed (2026-09-24), before window W2 has ever opened.**
No experiment dataset is on tabputer-1: `/srv/aug/stage` holds only the base image and the §4.4
acceptance weights, verified read-only in `receipts/m0-state-check-2026-09-24.md`. So the ordering
the locks exist to guarantee — commitment before data — holds as a matter of record, not of
assertion.

E4 needs no dataset and has already run; its receipts are in `receipts/`. E1, E3 and M5 wait for
W2. The maintainer's standing authorization to proceed is in the 0.8.0 working thread; these locks
are operator-signed, and their value is the hash recorded here before any data was read.

| Experiment | Design lock | sha256 | Analysis lock |
| --- | --- | --- | --- |
| E1 cost and prior shift | [`e1-design.md`](e1-design.md) | `e38ab71dbd90640e…` (amended 2026-09-24 with the actual post-dedup counts; no size or margin changed) | not written |
| E3 episode control | [`e3-design.md`](e3-design.md) | `a9422bf234dc285e…` | not written |
| E4 acceptance machinery | [`e4-design.md`](e4-design.md) | `1ab9e78deb838ee8…` | **executed**; see the E4a, E4b and E4c receipts |
| M5 artifact-form ladder | [`m5-design.md`](m5-design.md) | `d24e2b27a89e6e56…` | not written |
| M5b multimodal pilot | not written | — | not written |

## Format

One file per lock, `e1-design.md`, `e1-analysis.md`, and so on. Each begins with the date, the
plan commit it was written against, and the sha256 of the plan file. The maintainer adds a dated
note, and the hash of the finished file is recorded in the table above and copied to
`/srv/aug/ctl`.

A lock is a commitment, not a plan: once hashed, the only permitted change is a **prespecified**
narrowing that the lock itself already names. Anything else invalidates the experiment, and the
honest response is to say so and re-run, not to amend the lock.
