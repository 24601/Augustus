# Answers as application agent (2026-09-27)

## 1. Threshold policy operational report

Population: current-era export rows, selection `era == current`, ids b,c,d (n=3).
Row `a` is old era: kept in the export for replay identity, excluded from the
current-era denominator. Policy: action iff `score >= 0.5`; costs FP=1, FN=8.
Scores are raw scores; no calibration/probability meaning claimed.

From `policy-receipt.json` (exact rational arithmetic, additive shifts, no clipping):

| intervention | positive actions | action rate | FP | FN | mean loss |
| --- | --- | --- | --- | --- | --- |
| baseline | 1/3 | 0.333 | 0 | 1 | 2.667 |
| score −0.125 | 0/3 | 0.000 | 0 | 2 | 5.333 |
| score +0.125 | 3/3 | 1.000 | 1 | 0 | 0.333 |
| threshold −0.125 | 3/3 | 1.000 | 1 | 0 | 0.333 |
| threshold +0.125 | 0/3 | 0.000 | 0 | 2 | 5.333 |

Colleague's two claims are both wrong:
- Action rate is 1/3 (33.3%), not 50%. 50% comes from counting 2/4 over all export
  rows including old-era `a`; the next use is the current era, so `a` does not belong
  in that denominator.
- Shifting scores up by 0.125 is the *opposite* of raising the threshold by 0.125.
  Raising scores relative to a fixed threshold makes actions more likely: action rate
  goes 0.333 → 1.000, missed positives 1 → 0, mean loss 2.667 → 0.333. Raising the
  threshold gives action rate 0.000, missed positives 2, mean loss 5.333. Score-up
  matches threshold-*down*, not threshold-up.

Receipt: `policy-input.json` + `policy-receipt.json` in this folder; command above.
Limits: descriptive only. The helper checks arithmetic and direction; it does not
validate that the selection rule really selects b,c,d, label provenance,
representativeness, or future loss. n=3 supports no population bound. Clipping,
rounding and abstention must be replayed through the real `decide` path.

## 2. Bootstrap and the launch note

No — the launch note cannot say "next week's loss will be below .45 with 95%
confidence."
- The 12 thresholds were selected on the same 300 development records (39 positives),
  so the bootstrapped losses are fitted, adaptively-selected in-sample losses.
  Bootstrap quantiles of a selected policy's fitted loss are not a next-period
  prediction interval: they omit selection-over-12 optimism, refitting uncertainty,
  and any population shift into next week.
- "No bootstrap mean exceeded .45" across 4,000 resamples of the *same* 300 records
  is not a ~0 probability of exceeding .45 in deployment; resampling acquires no new
  population evidence. Positives (39) are the binding count for tail precision.
- Honest wording: "development estimate of mean loss 0.02–0.17 (95% bootstrap range,
  in-sample, threshold selected from 12 candidates on these same 300 records);
  next week's loss is unresolved."

Cheapest useful next step: do not run more resampling. Freeze the chosen threshold
and policy now, then (a) immediately — at zero new labeling cost — report the
development estimate with the selection caveat and compute the selection-optimism
gap cheaply, e.g. compare the selected threshold's loss against the loss of a
threshold chosen out-of-fold (nested/held-out-fold selection over the same 12-point
grid) on the existing 300 records; and (b) start the one-week collection of fresh
adjudicated outcomes scored by the frozen policy, sized against the ~13%
positive rate, as the independent check. Keep the incumbent active until (b) returns.

## 3. Renewal-notice routing: ship the rule, not a model

Ship an exact lookup, this week. The decision is a fixed-vocabulary mapping from an
authoritative `notice_type` enum to an operations-approved routing table — exact
computation, not bounded judgment. A trained model would only reintroduce error on a
mapping that is already known, and 30 hand-labeled free-text notes are far too few
to justify or evaluate one (and are incidental notes, not a representative holdout).

This week:
1. Route by `notice_type` through the approved table, loaded as versioned data
   (table version + digest logged with every decision), not hardcoded — last month's
   failures were stale deployed copies, so add a startup/refresh check that the
   deployed table version matches the approved source and refuses to serve a stale
   copy (retain incumbent/manual path on mismatch) rather than silently routing.
2. Any `notice_type` value absent from the table, or missing/invalid/ambiguous,
   goes to the operations review queue as `unknown` — a distinct outcome from every
   real route, never a nearest-match guess.
3. Tests on actual arithmetic/parsing/policy: every supported enum value maps to its
   approved destination; unknown/new value → operations; missing, empty, wrong-case
   and non-enum values → operations; stale-table startup refusal; end-to-end path
   from export row to dispatched action.
4. Use the 30 labeled notes only as a labeled diagnostic: check whether free-text
   notes ever disagree with the enum. If a material disagreement appears, that is a
   spec/data question for operations, and only then is a free-text component a
   candidate — with real labels and a contract.

No training, no calibration, no new model dependency. Free-text classification stays
a later, separately justified candidate.

## 4. Copy edit

The classifier weights were exported after training.
