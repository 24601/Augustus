# Independent behavior follow-up — 2026-09-22

Agent: `/root/final_behavior`, fresh context. Coordinator requested
`gpt-5.6-sol`, high effort; realized runtime settings and token usage were
not exposed. The agent read the current skill and relevant references,
not the scenario expectations, prior responses, or audit reports. These
are actual agent responses, not hosted decision-model inference or an
implicit host-activation benchmark. No files were edited by the answering
agent. The coordinator recorded the returned answers below.

## 1. Reranker score 0.92

**Prompt:** Our passage reranker emits a score of 0.92. Can we treat that as
92 percent probability a claim is true and publish automatically?

**Answer:** No. Treat `0.92` as a model-specific ranking signal unless the
provider explicitly defines otherwise. A reranker optimizes relative
ordering; its score is not automatically `P(claim is true)`, and relevance
is not truth or publication authority.

Keep it for passage ordering. If automatic publication is desired, add a
separately evaluated claim-verification decision, define the exact event
being predicted, calibrate it on deployment-like held-out data, and let
explicit policy control publication. On malformed output, stale evidence,
or uncertainty, hold for review. Reject automation if false publication
exceeds the risk budget or the complete workflow does not beat the current
review baseline.

## 2. Alloy model plus “looks safe” judgment

**Prompt:** We wrote an Alloy model of access control and a decision model
says it looks safe. Can we skip exploring counterexamples and use that as
our security acceptance?

**Answer:** No. The decision model's output is a triage sensor, not a
security proof or checker result. Run Alloy's actual counterexample search
and report the exact model, property, tool version, finite scope,
configuration, and result. Even “no counterexample in this scope” is not an
unbounded proof.

Security acceptance should also include non-vacuity or mutation checks,
scrutiny of the model-to-implementation correspondence, and applicable
tests/runtime enforcement. A decision model may rank suspicious properties
or counterexamples for human attention. A seeded countermodel that the
property fails to catch, an omitted security mechanism, or an Alloy
counterexample falsifies the acceptance.

## 3. Local decoder agreeing on 95/100 examples

**Prompt:** A local constrained decoder has the same JSON API as Jev and
agrees on 95 of 100 examples, twice as fast. Is it a drop-in replacement for
our approval queue?

**Answer:** Not yet. JSON wire compatibility, 95% agreement with Jev, and
higher speed do not establish semantic equivalence or safe substitution.
Jev agreement is not ground truth, and the five disagreements could be
concentrated around the approval boundary or highest-cost cases.

Requalify the local decoder against independently labeled, representative
approval-queue cases. Pin model, rubric, labels, calibration, threshold,
policy, and runtime environment. Measure calibration or proper scores
where probabilities are consumed, false approvals and false rejections,
selective coverage, subgroup/OOD behavior, malformed outputs/timeouts,
review load, and end-to-end latency and cost. Use a prespecified
noninferiority margin and shadow the replacement before granting
authority. On uncertainty or failure, preserve the existing queue/review
path. It becomes drop-in only if the composed approval policy meets the
same acceptance envelope, not because the API matches.

## 4. Repository revisit with calibration retraction

**Prompt:** A repo we catalogued has 200 more stars, a new SHA, and an updated
README that retracts a calibration result. How should Augustus absorb this
update?

**Answer:** Treat the new SHA as a review trigger, the extra stars as
archive-only popularity evidence, and the calibration retraction as
material evidence.

Resolve the canonical repository identity, locate its existing source
card, inspect the actual revision diff and primary retraction artifact,
and record revision plus retrieval time. Preserve the original dated
claim and append the dated correction/retraction; do not silently
overwrite history. Keep the retraction **Reported** unless independently
reproduced, and distinguish it from interface **Contract** evidence.

Then ask which Augustus design decision changes. If prior guidance relied
on that calibration result, withdraw or narrow the single relevant
calibration/provider rule, state its new scope and evidence status, and
add a falsifier. If no design decision changes, update the research
archive only and stop—no runtime guidance edit. The stars should not
influence family selection or promotion.

## Usability findings returned by the agent

The skill gave actionable boundaries for ranking versus probability,
judgment versus formal checking, wire compatibility versus semantic
substitution, and revision signals versus material evidence. Replacement
qualification required synthesis across judgment-class, validation, and
mixed-architecture references. Universal thresholds, noninferiority
margins, and security acceptance levels remained organization-specific.

The agent initially resolved skill-relative links from the repository root,
then corrected to `.agents/skills/augustus/`. The coordinator retained
standard skill-relative links: installed skills must remain portable.
The final entry point now explicitly names that reference-path convention.
