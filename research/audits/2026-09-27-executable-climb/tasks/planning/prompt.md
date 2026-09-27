# Make the experiment plan executable

Implement `solution.py` in standard-library Python with two functions below and
a JSON stdin/stdout CLI dispatched by `op` (`curve` or `select`). No network or
package installation. This is exact planning/selection code, not a model call.

`curve(rows, folds, sizes)`:
Rows contain unique `id`, `group`, and `label` strings. Each element of `folds`
is a list of held-out row IDs; only listed IDs are explicitly held out, but all
rows sharing a group with any listed ID must also be excluded from that fold's
training pool. Reject unknown IDs with ValueError. Report a list of fold objects,
in input order: `{"available": {label: count}, "sizes": [...]}`. Count available
rows for every label in the original rows, including zero. `sizes` is the sorted
unique positive integers from the requested sizes that are achievable for EVERY
class using only that fold's training pool. Do not oversample or move validation
rows into training to satisfy a requested size. Exclude booleans and non-integers
from requested sizes. Reject duplicate row IDs with ValueError.

`select(candidates, horizon, fn_cost, fp_cost, max_latency)`:
Each candidate has `name`, `n`, `fn`, `fp`, `latency_ms`, `fit_cost`, and
`already_paid`. Counts describe a common untouched evaluation population;
the caller guarantees n > 0 and nonnegative finite costs/counts. For the stated
future horizon compare expected FN/FP error costs plus future fit cost. A fit
cost already paid is sunk and must not be paid again. Exclude candidates whose
latency exceeds max_latency. Return null if none feasible, otherwise an object
with exactly `name` and `total_cost` for the cheapest candidate; break equal
costs by lexicographic name. The CLI receives named function arguments next to
`op`. Preserve fractional error rates until final output, without rounding money.

Implement and exercise actual boundary cases, not just a prose recommendation.
