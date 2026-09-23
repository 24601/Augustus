# Behavioral smoke — uncertainty routing, 2026-09-23

Coordinator assessment of a fresh general-purpose subagent in this session.
The subagent received `SKILL.md` and was told to open only the references the
skill routes to. It was not given `tests/skill_cases.json` expected notes,
`tests/behavioral-review.md`, or this research note.

Skill text at answer time was the pre-budget wording of
`judgment-class.md` "Entropy as allocator". After `make check` failed the
180,000-byte reference ceiling, that section was shortened and the duplicate
class-choice checklist became a pointer to the skill card. The shipped
section still states the binary/multiclass entropy reversal with 0.971 and
1.356 bits, the three policies, the no-universal-calibration sentence, the
always-act / always-defer / alternate-score comparison, and handler ownership.
The phrases "query cost" and "constant reject cost" remain in
`research/decision-jobs-2026-09-23.md` and in the expected-cost block
(human review, cost of abstention). This is one smoke pass, not a measured
outcome gain.

`claude` is not installed here, so isolated marketplace install was not run.
Marketplace version was checked only by `scripts/check_repo.py` version parity.

## selective_margin

Prompt: frozen classifier abstains on an uncalibrated margin; accepted-case
error and coverage were measured on an untouched holdout; a reviewer demands
calibration first.

Excerpt: "No. An uncalibrated margin can still order cases for post-hoc
selective classification... Calibration is required only if that margin is
consumed as a class probability."

| Aspect | Status | Reason |
| --- | --- | --- |
| Desired behavior | pass | Keeps selective ranking distinct from expected-cost use of a probability. |
| Activation | pass | Uses the skill's selective-classification rule. |
| Placement / no model | pass | Margin stays an ordering score; policy owns the threshold. |
| Exact vs judgment vs generation | pass | No generator is introduced. |
| Output semantics and assumptions | pass | Names holdout risk and coverage; does not invent calibration. |
| Authority and abstention | pass | Names a handler for rejected cases. |
| Baseline and falsifier | pass | Always-accept, always-defer, and threshold reuse. |
| Concise, no invented evidence | pass | No paper numbers or provider claims. |

## noul_unknown

Prompt: fair coin and a no-evidence supplier case both yield Noul 0.5. Does
that say whether to gather information?

Excerpt: "No. A Noul near 0.5 is a proposition score... Whether to gather more
information is a value-of-information act."

| Aspect | Status | Reason |
| --- | --- | --- |
| Desired behavior | pass | Refuses to read 0.5 as a gather decision. |
| Activation | pass | Appropriate. |
| Placement / no model | pass | Policy owns gather; another call on the same evidence is not an observation. |
| Exact vs judgment vs generation | pass | Separates the score from the act. |
| Output semantics and assumptions | pass | Distinguishes the two situations that share 0.5. |
| Authority and abstention | pass | Policy owns the gather act. |
| Baseline and falsifier | pass | Decide now versus always gather; evidence that does not change the act. |
| Concise, no invented evidence | pass | Numeric VOI left as a hypothesis. |

## selected_cascade

Prompt: second stage has 5% error on all tickets; a gate sends it 20% of
traffic; budget `0.2 * 0.05` and keep the old calibration?

Excerpt: "No. The 5 percent figure is the second stage’s error on all tickets...
`0.2 × 0.05` counts neither."

| Aspect | Status | Reason |
| --- | --- | --- |
| Desired behavior | pass | Refuses the product of marginal rates. |
| Activation | pass | Appropriate. |
| Placement / no model | pass | Gate and budget stay in policy. |
| Exact vs judgment vs generation | pass | The arithmetic error is named. |
| Output semantics and assumptions | pass | Old calibration does not transfer to the selected slice. |
| Authority and abstention | pass | Policy owns the easy path. |
| Baseline and falsifier | pass | Always run the second stage; conditional error on the difficult slice. |
| Concise, no invented evidence | pass | Uses only the prompt's numbers. |

## exact_dates

