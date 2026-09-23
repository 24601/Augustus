# Film embed audit, 2026-09-22

This audit covers a website and README change. It adds a homepage section for the
2:38 film "The story of Jev and Augustus" and a poster link in the README.
The skill package is unchanged.

## Hosting decisions

- **Video file:** GitHub release `film-jev-and-augustus`, a pre-release that is
  not marked latest. The MP4 stays out of git history, so clones and skill
  installs do not grow. The repository commits only the 114 KB poster.
- **On-page player:** a click-to-load facade. The poster link swaps to a
  `youtube-nocookie.com` iframe on activation. With JavaScript disabled, the
  facade stays a plain YouTube link and the transcript remains readable. The page
  requests only same-origin assets on load (`checks.json`, "hosts requested on load").
- **Rejected:** a native `<video>` pointing at the release asset. GitHub serves
  release assets as `application/octet-stream` with an attachment disposition.
  Chrome played the file, but Safari's handling of that content type is not
  dependable, so the release file is offered as a download link only.
- **Discoverability:** a `VideoObject` JSON-LD block with the name, description,
  thumbnail, upload date, `PT2M38S` duration, `contentUrl` (release MP4),
  `embedUrl` (nocookie) and the full transcript. The transcript is also on the
  page as HTML text, and the hero links to `#film`.

## Checks

- `make check`: pass.
- Built with `github-pages` 232 (Jekyll 3.10.0) in `ruby:3.3` Docker, because
  the local Ruby 4 cannot resolve that gem set.
  `python3 scripts/check_site.py _site`: pass.
- Viewports: 320, 390, 768 and 1440 CSS px in light and dark, requested
  through Puppeteer and Chrome with emulated `prefers-color-scheme`. All 8
  observed width/scheme pairs matched the requests, with no document-level
  horizontal overflow. Details in `checks.json`.
- Keyboard: focusing the poster link and pressing Enter replaces it with the
  iframe, which receives focus.
- Touch targets at 320 and 390 px: film links 44 px tall, transcript
  summary 44 px, and the poster link covers the whole image. Details in
  `touch-targets.json`.

## Independent review

Gemini 3.8 Flash reviewed screenshots at 1440 light, 1440 dark, 768 light,
390 dark and 320 light.

- **Accepted:** the section lacked the numbered mono index, so it is now
  `/03 — Film` and later sections are renumbered. The transcript toggle lacked
  a disclosure marker, now `+` / `−`. The duration appeared twice, so the
  eyebrow no longer repeats it.
- **Rejected with evidence:**
  - Touch targets under 44 px: measured at 44 px or more.
  - Caption and eyebrow contrast: they use the site's existing
    secondary-text tokens, #626262 on #fff (about 5.9:1) and #a1a1a1 on
    #0a0a0a (about 7.6:1), both above WCAG AA 4.5:1.
- **Not changed, optional:** placing the external links below the poster on
  narrow screens.

The play badge was moved off-centre after screenshots showed a centred
button covering the poster's title.
