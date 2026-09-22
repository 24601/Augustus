# Boundary audit: inserting judgment into an existing practice

When the request is a codebase, PR, running workflow, *or a non-software
practice* (inbox, hiring loop, reading list, incident command) — not a
greenfield design — hunt for judgment-shaped holes that are already
being filled badly. Do not start by wrapping an API. Prefer the smallest
insertion that lets policy own the rest. Cross-domain frames:
`mental-models.md`.

This card is an **operational recipe** (Hypothesis as a procedure). Each
insertion still earns its own Contract / Reported / Reproduced / Hypothesis
status on a decision-design card.

## Three-way split

At each workflow step, classify before proposing Jev:

- **Exact** → code *or policy*: arithmetic, dates, lookups, authorization,
  schema validation, cryptography, known transforms, parsers that already
  work, ledgers, law, recipes, two-person rules, thermometers, credit
  limits. Policy is the code of a practice that has no repository.
- **Bounded semantic judgment** → Jev-class candidate (fit test below).
- **Open-ended generation** → an LLM or a person writing: explanation,
  code generation, long-form synthesis, open-ended research. A
  judgment-class model may supply gate evidence, route, or inspect *around* that call;
  it does not generate.

Do not use a judgment model by default. A regex, lookup, checklist, or
recipe that already solves the problem stays.

## Symptoms (look here first)

Insertion points often look like:

- LLM → prose → parser → JSON → validation → retry
- a prompt-based classifier returning unconstrained JSON
- a large regex or if/else tree classifying *meaning*
- an agent loop whose only job is a bounded decision
- an expensive reasoning model used for a trivial classification
- the same semantic classifier duplicated across handlers
- humans reviewing obvious cases because the machine has no abstain path
- a weekly LLM summary of "how the project feels" instead of per-item
  instrumentation (rejected opposite of NATM)
- a hiring / bid / paper Score that hides vetoes in one "how good"
- a safety case that is a confidence number
- judged at t0, acted at t1, no re-probe (TOCTOU-of-Noul)

The shape of a real hole:

```text
unstructured or contextual evidence
        → a bounded judgment is required
        → software or an accountable process needs structured evidence
```

Typical contents of that hole: intent, routing, moderation, document
class, evidence/citation checks, guardrails, risk signals, candidate
selection, relevance, urgency, tool/function selection, extraction from a
*known* candidate set, RAG passage filtering, triage, quality, policy-to-
case comparison, fuzzy match / entity alignment, escalation.

## Fit test

A hole is a strong decision-model candidate when most of these hold:

- the input is language or context, not already-structured facts
- the required output can be bounded (labels, ranks, spans, rubric levels,
  or a proposition; Choice/Score/Noul are example interfaces)
- software or a repeatable human decision process can use the answer
- a knowledgeable person could answer from the supplied state without new research
- the judgment can be stated explicitly
- uncertainty is useful (abstain / confirm / escalate)
- the result can be tested against examples or labels
- code or accountable human policy can own the action after the judgment

Be skeptical when the task needs long deliberation, many dependent
intermediate conclusions, open-ended generation, or autonomous planning.
Decompose first ([question design](question-design.md)).

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
PRIMITIVE: bounded label / rank / span / rubric / proposition; atomic questions
COMPOSITION: what code or accountable policy does with the answers
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

The same judgment can support different policies for reversible and
irreversible actions. Policy owns authorization and thresholds, measured
on this system's data ([validation](validation.md)). A copied example
threshold is a hypothesis to test, not a deployment setting.

Shadow-mode the proposed policy and evaluate against prespecified acceptance
criteria. Failure to reject a hypothesis alone is not evidence of sufficient
safety or benefit; require adequate sample size and a controlled rollout.

## Around a generative model

Jev is often the control layer around an LLM, not a replacement
([mixed architecture](mixed-architecture.md) is the full placement card):

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
- a model choosing tools without bounded candidates, budgets, or host validation
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
- a Noul used as a proof, model-check, or DST property
- TOCTOU-of-Noul: judged at t0, acted at t1, no re-probe
  (`formal-methods.md` §5) — includes credit-then-wire, "looks done"
  then serve, "spec looks good" then merge
- vacuous / tautological spec (Hillel vibing specs) plus "the model said
  it looks good"; MCP "ran the checker" on a tautology (receipt theater)
- Apalache random-exec or Quint `run` cited as unbounded safety
- benchmark scores transferred to a different runtime or task without evidence
- Alloy vs Apalache collapsed into "we model-checked it"
- similarly named sources conflated; a done-Noul settling a durable promise
- independence fiction (multiplying Nouls) or Score unit fiction
- population-scale thresholds copied onto a small situated workflow
- silent base-code edits to satisfy Dafny/Lean

### TOCTOU-of-Noul (stop condition)

The check was never atomic because it was never a check. If the
insertion authorizes an irreversible act from a Noul taken before the
world can have moved, redesign: interlock in code/policy; re-probe;
treat t0 as advisory routing. Fail-closed authorize cannot be a stale
Noul. Same shape in inbox, hiring, kitchen, and incident command as in
agents.

### Vacuous spec (stop condition)

If the property is a restatement of a definition (`canImport = P ∨ Q`
then "prove" `¬P ∧ ¬Q ⇒ ¬canImport`), the checker passing is not a
result. Do not add a Noul "does this spec look good?" on top. Demand a
meaningful property that can fail on a plausible bad implementation, plus a run
of the real tool and a mutation/vacuity check (`formal-methods.md` §5 AI×FM).
A specification that
typechecks is not necessarily a faithful or adequately tested model.

### Harmful-uses checklist

Copy into the insertion's PR/decision card (`formal-methods.md` §5):

- [ ] Probabilistic gate on an irreversible act without a hard interlock?
- [ ] "Verified" only of a model the team has not broken?
- [ ] Properties strong, or tautological?
- [ ] Choice/Score rubrics versioned with the consumer?
- [ ] Abstention defined per-action with costs?
- [ ] CEX/triage stored as evidence, not enforcement?
- [ ] Alloy vs Apalache vs TLC named correctly?
- [ ] Resonate protocol settlement vs agent "done" Noul separated?
- [ ] Antithesis properties as harness asserts, not chat opinions?
- [ ] Speculative MCTS/RL depth capped without a real simulator?
- [ ] Sequence diagram of check-then-act missing an atomicity note?
- [ ] Silent code edits to make Dafny/Lean pass?

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
