# Local SMS review classifier — executed public-proxy journey

**Result:** frozen `word8` (word TF-IDF + logistic regression, C=8), threshold
0.45, passed the prespecified **proxy** confirmation against always-ham. No
production activation or efficacy claim. The CLI prints `ham`/`spam-review`;
it never deletes or modifies messages. Failures return ham with an explicit
non-ok status, meaning preserve the message, not “verified legitimate.”

Started at candidate `5b7610b767c9373cf2d0d25983f0e913f736caae`, not main.
Reloaded skills, then loaded Augustus Train and its companion. Actual consulted
skill hashes are in `skill-hashes.sha256`. No skills/tests edited, no expected
scenario notes or prior review recommendations consulted, no nested threads,
paid calls, pretrained models, GPU, or rental. All deliverables are in this folder.

## Replay from a clean copy of this directory

Python **3.11.6**, Linux x86-64 were used. Resolved numerical/inference packages
are pinned in `requirements.lock`; sklearn is BSD-3-Clause stock. No learned
pretraining lineage: vocabulary and coefficients are fitted from this corpus.
Run these from this directory (using a fresh copy avoids overwriting receipts):

```bash
uv venv .venv --python 3.11
uv pip install --python .venv/bin/python -r requirements.lock
.venv/bin/python journey.py prepare
.venv/bin/python journey.py fit word1
.venv/bin/python journey.py fit word8
.venv/bin/python journey.py fit char8
.venv/bin/python journey.py freeze
.venv/bin/python journey.py confirm
OPENBLAS_NUM_THREADS=1 .venv/bin/python verify.py
```

`prepare` downloads the pinned UCI ZIP if absent and rejects any digest change.
It refuses to replace an existing `work/`. Fits refuse to replace their models
or run after freeze. All raw corpus, splits, predictions, detailed development
errors and models live in ignored `corpus.zip` / `work/`; do not add them to Git.
Receipts are regenerated. Historical timing receipts are conservatively included
in replay's budget arithmetic; no need to delete tracked receipts to rerun.

Working offline inference after replay:

```bash
SHA=$(jq -r .sha256 work/active.json)
BUNDLE=$(jq -r .bundle work/active.json)
printf '%s\n' '{"text":"free prize"}' '{"text":"Meet me at home"}' |
  OPENBLAS_NUM_THREADS=1 .venv/bin/python sms.py "work/$BUNDLE" --sha256 "$SHA"
```

Observed actions: `spam-review`, `ham`; scores 0.9387629681 and 0.0060428568.
Scores are **uncalibrated** estimates, not promises of event probability. The
threshold was tuned empirically for the costs, not set to the calibrated Bayes
threshold 5/6. Equality routes to review. No network or fitting at inference.
Keep serving code, lockfile, contract, frozen receipt, and trusted model together.
Only deserialize a trusted artifact; a matching SHA does not make hostile pickle
safe. `work/incumbent.joblib` is the runnable rollback (hash it with `sha256sum`).

## Source and label guide

