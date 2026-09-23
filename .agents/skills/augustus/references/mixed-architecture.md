# Mixed architecture: judgment-class model + generator + code

This is Augustus's default placement. It is an architecture pattern, not a
provider tutorial.

```text
current evidence
  → exact preprocessing and candidate construction
  → bounded judgment
  → explicit policy
  → generator only for unresolved writing or candidate invention
  → authority/state re-check
  → checked action
  → observed outcome
```

Select the family from `judgment-class.md` by objective, and evaluate every
provider on the target data.

## Neighbor skills (load the right one)

- **Augustus:** decides where judgment belongs, which family fits, and how to
  falsify the placement.
- **Provider/API guidance:** owns live request fields, limits, SDK behavior, and
  authentication. Load it only when writing integration code and it is
  available.
- **Exact tools:** parsers, linters, solvers, databases, schemas, and policy
  engines keep their existing jobs.

This reference intentionally contains no request payload to copy.

## Default architecture

Assign one owner to each concern:

| Concern | Owner |
|---|---|
| Parse, count, calculate, validate schema, enumerate candidates | Code or exact tool |
| Estimate relevance, intent, risk, fit, or preference from supplied state | Judgment model |
| Choose thresholds, combine signals, authorize, rate-limit, log | Policy code and accountable operator |
| Write prose/code or invent a candidate not already present | Generator or person |
| Execute and verify effects | Host application |

The judgment model supplies evidence. It never owns permission. The host must
validate the operation and target, confirm authority, and refresh state just
before a consequential action. This closes the common time-of-check/time-of-use
gap: an earlier “safe” or “relevant” judgment cannot authorize an action after
the resource, user, permissions, or candidate set changed.

Batch independent questions that share state. Sequence only when a later
question genuinely depends on an earlier answer. Keep raw distributions apart
from derived actions so policy can be replayed without new inference.

## It's just classification

Classification is old. The architectural value is making one narrow semantic
judgment an explicit, testable software boundary rather than hiding it in an
LLM prompt or controller.

Use a decision model when the system needs a bounded answer, can supply the
relevant evidence, and has a meaningful abstention or fallback path. Prefer:

- a rule or parser when the answer is exact;
- a classical supervised model when the taxonomy is stable and representative
  labels are plentiful;
- a span extractor when the answer is text already present;
- a ranker when relative order is sufficient;
- a generator when new text or candidates are required.

Typed output means structurally valid, not factually correct. Calibration-aware
training means “measure this property,” not “assume it.”

## Cost-sensitive prefilter

A useful cascade spends expensive work only where it can change the outcome:

```text
broad candidate source
  → cheap exact filters
  → bounded judgment
  → {accept reversible path | gather evidence | generator | human | reject}
```

Name the irreversible act before choosing the error policy. Failure policy is
per action, not per model family:

| Intended action | Error / uncertainty fallback |
|---|---|
| Drop context, evidence, or a retrieved item | Keep it |
| Skip an expensive observation | Perform the observation |
| Rerank a list | Preserve the original order |
| Publish a draft | Hold or send to human, according to product policy |
| Call a mutating tool | Do not execute; require fresh review/authority |
| Auto-route a reversible request | Use a declared default or broader handler |
| Compact or overwrite state | Preserve the original and its recovery key |

“Fail open” and “fail closed” are ambiguous without the action. Say what the
system actually does on timeout, malformed output, missing key, empty candidate
set, low confidence, and stale state.

Evaluate the whole cascade. A high first-stage accuracy can still fail if its
few errors are correlated across a long trajectory or if fallback is too slow.
The later stage sees the residual, often harder population, not the original
traffic. Evaluate/calibrate each route on that selected population and recheck
any conformal assumptions after routing. Where every route can be scored on the
same labeled cases, the per-case best bounds a router's quality gain, not its
cost savings. Compare the learned router with
always-small, always-large, and exact-rule policies; count routing overhead and
record logged selection/propensities when estimating counterfactual route value.
Report:

- end-to-end task success and all-correct trajectory rate;
- coverage and candidate-recall before model selection;
- generator and human-escalation rates;
- p50/p95 latency including retries and fallbacks;
- total expected cost, including review and recovery;
- performance by action severity and distribution-shift slice.

Keep a measurement boundary for each cost and timing claim: stages included,
request granularity, concurrency, hardware, warm/cold state, cache reads/writes,
retries, and missing usage. Reduced context tokens can lose to cache-friendly
unfiltered input. A price from another model is a scenario estimate, not this
model's measured serving cost; API-equivalent prices are not subscription
charges. Unknown usage is not zero. Separate known subtotals from estimates.

