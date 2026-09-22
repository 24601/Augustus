# Design System: Augustus: developer reference

Current direction, 2026-09-22: the user requested “Vercel design system/Geist ×
stripe.dev.” This supersedes the earlier approved mineral/green serif brief.
The existing Stitch project is historical provenance, not the current palette.

## 1. Visual Theme & Atmosphere

A precise developer reference for people building with agents. The page should
feel like a working specification, not a dashboard or an AI startup template.
Its signature is a legible, content-rich worked example: the evidence, the narrow
judgment, the exact policy, and a test that could reject the change. Label it as
an illustrative design, never as measured product performance.

Use [Geist](https://vercel.com/geist/introduction) for neutral surfaces, consistent
type and component states; use [stripe.dev](https://stripe.dev/) for expansive,
tightly set headings, mono indexing and ruled editorial structure. Borrow the
principles, not brand marks, proprietary fonts, copied artwork or product claims.

## 2. Color Palette & Roles

- White (#FFFFFF): primary canvas. Off-white (#FAFAFA): outer page and code.
- Near-black (#171717): primary text, links and filled primary action.
- Gray (#626262): secondary text, not disabled-looking low-contrast decoration.
- Light gray (#F4F4F4): the bounded model-judgment region.
- Rule (#E2E2E2): decorative grid/dividers; stronger rule (#A1A1A1): annotations.
- Dark-mode canvas (#0A0A0A), outer/code (#111111), text/action (#EDEDED),
  secondary (#A1A1A1), judgment (#171717), rule (#303030) and strong rule
  (#737373). The action inverts to a light surface with dark text.
- No default green or violet brand accent, soft gradient wash or tinted CTA.
  Color is not needed to tell evidence, judgment, policy and execution apart.

## 3. Typography Rules

Geist Sans carries the entire text hierarchy: large, tightly tracked display
type; medium-weight section headings; regular readable body copy. Geist Mono is
for commands, release metadata and section/stage indices. Keep labels legible;
do not turn the entire page into tiny uppercase terminal text. Fonts are local,
unmodified WOFF2 assets with their upstream SIL OFL license and provenance.
Base prose and decision-study copy are 16px; compact reference/table copy may
use 14.4px, command text 12.8px, and mono metadata 12px. Aim for about 60 to 70
characters in narrative
passages; reference pages, short study annotations, and comparison tables may
use the wider grid to keep related information together. Inspect the actual
reading experience rather than treating a character count as a quality score.
Display type is confident but must not push the product explanation or install
action off the first mobile screen. Avoid forced line breaks on narrow screens.

## 4. Component Stylings

- Buttons: near-black/light inverse primary action, restrained 5px radius,
  clear contrasting label, minimum 44px height, visible hover/focus states.
  Ordinary destinations remain text links. No colored CTA or pill-heavy system.
- Containers: mostly unboxed. Rules separate genuinely different information;
  one coherent decision study has a clear internal reading order. Thin rails
  align the page; registration ticks mark a real section boundary and are hidden
  from assistive technology. No fake window chrome, skeletons or nested cards.
- Code: genuine copyable installation commands on a quiet contrasting surface.
  Commands wrap visually below 44rem without changing their clipboard text.
  Any remaining overflow stays inside its focusable code region, never on the
  whole page. Reading-page code regions have distinct numbered accessible names.
- Focus: a conspicuous outline with an offset. Color alone never encodes ownership.
- Motion: still by default. No reveal gating, pulsing, floating, or scroll effects.

## 5. Layout Principles

Use a compact masthead, an expansive thesis, and a wide annotated decision study
as the opening argument. Do not put a generic mock dashboard beside the hero.
A marginal note may explain the example's limits. Use different rhythms for
the study, concise use-case index, and installation reference; not repeated grids.

Desktop content occupies a shared maximum 1280px ruled grid. Mobile retains the
entire content and order in one column, with 12px outer and 20px inner gutters.
Navigation
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

Review evidence is candidate-specific. Approval of the previous serif/green
candidate is not approval of this reskin. Preserve earlier audits as history;
record fresh source hashes, screenshots and verification for the current bytes.
