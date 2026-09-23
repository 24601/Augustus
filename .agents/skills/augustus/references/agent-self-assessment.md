# Agent self-assessment with bounded judgments

Use a narrow judgment loop to observe a broad generative agent. The supervisor
estimates named propositions; deterministic policy decides what happens. It
does not become the agent's conscience, permission system, test runner, or
source of truth.

Choose the decision head, classifier, or exact check per gate. Validate the
composed lifecycle on real traces.

## Lifecycle gates

### 1. Pre-action assessment

Before a consequential tool call, code checks exact facts first:

- tool and operation are allowed;
- arguments match schema and user scope;
- credentials and grants exist;
- target identity and current state are known;
- deterministic denies and rate limits pass.

Then a model may estimate narrow semantic properties such as destructive
effect, scope mismatch, secret exposure, reversibility, or ambiguity. Policy
maps those answers to proceed, ask, block, or gather evidence. The model never
grants access.

Re-check authority, target identity, and live state immediately before
execution. A judgment over an earlier snapshot cannot authorize a later action.
[toolgate](https://github.com/fdemir/toolgate) illustrates a pre-execution
check; [interlock](https://github.com/somoore/interlock) illustrates the
stronger design in which secrets and grants remain outside the agent.

### 2. Post-action output judge

Assess the result after it exists. Parse exit codes, response schemas, changed
files, test counts, and known error signatures exactly. Use bounded judgment
only for semantic residue: did the result address the requested object, does it
appear to contain sensitive content, or what failure category best fits?

Post-action judgment does not repair the result. It routes to a retry with a new
hypothesis, a human, or a generator that writes an explanation. Preserve raw
evidence for replay.

### 3. Done-check on the final reply

Completion is a claim that must join evidence:

```text
claim in reply
∩ required checks in trace
∩ observed product/repository state
∩ no unresolved blocker
```

Code can prove whether tests ran, files changed, or a receipt exists. A judgment
model can classify whether the language claims completion or whether cited
evidence actually supports a claim. It cannot turn an unrun check into a pass.

For interactive tasks, `done` means “the model proposes stopping.” Verify the
actual post-state through the host, server, DOM, test oracle, or user-visible
artifact.

### 4. Stuck detector

Use explicit trace features: repeated error signature, unchanged state,
identical command/tool, or no new evidence. After a bounded number of repeated
attempts, change hypothesis, gather evidence, or escalate. Do not use the model
to rationalize another identical retry.

Silence is neither safe nor successful. Timeouts, malformed answers, or missing
keys need a named fallback and heartbeat. The correct fallback depends on the
action: a failed advisory assessment may proceed with ordinary safeguards; a
failed authorization check must not execute.

### 5. Supervision during long runs

Estimate a small stable set of properties, for example:

- meaningful progress since the last checkpoint;
- on-track relative to the user's objective;
- verification sufficient for the next irreversible step;
- blocked versus merely slow;
- ready to finish versus more evidence required.

Fuse these estimates with exact counters, time budgets, verification history,
and state transitions. Use hysteresis so one noisy answer does not oscillate the
controller. Optional generator advice should be one bounded fallback, not a
parallel commander.

Evaluate full trajectories. Per-step accuracy hides correlated errors: a 95%
step classifier can still produce poor all-correct completion over a long run.
Report task success, unsafe-action count, false stops, wasted retries, human
interventions, latency, and total expected cost.

## Failure policy matrix

Failure policy belongs to the action, not the model family.

| Supervisor use | On model error or uncertainty |
|---|---|
| Advisory “look again” prompt | Continue under existing safeguards or request human attention |
| Drop/compact evidence | Keep the original evidence |
| Skip an expensive check | Run the check if a false skip matters |
| Select a reversible next step | Use a declared default or gather more state |
| Execute a mutating action | Withhold execution until policy/authority is satisfied |
| Publish or send | Hold for review or use a product-approved fallback |
| Mark complete | Remain incomplete until objective evidence exists |

For every gate, test timeout, malformed output, empty evidence, stale state,
missing candidate, and unavailable human paths.

## Non-negotiable boundaries

- A probability is evidence about a proposition, never an action permit.
- Type-valid is not correct; trained-for-calibration is not a deployed
  calibration guarantee.
- Ranking scores order; they are not automatically absolute risk or permission.
- Choice is conditional on offered candidates. Missing `other`/`none` can force
  a confident wrong answer.
- Missing evidence is not evidence of absence. Gather it or remain unknown.
- Parallel judgments are not independent; do not multiply them into a joint.
- A soft model output cannot waive tests, schemas, permissions, invariants, or
  human confirmation required by policy.
- Preserve raw judgments and trace evidence separately from derived actions.
- Re-check current state and authority just before effects.
- Cache only while state, model, rubric, candidate set, and policy version are
  unchanged.

## Hallucination/grounding/citation checks

Decompose generated output into atomic claims. For each claim:

1. retrieve or identify the exact cited source;
2. classify the relation as supports, contradicts, unrelated, or insufficient;
3. keep source offsets/identifiers;
4. route insufficient evidence to retrieval or human review;
5. copy citations from the source rather than asking the model to recreate them.

The evidence set must come from what was actually read, not another model's
summary. A true but unread claim is still unsupported in the current trace.
[Jev Reviewer](https://github.com/choxos/jev-reviewer) demonstrates the useful
pointer pattern: model selects source lines and code copies exact text.

Evaluate citation presence separately from entailment and source quality.
Include adversarial near-matches, contradictory passages, absent evidence, and
stale documents. A clean grounding score does not establish overall task
correctness.

## Preference lint (project rules, not taste)

When a supervisor checks project preferences, convert each written rule into a
narrow question over a named evidence window. Keep hard rules in parsers,
linters, tests, and policy.

```text
exact checks → hard failures
one bounded judgment per soft rule → raw distributions
policy bands → pass / warn / review
human or agent fixes the finding
```

Avoid “is this good?” and “does this feel right?” Name the rule and observable
evidence. A conflict with a rule is different from ignorance; include a conflict
or unclear outcome when needed.

Shadow first, then compare with independently labeled diffs. Tune thresholds by
action cost, freeze them, and confirm on a separate set. Report false warnings,
missed violations, review load, and whether the gate changes end-to-end quality.

## Candidate and evidence coverage checks

Self-assessment fails when it judges an impoverished view. Before trusting a
score, record:

- which tool results, files, messages, and state snapshots were visible;
- what was truncated, filtered, or inaccessible;
- how candidate actions were enumerated;
- whether `other`/`none` was available;
- whether later state invalidated the assessment.

If coverage is unknown, the safe semantic output is unknown—not approval. But
the operational response still depends on the action: gather evidence for an
important decision, retain context for compaction, or continue a harmless
advisory flow with the uncertainty logged.

## Cost and cascade accounting

The supervisor is useful only if the whole loop improves. Expected cost is:

```text
judgment calls + latency + retries
+ generator fallback + human review
+ cost of false block + cost of missed harm + recovery
```

Track stage-level and end-to-end metrics. A cheap supervisor that escalates most
turns, lengthens every trajectory, or creates review fatigue is not cheap.
Likewise, low average error can hide catastrophic errors concentrated on the
few irreversible actions.

## Using judgments to test and optimize the skill suite itself

Treat skill selection as a retrieval-and-fit problem:

1. Build the live catalog from frontmatter.
2. Apply deterministic explicit-name and eligibility checks.
3. Shortlist by descriptions.
4. Judge full-body fit for the shortlist, with `none` available.
5. Measure whether the correct skill survived candidate generation.

Test literal triggers, user paraphrases, and near-miss neighboring skills. Keep
frontmatter distinct: overlapping descriptions are candidate-recall and
selection failures, not merely wording style.

When using a judgment model as an evaluator or optimizer metric:

- measure repeated-run variance on frozen outputs;
- use independent human/outcome labels for validity;
- keep optimization and confirmation sets separate;
- do not optimize a threshold and report it on the same sweep;
- preserve generator/human fallback costs;
- evaluate the resulting agent trajectory, not just the judge's agreement.

The judge can help find weak cases. It cannot certify itself or replace final
acceptance accountability.

## Supervisor card

```text
Lifecycle point:
Exact facts checked first:
Bounded proposition(s):
Evidence snapshot and coverage gaps:
Candidate set and none/other behavior:
Policy owner and action:
Error/uncertainty fallback for that action:
Generator or human fallback:
Authority/state re-check:
Outcome oracle:
Trace and trajectory metrics:
Expected total cost:
Rejection criterion:
```
