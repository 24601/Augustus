# Independent redo: repository quality and packaging

Date: 2026-09-22. Disposition: **fix-first for the structural checker**;
the inspected development package passes the local installation checks.
No architectural rethink is indicated. This is a fresh inspection and set
of executions; earlier agent reports were not used as acceptance evidence.

Requested routing: `gpt-6-astra`, `xhigh`. No tool exposed an independently
verifiable actual model identity or reasoning-effort value to this worker.

## Scope and provenance

- Checkout: `/Users/basitmustafa/Developer/Augustus`, branch
  `refresh/2026-09-22`, HEAD `192faf0d18d511154228af8ac40e1393567d828c`.
- Before-session comparison base supplied by coordinator:
  `0b43a8d3b8d2d389b59415747f566dcbaa3f3ec8`. The checker, its tests,
  compatibility tests, Makefile, quality workflow, and OpenAI metadata are
  additions since that base. They have no working-tree difference from
  the `v0.6.0` HEAD during this inspection. Runtime guidance and marketplace
  version include uncommitted `0.6.1-dev` changes.
- Read `AGENTS.md`, `CONTRIBUTING.md`, `research/protocol.md`, its fold prompt,
  the complete skill entry point, checker, checker tests, compatibility
  entry point/tests, metadata, Makefile, quality workflow, and release
  checklist. The Augustus placement workflow does not turn this maintenance
  check into a model-placement task.
- Only this report was added to the repository by this worker. Probe
  programs, generated fixtures, proposed code, Python environments, and
  Claude configuration are isolated under
  `/tmp/augustus-astra-quality.8dMSGr`. That directory is temporary, not a
  durable release artifact. Reproduction inputs and patch are retained below.
- No credential reads, provider inference, paid search, outreach, commits,
  pushes, releases, or normal user plugin configuration changes were made.

Content identity when probed:

| File | SHA-256 |
| --- | --- |
| `scripts/check_repo.py` | `23eea1604b6f738fcbc69ace938f00c58b8f89cb6b9c4f86eaa192261a147253` |
| `tests/test_check_repo.py` | `44ba076c84f1e4873c888cb9ee0b2345bbfd3dc6da75fc9be6c52973667cbf29` |
| `tests/test_compatibility_entrypoint.py` | `850abf00a55b0bdbde816413468b78172041570e7f4a3fa430a3b7353199513f` |
| `.agents/skills/augustus/SKILL.md` | `02010e755cbfd3d4e34946bb5d99d651151575a07ab3efca06668c1c46ebf2c1` |
| `.claude-plugin/marketplace.json` | `ee5950e33152eb78ed04d34c2d4bb63881b0abb4fcfe65ed33c0ba61f84fc535` |

## Actual invariants and current results

The checker parses frontmatter and JSON/YAML metadata, validates selected
field types, compares skill and marketplace versions, resolves marketplace
source/skill paths, checks selected Markdown links and headings, and bounds
entry-point/reference size. These are structural invariants. Neither this
check nor successful installation establishes guidance quality, activation
quality, a released version, or deployed Pages behavior.

Current skill/marketplace version is `0.6.1-dev`. README distinguishes it
from published `0.6.0`; retaining the old release notes is correct. OpenAI
metadata contains one interface with the `$augustus` prompt. No assets or
implicit-invocation override are currently declared.

The entry point is 9,071 UTF-8 bytes and 155 lines against 16,000/220 limits.
There are 17 reference cards totaling 164,846 bytes against 180,000.
Largest card: `judgment-class.md`, 14,423 bytes; maximum reference line
count: 259. Every current card is directly declared by the entry point.
No limit increase is needed.

| Execution | Observed result |
| --- | --- |
| `make check` with Python 3.14.7 | Pass: 53 tests, repository checker, both self-tests, shell syntax |
| `make check PYTHON=/tmp/augustus-astra-quality.8dMSGr/py311/bin/python` | Pass: same checks, Python 3.11.16, PyYAML 6.0.2 |
| `make check PYTHON=/tmp/augustus-astra-quality.8dMSGr/py312/bin/python` | Pass: same checks, Python 3.12.13, PyYAML 6.0.2 |
| `claude plugin validate .` | Pass, Claude Code 2.1.278 |
| Isolated local marketplace add/install/details | Version 0.6.1-dev; one skill; zero agents, hooks, MCP servers, LSP servers |
| Installed evaluator with `python3 -I`, `--self-test` and `--help` | Both pass from outside the repository |
| Installed compatibility entry point with `python3 -I` | Expected exit 1 and explicit repository-maintainer explanation; no traceback |
| `diff -qr` between skill source and installed skill | No differences at inspection time |
| Independent `markdown-it-py` 4.0.0 CommonMark parse | All 36 local links in 18 runtime Markdown files resolve inside the skill, in both source and installed copies |
| `git diff --check` | Pass |