For a retrieval filter, pair the same questions and initial candidates, measure
retained evidence recall and final answer quality, and include filtering and
follow-up searches in elapsed time. A reused control or another answer model
on a different question sample is not a fresh matched comparison. The
[decision-model-testing export](https://github.com/dorkitude/decision-model-testing/blob/ba6a5e2e9a60161564ead92a932ccbf3f88e4497/REPRODUCTION.md)
illustrates why code, numeric summaries, and complete replayable run evidence
are separate artifacts. Keep the unfiltered baseline if savings disappear at
the required quality and recall.

## Tool and skill routing

Routing is selection, not permission.

```text
catalog from the host
  → exact eligibility and grants
  → rank or Choice over eligible candidates + explicit none/other
  → code validates arguments and authority
  → host dispatches
```

The candidate catalog must come from live host state, not model memory. If the
catalog can be incomplete, include no-match and measure candidate recall.
Rank-then-verify is often efficient: descriptions create a shortlist, full
bodies or schemas decide fit. Explicit user requests and deterministic matches
should bypass the model.

For capability discovery, [JCR](https://github.com/NiazMorshed2007/jcr) is an
example of classify/search returning documented context without executing it.
The returned command is not a grant. For skill routing, a failed recommender can
degrade to no recommendation; a failed executor gate must withhold execution.

## Dual orchestration (Jev ∩ LLM ∩ MCP)

There are two valid arrangements:

1. **Judgment as a tool inside a generative loop.** The LLM decides when a
   bounded question is useful; code calls the provider and returns the typed
   result. This is flexible but depends on tool recall.
2. **Judgment as the outer controller.** Code asks fixed bounded questions at
   lifecycle points; an LLM is called only for open arguments, prose, or an
   ambiguous remainder. This is easier to measure and replay.

In either arrangement, MCP or another tool protocol is transport. It does not
change the trust boundary. Tool schemas describe possible calls; host policy
decides allowed calls. Do not expose secrets merely so a model can judge whether
using them is safe.

Generator fallback must be explicit:

- why it is invoked (missing candidate, low confidence, unsupported output);
- what state it receives;
- whether it may propose only or also act;
- how its output is validated;
- what happens when it also fails.

Never log fallback output as if it came from the primary decision instrument.

## Preference lint and gates

Split hard rules from soft interpretation.

```text
AST/schema/regex/linter → exact violations
judgment model          → one score or label per written soft rule
policy                  → warn / review / block, with an explicit middle band
```

Do not ask “is this good code?” Ask whether the visible change violates a
specific project rule. Judge only the evidence window named by the rule. Keep
hard correctness, security, build, and test checks in their existing tools.

Shadow the soft gate first. Tune thresholds on independently labeled changes,
not on the same sweep used to select them. A soft score should rarely be the
sole veto for an irreversible action; deterministic failures and accountable
review remain above it.

## Placement gallery

Use these patterns as templates, not endorsements:

- **Context sieve:** score blocks; code keeps errors, recent state, rules, and
  recovery handles. On model failure, preserve evidence.
- **Exact-text selection:** model selects line/span/node identifiers; code copies
  exact bytes. The model never writes the quote or selector.
- **Retrieve → rerank → decide:** retrieval protects recall, ranker orders, an
  independently evaluated decision stage decides whether anything is adequate
  when policy needs it.
- **Observe → choose → act → verify:** host observes and enumerates valid actions,
  model chooses, host executes, post-state verifies. `done` is not proof.
- **Typed decide → policy → generator leftover:** bounded fields drive routing;
  generator writes only the unresolved text.
- **Capability kernel:** secrets and grants remain outside the agent; judgments
  are sensors consumed by policy.

[JevOnly](https://github.com/buluoray/JevOnly) illustrates a closed-vote loop;
[waymode](https://github.com/mossburgh/waymode) illustrates host-owned typed
actions; [Stagehand's experimental integration](https://github.com/browserbase/stagehand/pull/2955)
illustrates pick-and-copy with a generator fallback. These are architectural
examples, not cross-provider benchmarks.

## Design-card extras for mixed systems

```text
Desired behavior and exact baseline:
Evidence source, freshness, and missing-evidence behavior:
Candidate source, coverage test, and none/other behavior:
Judgment family/provider/version:
Exact preprocessing and hard constraints:
Policy owner, thresholds, and per-action error behavior:
Generator role and fallback trigger:
Human role and expected review load:
Authority and state re-check before action:
Outcome oracle after action:
Stage metrics plus trajectory/cascade metrics:
Expected cost: inference + latency + generator + human + recovery:
Smallest experiment that would reject this placement:
```

A model-only scorecard is incomplete. Acceptance belongs to the composed system
under realistic candidates, errors, fallbacks, and trajectories.
