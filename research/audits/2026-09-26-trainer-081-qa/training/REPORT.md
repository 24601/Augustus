# Bounded training repair — reproduced fixture evidence

Applied Augustus 0.8.1-dev from [exact candidate commit](https://github.com/24601/Augustus/commit/233c76a6681a1b8e54ebc1b2b79156638d64f62b).
Only `training.py` required repair. Callable signatures are unchanged.
`training_control.py` passed before any repair and remains byte-identical (`cmp`
exit 0); SHA-256 `ad7e109f0e94e39f4b5a433bdbbf2a22b904cfeaf99bfe83e38fbdec9479cd92`.

## Actual behavior and repair

- Before: `tune_encoder=True` produced finite nonzero encoder gradients but
  exactly zero encoder movement: SGD only owned head parameters. Now SGD owns
  all trainable parameters. On the first checked batch, maximum absolute encoder
  weight change was 0.004096255845722818 and head weight change 0.03351399540618269.
  False mode leaves encoder exactly unchanged while head moves. True→False→True
  transitions pass on both implementations.
- Before: `soft_loss` thresholded probability mass into hard labels. Actual
  backward disagreed with independent scalar-calculus expectations on 3/5 entries
  (largest error 0.1). Now BCE receives the supplied probability mass unchanged.
  Loss 0.4250497651507345 and gradients match the independent oracle to 1e-12.
- Actual `DecisionModel → soft_loss → backward → make_optimizer.step` training,
  600 steps per configuration, CPU float64, seeds set before construction:
  target 0.30 previously yielded 0.0054438274; target 0.73 yielded 0.9946469741.
  Repaired and control models converge to 0.30 and 0.73 within 1e-5 in both
  modes; final losses match binary entropy within 1e-9. This is a known-optimum
  diagnostic, not a generalization/calibration or product-quality claim.

`test_contract.py` was written independently before changing either fixture.
Before: 3 test methods, 7 failing subtests, all in `training` (`before.txt`).
After: same tests, 16 parameterized cases, all pass in 4.901s (`after.txt`).
No model/provider call, GPU dependency, new model, calibration or cleanup needed.

## Isolated installation and skills actually read

Scratch root `/tmp/qa081-application`; `CLAUDE_CONFIG_DIR` was its `config/`
directory for every Claude invocation. Claude was installed by npm into `tool/`.
Installed plugin inventory: augustus and augustus-train; zero agents, hooks,
MCP servers and LSP servers. See `inventory.txt`. Recursive comparison of the
installed package with the exact commit's exported `.agents` returned no diff.

Read the **installed** copies under
`config/plugins/cache/augustus/augustus/0.8.1-dev/skills/`, not workspace skills:

| Read file | Actual installed SHA-256 |
| --- | --- |
| augustus/SKILL.md | afb92f55d3274debe4643e9de488946841e67f90df8ef6904a15ef82d2438ba4 |
| augustus-train/SKILL.md | 35a874a8f04bef217e4b556342d3f910d37a55e456c86f7c1557ae7748a590ea |
| augustus/references/boundary-audit.md | 00135dce79a4f5cb366619d931072fd211deb86244e0c66c0119fc3e52ad2c14 |
| augustus-train/references/fit-and-serve.md | f180a90ecec7031a4cd2be8401720872f09b1307c281ab5ab50a46faa5df128d |
| augustus-train/references/spec-defects.md | 245a9d13bcd4d22bc9806db1b4c8947db307028719f92a15125bab11ec94234e |

`installed-files.sha256` includes hashes for every installed file (hashing does
not mean all files were read). The boundary audit kept this exact contract in
code; fit-and-serve supplied the parameter-ownership and actual soft-target
training probes. No repository tests, skill_cases, research audits or parent
acceptance tests were read. Repository CONTRIBUTING and the required generic
building-skills guidance were read; no links to excluded evidence were followed.
No Claude inference/eval was run: installation and inspection are not proof of
automatic skill activation by Claude. This agent applied the installed guidance.

## Commands and environment

Parent fixture was obtained with `download_thread_file` from
`.local/qa081/training.tar.gz`. SHA-256 verified before extraction:
`ffcdfa50b56383797adae91a86c45db2e1c4eca8c00abad0a5d6a0a0aaf210e2`.

```sh
mkdir -p /tmp/qa081-application/{export,config,tool}
git archive 233c76a6681a1b8e54ebc1b2b79156638d64f62b | tar -x -C /tmp/qa081-application/export
npm install --prefix /tmp/qa081-application/tool @anthropic-ai/claude-code@2.1.283
export CLAUDE_CONFIG_DIR=/tmp/qa081-application/config
C=/tmp/qa081-application/tool/node_modules/.bin/claude
"$C" --version
"$C" plugin marketplace add /tmp/qa081-application/export
"$C" plugin install augustus@augustus
"$C" plugin list
"$C" plugin details augustus@augustus
mkdir -p qa-training
tar -xzf /tmp/qa081-training.tar.gz -C qa-training
uv venv /tmp/qa081-application/venv
uv pip install --python /tmp/qa081-application/venv/bin/python torch --index-url https://download.pytorch.org/whl/cpu
PYTHONDONTWRITEBYTECODE=1 /tmp/qa081-application/venv/bin/python qa-training/test_contract.py
```

The final command was run before and after repair with stdout/stderr saved.
For another machine, use `requirements.lock` with the same CPU index.
Tools: Claude Code 2.1.283; Node v26.10.0; npm 10.9.9; uv 0.12.9;
CPython 3.11.6; PyTorch 2.14.0+cpu (`torch.version.cuda is None`).
PyTorch emitted a missing-NumPy initialization warning; these tensor-only tests
do not use NumPy and passed without adding it. No checks were suppressed.
`make check` deliberately not run because it executes excluded repository tests;
only the application fixtures changed, and their direct executable tests ran.

Final repaired `training.py` SHA-256:
`77aa7a3995448bb873ce78642944f72c84af8687bd2b6bf640d40ffac1bd7c77`.
Original fixture hashes are in `original.sha256`. No commits, pushes, deployments
or callback messages. Files are ready for the parent to download.
