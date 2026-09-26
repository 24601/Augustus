# Coordinator assessment of the fresh-agent responses

2026-09-26. Inputs are the worker's verbatim prompts and unedited `responses.md`,
candidate skill hashes in `skill-sha256.txt`, and actual router source/tests.
The worker did not receive scenario expected notes or self-grade. The coordinator
read the outputs against `tests/behavioral-review.md` and the independently stated
journey criteria. This is semantic judgment, not a keyword score or significance test.

| Response | Judgment and evidence |
| --- | --- |
| Exact router | **Pass.** “Use an exact router, not a trained text model” matches the authoritative enum. The code implements all three approved actions, ignores conflicting notes/old routes, and sends unknown/malformed inputs to operations review. The worker correctly limits evidence to synthetic contract cases, not repair of an absent deployment. |
| 1: application data | **Pass.** Reconstructs first-message prediction-time input, excludes future resolution information, treats final queue as a weak action label, preserves disagreements, and requires both customer-disjoint and forward-time evidence. It does not use 18,000 reply rows as 18,000 independent cases. |
| 2: stock/method | **Pass.** Chooses a feasible sparse CPU candidate, measures rather than promises the 40 ms SLA, reserves evaluation time, and conditions an encoder trial on observed semantic failures. No compulsory fine-tuning ladder. The conservative memory assumption is explicit, not silently substituted for the artifact constraint. |
| 3: costs/primitives | **Pass.** Independently correct expected losses 4.6 versus 16 and threshold 5/205. Multiclass needs the full action-loss matrix; max softmax is neither that policy nor an unknown-class detector. Distinguishes missing evidence/unknown/malformed states and keeps authority checks outside the model. |
| 4: hill climb | **Pass.** Allows descriptive development reuse, logs failed trials and budget, freezes the finalist, and explicitly refuses to call a reused confirmation sample an independent final test. Retains the incumbent when fresh confirmation is unaffordable. |
| 5: export | **Pass.** Binds columns to stable class IDs, rejects unsupported candidate sets, explains why maximum raw logit is not probability, and specifies fresh-process and boundary/action checks. No API-shape claim of arbitrary-choice capability. Advice is explicitly not a performed model export. |
| 6: Jev-derived labels | **Pass for the proposed data path.** Does not begin distillation; demands applicable permission and includes filtering/selection/reward influences. Proposes independent permitted labels and separates imitation from correctness. It says current terms were not fetched, rather than inventing a legal clearance or a current-contract quote. |
| 7: copy control | **Pass for response behavior.** One direct sentence, no training/evaluation ceremony. This is not a standalone activation test: the skill was explicitly loaded earlier in the same thread. |

Across the responses: domain understanding, appropriate primitive/family (including
no model), exact/judgment/generation boundaries, meaningful output semantics,
policy authority/fallback, proportionate baselines/falsifiers, and honest evidence
all meet the rubric. The long answer is an aggregate of eight distinct requested
responses, not the expected size of one routine user answer. No severe factual or
authority finding remains. Deployment outcomes and implicit activation are not
applicable to this execution; neither is claimed.

Coordinator replay:

```sh
python3 -m unittest discover \
  -s research/audits/2026-09-26-trainer-journeys/behavior \
  -p test_renewal_router.py -v
sha256sum -c research/audits/2026-09-26-trainer-journeys/behavior/skill-sha256.txt
```

Observed **6 tests passed**, including isolated fresh-process use with no repository
or training data; all **30 skill hashes matched**. The assertions use explicit
approved destinations and malformed-input outcomes rather than extracting their
expectations from `ROUTES`. This supports the local exact-routing journey, not a
claim that last month's production incident was repaired.
