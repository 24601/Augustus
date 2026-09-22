# Independent behavior responses — 2026-09-21

## 1. Validated invoice dates

**Prompt:** Our invoices already have validated ISO due dates/payment dates. Should we use a decision model to decide if payment was late?

**Answer:** No. This is an exact date comparison, so keep it in code: parse the validated dates, apply the documented timezone and boundary rule, and compute `payment_date > due_date`. Encode grace periods, holidays, partial payments, and disputed invoices as explicit policy states rather than asking a model to rediscover them. A model would only be useful for a separate semantic task, such as deciding whether an unstructured dispute note claims an approved exception; it should not decide the lateness arithmetic.

References: [boundary audit](../../.agents/skills/augustus/references/boundary-audit.md), [question design](../../.agents/skills/augustus/references/question-design.md).

## 2. Refund-email pipeline

**Prompt:** We generate JSON with a large LLM to sort refund emails, then a service issues refunds above confidence 0.9. Audit this design; emails may omit order IDs.

**Answer:** The unsafe boundary is `confidence > 0.9 -> issue refund`. Valid JSON only proves shape, and a model score neither establishes refund eligibility nor authorizes a financial side effect. An omitted order ID is missing evidence, not uncertainty that a higher threshold fixes.

Split the workflow:

1. Use a bounded classifier for message intent, with `refund_request`, `other`, and `insufficient_evidence`; use span extraction only for identifiers literally present in the email.
2. Resolve the customer and order through authenticated account data or ask for the missing identifier. Never let the model invent or fuzzy-match the target of a payment.
3. In code, validate the order, amount, currency, ownership, refund window, prior-refund state, policy eligibility, operator/service authority, and an idempotency key. Re-read that state immediately before execution.
4. Auto-execute only if an explicitly approved policy permits that class of refund; otherwise hold for human review. Low confidence, no match, multiple plausible orders, malformed output, provider failure, and stale state all withhold the refund.

Replace the copied `0.9` cutoff with an operating point chosen from action costs and deployment calibration. Shadow the proposed policy first on a time-split, independently labeled set containing missing IDs, multiple orders, policy exceptions, hostile text, and new customer/email slices. Reject auto-refunding if end-to-end false refunds, missed valid refunds, review load, latency, or total cost fail prespecified limits; measure candidate resolution separately from intent accuracy.

References: [mixed architecture](../../.agents/skills/augustus/references/mixed-architecture.md), [question design](../../.agents/skills/augustus/references/question-design.md), [validation](../../.agents/skills/augustus/references/validation.md).

## 3. Selecting three library programs

**Prompt:** Our community library can fund three of eight proposed programs. Staff notes describe demand/accessibility and costs are known. Help us make the decision.

**Answer:** Use a small, transparent multi-criteria allocation process; do not hide the choice in one model score.

- First encode hard constraints: total budget, legal/mission eligibility, minimum accessibility requirements, scheduling capacity, and any communities that must not be excluded. Accessibility can be a floor rather than something high demand is allowed to compensate for.
- Have two reviewers independently rate each proposal's evidenced demand and accessibility from the staff notes using a short anchored rubric. Record `unknown` when the notes do not support a rating. Cost remains the known numeric value.
- Agree publicly on criterion weights and vetoes before seeing the total scores. Normalize criterion scales, then enumerate the 56 possible three-program portfolios and discard infeasible ones. Compare remaining portfolios on total benefit, cost, reach across communities, and concentration risk.
- Run sensitivity analysis across reasonable weights and resolve reviewer disagreements. If the winning portfolio changes easily, the decision is not robust: gather the specific missing evidence that could change it or make the trade-off explicitly at the library board.

The deliverable should be the eight-row evidence/rating table, the feasible portfolio table, declared weights/vetoes, and a short rationale for the chosen three. A model is optional for extracting candidate evidence from lengthy notes, but staff or the board should own criteria, ratings, and the final allocation.

References: [mental models](../../.agents/skills/augustus/references/mental-models.md), [question design](../../.agents/skills/augustus/references/question-design.md).

## 4. Four 95% checks

**Prompt:** Four model checks each pass 95% of the time; same document. Is chance all are right `.95^4`?

**Answer:** Not unless each 95% figure is a correctness probability for the relevant population **and** the four correctness events are conditionally independent. Checks on the same document usually share evidence, model behavior, and failure modes, so independence is unlikely. Also, a 95% rate of returning “pass” is not the same as 95% correctness.

