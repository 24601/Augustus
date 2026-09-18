# Launch kit — Augustus v0.1.0

Manual steps (need human accounts/OAuth; everything technical is ready).

## GitHub (needs a public repo)

1. Push this repo to GitHub (public).
2. Set description: "Augustus — design judgment-assisted systems with
   TypeSafe Jev System One models (Choice/Score/Noul). Named for De Morgan."
3. Set topics: `jev typesafe system-one-models structured-output
   calibrated-confidence ai-agents agent-skills decision-systems reranking
   beam-search`
4. Confirm the skills.sh badge resolves once indexed.

## skills.sh + other directories

- skills.sh indexes public GitHub repos with `SKILL.md`; install path is
  `npx skills add <owner>/<repo> --skill augustus`. If a submit form
  appears, use the README description + topics above.
- Same payload works for other Agent Skills directories.

## Claude (ready — user runs)

```bash
claude plugin marketplace add <github-url>
claude plugin install augustus@augustus
```

## Cursor (user runs)

```bash
npx skills add <owner>/<repo> --skill augustus
```

then select Cursor when prompted. ChatGPT: paste `SKILL.md` + `references/`
into GPT instructions or Project knowledge (see README).

## X announcement (draft)

> Augustus v0.1.0 — an agent skill for designing with TypeSafe's Jev, the
> decision model that returns typed judgments instead of text.
>
> Not another API wrapper: 5 classical-method mappings (features, selective
> decisions, decision circuits, reranking, beam search) each with the
> counterexample that breaks naive use + the experiment that tests it.
>
> Named for Augustus De Morgan — Jevons' mentor. Jev ← Jevons ← De Morgan.
>
> MIT. Install: claude plugin / npx skills add. [repo link]

Follow-up posts: the Score-ambiguity counterexample ([0,1,0] vs [0.5,0,0.5]
both score 1.0); the 255-option beam-search recipe; "Noul 0.5 is not medium".
