---
name: augustus
description: "Use when deciding where semantic judgment belongs versus generation or exact code; designing mixed architecture (typed decision/classification model + LLM writing); replacing prompt-to-JSON classifiers, brittle parsers, or unbounded agent loops that are really bounded judgments; planning context sieves, exact-text keep/drop, env triage, moderation/ranking, tool/skill routing, cost-sensitive prefilters, or AGENTS.md preference lint; answering \"Jev is just classification\" with a placement not a stack replacement; decomposing a task into typed Choice, Score, or Noul questions; or evaluating agent outputs with Jev. Not a substitute for the official typesafe-ai skill (live API contracts)."
license: MIT
metadata:
  version: 0.3.0
  typesafe_skill: v0.5.7
  typesafe_skill_commit: 65a39f3
  tribute: "Named for Augustus De Morgan (1806-1871), mentor of William Stanley Jevons."
---

# Augustus

Design systems where code stays in control and Jev supplies narrow, typed
semantic judgments. This skill owns the **design judgment**; the official
`typesafe-ai` skill plus the live docs own integration contracts — read them
before writing API code. Neighbor skills `tenbin` (lint/measure) and
`decision-first` (try-Jev-first habit) own their jobs; do not collapse into
another Jev how-to. Mappings stay backend-agnostic: the *typed judgment
provider* is TypeSafe Jev by default; an open Choice/Score/Noul head is a
substitute you must self-eval, not a second how-to (`research/notes.md` §18).

Central model: **evidence → semantic judgments → explicit policy → checked
action → observed outcome.** Default placement is **mixed architecture**
(decision model + generator + code), not stack replacement. Every design
must name what Jev estimates, what the LLM is still for, what code
guarantees, and what experiment could prove the idea wrong.

For genuinely new problem shapes, use the toolbox sweep
(`references/toolbox-mapping.md`): find the judgment-shaped component of a
classical method you already trust, substitute it, classify the win
(marginal / newly-feasible / invalid), and falsify.

## Protocol

1. If the request is "replace the LLM/stack with Jev" or "isn't this just
   classification?": read `references/faq.md` then
   `references/mixed-architecture.md` before any mapping. Answer with a
   placement (sieve / keep-drop / triage / rank / route / gate / replace-
   one-classifier-step), not a rewrite. If it is an existing system, PR,
   or running workflow: also run the boundary audit
   (`references/boundary-audit.md`). Classify each step as exact / bounded
   judgment / generation; recommend the smallest insertion, not a redesign.
   Greenfield with no replacement framing: start at step 2.
2. Start from the desired behavior: what the software shows, selects,
   changes, or hands off. Work backward to the judgments it needs.
3. Keep exact work in code: arithmetic, counting, dates, lookups,
   authorization, safety interlocks, control flow, side effects. Keep
   open-ended writing, explanation, and code generation on a generative
   model; Jev may gate, route, or verify around that call.
4. Give Jev one narrow judgment per question (a knowledgeable person could
   answer in a second given the state). Split multi-factor judgments; fuse
   in code with visible weights.
5. Batch independent questions (including speculative ones) in one request.
   Sequence a second request only when its state or options depend on an
   earlier answer.
6. Route on uncertainty with per-action thresholds tuned on your own data.
   The same judgment can authorize a reversible path and must not authorize
   an irreversible one.
7. Ship a decision-design card (below) and the smallest falsifying
   experiment. Record model, rubric, candidate-source, and policy versions.
   Keep questions, criteria, and thresholds in one reviewable module; store
   raw judgments separately from derived actions.

## Mapping index

