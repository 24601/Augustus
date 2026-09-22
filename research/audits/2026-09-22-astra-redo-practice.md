# Independent redo: practical curation and primary-source QA

Review date: 2026-09-22. Scope: practical guidance and the five requested
source surfaces. This review was independently derived from the mission,
the current files, and newly retrieved primary artifacts. The earlier refresh
report supplied source leads, not accepted conclusions.

Requested worker identity: `gpt-6-astra`, `xhigh`. The parent assignment and
GPT-6 role instructions are observable; this worker has no independent
backend model/build attestation. The live agent listing exposes names and
status, not model identity. No GPT-5.6 output is adopted as this review's proof.

## Verdict

**Fix-first, scoped to practical guidance.** The September 22 additions about
aggregation semantics, media coverage, complete-workflow accounting, finite
support, and injection controls are useful and supported. Retain them. Three
older recommendations in FAQ/optimizer guidance overconstrain family choice
or overstate what one number means; correct them before treating the practical
set as fully integrated. No architectural rethink or new provider is warranted.
The coordinator owns the complete acceptance decision.

### Required corrections

1. **Distribution consumption does not require specialist training.**
   `optimizer-integration.md` under “Specialist as metric vs few-shot as
   classifier” and `faq.md` under “Train a specialist…” steer hosted APIs
   toward winner-only use and specialist training toward distribution use.
   This conflicts with the class/validation guidance. Either hosted or local
   predictions can support expected loss if their semantics and calibration
   are adequate; either can fail. Replace the distinction with evidence,
   privacy, latency, operating cost, stability of the task, label availability,
   and measured quality of the policy-consumed distribution. Retain independent
   gold and runtime validation. Counterexample: a sufficiently calibrated
   hosted distribution beats a poorly calibrated local specialist on the same
   frozen policy. Falsifier: a held-out expected-loss comparison should be
   allowed to retain the hosted provider in that case.
2. **RAG need not acquire another decision model.** `faq.md` under “Should RAG
   stop at Top-K / a reranker?” permits this only when ranking is the product,
   then prescribes an absolute judgment or human step. A retrieved shortlist
   can feed an answerer directly if the measured baseline meets its evidence,
   quality, and cost requirements. Add an absolute accept/no-match gate when
   a particular action requires it and its benefit is demonstrated. Calibrating
   an existing score is also possible; a new model is not mandatory.
   Counterexample: rerank-to-answer already meets its target and a filter
   drops necessary context. The gate must lose the comparison and be omitted.
