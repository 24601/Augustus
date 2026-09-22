# Independent redo: offline evaluator and research collectors

Date: 2026-09-22. Scope disposition at initial inspection: **fix-first**.
The placement and tool architecture do not need a rethink. Ordinary metric
arithmetic, selective-policy accounting, and non-publishing collection hold up;
eight adversarial parser, identity, failure, and numeric cases need correction.
This is a tools-scope finding, not acceptance or rejection of the whole release.

## Identity, scope, and method

The coordinator requested a fresh GPT-6 Astra/xhigh redo of the earlier tool
review and implementation. This worker's instruction context identifies Codex
based on GPT-6; its tool outputs do not independently expose the routed model
name or reasoning effort. The coordinator must retain the model-routing receipt
separately. Python runtime results below are directly observed. No claim of
paid model inference, live source validation, or product acceptance follows.

Inspected the complete evaluator, collector, fingerprint helper, both shell
wrappers, and all three corresponding test files. Read AGENTS.md,
CONTRIBUTING.md, the Augustus skill, validation reference, research protocol,
fold prompt, and research README. Derived the checks from their contracts and
the mission before running existing tests. Did not read or adopt an earlier
tools audit as evidence. The memory registry had no relevant Augustus entry.

Git HEAD at inspection was published v0.6.0,
`192faf0d18d511154228af8ac40e1393567d828c`; the worktree carried the coordinator's
0.6.1-dev refresh. The five audited executable files and their tests were
identical to that HEAD at inspection. Compared the relevant arithmetic,
fingerprint, and wrapper logic with the pre-session baseline
`0b43a8d3b8d2d389b59415747f566dcbaa3f3ec8` without executing old scripts.

Initial executable SHA-256 values:

| File | SHA-256 |
| --- | --- |
| `.agents/skills/augustus/scripts/evaluate_decisions.py` | `772196cad3801f07eaf8b81893f4db691be2a1a8e16e191739ae5a863ac1ab7f` |
| `research/refresh.py` | `dbd35485665b31fe2e6595abacd631e2a12274da052c118ea54187f2313cafb7` |
| `research/revisit_fingerprints.py` | `362537406b3c678810af7fb8c27a1a1225489d59f307305317dc48b15d925a2d` |
| `scripts/hourly-refresh.sh` | `18fd7b3ff1f127692620878f5eccc93d7ac43fdd7e5b23cff55cea0ca81ed98a` |
| `scripts/refresh-jev-research.sh` | `590f39a98603890defe7e7cdcf0f5eb0ae728da5d6068fa7f888dd50eff8b399` |

Only this audit was written in the repository by this worker. Independent
probes were created with apply_patch under
`/tmp/augustus-astra-tools.WUWx3L/`. That path is temporary working evidence;
the reproducible cases, results, and commands are retained below. No network
request, paid search, inference, external write, Git mutation, or subagent
was used by this worker. The collector's HTTP dependencies were replaced with
local test doubles.

## Findings requiring correction

1. **Ambiguous evaluator JSON silently changes the judgment.** In `load`,
   `json.loads` accepts duplicate fields. The row
   `{"id":"ambiguous","p":0.01,"p":0.99,"y":0}` exits successfully and
   reports Brier `0.9801`; its first probability would yield `0.0001`.
   Reject duplicate object keys using an object-pairs hook. This is a parser
   ambiguity, not an arithmetic failure. Apply the same discipline to other
   evidence parsers when their input can contain conflicting duplicate fields.
2. **An explicit stable-identity conflict is ignored.** Fingerprint records
   with the same `id` and identical fields but `node_id` changing from `R_one`
   to `R_replacement` return `unchanged` / `skip`. The collector already
   preserves the stable node ID. Reject a comparison when both supplied
   stable IDs conflict. Do not infer rename or continuity from matching names.
   Historic records without node IDs need an explicit compatibility policy;
   absence must not be invented into a stable-identity match.
3. **Interrupted HTTP bodies abort all collection.** A response reader raising
   `http.client.IncompleteRead` escapes `fetch_url` and `collect`, losing the
   structured receipt and subsequent sources. Normalize relevant HTTP protocol
   exceptions into `RefreshError`; keep the source error and continue.
4. **A bounded but deeply nested response aborts all collection.** JSON with
   10,000 nested arrays is only 20,007 bytes, below the 262,144-byte body cap,
   but raises `RecursionError` instead of producing a source-error receipt.
   Normalize decoder depth failures; a byte cap alone does not bound nesting.
5. **Huge JSON integers escape ordinary evaluator validation.** `p=10**400`
   reaches `float(value)` and raises `OverflowError` outside the error handler.
   Convert the overflow to the same normal input error as other invalid
   probabilities, before any metric report is emitted.
