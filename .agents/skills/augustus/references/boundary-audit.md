# Boundary audit: inserting judgment into existing software

When the request is a codebase, PR, or running workflow — not a greenfield
design — hunt for judgment-shaped holes that are already being filled badly.
Do not start by wrapping the API. Prefer the smallest insertion that lets
code own the rest.

This card is an **operational recipe** (Hypothesis as a procedure). Each
insertion still earns its own Contract / Empirical recipe / Hypothesis
status on a decision-design card.

## Three-way split

At each workflow step, classify before proposing Jev:

- **Exact** → code: arithmetic, dates, lookups, authorization, schema
  validation, cryptography, known transforms, parsers that already work.
- **Bounded semantic judgment** → Jev candidate (fit test below).
- **Open-ended generation** → an LLM: writing, explanation, code
  generation, long-form synthesis, open-ended research. Jev may gate,
  route, or verify *around* that call; it does not generate.

Do not use Jev by default. A regex or lookup that already solves the
problem stays.

## Symptoms (look here first)

Insertion points often look like:

- LLM → prose → parser → JSON → validation → retry
- a prompt-based classifier returning unconstrained JSON
- a large regex or if/else tree classifying *meaning*
- an agent loop whose only job is a bounded decision
- an expensive reasoning model used for a trivial classification
- the same semantic classifier duplicated across handlers
- humans reviewing obvious cases because the machine has no abstain path

The shape of a real hole:

```text
unstructured or contextual evidence
        → a bounded judgment is required
        → software needs a typed value to continue
```

Typical contents of that hole: intent, routing, moderation, document
class, evidence/citation checks, guardrails, risk signals, candidate
selection, relevance, urgency, tool/function selection, extraction from a
*known* candidate set, RAG passage filtering, triage, quality, policy-to-
case comparison, fuzzy match / entity alignment, escalation.

## Fit test

A hole is a strong Jev candidate when most of these hold:

- the input is language or context, not already-structured facts
- the required output can be bounded (Choice set, Score levels, Noul
  proposition)
- software needs the answer programmatically
- a knowledgeable person could answer in a second given the state
- the judgment can be stated explicitly
- uncertainty is useful (abstain / confirm / escalate)
- the result can be tested against examples or labels
- code can own the action after the judgment

Be skeptical when the task needs long deliberation, many dependent
intermediate conclusions, open-ended generation, or autonomous planning.
Decompose first (`references/question-design.md`).

## Opportunity map

Walk the workflow: inputs, deterministic steps, semantic decisions, model
calls, parsers, routers, tool calls, side effects, human-review points.

For each candidate, one row — then a decision-design card if you proceed:

```text
LOCATION: module / workflow step
CURRENT METHOD: how the judgment is made today
CANDIDATE: yes / no / maybe
WHY: bounded semantic decision or not
STATE: minimum evidence (structured, current, observed — not assumed)
PRIMITIVE: Choice / Score / Noul; atomic questions
COMPOSITION: what code does with the answers
UNCERTAINTY: behavior when unclear (per-action, not one global bar)
RISK: cost of a wrong judgment
EVALUATION: experiment that could reject this insertion
```

Prioritize leverage: replace fragile semantic code, repeated LLM parsing,
expensive trivial reasoning, unbounded agent loops used as classifiers,
duplicated classifiers, or manual review of obvious cases. Keep behavior
bounded and testable.

Recommend the **smallest viable boundary**. Do not redesign the
application around Jev.

## Atomic questions, then code

One coherent judgment per question. Policy stays in code — never "what
should the application do?" as a single question.

Fan out independent questions over the same state (speculative ones
included; code ignores unused answers). A second request only when the
first answer is required to fetch evidence, build state, choose the next
candidate set, or walk a hierarchy.

The same judgment can authorize a low-stakes path and must not authorize
an irreversible one. Thresholds are per-action policy, measured on this
system's data (`references/validation.md`). A copied example threshold is
a prior, never a setting.

Shadow-mode the gate (log the action you would have taken) until the
falsifying experiment fails to reject it; then enforce.

## Around a generative model

Jev is often the control layer around an LLM, not a replacement:

- input → guardrail Nouls → LLM → citation/quality verification → code
  decides whether to return
- query → retrieve → relevance / injection judgments → selected context
  → reasoning model
- request → function Choice + bounded argument judgments → confidence /
  risk gate → typed function (code still validates arguments,
  authorization, and side effects)

## Centralize policy; keep raw judgments

Keep questions, criteria, weights, and threshold constants in one
reviewable module — not scattered across route handlers. A reviewer must
be able to see: what is judged, the definitions, the action thresholds,
which actions are reversible, and the low-confidence path.

Store raw answers (Choice + probabilities + confidence, Score
distribution, Noul value) separately from derived actions, so thresholds
and weights can be retuned without re-inference. Do not retain sensitive
state beyond legitimate need.

## Red flags

Stop and redesign when you see:

- one giant question making many unrelated judgments
- Jev choosing its own next tool in a loop
- business logic hidden in prompt prose
- deterministic calculations delegated to Jev
- high-stakes side effects with no risk gate
- thresholds copied from an example
- serial calls whose questions could share one state
- huge irrelevant state
- confidence treated as guaranteed correctness
- Noul 0.5 read as "medium"
- typed output described as hallucination-proof
- SDK fields written from memory instead of live docs

## Completion

A finished insertion answers:

- Why is a model needed here at all?
- What exact judgment is it making, why atomic, why this primitive?
- What evidence can it see, and which judgments share a request?
- What remains deterministic?
- What happens when the answer is uncertain? when it is wrong?
- How do we measure "better than the current method"?
- Can a human review the questions and thresholds in one place?

If those are unclear, the boundary is not finished. Fill the
decision-design card and the smallest falsifying experiment next.
