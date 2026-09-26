**Over the next 5,000 decisions, the zero-shot model wins: $950, against $1,075 for the fitted encoder including the $200 fit.** The fitted model only pays back its fit cost after about **13,334 future decisions**.

### Cost per decision (from the 1,000 held-out examples)

| Option | FN × $8 | FP × $1 | Cost per 1,000 | Per decision |
|---|---|---|---|---|
| Constant-negative | 40 × 8 = 320 | 0 | $320 | $0.320 |
| Fitted encoder | 15 × 8 = 120 | 55 | $175 | $0.175 |
| Zero-shot | 10 × 8 = 80 | 110 | $190 | $0.190 |

### Total cost over the next 5,000 decisions

| Option | Error cost | Fit cost | Total |
|---|---|---|---|
| **Zero-shot** | $950 | $0 | **$950** |
| Fitted encoder | $875 | $200 | $1,075 |
| Constant-negative | $1,600 | $0 | $1,600 |

### Break-even
- **Fitted vs. zero-shot (the best option that needs no fitting):** the fitted model saves $0.015 per decision, so $200 ÷ $0.015 ≈ 13,333.3. It breaks even at **about 13,334 future decisions**. At 5,000 decisions it has only earned back $75 of the $200.
- **Fitted vs. constant-negative:** it saves $0.145 per decision and breaks even at about 1,380 decisions. The fitted model clearly beats doing nothing, but zero-shot beats doing nothing by nearly as much for free.

### Two points that could change the decision
1. **If the $200 is already spent, it's a sunk cost.** Looking back, fitting wasn't worth it at a 5,000-decision horizon. Looking forward, the fitted model is the cheapest one to keep using, at $0.175 per decision against $0.190.
2. **The advantage is small and uncertain.** The two models differ by $15 per 1,000 examples. That gap comes from only 5 false negatives and 55 false positives on a test set with just 40 positives. Sampling noise of that size could easily reverse the ranking. Also, both costs are dominated by false negatives, so if the true positive rate or the $8 figure is off, the answer can flip. Before you rely on the 13k break-even figure, get a confidence interval, for example by bootstrapping the 1,000 examples.
