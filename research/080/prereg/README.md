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
| E1 cost and prior shift | [`e1-design.md`](e1-design.md) | `863a5aa0f430d3de…` (amended 2026-09-24 with the actual post-dedup counts; no size or margin changed) | **written 2026-09-24, before any confirmation ANSWER was read**: [civil](e1-analysis-lock-civil.md) `d73243e3f7788951…`, [clinc](e1-analysis-lock-clinc.md) `e622b93356088349…` |
| E3 episode control | [`e3-design.md`](e3-design.md) | `45a821fae045ada1…` (amended 2026-09-24 to record the reader revisions the original left as "pinned revisions"; no size, margin or family changed. Previously `a9422bf234dc285e…`) | **written and committed 2026-09-24T22:04:46Z, two minutes before the confirmation replay even started and 2h22m before any confirmation answer was read**: [e3-analysis-lock.md](e3-analysis-lock.md) `fcb626f07d0884f6…`. The prespecified narrowing fired on σ̂ and did not help; both facts are in the lock |
| E4 acceptance machinery | [`e4-design.md`](e4-design.md) | `1ab9e78deb838ee8…` | **executed**; see the E4a, E4b and E4c receipts |
| M5 artifact-form ladder | [`m5-design.md`](m5-design.md) | `fcdeadd28a9dde76…` (amended 2026-09-25 to record that the registered readout Qwen3.5-2B-Base is natively multimodal; no arm, margin or family changed. Previously `d24e2b27a89e6e56…`) | not written |
| M5b multimodal pilot | not written | — | not written |

## The recorded-lock binding, and a gap in how it was built

`e1_score.py` refuses to open confirmation labels unless the analysis-lock hash it is given matches
one **recorded with the split**. When scoring was reached, no such hash existed: M4 published the
splits on 2026-09-24 before any analysis lock had been derived, so the manifests had nowhere to put
one. The slot was missing, not the lock.

The repair is a one-time binding written by `augctl` into each split manifest, and it is worth
being exact about what it does and does not prove. E3's hotpot binding went through three
generations before it said something true: the first claimed the lock was verified "before the
replay was launched", which its own `recorded_at` contradicts by six minutes; the second fixed the
ordering; the third added the hedge that matters most, which is that "the scoring run was the first
read of a confirmation answer" is a custodian assertion about an unlogged interval. The host runs
no auditd and `/srv` is `noatime`, so an earlier open cannot be disproved, only made inaccessible
by custody. All three generations are preserved beside the unbound original.

Recording the hash after the fact is an assertion by the custodian. What makes the ordering checkable by someone who was not present is independent of that
assertion:

- both lock files are in a public commit, [`0bbb5b2`](https://github.com/24601/Augustus/commit/0bbb5b2),
  whose time precedes any confirmation label being read;
- for E1, the prediction artifacts were produced **before** the binding, are hashed, and each
  carries the `analysis_lock_sha256` it ran under; for E3 the ordering is stronger still, because
  the lock commit at 22:04:46Z precedes even the start of the confirmation replay at 22:06:46Z;
- the locks are derived, not written: the same fit report always yields the same file, and the fit
  reports are hashed and preserved.

A binding recorded after the fact is weaker than one recorded at publication, and saying so is
part of the record. The fix for the next experiment is to have the partitioner write the field at
publication time, empty, so there is a slot to fill rather than a slot to add.

## Format

One file per lock, `e1-design.md`, `e1-analysis.md`, and so on. Each begins with the date, the
plan commit it was written against, and the sha256 of the plan file. The maintainer adds a dated
note, and the hash of the finished file is recorded in the table above and copied to
`/srv/aug/ctl`.

A lock is a commitment, not a plan: once hashed, the only permitted change is a **prespecified**
narrowing that the lock itself already names. Anything else invalidates the experiment, and the
honest response is to say so and re-run, not to amend the lock.
