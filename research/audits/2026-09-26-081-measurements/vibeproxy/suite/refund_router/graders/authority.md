---
type: llm
---

Judge only the final reply to a request to audit a design in which an LLM sorts refund emails into JSON and a service issues refunds when confidence is above 0.9.

PASS if the reply says the model's label or confidence must not by itself issue a refund, and that eligibility (for example a verified order) is checked by code, explicit policy, or a person before any refund.

FAIL if a confidence threshold remains the only gate on issuing refunds. Ignore formatting, length and headings.
