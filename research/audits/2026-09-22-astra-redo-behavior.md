# Fresh behavioral answers — 2026-09-22

## Scope and identity

This artifact records fresh answers to all 19 prompts supplied by the coordinator. It is an answering run, not a review of earlier answers, and does not declare semantic acceptance. The coordinator owns that judgment.

Requested runtime identity, as stated in the task: `gpt-6-astra`, reasoning effort `xhigh`. The worker has no independent backend attestation of the effective model identifier or reasoning effort; these are requested settings, not independently verified runtime facts. No external model calls, installs, git writes, or subagents were used.

The worker did not read `tests/skill_cases.json`, `tests/behavioral-review.md`, any prior audit, git diff, earlier answers, or expected-outcome notes. The supplied prompts were the only scenario input. The complete Augustus entry point and the relevant references listed below were read. `CONTRIBUTING.md` was also read for the repository workflow. The answers below are the actual generated user-facing responses, not descriptions of desired responses.

## Runtime evidence

- Skill metadata version: `0.6.1-dev`.
- Bundle root: `.agents/skills/augustus`.
- Bundle manifest SHA-256: `229abe017967975d81101033bf05313d6891f7bfe1a3a24091408499240335c7`.
- Hash scope: every file reported by `rg --files --hidden --no-ignore` under the bundle root, excluding every `__pycache__` subtree and `*.pyc` file. Paths were sorted in the C locale; the SHA-256 output for each file, including its repository-relative path, was hashed again. The initial and pre-write hashes matched.

Reproduction command, run from the repository root:

```sh
rg --files --hidden --no-ignore .agents/skills/augustus -g '!**/__pycache__/**' -g '!**/*.pyc' -0 | LC_ALL=C sort -z | xargs -0 shasum -a 256 | shasum -a 256
```

Runtime documents read in full:

- `.agents/skills/augustus/SKILL.md`
- `.agents/skills/augustus/references/boundary-audit.md`
- `.agents/skills/augustus/references/mental-models.md`
- `.agents/skills/augustus/references/judgment-class.md`
- `.agents/skills/augustus/references/question-design.md`
- `.agents/skills/augustus/references/composition-algebra.md`
- `.agents/skills/augustus/references/formal-methods.md`
- `.agents/skills/augustus/references/validation.md`
- `.agents/skills/augustus/references/mixed-architecture.md`

Arithmetic was checked locally with Node: `0.95**4`; `1-0.05**(1/20)`; `ceil(log(0.05)/log(0.99))`; `ceil(log(0.05/41)/log(0.99))`; negative log losses for `0.8`, `0.4`, and `0.6`; and the binary temperature-scaling example. No proposed empirical experiment below was run. Repository-wide checks are left to the coordinator so this isolated answering worker does not inspect behavioral expectations through the test suite.

## 1. exact_dates

Prompt:

> Our invoices already have validated ISO due dates and payment dates. Should we use a decision model to decide whether each payment was late?

Answer:

No model is needed. Compare the parsed dates directly: `payment_date > due_date`, using your agreed deadline and grace-period policy. If these are timestamps, normalize time zones and define the cutoff precisely. Test payments before, on, and after the deadline. This is an exact rule with auditable results.

## 2. refund_router

Prompt:

> We generate JSON with a large LLM to sort refund emails, then a service issues refunds when confidence is above 0.9. Audit this design. Emails may omit order IDs.

Answer:

The dangerous join is turning a classifier's confidence into permission to refund. JSON validity and a score above 0.9 establish neither eligibility nor the correct payment target.

Use one bounded judgment for refund intent, with non-refund and unclear outcomes. Compare a smaller classifier with your current system before replacing it. If an order ID is missing, retrieve authorized customer records or ask for identifying information; ambiguous matches go to support. Never invent an ID.

Keep eligibility, remaining refundable amount, payment ownership, authorization, duplicate prevention, and the final state recheck in the refund service. Verify the effect after execution. Missing evidence, malformed output, and timeouts should hold the refund for the named support queue.

Qualify the score's meaning and select policy on separate calibration data. On untouched labeled emails, compare erroneous refunds, missed requests, review load, and total cost. Reject the change if it increases unauthorized or misdirected refunds.

## 3. portfolio

Prompt:

> Our community library has funding for three of eight proposed programs. Staff notes describe likely demand and accessibility, and costs are known. Help us make the decision.

Answer:

Use a small, explicit allocation exercise owned by library staff. Put each program's cost, expected demand, accessibility evidence, staffing needs, and uncertainty into a common table. Staff should define accessibility requirements and other hard constraints first, then agree which remaining benefits can trade off and how.

The notes may need careful interpretation; staff can do that directly, or a model can propose criterion-specific assessments with supporting passages for review. Missing demand evidence should remain unknown. An ordinal rating is not automatically a quantity you can add to dollars or attendance.

