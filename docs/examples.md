---
title: "Worked examples: routing and portfolio decisions"
description: "See how Augustus audits a refund classifier and helps a library choose programs. Example design cards, failure boundaries, and falsifying tests."
permalink: /examples.html
page_class: examples
---

# What a useful Augustus answer looks like

These are illustrative design examples, not tested product integrations or
claims about model performance. Bring your workflow, evidence, constraints,
and current baseline. The skill helps decide whether a model belongs at all.

## Refund-email routing

**Ask:** “We generate JSON with an LLM to route refund emails. A service issues
refunds above confidence 0.9. Some emails omit order IDs. Audit the design.”

**Expected design card:**

| Concern | Recommendation |
| --- | --- |
| Useful judgment | Identify refund intent; extract an order ID only if it is actually present. |
| Candidate / evidence gap | An absent ID needs authenticated lookup or a question to the customer, not a more confident guess. |
| Exact work | Check ownership, eligibility, amounts, prior refunds, permissions, and idempotency in code. |
| Authority | An approved policy decides which refunds may execute. A model score does not grant permission. |
| Failure | Missing target, stale state, no match, malformed output, and provider failure hold the refund. |
| Falsifying test | Compare the proposed route with the current baseline on held-out cases, measuring false refunds, missed valid requests, review load, latency, and total cost. |

The `0.9` threshold is not inherently meaningful. First establish what the
score measures, then choose an operating point from deployment evidence and
action costs. A typed response proves response shape, not refund entitlement.

## Three library programs under a budget

**Ask:** “We can fund three of eight programs. Staff notes describe demand
and accessibility; costs are known. Help us decide.”

**Expected design card:**

| Concern | Recommendation |
| --- | --- |
| Method | Multi-criteria analysis plus exact budget and capacity constraints. |
| Evidence | Link each rating to the staff notes; preserve unknowns and disagreements. |
| Values | People agree on criteria, weights, accessibility floors, and vetoes. A model does not invent stakeholder preferences. |
| Exact work | Enumerate the 56 three-program combinations, reject infeasible portfolios, and compare the rest. |
| Robustness | Vary plausible weights and examine which missing evidence could change the choice. |
| Model role | Optional extraction or rubric support for lengthy notes; no model is required if staff can assess them directly. |

Without the eight proposals and stakeholder choices, Augustus should provide
this process—not fabricate a winning portfolio. The same separation of
evidence, judgment, policy, and checked outcome works outside software.

## A useful “no”

“Our invoices already have validated due dates and payment dates. Should a
model decide whether payment was late?”

No. Compare dates in code under explicit timezone, boundary, and grace-period
rules. Consider semantic judgment only for a separate unstructured issue that
the dates cannot resolve, such as an exception request.

## Try and improve it

[Install Augustus](https://github.com/24601/Augustus#install), then ask it to
review one real decision. Keep the proposal small enough to reject cheaply.
If the recommendation overreaches, misses a constraint, or is hard to use,
[share a sanitized example](https://github.com/24601/Augustus/issues/new/choose).
Include what you expected and what it actually recommended; never upload
customer data, private prompts, credentials, or confidential contracts.
