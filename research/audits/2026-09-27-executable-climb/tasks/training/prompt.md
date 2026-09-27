# Fit, export and serve a tiny soft-target classifier

Build `solution.py` with standard-library Python only. This local component learns
a logistic predictor for one numeric feature from supplied probability targets.
No network/packages. Implement the functions and CLI below, and run actual fits
and fresh-process serving checks. Targets are probabilities, not hard classes.

`fit(rows, epochs, lr)` takes objects with finite numeric `x` and `target` in
[0,1]. Use a logistic model sigmoid(w*x+b), zero-initialized w and b, full-batch
gradient descent on mean binary cross entropy, and exactly epochs updates with
the supplied positive learning rate. Both parameters update simultaneously from
the same old parameters on each step. Return exactly `{"w": w, "b": b}`.
Do not replace targets with class labels or silently add regularization.

`export(path, model, temperature, fn_cost, fp_cost)` writes one self-contained
JSON inference artifact, refusing to overwrite an existing path. The calibrated
logit is (w*x+b)/temperature. Temperature and both action costs must be finite,
positive numbers, not booleans. Reject invalid values with ValueError before
creating an artifact. `load(path)` returns the bundle and must refuse a missing
or invalid required temperature or action cost (ValueError or KeyError).

`predict(bundle, x)` returns exactly `{"p": probability, "action": ...}`.
Use the supplied calibrated probability and error costs to minimize expected
loss: a false positive costs fp_cost, a false negative costs fn_cost. Choose
`"negative"` on an exact tie, otherwise `"positive"` or `"negative"` as appropriate.
Probabilities must remain finite for finite logits of either sign, including
very large magnitude. Bundle may be your own documented JSON schema, but must
have top-level `temperature`, `fn_cost`, `fp_cost` keys for required-policy checks.

CLI: `python3 solution.py fit training.json artifact.json`, where training.json
contains rows, epochs, lr, temperature, fn_cost, fp_cost. Then
`python3 solution.py predict artifact.json` reads JSONL objects `{"x": number}`
and writes one prediction per line. Serving must work in a fresh process with
only solution.py and the artifact, after removing the training file.
