# Launch kit — Augustus v0.1.0

Manual steps (need human accounts/OAuth; everything technical is ready).

## GitHub

Public mirror: https://github.com/24601/Augustus

Description, topics, and homepage are set on the About box. Confirm the
skills.sh badge resolves once indexed.

## skills.sh + other directories

- skills.sh indexes public GitHub repos with `SKILL.md`; install path is
  `npx skills add 24601/Augustus --skill augustus`. If a submit form
  appears, use the README description + topics above.
- Same payload works for other Agent Skills directories.

## Claude (ready — user runs)

```bash
claude plugin marketplace add 24601/Augustus
claude plugin install augustus@augustus
```

## Cursor (user runs)

```bash
npx skills add 24601/Augustus --skill augustus
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
> MIT. Install: `claude plugin marketplace add 24601/Augustus` then
> `claude plugin install augustus@augustus`, or
> `npx skills add 24601/Augustus --skill augustus`.
> github.com/24601/Augustus

Follow-up posts: the Score-ambiguity counterexample ([0,1,0] vs [0.5,0,0.5]
both score 1.0); the 255-option beam-search recipe; "Noul 0.5 is not medium".
