# Handoff: Augustus discoverability actions via grok-bot-cli (Basit's local machine)

Context: The Augustus skill (TypeSafe Jev design judgment) is built and pushed to
https://ampcode.com/@basit/Augustus. The sandbox cannot fork/create repos/issues
(GH token is a scoped integration token; no `op` CLI). These actions need the
local GitHub credentials (1Password-stored `gh` or 24601 account).

## Task 1 — Create the public GitHub repo for the skill

```bash
gh auth status   # confirm 24601 with repo scope
gh repo create Augustus --public --description "Agent skill: design judgment-assisted systems with TypeSafe Jev (System One). Method substitution, composition algebra, question design, validation gates. MIT." --source /tmp/augustus-mirror --push
```

Source content is the Amp repo; mirror everything except `.git`:
the repo is currently only at ampcode.com/@basit/Augustus — clone locally,
push to github.com/24601/Augustus (or the carcinize-corp org if preferred).

## Task 2 — Three PRs to the awesome lists

For each: `gh repo fork <owner>/<repo> --clone` → branch → edit README → PR.

### PR 1 — AnotiaWang/awesome-jev (Agent Tools section, after `jev-system-architect`)

```markdown
- [augustus](https://github.com/24601/Augustus) - Agent skill: design judgment-assisted systems with Jev — maps Choice/Score/Noul onto classical methods (decision theory, MCTS, rerank, routing), 11-position composition algebra, question-design diagnosis table, validation gates with falsifying experiments, optimizer coupling (Ax, DSPy, ProgramAsWeights). Companion to the official skill: integration contracts vs design judgment. Hourly-refreshed research base: 187 launch-week repos analyzed.
```

### PR 2 — yibie/awesome-jev (classification/routing or agent-decisions category)

```markdown
- [augustus](https://github.com/24601/Augustus) - Agent skill: the design/mental-model layer for Jev — toolbox sweep maps trusted classical methods onto Choice/Score/Noul, composition algebra positions judgment in any construct, question-design + validation cards make designs falsifiable. Includes the analyzed 187-repo launch-week evidence base (evidence.csv + findings).
```

### PR 3 — Anil-matcha/awesome-jev-by-typesafe (Related Projects or a use-case anchor)

```markdown
- [augustus skill](https://github.com/24601/Augustus) — design-judgment agent skill for Jev: method substitution toolbox, composition algebra (11 positions), question-design mechanics, validation gates. Companion to integration-focused skills; evidence-backed with a launch-week ecosystem analysis (docs/ecosystem.md).
```

## Task 3 — (optional, same session) X launch post

Post from the owner account linking the skill + ecosystem index. Draft:

> We built the first deep-design skill for Jev (TypeSafe's System One model):
> not "how to call it" but where judgment belongs in software — mapping MCTS,
> decision theory, retrieval re-rank, routing onto Choice/Score/Noul, with a
> composition algebra and falsifying experiments. 187 launch-week repos analyzed.
> github.com/24601/Augustus

## Verification / done-when

- github.com/24601/Augustus exists, pushes, README renders badges + install commands.
- 3 PRs open (or issues if PRs rejected), with URLs reported back.
- Optional X post live.

## Notes

- Do NOT create issues as "24601" unless Basit confirms — he wants no stray
  submissions left behind; prefer clean PRs from forks only.
- Repo content must include: .agents/skills/augustus/, .claude-plugin/marketplace.json,
  docs/ (launch.md, ecosystem.md), research/ (notes.md, sources.json, archive/),
  scripts/, README, CHANGELOG, LICENSE. No secrets (none present).
- Keep the Amp repo (ampcode.com/@basit/Augustus) as canonical; the GH repo is
  the mirror/registry surface.
