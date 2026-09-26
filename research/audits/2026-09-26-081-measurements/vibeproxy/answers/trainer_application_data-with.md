Frame everything around the decision you'll actually make: **one first customer message from a new customer arrives, and you pick a queue using only what's visible at that moment.** Most of the dataset work follows from that.

## 1. Reshape: one example per ticket, not per row

- **Group the 18k rows by ticket ID.** Keep only the earliest inbound customer message. Later replies and agent messages aren't available when routing happens. Expect the dataset to shrink to a few thousand tickets. That's the real sample size.
- **Strip quoted copies** (`>` lines, "On … wrote:", forwarded blocks) and signatures. Keep punctuation, casing and negation.
- **Drop anything that doesn't exist at arrival time:** resolution notes, final queue as a feature, later replies, assignee, tags added by agents, reopen or SLA fields.
- **Don't use customer ID as a feature.** New customers won't have any history. Keep it only as a grouping key for splits.
- **Collapse near-duplicates** such as templated emails and the same issue resubmitted, so they can't land on both sides of a split.

## 2. Fix the label before training on it

"Final queue" tells you where a ticket ended up. It doesn't tell you where the first message should have gone.

- **Write a short labeling guide (version it):** "Given only this first message, which queue should receive it?" Settle the billing/engineering boundary explicitly. For example, a charge failure caused by a bug: does billing triage it first, or does it go straight to engineering? That's a policy call for you to make, not something the model can learn.
- **Check reassignment history if the export has it.** A ticket that went billing → engineering was probably escalated after investigation. In that case, billing may be the correct *first-routing* label.
- **Have both reviewers label the same stratified sample independently, about 300–500 tickets.** Oversample billing/engineering and recently reassigned tickets. Measure agreement per class, adjudicate, revise the guide, and repeat once.
- **If they still disagree on a pattern, the categories don't fit the data.** Add an explicit "ambiguous → triage" outcome or keep soft labels rather than forcing a coin flip. Record both original judgments and the adjudicated label.
- **Label status:**
  - `final_queue` = weak label, usable for training.
  - `adjudicated` = gold, which evaluation needs.
  - Keep unlabeled or unclear tickets as null, never as a default class.

## 3. Split to match the claim: new customers, a future month

A random row split would overstate performance. It leaks threads, customers and templates across splits.

- **Split by time:**
  - Train on older months.
  - Use the next-to-last month for development (tuning, thresholds).
  - Hold out the latest month for confirmation.
- **Group by customer as well.** Development and confirmation should contain only customers never seen in training. Ideally, use only each customer's *first* ticket, since that's closest to "new customer, first message."
- **Compare class mix and message style** between new customers' first tickets and the overall data. Onboarding and billing-setup questions are often over-represented.
- **Confirmation set:** adjudicated labels, never used for tuning or for choosing labeling examples. Once you look at it to make a change, it becomes development data.
- **Challenge set, reported separately:** billing/engineering boundary cases and reviewer-disagreement cases. Report counts alongside rates, because a slice with 15 examples can't support a strong recall claim.
- **Freeze** ticket IDs per split, the cutoff dates, the guide version, the normalization rule and file hashes.

## 4. Evaluate against something real

- **Comparators:** your current routing (the queue first assigned) and a cost-aware constant rule. Beat those before comparing models.
- **Metrics:**
  - Per-queue recall.
  - The billing↔engineering confusion cell.
  - An expected misroute cost, if a wrong engineering assignment costs more than a wrong billing one.
  - How often low-confidence cases go to a triage/fallback queue.
- **Start with TF-IDF + logistic regression** fit on training data only. It's local, fast, and often competitive. Move to a small sentence encoder with a classifier head only if development errors point to representation problems. Set any confidence threshold on development data, then freeze it.
- **The real test is next month:** log predictions against the adjudicated queue for new customers' first messages before letting the model route on its own.

If you point me at the CSV (or its column names), I can write the preparation script: ticket collapse, quote stripping, leakage column drop, grouped time split, and a disagreement-sampling sheet for your reviewers.
