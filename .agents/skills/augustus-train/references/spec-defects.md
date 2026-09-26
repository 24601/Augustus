# Spec defects that look like modelling results

Every defect here was found by grading real arms, and each one punished the arms that **read the
spec** while sparing the arms that **learn from fit examples**. That asymmetry is why they matter:
they sit directly across the comparison a rung ladder is meant to make.

Source: `research/080/receipts/m5-grading-2026-09-25.md`.

## The answer vocabulary is not the stored label

**Symptom:** an arm scores zero with a 100% invalid rate while emitting exactly what the spec named.

The spec said the options were `toxic` and `not toxic`. The stored labels were `0` and `1`. The
scorer built its label set from stored values, so a compiled program that obeyed its instructions
was graded 60,000 invalid outputs out of 60,000.

**Fix:** declare the surface once — a map from stored value to the spec's wording — render both
sides through it, and accept either spelling when matching. Verify it is a relabelling by checking
that every fit-based arm's score is unchanged; if one moves, the map is wrong.

## The spec describes a different task than the labels encode

**Symptom:** an arm abstains on everything, or answers a question no column scores.

A spec asked for one of 150 in-scope intents. The labels had only ever been binary in-scope
detection. Every arm that read that spec answered a question nobody was scoring, and no mapping
repairs it — those arms have to be run again against a corrected spec.

**Fix:** before any run, check that the spec's option set and the stored label set describe the
same decision. Settle polarity from the rule that *produced* the label, not from a minority count.

## The abstain option collides with a real class

**Symptom:** an arm that answers correctly is charged the abstention price.

The abstain label for one task was `out of scope`, which was also one of its two real answers. An
arm that correctly called a query out of scope paid 0.3 for refusing instead of 0.0 for being
right, and one that called it wrongly paid 0.3 instead of 1.0.

**Fix:** the refusal and the class are different acts and need different names.

## Options named by reference rather than enumerated

**Symptom:** a generative or compiled artifact invents plausible label-shaped strings.

"One of the 77 BANKING77 intent labels" is resolvable by a person and not by a compiled program
that sees a handful of worked examples inside a token budget. It produced 1,749 distinct strings
over 6,000 rows, none of which the spec had listed.

**Fix:** write every allowed answer into the spec verbatim, and rewrite worked examples into the
same wording so nothing is shown two spellings of one answer. Measured cost of doing so: none — a
77-line option list still left all 24 examples inside a 5,120-token prompt.

**Measured limit:** enumeration halved the problem and did not solve it. A fine-tune on 4,800
teacher examples halved it again. The artifact still emitted 862 distinct strings and was invalid
on 34.5% of rows. Two independent fixes, each worth about half.

## A counter that contradicts its own rule

**Symptom:** an invalid output is reported as an abstention.

`if matched == costs.get("abstain_label")` returns true when both sides are `None` — which happens
on every task with no abstain label, for every unmatched output. It printed an abstention rate of
1.0 for an arm that had abstained zero times.

**Fix:** guard the comparison. More generally: when a counter and a rule disagree, report the one
that matches the rule and fix the counter afterwards, rather than reporting the number the file
happened to compute.

## A flag whose name inverts its meaning

**Symptom:** a losing arm carries `superior_by_margin: true`.

The field computed `lower_bound > margin` on a difference of **costs**, so it fired exactly when the
arm was worse. One arm carried it while costing 0.69 more than the comparator.

**Fix:** name a flag after what it computes. Rename, never recompute, and leave stored reports with
the value they produced.

## The teacher's distribution is the training distribution

**Symptom:** a fine-tuned artifact has a behaviour nobody can explain, or lacks one everybody
expected.

A teacher synthesizing 14,400 training examples used the abstain option **zero times**, on specs
that offered it every time. Whatever the resulting program does about declining, it did not learn
it from its training data.

**Fix:** measure the teacher's output distribution before the fine-tune, not after the arm is
scored. Malformed-output rate belongs in the same measurement: one spec produced a 0.661 discard
rate where two others produced almost none, because a single dropped quote makes a whole response
contribute zero examples instead of eight.
