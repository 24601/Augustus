**The zero-shot model is the better choice.** Over the next 5,000 decisions, fitting doesn't pay back its $200 cost. The fitted model only breaks even with zero-shot after about 13,334 future decisions.

**Cost per 1,000 decisions** (FN × $8 + FP × $1)

| Option | FN cost | FP cost | Total per 1k | Per decision |
|---|---|---|---|---|
| Constant-negative | 40 × 8 = 320 | 0 | **$320** | $0.320 |
| Fitted encoder | 15 × 8 = 120 | 55 | **$175** | $0.175 |
| Zero-shot | 10 × 8 = 80 | 110 | **$190** | $0.190 |

**Over the next 5,000 decisions, including the fit cost**

- Zero-shot: 5 × 190 = **$950** (best)
- Fitted: 5 × 175 + 200 = **$1,075**, which is $125 worse
- Constant-negative: 5 × 320 = **$1,600**

**Break-even against zero-shot**

The fitted model saves $0.015 per decision compared with zero-shot. Recovering $200 at that rate takes 200 / 0.015 ≈ 13,333.3 decisions, so fitting only comes out ahead from about **13,334 future decisions** on. At 5,000 it has recovered only $75 of the $200.

Even if you count the 1,000 evaluation examples as decisions (6,000 total), the fitted model costs $1,250 against zero-shot's $1,140, so zero-shot still wins.

**How reliable the numbers are:** The $15-per-1,000 gap rests on only about 40 positives in the test set. Being wrong on 2 positives, or 15 negatives, would erase the gap, so the break-even point is very uncertain. The ranking also depends heavily on the 8:1 cost ratio. Below about 5.5:1 zero-shot is cheaper per decision and the fitted model never breaks even. At higher ratios the break-even volume falls. Both models are clearly better than the constant-negative baseline.