6. **Finite mean costs overflow through an intermediate product.** Two false
   positives with finite `C_FP=1e308` should have population mean cost `1e308`;
   both complete and selective calculations return infinity because they
   multiply counts before dividing. Multiply costs by event fractions instead.
   This is a real numerical defect at extreme finite inputs, not evidence of
   likely ordinary business-cost failure.
7. **The collector can emit an unclassifiable successful receipt.** Its
   timestamp parser accepts `2026-09-22 00:00:00Z`; fingerprint validation
   requires `T` and rejects the same receipt. Align the accepted timestamp
   grammar so every successful collector fingerprint can be classified.
8. **Boolean schema versions are accepted.** `load_store` accepts
   `schema_version: true` because Python equates `True` and `1`. Require an
   integer version excluding booleans. This is lower-severity schema strictness.

Precise correction locations in the initial source: evaluator `load`,
`_finite_number`, `_complete_cost`, and `selective_policy`; collector
`fetch_url`, `_json`, and `_utc_timestamp`; fingerprint `classify` and
`load_store`. Implementation ownership remains with the coordinator so no
concurrent implementation/test edits were made by this worker.

## Independently reproduced behavior that passed

The fresh harness used actual outputs and arithmetic oracles. It did not
check a slogan, return a supplied expected boolean, or equate a static
`capability_change_claimed=False` field with verified semantic safety.

- Seed `20260922`: 500 datasets of 1–24 rows, probabilities in tenths and
  binary outcomes. Compared Brier against Decimal arithmetic, AUC against
  all positive/negative pairs with half credit for ties, and optimal policy
  cost against exhaustive thresholds including always-negative. Confirmed
  equal-width bin count conservation and ECE for 2, 3, and 7 bins, plus
  quantile ECE invariance under tied-probability row permutations.
- Exhausted 1,000 three-row combinations from probabilities
  `{0,.25,.5,.75,1}` and both outcomes. Independently assigned negative,
  positive, or abstain at `.25/.75` boundaries; compared decided coverage,
  abstention rate, conditional selective error, and total-population costs
  for false-positive/false-negative/abstention costs `3/7/.5`.
- Undefined selective error for all-abstain, missing-cost unknowns, one-class
  AUC, exact-impossible-outcome infinite log loss, invalid probabilities,
  duplicate row IDs, and full-versus-partial baseline behavior are retained.
  Ordinary costs matched arithmetic; the finite extreme above did not.
- GitHub path validation rejected URLs, command fragments, traversal,
  query strings, fragments, and newlines without any fetch call. Slash-bearing
  branches were percent encoded. Receipts preserved requested name,
  canonical name, and node ID; the empty-description hash was independently
  checked against known SHA-256 prefix `e3b0c44298fc`.
- HTTP 400/401/403/429/500/503 became explicit source errors. Latest-release
  404 stayed null/unknown; it did not establish model or repository absence.
  An invalid first source did not prevent a valid second source receipt.
  Exactly 262,144 bytes were accepted; 262,145 were rejected before parsing.
- Fingerprint changes and null transitions requested inspection, material
  signal labels requested a material revisit, and star-only movement stayed
  an observation. Those labels route review; they cannot prove that a human
  inspected a source or that its capabilities changed.
- Ran the real hourly wrapper with an invalid source, which cannot reach
  HTTP. Stdout remained a parseable error receipt with exit 1; diagnostics
  stayed on stderr. The tracked fingerprint and refresh-log diffs were
  identical before and after. Complete source inspection found no staging,
  committing, pushing, cloning, publishing, cadence ownership, or command
  execution based on retrieved text. Only an explicitly requested new receipt
  path can be written; existing output paths are refused.

Compared with the old baseline, selective-policy coverage is now distinct
from positive action rate, probability ties stay together in quantile ECE,
AUC avoids the old pairwise quadratic path, costs are explicit, fingerprint
movement requests inspection rather than declaring a material finding, and
the old automatic `git add -A` / commit / push loop is absent. These are
independently inspected improvements, not grandfathered acceptance.

## Commands and observed results