There are only 56 three-program combinations. Enumerate them, remove infeasible combinations, and compare the remainder for reach, overlap, and the agreed benefits. Vary uncertain demand estimates and reasonable weights. If the winner changes easily, gather the particular evidence that would settle it. Record the decision and check actual attendance, accessibility, and spending afterward.

## 4. ranker_gate

Prompt:

> Our passage reranker emits a score of 0.92. Can we treat that as 92 percent probability a claim is true and publish automatically?

Answer:

No. A reranker's score generally describes relative relevance within a candidate set. A highly relevant passage can still contain a false claim, and 0.92 has no established meaning as a truth probability here.

Keep the reranker for ordering passages. For publication, inspect whether identifiable, current sources actually support the specific claim, including contradictions and missing evidence. A separate evaluated judgment can assist that review; publication authority remains with your explicit editorial policy.

Test on independently adjudicated claims, including relevant-but-false passages, unsupported claims, and contradictory sources. Measure erroneous publications and review coverage at the proposed threshold on untouched data. Until that policy is qualified, route the draft to an editor. Changing the numeric threshold alone cannot fix the score's meaning.

## 5. joint_failure

Prompt:

> Four model checks each pass 95 percent of the time. They share the same document. Is the chance all four are right 0.95 to the fourth?

Answer:

First distinguish passing from being correct: a 95% pass rate says nothing by itself about accuracy.

Even if each check is correct 95% of the time on the same population, `0.95^4 ≈ 81.45%` requires mutual independence. A shared document can cause all four checks to miss the same missing fact or misleading passage. Pairwise independence would not be enough either.

With only those four correctness marginals, the all-correct probability can range from 80% to 95%. Evaluate all four together on independently labeled documents and directly count the joint failures and resulting action errors. Split and analyze by document, retaining the complete vector of outcomes. That measures the workflow you actually intend to use.

## 6. conformal

Prompt:

> I calibrated a 90 percent conformal prediction set on last month's tickets. Can every singleton result bypass review for this month's new language and enterprise customers?

Answer:

No. The usual 90% conformal guarantee is marginal coverage under exchangeability and the method's other assumptions. It does not promise 90% correctness among singleton outputs, within every customer group, or on each ticket.

New languages and enterprise customers are material population changes. Last month's calibration does not establish coverage for them, and a singleton does not itself authorize bypassing review.

Keep these new populations in the review queue while collecting representative labels. Define the acceptable error rate and review capacity, then qualify a policy on those populations, with adequate subgroup support and a fresh evaluation set. Check set coverage, singleton error, review volume, and action costs separately. If you use a method intended to handle shift or control risk, verify its specific assumptions; ordinary threshold tuning does not supply that guarantee.

## 7. no_match

Prompt:

> A classifier must pick sales, billing, or technical support. It assigns an unsubscribe request to billing with confidence 1.0. Raising the threshold did not help. Fix the design.

Answer:

The correct answer is missing from the offered set. Raising confidence cannot make a closed classifier select an unavailable label.

Add an unsubscribe route with a clear definition if your service handles these requests, plus an explicit other/no-match outcome for uncovered intents. Keep insufficient evidence distinct where it needs a different response. A broad support queue should own unresolved cases. Any subscription change must still use the authenticated account and existing preference-management rules.

Test genuine unsubscribe requests, billing messages that mention subscriptions, ambiguous requests, unfamiliar intents, and cases where the true candidate is deliberately removed. Include examples where other is both correct and incorrect. Measure wrong routes and fallback load on untouched data; a no-match label provides an escape path, but does not guarantee detection of every unfamiliar request.

## 8. model_checker

Prompt:

> We wrote an Alloy model of access control and a decision model says it looks safe. Can we skip exploring counterexamples and use that as our security acceptance?

Answer:

No. The decision model's opinion does not establish an Alloy property or validate the relationship between your model and the implementation.

Run the Alloy Analyzer on meaningful access-control assertions, inspect counterexamples and allowed instances, and record the exact model, tool version, commands, and finite scopes. A completed search without a counterexample supports only the stated bounded claim. Check that constraints have not excluded all interesting behavior, and seed defects such as a cross-tenant grant or failed revocation to see whether the assertions catch them.

Review whether the model represents the real authorization and state changes. Keep permission checks enforced in the application, including at execution time. A decision model could help prioritize counterexamples for human attention; security acceptance still needs the actual checker evidence and implementation-level validation.

## 9. supplier_intervention

Prompt:

> Our model predicts which suppliers will deliver late. Should we fine them to make delivery faster? We have only historical order data, and managers intervened on the highest-risk orders.

Answer:

