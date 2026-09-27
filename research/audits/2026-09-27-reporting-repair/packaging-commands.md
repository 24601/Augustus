# Offline Claude packaging verification

Candidate archive SHA-256:
`559dc419c9adcf11befc716c1cc4243ad5ba7b1e524f865a2e4d575017d6a5a0`.
All operations were confined to this disposable evidence directory. No inference,
normal configuration writes, publication, push, or prior behavioral-output reads.

Commands executed from this directory after safe archive extraction:

```sh
cli() {
  env -i PATH=/usr/bin:/bin HOME="$PWD/home" \
    CLAUDE_CONFIG_DIR="$PWD/config" TMPDIR="$PWD/tmp" \
    CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1 DISABLE_AUTOUPDATER=1 \
    /Users/basitmustafa/.local/share/claude/versions/2.1.282 "$@"
}
cli plugin validate "$PWD/candidate/.claude-plugin/marketplace.json"
cli plugin marketplace add "$PWD/candidate"
cli plugin install augustus@augustus --scope user --json
cli plugin details augustus@augustus
```

All exited 0. Details reports **augustus 0.8.2-dev**, two skills (`augustus`,
`augustus-train`), zero agents/hooks/MCP/LSP servers. The user scope is inside
the isolated HOME/config, not the user's normal configuration.

Read installPath from isolated `config/plugins/installed_plugins.json`:

```sh
TRAINER="$PWD/config/plugins/cache/augustus/augustus/0.8.2-dev/skills/augustus-train"
# Both invocations used an empty inherited environment, local HOME/TMPDIR,
# PATH=/usr/bin:/bin and PYTHONDONTWRITEBYTECODE=1.
/opt/homebrew/bin/python3 "$TRAINER/scripts/policy_receipt.py" --help
/opt/homebrew/bin/python3 "$TRAINER/scripts/policy_receipt.py" policy-input.json
```

The JSON fixture was extracted from the installed `references/fit-and-serve.md`
JSON fence containing `population`; it was not taken from prior experiment
outputs. Help and fixture execution exited 0. Baseline independently asserted:
**n=3, positive_actions=1, FP=0, FN=1**, action rate 1/3, mean loss 8/3.
Receipt input hash matches the actual fixture bytes.

All **31 installed files match the candidate byte-for-byte**, including the
trainer helper and reference. `verification-receipt.json` contains complete
candidate/install filename-to-SHA256 maps. Logs and fixture output are adjacent.

Important hashes:

- Installed helper: `6bafc5ae4fd33cc0d969924f987cc045b202a4d2da3fffc61b6479bd225d778e`
- Installed fit-and-serve: `5ade9865a8df7c3e7674df15f9187238a516f94e1af6ac0798deff3aa66288a3`
- Marketplace: `cf044c0f8fbce53497c1d8de95d260a0496e49ba8bdedcc8d7dae2eec1a1e54c`
- Extracted fixture: `c55b3aae0534073c000dc8e634e77c33df5fb99337acdedf86e82034bd91ba08`
