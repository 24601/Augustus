# Mental models for applying System One / Jev-class judgment (seed)

Scope: AI · modern SWE · business · knowledge work · life. Formal methods = one pillar.

## Core job split (everywhere)
Evidence → narrow typed judgments (Choice / Score / Noul) → explicit policy → checked action.
Generative models write/invent; judgment models decide among menus. Humans still own values & irreversible stakes.

## Mathematical / logical / algorithmic frames

| Frame | What it gives you | Example placement of Jev-class tools |
|---|---|---|
| **Decision theory / EU** | Actions = expectations under beliefs + utilities | Score urgency; Choice among options; thresholds from action costs |
| **Selective classification / abstention** | Refuse when uncertain | Noul + confidence → escalate / ask / delay |
| **Calibration** | p means frequency under your distribution | Bake-offs; temperature; never trust vendor ECE alone |
| **Value of information** | When to gather more evidence | Noul “enough evidence?” before irreversible Choice |
| **Signal detection / cost-sensitive** | FP/FN asymmetry | Moderation, fraud, medical triage — thresholds by harm |
| **Multi-criteria decision analysis** | Named criteria, weights in policy | Parallel Nouls/Scores fused in code (visible weights) |
| **Ranking / choice under menus** | Choice probs conditional on offered set | Always include “other/none”; listwise interaction |
| **Search (beam / A\* / heuristic)** | Judgment-shaped node evaluation | Bounded rerank of shortlists; not open invent |
| **Control / hysteresis** | Avoid chatter at thresholds | Different enter vs exit Noul bars for automation |
| **TOCTOU / check-then-act** | Soft check ≠ atomic safety | Never authorize side effects with stale Noul alone |
| **Contracts & invariants (FM)** | Exact properties stay exact | Dafny/TLA+/Alloy own proof; judgment triages what to prove |
| **DST / falsification** | Explore concrete failures | Antithesis/PufferLib; judgment ranks interesting traces |
| **STAMP / systems safety** | Accidents from interactions | Leveson: judgment monitors constraints, not blame |
| **NATM / observational design** | Adapt to measured ground | Instrument → judge → revise policy (not big-bang proof) |
| **Norman gulfs** | Execution/evaluation gaps | Product & org UX: which gulf does judgment close? |
| **Situated software (Shirky)** | Context-bound tools | Local taxonomies; don’t universalize one Choice set |
| **Data & Reality (Kent)** | Models ≠ world | Soft categories drift; re-eval on your data |

## Domain sketches (non-SWE)

**Business:** go/no-go, pricing tier Choice, lead scoring, hiring stage gates — policy owns money/legal; model owns semantic fit.
**Knowledge work:** triage inbox, rank sources, “is this claim supported?”, meeting next-step Choice — VOI for research depth.
**Life:** medical info triage (not diagnosis as authority), travel option ranking, “enough sleep to drive?” as Noul with hard policy — irreversible stakes stay human.
**AI systems:** tool/skill routing, context sieve, env-break taxonomy — mixed architecture.

## Harm across domains
Soundness theater; hard-gating soft judgment; vibe-coded “specs”; treating Choice as preference revelation for ethics; automation without abstention path.
