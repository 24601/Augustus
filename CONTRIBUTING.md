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
python3 research/revisit_fingerprints.py --self-test
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
- Do not reopen or amend a merged fold PR (#23–#50)
- uniqueness_gate.py checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 + 1049 + 1143 + 1248 + 1340 + 1441 + 1542 + 1643 + 1746 consecutive locks, plus the revisit / since-last-look protocol substring in the skill and research files.
- Hourly uniqueness dump: `research/changelog-hourly.md` (archive,
  not release notes)
- Treat **revisit HIGH like novel HIGH**. Catalogued repos are not
  done. If fingerprints moved (`default_sha`, `pushed_at`,
  `description_hash`, `release_tag`) or the README / API / release /
  calibration claim / serving port / bench rewrote, densify the prior
  notes card. Stars / likes / forks alone is star-noise, not a fold.
  Do not mint a sibling first sighting. Do not invent equivalence.
  SHA move is not a replica. Checklist:
  `research/revisit-checklist.md`. Helper:
  `research/revisit_fingerprints.py`. `notes.md` §122.

Revisit / since-last-look lock: catalogued repos are not done; store fingerprints default_sha, pushed_at, description_hash, release_tag; material change is README/API/release/calibration claim/serving port/bench rewrite; star-noise is stars/likes/forks alone; densify the prior notes section, do not mint a sibling first sighting; do not invent equivalence; SHA move is not a replica; treat revisit HIGH like novel HIGH for Augustus; notes.md §122

## Secrets

No API keys, tokens, or `.env` files in the tree. Push protection and
secret scanning are on. See `SECURITY.md`.

## Branch protection

Default-branch protection, required checks, and org settings are
parent-owned. This file does not change them. Prefer a PR off latest
`main`. Do not force-push shared branches.
