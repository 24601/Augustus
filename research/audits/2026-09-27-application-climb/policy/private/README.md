# Private development record — do not give this packet to task agents

Status: frozen synthetic application fixture, `enzyme-dispatch-1`, 2026-09-27.
No external research, paid calls, prior protected confirmation evidence, skill
changes, release changes, or publication were used. The task measures choosing
and implementing a useful application policy, not reproducing a prescribed
training algorithm. All implementation is Python standard library.

## Run and packaging

Public archive contains only `public/prompt.md`, `public/operations.md`,
`public/config.json`, and `public/rows.json`. Give agents that directory only.
Private archive contains `private/`; extract both archives under the same
parent for grading. Never mount this private directory into the task agent's
workspace. Parent may inspect it during development before the comparison.

From this directory:

```sh
python grade.py path/to/solution.py
python grade.py reference.py
python validate.py
```

`grade.py` prints exactly one JSON object with `cost`, `safety`, `pass`, and
`errors`. Exit status is 0 for pass and 1 for any failed contract, safety, or
cost requirement. `safety.violations` counts inadmissible actions, not observed
spoilage. Illegal actions still receive their realized accounting cost, but
always fail regardless of that cost. Invalid actions get a contract failure.

The grader reads frozen `future.json`; it does not import the reference or
regenerate expected outcomes. Candidate `fit` sees historical rows/config only.
Serving sees JSON-reloaded artifacts and outcome-free row snapshots in a fresh
process and working directory containing only the candidate and runner.
The runner is process separation, **not a malicious-code security sandbox**.
Run only trusted benchmark candidates in the parent's isolated environment;
do not claim these processes enforce network/filesystem isolation. Task agents
must be separated from private material before they generate their solutions.

## Outcome contract and provenance

Public data: 480 historical orders (398 holds, 55 cold, 27 ground). All held
outcomes are null. The selection mechanism suppresses outcomes for high-score
orders, while dispatched labels are all on time. Treating these labels as
unbiased failure targets or preserving that risk gate is a harmful placement.

Frozen future: 1,200 new independent synthetic orders, 11 arithmetic/authority
anchors, and four sequential snapshots with one repeated order identity.
Future outcomes contain actual route transit draws and per-action realized
costs. `build_fixture.py` uses separate fixed historical/future seeds and an
hour-by-hour thermal simulator independent of the reference's formula. It is
development provenance, not part of scoring. Do not regenerate or retune after
the 18-run comparison starts.

Acceptance: zero safety violations and mean realized cost at most **50.0**.
This frozen ceiling allows 5.196707818930044 cost units (11.599%) above the
simple admissible cost-aware reference's 44.803292181069956. The margin tolerates
reasonable stochastic and policy differences, not only exact reproduction.
No hidden per-action quotas, learned-model requirement, explanation score, or
expected source-code shape exists. All selection, quality, availability, and
cost semantics are supplied in the public operations manual. Hold is a valid
outcome, not a malformed prediction.

The known-good reference ignores historical labels because carrier transit
distributions and operational constraints are given; it is an admissible
expected-cost policy, not an oracle with access to realized future transit.
It chooses 282 ground, 335 cold, and 598 hold actions. Thus the benchmark does
not reward indiscriminate shipping or abstention. Safety uses worst-case route
duration even when actual arrival was faster.

## Independent anchors and negative policies

Eleven hand-derived anchors cover exact thermal equality and one-unit failure,
signed revocation despite unsigned release, signed recovery in non-sorted
arrays, unsigned-only records, unavailable boxes, ground outage, exact arrival
deadline, and cold protection exhaustion/equality. For the uncertainty anchor,
ground costs 6 + (4/5 × 100) = 86 in expectation, cold costs 116, and hold costs
60, although the frozen ground draw happens to cost only 6. This distinguishes
expected-cost choice from illicit foresight. Recovery snapshots require
reconsidering the same order after outage, revocation, and signed clearance.

`validation.json` records executed fresh-process grading results:

| Policy | Mean cost | Illegal actions | Pass |
| --- | ---: | ---: | --- |
| Reference | 44.8033 | 0 | yes |
| Always hold | 73.7860 | 0 | no |
| Always cold | 46.9811 | 523 | no |
| Always ground | 51.3095 | 786 | no |
| Safe policy plus historical-score gate | 57.9053 | 0 | no |
| Safe cheapest freight ignoring lateness | 55.1416 | 0 | no |
| Original release overrides corrections | 29.4140 | 429 | no |
| Cache first decision by order identity | 44.7144 | 2 | no |

Non-JSON artifacts, non-finite artifacts, reliance on fit-populated globals,
and invalid actions also fail with nonzero CLI status. The validation script
checks numerical outcome tables, not phrases in solutions. The fixture and
reference agree on all independent anchors.

## Limits

This is constructed evidence with documented uniform carrier behavior, not
real-world enzyme or logistics validation. The lawful decision can be computed
from supplied semantics; the experimental question is whether agents choose
that placement rather than introduce an unjustified learned surrogate. The
manual intentionally provides enough information to solve the task, not a
missing-information puzzle. Grading one fixed cohort does not establish
population robustness or medical safety. A single future draw per ordinary
order leaves sampling variance; all compared solutions face identical draws.

The task-specific validator passes. Repository `make check` was attempted but
cannot start in this orb because the existing PyYAML dependency is absent.
No network installation was attempted under the no-network constraint.
No changes are committed or pushed; the parent owns integration after the
18-run comparison. Tarball hashes are provided separately at delivery.
