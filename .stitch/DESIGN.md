# Design System: Augustus: decision fieldnotes

## 1. Visual Theme & Atmosphere

A working technical publication for people building with agents. The page should
feel like an annotated decision study, not a dashboard or an AI startup template.
Its signature is a legible, content-rich worked example: the evidence, the narrow
judgment, the exact policy, and a test that could reject the change. Label it as
an illustrative design, never as measured product performance.

## 2. Color Palette & Roles

- Pale mineral (#F3F4EF): the reading canvas, without texture or gradient effects.
- Charcoal (#202620): primary text and strong structural rules.
- Forest green (#315C45): primary action and the bounded model judgment.
- Secondary ink (#546054): explanatory text, never low-contrast decoration.
- Light sage (#E3E9DE): the worked decision's judgment region, not every section.
- Rule (#BEC6BA): quiet dividers within a section.
- White (#FFFFFF): code surfaces and contrasting text on forest green.
- Dark-mode canvas (#171D19), text (#E8EDE5), secondary text (#B9C5B8),
  accent (#ABD5B4), inset surface (#242F27), judgment region (#2D3C30), and
  rule (#566653) preserve the same hierarchy.

## 3. Typography Rules

IBM Plex Serif gives headings the voice of a mathematical publication. IBM Plex
Sans carries navigation and explanatory copy. IBM Plex Mono is reserved for
actual commands, identifiers, and expressions. No all-caps microtext treatment.
Body copy is at least 16px. Aim for about 60 to 70 characters in narrative
passages; reference pages, short study annotations, and comparison tables may
use the wider grid to keep related information together. Inspect the actual
reading experience rather than treating a character count as a quality score.
Display type is confident but must not push the product explanation or install
action off the first mobile screen. Avoid forced line breaks on narrow screens.

## 4. Component Stylings

- Buttons: square-edged forest-green primary action, clear contrasting label,
  minimum 44px touch height. Ordinary destinations remain underlined text links.
- Containers: mostly unboxed. Rules separate genuinely different information;
  one coherent decision study has a clear internal reading order. No shadows,
  fake window chrome, nested cards, skeleton bars, decorative gauges, or pills.
- Code: genuine copyable installation commands on a quiet contrasting surface.
  Commands wrap visually below 44rem without changing their clipboard text.
  Any remaining overflow stays inside its focusable code region, never on the
  whole page. Reading-page code regions have distinct numbered accessible names.
- Focus: a conspicuous outline with an offset. Color alone never encodes ownership.
- Motion: still by default. No reveal gating, pulsing, floating, or scroll effects.

## 5. Layout Principles

Use a broad publication masthead, a concise thesis, and a wide annotated decision
study as the opening argument. Do not put a generic mock dashboard beside the
hero. A marginal note may explain the example's limits. Use different rhythms for
the study, concise use-case index, and installation reference; not repeated grids.

Desktop content occupies a shared approximately 1160px reading grid. Mobile
retains the entire content and order in one column, with 20px gutters. Navigation
wraps naturally without a hidden menu. Tables and code may scroll in labelled,
keyboard-focusable regions. Keep the skip link and semantic headings. All content
and navigation work with JavaScript disabled and reduced motion enabled.

## 6. Product Truth and Acceptance

Augustus is an agent skill and method engine for finding, building, evaluating,
and iteratively improving decision-model systems, including evals, bounded
hill-climbing loops, and Software 3.0 workflows. It is not a hosted runtime or
an autonomous optimizer. TypeSafe Jev is the default hosted exemplar, not the
whole mission; this project is independent. No new model is a valid conclusion.

Keep install commands, examples, ecosystem, current release, research, and source
reachable. Do not invent benchmarks, adoption statistics, customer marks, or
claims of proven outcome gains. A design review is evidence, not acceptance.
Inspect rendered desktop, tablet, and mobile pages in both themes, keyboard
navigation, no-JavaScript visibility, local overflow, and actual link targets.
Mechanical checks cannot certify taste; compare the complete rendered argument.
