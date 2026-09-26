# Measurement attempt: blocked on authentication

**Follow-up:** the owner-directed [VibeProxy pilot completed](review.md).
The failed OAuth attempt below remains historical; do not combine it with the
successful run's outcome denominator.

The 0.8.1 release is published; see the
[publication receipt](../2026-09-26-release-081.md). This receipt is **not** an
activation or benefit result.

The [pilot plan](plan.md) and complete suite fingerprints were committed before
inference in [f6839e9](https://github.com/24601/Augustus/commit/f6839e9).
The seven release cases plus four archived additions were prepared against the
exact release export. No prompts or graders were changed after this attempt.

## Observed attempt

Claude Code 2.1.283, 2026-09-26T23:31:25Z. Mac preflight found no Claude login;
the orb had an existing OAuth environment credential. In isolated configuration,
`claude auth status` reported `loggedIn: true`, `authMethod: oauth_token`.
That local report did **not** establish valid provider authentication.

The actual evaluation failed immediately with HTTP 401: OAuth token invalid.
It exited 2, `partial: true`, `partialReason: auth_failed`, reported cost $0,
and elapsed five seconds. The CLI emitted two internal authentication retry
events; the coordinator did not launch another attempt. Both the agent and the
paid judge failed authentication. Only the first case's with-skill arm was
attempted; no successful response, baseline arm, or comparison exists.

[Original result JSON](pilot-auth-failure.json) retains the failure. Its displayed
zero score and failed skill-call grader are **missing evidence**, not failed task
performance or an activation miss. Neither skill benefit nor activation rate can
be estimated from this attempt. No valid outcome denominator exists.

The trace initialization named `claude-opus-5-5`, loaded `.agents` with
`.agents:augustus` and `.agents:augustus-train`, and listed no MCP servers. It also
listed Claude's built-in `agents-md` plugin and built-in skills such as `verify`
and `debug`; a successful follow-up must compare this inventory with the
baseline rather than claim there were literally no other skills. Initialization
is client metadata, not evidence the requested inference model ran.

## Exact attempted command

Working directory: disposable exact release export `/tmp/measure081/source`.
The four added cases were copied into its `tests/plugin-evals` directory so the
relative plugin references resolve to its `.agents`. No normal config changed.

```sh
CLAUDE_CONFIG_DIR=/tmp/measure081/config \
  /tmp/release081-tools/node_modules/.bin/claude plugin eval . \
  --eval-dir tests/plugin-evals --ablation with-without \
  --model claude-opus-5-5 --judge-model claude-haiku-4-5-20251001 \
  --runs 1 --concurrency 1 --max-cost-usd 3 \
  --keep-temp --no-publish --no-scaffold --mocks record --trust-plugin \
  --output-dir /tmp/measure081/results/pilot \
  --json /tmp/measure081/results/pilot.json
```

## Required next action

The owner must refresh the managed Claude OAuth token or provide a valid managed
Anthropic API credential, or authorize an authenticated Claude session on the Mac.
Do not paste credentials into a thread or committed files. Credential presence,
local auth status and supported model names are not live entitlement tests.

After that, run the unchanged bounded pilot once and verify trace isolation,
successful exact skill loads, outcome grading, costs and paired denominators
before considering repetitions or a larger outcome study. Do not silently
switch model identities or label this failed attempt a baseline observation.
