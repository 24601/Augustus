---
layout: default
title: Release notes v0.5.1
---

# Release notes v0.5.1

Patch on the 0.5.0 package surface. v0.5.0 (2026-09-20) shipped class-wide
recipes and Pages. Hourly folds after that stayed pinned at 0.5.0. This
cut is the human-facing pin.

Place typed probabilistic judgment for the decision-model class. TypeSafe
Jev (Choice, Score, Noul) is the dominant exemplar most users will call.
Peers are in the class. They are not equal in adoption. Exact work stays
in code or policy. A soft score is not a proof.

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12). Live HEAD of that repo is still this commit.
Checked 2026-09-21.

Prior class recipes: [v0.5.0 notes](release-notes-v0.5.0.md).
Diagram: [with vs without Augustus](https://24601.github.io/Augustus/).

### Added

- **GEPA domain-adapt.** Praneeth ADE on a Jev Choice. Schema-valid is
  not the same as correct. API confidence is not P(correct). GEPA revises
  Choice instructions and criteria with weights fixed. Brier and F1 stay
  *theirs*. A review queue is not an F1. A soft score is not a gate.

### Changed

- Package pin 0.5.0 to 0.5.1 (skill metadata, marketplace, README, Pages
  kicker, CITATION.cff).
- README still ends at License. The uniqueness gate fails if a dump wall
  returns after that heading.
- Skill YAML description is a short class-first blurb. The trigger
  keyword wall is `references/activation-triggers.md`.

Catalog densifies since 0.5.0 stay in `research/notes.md` and
`research/changelog-hourly.md`. They are not release-note walls.

No invented metrics. No `pipeline()` install recipes.

## Recipes

Backend-agnostic. Problem, without Augustus, with Augustus, what to
measure. Numbers below are *theirs*, not a new bench. Quote the source
card. Do not treat this page as a leaderboard.

### Domain adapt: GEPA on Jev

- **Problem.** A schema-valid Choice is treated as a correct label, API
  confidence is treated as P(correct), or F1 is treated as the
  review-queue policy.
- **Without.** Ship the adapted prompt. Treat GEPA as a new scoring-table
  species.
- **With.** schema-valid is not the same as correct. API confidence is not
  P(correct). GEPA revises Choice instructions and criteria with weights
  fixed. Brier and F1 stay *theirs*. A review queue is not an F1. A soft
  score is not a gate. Not an 18th scoring-table species.
- **Measure.** Brier 0.1357→0.0747 *theirs*. F1 69.1%→79.7% *theirs*.
  FN 4→6 *theirs*. Retention of positives under the review cutoff is a
  different ledger from F1.

Earlier class recipes (encoder locate vs decide, open heads, NanoJev,
llm-to-jev, jcr, prompted JSON, measurement honesty) stay on the
[v0.5.0 notes](release-notes-v0.5.0.md).

Homepage: https://24601.github.io/Augustus/

### Install

```bash
claude plugin marketplace add 24601/Augustus
claude plugin install augustus@augustus
```

```bash
npx skills add 24601/Augustus --skill augustus
```

Full notes: [CHANGELOG.md](https://github.com/24601/Augustus/blob/main/CHANGELOG.md)
