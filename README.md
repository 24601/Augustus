# Augustus

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/github/v/release/24601/Augustus)](https://github.com/24601/Augustus/releases)
[![Claude Code](https://img.shields.io/badge/Claude_Code-marketplace-purple.svg)](.claude-plugin/marketplace.json)
[![Skills.sh](https://img.shields.io/badge/skills.sh-compatible-green.svg)](https://www.skills.sh/)

**Augustus** — named for Augustus De Morgan (1806–1871), mentor and professor
of William Stanley Jevons — is an agent skill for designing systems around
the class of **fast, cheap categorization / classification / scoring
models**. [TypeSafe](https://docs.typesafe.ai/) Jev is the documented
exemplar (Choice, Score, Noul), not the monopoly: open heads (Laya),
GLiClass-adjacent encoders, listwise rankers, and vision scorers sit in
the same design space. Code stays in control; the judgment-class model
supplies bounded answers software can act on.

> Companion, not replacement, to the official
> [`typesafe-ai` skill](https://github.com/typesafe-ai/skills). That skill
> owns Jev integration contracts; Augustus owns the **design judgment**:
> which *family* and classical methods map, what the objective implies for
> fail-open vs fail-closed, what that does to agent architecture, and
> what experiment would prove a design wrong. Not a TypeSafe-only how-to.

## The skill

- `.agents/skills/augustus/SKILL.md` — working protocol + decision-design card
- `.agents/skills/augustus/references/judgment-class.md` — the class (Jev
  exemplar, not monopoly): open heads, GLiClass-adjacent, listwise vs
  decision objectives, vision scoring, agent-architecture portents
- `.agents/skills/augustus/references/formal-methods.md` — judgment vs
  proof ownership; Alloy/TLA+/Quint/P/NuSMV/PRISM/Event-B;
  Dafny/JML/Frama-C/SPARK; DST (Antithesis/Resonate); TOCTOU, soundness
  theater, vibing specs (Hillel); NATM/snap-fit/Norman/Leveson
- `.agents/skills/augustus/references/mixed-architecture.md` — default
  placement: judgment-class model + LLM + code; preference lint; provider
  (Jev default / other family with self-eval)
- `.agents/skills/augustus/references/applied-mappings.md` — context sieve,
  exact-text keep/drop, env triage, moderation/ranking, skill routing
- `.agents/skills/augustus/references/faq.md` — "just classification",
  stack replacement, Jev vs open head vs GLiClass vs CLIP, not-another-how-to
- `.agents/skills/augustus/references/mappings.md` — 5 classical-method
  mappings with boundaries, counterexamples, acceptance tests
- `.agents/skills/augustus/references/validation.md` — design gate, eval
  recipes, Jev-for-skills (routing, self-monitoring, testing, modularity,
  frontmatter)
- `.agents/skills/augustus/references/boundary-audit.md` — existing-system
  insertion: fit test, opportunity map, smallest boundary, red flags
- `.agents/skills/augustus/scripts/evaluate_decisions.py` — offline evaluator
  for selective binary decisions (Brier, reliability, threshold/cost sweep)

Plus `research/` — the living evidence archive behind the skill, refreshed
hourly (see `research/README.md`).

## Install

**Claude Code** (plugin marketplace, mirrors the official TypeSafe layout):

```bash
claude plugin marketplace add 24601/Augustus
claude plugin install augustus@augustus
```

**Any skills-compatible agent** (Amp, Codex, Cursor, …):

```bash
npx skills add 24601/Augustus --skill augustus
```

**ChatGPT**: skills are not a native ChatGPT primitive — paste
`.agents/skills/augustus/SKILL.md` plus the `references/` files into a
GPT's instructions or a Project's knowledge and it will follow the protocol.

**Amp**: repo-local `.agents/skills/` are discovered automatically.

## GitHub topics

`jev` `typesafe` `typesafe-ai` `system-one` `system-one-models`
`structured-output` `calibrated-confidence` `ai-agents` `agent-skills`
`decision-systems` `reranking` `beam-search` `claude-code` `python` `llm`
`decision-theory` `semantic-search` `agent-workflows` `mixed-architecture`
`tool-routing` `skill-routing` `semantic-lint` `classification` `gliclass`
`listwise-ranking` `vision-scoring` `open-weights` `formal-methods`
`model-checking` `deterministic-simulation`

## Versioning

See [CHANGELOG.md](CHANGELOG.md) and
[releases](https://github.com/24601/Augustus/releases). Current: **0.3.0**,
written against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`). Re-read live TypeSafe docs before treating that pin as current
API behavior.

## License

MIT — see [LICENSE](LICENSE).
