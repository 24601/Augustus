# Augustus

Design judgment for the decision-model class. TypeSafe Jev
(Choice, Score, Noul) is the dominant product most users will call.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/24601/Augustus)](https://github.com/24601/Augustus/releases)
[![Pages](https://img.shields.io/badge/docs-24601.github.io-blue.svg)](https://24601.github.io/Augustus/)
[![Claude Code](https://img.shields.io/badge/Claude_Code-marketplace-purple.svg)](.claude-plugin/marketplace.json)
[![Skills.sh](https://img.shields.io/badge/skills.sh-compatible-green.svg)](https://www.skills.sh/)

**Homepage:** [24601.github.io/Augustus](https://24601.github.io/Augustus/)

Design-judgment skill for where the decision-model class belongs.
TypeSafe Jev (Choice, Score, Noul) is the dominant exemplar. Classical
decision methods, composition algebra, and a validation gate.

**Augustus**, named for Augustus De Morgan (1806–1871), mentor and professor
of William Stanley Jevons, is the design-judgment skill for **where** the
decision-model class belongs (classifiers, encoders and decoders, specialized
AR and constrained heads, vision and listwise scorers, and what TypeSafe
calls System One), using mathematical, logical, and algorithmic mental
models. It applies across **AI, software, business, knowledge work, and
life**, not only SWE.
[TypeSafe](https://docs.typesafe.ai/) Jev is the dominant product most
users will call (Choice, Score, Noul). Formal methods are one pillar.
Exact work stays in code or policy; the model owns narrow judgment;
never launder a Noul as a proof.

> **Not a TypeSafe product.** Companion, not replacement, to the official
> [`typesafe-ai` skill](https://github.com/typesafe-ai/skills). That skill
> owns Jev integration contracts; Augustus owns the **design judgment**:
> which *pillar*, *family*, and classical method map, what the objective
> implies for fail-open vs fail-closed, and what experiment would prove a
> design wrong. Not a TypeSafe-only how-to. Integrity / reward-hack
> companion: [`rh-guard`](https://github.com/24601/rh-guard).

![Jev-class models with vs without Augustus. Without: call the model, act on the score, then quiet failure modes (soft Noul treated as hard gate, GPT bakeoff framing, no falsifier, polarity unchosen). With Augustus: state, pillar and family map, question design, fail-open vs fail-closed, typed Choice Score Noul, code owns effects, named falsifying experiment.](docs/assets/with-without-augustus.svg)

Jev-class: Jev, kev, Laya, OpenJev, GLiNER, SemIf, NanoJev, Jeff-1, localjev.
Call and act, or place the judgment. Same split for any typed probabilistic
judgment tool, not Jev-only.

## Recipes

Class-wide, not a TypeSafe how-to. Full cards:
[`docs/release-notes-v0.5.0.md`](docs/release-notes-v0.5.0.md) ·
[Pages recipes](https://24601.github.io/Augustus/#recipes).

- **Decide vs generate.** Without: treat tryDecide as another token stream. With: decide is not generate; typed calibrated judgments, not chat. Third-party benches stay *theirs*.
- **Encoder (GLiNER / GLiClass).** Without: treat locate/categorize as a decision head and hard-gate spans. With: species map; remainder after extractive spans. Ports are class members, not Jev replicas. Measure span quality separately from ECE.
- **Open heads (Laya, SemIf, kev, Jeff-1).** Without: wire-compat or argmax agree as replica. With: softmax ≠ calibrated Noul; systems timing ≠ semantic equivalence. Measure ECE/Brier on held-out, not only speed.
- **NanoJev.** Without: game wins as calibration. With: specialist gameplay S1; local boolean ≠ TypeSafe noul. Measure held-out game separately from ECE.
- **llm-to-jev.** Without: ship converted prompts as equivalent behavior. With: heuristic on-ramp; review the Score rubric. heuristic conversion ≠ calibrated Noul.
- **jcr.** Without: run what the tree found. With: lookup returns context; **does not execute**. Routing ≠ permission; docs ≠ authority to run.
- **localjev / prompted JSON.** Without: parse generated JSON as a Noul. With: schema-valid ≠ picked-right.
- **Open-Jev v3 / held-out / wide ranking.** Without: treat v3 rows as a released replica, a held-out protocol as Harbor, 83% as Harbor, or Jev as a Lean writer. With: v3 data prepared ≠ retrained released models; held-out protocol ≠ Harbor; 1,280-row panel ≠ Harbor; finite training loss ≠ quality improvement; website redesign ≠ calibration; Jev is a gate not a generator; *theirs* not Harbor.
- **JevBench public-subset / 35B transfer / browser 5-10x.** Without: treat 231 as the full 534, 0.550 as Harbor, 5-10× as a replica, or fail-open routing as a grant. With: public-subset ≠ Harbor; 231 ≠ 534; evaluate.load honour bf16; 5-10× *theirs* not Harbor; routing ≠ permission; softmax next-token ≠ calibrated Noul; *theirs* not Harbor.
- **openjev MLX / TypeLLM v0.1.1.** Without: treat MLX text gen as a calibrated replica, a GitHub Release as a Noul, n=8 as Harbor, or option-order 0.188 as gold. With: dual serving is not generate; Hosted Codiv ≠ TypeSafe; wire-compat ≠ logit-equiv; Constrained AR ≠ calibrated Noul; PyPI packaging ≠ calibrated Noul; n=8 is not Harbor; option order can change an answer; *theirs* not Harbor.
- **aisearchio census / open System One.** Without: treat TypeSafe-compatible as a replica, 76.7% as Harbor, or a 15-link list as an endorsement. With: TypeSafe-compatible ≠ TypeSafe replica; replica ≠ TypeSafe; catalog ≠ endorsement; *theirs* not Harbor.

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
- `research/notes.md`: living hourly catalog (dense); §118 llm-to-jev conversion assistant (heuristic on-ramp, not a replica); §122 revisit / since-last-look protocol
- `research/README.md`: evidence archive index (sources, refresh log, hourly dumps)
- `research/revisit-checklist.md`: revisit already-catalogued repos when fingerprints move (revisit HIGH like novel HIGH)
- `research/changelog-hourly.md`: hourly uniqueness dumps after v0.3.0

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
[releases](https://github.com/24601/Augustus/releases). Current: **0.5.0**,
written against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`; live HEAD still this commit). Re-read live TypeSafe docs
before treating that pin as current API behavior.

## License

MIT. See [LICENSE](LICENSE). Security reports: [SECURITY.md](SECURITY.md).
Contributions: [CONTRIBUTING.md](CONTRIBUTING.md).