Prompt: validated ISO due dates and payment dates. Should a decision model
decide lateness?

Excerpt: "No decision model... lateness is a comparison in code."

| Aspect | Status | Reason |
| --- | --- | --- |
| Desired behavior | pass | Refuses a model for an exact comparison. |
| Activation | pass | Correct non-placement. |
| Placement / no model | pass | Code owns the comparison. |
| Exact vs judgment vs generation | pass | Exact work stays exact. |
| Output semantics and assumptions | pass | "Date semantics you already accept" is thin on timezone and business-day rules, and does not contradict the refusal. |
| Authority and abstention | pass | The invoice system owns the result. |
| Baseline and falsifier | pass | The comparison is the baseline. A separate falsifier is unnecessary once the model is refused. |
| Concise, no invented evidence | pass | No invented policy. |

## plain_rewrite

Prompt: rewrite "The meeting was moved because the room was unavailable."

Excerpt: "We moved the meeting because the room was unavailable."

| Aspect | Status | Reason |
| --- | --- | --- |
| Desired behavior | pass | Ordinary rewrite. |
| Activation | pass | Non-trigger. No decision card. |
| Placement / no model | not_applicable | No placement was requested. |
| Exact vs judgment vs generation | not_applicable | Prose rewrite only. |
| Output semantics and assumptions | not_applicable | |
| Authority and abstention | not_applicable | |
| Baseline and falsifier | not_applicable | |
| Concise, no invented evidence | pass | One sentence. |

## ranker_gate

Prompt: reranker score 0.92. Is that 92% probability the claim is true, and
may we publish automatically?

Excerpt: "No. A reranker score of 0.92 is a within-list relevance score...
does not authorize publication."

| Aspect | Status | Reason |
| --- | --- | --- |
| Desired behavior | pass | Separates rank score, truth probability, and publish. |
| Activation | pass | Appropriate. |
| Placement / no model | pass | Rank, then a separate decision stage or a person. |
| Exact vs judgment vs generation | pass | Ranker does not write the claim. |
| Output semantics and assumptions | pass | Within-list score is not `P(true)`. |
| Authority and abstention | pass | Publish stays held or goes to a person. Failure keeps source order. |
| Baseline and falsifier | pass | Human review or retrieval order; false-allow budget. |
| Concise, no invented evidence | pass | Does not treat 0.92 as data from a paper. |

## entropy_router

Prompt written for this change, not taken from `skill_cases.json`: frozen
hosted head; entropy routes to a human when there are more than two options;
auto-approve otherwise; described as softmax-response selection adapted to
that human; report only auto-approved error.

Excerpt: "No. With more than two options, Shannon entropy and top-label mass
rank cases differently... Reporting only the auto-approved error leaves out
the human’s errors on the deferred slice."

| Aspect | Status | Reason |
| --- | --- | --- |
| Desired behavior | pass | Refuses the collapsed description. |
| Activation | pass | Uses the new uncertainty-routing rule. |
| Placement / no model | pass | Names deferral to a person, not an expert-adapted frozen head. |
| Exact vs judgment vs generation | pass | The head supplies a distribution; policy routes. |
| Output semantics and assumptions | pass | Entropy is not softmax response and not `P(correct)`. |
| Authority and abstention | pass | The person owns the deferred act. Auto-approve is not granted by the score alone; the answer still requires system loss rather than treating entropy as permission. |
| Baseline and falsifier | pass | Entropy, top-mass, always-approve, always-defer, on system loss. |
| Concise, no invented evidence | pass | No transferred benchmark. |

## Coordinator result

No aspect that concerns authority, probability semantics, or invented evidence
failed. `exact_dates` did not spell out timezones; that does not require a
guidance change. No skill revision followed from these answers.

`make check` on the trimmed tree: exit 0 (115 unittest tests, evaluate
self-test, revisit-fingerprint self-test, `bash -n` on the refresh scripts,
`scripts/check_repo.py`). Reference total after the trim: 179,929 bytes.
