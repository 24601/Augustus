# Research that improves the skill

The objective is better decision design. A growing source count is not a
quality metric. Study methods as well as products: decision theory,
selective prediction, calibration, conformal methods, causal effects,
decision-focused learning, extraction, routing, optimization, and human
decision processes. Vendor discovery alone cannot cover this mission.

Synthesize mechanisms rather than the median opinion of a catalog. Explain why
an approach worked or failed and under which conditions a combination should
help. Cross-field imports need an explicit mapping of variables, units, objective,
observation process and theorem assumptions; attractive analogies stay hypotheses.
Promotions should equip an agent to find, implement, evaluate or improve a decision
program. Separate a valid derivation, an executed fixture, reported benchmark and
observed deployment outcome. Neither a theorem about assumed inputs nor a rising
optimizer proxy score establishes product benefit.

## Source and claim identity

Use the canonical owner/repository, model-card ID, paper DOI/arXiv ID, or
official documentation URL. Store a revision and retrieval time when
observable. Distinguish retrieval time, publication time, and the time an
experiment ran. Renames preserve identity when evidence supports that join;
matching names or copied READMEs do not.

For mutable official pages, retain the resolved URL, actual retrieval timestamp,
response digest and inspection depth; archive permitted bodies when needed for
reconstruction. A later digest is not a capture of an earlier response. Keep
known stable repository node IDs so name reuse cannot look like an unchanged
source; legacy missing IDs remain an explicit identity limit.

The existing `sources.json`, `revisit_fingerprints.json`, `notes.md`, and
`archive/hourly/` retain the historical evidence. Search by canonical ID
before creating a card. Record new evidence under the existing source
section when revisiting it. Preserve corrections and retractions as dated
changes; do not quietly replace a prior result.

For each material finding record:

```text
Source ID, URL, revision, retrieved_at:
Prior card/section (or first sighting):
Observed change and exact supporting artifact:
Evidence status: Contract | Reported | Reproduced | Hypothesis | Unknown
Claim: population, task, model/rubric, metric, split, sample size:
Limitations: label provenance, uncertainty, confounds, unavailable evidence:
Design implication and counterexample:
Disposition: archive-only | refine-reference | new-placement | investigate
Target reference and falsifier (if changing guidance):
```

Contract labels cover documented interfaces, not vendor performance promises.
Reported numbers stay attributed even when a repository has tests. A local
reproduction needs actual commands, inputs, runtime, output, and artifacts.
HTTP 401/404 or a failed fetch means unavailable evidence; do not infer that
a model does not exist. Do not quote search snippets as inspected papers.

## Discovery and revisits

Use the [maintenance contract](maintenance.md) for recurring collection,
changed-source review, aged-card sampling, and whole-skill reassessment. Verify
scheduler liveness and completed-review receipts separately; a cadence written
in a source registry or a script filename does not establish an active job.

Treat revisit HIGH like novel HIGH. Compare fingerprints, then inspect the
actual diff. A moved SHA or push time is a review trigger, not evidence of
changed capability. Material changes include contracts, release contents,
calibration claims, serving behavior, evaluation protocols, and retractions.
Stars, likes, or forks alone are archive-only observations.

Discovery queries must span the relevant class and classical literature.
Use primary papers, official docs, code, and model cards. Avoid star-sorted
caps; disclose pagination limits, missing sources, and search coverage.
Keep the existing preference against paid X/Twitter collection. Do not
install or run third-party projects merely because a scan found them.

For a full refresh, retain a coverage ledger: prior scan cutoff, broader-review
date, retrieval window, queries, page counts and caps, requested URLs, failed
fetches, and selection reasons. Distinguish catalog traversal, metadata triage,
primary-artifact inspection, and reproduction. Split searches that exceed a
host's result cap; disclose moving totals in a live index. A directory vote,
star, or repeated appearance in correlated lists is not independent evidence.
Identify older work newly discovered today separately from newly published work.
Close every explicitly requested source with a disposition or an evidence gap.

When inspecting a benchmark, trace its labels, denominators, splits, retries,
cost/timing boundaries, and accessible raw artifacts. Note semantic changes
inside API-compatible wrappers. Unknown usage must remain unknown, proxy rates
must stay estimates, and public code must not be called a reproduced run.
Update last-look fingerprints only for sources actually reviewed, with the
review depth recorded; metadata collection alone does not reset their review age.

The probe collector is deliberately narrower than discovery. It checks
specified sources and returns evidence for review. It does not claim to
census the ecosystem or automatically promote findings into doctrine.

## Promotion into guidance

Ask: “Which future design decision changes because of this evidence?” If
none, retain the card in research only. For a promotion, state the old rule,
the evidence that challenges it, the smallest revised rule, its scope, and
a falsifying example. Edit the relevant concept once and link supporting
material. Do not append the same paragraph to all references.

Preserve useful negative results. Separate architectural existence, wire
compatibility, measured quality, and equal-quality cost. A new endpoint,
release, port, or compression format does not by itself create a new model
family or establish parity. A harness does not turn every run into gold.

## Review and stopping rule

Use [the fold prompt](prompts/research-fold.md). Run `make check`, inspect
the diff, and review semantic changes against the skill's decision-design
card. If the evidence only updates the archive, say so and stop. A research
run need not change the product. No script stages, commits, or publishes.
Preserve the source packet before ending a partial run and name what is
still unverified.

Periodically assess usefulness: accepted design corrections, resolved
uncertainties, reproductions, negative results, runtime size, and time to
find the relevant rule. Counts of repos, locks, or hourly commits do not
measure progress toward the mission.
