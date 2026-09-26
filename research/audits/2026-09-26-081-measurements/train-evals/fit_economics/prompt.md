---
plugins: ["../../../.agents"]
tags: [trigger]
max_turns: 12
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
---
Help decide whether this trained binary decision model was worth fitting. On the same untouched 1,000 examples, the constant-negative baseline has 40 false negatives and zero false positives. A fitted encoder has 15 false negatives and 55 false positives. A zero-shot model has 10 false negatives and 110 false positives. False negatives cost $8 each and false positives $1 each. Fitting cost $200 once; assume these rates stay fixed for another 5,000 decisions and ignore inference costs. Which option wins, including the fit cost, and at what future volume does the fitted model break even against the best unfitted option? Do not run training.
