---
layout: default
title: Decision-model families and evidence
page_class: dense
---

# Decision-model families and evidence

This page is a navigation map, not a leaderboard or live census. Start with the
decision you need to make, then choose a model family whose output has the right
meaning. Treat provider and project claims as evidence to test in your own
workflow.

## Start here

- [Augustus skill](https://github.com/24601/Augustus/blob/main/.agents/skills/augustus/SKILL.md) — the concise runtime method.
- [Judgment class](https://github.com/24601/Augustus/blob/main/.agents/skills/augustus/references/judgment-class.md) — family selection and placement.
- [Validation](https://github.com/24601/Augustus/blob/main/.agents/skills/augustus/references/validation.md) — held-out workflow evaluation.
- [Boundary audit](https://github.com/24601/Augustus/blob/main/.agents/skills/augustus/references/boundary-audit.md) — ownership, authority, and safety boundaries.

## Default hosted exemplar

Augustus uses TypeSafe Jev Choice/Score/Noul as its default hosted exemplar.
That is a practical teaching preference, not a claim of universal superiority,
equivalence with other families, or market adoption. Read the
[current TypeSafe skills](https://github.com/typesafe-ai/skills) before writing
integration code, and verify contracts against the service version you use.

## Family map

<p class="table-hint">Scroll to compare all columns →</p>
<div class="table-scroll" role="region" aria-label="Decision-model family comparison" tabindex="0" markdown="1">

| Family | Useful for | Evidence and boundary to inspect |
| --- | --- | --- |
| Hosted decision API | Bounded choices, ordinal scores, or compact classifications over caller-supplied evidence | Current request and response contract, latency, privacy, candidate coverage, and held-out task quality |
| Supervised classifier or decision head | Repeated decisions with labeled domain data and controlled deployment | Dataset provenance, class balance, distribution shift, calibration where policy needs it, and serving behavior |
| Encoder or extractor | Locating spans, entities, fields, or schema-conditioned signals | Offset fidelity, recall on target documents, multilingual or domain coverage, and the downstream decision that consumes the extraction |
| Ranker or reranker | Ordering retrieved items, search results, reviews, or work queues | Candidate recall before ranking, order metrics tied to user outcomes, tie behavior, and fallback when evidence is weak |
| Constrained autoregressive readout | Selecting among allowed values using an existing generative model | Tokenization and option-order effects, latency, output constraints, and whether scores have the semantics required by policy |
| Vision or perception scorer | Judging images, regions, controls, or visual state | Sensor coverage, localization error, modality loss, adverse visual cases, and independent checks before action |

</div>

These families can be composed. A common pattern extracts observable evidence,
ranks or classifies it, applies explicit policy, then lets deterministic code or
an authorized person perform and verify the action.

## How to choose

1. Write the desired behavior and a simple deterministic or human baseline.
2. Separate exact computation and hard constraints from the uncertain judgment.
3. Define the output semantics: category, order, score, abstention, or evidence span.
4. Check that the candidate set and observations contain the information needed for the decision.
5. Set policy from action costs and authority, including fallback and review.
6. Evaluate held-out workflow cases and inspect errors before expanding scope.

## Evidence labels

- **Contract** — behavior guaranteed by a current specification or API contract.
- **Reported** — a result stated by its author or provider and not independently reproduced here.
- **Reproduced** — rerun with enough procedure and artifacts to inspect.
- **Hypothesis** — a plausible design claim awaiting a discriminating test.
- **Unknown** — evidence is absent, stale, or insufficient for the decision.

Keep the label attached when a claim is copied into a design note. A public
benchmark can support a hypothesis, but deployment policy should follow evidence
from the intended inputs, failure modes, and action costs.

## Research and provenance

The public runtime skill stays concise. Broader observations and historical
snapshots remain available for research and audit:

- [Research guide](https://github.com/24601/Augustus/blob/main/research/README.md)
- [Working notes](https://github.com/24601/Augustus/blob/main/research/notes.md)
- [Source registry](https://github.com/24601/Augustus/blob/main/research/sources.json)
- [Archived findings](https://github.com/24601/Augustus/blob/main/research/archive/findings.md)
- [Hourly evidence archive](https://github.com/24601/Augustus/tree/main/research/archive/hourly)
- [Revisit checklist](https://github.com/24601/Augustus/blob/main/research/revisit-checklist.md)
- [Historical ecosystem snapshot at `0b43a8d3b8d2d389b59415747f566dcbaa3f3ec8`](https://github.com/24601/Augustus/blob/0b43a8d3b8d2d389b59415747f566dcbaa3f3ec8/docs/ecosystem.md)

Release context remains in
[v0.5.1](https://github.com/24601/Augustus/releases/tag/v0.5.1) and
[v0.5.0](https://github.com/24601/Augustus/releases/tag/v0.5.0). For corrections
or new evidence, use the repository's
[contribution guide](https://github.com/24601/Augustus/blob/main/CONTRIBUTING.md).
