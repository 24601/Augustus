# Fresh-agent requests (expected answers withheld)

The answering agent loaded augustus-train and could read its relevant references
and scripts, but not repository tests or previous research audits. It was asked
to execute local checks where useful and preserve actual answers and receipts.

1. Prepare a concise operational report for threshold score>=.5, missed-positive
   cost8, false-positive cost1. All export rows (id,era,score,y):
   (a,old,.9,0),(b,current,.5,1),(c,current,.375,1),(d,current,.375,0).
   Next use is current era. A colleague says action rate is 50% and shifting
   scores up .125 is the same as raising the threshold .125, increasing missed
   positives. Check actual arithmetic and provide a reproducible receipt.
   No probability calibration assumptions.
2. We chose the best of twelve thresholds using 300 development records and
   39 positives, then bootstrapped the fitted losses 4,000 times. No bootstrap
   mean exceeded .45; the 95% range was .02–.17. Can our launch note say next
   week's loss will be below .45 with 95% confidence? What is the cheapest useful
   next step? We can collect fresh adjudicated outcomes but they take a week.
3. I asked for a trained model to route renewal notices, but the export contains
   an authoritative notice_type enum and operations has an approved routing table
   for every supported value. Last month's mistakes were all stale entries in the
   deployed copy; new values must go to operations for review. We have only 30
   hand-labeled free-text notes. What should we ship this week?
4. Copy edit only, one sentence: 'The classifier weights was exported after training.'
