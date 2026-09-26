The core problem is that your export is a record of what happened to tickets, and you want to predict something narrower: where the first message from a new customer should go. Most of the work is cutting the data down to what the model will actually see at routing time.

## 1. Use one example per ticket
- **Group rows by ticket ID and keep only the first customer-authored message.** Drop later replies, agent replies and internal notes.
- **Remove quoted copies inside that message** (`>` lines, "On … wrote:", forwarded blocks, signatures). Otherwise the model learns from text it won't see.
- **Deduplicate exact and near-duplicate first messages**, such as templated or auto-generated tickets. MinHash or TF-IDF cosine above about 0.9 works for this.
- Expect 18,000 rows to shrink to a few thousand tickets. That's normal, and those tickets are your real sample size.

## 2. Keep leaked information out of the inputs
Only use what exists when the first message arrives: subject, body, maybe channel or product area.

Exclude these:
- **Resolution notes.** They're written after routing, so they directly leak the answer.
- **Final queue as an input.** It's the label (see below), never an input.
- **Customer ID.** Keep it only for grouping the splits. As a feature it lets the model memorize customers, and next month's customers are new.
- **Anything after routing:** reassignment counts, handle time, agent names, later timestamps.

## 3. Decide what the label means before training
"Final queue" isn't the same as "correct queue for the first message." A billing ticket that ends up with engineering can mean either of two things:
- **The first message was ambiguous or misrouted.** The right label is probably billing, or it's a genuinely mixed case.
- **The problem turned out to be a bug in billing.** From the first message alone, billing may still have been the right first stop.

Here's how I'd handle it:
- **Write one labeling rule:** "the queue that should receive this ticket given only the first message." Add short guidelines with examples for the billing/engineering boundary.
- **Use routing history if the export has it** (initial queue and reassignments). Tickets that were reassigned are where the labels are least reliable. Measure how many there are.
- **Measure reviewer agreement.** Have both reviewers label the same 200–300 tickets independently and compute Cohen's kappa for each class pair. Low agreement on billing vs. engineering means you need clearer guidelines, a merged class, or a "needs triage" outcome. More model tuning won't fix it.
- **Settle disagreements with a third person or a joint discussion.** Keep a flag marking ambiguous cases rather than forcing a clean label and hiding them.

## 4. Split the data the way it will be used
You'll deploy on new customers next month, so the test set should look like that:
- **Split by time.** Train on older months, validate on the next period, test on the most recent month.
- **Split by customer.** No customer should appear in both train and test. Use group k-fold on customer ID for any cross-validation.
- **Check for near-duplicate messages across splits** after splitting.
- If you can, restrict the test set to customers whose first ticket falls in that window, since that's your deployment population.

## 5. Build a small, carefully labeled evaluation set
- **Take a gold test set of about 500–1,000 tickets from the most recent period.** Have both reviewers label them and settle every disagreement. Don't tune anything on it.
- **Look at more than accuracy.** Report per-class precision and recall and a confusion matrix, with extra attention on billing vs. engineering. If you know what each kind of misroute costs, weight the errors by that cost.
- **Add a confidence threshold.** Tickets below it go to human triage. Report coverage vs. accuracy at that threshold, because that's how it will actually run.
- **Compare against simple baselines:** always predicting the most common queue, your current keyword rules if you have any, and TF-IDF with logistic regression. With a few thousand tickets, the linear baseline may well be good enough, and it's easy to inspect.

## 6. Checks before you trust the numbers
- **Class balance over time:** have any queues changed or been added recently?
- **Remove or mask personal data** such as emails, phone numbers and account numbers in the text.
- **Test for leakage:** a model trained on customer ID or resolution notes alone should score near chance. If it doesn't, something is leaking.

If you share the CSV's column names, or point me to the file, I can write the extraction, cleaning and splitting script and the agreement and evaluation report.