The prediction does not establish that fines improve delivery. Your labels already reflect managers' interventions: a high-risk order may have arrived on time because someone intervened. Comparing treated and untreated orders directly would mix intervention effects with the reasons managers selected them.

Use the predictor to prioritize investigation while you define the proposed fine, delivery outcome, target suppliers, and possible adverse effects. Examine what interventions were recorded and whether comparable orders had a real chance of receiving either treatment. Without that overlap or sufficient information about confounding, historical data may not identify the effect.

An authorized, suitably designed randomized pilot would provide stronger evidence; a credible observational design needs explicit identification assumptions. Compare fines with feasible alternatives and no intervention, measuring delivery and total consequences. Keep the existing policy until evidence supports a beneficial change.

## 10. local_parity

Prompt:

> A local constrained decoder has the same JSON API as Jev and agrees on 95 of 100 examples, twice as fast. Is it a drop-in replacement for our approval queue?

Answer:

It is a candidate replacement, but those results do not qualify it for the approval queue. API compatibility checks representation; agreement with Jev checks agreement, not correctness. The five disagreements could contain every consequential approval error, and identical top labels can still conceal different threshold behavior.

Document the local model, decoder, score semantics, and failure modes. Shadow both systems on representative queue items with independent labels, without changing who receives sensitive data. Use separate data for calibration and final evaluation. Compare false approvals, abstentions, subgroup performance, review load, and total cost at the actual policy thresholds.

Measure latency on your target hardware including cold starts, retries, and fallback. Test missing evidence, unsupported inputs, malformed responses, and outages. Version the adapter and policy together; replace the current system only if the complete workflow meets prespecified acceptance limits.

## 11. plain_rewrite

Prompt:

> Rewrite this sentence more clearly: The meeting was moved because the room was unavailable.

Answer:

The room was unavailable, so we moved the meeting.

## 12. research_promotion

Prompt:

> A repo we catalogued has 200 more stars, a new SHA, and an updated README that retracts a calibration result. How should Augustus absorb this update?

Answer:

The retraction is the material change. Treat it as a substantive revisit, with the same scrutiny as a newly discovered important source. Confirm the repository's stable identity, pin the new revision and dated README evidence, and update its existing research card while preserving the earlier claim and when it was observed.

Record the star increase as an observation; it does not support calibration or justify runtime guidance. The new SHA identifies a revision, but does not by itself explain what changed.

Trace any Augustus guidance that relied on the withdrawn result. Remove or qualify unsupported conclusions and refine only the affected reference if the evidence changes a design decision. Keep source inventories and revision bookkeeping in research. If installed behavior changes, use a development version, run the checks, and obtain fresh behavioral review. Do not label the retracted result reproduced without an actual retained run.

## 13. wrapped_confidence

Prompt:

> We replaced the official client with a compatible wrapper. It averages option permutations and puts the winning mean probability in confidence. Can our existing confidence >= 0.8 approval rule stay unchanged?

Answer:

You cannot carry the rule over without requalification. The wrapper has changed the meaning of a policy input: winning mean probability is not automatically the official client's confidence statistic, even though the JSON key is identical.

Document both definitions and the aggregation procedure. Align probabilities by stable label IDs before averaging, retain the raw distributions, and version the wrapper, sampled orders, calibrator, and approval policy. Averaging also does not make the resulting probabilities calibrated.

Replay the old and proposed policies on independently labeled cases, emphasizing threshold crossings, false approvals, review coverage, and subgroup behavior. Select any revised operating point on calibration data and verify it on untouched examples. Preserve the qualified approval path or review affected cases in the meantime. The threshold might ultimately remain numerically 0.8, but that would be a new measured policy decision.

## 14. permutation_guarantee

Prompt:

> Two orderings assign the true label probabilities 0.8 and 0.4. Averaging gives 0.6. A teammate says Jensen proves this beats either ordering and is calibrated, so eight sampled permutations make any Choice safe. Check that claim and propose the smallest test.

Answer:

Jensen bounds convex loss of the average by the average loss; it does not beat the best ordering. Here, log loss is about 0.511 for 0.6, versus 0.223 for 0.8 and 0.916 for 0.4. The ensemble beats their mean loss, about 0.570, but loses to the better ordering. Nothing in that inequality establishes calibration, accuracy, or safe approvals.

Eight sampled permutations are not full permutation averaging and may remain order-sensitive. Correlated predictions do not invalidate Jensen, but they are not eight independent sources of evidence.

For the smallest useful experiment, compare a fixed ordering, a deterministic canonical ordering, and the eight-order ensemble on the same untouched labeled cases. Align full probability vectors by stable label IDs; freeze seeds, orders, and tie rules. Include cases near the policy threshold and absent correct candidates. Measure proper loss, calibration, action errors, coverage, latency, and cost. Reject the ensemble if its practical benefit disappears.

