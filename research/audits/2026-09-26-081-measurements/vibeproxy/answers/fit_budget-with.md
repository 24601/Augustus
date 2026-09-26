## Recommendation

**Don't fine-tune a large model yet, and don't start by collecting more data.** Measure the current rules first. Then compare them with two small models on a laptop, and let a learning curve tell you whether more data is worth collecting.

Why:
- **No baseline.** Without a number for the current rules, you can't tell whether any model is an improvement.
- **144 examples is too few for large-model fine-tuning.** At 80% accuracy, the 95% interval on all 144 is about ±6.5 points. A single queue's 24 examples give about ±17 points. Fine-tuning would add variance and cost, and you couldn't measure what it gained.
- **Whether to collect more data is something you can measure.** A learning curve on the data you already have shows whether it would help, and which queues to collect for.

## Experiment plan (about one day)

**0. Freeze the inputs (1–2 h)**
- Put the 144 rows in `data.jsonl` with `id`, `text`, `label`, and a group key (`customer`/`thread`/`template`).
- Remove near-duplicates. Keep rows from the same group in the same fold, because a random split will leak.
- Write down:
  - The real traffic share of each queue. Your data has 24 per queue, but production traffic probably isn't balanced, so reweight the metrics to match it.
  - A 6×6 misrouting cost matrix, or at least which confusions are expensive. Ask whoever owns the queues.
  - What happens to "unsure" cases, e.g. a human triage queue.
- Commit a manifest with the data hash, candidate list and metrics. Nothing on this list changes after you see results.

**1. Measure the label ceiling (1 h)**
- Have a second person relabel a stratified subset of 36 without seeing the original labels.
- Record their agreement and Cohen's κ. If agreement is about 85%, no model will reliably do better than that. Low κ on particular queue pairs means the queue definitions need fixing, not a model.

**2. Measure the rules (30 min)**
- Run the current rules on all 144. They weren't fit to this data, so no split is needed.
- Report:
  - accuracy with a Wilson interval
  - macro-F1
  - the 6×6 confusion matrix
  - cost-weighted error
  - the no-match rate
- Also compute the majority-class baseline.

**3. Fixed candidates, all local and cheap**

| ID | Candidate |
|---|---|
| R | current rules |
| A | TF-IDF (word 1–2-grams plus character 3–5-grams) → logistic regression |
| B | frozen small sentence embedding (e.g. a MiniLM/BGE-small-class model, run locally) → logistic regression |
| C *(optional)* | few-shot prompt to a hosted LLM, *only if sending this request text to an external API is allowed* — confirm first |

Tuning is limited to the regularisation strength C ∈ {0.1, 1, 10}, chosen by inner cross-validation. There is no other search.

**4. Evaluation protocol**
- Use repeated grouped stratified 5-fold cross-validation, 10 repeats, with the same folds for every candidate.
- For each fold, record per-row predictions and the top-label probability. Keep these raw outputs.
- Metrics:
  - traffic-weighted accuracy and cost
  - macro-F1
  - per-queue recall
  - confusion matrix
- For the comparison (best model minus rules):
  - Compute the paired difference on the same rows, with a bootstrap CI that resamples groups rather than rows.
  - Also plot risk against coverage: the error rate among the cases the model routes itself, as more low-confidence cases are sent to triage instead.
  - Pick the triage threshold inside the folds only, never on the final numbers.

**5. Learning curve**
- For A and B, train on 6, 12, 18 and 24 examples per queue within each fold, and evaluate on the same held-out folds.
- Record the slope between 18 and 24 per queue, overall and for each queue.

## Stop rule (applied once, in this order)

1. **Fix labels first:** second-labeller agreement below about 80%, or low κ on specific queue pairs → pause the modelling. Rewrite the queue definitions and relabel before anything else.
2. **Collect more data:** the 18→24 slope is at least 3 points for the best model, or any queue's recall interval is wider than ±15 points and that queue matters for cost → collect more data.
   - Target about 100 per queue.
   - Pull from real traffic, and oversample the pairs the confusion matrix shows are mixed up.
   - Then rerun this exact plan.
3. **Adopt the small model:**
   - Conditions:
     - the best of A/B beats R on traffic-weighted cost
     - the lower bound of the 95% paired CI is above 0
     - the gain is at least a margin you fix now (e.g. 5 points of accuracy, or X% of misrouting cost)
     - no queue's recall is more than 10 points worse than under the rules
   - What to do:
     - Freeze the model and its triage threshold.
     - Run it in shadow mode beside the rules on about 200 fresh, labelled production requests.
     - Promote it only if the shadow result is still inside the margin.
4. **Keep the rules:** the interval includes 0, or the gain is below the margin → keep the rules. Use the confusion matrix to patch them, and log real traffic so you can build a larger labelled set.
5. **Revisit large-model fine-tuning only if** you have several hundred examples per queue and the small models have levelled off below a target that matters for the business. Even then, try the few-shot LLM (C) first.

**Hard budget:** one working day, the candidates above, and one rerun after new data. If none of the adopt conditions is met within that, the default outcome is to keep the rules.

## Caveats
- Every conclusion above is a hypothesis until you run it. I haven't run anything, and there's no data in the working directory.
- 144 examples can't certify a low error rate. Even with 24 error-free examples in one queue, the 95% upper bound on that queue's error rate is about 12%. The shadow run on fresh traffic is the real confirmation; the cross-validation is not.
- Decide in advance whether the goal is cost, accuracy or triage load. Without that, choosing the margin in step 3 turns into a judgment call made after seeing the results.

If you want, I can write the harness (`eval.py` with the grouped repeated CV, the paired bootstrap and the learning curve) against your data file. It wouldn't train anything beyond what the plan specifies.
