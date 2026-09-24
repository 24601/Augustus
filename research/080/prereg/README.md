# Pre-registration locks

Two locks per experiment, hashed and dated here, with read-only copies under `/srv/aug/ctl` on
tabputer-1. The grader refuses to score confirmation data unless the analysis-lock hash matches.

| Lock | When | What it fixes |
| --- | --- | --- |
| **Design** | Before any experiment-dataset download or any read of dataset text or labels. Provisioning artifacts — wheels, the base image, the §4.4 acceptance weights — are not experiment data | Estimands, arms, controls, margin rules, family and m, α = 0.05, power 0.8, **the bound R on each loss**, the method, **the mode and its direction**, seeds, split proportions, the n rule, **`true_delta` per contrast**, caps, and the outcome rows |
| **Analysis** | After fitting, calibration and pilots; before any confirmation read | Split-manifest hashes, σ̂ per contrast, the numeric margins, the required n, the powered set, the allocation of n, the hashes of the frozen arms, and any prespecified narrowing. **It never re-chooses `true_delta` or a margin** |

## Status

Nothing is locked yet. M2 writes the four design locks (E1, E3, E4, M5) and they must be hashed
**before window W2 opens**, which is the only window that downloads experiment data.

| Experiment | Design lock | Analysis lock |
| --- | --- | --- |
| E1 cost and prior shift | not written | not written |
| E3 episode control | not written | not written |
| E4 acceptance machinery | not written | not written |
| M5 artifact-form ladder | not written | not written |
| M5b multimodal pilot | not written | not written |

## Format

One file per lock, `e1-design.md`, `e1-analysis.md`, and so on. Each begins with the date, the
plan commit it was written against, and the sha256 of the plan file. The maintainer adds a dated
note, and the hash of the finished file is recorded in the table above and copied to
`/srv/aug/ctl`.

A lock is a commitment, not a plan: once hashed, the only permitted change is a **prespecified**
narrowing that the lock itself already names. Anything else invalidates the experiment, and the
honest response is to say so and re-run, not to amend the lock.