```text
make check
  PASS: Python 3.14.7; structural checker, 53 unit tests,
  evaluator/fingerprint numerical smoke checks, shell syntax.
python3.11 -m unittest discover -s tests -p 'test_evaluate_decisions.py' -v
python3.11 -m unittest discover -s tests -p 'test_refresh.py' -v
python3.11 -m unittest discover -s tests -p 'test_revisit_fingerprints.py' -v
  PASS: 12 + 10 + 7 tests; Python 3.11.16.
python3.12 -m unittest discover -s tests -p 'test_evaluate_decisions.py' -v
python3.12 -m unittest discover -s tests -p 'test_refresh.py' -v
python3.12 -m unittest discover -s tests -p 'test_revisit_fingerprints.py' -v
  PASS: 12 + 10 + 7 tests; Python 3.12.13.
shellcheck scripts/hourly-refresh.sh scripts/refresh-jev-research.sh
  PASS: ShellCheck 0.11.0.
git diff --check
  PASS at initial inspection.
make check PYTHON=python3.11
make check PYTHON=python3.12
  BLOCKED before tests: these bare interpreters lack PyYAML.
python3.11 /tmp/augustus-astra-tools.WUWx3L/test_astra_tools.py
python3.12 /tmp/augustus-astra-tools.WUWx3L/test_astra_tools.py
  Initial 20-case adversarial suite on each runtime:
  12 passed, 4 failed, 4 errored.
```

The first deep-JSON probe used 1,100 arrays: it raised under Python 3.11,
but Python 3.12 decoded it and then reported a missing-field error normally.
The retained probe uses 10,000 arrays to exercise decoder exhaustion on both
versions. This difference is a runtime observation, not an implementation
fix. Post-correction results, if any, must be recorded separately.

Resource observations: the collector bounds each actual response body and
passes a 15-second socket timeout, but has no total elapsed-time deadline
or source-count budget. The evaluator loads all rows, equal-width reporting
costs O(rows × bins), and exact threshold selection currently costs O(rows²)
for distinct probabilities. A local Python 3.11 timing probe measured
1,000/2,000/4,000 rows at 0.057327/0.216079/0.841879 seconds, consistent with
the source-level quadratic analysis. These tools suit bounded local review;
no large-dataset or hard-deadline guarantee was tested or established.

## Durable minimal reproductions

The following can be pasted into Python from the repository root; all
responses and input lines are local. Each expression describes the initial
observed result so the evidence remains usable after temporary files expire.

```python
import importlib.util, json, sys
from pathlib import Path
from unittest.mock import patch
from http.client import IncompleteRead

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result

e = load_module('redo_e', '.agents/skills/augustus/scripts/evaluate_decisions.py')
r = load_module('redo_r', 'research/refresh.py')
f = load_module('redo_f', 'research/revisit_fingerprints.py')

# Initial: accepts p=.99. Required: ValueError for duplicate field.
with patch.object(e, '_utf8_lines', return_value=iter([
    '{"id":"x","p":0.01,"p":0.99,"y":0}'
])):
    e.load('unused')

# Initial: OverflowError. Required: normal ValueError input rejection.
e._finite_number(10**400, 'p')

# Initial: inf in both cases. Required: finite population mean 1e308.
rows = [{'p': .9, 'y': 0}, {'p': .9, 'y': 0}]
e.sweep(rows, [.5], 1e308, 1)[0]['cost']
e.selective_policy(rows, .2, .8, 1e308, 1, .5)['cost']

before = {'id': 'github:owner/repo', 'node_id': 'R_one', 'fingerprints': {
    'default_sha': 'a'*40, 'pushed_at': '2026-09-22T00:00:00Z',
    'description_hash': '123456789abc', 'release_tag': None}}
# Initial: unchanged/skip. Required: reject contradictory stable identity.
f.classify(before, dict(before, node_id='R_replacement'))

# Initial: returns the object. Required: reject boolean schema_version.
store = {'schema_version': True, 'stored_fields': list(f.STORED_FIELDS),
         'looks': [before]}
with patch.object(Path, 'read_text', return_value=json.dumps(store)):
    f.load_store(Path('unused'))

# Initial: collector parser accepts; fingerprint parser rejects.
stamp = r._utc_timestamp('2026-09-22 00:00:00Z', 'probe')
f._validate_fingerprint(dict(before['fingerprints'], pushed_at=stamp))

# Initial: RecursionError rather than structured per-source failure.
deep = b'{"a":' + b'['*10000 + b'0' + b']'*10000 + b'}'
r.collect(['github:owner/repo'], lambda *_: r.HttpResponse(200, deep))

# Initial: IncompleteRead rather than structured per-source failure.
class PartialResponse:
    status = 200
    def __enter__(self): return self
    def __exit__(self, *_): return False
    def read(self, size): raise IncompleteRead(b'partial', 20)
with patch.object(r, 'urlopen', return_value=PartialResponse()):
    r.collect(['github:owner/repo'])
```

No live API reachability, identity-renaming event, reviewer completion,
calibration, model quality, deployed action success, behavioral skill
acceptance, installation, or release outcome was verified by these offline
checks. The recommendation is to correct the concrete failures, add actual
regression cases, and re-run the focused probes and full offline checks.
