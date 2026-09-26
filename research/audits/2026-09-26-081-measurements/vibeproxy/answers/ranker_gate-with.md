No. A 0.92 from a reranker isn't a 92% chance the claim is true, and it isn't enough to justify auto-publishing on its own. There are three separate problems.

**1. It measures the wrong thing.** A passage reranker scores how *relevant* a passage is to a query. It doesn't score whether a claim is *true*. A passage can be highly relevant and still:
- contradict the claim,
- be outdated, satirical or wrong,
- mention the topic without supporting the specific assertion.

"This passage is about X" is a different statement from "X is true." For truth you need an entailment or verification step, such as an NLI model or an LLM judge that asks whether the passage supports, contradicts or doesn't address the claim. That score needs to be calibrated too.

**2. The raw score isn't a probability.** Most rerankers are trained with ranking losses (pairwise or listwise, or a cross-encoder logit through a sigmoid). Their outputs are only meaningful *relative to other passages for the same query*. A score of 0.92 might be right 60% of the time on your data, or 99%. You only find out by measuring.

**3. The decision to publish carries its own costs.** Even a perfectly calibrated 92% means about 1 in 12 auto-published claims is wrong. Whether that's acceptable depends on what a false publication costs compared with a human review.

**What I'd do instead:**

1. **Build a labeled set.** Take a few hundred claims covering the full score range, labeled true or false by humans, drawn from your real traffic.
2. **Add a verification signal.** Use a claim-vs-evidence entailment check, ideally across several independent passages, not just the top one.
3. **Calibrate.** Fit isotonic regression or Platt scaling on held-out labels so the score maps to an actual empirical accuracy. Check it with a reliability diagram or expected calibration error (ECE).
4. **Set the threshold from costs.** Pick the cutoff where precision meets your tolerance, e.g. "auto-publish only where measured precision is at least 99%."
5. **Use three bands, not two.** Auto-publish above a high threshold, auto-reject below a low one, and send the middle band to a human.
6. **Monitor.** Audit a sample of auto-published items on an ongoing basis. Calibration drifts as topics, sources and models change.

If you share the reranker model and a sample of scored outputs with labels, I can help you set up the calibration and threshold analysis.
