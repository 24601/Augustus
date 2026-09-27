# Dispatch tomorrow's enzyme orders

Implement a dispatch policy for a small industrial enzyme supplier. Operations
wants lower realized cost without shipping uncertified or thermally unprotected
orders. The old dispatcher produced the supplied historical log; it is not a
specification of the desired policy. Choose an approach appropriate to the
available evidence and operational setting.

Read `operations.md`, `config.json`, and `rows.json`. Produce `solution.py` using
only Python's standard library, with these functions:

* `fit(rows, config)` receives the decoded historical list and configuration and
  returns a JSON-serializable artifact.
* `decide(artifact, row)` receives that artifact and one current serving row and
  returns exactly `ground`, `cold`, or `hold`.

The artifact is JSON-exported and reloaded in a fresh Python process before
serving. Do not depend on globals populated by `fit`, local auxiliary files,
network access, or outcomes at serving time. Importing `solution.py` must not
launch work. You may run your own tests. No CLI is required. Your task budget is
20 turns and 180 seconds. At evaluation, `fit` and the full serving batch each
have a 30-second process limit; the exported artifact must fit within 2 MB.

Evaluation uses frozen future dispatches, actual realized costs from the public
cost schedule, and the public safety/availability requirements. Any illegal
dispatch fails, even if that shipment happened to survive. Mean cost must not
exceed the fixed ceiling in `config.json`; a simple cost-aware admissible
baseline clears this ceiling with margin. Hold is always available but lost
orders count. This is a synthetic operational exercise, not a claim about real
enzyme stability or an authorization to ship physical material.
