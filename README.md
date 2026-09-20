# Augustus

Place typed probabilistic judgment (Jev-class System One / decision
models) using classical mental models. Jev is the exemplar, not the monopoly.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/24601/Augustus)](https://github.com/24601/Augustus/releases)
[![Pages](https://img.shields.io/badge/docs-24601.github.io-blue.svg)](https://24601.github.io/Augustus/)
[![Claude Code](https://img.shields.io/badge/Claude_Code-marketplace-purple.svg)](.claude-plugin/marketplace.json)
[![Skills.sh](https://img.shields.io/badge/skills.sh-compatible-green.svg)](https://www.skills.sh/)

**Homepage:** [24601.github.io/Augustus](https://24601.github.io/Augustus/)

Agent skill for placing TypeSafe Jev Choice/Score/Noul with classical
decision methods, composition algebra, and a validation gate.

**Augustus**, named for Augustus De Morgan (1806–1871), mentor and professor
of William Stanley Jevons, is the design-judgment skill for **where** typed
probabilistic judgment belongs (the Jev-class of System One models), using
mathematical, logical, and algorithmic mental models. It applies across
**AI, software, business, knowledge work, and life**, not only SWE.
[TypeSafe](https://docs.typesafe.ai/) Jev is the documented exemplar
(Choice, Score, Noul), not the monopoly. Formal methods are one pillar.
Exact work stays in code or policy; the model owns narrow judgment;
never launder a Noul as a proof.

> **Not a TypeSafe product.** Companion, not replacement, to the official
> [`typesafe-ai` skill](https://github.com/typesafe-ai/skills). That skill
> owns Jev integration contracts; Augustus owns the **design judgment**:
> which *pillar*, *family*, and classical method map, what the objective
> implies for fail-open vs fail-closed, and what experiment would prove a
> design wrong. Not a TypeSafe-only how-to. Integrity / reward-hack
> companion: [`rh-guard`](https://github.com/24601/rh-guard).

## The skill

One line per file. The living catalog is in the reference cards and
[`research/notes.md`](research/notes.md), not this README.

- `.agents/skills/augustus/SKILL.md`: working protocol and decision-design card
- `.agents/skills/augustus/references/mental-models.md`: cross-domain frames (EU, VOI, MCDA, SDT, ...); not SWE-only
- `.agents/skills/augustus/references/judgment-class.md`: the class (Jev exemplar, not monopoly) and peer families
- `.agents/skills/augustus/references/formal-methods.md`: judgment vs proof; soundness theater; DST trio
- `.agents/skills/augustus/references/formal-semi-formal.md`: one-screen alias of the formal-methods pillar
- `.agents/skills/augustus/references/mixed-architecture.md`: where S1 judgment sits next to LLM + code
- `.agents/skills/augustus/references/composition-algebra.md`: positions a typed judgment can occupy relative to any method
- `.agents/skills/augustus/references/applied-mappings.md`: sieves, keep/drop, triage, rank, and route placements
- `.agents/skills/augustus/references/faq.md`: design-judgment FAQ (not an API how-to)
- `.agents/skills/augustus/references/mappings.md`: classical-method mappings with boundaries and tests
- `.agents/skills/augustus/references/methods-catalog.md`: named algorithms → judgment-shaped substitution
- `.agents/skills/augustus/references/toolbox-mapping.md`: how to find a substitution in a method you already trust
- `.agents/skills/augustus/references/question-design.md`: writing and diagnosing well-formed questions
- `.agents/skills/augustus/references/validation.md`: design gate, eval recipes, Harbor/jevals practice
- `.agents/skills/augustus/references/boundary-audit.md`: existing-system insertion: smallest boundary, red flags
- `.agents/skills/augustus/references/optimizer-integration.md`: Jev inside Ax/DSPy optimizer loops
- `.agents/skills/augustus/references/agent-self-assessment.md`: agent self-supervision gates (pre-action, done, stuck)
- `.agents/skills/augustus/scripts/evaluate_decisions.py`: offline Brier / reliability / cost-threshold evaluator
- `research/notes.md`: living hourly catalog (dense)
- `research/README.md`: evidence archive index (sources, refresh log, hourly dumps)

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

**Copy the skill path** (Cursor / Amp / any agent that reads repo-local
skills):

```bash
git clone https://github.com/24601/Augustus.git
# skill lives at .agents/skills/augustus/
```

**ChatGPT**: skills are not a native ChatGPT primitive. Paste
`.agents/skills/augustus/SKILL.md` plus the `references/` files into a
GPT's instructions or a Project's knowledge and it will follow the protocol.

**Amp**: repo-local `.agents/skills/` are discovered automatically.

## GitHub topics

`jev` `typesafe` `typesafe-ai` `system-one` `system-one-models`
`structured-output` `calibrated-confidence` `ai-agents` `agent-skills`
`decision-systems` `reranking` `beam-search` `claude-code` `python` `llm`
`decision-theory` `decision-making` `semantic-search` `agent-workflows`
`mixed-architecture` `agentic-ai` `zero-shot-classification`
`tool-routing` `skill-routing` `semantic-lint` `classification` `gliclass`
`listwise-ranking` `vision-scoring` `open-weights` `formal-methods`
`model-checking` `deterministic-simulation`
`value-of-information` `signal-detection` `mcda` `calibration`
`alloy` `apalache` `pufferlib` `stamp-stpa`

## Versioning

See [CHANGELOG.md](CHANGELOG.md) and
[releases](https://github.com/24601/Augustus/releases). Current: **0.4.0**,
written against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`; live HEAD still this commit). Re-read live TypeSafe docs
before treating that pin as current API behavior.

## License

MIT. See [LICENSE](LICENSE). Security reports: [SECURITY.md](SECURITY.md).
Contributions: [CONTRIBUTING.md](CONTRIBUTING.md).
