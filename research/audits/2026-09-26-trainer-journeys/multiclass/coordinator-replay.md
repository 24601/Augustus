# Coordinator replay and acceptance

2026-09-26. Inspected all four Python files, the predeclared contract, dependency
lock, source/license record and receipt. Retrieved archive SHA-256
`ed290ef8fe6f52d070dd92e99305ef3d2b1174fa4b1ee1a34461c8001f7268d6`;
it contained nine source/license/receipt files, no corpus or binary model.

Executed the README sequence with the exact six locked packages in a new
Python 3.11 environment and new `/tmp/augustus-multi-run` output directory.
The downloaded source/README/license hashes matched the worker's pinned revision.
Preparation reproduced the entire duplicate audit and split hashes. Confirmation
and raw source were moved outside the run directory before fitting and restored
after freeze. This is phase separation, not an enforced privilege boundary.

All three fits and 72 policies ran. The selected `word-char-svc` policy remained
top margin 0 / winner gap 0.25. Fit/search consumed **29.89 in-function CPU seconds**.
The serving checks passed hand-derived losses, boundary/tie/label-column cases,
fresh-process requests, and missing/corrupt-artifact fallback.

Worker and coordinator replay agreed exactly on development metrics, confirmation
metrics and all 150 intent recalls, selected policy, decision, conditional bound,
all declared gates, and post-freeze overlap sensitivity. **5,477 fresh-process
actions/reasons/queues matched**, with maximum observed margin drift 0.

Independently counted actions from the saved confirmation predictions, without
calling `experiment.metrics`: **3,755 correct routes, 185 misroutes, 1,537 reviews**.
The declared costs give `(185 + 0.3 × 1537) / 5477 = 0.11796603980281174` versus
0.3 for always-review. Independently evaluating the predeclared range-one
Hoeffding expression gives upper delta **−0.16549664017296636**. That expression
is appropriate for a constant-cost incumbent's difference range, but its
independent-unit assumption is not established by these public corpus rows.

Replay warm p95 **1.588 ms**, cold start **1.743 s**, peak RSS **288.23 MiB** satisfy
the declared local resource limits. Original timing receipts remain unchanged.

**Accepted as a working multiclass/public-proxy journey, not clean population
confirmation.** The source contains near-duplicate and unknown seed-family
dependencies; these are disclosed rather than hidden or declared clean. The
215 high-similarity rows are retained as diagnostics; the remaining 5,262-row
descriptive cost is 0.122558, not a new selected confirmation claim. OOS routing
still fails on 92 of 1,000 source OOS examples. Neither a calibrated probability,
arbitrary new-label support, universal unknown detection nor production safety
is claimed. The complete frozen inference path works and its limitations remain
visible; production promotion would require application-specific outcomes.
