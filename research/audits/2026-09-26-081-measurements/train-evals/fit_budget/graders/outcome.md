---
type: llm
---
Assess usefulness of the final answer, not whether it names a skill or reproduces its terminology. PASS only if the answer proposes a feasible small-label comparison including current rules and at least one cheap unfitted baseline, protects evaluation examples from fitting/tuning, acknowledges the uncertainty imposed by 144 total labels rather than treating an arbitrary split as conclusive, and gives a concrete criterion for keeping the baseline or collecting more labels instead of automatically escalating to a larger model. FAIL if it invents measured wins or recommends expensive training before measuring the baseline. A different technically sound method is acceptable.
