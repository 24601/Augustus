# Don't choose a model yet: measure the current rules first, then compare them with cheap small models

**Recommendation:** Don't fine-tune a large model. You have 144 examples and no baseline, so you couldn't tell whether a fine-tune helped. The cheapest useful step is to score the current rules against small models on the data you already have. Only collect more data if the learning curve suggests it will help.

**How much 144 examples can show:** At about 80% accuracy, the 95% confidence interval is roughly **±6.5 points overall** and **±16 points for each queue** (24 examples). So this data can only reliably show differences of about 10 points or more. The plan is built around that limit.

## Before running anything, write these down in a dated file

1. **Arms, all fixed in advance with no tuning:**
   - **A. Current rules.** No training.
   - **B. TF‑IDF + logistic regression.** Use word 1–2-grams plus character 3–5-grams, with default settings.
   - **C. Sentence embeddings + logistic regression.** Use a small local embedding model and default settings.
   - **D. (Optional) Prompted LLM, zero-shot.** Give it one paragraph describing each queue and no fine-tuning. Include this only if the data is allowed to leave the laptop.
2. **Primary metric:** accuracy on out-of-fold predictions for all 144 examples. The classes are balanced, so this equals balanced accuracy.
   - Also report accuracy weighted by each queue's share of real traffic. Your production traffic almost certainly isn't one-sixth per queue.
   - Secondary: recall for each queue and the confusion matrix.
3. **Smallest improvement worth acting on:** Δ = 10 points. You can raise it if some misroutes are expensive.
4. **The decision table below.**

## Steps

**1. Estimate the label ceiling (about 1 hour).**
- Have a second person relabel 36 examples (6 per queue) without seeing the original labels.
- Compute raw agreement and Cohen's kappa.
- The agreement rate is the best accuracy any method can be measured at.
- Clarify "independently labelled": if it means a single annotator per item, you have no estimate of label noise, and this step is what gives you one.

**2. Score the rules on all 144.**
- Check whether the rules were written or adjusted while looking at these examples. If so, their score is optimistic. Note that and, if you can, score them separately on examples the rule author never saw.

**3. Cross-validate arms B, C and D.**
- Use repeated stratified 6-fold cross-validation, 5 repeats, with fixed seeds.
- Each fold trains on 20 examples per queue and tests on 4.
- Keep the out-of-fold prediction for every example, so every arm is compared on the same 144 items.

**4. Run paired comparisons against the rules.**
- For each arm, run an exact McNemar test on the items where it and the rules disagree.
- Also compute a paired bootstrap 95% confidence interval for the accuracy difference (10k resamples, resampling items).

**5. Build a learning curve for the best arm.**
- Inside each fold, train on 6, 12, 18 and 20 examples per queue.
- Plot out-of-fold accuracy against training size.
- Record the slope between 12 and 20 examples per queue.

**6. Do error analysis (30 minutes).**
- Read every misroute made by the best arm.
- Tag each one as a label error, a genuinely ambiguous request, overlapping queue definitions, or a true model error.

**Time box:** one working day. No hyperparameter searches: tuning on 144 examples just overfits to them.

## Decision table: stop at the first row that matches

| # | Condition | Decision |
|---|---|---|
| 1 | Rules accuracy ≥ label agreement − 5 points | **Stop. Keep the rules.** They are already at the label ceiling, so the remaining work is sharpening queue definitions, not modelling. |
| 2 | Best arm beats the rules by ≥ Δ **and** the lower bound of its paired CI is > 0 | **Stop. Adopt that small model.** Run it in shadow mode next to the rules for 2 weeks, then switch. |
| 3 | The CI includes 0 **and** the learning curve still rises ≥ 3 points from 12 to 20 per queue | **Collect more data:** about 100–120 per queue, weighted toward the queues that get confused most. That brings the overall interval to about ±3 points. Then rerun this plan unchanged. |
| 4 | The CI includes 0 **and** the curve is flat | **Stop. Keep the rules.** More data or bigger models won't help. Error analysis will most likely point to overlapping queue definitions or noisy labels. Fix those first. |

**When a large-model fine-tune becomes worth testing:** only when all of these hold:
- you have at least several hundred examples per queue,
- the small model has plateaued below a target you've written down,
- error analysis shows semantic mistakes that embeddings miss,
- a prompted LLM (arm D) has already been tried and fell short.

Until then it adds cost without any way to measure the gain.
