# M4 receipt: E1 partitions published under custody (2026-09-24)

Operator: an Amp thread on the runner `tabputer`, mode `gpt6a-med`, thread
`T-01a0d3f0-019d-7498-b7b7-a90c18471941`. Durable evidence on the host:
`/srv/aug/ctl/m4-evidence.json`, sha256 `2ab0cde0…`. **No row text and no label value was
printed at any point**, and no fitting or scoring ran.

## The blocker, and which fix won

`augctl` had pandas but no Parquet engine, no pyarrow, no duckdb, no fastparquet. It may not
install, may not run a container, and must not execute anything `augexp` fetched — and `augexp`
could not do the conversion instead, because converting touches every row **including the
confirmation labels**.

Four options were offered. **Option B won on the first try**: the host's own CPython 3.14.7 plus a
single `pyarrow 23.0.1` cp314 wheel, no dependencies, downloaded wheels-only in a
**three-second** proxy window (09:09:12–09:09:15 MDT) with **no allowlist edit**, since
`files.pythonhosted.org` was already allowed. Root verified the recorded wheel hash
(`4982d713…`) and all 749 installed files against the wheel, then moved the venv to
`/srv/aug/lib/venv`: 1,948 entries root-owned, **zero writable by `augctl`**, write probe
EACCES(13).

uv was never needed. python3.12/3.13 exist only under `/home/basit/.local/bin` and are not
executable by `augexp`, which is correct and was left alone. The stdlib Parquet reader
(`exp/parquet_min.py`) was therefore not used, and stays as insurance.

## What was partitioned

Normalization: splits in train, validation, test order; zero-based per-split ids.

| Corpus | Rows in | Exact duplicates dropped | Positive rate |
| --- | --- | --- | --- |
| CivilComments (`text`, `toxicity ≥ 0.5`) | 1,999,514 | 32,490 | **0.07991** |
| CLINC150 plus (`text`, intent = OOS class **42**, identified from each shard's ClassLabel names, 151 classes) | 23,850 | 5 | 0.05660 |

**The planning population was well chosen.** E1's synthetic planning population in `calc_v4.py`
assumed a prevalence of 0.08; the real CivilComments positive rate is 0.07991.

| Partition | CivilComments | CLINC |
| --- | --- | --- |
| fit | 200,000 | 8,000 |
| fit-B | 200,000 | — |
| calibration | 100,000 | 3,000 |
| M5 pool | 100,000 | — |
| **confirmation** | **1,367,024** | **12,845** |

## Reconciliation with the design lock

The lock said "about 1,400,000" for CivilComments confirmation and 12,850 for CLINC. The actual
figures are **1,367,024** and **12,845**, the difference being exact-duplicate removal, which the
lock requires and which happens before partitioning. Nothing in the lock is violated and no size
was adjusted: every planning n still fits. E1's equivalence contrasts need 78k to 688k rows and
its superiority contrasts 1,425 to 18,754 [Rep, `calc_v4.py` §2], all inside 1,367,024. CLINC was
already expected to power no equivalence contrast, and 12,845 does not change that.

## Custody and the audit

The overlap audit ran on partition ids and normalized texts only, one run per corpus, with
`confirmation_inputs` flagged. **Both clean**: no leaks, no other overlap, nothing uncheckable.

Published to `/srv/aug/stage/parts`, root:augexp, directories 0550 and `rows.json` 0440: eight
partitions, all eight literal file hashes verified against
`/srv/aug/ctl/publication-manifest-e1.json`. Confirmation inputs carry exactly `id, text` and **no
label column**. Retained labels are exactly `id, label`, `augctl`-owned 0600 under a 0700
directory. As `augexp`: all eight published partitions readable, zero writable, and an actual open
of either labels file returns **EACCES(13)**.

## Stated limits

- **The container probes were not repeated.** `augexp`'s `/run/user/48201` is absent and podman
  cannot initialize, because linger is disabled outside a window. Nothing was changed to work
  around that, which is the right call: it means containers cannot start at all right now. The
  host probes were repeated in full for both principals with zero failures, and ten proxied URL
  checks timed out after close, `pypi.org` and `files.pythonhosted.org` included.
- The audit's `clean` bounds **exact normalized overlap**, not semantic independence or
  near-duplicates, exactly as the tool says.
- Manifest partition digests are canonical-JSON digests, not literal file digests; both were
  computed and recorded separately, which is a distinction worth keeping.
- The runner used the repository-root `overlap_audit.py` (sha256 `f06ca03b…`) because the relative
  path in the task text did not exist; the file is unmodified.
