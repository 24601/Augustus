# Augustus 0.8.1-dev: executed repair QA

Reproduced 2026-09-26 against [candidate 233c76a](https://github.com/24601/Augustus/commit/233c76a6681a1b8e54ebc1b2b79156638d64f62b).
This is application-fixture and local-install evidence, not a production-model
benchmark, automatic-activation result, or skill-versus-no-skill experiment.
No installed behavior changed during this QA; the last published release remains
0.8.0. Publishing 0.8.1 and checking its remote tag are separate work.

## Outcome

Both fresh agents used installed copies of the exact candidate. They repaired all
five injected defect categories: missing encoder optimizer ownership, hardened
soft targets, omitted required calibration, unattainable/nonmonotone threshold
selection, and stale hardcoded routing. Real CPU fitting, actual backward/step,
fresh-process inference, fail-closed startup, and authoritative-map recovery ran.
The coordinator replayed both workers' tests and the separately held grader.

| Check | Observed result |
| --- | --- |
| `make check` | 192 tests, both self-tests, structural and shell checks pass |
| Frozen grader on original fixtures | 6 failures; 3 byte-preservation checks pass |
| Frozen grader on repairs | 8 pass; 1 byte-preservation failure retained |
| Valid original acceptance checks | All 8 pass, without modifying the grader |
| Post-result Decimal adjudication | Discovered control defect and repair verified |
| Worker training tests, coordinator replay | 3 methods pass, including real convergence and mode transitions |
| Worker serving tests, coordinator replay | 6 methods pass, including 1,364 exhaustive threshold combinations |
| Installed file hashes | Both workers' 30 files match exact exported candidate |

The ninth original check was **invalid**, not silently made green. The serving
worker found that the supposedly correct control subtracts opposite maximum
finite floats before temperature scaling, overflowing to negative infinity.
For logits `[-float_max, float_max]`, temperature `float_max`, levels `[0,4]`,
and threshold 3.8, it returns `[0,1]` and acts. Correct probabilities are about
`[0.119203,0.880797]`, requiring review. The worker repaired this in both serving
paths. A separately written coordinator Decimal oracle confirms the defect and
repair, including reversed/equal logits and subnormal temperature. Original
fixtures, frozen grader, and failing output remain intact. This is not a third
successful unchanged control: only training and routing are valid unchanged
controls. No installed Augustus code had this fixture bug.

## Independence and provenance

- [Training worker](https://ampcode.com/threads/T-01a0dfe4-e562-759d-830a-0043f12316f6):
  medium requested; isolated Claude Code 2.1.283 plugin installation. See
  [report](training/REPORT.md), inventory, source, independent tests and hashes.
- [Serving/routing worker](https://ampcode.com/threads/T-01a0dfe5-33d3-7047-baf0-3675fb9a8ab8):
  medium requested; Skills CLI 1.7.0, scratch Codex installation. See
  [report](service/REPORT.md), source, independent tests and hashes.
- These are Amp agents reading installed guidance, not Claude/Codex inference
  runs. Runtime model identity was not independently attested. No paid provider
  evaluation, GPU training, or automatic skill-selection measurement ran.
- Workers received application contracts and fixtures, not coordinator tests or
  expected scenario notes. Repository-test/audit restrictions were prompt-level,
  not an enforced filesystem sandbox. The uncommitted grader was not transferred
  into their separate orbs. Its baseline ran and hash was recorded before the
  coordinator read worker outcomes; that is not a timestamped external commitment.
- Frozen `grade.py` SHA-256:
  `b5a627cefb7d3ea9030562b1bc95c312a587502e6b76bb72ea719f9a8ba713ce`.
  [Baseline](baseline.txt), [unmodified acceptance result](acceptance.txt),
  [eight valid checks](valid-acceptance.txt), and
  [post-result adjudication](control-adjudication.txt) distinguish each stage.
- Downloaded training result archive SHA-256:
  `bed170ca7661c239d2a4bf441f78a5c3791bc259389423df1d4ec154962778f7`;
  serving archive: `8d1600ae00717657481670b27a5a33b1d376d26140a303166983d34e87081bf0`.
  Both verified before extraction. Sources and receipts, not archives, are kept.
  Raw worker logs and `repairs.diff` retain trailing spaces emitted by unittest
  and unified-diff context lines; unrestricted `git diff --check` flags those.
  Source and documentation whitespace checks pass; raw evidence is not rewritten.
- Coordinator also validated and installed the exact export with Claude Code
  2.1.283 in isolated configuration: two skills, no agents/hooks/MCP/LSP;
  recursive installed `.agents` comparison found no differences. Worker hashes
  independently matched the coordinator's candidate export (30/30 each).

## Replay

Python 3.11.6 and CPU Torch 2.14.0+cpu were used. Repository checks additionally
use the pinned root development requirements. No NumPy is needed by these
tensor-only tests; Torch's missing-NumPy warning is retained, not suppressed.
Training dependency versions are in `training/requirements.lock`.

From the repository root, with dependencies installed:

```sh
Q=research/audits/2026-09-26-trainer-081-qa
python3 -B "$Q/training/test_contract.py"
python3 -B "$Q/service/test_repair.py"
python3 -B "$Q/check_control.py"
S=$(mktemp -d)
cp "$Q"/training/training*.py "$Q"/service/{service,service_control,routing,routing_control}.py "$S/"
# Expected exit 1: six original failures.
python3 -B "$Q/grade.py" "$Q/fixtures"
# Expected exit 1: invalid unchanged-service assertion, retained intentionally.
python3 -B "$Q/grade.py" "$S"
# All eight valid original checks; separate from the post-result adjudication.
python3 -B "$Q/grade.py" "$S" \
  Acceptance.test_optimizer_membership_and_actual_updates \
  Acceptance.test_soft_target_objective_gradient_and_fit \
  Acceptance.test_calibration_and_fresh_process_actions \
  Acceptance.test_required_calibration_refuses_missing_and_invalid \
  Acceptance.test_attainable_thresholds_against_exhaustive_policy_oracle \
  Acceptance.test_authoritative_mapping_and_recovery_without_training \
  Acceptance.test_correct_training_unchanged \
  Acceptance.test_correct_routing_unchanged
rm -r "$S"
make check
```

The fixtures are intentionally broken historical inputs, not shipped runtime.
These extra Torch application checks are explicit replay commands, not hidden
dependencies of `make check`. Passing them supports the bounded claim that
installed guidance can be used to diagnose and repair these applications. Two
agents and small deterministic tasks cannot establish general model-selection
quality, causal skill benefit, or production readiness for an arbitrary task.
