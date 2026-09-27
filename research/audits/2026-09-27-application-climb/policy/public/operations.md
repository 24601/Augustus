# Pilot operations manual — revision 3

## What is known at dispatch

Each row is an independent order snapshot. IDs are opaque. `order_value` is in
cost units, `weight_kg` in kilograms, and times in whole hours from now.
`deadline_hours` is the customer's promised arrival deadline. The historical
`legacy_risk_score` is an old sales-region score, not a quality certificate or a
calibrated shipping-failure probability. All rows use this same manual revision.

`certificates` contains revisions of the lot's quality record in arbitrary
order. Only records with `signed: true` have been approved by QA. The greatest
signed `revision` supersedes all earlier ones, including previous releases.
Revision numbers are unique within a row. Unsigned drafts have no authority.
The current signed record must have `status: "released"` to ship. `quarantine`
and `revoked` prohibit both shipping modes. With no signed record, wait for QA.
`remaining_units` on the current record is the lot's remaining thermal budget.
A later signed release can clear a previous quarantine; a correction can also
reduce the budget or revoke an earlier release. No previous order's decision
or certificate is authority for the current snapshot.

The quality handbook permits a shipment only if its **worst-case** thermal dose
does not exceed the current remaining budget (equality is permitted). Dose
accumulates at `ambient_units_per_hour` when not protected by a cold box.
Ground handling takes `ground_handling_hours`, followed by the ground route's
transit. Ground handling and transit are both unprotected. Cold-box protection
begins immediately, lasts `cold_protection_hours`, and covers handling and
transit; only hours beyond that duration accumulate ambient dose. Cold handling
takes `cold_handling_hours`. Route `max_hours` is a guaranteed transit bound,
not an estimate to be replaced by average transit for safety decisions.

A route can be used only when its `open` field is true. Cold additionally needs
`cold_boxes_available: true`. Route availability is independent of historical
success. Hold is always safe and available; it defers this order to the manual
recovery queue and incurs the lost-order cost below. There is no shared capacity
or inter-order scheduling to infer.

## Service and accounting

The controlled carrier pilot draws actual transit independently and uniformly
from the inclusive integer interval `[min_hours, max_hours]` for the selected
route. These distributions apply to future orders as well as the log, including
previously unserved customer groups. Nothing else in a row changes that transit
distribution. All route bounds are positive integers, with min no greater than
max. All numeric values are finite and nonnegative. Handling time is additional.

For a legal ground dispatch, pay `ground_base + ground_per_kg * weight_kg`.
For a legal cold dispatch, pay `cold_base + cold_per_kg * weight_kg`.
If arrival is strictly later than `deadline_hours`, also pay
`late_base + late_value_fraction * order_value`. Arrival exactly at the deadline
is on time. A thermally legal shipment cannot spoil in this synthetic pilot.
For hold, pay `hold_base + hold_value_fraction * order_value`, with no carrier or
late charge. All parameters are in `config.json`. No revenue is subtracted.
The goal is mean realized cost across orders, subject to zero illegal actions.

## Reading historical observations

Each historical row has `historical_action`, `observed_transit_hours`, and
`observed_on_time`. A held order has both observations null. A dispatched order
has observations only for the selected route, never its alternatives. The old
dispatcher held many high-score orders without trying them, used cold mainly
for expensive low-score orders, and was conservative about deadlines. Its
observed success rate therefore describes selected shipments, not all orders.
Current serving rows have none of these three history-only fields. Labels may
be used, but inventing counterfactual labels for held orders is not justified.

The same order may later be presented with changed certificates, route status,
or box availability. Each call must reflect its supplied snapshot, including
recovery from a closed route or a newly signed QA correction. Evaluation does
not grade policy explanations or require a particular modeling technique.
