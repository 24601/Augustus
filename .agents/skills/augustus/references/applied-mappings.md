# Applied placements: sieves, keep/drop, triage, rank, route

These cards describe where a bounded judgment sits in running software. They
are provider-neutral; `judgment-class.md` owns family choice, and live provider
documentation owns API details.

For every placement, record the evidence source, candidate coverage, exact
constraints, policy owner, error behavior, fallback, and outcome oracle. A
model's output is evidence, never permission.

## 1. Context sieve

**Goal:** reduce context without silently losing decisive evidence.

```text
blocks = deterministic split(tool output, history, files)
always_keep = instructions + errors + corrections + recent state + signatures
judgments = relevance(block, current task) for remaining blocks
policy = keep | hide-behind-recall-key
on error/uncertainty/truncation → keep
```

Use a bounded relevance judgment per block, or locate exact supporting spans and
copy them verbatim. Do not ask the model to summarize unless a generator is
explicitly part of the design. Preserve an immutable archive or recall key.

Coverage questions:

- Did the splitter retain headers, errors, identifiers, and continuation state?
- Can a hidden block be restored without inference?
- Is a rule/correction always kept regardless of score?
- Are transport errors distinguishable from “irrelevant”?

[GLiNER2.5 compaction](https://github.com/m-newhauser/gliner25-compaction) is
an extractive locate/categorize example; [jev-pruner](https://github.com/tamaratran/jev-pruner)
is a score-then-preserve-original example; [carryforward](https://github.com/Dharundp6/jev-carryforward)
keeps a verbatim fact ledger and uses judgment only for recall. Evaluate answer
quality after compaction, not token reduction alone.

## 2. Exact-text keep / drop

**Goal:** choose among bytes or nodes already held by the program.

```text
candidates = hunks | lines | spans | records | observed controls
model      = include / exclude / mixed, or relevance per candidate
policy     = exact subset operation
output     = original bytes and identifiers, never model-authored replacements
```

Use this for staging hunks, selecting citations, retaining evidence, or choosing
observed UI controls. `mixed`, no-match, low-confidence, or invalid identifiers
go to review or remain unchanged. The model cannot split a hunk, invent a quote,
or recover an omitted candidate.

The pointer-not-generator pattern is strongest when code verifies the pointer
against the source immediately before use. [Jev Reviewer](https://github.com/choxos/jev-reviewer)
points to source lines so code can copy exact quotations. In computer use,
[gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast)
scores observed accessibility/DOM controls; code still clicks and verifies.

Test exact byte preservation, invalid-id rejection, empty candidate sets,
no-match behavior, and candidate recall before judging selection quality.

## 3. Environment / harness triage

**Goal:** distinguish environment failures from agent or product failures before
spending a generator on diagnosis.

```text
exact facts = exit codes, missing files, timeouts, tool versions, test names
judgments   = failure category, likely shared cause, needs-human?
policy      = retry | repair environment | investigate product | escalate
generator   = writes an explanation only for selected incidents
```

Do not ask one vague “was the run good?” question. Parse hard evidence first,
then ask narrow questions over the trace. Cluster repeated failures in code so
one incident does not become twenty model calls.

A merge or release gate must not let the model waive a deterministic failing
check. A judgment may classify a failure as likely infrastructure noise, but
the policy decides whether to rerun, quarantine, or block. Missing evidence is
`unknown`, not clean.

[latch](https://github.com/CaseReed/latch) illustrates clustering a finished
red run before applying policy. The durable lesson is separation of evidence,
semantic cause, and gate—not its particular thresholds.

Evaluate with frozen traces containing real product failures, infrastructure
failures, mixed cascades, truncation, and missing secrets. Report false passes,
false blocks, time-to-diagnosis, and the end-to-end resolution rate.

## 4. Moderation and ranking

Moderation and ranking can share a model call but not an interpretation.

- **Ranking** orders items. On model failure, retain the source order or baseline
  rank. Measure nDCG, recall at K, or downstream user utility.
- **Moderation** chooses a policy lane such as publish, hold, or human review.
  Measure false-allow/false-hold by action severity and base rate.

Do not threshold a listwise relevance score as a calibrated permit. If a ranked
item can cause a consequential action, add a pointwise decision stage, exact
constraint, or human confirmation.

A practical pipeline is:

```text
retrieve broadly → rank shortlist → absolute fit/no-match judgment
→ policy lane → optional generator/human
```

Candidate coverage is upstream: neither ranker nor moderator can select an
item that retrieval omitted. An explicit `other`/`none` is required whenever
the offered labels are not exhaustive.

## 5. Skill / tool routing

**Goal:** select a relevant capability from an eligible catalog without
confusing discovery with authority.

```text
catalog = live host inventory
eligible = exact grants, platform, and schema filters
shortlist = lexical/embedding/ranker pass
fit = Choice + none/other, using full candidate descriptions
dispatch = code validates args, user intent, authority, and current state
```

Explicit user requests and exact matches bypass the model. Large catalogs may
use a two-stage shortlist, but evaluate whether the correct option survives the
first stage. A router that is accurate conditional on its shortlist can still
fail because candidate recall is poor.

No-match is part of correctness. A selected skill or documented command is not
a grant to run it. [skill-broker](https://github.com/adamjralph/skill-broker)
captures the candidates-versus-grants distinction; [JCR](https://github.com/NiazMorshed2007/jcr)
returns capability context without executing it.

Measure catalog coverage, top-K survival, final fit, no-match accuracy, latency,
and downstream task success. Include tool-call validation and authorization in
the trajectory eval.

## 6. Expensive observation router

**Goal:** buy OCR, a full document read, a lab test, or a generative diagnosis
only when cheap structure cannot answer.

```text
cheap exact observation
  ├─ sufficient → use it
  └─ insufficient/uncertain → bounded judgment: would more evidence change act?
                               ├─ yes/error → gather
                               └─ no → continue
```

The model does not manufacture missing evidence. It estimates whether an
additional observation is worth its cost. The fallback for router error is set
by the omitted observation's consequence: OCR a page when a false skip loses a
required field; skip only when the product can tolerate that miss.

Evaluate false skips with planted hard cases, preservation/order guarantees,
observation savings, p95 latency, and final task quality. Expected cost includes
the observation, router latency, later generator calls, human recovery, and the
cost of an undetected miss.

## 7. Capability kernel / human-confirmed gate

**Goal:** keep secrets, permissions, and irreversible effects outside the
agent's trust boundary.

```text
host creates closed action set and redacted/stunt-double state
model supplies bounded risk/fit evidence
policy returns BLOCK | ASK | ALLOW
human confirms high-impact actions
host refreshes identity, authority, target, and state
host executes and records receipt
```

The model never grants access. A positive score cannot override a deterministic
deny, missing permission, stale identity, or failed invariant. Keep secrets out
of model-visible state when possible; a model judging whether exfiltration is
safe is weaker than a system that never exposed the secret.

[interlock](https://github.com/somoore/interlock) is an example of the sensor /
policy split. [toolgate](https://github.com/fdemir/toolgate) illustrates a
pre-execution check over proposed calls. They occupy different trust boundaries.

Test bypasses, stale-state races, altered targets, provider outages, malformed
answers, approval replay, and post-action receipts. Soft judgment may influence
ASK versus routine handling, but it is not the sole safety interlock.

## 8. Decide → policy → LLM leftover cascade

**Goal:** use bounded decisions for control and a generator only for content
that must be written.

```text
prepare evidence exactly
→ batch typed judgments
→ policy: auto | review | gather | generate
→ generator writes only the leftover fields
→ validate generated output
```

Examples include triaging email before drafting a response, classifying a
ticket before writing a summary, or selecting a code action before generating
arguments. The generator fallback is not free: log why it ran, its latency and
cost, and whether a human still reviewed the result.

Do not treat a chat model's self-reported `confidence` as equivalent to a
decision probability. Do not round a middle band into action. If a provider is
unavailable, use a declared fallback lane and label its provenance correctly.

Evaluate all arms on the same frozen examples. Report stage accuracy,
calibration/selective risk where meaningful, auto-coverage, generator rate,
human rate, end-to-end outcome, and total expected cost. Cascade success—not a
single component score—is the product metric.

## 9. Closed-vote computer-use

**Goal:** complete an interactive task using only candidates constructed from
observed state and user-supplied facts.

```text
observe → enumerate valid actions and values → bounded vote
→ policy/risk check → execute existing handler → observe and verify
```

The model does not invent selectors, fill values, or permissions. Code keeps a
fact register from the goal and page, validates operation/target pairs, and
re-observes after every effect. A `done` vote only proposes termination; success
comes from a task oracle, server state, or independently checked UI state.

[JevOnly](https://github.com/buluoray/JevOnly) demonstrates the no-planner
extreme. [waymode](https://github.com/mossburgh/waymode) demonstrates an app
retaining handlers and permissions while exposing live typed actions.
[Cua-S1](https://github.com/trycua/cua/tree/main/libs/cua-s1) is a specialist
peer, not TypeSafe Jev.

Candidate generation and state freshness dominate the failure surface. Include
missing controls, reordered pages, stale element ids, unexpected dialogs,
authentication transitions, and irreversible actions in evaluation. Report
full-trajectory success, step count, recovery rate, latency, model/generator
calls, and human interventions—not only per-step choice accuracy.

## Compact acceptance checklist

- The family matches the output: decide, locate, categorize, rank, or perceive.
- Candidate coverage and missing-evidence behavior are measured.
- Exact constraints and policy are visible in code.
- Errors map to a named action, not a family-wide “fail open/closed” slogan.
- Generator and human fallbacks are explicit and costed.
- Authority and state are re-checked immediately before effects.
- The outcome is verified by evidence the judged system cannot forge.
- Evaluation includes cascades and trajectories, not only isolated questions.
