# Contributing

Docs and skill PRs are welcome. This is a placement skill, not a TypeSafe
product and not a vendor how-to.

## What to send

- Skill / reference-card clarifications that keep Jev as **exemplar, not
  monopoly**
- Measurement-honesty fixes (ranking ≠ calibration; Score is 0..n−1;
  Noul has no confidence field; soft Noul ≠ hard gate)
- Composition notes (fail-open vs fail-closed per action; prune ≠ deny)
- Formal-methods honesty (a Noul is a SENSOR, not a proof)

Do not invent metrics. Do not paste `pipeline()` / `pip` / `npm` install
recipes that read as endorsements. Quote *theirs* and label vendor
figures.

## Adversarial review

Read the change against the skill's own non-negotiables before opening
the PR. The usual failure modes are soundness theater: hard-gating a
soft Noul, treating ECE as an edge, treating 0.85 / minProbability as
Harbor, or laundering a score as a proof.

Run what you can locally:

```bash
python3 .agents/skills/augustus/scripts/evaluate_decisions.py --self-test
python3 .agents/skills/augustus/scripts/uniqueness_gate.py
```

The Pages workflow must stay green. After #34 it greps `_site/index.html`
for `TypeSafe Jev Choice/Score/Noul`, `Install the skill`, and `LICENSE`
(`LICENSE` is in `docs/_layouts/default.html`; the other two stay in
`docs/index.md`).

## Fold uniqueness

Hourly research folds carry uniqueness locks so the same cluster is not
re-opened as "new." Before folding:

- Read `research/notes.md` and the uniqueness fragments in
  `.agents/skills/augustus/SKILL.md`
- Do not re-fold an already-landed section as a new beat
- Do not reopen or amend a merged fold PR (#23–#34). #35 is the 0843 fold.
- Pre-0.4.0 uniqueness dump: `research/changelog-hourly.md` (archive,
  not release notes)

## Secrets

No API keys, tokens, or `.env` files in the tree. Push protection and
secret scanning are on. See `SECURITY.md`.

## Branch protection

Default-branch protection, required checks, and org settings are
parent-owned. This file does not change them. Prefer a PR off latest
`main`. Do not force-push shared branches.
