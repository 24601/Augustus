# 0.8.0-dev: exercise the installed data-to-decision journey

## Scope and acceptance, fixed before inspecting journey results

Candidate: `5b7610b767c9373cf2d0d25983f0e913f736caae`, on
`research/080-exopo-trainer`. This is development acceptance, not a release or
production deployment. The question is whether fresh agents can use the actual
skills to build task-specific artifacts, not whether Augustus caused an improvement
over an agent without the skill. No with/without effect is claimed.

Three independently owned fresh-agent executions use the same candidate:

- **Binary**: public UCI SMS messages as an application proxy, offline CPU spam
  review, FP cost 5 / FN cost 1. Assemble records, choose candidates, run bounded
  improvement, freeze/evaluate, export and reload. No message deletion.
- **Multiclass**: public CLINC150 as an intent-routing proxy, actual multiple
  intent actions plus out-of-scope/review. Misroute 1 / review 0.3 / correct 0.
  Choose the supported taxonomy before final evaluation; exercise the full path.
- **No training and behavior**: repair an authoritative renewal enum routing
  table and fallback; execute the code. Separately answer seven advisory tasks
  covering data, method choice, asymmetric costs, adaptive reuse, export semantics,
  provider-derived labels and copy-editing. Workers do not receive rubric notes.

The two fits have a 20 CPU-minute search cap each, no rentals or paid calls.
Application datasets are public proxies, not private customer outcomes. Existing
public benchmark access is not secret-label custody. No GPU/platform generality
or general instruction-conditioned Jev-training claim follows.

Requested routing (Amp reports these modes; underlying provider model identity
is not separately attested):
[trainer implementation, high](https://ampcode.com/threads/T-01a0de91-3c25-75c8-bb91-61528214da58),
[scenarios, medium](https://ampcode.com/threads/T-01a0de91-7239-74b8-a09d-2e3b5358a410),
[factual repair, low](https://ampcode.com/threads/T-01a0de91-b8d0-72be-811c-0f79f55ecde4),
[binary execution, medium](https://ampcode.com/threads/T-01a0dea2-cdde-7359-b741-bfafff7e2432),
[multiclass execution, medium](https://ampcode.com/threads/T-01a0dea3-13ff-736c-841e-0145539826c1),
[rules and responses, low](https://ampcode.com/threads/T-01a0dea3-8139-72cd-9086-24469140a8bc).
The coordinator owns integration, replay and semantic acceptance.

Acceptance requires actual, replayable commands and source, data identity and
label/split limitations, real candidate outputs and rejected trials, an evidence-
matched selection decision, and fresh-process inference without retraining.
Inspect independently whether confirmation influenced candidate choice, whether
metrics match the action costs, and whether the exported input/label/policy
contract survives reload and failure inputs. A loss, inconclusive comparison or
incumbent retention is acceptable; invented results or an unexecuted plan is not.
The exact router must preserve approved routes, handle unknown/malformed values,
and demonstrate correction of stale routing without training a ceremonial model.

For advisory responses, use the repository's behavioral rubric: assess concrete
decisions, arithmetic and authority, not phrases. The asymmetric-cost case has
independently calculated expected losses 4.6 versus 16 at probability 0.08,
with equal-loss threshold 5/205. Confidence/shape equivalence, future-data leakage,
and recycling confirmation into an independent claim must not pass.

## Installation and reference smoke, coordinator executed

Exported the candidate with `git archive`, excluding ignored files. In a temporary
`CLAUDE_CONFIG_DIR`, Claude Code 2.1.283 validated the marketplace, added the local
export, installed `augustus@augustus`, and reported **two skills**, zero agents,
hooks, MCP or LSP servers. Skills CLI 1.7.0 `add <export> --list` discovered both;
`add <export> --skill augustus augustus-train --agent codex --copy --yes` installed
them in a separate temporary project. Both installed trees matched all **30**
exported skill files byte-for-byte: zero missing, extra or differing files.

The coordinator also extracted the exact Python blocks from `fit-and-serve.md`
into an isolated scikit-learn 1.7.2 environment: fit six synthetic rows, export,
make fit/development inputs unavailable, and run inference in a new process.
Ordinary, empty, zero-vocabulary and overlong inputs returned the expected statuses
and review fallback. Binary evaluation of two development examples gave costs
0.5 at threshold 0.2 and 0 at 0.4, independently checked from FP/FN counts; the
in-sample-selection warning was present. This is fixture plumbing, not predictive
evidence. One coordinator parsing attempt expected JSON from the evaluator; its
CLI prints text, so the check was corrected to its actual output contract. The
installed example itself ran unchanged.

`make check` on the integrated candidate passed **190 tests**, both numerical
self-tests and shell syntax. Trainer activation graders now require the actual
trainer skill name rather than accepting a main-skill call as equivalent. Paid
Claude plugin activation/with-without evaluation has not been run; package discovery
and explicit fresh-agent use must not be described as implicit activation proof.

The E4c local fixture was adapted to supply the newly required confirmation IDs
for its benign control. `python3 research/080/exp/e4c_local.py` reported seven
active planted exploits refused and the benign control accepted. Historical
receipts were not rewritten; this rerun tests the current helper contract.

## Journey results

All three journeys were executed and replayed by the coordinator:

| Journey | Observed outcome | Evidence |
| --- | --- | --- |
| Binary specialist | Three real fits, selected word TF-IDF/logistic C=8, rejected character challenger; 1,025 fresh-process rows matched. FP 2 / FN 15; group-weighted loss 0.023857 versus 0.107356 for always-ham. Six tests passed. | [Worker recipe](binary/README.md), [coordinator replay](binary/coordinator-replay.md) |
| Multiclass + review | 150 supported intents plus OOS; three fits / 72 policies, selected word+character SVM. All 5,477 fresh-process rows matched; mean loss 0.117966 versus 0.3 review-only. Loss and policy/fallback checks passed. | [Worker recipe](multiclass/README.md), [coordinator replay](multiclass/coordinator-replay.md) |
| No training + behavior | Exact enum routing, six correction/failure/fresh-process tests passed. Seven advisory responses accepted on concrete decisions, arithmetic and evidence limits. | [Raw responses](behavior/responses.md), [coordinator review](behavior/coordinator-review.md) |

The binary refit did not reproduce the original joblib byte hash, although the
selection, split hashes, reported metrics, probe scores and each artifact's own
reload contract matched. The multiclass source has near-duplicate/unknown-family
dependence; its conditional bound is not clean population-generalization evidence.
Both limitations are retained in the replay reports, not hidden by a green status.

**Development acceptance:** the installed skill now guides an executed
data-to-artifact and bounded-improvement path, with export/reload, honest selection
and a no-training result. Source, dependencies and data identities are replayable.
The two public benchmarks test application-shaped plumbing and local model quality,
not deployment effectiveness, broad platform coverage, training a general Jev,
or an improvement caused by the skill versus an unassisted agent. The third journey
is a contract fixture, not production repair. Implicit activation remains unmeasured.
No tag/release or production activation is performed by this audit.
