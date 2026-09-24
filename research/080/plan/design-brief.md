# ExoPO position paper — design brief (maintainer direction, 2026-09-23)

Paper: "When the Model Is Not the Policy: Exogenous Policy Optimization for Agents That Act".
Confidential: 0.8.0 stays off GitHub for now; build and review locally.

## Two artifacts (clarified by the maintainer)
1. **The paper** — very modern, very well designed, restrained, professional
   (typeset paper; clean, not trendy).
2. **The project website** — restrained but design-forward, interactive,
   explanatory and innovative; this is where the explorables live.

## Direction (maintainer's words, paraphrased faithfully)
- Very modern, very well designed, restrained. Professional but design-forward.
- NOT the en-vogue "beige paper + green" look; no gimmicky typography changes; no
  wall of headings (few, meaningful sections; prose carries the argument).
- Interactive: it explains by letting the reader manipulate the mechanism.
- Innovative — the form should demonstrate the thesis, not decorate it.

## Implications to carry into plan/review
- Interactivity must be load-bearing, each figure a small explorable tied to a claim:
  cost sliders that move a two-act threshold (C_FP/(C_FP+C_FN)) without retraining;
  a same-menu entropy vs top-mass reversal the reader can drag;
  a deferral simulator (handler loss by case, Chow vs Mozannar–Sontag vs entropy band,
  showing population-calibration failure); the exogeneity test as an interactive
  checklist that routes a reader's scenario to endogenous/exogenous/mixed.
- Restraint: one typeface family (or two at most), neutral palette with a single
  accent used only for data/state, generous whitespace, no ornament; headings only
  where the argument turns. Works without JS as a readable paper; JS enhances.
- Honesty in the medium: simulations labeled as simulations/theory; no invented
  benchmark numbers; reported results attributed; falsifiers visible.
- Accessibility: keyboard-operable controls, reduced-motion respect, AA contrast,
  mobile-first reading width.