3. **Noul 0.5 identifies an equal binary assignment, not its cause.** The FAQ
   calls it “maximum uncertainty.” That is defensible as Bernoulli entropy,
   but is inadequate practical diagnosis and weaker than the entry point's
   existing distinction. State that yes/no receive equal probability; it is
   not intensity and does not distinguish missing evidence, conflicting
   evidence, population randomness, or model failure. A known fair coin and
   an unread case may both yield 0.5 but call for different information work.
   The [official Noul definition](https://docs.typesafe.ai/primitives/noul)
   supports the equal-probability reading, not a diagnosis of missing knowledge.

### Additional refinements worth making

- The FAQ's final acceptance sentence asks the model to beat a baseline on
  quality, latency, **and** cost. Use the user's prespecified utility and hard
  constraints; useful deployments often exchange latency or cost for quality.
  Pareto dominance is welcome but not a universal prerequisite.
- `boundary-audit.md` correctly rejects vacuous specifications, but “Demand a
  subtle property (concurrency, liveness, multi-step)” is too narrow. Demand a
  meaningful property capable of failing on a plausible bad implementation.
  A simple wrong-account transfer invariant can matter more than a subtle
  concurrency theorem. Formal-methods acceptance remains outside this audit.
- Its fit test and opportunity-card primitive list remain more software/Jev
  specific than the stated domain-general mission. A repeatable human decision
  process is a valid consumer; Choice/Score/Noul are examples alongside ranks,
  spans, and ordinary human rubrics. No new reference is needed for this repair.

## Practical reference disposition

All nine assigned references were read in full. Each was assessed for a useful
placement, baseline, evidence boundary, explicit policy, failure behavior, and
a result that could reject the placement.

| Reference | Independent judgment |
| --- | --- |
| `judgment-class.md` | Retain. Families are separated by task/objective, not hosting or compatible JSON. Coverage, causal identification, runtime limits, and media-window cautions prevent important category mistakes. |
| `question-design.md` | Retain. Referent identity, no-match/missing/conflicting outcomes, exact preflight, ordinal semantics, and wrapper semantics are actionable. One coherent proposition may include an interaction; atomicity must not imply statistical independence. |
| `mixed-architecture.md` | Retain. Exact authority and execution remain separate from judgments; the residual routed population and complete cost boundary are essential. A gate remains optional when the baseline suffices. |
| `validation.md` | Retain. Splits, route/slice evaluation, proper scores, finite support, paired comparisons, and label-preserving attack controls are substantially correct. No certification implementation is claimed. |
| `boundary-audit.md` | Useful insertion recipe; refine the narrow fit-test and “subtle property” wording above. Some inherited named-tool examples are less task-focused than the newer cards. |
| `applied-mappings.md` | Retain. The nine placements supply concrete evidence, fallback, authority, and outcome checks. Pointer selection and reversible evidence hiding are especially useful. These are hypotheses/templates, not demonstrated universal gains. |
| `optimizer-integration.md` | Fix the hosted-versus-specialist distribution rule. Executor versus metric separation, independent labels, and confirmation outside optimization are otherwise useful. |
| `agent-self-assessment.md` | Retain. Completion joins claims to observed state and traces; supervision cannot waive exact checks. Full-trajectory evaluation and action-specific fallbacks correctly bound the supervisor. |
| `faq.md` | Fix the three contradictions and soften the all-dimensions-win criterion. Its short answers otherwise route users to the appropriate detailed reference. |

The current set is far more useful than a catalog of projects: it yields a
reviewable placement and experiment. Its success is not established by this
inspection alone. Fresh scenario responses and coordinator review remain
required for behavioral acceptance.

## Requested-source verification

Primary retrievals in this worker occurred on 2026-09-22, with a recorded
review checkpoint at 16:18:24Z; the Jevusers API response itself records
2026-09-22T16:15:40.280Z. GitHub and Hub
live-head reads matched the pinned revisions below. Exact per-fetch timestamps
were not persisted. No inference, weight download, third-party execution,
paid search, private receipt access, or external mutation occurred.

### TypeLLM/pijev

Canonical revision: `bca3a73d6419b794d63cd780ba4a0254579d7ccc`, also the live
`main` returned by GitHub during this review. Read the entire
[implementation](https://github.com/TypeLLM/pijev/blob/bca3a73d6419b794d63cd780ba4a0254579d7ccc/pijev/__init__.py),
[README](https://github.com/TypeLLM/pijev/blob/bca3a73d6419b794d63cd780ba4a0254579d7ccc/README.md),
and [mock-transport tests](https://github.com/TypeLLM/pijev/blob/bca3a73d6419b794d63cd780ba4a0254579d7ccc/tests/test_symmetry.py).

**Contract from code:** sorted semantic labels, distinct sampled orders,
per-label normalization/mean, finite/support/mass validation, stable tie choice,
and non-Choice passthrough are explicit. Choice `confidence` becomes the winning
mean probability. The same batch retains Score's native confidence, so one
field name can have different semantics within a mixed response. Default eight
orders and the 720-question client cap do not replace provider token limits.

**Mathematical result:** Jensen bounds ensemble convex loss by mean member
loss; it does not bound it by the best member. For true-label probabilities
0.8 and 0.4, the 0.6 mean has log loss 0.510825624, versus best 0.223143551
and member mean 0.569717142. Two-class Brier values are 0.32, 0.08, and 0.40.
These numbers were independently computed with Node arithmetic. Correlation
does not invalidate Jensen; it invalidates treating members as independent
evidence. Neither Jensen nor the mock tests demonstrates calibration or lower
action loss. The README's “Guaranteed Better Calibration” heading remains
stronger than its qualified body. **Disposition:** keep the current bounded
aggregation/score-contract guidance; no universal improvement claim.

### akhilaaa3/Jev-Omni and DecisionBench

Canonical revision: `55b53f2ec1b4c656c8a6172b0c7555ae578a9c3f`, also the live
Hub SHA. Read the pinned
[card](https://huggingface.co/akhilaaa3/Jev-Omni/blob/55b53f2ec1b4c656c8a6172b0c7555ae578a9c3f/README.md),
[multimodal loader](https://huggingface.co/akhilaaa3/Jev-Omni/blob/55b53f2ec1b4c656c8a6172b0c7555ae578a9c3f/jev_omni.py),
[text loader](https://huggingface.co/akhilaaa3/Jev-Omni/blob/55b53f2ec1b4c656c8a6172b0c7555ae578a9c3f/load_model.py),
[config](https://huggingface.co/akhilaaa3/Jev-Omni/blob/55b53f2ec1b4c656c8a6172b0c7555ae578a9c3f/decision_config.json),
and [verification](https://huggingface.co/akhilaaa3/Jev-Omni/blob/55b53f2ec1b4c656c8a6172b0c7555ae578a9c3f/verification.json).

**Code-level limits:** audio is mono 16 kHz and clipped to 30 seconds; video
uses 16 sampled frames by default and is submitted as images, without the
video audio track. The public multimodal loader requires CUDA, separately
downloads the base components, converts linear weights to BF16, and runs
autocast. Its download calls do not pin revisions. The multimodal API accepts
2–256 options, whereas the separate text helper permits 1–256. Duplicate option
strings would collapse keys in the returned probability dictionary; preflight
should enforce unique stable options. None of this establishes model quality.

**Reported, not reproduced:** the card's accuracy/ECE and warm H200 timings;
the stated strongest option-count support is at most 20. Its 12-example
verification separates approximate merge probability differences (about 0.201)
from the FP32 comparison (about 0.000034); argmax agreement is insufficient for
threshold-policy parity. The 30,000-question card description and 24,000 final
recipe are distinct scopes with incomplete training provenance.

The [DecisionBench card](https://huggingface.co/datasets/akhilaaa3/decision-bench/blob/19334fec40b54b693a63e1ffd91636651d39e847/README.md)
at `19334fec40b54b693a63e1ffd91636651d39e847` describes synthetic labels,
80 scenarios/293 questions per subset, macro accuracy, question-weighted ECE,
exclusion of missing/refused answers, and **last-attempt-only retry cost**.
Jev-Omni's serving price is a Gemma 3 12B input-token proxy. Its requirement
that both classifiers resend state for every question conflicts with the
[official Jev model contract](https://docs.typesafe.ai/models), which documents
shared state and many parallel questions. The benchmark may report its chosen
request shape, but cannot establish that batching is unavailable or that the
chosen shape is each system's cheapest supported operation. **Disposition:**
retain the media and accounting additions; archive these extra caveats.

Falsifier: an inspection with a decisive unsampled visual event or an audio-only
event must not receive whole-video sign-off. Cost acceptance needs supported
batching, all attempts, missing-response rates, actual hardware/usage, complete
latency, and an explicit quality target. No such experiment ran here.

### dorkitude/decision-model-testing

Canonical revision: `ba6a5e2e9a60161564ead92a932ccbf3f88e4497`, also live `main`.
Read the root README, all four experiment READMEs,
[reproduction boundary](https://github.com/dorkitude/decision-model-testing/blob/ba6a5e2e9a60161564ead92a932ccbf3f88e4497/REPRODUCTION.md),
the complete recursive file inventory, both RAG summary projections,
[cascade projection](https://github.com/dorkitude/decision-model-testing/blob/ba6a5e2e9a60161564ead92a932ccbf3f88e4497/experiments/jev-vs-LLM-for-evals/results/cascade-evaluation-v1/cascades.json),
and [statistical aggregation source](https://github.com/dorkitude/decision-model-testing/blob/ba6a5e2e9a60161564ead92a932ccbf3f88e4497/experiments/jev-vs-LLM-for-evals/internal/study/statistics.go).

**Reported numeric projections:** Kimi retains 307/2,020 chunks and has
98/100 DeepSeek acceptance in each arm. Claude categorical has 96/100 in each
arm, one baseline-only and one filtered-only success, and a source-document
cluster bootstrap interval of −3 to +3 points. Neither equality nor the Kimi
zero-width empirical difference interval establishes population equivalence.
The 513-unit Jev→GPT-OSS simulation has strict scores 0.801169591 versus
0.764132554 and cost ratio 0.563083171. LLMBar→Qwen loses 0.035228172.
The projection preserves 24 unknown-cost attempts and a null total-cost
estimate; source code gives invalid required stages zero strict score and
retains benchmark-specific aggregation. These are not local reproductions.

The public export excludes source-bearing historical receipts and skips their
tests. Hashes on derived projections identify private originals but cannot
reconstruct them. Fresh RAG work requires a private dense index, credentials,
and paid services. [Kimi timing](https://github.com/dorkitude/decision-model-testing/blob/ba6a5e2e9a60161564ead92a932ccbf3f88e4497/experiments/jev-search-result-narrower/README.md)
starts at the first answer-model request; initial retrieval/filtering are
excluded. [Claude comparison](https://github.com/dorkitude/decision-model-testing/blob/ba6a5e2e9a60161564ead92a932ccbf3f88e4497/experiments/jev-search-result-narrower-claude-RAG/README.md)
reuses inspected historical controls and uses API-equivalent cost rather than
incremental subscription charges. **Disposition:** retain complete-workflow,
paired-comparison, private/public-evidence, and unknown-usage distinctions.

### Jevusers main and apps

Read [main](https://jevusers.com/), [apps](https://jevusers.com/apps),
[methodology](https://jevusers.com/about), and the linked
[JSON API](https://jevusers.com/api/projects) directly. Fresh JSON contains
400 project records. Parsing the actual HTML with Python's standard
`HTMLParser` counts 1,299 `li` elements with class `app`; this is structured
directory traversal, not code review. Augustus is present once among app
links and in the API. Its API summary still says “dominant exemplar,” so the
directory has not yet reflected the source project's preferred wording.

The directory ranks by stars and discovers through repository metadata/README
queries; the app list aggregates 31 curated lists. Repeated inclusion is
correlated discovery evidence. Neither listing count nor inclusion establishes
independent quality, deployment, adoption, or a new model family.
**Disposition:** discovery/archive only. Do not submit a duplicate listing or
silently treat directory prose as current product authority.

## Supporting controls and domain-general theory

The [official confidence page](https://docs.typesafe.ai/confidence) describes a
distribution-derived statistic, distinct from maximum option probability. Its
interactive explorer labels its displayed formula an approximation; do not
promote that demo into an exact backend formula. The official model page
documents text-only hosted Jev, shared-state batching, token budgets, and
input-token billing. These are interface contracts; calibration and performance
prose still requires population-specific measurement.

[Decision Injection Bench](https://github.com/cwhy/decision-injection-bench/blob/f566360ffac91bfc50574aef722307dcbf51d5e1/README.md),
`f566360ffac91bfc50574aef722307dcbf51d5e1`: README inspection confirms clean and
length-matched controls, unequal eligible denominators, public authored cases,
and label-changing adaptive attacks being treated as unvalidated diagnostics.
Repeated calls do not enlarge independent case support. This supports the
validation addition, not a robustness ranking or safety certificate.

[willkelly/jev-evaluation](https://github.com/willkelly/jev-evaluation/blob/d80f375621ad4b9306c6dff6941242925d7e2386/README.md),
`d80f375621ad4b9306c6dff6941242925d7e2386`: README inspection supports the
referent-resolution lead and solver/construction label claim. Raw logs were
not fetched or replayed. Its broad statements that batching is free and the
endpoint limits only tokens should remain attributed observations; current
official docs also list a request-rate limit. Do not turn that experiment's
envelope into the live contract.

Primary identity/objective checks support the practical family map:
[GLiNER](https://arxiv.org/abs/2311.08526v1) extracts entities/spans;
[GLiClass](https://arxiv.org/abs/2508.07662v1) addresses sequence/multi-label
classification; [DF²](https://proceedings.mlr.press/v286/kong25a.html) concerns
decision-focused learning; [TabPFN](https://github.com/PriorLabs/TabPFN) exposes
tabular classification/regression and explicitly separates code from weight
licenses. These were abstract/official-README checks, not evaluations or code
audits. Retain simple supervised, exact, human, ranking, and extraction choices.
No new family is established merely by a new port or multimodal loader.

The recent papers warrant the current narrow treatment:

- [Available Guardrails, v1](https://arxiv.org/pdf/2609.22048v1), submitted
  September 18: inspected abstract and methods §§3.1–3.4. Its fixed IID
  certification sample and simultaneous reporting units support planning
  accepted-case support. The dynamic program optimizes contiguous partitions
  of a fixed ordering and an approximate planning objective, not unrestricted
  realized coverage. Independently computed zero-error values are
  `1-0.05^(1/20)=0.1391083407`, `ceil(log(.05)/log(.99))=299`, and
  `ceil(log(.05/41)/log(.99))=668`. The last is a Bonferroni minimum per unit
  with zero errors, not a promise of obtaining zero errors or enough accepts.
  Retain the classical support rule; keep the optimizer in research.
- [Strategic Decision Focused Learning, v1](https://arxiv.org/html/2609.14907v1),
  September 14: inspected formulation, strategic-response assumptions, and
  propositions. Exogenous states, informed opponents, and equilibrium response
  matter to its non-monotonic examples. It is a reason to measure strategic
  utility in a matching application, not a general reason to degrade prediction
  accuracy. No new runtime recipe is justified by these existence results.
- [Drift-Aware LLM Routing, v1](https://arxiv.org/html/2609.00662v1), September 1:
  inspected architecture, hard meter, assumptions, and synthetic evaluation.
  Learned estimates and exact budget enforcement remain separate. The reported
  4,800-request synthetic study and prospective real-data protocol do not
  establish production routing quality. Audit feedback has a real budget.
  Keep as a research candidate; existing routing/shift guidance covers its
  immediate design lesson.

## Evidence depth, checks, and limits

Read `AGENTS.md`, `CONTRIBUTING.md`, `research/protocol.md`, the fold prompt,
the entire current Augustus entry point, all nine assigned references, and
the aggregation subsection of composition algebra. Inspected the complete
practical-reference delta from published `192faf0d18d511154228af8ac40e1393567d828c`.
The supplied before-session baseline `0b43a8d3b8d2d389b59415747f566dcbaa3f3ec8`
has a very large historical rewrite; its full diff was not consumed here.
This verdict is based on freshly reading the resulting references, not on
accepting the previous curation report or claiming every removed line reviewed.

Only this audit file was authored by this worker. It makes no runtime edits.
The workspace is shared and already dirty, so later coordinator edits may
supersede the observed file hashes. At 16:18:24Z the SHA-256 values were:

```text
judgment-class.md       a0b720796d1ef85bf5b78c7c7c8b1f9f98c841876611b5abf390b397314c3eb7
question-design.md      2832a7f144bfb8b771e76e214796bb1492e766d99e656d9e3c0d6b7c672a01c5
mixed-architecture.md   7da9838ae6ae0c099687086b41f497558b5613eddc351c7e9b1207f4284d9b20
validation.md           1fb88915573b34ed2f72d903c040ee2fff9829df3dcb26b6abb3658f6380fbd0
boundary-audit.md       0373c79a02e1bea3b1cb04b7f0bc923d7548c5626a66616305956e7998a8973b
applied-mappings.md     ec1fa626a6647cd80f1901f4fc7fb177f02edd9ecb9d51574f0bc8cc0a527a1e
optimizer-integration.md a9c7334ce7e09c49779bac3bdc94361c4a8e8d09f8e8792965103f9bec1b1243
agent-self-assessment.md ea1e310ffb9bf914991093adf48aed3c883bf8aa78319beae669874a8e9ff21a
faq.md                  9a19e1d16236882bec9a24bdcf5369e8690e1653a419a24e55c8df14ca5197d7
```

Arithmetic ran directly in Node without imported research code. Primary
artifacts were read through public HTTP and the web reader. The Hub web reader
failed, then direct public raw HTTP succeeded. A guessed Noul document path
and test filename returned 404; documented `/primitives/noul` and the repository
tree resolved them. Available Guardrails HTML was unavailable; primary PDF
text provided the methods. These retrieval failures do not imply absent models
or unsupported capabilities.

Still unverified: any provider behavior, local model inference, data rights
outside documented claims, all benchmark raw labels/receipts, real calibration,
invoice costs, live performance, complete code/security of external projects,
and the papers' full proofs/implementations. Most architectural-example repos
in the inherited references were not freshly re-audited; no new correctness or
freshness claim is made for them. No all-ecosystem census or exhaustive
literature search is claimed by this scoped redo. Behavioral execution and
final integrated acceptance belong to the coordinator's separate work.

`make check` passed after writing this artifact: repository structural checks,
53 unit tests, both numerical self-tests, and shell syntax. `git diff --check`
also passed. These checks do not resolve the practical findings or certify
semantic quality. The final edit records this result and clarifies the retrieval
timestamp; it changes no tested behavior.
