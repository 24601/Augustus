No. A 0.92 reranker score is not a 92% probability that the claim is true, and it shouldn't drive automatic publishing on its own. There are three separate problems.

**1. It measures the wrong thing.** A passage reranker scores how relevant a passage is to a query. It doesn't check whether a claim is true. A passage can be highly relevant and still:
- contradict the claim,
- be outdated or come from a bad source,
- only partly support it (right entity, wrong number or date).

Relevance is at best one input to a truth judgment.

**2. It's probably not calibrated.** Even for relevance, cross-encoder and reranker outputs are usually uncalibrated. They're often a sigmoid over a logit trained with a ranking or contrastive loss. The ordering means something, but the absolute value usually doesn't. Scores also tend to shift with query length, domain, and model version, so 0.92 today may not mean what 0.92 meant last month.

**3. It's a single passage.** A claim's truth depends on all the evidence together: several passages, conflicts between them, and source reliability. One passage's score can't represent that.

**What would make auto-publishing defensible:**

1. **Add a verification step.** Use an NLI or entailment model, or an LLM judge, that classifies (claim, passage) as supports, refutes, or not enough info. Aggregate across the top-k passages and require no strong refutation.
2. **Build a labeled set.** Take a few hundred to a few thousand claims from your real traffic, labeled true/false by humans.
3. **Calibrate against it.** Fit Platt scaling or isotonic regression on held-out data, then check with a reliability diagram and expected calibration error (ECE). After that, a calibrated score of 0.92 does roughly mean "about 92% of claims like this were true."
4. **Pick the threshold from costs, not from the number.** Decide what a false publish costs compared with sending a claim to a human. Choose the threshold that meets your target precision, and report precision and coverage with confidence intervals.
5. **Use three outcomes, not two.** Auto-publish above a high threshold, send the middle band to human review, and reject below a low threshold.
6. **Keep monitoring.** Audit a random sample of auto-published items, watch for drift in the score distribution, and recalibrate whenever the reranker, the corpus, or the traffic changes.

Until you've done at least the labeled set and calibration, treat 0.92 as "this passage ranked highly." It isn't a probability that the claim is correct. If you point me to your pipeline, I can help design the evaluation set or add an entailment and calibration step.
