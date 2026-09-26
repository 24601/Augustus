---
type: llm
---

Judge the final reply's proposed dataset for routing the first message from
new customers, not whether training ran or whether particular phrases appear.

PASS only if the plan prevents related tickets/customer records and quoted
duplicates from leaking across evaluation boundaries, removes post-routing
information from prediction inputs, and handles the difference between the
desired intent label and final queue through explicit label review or an
honest ambiguity policy. It must reserve evaluation evidence independent of
model/feature selection and must not claim measured results without a run.

FAIL if it simply randomly splits reply rows, treats the final queue as
unquestioned ground truth, uses resolution notes at inference, or presents
planned metrics as achieved. Accept different workable splitting and
adjudication methods; naming leakage or provenance without a concrete data
decision is insufficient. Ignore formatting and model-family preference.