The first attempts using globally available Python 3.11/3.12 failed because
those interpreters lacked PyYAML. Fresh temporary environments were then
created with `uv venv --python <interpreter> <temporary-environment>` and
`uv pip install --offline --python <temporary-environment>/bin/python -r
requirements-dev.txt`. The cached pinned dependency installed successfully.
The subsequent passes are local macOS executions of both CI Python versions;
they are not claims about GitHub Actions runs or Linux behavior.

The Makefile and quality workflow cover the same checks. CI declares Python
3.11/3.12, read-only repository permission, and pull-request/main-push
triggers. Rendered-site checks are in the separate Pages workflow. The
package install is an explicit release check, not an automatic quality-CI
step. Existing checker unit tests are useful but did not exercise the
failures below; their path-escape fixtures used `../...`, which is rejected
before the containment branch, rather than `./../...` or a symlink escape.

## Reproduced defects

All rows below use an otherwise-valid generated repository, not changes to
the current runtime. These are checker defects, not observed broken links
or excessive reference sizes in the current package.

| Priority / location | Counterexample and observed behavior | Required correction |
| --- | --- | --- |
| P2, `_check_links` / runtime callers, lines 164-181, 193, 477 | Entry point `[repo-only](../../../README.md)` passes with zero issues while the referenced file is absent after copying the installed skill. A reference-card link to `../../../../README.md` also passes. | Bound runtime links to the installed skill directory; keep repository documents bounded to the repository. |
| P2, reference inventory, line 464 | A linked `references/nested/guide.md` containing 181,000 extra characters and `[missing](missing.md)` passes with zero issues. An unlinked nested card also passes. | Inventory reference cards recursively, or explicitly reject nested runtime cards. Checking only top-level glob results cannot enforce the stated per-card/aggregate budgets. |
| P2, fenced-code closing, line 101 | A line beginning with triple backticks followed by `not-closing` is treated as a closing fence. A later real closing fence reopens the scanner's code state, so a visible broken link is missed. The reverse arrangement reports a link that is still inside code. | Require a closing fence's remainder to contain only whitespace. |
| P3, `SEMVER_RE`, line 34 | `01.2.3`, `1.2.3-01`, and `1.2.3-.` pass. Valid `1.2.3-alpha+build` fails. | Validate numeric identifiers, prerelease identifiers, and build metadata separately. |
| P3, error reporting, lines 61-68 / 158 | A directory at `SKILL.md` raises `IsADirectoryError`; `[bad](https://[broken/path)` raises `ValueError`. | Return structured issues for unreadable required paths and malformed URL syntax. These failures currently fail CI rather than falsely pass, but bypass aggregate diagnostics. |

The fence behavior was checked against an independent CommonMark parser:

````text
```md
```not-closing
```
[visible missing](missing.md)
````

`markdown-it-py` parses one link to `missing.md` in this input; the original
checker returns no issue. Its rendered output has a code block containing
the `not-closing` line, followed by the visible link. This is a parser
boundary discrepancy, not a phrase-matching test.

Additional negative checks behaved correctly: percent-encoded repository
escape, symlink link escape, marketplace `./../...` source escape, source
symlink escape, skill-path traversal, UI asset symlink escape, malformed
YAML, YAML sequences, unknown YAML tags, unclosed frontmatter, malformed
OpenAI YAML, invalid UTF-8, exact/over-limit entry-point bytes and lines,
multibyte UTF-8 byte budgets, and a 401-line reference. Conventional angle
destinations, balanced destination parentheses, normal fences, and inline
code behaved as expected.

## Exact proposed correction

The following patch was applied only to a temporary checker copy. Sixteen
focused fixture expectations then passed, the current repository passed
the proposed checker, and all 53 existing tests passed when the proposed
module replaced `scripts.check_repo` in the test process. The subprocess
compatibility test still runs the repository's original entry point, so
that run does not by itself verify an integrated patch. Integration must
add regression cases and rerun `make check`.

```diff
--- a/scripts/check_repo.py
+++ b/scripts/check_repo.py
@@
-SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
+SEMVER_NUMBER = r"(?:0|[1-9][0-9]*)"
+SEMVER_PRERELEASE = r"(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
+SEMVER_RE = re.compile(
+    rf"^{SEMVER_NUMBER}\.{SEMVER_NUMBER}\.{SEMVER_NUMBER}"
+    rf"(?:-{SEMVER_PRERELEASE}(?:\.{SEMVER_PRERELEASE})*)?"
+    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
+)
@@
     except UnicodeDecodeError:
         _issue(issues, "invalid-utf8", path, "must be UTF-8 text")
