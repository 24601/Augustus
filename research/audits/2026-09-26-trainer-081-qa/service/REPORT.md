# Bounded application repair — Augustus 0.8.1-dev

## Scope and decision

Used the exact export of [233c76a6681a1b8e54ebc1b2b79156638d64f62b](https://github.com/24601/Augustus/commit/233c76a6681a1b8e54ebc1b2b79156638d64f62b).
Installed both skills into a new, empty scratch project with Skills CLI 1.7.0,
target Codex, telemetry disabled. Read those installed files, not workspace skill
copies. No model, training, paid calls, deployment, commits, pushes, nested
threads, or callback messages. All application behavior here is exact arithmetic
or an authoritative lookup; a model would add no value.

Acceptance: required positive finite non-bool temperature must load and affect
the distribution and action; invalid/missing required temperature refuses load;
non-required calibration stays raw; threshold selection maximizes attainable
empirical coverage; routing obeys the supplied mapping and malformed/unknown
records fall back to operations. Function signatures and JSONL serving remain.
Reject any repair that changes those semantics or breaks a previously correct
case. This is a local contract-fixture result, not evidence of calibration quality,
population risk, certification, or production activation.

## Findings and repairs

- `service.py`: added required-temperature validation and temperature-scaled
  inference. Kept strict `expected > threshold`. The original produced expected
  score 3.6 instead of 3.0 on logits `[0, log(9)]`, levels `[0,4]`, temperature 2;
  this changes the action at threshold 3.2.
- `service.py`: threshold sweep evaluates complete equal-score groups and keeps
  scanning after risk violations. An error at the highest score can be diluted
  by later correct rows; equal scores cannot be split by a threshold. The initial
  tie case selected coverage 0.5 even though the returned threshold accepted both
  rows. No feasible nonempty set returns threshold null, coverage 0, risk null.
- `routing.py`: load the approved JSON file instead of hardcoded destinations.
  The independent fixture changes renewal to legal and adds audit → compliance.
- `service_control.py`: normal calibration behavior was already correct, but the
  finite-input contract exposed an actual overflow defect. With logits
  `[-sys.float_info.max, sys.float_info.max]` and temperature `sys.float_info.max`,
  subtraction overflow yielded probabilities `[0,1]` instead of approximately
  `[0.1192029220,0.8807970780]`. Levels `[0,4]`, threshold 3.8 falsely selected act.
  Both inference implementations now subtract first normally, scaling first
  only when the subtraction overflows. This is a demonstrated contract repair,
  not cleanup of a supposedly correct control. Baseline failure is preserved.
- `routing_control.py`: **unchanged, byte-identical** to the supplied archive;
  its authoritative loading and fallback behavior already satisfy the contract.
  SHA-256: `bb17b1e236fe82eda443ce2db5141c36c25dc5b08ed83b25e71236a620172224`.

## Independent verification

`python3 -B test_repair.py`: six test methods passed. The threshold test checks
1,364 exhaustive combinations (0–4 rows over two scores and binary errors, four
risk caps), deriving expected results by enumerating actual accepted sets rather
than duplicating prefix accumulation. Other tests cover rejected temperatures,
raw mode, ordered levels, strict boundary/equality, maximum finite logits,
subnormal temperature, changed and empty route maps, malformed records, and
fresh-process JSONL inference plus fail-closed startup for both service modules.

Before changes: six methods ran, 16 assertion failures including subtests.
After changes: six methods ran, all passed. See `baseline-tests.txt` and
`final-tests.txt`. Fresh-process tests run in a temporary directory with only the
JSON bundle, without training data. Additional replay fixtures `bundle.json` and
`inputs.jsonl` produce `decisions.jsonl` and `control-decisions.jsonl` with actions
review, review, act and equal results across both implementations.

No repository tests, scenario expectations, research audit files, or parent grader
were read. `make check` was not run: this isolated application uses the independently
written tests instead of the repository test suite. Installed references read:
`augustus/references/boundary-audit.md`, `augustus/references/validation.md`,
`augustus-train/references/fit-and-serve.md`, and
`augustus-train/references/spec-defects.md`. The latter is an installed runtime
reference; its linked historical research was not opened.

## Installation provenance and commands

Archive retrieved with `download_thread_file` from parent
`T-01a0d176-6c28-75e9-a727-f948d3747917`, path `.local/qa081/service.tar.gz`,
saved as `/tmp/qa081-service.tar.gz`. Verified SHA-256:
`01cbe5140d85ceec27b2a7c36c26959c5d5fbb90f3f2b1080adec44119f93dfa`.

Commands (working directories specified below):

```sh
# Repository root; scratch directories were new and empty.
mkdir -p /tmp/qa081-export /tmp/qa081-install
git archive 233c76a6681a1b8e54ebc1b2b79156638d64f62b | tar -x -C /tmp/qa081-export
sha256sum /tmp/qa081-service.tar.gz
tar -tzf /tmp/qa081-service.tar.gz
mkdir qa-service
tar -xzf /tmp/qa081-service.tar.gz -C qa-service

# /tmp/qa081-install
DISABLE_TELEMETRY=1 DO_NOT_TRACK=1 npx -y skills@1.7.0 add /tmp/qa081-export --skill augustus augustus-train -a codex -y
DISABLE_TELEMETRY=1 DO_NOT_TRACK=1 npx -y skills@1.7.0 --version
cat .agents/skills/augustus/SKILL.md .agents/skills/augustus-train/SKILL.md
cat .agents/skills/augustus/references/boundary-audit.md .agents/skills/augustus/references/validation.md .agents/skills/augustus-train/references/fit-and-serve.md .agents/skills/augustus-train/references/spec-defects.md
diff -qr /tmp/qa081-export/.agents/skills .agents/skills
find .agents/skills -type f -print0 | sort -z | xargs -0 sha256sum > /home/user/workspace/repo/qa-service/installed-skill-sha256.txt

# qa-service; baseline before patching, final after patching.
python3 -B test_repair.py > baseline-tests.txt 2>&1
python3 -B test_repair.py > final-tests.txt 2>&1
python3 -B service.py bundle.json < inputs.jsonl > decisions.jsonl
python3 -B service_control.py bundle.json < inputs.jsonl > control-decisions.jsonl
cmp decisions.jsonl control-decisions.jsonl
```

Installation reported two skills copied to `.agents/skills/`, targeting Codex.
The post-install recursive comparison against the exact export found no differences.
`installed-skill-sha256.txt` records all 30 installed files. Entry-point SHA-256:

- augustus: `afb92f55d3274debe4643e9de488946841e67f90df8ef6904a15ef82d2438ba4`
- augustus-train: `35a874a8f04bef217e4b556342d3f910d37a55e456c86f7c1557ae7748a590ea`

Observed versions: Skills CLI 1.7.0; Node v26.10.0; npm 10.9.9; Python 3.11.6;
Git 2.55.0; Linux x86_64. Python tests and serving use only the standard library.
Implementation changes are recorded in `repairs.diff`; final source/test/fixture
hashes are in `application-sha256.txt`. Local files are ready for parent download;
there are no commits or external changes.
