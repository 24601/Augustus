# Changelog

## 0.1.0 — 2026-09-18

Initial release of the Augustus skill (`augustus` v0.1.0, MIT).

- Working protocol: evidence → judgments → policy → checked action → outcome,
  with decision-design card and evidence labels (Contract / Empirical recipe /
  Hypothesis).
- Five classical-method mappings with boundaries, counterexamples, and
  acceptance tests; MCTS-as-value, bandits, tournament brackets, and
  correlated-checks marked experimental/rejected in place.
- Validation reference: design gate, behavioral tests, Jev-for-skills
  (rank-then-verify routing, self-monitoring, grounding checks, skill
  testing, modularity, frontmatter guidance).
- `evaluate_decisions.py`: offline Brier / reliability / threshold-cost
  evaluator with self-test.
- Research archive baseline (40 sources, 2026-09-18) + hourly refresh script.
- Claude Code marketplace manifest; skills.sh-compatible layout.