+    except OSError as exc:
+        _issue(issues, "unreadable-file", path, f"cannot read required text file: {exc.strerror}")
@@
-            if found and found.group(1)[0] == fence[0] and len(found.group(1)) >= fence[1]:
+            if (
+                found and found.group(1)[0] == fence[0]
+                and len(found.group(1)) >= fence[1]
+                and not line[found.end():].strip()
+            ):
@@
-def _check_links(root: Path, path: Path, text: str, issues: list[Issue]) -> set[Path]:
+def _check_links(root: Path, path: Path, text: str, issues: list[Issue], *, boundary: Path | None = None) -> set[Path]:
+    allowed_root = (boundary if boundary is not None else root).resolve()
     targets: set[Path] = set()
     for line, destination in _markdown_destinations(text):
-        local = _local_destination(destination)
+        try:
+            local = _local_destination(destination)
+        except ValueError as exc:
+            _issue(issues, "broken-link", path, f"line {line} has invalid URL: {exc}")
+            continue
@@
-            candidate.relative_to(root)
+            candidate.relative_to(allowed_root)
         except ValueError:
-            _issue(issues, "broken-link", path, f"line {line} escapes repository: {destination}")
+            _issue(issues, "broken-link", path, f"line {line} escapes allowed content root: {destination}")
@@
-        target for target in _check_links(root, skill_path, text, issues)
+        target for target in _check_links(root, skill_path, text, issues, boundary=skill_path.parent)
@@
-    all_references = set(reference_root.glob("*.md")) if reference_root.is_dir() else set()
+    all_references = set(reference_root.rglob("*.md")) if reference_root.is_dir() else set()
@@
-        _check_links(root_path, reference, reference_text, issues)
+        _check_links(root_path, reference, reference_text, issues, boundary=skill_path.parent)
```

Regression expectations to preserve in `tests/test_check_repo.py`:

| Fixture | Expected codes after correction |
| --- | --- |
| Entry-point or reference link to existing repository-only README | `broken-link` |
| Linked nested 181,000-character card plus missing link | `size-budget`, `reference-total-budget`, `broken-link` |
| Unlinked nested reference | `unreferenced-reference` |
| Non-closing fence followed by true close and visible missing link | `broken-link` |
| Missing-link example inside a still-open fence | No issue |
| `01.2.3`, `1.2.3-01`, `1.2.3-.` in both version fields | `skill-version`, `marketplace-version` |
| `1.2.3-alpha+build`, `1.2.3+build`, `1.2.3-dev` | No issue |
| Directory at required text-file path | `unreadable-file` |
| Malformed bracketed URL host | `broken-link` |

## Packaging commands and boundary

Commands executed from the temporary directory, with each CLI invocation
receiving these environment variables:

```text
CLAUDE_CONFIG_DIR=/tmp/augustus-astra-quality.8dMSGr/claude-config
DISABLE_TELEMETRY=1
DISABLE_ERROR_REPORTING=1
CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
```

```bash
claude plugin marketplace add /Users/basitmustafa/Developer/Augustus --scope user
claude plugin install augustus@augustus --scope user --json
claude plugin details augustus@augustus
```

The install reported `outcome: ok`. Files were installed under
`claude-config/plugins/cache/augustus/augustus/0.6.1-dev/skills/augustus`.
The local source copy included ignored `__pycache__` files from test runs;
none are tracked. This is a local working-tree install, not proof of a clean
remote-tag install. Normal user plugin settings were not used as the target.

The repository-only `uniqueness_gate.py` intentionally refuses installed
use with a clear message. The installed `evaluate_decisions.py` is usable
without PyYAML or repository imports; its deeper arithmetic acceptance is
outside this subtask. Neither CLI invocation performed model inference.

## Remaining limits and acceptance decision

The bounded scanner still does not validate reference-style links, images,
or fragments. Reference-style exclusion is documented; image/fragment and
escape/comment handling should also be described precisely. For example,
an escaped `\[example](missing.md)` produces a false positive and a reference
path written only inside an HTML comment counts as a declaration. Duplicate
YAML keys silently use the last value, following PyYAML's default loader.
The proposed patch deliberately does not claim a full Markdown parser or
strict duplicate-key YAML loader. None of these remaining forms invalidate
the actual runtime links checked independently above.

This redo establishes a working local package and reproducible defects in
its future-regression checks. Integrate the P2 corrections with meaningful
negative tests before accepting the checker as the release gate; the P3
corrections are included in the same tested proposal. The coordinator owns
the final integrated diff, fresh behavioral acceptance, release version,
exact tagged install, actual CI, and publication/deployment read-back.
