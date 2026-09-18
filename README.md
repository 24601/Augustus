# Augustus

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-marketplace-purple.svg)](.claude-plugin/marketplace.json)
[![Skills.sh](https://img.shields.io/badge/skills.sh-compatible-green.svg)](https://www.skills.sh/)

**Augustus** — named for Augustus De Morgan (1806–1871), mentor and professor
of William Stanley Jevons — is an agent skill for designing judgment-assisted
systems with [TypeSafe](https://docs.typesafe.ai/) Jev System One models. Code
stays in control; Jev supplies narrow, typed semantic judgments (Choice,
Score, Noul) that software can act on directly.

> Companion, not replacement, to the official
> [`typesafe-ai` skill](https://github.com/typesafe-ai/skills). That skill
> owns integration contracts; Augustus owns the **design judgment**: which
> classical methods map onto Jev primitives, what breaks in translation, and
> what experiment would prove a design wrong.

## The skill

- `.agents/skills/augustus/SKILL.md` — working protocol + decision-design card
- `.agents/skills/augustus/references/mappings.md` — 5 classical-method
  mappings with boundaries, counterexamples, acceptance tests
- `.agents/skills/augustus/references/validation.md` — design gate, eval
  recipes, Jev-for-skills (routing, self-monitoring, testing, modularity,
  frontmatter)
- `.agents/skills/augustus/scripts/evaluate_decisions.py` — offline evaluator
  for selective binary decisions (Brier, reliability, threshold/cost sweep)

Plus `research/` — the living evidence archive behind the skill, refreshed
hourly (see `research/README.md`).

## Install

**Claude Code** (plugin marketplace, mirrors the official TypeSafe layout):

```bash
claude plugin marketplace add <this-repo-url>
claude plugin install augustus@augustus
```

**Any skills-compatible agent** (Amp, Codex, Cursor, …):

```bash
npx skills add <owner>/<repo> --skill augustus
```

**ChatGPT**: skills are not a native ChatGPT primitive — paste
`.agents/skills/augustus/SKILL.md` plus the two `references/` files into a
GPT's instructions or a Project's knowledge and it will follow the protocol.

**Amp**: repo-local `.agents/skills/` are discovered automatically.

## Suggested GitHub topics

`jev` `typesafe` `system-one-models` `structured-output`
`calibrated-confidence` `ai-agents` `agent-skills` `decision-systems`
`reranking` `beam-search`

## Versioning

See [CHANGELOG.md](CHANGELOG.md). Current: **0.1.0**.

## License

MIT — see [LICENSE](LICENSE).