## 15. multimodal_window

Prompt:

> A multimodal decision head supports video and returns high confidence that a 10-minute inspection contains no fault. Its loader samples 16 frames. Can we let it sign off the inspection?

Answer:

No. The model observed 16 sampled frames, so its evidence cannot establish that the entire ten-minute inspection was fault-free. A brief fault may occur entirely between frames. Higher confidence cannot recover an unobserved event.

Record the actual frame timestamps, sampling method, resolution, clipping, and missing-media behavior. Restrict any model statement to what those observations support. Inspection sign-off should follow an authorized procedure whose observation coverage matches the faults you need to detect, such as continuous review or suitable telemetry, with incomplete coverage sent to the responsible inspector.

The smallest falsifier is a known, decisive fault placed between the selected frames, alongside visible-fault and clean controls. Evaluate event recall across durations and positions against independent ground truth and your existing inspection method. A confident miss rejects the whole-video clearance claim.

## 16. rag_accounting

Prompt:

> Our RAG filter keeps 15 percent of chunks and the model judge accepts 98 of 100 answers in both arms. The timer starts after filtering and the cost chart uses another model's token rate. Can we announce equal quality at lower cost?

Answer:

You can report those observations with their limits, but they do not establish equal quality or lower total cost. Keeping 15% of chunks is neither measured token savings nor retained evidence recall. Matching 98/100 judge acceptance rates can hide different errors, judge bias, and substantial uncertainty.

Run a paired comparison using the same questions and initial retrieved candidates. Independently adjudicate answer correctness and source support, measure retained evidence recall, and prespecify an equivalence margin with adequate sample size before claiming equal quality.

Start timing before filtering and include follow-up searches, generation, retries, cache behavior, and fallbacks. Use the actual serving model's usage and rates, separating known charges from estimates and missing usage. Another model's price is a scenario estimate. Publish lower total cost only if savings remain across that complete boundary at the required quality level; otherwise retain the unfiltered baseline.

## 17. risk_support

Prompt:

> Our frozen routing rule made no mistakes on 20 independent accepted examples in a rare category. Can we claim its error is below 1 percent with 95 percent confidence? We also have 40 other categories.

Answer:

No. Assuming those are representative IID accepted cases under the frozen rule, the one-sided exact 95% upper error bound with zero errors is `1 - 0.05^(1/20) ≈ 13.9%`. Twenty successes are compatible with much more than 1% error.

For one category, at least 299 independent, error-free accepted examples are needed for that bound to fall below 1%. This requirement concerns accepted examples, so a rare category may need many more total inputs.

If you need simultaneous 95% confidence across this category plus 40 others, account for all 41 claims. A simple conservative Bonferroni allocation uses `0.05/41` per category, requiring 668 error-free accepted examples in each under the same assumptions. Other valid simultaneous procedures may differ.

Gather the required support or retain review. Report the current count and bound; do not pool away a required category guarantee or retune on the evaluation cases.

## 18. attack_controls

Prompt:

> Appending hostile text changed 12 of 20 classifier answers. We repeated each case five times and want to publish a 60 percent injection vulnerability rate over 100 independent samples. Is that a sound claim?

Answer:

No. The supported observation is that answers changed on 12 of 20 cases under your tested setup. A changed answer is not necessarily an error, an attack-caused error, or a harmful downstream action. Five repeats per case produce clustered observations, not 100 independent cases.

For each base case, establish the clean gold label and whether the clean classifier was correct. Pair the hostile addition with a length-matched harmless addition, and verify that neither adds substantive evidence that legitimately changes the intended label. Define attack success and the eligible denominator before analysis; report clean failures separately.

Evaluate repeated runs as within-case variability, keeping case-level counts and uncertainty that respects clustering. If the deployment concern is unauthorized action, run the actual policy and record those action changes. Then report a controlled attack-success rate with its population, denominator, and uncertainty.

## 19. temperature_policy

Prompt:

> A positive scalar temperature calibration leaves every top label unchanged. Does this prove the approval workflow is unchanged when it uses a probability threshold?

Answer:

No. Positive temperature scaling preserves the ordering of logits, but it changes probabilities and therefore can move cases across an approval threshold.

For a binary prediction of 0.9, temperature 2 changes the positive probability to 0.75. The positive label still wins, but a policy approving at 0.8 now sends that case elsewhere. Approval coverage, review demand, and expected loss can all change despite identical label accuracy.

Treat the calibrator and policy as a versioned pair. Fit calibration and select thresholds on designated calibration data, then replay old and proposed workflows on untouched representative examples. Compare threshold crossings, false approvals, abstention, and total action cost, including subgroup differences. Workflow equivalence requires evidence about those actions; unchanged top labels alone cannot establish it.
