# Website reskin: Geist × stripe.dev

Date: 2026-09-22. Scope: website, its assets, review guidance and structural
checks. This supersedes the mineral/green serif direction in the
[earlier audit](2026-09-22-website-design.md), not its historical evidence.
The user explicitly requested a Vercel/Geist × stripe.dev visual direction.
The v0.7.0 skill, marketplace, README, citation metadata and tag are unchanged.

## Design judgment

The parent inspected the live [Stripe developer site](https://stripe.dev/) and
[Geist grid](https://vercel.com/geist/grid), alongside the official
[typography](https://vercel.com/geist/typography),
[colors](https://vercel.com/geist/colors) and
[font](https://vercel.com/font) references. Stripe's large, tightly tracked
headings, small mono indexing, ruled columns and registration marks informed
the composition. Geist informed the neutral surfaces, actual font family and
component states. These are design interpretations, not claims of affiliation.

The implemented system uses locally served Geist Sans/Mono, a maximum 1280px
ruled frame, large sans headings, near-black/light-inverse actions, numbered
section labels and a four/two/one-column decision study. Favicon and share
artwork use Augustus's own outline A. No Vercel/Stripe logos, proprietary Söhne
fonts, copied illustrations, animated headline, invented metrics or JavaScript
framework were added. The study remains explicitly illustrative, and the
skill/method-engine, implementation/evaluation and no-model messages remain.

Design-system, responsive-design and accessibility guidance informed the token
roles, consistent states, responsive layout and keyboard checks. A monochrome
palette alone is not the quality criterion: the page's specific argument and
working installation path must survive the visual treatment.

No new Stitch/OpenDesign generation or external Fable/Gemini review ran for
this reskin. The earlier Stitch project and reviews remain historical;
`.stitch/metadata.json` explicitly distinguishes them from the current contract.

## Font and share provenance

The two unmodified variable WOFF2 files come from
[vercel/geist-font at 10dc7658](https://github.com/vercel/geist-font/tree/10dc7658f13c38a474cde201bb09a4617267545b).
Both upstream copyright/license texts accompany them; trailing license
whitespace is normalized. Fonts retain SIL OFL 1.1, separately from Augustus's
MIT license. Exact paths and hashes are in the
[font README](../../docs/assets/fonts/README.md).

Both local font requests returned HTTP 200 with `font/woff2` content type;
Sans is 69,760 bytes and Mono is 71,596 bytes. Browser rendered-font inspection
identified custom `Geist-Medium` on the H1 and custom `GeistMono-Regular` on
the opening label, not merely CSS family declarations or plausible fallbacks.
The social SVG's title likewise rendered with custom Geist before a lossless
1200×630 PNG export. The parent opened the resulting bitmap. Its SHA-256 is
`b0499433225e80b8ae32d9399eddf44105e4e9ff6e0cb94c7d1fdcca46493f04`.

The HTML uses the PNG for sharing. The fonts use local preload and
`font-display: swap`; there are no third-party font requests or font-loader JS.

## Verification

- `make check`: **115 tests**, repository checks, numerical/revisit self-tests
  and shell syntax passed under the isolated Python 3.12 environment.
- Production `github-pages` **232**, Jekyll **3.10.0** build passed. Explicit
  activation selected the Pages gem versions. `scripts/check_site.py` passed
  against the actual `/Augustus/` output.
- Chrome: home, placements, examples, ecosystem and v0.7.0 notes at **320,
  390, 768 and 1440 CSS pixels**, light/dark: **40 unique observed cases**,
  actual requested dimensions/theme matched, one H1 and no document overflow.
  The [measurement receipt](2026-09-22-website-geist/layout-checks.json) records
  actual widths, computed canvas color, command and table regions.
- Parent visually inspected the full desktop/mobile pages and representative
  tablet, phone, dark-theme, installation and shared-reading screenshots.
  Screenshot dimensions were checked, not inferred from requested sizes.
- Keyboard-only at 390px: Tab focuses the visible skip link with a 3px outline;
  Return focuses `MAIN#main`; the next Tab reaches Install; Return reaches
  `#install`. Repeated with **page JavaScript disabled and reduced motion**.
  [Interaction receipt](2026-09-22-website-geist/interaction-checks.json).
- The family table was too cramped at 320px despite having no page overflow.
  It now retains readable 640px columns inside a named, focusable scroll region
  with a visible instruction. Twelve Tabs reached it; Right keys moved its
  scroll position from **0 to 386**, exposing the final column in a **254px**
  viewport. Native table/header semantics remain. See the
  [keyboard receipt](2026-09-22-website-geist/table-keyboard.json).
- Added parsed regression cases for the table container's accessible name,
  actual tab index and region role, including invalid/missing references and
  class-token rather than substring matching. These are bounded structural
  checks, not proof that all overflow containers are detected or usable.
- Commands remain exact text, visually wrapped on phones. Pinch-scale emulation
  reached **2×** and was reset; this is not native browser text-zoom testing.
- Opaque sRGB text-token contrast: primary/action **17.93:1 light**, **16.91:1
  dark**; the lowest tested secondary/background pair is **5.55:1**. Decorative
  rules are not text or sole control boundaries. See the
  [contrast calculation](2026-09-22-website-geist/contrast.json).
- `git diff --check` passed. Released package paths compare unchanged against
  `v0.7.0`. No skill behavior or provider integration was exercised or changed.

### A verification trap corrected

An initial responsive loop used a browser-wide viewport setter with multiple
tabs open; it resized another tab, leaving repeated 390px measurements. Those
results were rejected. The accepted matrix uses the target tab's viewport,
asserts actual width/height and computed theme, and counts unique configurations.
Contributor guidance now requires these checks. A loop count is not coverage.

The small pointer/blue halo at the outer top-left of screenshots is browser
automation overlay, not website artwork. The keyboard-table screenshot retains
the earlier pointer position. No screenshot was retouched to hide defects.

## Fresh independent review

The parent inspected the complete accumulated reskin diff and reran checks
before freezing a public-only review folder. Host metadata and credentials were
excluded. The [manifest](2026-09-22-website-geist/review-manifest.json) records
the exact source, rendered output, screenshots and brief. `source/` maps to
`docs/`; other paths name frozen review inputs, not committed runtime files.

Requested reviewer: native **gpt-6-astra / high**, fresh context,
`/root/geist_design_review`. Ownership is read-only source/visual review, with
no edits, delegation, network or external services. This is an instruction
boundary, not a claimed filesystem sandbox. Parent/child effective backend,
effort and token usage are not exposed by native status metadata; requested
routing is not independent runtime attestation.

Review disposition: **ship**, no required corrections. The reviewer directly
inspected all 13 current screenshots and the social PNG; compact 320px navigation
was optional polish, not a blocker. The parent accepts the implementation based
on the integrated diff, live checks and images, not the verdict alone. See the
[review return](2026-09-22-website-geist/astra-review.md),
[frozen brief](2026-09-22-website-geist/review-brief.md) and
[test output](2026-09-22-website-geist/checks.log). The frozen inputs were
hash-checked again after review; no changes were found.

## Limits and publication boundary

Not tested: Safari, physical devices, screen readers, arbitrary native text
zoom, print rendering or social-platform cache refresh. A scrollable wide
table requires lateral navigation on phones. The 320px navigation remains
compact. These checks are not a WCAG certificate, measured conversion lift,
indexing/adoption evidence or proof of user outcomes.

This candidate updates PR #92. It does not authorize or claim a merge, Pages
deployment, new release, external listing updates or changed account settings.
Earlier Fable/Gemini approvals apply only to the previous candidate.

API-EQUIVALENT COST RECEIPT: unavailable. Native tools did not expose observed
parent or reviewer token usage. Routed USD, same-token Astra repricing and
price difference are unavailable, not zero. No savings or subscription-charge
claim is made; historical external-review subtotals are not attributed here.

## Screenshots

- [Desktop](2026-09-22-website-geist/desktop.jpg) and
  [complete desktop](2026-09-22-website-geist/desktop-full.jpg).
- [390px phone](2026-09-22-website-geist/mobile.jpg),
  [complete phone](2026-09-22-website-geist/mobile-full.jpg),
  [320px phone](2026-09-22-website-geist/home-320.jpg),
  [768px tablet](2026-09-22-website-geist/home-tablet.jpg).
- [Dark desktop](2026-09-22-website-geist/dark-desktop.jpg),
  [phone installation](2026-09-22-website-geist/mobile-install.jpg),
  [dark phone installation](2026-09-22-website-geist/dark-mobile-install.jpg).
- [Examples](2026-09-22-website-geist/examples-mobile.jpg),
  [placements](2026-09-22-website-geist/placements-tablet.jpg),
  [family table](2026-09-22-website-geist/ecosystem-320.jpg),
  [keyboard-scrolled family table](2026-09-22-website-geist/ecosystem-keyboard.jpg).
- [Superseded green design](2026-09-22-website-geist/before-desktop.jpg).
