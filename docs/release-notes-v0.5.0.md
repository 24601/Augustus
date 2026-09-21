---
layout: default
title: Release notes v0.5.0
---

# Release notes v0.5.0

Place typed probabilistic judgment. Jev is the exemplar, not the
monopoly. The same with/without split applies to GLiNER/GLiClass, Laya,
SemIf, NanoJev, kev, Jeff-1, localjev, llm-to-jev shaped prompts, and
other Choice/Score/Noul-style tools. Exact work stays in code or policy.
A soft score is not a proof.

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12). Live HEAD of that repo is still this commit.

Diagram: [with vs without Augustus](https://24601.github.io/Augustus/)
(README SVG + Pages). Merged #39 hygiene is on main. Open #41 is
not in this cut.

### Added

- **Pages / onboarding.** Custom layout. With vs without comparison.
- **README.** Scannable skill map. No uniqueness wall.
- **Class / migration.** llm-to-jev on-ramp. SemIf rename densify. NanoJev
  unified-games densify. jcr lookup **does not execute**.
- **Measurement honesty.** Hysteresis is policy. Instruct-tuning ECE.
  hop-ECE invariance. Harbor-jevals / Verdict / DecisionOps as themes.
  ranking ≠ calibration. soft Noul ≠ hard gate.

No invented metrics. No `pipeline()` install recipes.
heuristic conversion ≠ calibrated Noul.

## Recipes

Backend-agnostic. Problem → without Augustus → with Augustus → what to
measure. Numbers below are *shapes*, not new benches. Quote *theirs* on
the source card; do not treat this page as a leaderboard.

### Encoder locate vs decide — GLiNER / GLiClass

- **Problem.** A locate or categorize encoder is dropped in as if it were
  a Choice/Score/Noul head.
- **Without.** Swap GLiNER for the decision model. Hard-gate spans or
  label scores. Bake off against a chat LLM.
- **With.** Species map first (locate vs categorize vs safety-schema vs
  decide). Extractive spans stay extractive. Remainder judgment is a
  separate question. Soft scores ≠ hard gates.
- **Measure.** Span/F1 or assignment quality on the encoder task,
  separately from ECE/Brier on the decision. Never quote a softmax or
  span score as a calibrated Noul.

### Open heads — Laya, SemIf, kev, Jeff-1

- **Problem.** Wire-compat, argmax agree, or a speedup is treated as a
  replica of a calibrated decision model.
- **Without.** Drop-in swap. Ship the systems timing. Skip OOD. Treat
  accuracy as calibration.
- **With.** Softmax over options ≠ calibrated Noul. Systems comparison ≠
  semantic equivalence. Replica honesty: name the head (open, constrained-AR,
  encoder, specialist). Acc vs ECE. Fail polarity in code.
- **Measure.** Held-out ECE/Brier *and* accuracy/AUC. In-distribution vs
  OOD. Do not promote a speedup (even a large one) as semantic
  equivalence.

### Gameplay specialist — NanoJev

- **Problem.** Game success is treated as a calibrated Noul.
- **Without.** Quote a win rate as if it licensed a production gate.
- **With.** Specialist gameplay S1 / open replica, not TypeSafe Jev. Local
  boolean ≠ TypeSafe noul. Soft scores ≠ hard gates.
- **Measure.** Held-out game metrics on one ledger. ECE/Brier on another.
  Do not mix the two.

### Prompt conversion — llm-to-jev

- **Problem.** A decision-shaped LLM prompt is assumed to be an equivalent
  Choice/Score/Noul.
- **Without.** Paste, convert, ship. Treat the compiler as a replica.
- **With.** Heuristic on-ramp, not an LLM and not a guarantee. Review the
  generated Score rubric. Ordered criteria, not an arbitrary 0–1 range.
  Prose stays with the LLM. Conversion ≠ calibrated Noul.
- **Measure.** Suitability / compatibility labels and human review of
  generated criteria. Not "equivalent behavior."


### Domain adapt — GEPA on Jev

- **Problem.** A schema-valid Choice is assumed correct, or API confidence is
  treated as P(correct), or F1 is treated as a review-queue policy.
- **Without.** Ship the adapted prompt. Treat GEPA as a new scoring-table
  species.
- **With.** schema-valid is not the same as correct. API confidence is not
  P(correct). GEPA revises Choice instructions/criteria with weights fixed.
  jev-1.13.0 weights fixed. review-queue policy is not F1. Soft is not gate.
  Not an 18th scoring-table species.
- **Measure.** Brier 0.1357→0.0747 *theirs*. F1 69.1%→79.7% *theirs*. FN 4→6.
  Retention of positives under the review cutoff is a different ledger.

### Capability lookup — jcr

- **Problem.** Finding a documented command is treated as permission to
  run it.
- **Without.** The agent executes whatever the tree returned.
- **With.** One tool, nested capability tree, returns context, **does not
  execute**. Routing ≠ permission. Docs ≠ authority to run. 0.6 band is
  application policy.
- **Measure.** Lookup+explain only. Input/cost/wall-time deltas are not
  Harbor task-execution.

### Prompted JSON vs structured read — localjev

- **Problem.** Parsed JSON from a generator is treated as a Noul.
- **Without.** Schema-valid output is taken as the picked-right
  probability.
- **With.** Prompted JSON ≠ structured logit read. Wire-compat ≠
  logit-equiv. Schema-valid ≠ picked-right.
- **Measure.** Schema pass rate separately from calibration and from
  "did code take the right effect." Entropy-as-confidence is not ECE.

### Measurement honesty — hysteresis, ECE, Harbor

- **Problem.** A single threshold, an equal-width ECE, or a schema-pass
  is treated as Harbor.
- **Without.** 0.85 as a hard gate. Ranking as calibration. Silent
  provider failure as a policy outcome. Instruct-tuned confidence as
  honesty.
- **With.** Hysteresis `{enter, exit}` is policy attached to a
  probability. Report equal-width *and* quantile ECE. hop-ECE must not
  move under permutation (if it does, the instrument is the story).
  DecisionOps: ACT / REVIEW / FALLBACK; a provider failure is **not** a
  policy outcome. VERIFY needs discriminating evidence.
- **Measure.** Accuracy@0.5 vs ECE (they can disagree). Schema-pass vs
  joint fields. Quality denominators include only valid scored answers.

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
