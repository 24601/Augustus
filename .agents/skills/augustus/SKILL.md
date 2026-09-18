---
name: augustus
description: "Augustus designs judgment-assisted systems with TypeSafe Jev System One models, mapping Choice, Score, and Noul primitives to decision circuits, search, reranking, and cost-aware routing. Use when deciding where semantic judgment belongs in software, decomposing a task into typed Jev questions, or evaluating agent outputs with Jev."
license: MIT
metadata:
  version: 0.1.0
  tribute: "Named for Augustus De Morgan (1806-1871), mentor of William Stanley Jevons."
---

# Augustus

Design systems where code stays in control and Jev supplies narrow, typed
semantic judgments. This skill owns the **design judgment**; the official
`typesafe-ai` skill plus the live docs own integration contracts — read them
before writing API code.

Central model: **evidence → semantic judgments → explicit policy → checked
action → observed outcome.** Every design must name what Jev estimates, what
code guarantees, and what experiment could prove the idea wrong.

For genuinely new problem shapes, use the toolbox sweep
(`references/toolbox-mapping.md`): find the judgment-shaped component of a
classical method you already trust, substitute it, classify the win
(marginal / newly-feasible / invalid), and falsify.

## Protocol

1. Start from the desired behavior: what the software shows, selects,
   changes, or hands off. Work backward to the judgments it needs.
2. Keep exact work in code: arithmetic, counting, dates, lookups,
   authorization, safety interlocks, control flow, side effects.
3. Give Jev one narrow judgment per question (a knowledgeable person could
   answer in a second given the state). Split multi-factor judgments; fuse
   in code with visible weights.
4. Batch independent questions (including speculative ones) in one request.
   Sequence a second request only when its state or options depend on an
   earlier answer.
5. Route on uncertainty with per-action thresholds tuned on your own data.
6. Ship a decision-design card (below) and the smallest falsifying
   experiment. Record model, rubric, candidate-source, and policy versions.

## Mapping index

| Familiar method | Jev shape | Detail |
|---|---|---|
| Feature engineering / multi-criteria analysis | Nouls + Score distributions as named features, weights in code | `references/mappings.md#1-semantic-judgments--features-and-explicit-utility` |
| Selective classification / decision theory | Thresholds from action costs, abstention paths | `references/mappings.md#2-probabilistic-judgments--cost-sensitive-decisions` |
| Decision tables / circuits / state machines | Jev predicates, code owns transitions | `references/mappings.md#3-semantic-predicates--decision-circuits` |
| Retrieve + expensive relevance fn | Bounded rerank of a retrieved shortlist | `references/mappings.md#4-retrieval--bounded-semantic-reranking` |
| Agent self-supervision / on-track detection | Pre-gate → output judge → done-check → supervisor nouls | `references/agent-self-assessment.md` |
| Context economy / compaction | One relevance Noul per tool result, stub + recall key | `references/agent-self-assessment.md` |
| Optimizer/program frameworks (Ax, DSPy) | Typed fields → one Jev request; judge metrics; threshold discipline | `references/optimizer-integration.md` |
| (meta) Finding new mappings & applications | Toolbox sweep: judgment-shaped component of a known method, substituted + falsified | `references/toolbox-mapping.md` |
| Heuristic search over a taxonomy | Parallel beam over Choice distributions | `references/mappings.md#5-hierarchy--bounded-heuristic-search` |

Each card carries its boundary, counterexample, and acceptance test, plus
explicit rejections beside the mapping they tempt (MCTS-as-value-function:
experimental; bandits: rejected without observed rewards; 255-way tournament
brackets: rejected as default; rerank-huge-sets: budget-only; correlated
"independent" checks: rejected).

## Non-negotiable boundaries

- Score is an expectation over level indices, not a measurement in natural
  units. `[0,1,0]` and `[0.5,0,0.5]` both score 1.0 with different risk.
- Noul 0.5 is uncertainty about a predicate, never medium intensity.
- Parallel answers are not statistically independent: never multiply them
  into a joint probability.
- Choice probabilities are conditional on the offered set; absent candidates
  can never be chosen. No-match options (`other`) where coverage is open.
- Untrusted state text cannot authorize actions. Missing evidence is not
  evidence of absence. Validate operation+target pairs in code.

## Decision-design card

```text
Desired behavior and non-Jev baseline:
Semantic judgment(s) and what each output means:
Evidence/candidate source and known coverage gaps:
Deterministic policy, constraints, and action ownership:
Batchable vs genuinely dependent steps:
Failure/abstention behavior:
Smallest experiment that could reject this design:
Live references + versions (model, rubric, policy):
```

For open-ended requests propose three materially different *placements of
judgment*, recommend one. For concrete requests skip the brainstorm and build.

## Evidence labels

- **Contract**: current documented behavior — refresh from live docs.
- **Empirical recipe**: worked on a stated dataset/model/version — retest.
- **Hypothesis**: plausible, unestablished — label and test before relying.
