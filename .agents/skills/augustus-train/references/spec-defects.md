# Spec defects that look like modelling results

Use these checks at the label/model/evaluator boundary before fitting. The examples
are **Reported** findings in the
[M5 receipt](https://github.com/24601/Augustus/blob/cd6b904f6af412adb643bdcf6281bfcccb33952b/research/080/receipts/m5-grading-2026-09-25.md),
not a reproduction by this skill. Some defects particularly harmed spec-reading
arms while sparing fit-based arms; that is an unfair comparison, not model quality.

Test the fixes on independently hand-scored examples. A purely fixed-label head
does not need an instruction prompt, but still needs a correct label/policy map.
If the target or scorer changes, invalidate affected claims and re-evaluate rather
than disguising the repair as a better model.

## The answer vocabulary is not the stored label

**Symptom:** an arm scores zero with a 100% invalid rate while emitting exactly what the spec named.

The spec said the options were `toxic` and `not toxic`. The stored labels were `0` and `1`. The
scorer built its label set from stored values, so a compiled program that obeyed its instructions
was graded 60,000 invalid outputs out of 60,000.

**Fix:** declare a one-to-one map from stored value to canonical output, including
polarity, and only the intentional aliases. Render prompts and evaluation through
the same contract. Reject collisions or unknown values instead of fuzzy-matching
them after seeing scores. Verify a pure relabeling leaves decisions and costs
unchanged; independently test positive, negative, abstain and invalid cases.

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
that sees a handful of worked examples inside a token budget. The recorded runs
produced many plausible strings outside the true taxonomy; the spec had not
provided the complete output vocabulary.

**Fix:** write every allowed answer into the spec verbatim, and rewrite worked examples into the
same wording so nothing is shown two spellings of one answer. In the reported
configuration, a 77-line option list still left all 24 examples inside a 5,120-token
prompt. Fitting the prompt budget does not establish zero serving cost.

**Reported limit:** enumeration did not solve invalid output. The later fine-tuned
artifact still emitted 862 distinct strings and was invalid on 34.5% of rows.
Distinct output strings and row-level invalid rate are different denominators;
do not describe both interventions as “halving the problem.” Explicit vocabulary
plus constrained decoding/validation is a candidate fix, to be tested on the
actual runtime rather than assumed from the prompt.

## A counter that contradicts its own rule

**Symptom:** an invalid output is reported as an abstention.

`if matched == costs.get("abstain_label")` returns true when both sides are `None` — which happens
on every task with no abstain label, for every unmatched output. It printed an abstention rate of
1.0 for an arm that had abstained zero times.

**Fix:** guard the comparison and test invalid output with and without a declared
abstain label. Correct the counter and rerun the affected report, preserving the
old report as superseded evidence. Never present a known-bad counter as a result.

## A flag whose name inverts its meaning

**Symptom:** a losing arm carries `superior_by_margin: true`.

The field computed `lower_bound > margin` on a difference of **costs**, so it fired exactly when the
arm was worse. One arm carried it while costing 0.69 more than the comparator.

**Fix:** declare the subtraction direction and test wins, losses and margin
equality by hand. If renaming a historical flag, preserve its original arithmetic
and explain the correction. For a new acceptance decision, compute the correct
bound and comparator; preserving history does not require preserving a bug.

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

## Read the experimental lessons at their actual scope

- The receipt eventually covers **twelve** graded arms: A1, A2a, A2b, R1, R2a,
  R2b, R3a, R4-gliner2, AnyJev L0, imajev, Lumma-Fev and decider. Its “ten arms”
  summary is stale. Exploratory additions do not inherit the registered family.
- R3a consumed the bundle's **2,000** fit examples: see the
  [export cap](https://github.com/24601/Augustus/blob/cd6b904f6af412adb643bdcf6281bfcccb33952b/research/080/exp/m5_export.py)
  and [R3a data path](https://github.com/24601/Augustus/blob/cd6b904f6af412adb643bdcf6281bfcccb33952b/research/080/exp/m5_fit.py).
  The 1,600-row fit describes R4-gliner2, not R3a. R3a lost T2a to R2a's
  frozen-encoder head (mean costs 0.1488 versus 0.1177); there is no universal
  winning artifact family or mandatory escalation order.
- imajev's 11% T2a order flip was measured at **rotations 1**, not its default 4,
  as the [source run notes](https://github.com/24601/Augustus/blob/cd6b904f6af412adb643bdcf6281bfcccb33952b/research/080/sources/imajev-anyjev-2026-09-25.md)
  specify. Test the configuration actually served, preserving option identity
  across permutations. AnyJev's binary zero flips do not extend to its partitioned
  77-option run, where changing partitions also changes the question.
- Emitted class proportions, accuracy and loss moving together suggest an
  operating-point investigation; they do not isolate threshold causality from
  representation, data or model differences. Freeze scores and vary policy on
  development data to test that hypothesis. Matching prevalence is not calibration.
- Increasing confidence with correctness is a discrimination observation, not
  reliability evidence. For calibration, compare probabilities of the same stated
  event with empirical event rates on representative independent labels, with
  counts and uncertainty. Chosen-class confidence is not positive-class probability.