If each check truly has marginal correctness 0.95 but dependence is otherwise unknown, the probability all four are correct can range from 0.80 to 0.95; `.95^4 = 0.8145` is just the independence case. Label whole documents and directly measure the all-four-correct rate, preserving document-level clustering and reporting uncertainty. For consequential policy, evaluate the composed action rather than manufacturing a joint probability from marginal scores.

References: [judgment class](../../.agents/skills/augustus/references/judgment-class.md), [validation](../../.agents/skills/augustus/references/validation.md).

## 5. Conformal singleton bypass

**Prompt:** I calibrated a 90% conformal prediction set on last month's tickets. Can every singleton bypass review for new languages and enterprise customers this month?

**Answer:** No. A 90% conformal guarantee is marginal over a target population under the method's exchangeability assumptions; it is not 90% correctness for every singleton, a subgroup guarantee, or an authorization rule. New languages, enterprise customers, and a new month are explicit distribution-shift risks, so last month's calibration may not transfer.

Keep those slices in review until you have representative calibration and untouched evaluation data for the current population. Check empirical coverage and error cost by language, customer tier, and time; consider a group-conditional/Mondrian method only where each group has enough valid calibration data. Decide bypass policy from the cost of a wrong action and measured selective risk, not set size alone, and monitor coverage, singleton rate, review load, and drift after a controlled rollout.

References: [validation](../../.agents/skills/augustus/references/validation.md), [mental models](../../.agents/skills/augustus/references/mental-models.md).

## 6. Missing unsubscribe class

**Prompt:** A classifier picks sales, billing, technical support; an unsubscribe request gets billing confidence 1.0. Raising threshold didn't help. Fix design.

**Answer:** The candidate set is wrong. A closed classifier must choose one offered label, so confidence 1.0 only means “billing relative to these inadequate options.” A threshold cannot recover a missing outcome.

Add a dedicated `unsubscribe` intent plus `other/none` and `insufficient_evidence`. If messages can contain both billing and unsubscribe requests, use multi-label classification or run an independent unsubscribe proposition rather than forcing one route. Once detected, code should execute the exact opt-out policy: verify the address/account and subscription scope, record the suppression, meet the required deadline, and confirm the effect. Route any remaining billing content separately. Test unsubscribe paraphrases, mixed-intent messages, missing/removed true labels, option-order changes, and out-of-domain mail; failures should go to triage, not a forced department.

References: [question design](../../.agents/skills/augustus/references/question-design.md), [judgment class](../../.agents/skills/augustus/references/judgment-class.md).

## 7. Supplier lateness and fines

**Prompt:** Our supplier lateness predictor: should we fine them to make delivery faster? Only historical orders; managers intervened on highest-risk orders.

**Answer:** Do not infer that from this predictor or use its risk score to auto-fine suppliers. It estimates lateness under the historical management policy, while targeted interventions changed outcomes for the highest-risk orders. That confounds the labels: a supplier predicted risky but delivered on time may have done so because a manager intervened. Predictive risk does not estimate the causal effect of a fine, and a fine may also change quality, prices, reporting, or supplier retention.

Keep contractual authority and any existing late-delivery rule exact and reviewable. To answer “will a fine improve delivery?”, define the treatment, eligible population, delivery outcome, time horizon, and adverse outcomes, then use a prospective randomized pilot among ethically and contractually eligible, similarly situated orders if feasible. Otherwise use a credible causal design with recorded intervention propensity and acknowledge its stronger assumptions. The current predictor can stratify a pilot or prioritize review, but it cannot authorize the treatment. Reject the fine policy if it does not improve on-time delivery net of quality, cost, disputes, and supplier-exit effects.

References: [mental models](../../.agents/skills/augustus/references/mental-models.md), [validation](../../.agents/skills/augustus/references/validation.md), [mixed architecture](../../.agents/skills/augustus/references/mixed-architecture.md).

## 8. Clear rewrite

**Prompt:** Rewrite more clearly: The meeting was moved because the room was unavailable.

**Answer:** The room was unavailable, so the meeting was moved.

References: none; this is a direct language edit.

## Review protocol used

The response set follows the repository's independent behavioral-review procedure in [CONTRIBUTING.md](../../CONTRIBUTING.md). These are an independent agent's actual answers, not hosted decision-model inference, an external benchmark, or a measured performance improvement. Expected-outcome notes were withheld from the answering agent.

## Difficulties using the skill

No material navigation difficulty. The skill clearly separated exact work, bounded judgment, policy, and checked action. The supplier-fine prompt required applying the validation reference's warning about counterfactual claims to an observational, intervention-confounded setting; the available facts were insufficient for a numeric treatment recommendation. The library prompt likewise lacked proposal details and stakeholder weights, so the answer provides a decision process rather than inventing a winning portfolio.
