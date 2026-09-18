# Jev usage digest — first run (2026-09-18)

Lens: X = how people think/use Jev (advice, products, skepticism). GH = secondary discovery.

## Dominant mental models (from first ~400 posts)

1. **Cost/prefilter before the LLM** — cheap relevance / irrelevance judgments to drop chunks or gate calls before an expensive generative model.
2. **Tool / skill routing** — pick the right tool, skill, or path; products like Toolrouter shipping this; open JevRouter harnesses.
3. **Agent gates & preference lint** — AGENTS.md prefs as Jev linters; confidence gates; harnesses (jev-harness, shadow mode).
4. **Mixed architecture, not stack replacement** — decision/classification model + LLM for writing; explicit pushback against “replace everything.”
5. **Skepticism as design signal** — “it’s just classification / oldest AI task” → Augustus should answer *where* typed judgment beats ad-hoc LLM classify, not claim novelty of classification itself.
6. **Reproduce / open heads** — community interest in training lightweight decision backbones / OpenJev-adjacent work (feeds Jev-omni).
7. **Early product surface** — real-time chat moderation (~200ms), EffectTS AI SDK interest, Home Assistant, semantic SQL, browser agents without LLM-in-loop, skill rankers.

## GH movers (topic:jev, last hour) — novel shapes

- Skill ranking for next step (skillranker)
- Git hunk staging by sentence (git-jev-stage)
- Command-output prune (jevprune)
- LlamaIndex reranker/router
- Home Assistant integration
- Semantic SQL over Postgres (jevql)
- Browser agent: code + Jev, no LLM loop (lizard-agent)
- Clean Code PR judge; malicious-code scanner; decision-first agent skill

## Augustus update targets

- Strengthen “mixed architecture” + cost-sensitive prefilter cards with live ecosystem examples
- Add product-pattern gallery (moderation, tool route, skill rank, preference lint) without diluting design-judgment mission
- Address classification-skepticism in non-negotiables / FAQ
- Maximize exposure: topics, skills.sh, marketplace already present — refresh research/notes + examples from this archive

## Jev-omni update targets

- Ingest raw X under `data/x/` (this run)
- Note cross-modal gap: discourse still mostly text decisions; few true omni-input System One claims — opportunity, not clone
- Track LightJev / trained-heads / reproduce threads as training signal
