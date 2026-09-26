# Bounded search notes

Contract recorded before preparation and fitting. Exact candidate checkout;
`reload_skills` preceded loading `augustus-train` and companion `augustus`.
No scenario expected notes or prior reviewer recommendations read.

1. **Incumbent:** always ham. This is runnable and the cheapest constant under
   the fit prevalence and 5:1 costs. Sparse lexical features are appropriate
   stock for a small fixed-label text task with CPU-only inference. No pretrained
   encoder, teacher, or paid provider; sklearn's BSD-licensed implementation
   fits vocabulary and coefficients solely on fit rows.
2. **word1:** word unigrams/bigrams, TF-IDF, logistic C=1. Search loss 0.025871
   per group at threshold 0.35, versus incumbent 0.115423. One false positive,
   26 missed spam out of 136. The threshold is empirical, not a calibrated
   posterior cost threshold; no downstream probability claim.
3. **Next hypotheses (recorded before execution):** the development errors
   include merged premium-rate numbers/charge strings and several nearly
   identical secret-admirer messages near threshold. Test character subwords
   (char8) to retain these patterns, and weaker regularization with unchanged
   word features (word8) to test underfitting. Maximum three fits total.
   These are hypotheses, not verified root causes. Development labels also
   include apparent reports about spam rather than incoming spam itself
   (line-1461, line-5373), and a proverb (line-2775). Preserve publisher labels;
   no model-driven relabeling. This limits product transfer.
4. Freeze the lowest development group loss across these trials; stop after
   this bounded comparison. One confirmation against the original constant,
   not a claim of statistically proven improvement over every fitted trial.
