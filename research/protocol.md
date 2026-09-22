# Research that improves the skill

The objective is better decision design. A growing source count is not a
quality metric. Study methods as well as products: decision theory,
selective prediction, calibration, conformal methods, causal effects,
decision-focused learning, extraction, routing, optimization, and human
decision processes. Vendor discovery alone cannot cover this mission.

## Source and claim identity

Use the canonical owner/repository, model-card ID, paper DOI/arXiv ID, or
official documentation URL. Store a revision and retrieval time when
observable. Distinguish retrieval time, publication time, and the time an
experiment ran. Renames preserve identity when evidence supports that join;
matching names or copied READMEs do not.

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
