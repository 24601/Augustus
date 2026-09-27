# Targeted reporting repair, 0.8.2-dev

User authorized the concrete fixes proposed after inspecting actual application
outputs. This is not another optimization campaign or a release. Published 0.8.1
is unchanged; both skill and marketplace development versions are 0.8.2-dev.

## Changes and falsifiers

- Population-bound binary raw-score receipts compute numerator, denominator,
  FP/FN and cost from explicit IDs, bind selected values and policy, and hash the
  CLI input. A regression using all four rows instead of three must fail.
- Distinct score-up/down and threshold-up/down calculations expose reversed
  explanations. Boundary tests use asymmetric costly errors; exact rational
  arithmetic avoids overflow and cancellation in these diagnostic calculations.
- Guidance distinguishes selected training loss, procedure estimates and
  independent evidence, and stops resampling that cannot change a decision.
- Robustness alternatives remain conditional on observed instability. No
  universal smoothing, mandatory model or calibration step was added.

The existing binary probability evaluator is intentionally unchanged: raw vendor
scores do not acquire probability meaning. The new trainer helper is a narrow
diagnostic, not a fitting/search framework. It cannot verify selection semantics,
label truth, sampling, serving rounding/clipping, drift realism or future loss.
Applications must replay actual policy behavior when it differs from the helper.

## Executed checks

```sh
python3 -m unittest discover -s tests -p test_policy_receipt.py -v
python3 research/audits/2026-09-27-reporting-repair/reproduce.py
python3 .agents/skills/augustus-train/scripts/policy_receipt.py \
  research/audits/2026-09-27-reporting-repair/behavior/policy-input.json
make check
```

Five new tests pass, including selected-population arithmetic, directional
perturbations, identity binding, bad IDs/values, duplicate JSON keys, CLI and
maximum-finite arithmetic. Full suite: 197 tests and both self-tests pass.
`prior-output-replay.json` replays the already-revealed application audit:
555/1,200 historical actions versus 44/300 current actions; future-audit loss
0.20325 at baseline, 0.34275 with score −0.01, 0.154 with score +0.01.
This is regression evidence, not fresh confirmation or training data.

## Fresh-agent behavior

A tool-invoked fresh Task agent received only the candidate skill/references and
the requests in `prompts.md`, not test answers or previous audit findings. Model
identity was not independently exposed by the Task tool; no routing claim is made.
Exact file hashes, executed command, input, receipt and raw answers are retained
under `behavior/`. The coordinator reread the answers and independently reran the
CLI; output matches byte-for-byte.

| Request | Observed result | Coordinator assessment |
| --- | --- | --- |
| Population and direction | 1/3, not 2/4; score-up FN 0, threshold-up FN 2; actual helper used | Targeted arithmetic/reporting pass |
| Bootstrap launch note | Refuses 95% future guarantee; freezes policy, proposes fresh outcomes and bounded selection-optimism check | Targeted evidence/stopping pass |
| Existing trainer_no_training scenario | Chooses approved lookup, repairs stale versions, unknowns to operations | Core choice pass; see caveat |
| Copy-edit control | One corrected sentence, no model/eval ceremony | Output-shape pass; not activation measurement |

Retained caveat: the no-training answer says 30 notes are “far too few” to justify
or evaluate a model, too categorical without task assumptions. The decisive
reason is the authoritative mapping, not a universal sample-size floor. This
sentence is not accepted as guidance; raw output is preserved. The bootstrap
answer's extra out-of-fold check is justified by selection optimism, not required
on every task. No comparative skill-effect or cost-reduction claim follows from
this small smoke. The original independent confirmation packet remains unopened.

No application was deployed. No activation-description changes were made. A
same-budget comparison on untouched requests is still needed before claiming
these repairs improve overall agent outcomes or reduce cost.
