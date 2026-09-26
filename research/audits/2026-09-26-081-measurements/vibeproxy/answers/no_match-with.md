The working directory has no classifier code, so what follows is a design fix, not a patch.

## Why a higher threshold can't fix this

The classifier is only allowed to answer sales, billing or technical support. An unsubscribe request isn't any of those, but the model still has to pick one. Billing is the closest match, and the scores are normalized across just those three options, so billing ends up at 1.0.

That 1.0 means "billing beats the other two." It does not mean "this is a billing request." A confident wrong answer clears any threshold you set. You can't fix a missing option with a threshold.

## The fix: check scope before routing

**1. Handle unsubscribe in code, before the classifier.**
An unsubscribe usually has a legal deadline (CAN-SPAM, GDPR) and a known action. It shouldn't depend on a model. Catch it with:
- the list-unsubscribe header, an unsubscribe link or endpoint, or a form field; and
- a keyword/regex pass ("unsubscribe", "stop emailing", "remove me", "opt out").

A match goes straight to the suppression-list handler. Keep the matching broad: sending a borderline message to a human check costs little, while missing an opt-out can bring a compliance problem.

**2. Add a scope question before the routing question.**
The first question is: "Is this about sales, billing, technical support, or none of these?" Give it an explicit `none_of_these` option (or `other` with a short reason). Only in-scope messages go on to the three-way router. Doing this as two steps keeps "is this in scope?" separate from "which team?".

**3. Treat the three-way router's score as a relative score.**
Use it to rank the three teams, not as a probability that the message belongs there. Low margins, or a scope answer of `none`, go to a named fallback: a general inbox or human triage queue with an owner. Don't default to billing.

**4. Define what happens on every failure.**

| State | Action |
|---|---|
| Unsubscribe detected in code | Suppress now and confirm; don't route |
| Scope = none | Human triage queue |
| Two teams nearly tied | Human triage, or the cheaper-to-fix team if you've costed it |
| Malformed output or timeout | Human triage (not billing) |

## How to check it

- **Test set:** in-scope messages for each team, plus messages none of them should get: unsubscribes, spam, legal/GDPR requests, job applications, complaints. Held-out messages that no rule or prompt was tuned on decide whether you adopt it.
- **Metrics:**
  - how often out-of-scope messages get routed to a team (currently it's every time);
  - unsubscribe recall (should be close to 100%);
  - routing accuracy on in-scope messages;
  - how much ends up in human triage.
- **Rejection test:** if the new design loses noticeably more in-scope accuracy than it gains in catching out-of-scope messages, or the triage queue grows beyond what the team can handle, keep the current router and add only the unsubscribe code path.

If you share the classifier code or prompt, I can build the unsubscribe pre-filter, the scope question and an evaluation script against your data.
