# Offline multiclass support router — executed journey

**Terminal decision: accept the frozen word+character SVM for this local proxy;
no production activation.** All predeclared gates passed. The always-review
incumbent remains runnable for rollback. This is an actual 150-intent queue
recommender, not a binary in-scope detector and not a general Jev replacement.

Started from [the exact Augustus candidate](https://github.com/24601/Augustus/commit/5b7610b767c9373cf2d0d25983f0e913f736caae),
not main. Called `reload_skills`, then loaded `augustus-train` and `augustus`.
Read the trainer's data/splits, fit/serve, improve/confirm and compute references.
No scenario expected notes or prior review advice were read; no nested agents,
paid calls, rentals, skill edits, test edits, push or merge were used.
The receipt fingerprints all 30 tracked candidate skill files, including the
actually loaded entry points. Parent installation checks are separate evidence.

## Contract and supported actions

[contract.json](contract.json) was written before fitting or inspecting test
outcomes. All 150 official training intents are supported; no budget-driven
subset was needed. `prepare` freezes their identities and action map to
`taxonomy.json` before fitting. The complete label vocabulary is also preserved
in `receipt.json` under `audit.label_counts.fit` (minus the reject class `oos`).

Input is a JSON object containing only `text`, an English, single-intent utterance
of 1–2000 characters. Output recommends `support.<intent>` or
`support.manual_review`, with an explicit reason. For example:

- `balance` → `support.balance`: triage an account-balance inquiry.
- `play_music` → `support.play_music`: triage a playback request.
- `weather` → `support.weather`: triage a weather-information request.
- `transfer` → `support.transfer`: triage a transfer request, **not execute it**.

The emitted recommendations do not enqueue remotely or execute account actions.
An application operator owns manual review and downstream authorization.
The corpus contains single-intent utterances across many classes, not gold for
several simultaneous intents in one utterance. Multi-intent, multilingual and
adversarial smoke probes are diagnostics, not supported-population guarantees.
Additional request fields, including new label/options overrides, are rejected.
SVM margins and winner gaps are relative scores, **not calibrated confidence**.

## Data, labels and independence limits

Source: [clinc/oos-eval at the pinned revision](https://github.com/clinc/oos-eval/tree/828f8093932c8fe6ca7936c3d2e52903b1c523de),
`data/data_full.json`. Attribution: Larson et al., *An Evaluation Dataset for
Intent Classification and Out-of-Scope Prediction* (EMNLP-IJCNLP 2019),
[paper](https://aclanthology.org/D19-1131/).
The [CC BY 3.0 license](LICENSE.clinc) is retained verbatim; source, README and
license SHA-256 values and retrieval time are in [receipt.json](receipt.json).
Corpus and binary artifacts are regenerated outside Git.

Official labels are crowdsourced paraphrases/scenario responses, not our own
adjudicated support-ticket outcomes. No private records, teachers, pretrained
representations or synthetic training labels were used. Learned vocabulary,
IDF and SVM weights see training rows only. The feature methods are word
TF-IDF (1–2 grams), character TF-IDF (3–5 grams) and their union, each with
LinearSVC C=1. Character features challenge lexical brittleness; their union
tests complementary evidence. Bigger encoders were unnecessary for this CPU
budget and have additional dependency and pretraining-lineage costs.

Normalized duplicate removal uses NFKC, casefold and word-token whitespace.
Earlier role owns the row; later duplicates are dropped, labels never rewritten.
There were 67 removals (28 train, 16 dev, 23 test), including four cross-role
label conflicts. Retained counts: **15,072 train, 3,084 dev, 5,477 test**.
IDs, conflict IDs, counts per label and split hashes are in the receipt.
No worker, seed-family, account or time IDs are supplied, so semantic-family
and future-time independence cannot be established.

Character-trigram audit found 175 retained test rows at cosine ≥0.95 to train.
A post-freeze diagnostic including dev found 215 near rows. They remain explicitly
labeled diagnostics, not clean independent generalization evidence. Removing
them descriptively leaves 5,262 rows with cost **0.122558**, versus 0.300 review.
This did not alter the model, threshold, acceptance rule or original test result.
Lower-similarity rows are not proof against hidden semantic-family overlap.

The fit process never opens confirmation data; both `confirm.json` and the raw
source directory were moved away before fitting and restored only after the
model/threshold/hash manifest was frozen. This is an auditable file/phase split,
not an OS privilege boundary. Test outcomes were inspected only after freeze.

## Search and observed outcomes

Costs: correct route 0, wrong route (including OOS routing) 1, review 0.3.
Dev selection weights the OOS prior to 1000/5500 from the **documented** test
design; observed test labels/outcomes do not select the prior. Other mass is
equally divided across 150 intents. Three fits × 24 margin/gap policies = 72
policies; the full regenerable trial ledger and raw development scores stay
outside Git. The compact receipt preserves each family's best eligible policy.

| Challenger | Selected top / gap | Weighted dev cost | OOS routed on dev |
| --- | --- | --- | --- |
| Word SVM | 0 / 0.5 | 0.128065 | 9/100 |
| Character SVM | −0.5 / 0.5 | 0.121671 | 11/100 |
| Word + character SVM | 0 / 0.25 | **0.116102** | 9/100 |

One finalist was frozen, without refitting on dev or test. Independent-role
test results: **3,755 correct routes, 185 misroutes, 1,537 reviews**.
Mean cost **0.117966**, coverage **71.94%**, OOS misroutes **92/1,000**;
93 misroutes were in-scope confusions. Lowest intent correct-route recall was
`distance`, 13/30 = 43.33%, above the predeclared 30% empirical floor.
Every intent's denominator and recall are retained.

Paired cost difference versus incumbent: **−0.182034**. The predeclared
one-sided 95% Hoeffding upper bound is **−0.165497**, below −0.03.
This bound is conditional on independent representative rows; unknown seed
families prevent a categorical population-generalization claim. Slice gates
are empirical checks, not simultaneous confidence bounds. Actual review cost,
queue usefulness, real support prevalence and production drift remain unmeasured.

## Runtime and checks

- All fit/search: 30.33 measured in-function CPU seconds; whole process
  `/usr/bin/time -v`: 30.75 user + 0.61 system = **31.36 CPU seconds**,
  31.39 seconds wall, 457.30 MiB peak RSS. RLIMIT_CPU=1200, one numerical
  thread, three fits, no further search. Well below the 20 CPU-minute cap.
- Timed preparation replay: 7.18 user + 0.24 system seconds, 7.88 wall;
  regenerated train/dev/test/taxonomy files were byte-identical via `cmp`.
  Initial preparation was not separately instrumented.
- Frozen confirmation + full fresh-process replay: 11.76 user + 0.87 system
  seconds, 12.47 wall. All **5,477 actions/reasons/queues matched**, maximum
  observed top-margin drift 0; tolerances were action equality and 1e-10.
- Cold single-request process: 1.448 seconds. Warm single-request p95 over
  the first 200 official test rows: 1.526 ms. This is a bounded sample, not a
  full production latency distribution. Confirmation peak RSS: 287.92 MiB.
- `check.py`: hand-derived asymmetric loss cases, thresholds just above/below
  and exactly equal, ties, label-column permutation, OOS, no-feature and NaN
  policy cases. Fresh bundle-only process exercised three distinct routes,
  semantic unknown, emoji, null, missing/wrong types, empty/blank/overlong text,
  unknown label override, invalid JSON, multi-intent/shifted/injection probes,
  missing/corrupt bundle and the runnable incumbent. All assertions passed.
- Initial `make check` found missing PyYAML in the system interpreter. Installed
  the repository-pinned PyYAML 6.0.2 into a separate check environment, not the
  inference lock. `make check PYTHON=/tmp/augustus-multiclass/check-venv/bin/python`
  then passed repository checks, **190 tests**, numerical self-tests and shell
  syntax. No existing check or assertion was weakened.

## Reproduce and use

Run from the repository root at the candidate plus these owned files. Python
3.11.6 was used. Only `prepare` needs public network access; fitting, inference
and confirmation are offline. `uv` is environment tooling, not a runtime
dependency. Use new output directories; scripts refuse to overwrite runs.

```sh
D=research/audits/2026-09-26-trainer-journeys/multiclass
W=/tmp/augustus-multiclass-replay
mkdir -p "$W"
uv venv "$W/venv"
uv pip install --python "$W/venv/bin/python" -r "$D/requirements.lock"
P="$W/venv/bin/python"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
"$P" "$D/check.py"
/usr/bin/time -v "$P" "$D/experiment.py" prepare "$W/run"
mkdir "$W/sealed"
mv "$W/run/confirm.json" "$W/run/source" "$W/sealed/"
/usr/bin/time -v "$P" "$D/experiment.py" fit "$W/run"
"$P" "$D/check.py" "$W/run"
mv "$W/sealed/confirm.json" "$W/sealed/source" "$W/run/"
/usr/bin/time -v "$P" "$D/experiment.py" confirm "$W/run"
"$P" "$D/summarize.py" "$W/run" "$W/receipt.json"
printf '%s\n' '{"text":"what is my bank account balance"}' \
  '{"text":"explain quantum entanglement"}' '{"text":null}' | \
  "$P" "$D/router.py" "$W/run/finalist"
# Explicit rollback; every request goes to support.manual_review:
printf '%s\n' '{"text":"what is my bank account balance"}' | \
  "$P" "$D/router.py" incumbent
```

Original commands used `D` as above, `W=/tmp/augustus-multiclass`, and the
same phase sequence. The final compact receipt was written to `$D/receipt.json`.
An additional preparation replay used `$W/preparation-replay`; `cmp` compared
its `fit.json`, `dev.json`, `confirm.json`, `taxonomy.json` with `$W/run`.

Compare source/split/taxonomy hashes, finalist policy, action counts and losses,
not runtime, timestamps or entire binary manifests. `summarize.py` was added
after freeze and does not participate in fitting or acceptance; its hash appears
in a replay manifest but not the original frozen three-file source manifest.
Only deserialize the locally generated trusted joblib bundle. Its digest
detects accidental corruption, not malicious replacement of bundle + manifest.
For production, authentication, service supervision, review capacity and real
outcome validation would be separate work; none is claimed here.