| Familiar method | Judgment shape | Detail |
|---|---|---|
| Mixed architecture (decision model + LLM) | Provider judges, LLM writes, code owns control; not a stack replacement | `references/mixed-architecture.md` |
| Context sieve | Relevance Noul per block; always-keep set in code; stub + recall key | `references/applied-mappings.md#1-context-sieve` |
| Exact-text keep / drop | Choice include/exclude/mixed over candidates code already holds | `references/applied-mappings.md#2-exact-text-keep--drop` |
| Environment / harness triage | Scan every step for env failure; LLM autopsy only on flags | `references/applied-mappings.md#3-environment--harness-triage` |
| Moderation and ranking | Hold-before-publish vs graded rerank; fail policy per action | `references/applied-mappings.md#4-moderation-and-ranking` |
| Skill / tool routing | Choice over a closed catalog + whether-anything-fits; code dispatches | `references/applied-mappings.md#5-skill--tool-routing` |
| Agent preference lint / semantic gates | Project-defined rules as criteria; provider classifies evidence; code maps outcome | `references/mixed-architecture.md#preference-lint-and-gates` |
| "It's just classification" / stack-replacement FAQ | Typed judgment is a software primitive, not a new task | `references/faq.md` |
| Feature engineering / multi-criteria analysis | Nouls + Score distributions as named features, weights in code | `references/mappings.md#1-semantic-judgments--features-and-explicit-utility` |
| Selective classification / decision theory | Thresholds from action costs, abstention paths | `references/mappings.md#2-probabilistic-judgments--cost-sensitive-decisions` |
| Decision tables / circuits / state machines | Jev predicates, code owns transitions | `references/mappings.md#3-semantic-predicates--decision-circuits` |
| Retrieve + expensive relevance fn | Bounded rerank of a retrieved shortlist | `references/mappings.md#4-retrieval--bounded-semantic-reranking` (independent TREC DL2019 benchmark: Jev zero-shot best MAP 0.4748, nDCG@10 0.683 vs tuned monoBERT 0.718 — competitive, not dominant) |
| Agent self-supervision / on-track detection | Pre-gate → output judge → done-check → supervisor nouls | `references/agent-self-assessment.md` |
| Optimizer/program frameworks (Ax, DSPy) | Typed fields → one Jev request; judge metrics; threshold discipline | `references/optimizer-integration.md` |
| (meta) Finding new mappings & applications | Toolbox sweep: judgment-shaped component of a known method, substituted + falsified | `references/toolbox-mapping.md` |
| Named methods / operators / theorems | Substitution tiers: operand-judgments, preconditioned theorems, non-substitutable | `references/methods-catalog.md` |
| (meta) Where Jev sits relative to any construct | 11 positions + logical-operator rules + position×construct traversal as the application generator | `references/composition-algebra.md` |
| Question mechanics & debugging | Instruction/criteria/state shape, budgets, diagnosis table, revision discipline | `references/question-design.md` |
| Heuristic search over a taxonomy | Parallel beam over Choice distributions | `references/mappings.md#5-hierarchy--bounded-heuristic-search` |
| Existing-system insertion / code-smell audit | Opportunity map, fit test, smallest boundary, policy centralization | `references/boundary-audit.md` |

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
- Classification is not the product. The claim is a software primitive:
  typed, calibrated, batched, schema-valid judgments that code can
  threshold — placed beside generation, not instead of it. Regexes that
  already work stay; trained classical classifiers still win on stable
  labeled taxonomies; open-ended writing stays on an LLM. Full answer:
  `references/faq.md`.

## Decision-design card

```text
Desired behavior and non-Jev baseline:
Semantic judgment(s) and what each output means:
Evidence/candidate source and known coverage gaps:
Deterministic policy, constraints, and action ownership:
Batchable vs genuinely dependent steps:
Failure/abstention behavior:
Smallest experiment that could reject this design:
Typed judgment provider (TypeSafe Jev default; open head only with self-eval):
Live references + versions (model, rubric, policy):
```

For open-ended requests propose three materially different *placements of
judgment*, recommend one. For mixed-architecture requests also fill the
extras on `references/mixed-architecture.md` (what the LLM is still for,
cascade costs, fail-open vs fail-closed). Applied placements (sieve,
keep/drop, env triage, moderation/ranking, skill routing):
`references/applied-mappings.md`. For concrete requests skip the
brainstorm and build.

## Evidence labels

- **Contract**: current documented behavior — refresh from live docs.
- **Empirical recipe**: worked on a stated dataset/model/version — retest.
- **Hypothesis**: plausible, unestablished — label and test before relying.
