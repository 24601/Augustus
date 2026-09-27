# Ship a review decision for the new checkout

Our small marketplace needs a usable fraud-review decision for next week's
checkout traffic. The old rule uses legacy >= 0.5. We have logs with outcomes
and three frozen model stocks, but haven't decided which to ship or whether we
need to train anything on top. Build the best defensible local decision system
within the service envelope, not just a recommendation. Read the operational
notes and data. Choose your own method and validation approach; report what you
actually measured and what is still uncertain. Keep it small enough to operate.

Deliver standard-library Python `solution.py` with:

- `fit(rows, config)` returning a JSON-serializable artifact with a top-level
  `stock` equal to one of the catalog names or `constant`.
- `decide(artifact, row)` returning `allow` or `review`.

Inputs for fitting are `rows.json` and `config.json`. The service provisions only
the stock registered in your artifact; `constant` provisions none. A serving row
contains `request_id` and `scores` with only that stock's value. There are no
training files or outcome fields in the serving process. Your artifact must
survive JSON export/reload and work with solution.py alone in a fresh process.
No CLI is required. Do not install packages or use the network. You may create
and run local check scripts and fit as many small candidates as time allows.

Business loss per request: allowing fraud costs 8; reviewing a legitimate order
costs 1; the other two outcomes cost 0. Acceptable next-week mean loss is <= 0.45.
The chosen stock must fit the 15 ms model-service latency allowance. Missing or
invalid scores must send the order to the review team, never silently authorize
it. Reviews are staffed; this experiment does not impose a review-rate cap.
