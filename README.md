# Augustus

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/github/v/release/24601/Augustus)](https://github.com/24601/Augustus/releases)
[![Claude Code](https://img.shields.io/badge/Claude_Code-marketplace-purple.svg)](.claude-plugin/marketplace.json)
[![Skills.sh](https://img.shields.io/badge/skills.sh-compatible-green.svg)](https://www.skills.sh/)

**Augustus** — named for Augustus De Morgan (1806–1871), mentor and professor
of William Stanley Jevons — is an agent skill for **placing typed
probabilistic judgment** (the Jev-class of System One models) using
mathematical, logical, and algorithmic mental models. It applies across
**AI, software, business, knowledge work, and life** — not only SWE.
[TypeSafe](https://docs.typesafe.ai/) Jev is the documented exemplar
(Choice, Score, Noul), not the monopoly. Formal methods are one pillar.
Exact work stays in code or policy; the model owns narrow judgment;
never launder a Noul as a proof.

> Companion, not replacement, to the official
> [`typesafe-ai` skill](https://github.com/typesafe-ai/skills). That skill
> owns Jev integration contracts; Augustus owns the **design judgment**:
> which *pillar*, *family*, and classical method map, what the objective
> implies for fail-open vs fail-closed, and what experiment would prove a
> design wrong. Not a TypeSafe-only how-to.

## The skill

- `.agents/skills/augustus/SKILL.md` — working protocol + decision-design card
- `.agents/skills/augustus/references/mental-models.md` — cross-domain
  frames (EU, abstention, VOI, MCDA, SDT, search/control, Leveson,
  NATM/snap-fit/Norman); not SWE-only
- `.agents/skills/augustus/references/judgment-class.md` — the class (Jev
  exemplar, not monopoly): open heads (Laya, kev, encoder DeBERTa, LoRA
  distill), constrained-AR (TypeAR, pcdServer), announced decision-model (Watch),
  open multimodal RLCD (blackwood-rlcd; not Archer),
  GLiNER/GLiClass species (locate vs categorize vs local multi-head),
  listwise vs decision objectives, vision scoring, when-to-use axes,
  agent-architecture portents
- `.agents/skills/augustus/references/formal-methods.md` — judgment vs
  proof ownership; Alloy Analyzer vs Apalache (finder ≠ BMC ≠
  inductiveness); TLA+/Quint/P/NuSMV/PRISM/Event-B/mCRL2/KeYmaera;
  Dafny/JML/Frama-C/SPARK/ITP; DST trio (Antithesis hypervisor, Resonate
  HQ durable-async Lean+oracle+SDK, PufferLib env+seed); TOCTOU-of-Noul,
  soundness theater, AI×FM harms (Hillel, Cauli); NATM/snap-fit/Norman/
  Leveson/Kent/Shirky
- `.agents/skills/augustus/references/formal-semi-formal.md` — one-screen
  alias of the FM pillar
- `.agents/skills/augustus/references/mixed-architecture.md` — default
  placement: judgment-class model + LLM + code; preference lint; provider
  (Jev default / other family with self-eval)
- `.agents/skills/augustus/references/applied-mappings.md` — context sieve,
  exact-text keep/drop, env triage, moderation/ranking, skill routing
- `.agents/skills/augustus/references/faq.md` — "just classification",
  stack replacement, Jev vs open head vs encoder vs LoRA vs constrained AR vs kev vs blackwood,
  wait-for-Archer, missing-other confident-wrong, soft project rules vs linter (Abide), GLiNER vs GLiClass vs CLIP, LLM-as-judge, in-engine vs CLI store,
  hard envelope (bitrate / planner), not-another-how-to
- `.agents/skills/augustus/references/mappings.md` — classical-method
  mappings with boundaries, counterexamples, acceptance tests (including
  Hypothesis cards §6–§19 — promote only with a test that ran)
- `.agents/skills/augustus/references/validation.md` — design gate, eval
  recipes, Jev-for-skills (routing, self-monitoring, testing, modularity,
  frontmatter), and Eval & hill-climb (jevals hygiene + Harbor taskset;
  open-jev-laya-bench as ECE/NLL/Brier bake-off exemplar; Abide replay as
  Harbor-adjacent soft-rule measurement)
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
`model-checking` `deterministic-simulation` `decision-theory`
`value-of-information` `signal-detection` `mcda` `calibration`
`alloy` `apalache` `pufferlib` `stamp-stpa`

## Versioning

See [CHANGELOG.md](CHANGELOG.md) and
[releases](https://github.com/24601/Augustus/releases). Current: **0.3.0**,
written against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`). Re-read live TypeSafe docs before treating that pin as current
API behavior.

## License

MIT — see [LICENSE](LICENSE).