UCI SMS Spam Collection, dataset 228, Almeida & Hidalgo (2011), DOI
[10.24432/C5CC84](https://doi.org/10.24432/C5CC84).
[Official source/license](https://archive.ics.uci.edu/dataset/228/sms+spam+collection),
inspected 2026-09-26; official page states **CC BY 4.0**. Credit Tiago Almeida and
José María Gómez Hidalgo and their 2011 DOCENG paper, *Contributions to the study
of SMS spam filtering: new collection and results*. The ZIP's older readme also
retains copyright, as-is warranty and liability language, and requests citation
and a notification email. No outreach was made. This receipt records both, rather
than implying every underlying contributed source has newly verified terms.

Download: `https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip`.
SHA-256: `1587ea43e58e82b14ff1f5425c88e17f8496bfcdb67a583dbff9eefaf9963ce3`.
Raw member and readme digests are in `data-receipt.json`. The source page/readme
were inspected, not archived; no historical webpage snapshot claim.

Labels v1: publisher `ham` → 0, `spam` → 1; spam means recommend human review,
not authorize removal. Unknown labels/empty source records stop preparation,
not silently become ham. No independent adjudication claimed. Incoming message
text is the only feature; sender, consent, chronology and conversation are absent.
Do not relabel suspicious annotations to match the model. Development inspection
found reports *about* spam and context-dependent labels (see `decisions.md`).
This is an inherited proxy taxonomy, not a complete definition of unwanted SMS.

Raw: 5,574 rows (4,827 ham, 747 spam). NFKC/casefold/whitespace-normalized exact
deduplication keeps first occurrence, with conflicting exact keys excluded
(none found); **415 duplicate rows removed**, leaving 5,159. Raw text remains
unchanged as model input. Label-blind groups use URL/digit-normalized templates,
character 3–5-gram cosine similarity ≥0.90, and connected components: **5,027
groups**, largest 12. The grouping vectorizer sees all texts only for partition
construction and is never reused by the classifier. Splits: 3,105 / 1,029 / 1,025
rows, 3,016 / 1,005 / 1,006 groups, fit/search/confirmation. No strata or reseeding.
Split IDs, group membership and content hashes regenerate in `work/split-manifest.json`.

This heuristic binds obvious near-duplicates but cannot prove semantic,
sender, campaign or source independence. No timestamps support a future-time
claim. Deduplication and equal group weighting change the target population:
primary loss is mean of within-group mean row costs, not raw-message prevalence.
Row-weighted diagnostics are also reported. Public access and full-data grouping
are disclosed: confirmation labels were omitted from fit/search code paths by
convention, **not locked away by enforced custody**.

## Measured decisions

| Trial | Search threshold | Group loss | FP | FN |
| --- | ---: | ---: | ---: | ---: |
| Always ham | — | 0.115423 | 0 | 136 |
| word1, C=1 | 0.35 | 0.025871 | 1 | 26 |
| word8, C=8 | 0.45 | **0.015920** | 0 | 21 |
| char8, C=8 | 0.50 | 0.021227 | 0 | 26 |

Three actual fits, 18 thresholds each, same development data. Character stock
was rejected; word8 improved descriptively over word1. No claim that those two
fitted models were independently compared. Hypotheses and label concerns were
written after word1 and before the two improvement trials in `decisions.md`.

One frozen finalist, no refit: **1,025 confirmation messages / 1,006 groups**.
Confusion: TN=897, FP=2, FN=15, TP=111. Review FPR 0.2225%, spam recall 88.10%.
Candidate group loss **0.023857** vs incumbent **0.107356**; paired delta
**−0.083499**, one-sided 95% paired-group bootstrap upper **−0.064612**, below
the prespecified −0.005 gate. Row loss 25/1025 = 0.024390 vs 126/1025 = 0.122927.
All three no-feature fallbacks remain in evaluation; none were dropped.
The percentile bootstrap is an approximate, conditional analysis assuming these
groups represent independent units. It cannot repair residual dependencies,
source bias, inherited label error or a public benchmark's reuse.

Short ≤60-character slice: 551 rows, 4 spam, 2 FP/1 FN; long >160 slice: 36 rows,
7 spam, 0 errors. These are diagnostics, not powered safety guarantees. Sparse
English-era lexical features, UK spam and Singapore/student ham do not establish
performance for modern scams, new languages, changed prevalence or adversaries.
Collect independent contemporary, consent/context-aware labels before deployment.

## Executed checks and resources

`confirm` fresh-process CLI replay: **1,025/1,025 actions/statuses equal**, scores
within 1e-12. Empty, long, wrong type, malformed JSON, emoji, shifted-language,
ambiguous input, boundary/tie and digest failure exercised. `verify.py`: **6 tests
passed**, including hand-computed asymmetric losses, all pairwise partition
separation, actual installed dependency versions, missing/corrupt/wrong-version
bundles, inference exception fallback, and a fresh serving-only directory.
The fresh process does not read training files; this is not an OS access sandbox.

Measured warm single-message p95 **0.365 ms**, cold CLI **0.769 s**, confirmation
process peak RSS **122.15 MiB**, all within contract gates. Initial fit/search
CPU sums **2.592 seconds**; stage receipts total **11.954 CPU seconds**, including
preparation/confirmation/child work, excluding interpreter import/setup overhead.
These are observations, not latency SLAs. Thread pools fixed to one for training;
per-process CPU limits plus cumulative completed-stage accounting bound runs.
Failed/unrecorded process time is not automatically accumulated; no such fitting
failure occurred. The whole training run is far inside the 1,200-second budget.

Repository `make check` initially lacked PyYAML in the system interpreter. After
installing repository-pinned PyYAML 6.0.2 into the isolated environment:
`make check PYTHON=research/audits/2026-09-26-trainer-journeys/binary/.venv/bin/python`
passed structural checks, **190 tests**, numerical self-tests and shell syntax.
This command is run from repository root; full logs stay ignored in `work/`.
Receipts, source and docs only are committed locally; no push/merge/deployment.
