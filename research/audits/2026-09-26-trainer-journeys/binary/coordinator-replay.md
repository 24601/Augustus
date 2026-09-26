# Coordinator replay and acceptance

2026-09-26. Inspected the entire `journey.py`, `sms.py`, `verify.py`, contract,
dependency lock, source/label notes and receipts before execution. Retrieved the
worker's archive with SHA-256
`ed1a60a1355d0a81b1b27533ba1718f18a5841588865143a52bf7728535f30a0`;
its 22 files contained source/receipts only, no model or corpus.

Executed the README sequence from a separate temporary copy, creating a new
Python 3.11 environment with the exact five locked packages. Downloaded and
hash-verified the UCI source, prepared groups/splits, fitted `word1`, `word8`,
`char8`, froze, confirmed and ran `verify.py`. **Six tests passed.** The new fit
selected the same `word8`, threshold 0.45, with the same split/contract hashes.
Worker and replay agreed exactly on confusion counts, group/row losses, paired
delta, bootstrap upper bound, all reported confirmation statuses and acceptance.
The fresh-process check replayed all **1,025 rows** with unchanged actions/statuses
and score tolerance 1e-12.

Independent calculation directly from source confirmation labels and saved CLI
decisions (without `journey.metrics`) gave **FP 2, FN 15, TP 111, TN 897**.
Using the fixed 5/1 loss matrix, averaging within groups and then across groups,
candidate-minus-incumbent loss was **−0.08349900596421471**. All fallback rows
were included. The approximate bootstrap and representativeness limits in the
original receipt remain; the coordinator did not upgrade them to a distribution-
free guarantee or production outcome.

Replay warm p95 was **0.576 ms**, cold start **0.891 s**, peak RSS **122.00 MiB**,
within the declared envelope. Original timings remain in original receipts.

An initially overstrict coordinator comparison also demanded the *refitted*
joblib bytes match the worker's artifact. They did not: original digest
`93a44838427cf156a12eb46fb16ae43b8f5a6e33f8fccdf425d484f843696649`,
replay digest `23362a34840ad6398c551728a7585278657ca43f25d6e232b7540021aa5456d6`.
No bitwise-refit claim was part of the application contract. Both artifacts
passed their own digest-verified fresh-process inference checks; selected policy,
metrics and recorded probe scores matched. The byte difference's cause was not
isolated, and parameter/score equality on every row across the two refits is not
claimed. Do not reuse the worker's digest for the newly fitted bundle.

**Accepted as a working public-proxy journey.** Three real fits include a rejected
character candidate; selection uses development groups only and the final fit is
not changed after confirmation. The CLI is usable offline, preserves messages on
failure and does not authorize deletion. This supports data assembly, feasible
method selection, bounded improvement and export/reload—not general Jev training,
new-campaign efficacy, or causal proof that the skill improved the agent.
