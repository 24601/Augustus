# Isolation qualification: the channel is sensitive, and the baseline is clean

Before spending on comparison inference, the Mac runner captured **complete
request bodies** from the exact Claude Code 2.1.282 build against offline mock
endpoints. No provider inference or configuration change occurred. Evidence:
`isolation-qualification.tar.gz`, SHA256
`861a63b7a88317eef74ab680499943c2c45304edf11418386b5ee18e189867b1`, 84 files.

A negative result is only meaningful if the instrument can detect a positive, so
sentinels were planted in **disposable synthetic** user-config, ancestor
`CLAUDE.md` and ancestor `AGENTS.md` locations. Your real global configuration
was never modified.

| Condition | Sentinel or Augustus text in the actual request | Reading |
| --- | --- | --- |
| Baseline, harness flags | absent from system, messages and tool schemas | control is clean |
| Explicit plugin arm | descriptions listed first; bodies appear only after each load | treatment is delivered |
| Relaxed sources, ancestor `CLAUDE.md` | present | channel is sensitive |
| Relaxed sources, ancestor `AGENTS.md` | present | channel is sensitive |
| Relaxed sources, config-dir skills | real `augustus` description present | channel is sensitive |

The last row **corrects an earlier claim** from the preceding investigation that
the config-directory skill channel showed no sensitivity. It does. The operative
control is `--restricted` with empty setting sources, not the environment
variables alone. The ineffective managed-settings override was dropped from the
isolation claim and a test now enforces its absence; both standard managed paths
were absent and unchanged before and after.

Every arm receives an identical 3,936-byte system prompt, an identical 7-tool
schema set including a byte-identical `Skill` schema, and one user message whose
only added content is a git-attribution reminder. **"Without Augustus" is
accurate; "without any skills" is not** — Claude's bundled skills are listed in
all arms and are guard-denied when invoked.

## Defects found and repaired before any paid run

An oracle review of the runner's new outer OS fence caught two real problems:
nesting Seatbelt broke the Python tool sandbox and would have failed every Bash
call in a paid run, and staging plugin snapshots under arm-named directories
leaked arm identity into the prompt through `--add-dir`. Both are fixed: the
outer fence is reverted, snapshots stage to a neutral runtime path, and the
harness now fails closed on missing guard coverage, checks task-file integrity,
asserts in-sandbox network and home denial, and asserts request headers carry
only the placeholder bearer token.

## Accepted residuals

- **CLI egress is environment-scoped, not OS-enforced.** Captured headers show
  only the placeholder credential, but this is configuration, not a kernel fence.
- **The proxy's OAuth route is uncharacterized.** With a synthetic API key the
  disposable backend forwarded the captured body with byte-identical system and
  message content and no changed top-level keys. The OAuth path first fetches a
  profile from the real provider host, which the offline test blocks, so that hop
  was never exercised. The binary carries cloaking and system-prompt-collection
  symbols.

Both residuals are **arm-independent**: they can shape the absolute prompt every
arm receives, but cannot differentially contaminate one arm. That is sufficient
for an incremental comparison and insufficient for any claim about absolute
prompt content. Proxy processes restart per attempt so cross-run state is
excluded by construction rather than argued.
