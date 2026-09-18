# Mental models for placing System One judgment (across domains)
**Date:** 2026-09-18  
**Companion to:** `FORMAL-METHODS-SYSTEM-ONE.md` (formal/semi-formal is **one pillar**, not the whole sky)  
**Audience:** Augustus De Morgan — design-judgment beyond SWE
**Seed table:** `MENTAL-MODELS-SEED.md` (compact frame→placement matrix; keep both)

TypeSafe **Jev-class** tools (Choice / Score / Noul + code-owned policy) are cheap, typed, distributional judgments. They become dangerous or magical depending on the **mental model** of the slot they occupy. This note catalogs mathematical / logical / algorithmic frames for *placement* across AI systems, modern SWE, business decisions, knowledge work, and everyday life.

Statuses: **Contract** (matches Jev/Augustus docs) · **Empirical recipe** · **Hypothesis**.

---

## 1. Master rule (all domains)

**Judgment estimates; policy decides; the world confirms.**  
Composition-algebra: Jev never performs the side effect. Irreversible concession belongs to a **probe** (measurement, receipt, test, signed commit) — not to a Noul.

Cross-link FM pillar: TOCTOU is the universal name for "checked with a soft estimate, then acted as if the check were still true."

---

## 2. Decision theory & selective classification

| Idea | Placement of Jev-class | Caveat |
|---|---|---|
| **Expected utility** | Score/Noul features enter EU calculation; **code** owns utilities & actions | Utilities are value judgments — don't hide them in the prompt |
| **Selective classification / abstention** | Confidence bands → act / abstain / escalate (**Contract** confidence-routing) | No universal τ; calibrate per action & population |
| **Cost-sensitive threshold** | For calibrated binary p: `τ = C_FP/(C_FP+C_FN)` (**Contract** mappings) | Requires YOUR costs & calibration, not blog defaults |
| **Value of information (VOI)** | Noul "is more evidence worth it?" as *meta*-gate before buying data/tests | VOI needs a model of downstream utility; else it's vibes |
| **Satisficing vs optimizing** | Choice for "good enough" menus; Score for graded quality | Don't run MCTS theater when satisficing is the real goal |

**Everyday:** leave-or-stay, buy-or-wait, send-or-edit — same abstention geometry as prod incident gates.

**Business:** hire / no-hire / more-interviews as selective classification with asymmetric costs.

---

## 3. Bayesian updating & calibration

| Idea | Placement | Caveat |
|---|---|---|
| **Likelihood-ish features** | Nouls as *inputs* to a Bayesian/logistic layer (CatBoost recipe) | Noul ≠ calibrated P(event) on your base rate |
| **Calibration plots** | Mandatory before thresholds (**Contract**) | Open encoders can beat ECE; still verify |
| **Base-rate neglect** | Force priors in code for rare incidents/fraud | Soft models amplify vividness bias |
| **Conformal prediction** | Distribution-free sets around System One outputs (neurosymbolic conformal classif.) | Sets need exchangeability assumptions — say them |

**FM link:** conformal abstention is the statistical sibling of "model checker didn't explore that; don't claim it."

---

## 4. Multi-criteria decision analysis (MCDA)

| Idea | Placement | Caveat |
|---|---|---|
| **Named criteria** | One Score/Noul per criterion; judge once; re-weight in code (**Contract** mappings §1) | Score units don't transfer across concepts |
| **Pareto / non-compensation** | Hard constraints separate from compensating weights | Weighted sum hides veto criteria |
| **Rubric versioning** | Version questions with the consumer model | Silent rubric drift = silent policy change |

**Knowledge work:** paper triage, vendor scorecards, grant panels — same pattern as 1018-paper cookbook.

---

## 5. Ranking & choice theory (intuition only)

| Idea | Placement | Caveat |
|---|---|---|
| **Plackett–Luce / listwise** | Choice over ≤255 options; prefilter first (**Contract**) | Cross-pool Choice probs not comparable |
| **Arrow-style impossibility (intuition)** | Don't expect one Score to be "the social welfare function" | Aggregation policy is political — put it in code review |
| **Tournament brackets** | Usually **anti-pattern** for unstructured sets | Prefer retrieval + shared rubric |

---

## 6. Search & planning components

| Construct | Jev-shaped hole | Governing caveat (Augustus) |
|---|---|---|
| **A\*** | Heuristic h(n) from Score | Inadmissible heuristic → only informal guidance |
| **Beam search** | Choice as branch priority | Geometric path score ≠ leaf probability |
| **MCTS / PUCT** | Priors + leaf values from Choice/Score; Noul prune (**Empirical recipe** archive) | Grounded vs speculative env typed; probe concedes |
| **Bandits** | Arm = Choice option; reward from later probe | Don't use Noul as reward without outcome |

**AI systems:** tool-routing, skill selection, debate path expansion.  
**Life:** itinerary planning — beam over cities; hard constraints (passport, budget) in code.

---

## 7. Control theory & hysteresis

| Idea | Placement | Caveat |
|---|---|---|
| **Setpoint vs estimate** | Jev estimates process variable; controller policy in code (foreman pattern) | Model never commands actuators directly |
| **Hysteresis** | Separate enter/exit thresholds for alarms | Prevents flapping in ops & relationships |
| **Deadbands** | Abstain region around τ | Maps to selective classification |
| **Observers** | Soft sensors for latent state (tone, progress, risk) | Validate against occasional hard sensors |

**STAMP/STPA (orgs):** soft estimates feed controllers; **safety constraints** are separate. "We run sentiment on tickets" ≠ hazard control.

---

## 8. Signal detection (ROC, DET, cost curves)

| Idea | Placement | Caveat |
|---|---|---|
| **ROC / PR curves** | Sweep τ on held-out; publish cost curves | Accuracy at one τ is vanity |
| **d' / criterion** | Separate sensitivity of model from policy bias | Leadership often moves criterion while blaming model |
| **Alert fatigue** | Score severity → rate-limit in code | Pure Noul gates without budget destroy recall (**SYNTHESIS** hard boundary) |

---

## 9. Mechanism design & auctions (lite)

| Idea | Placement | Caveat |
|---|---|---|
| **Scoring rules** | Score as reported belief; payoffs for honesty are rare in apps | Without incentives, expect gaming |
| **Allocation Choice** | Assign scarce resources (GPU, reviewer time, seats) | Strategy-proofness not free — assume gaming |
| **Second-price intuition** | Separate "value estimate" (Jev) from "payment rule" (code) | Don't let the estimator set both |

**Business:** ad ranking, marketplace listing quality, incident commander assignment.

---

## 10. Operations research (routing, assignment, scheduling)

| Idea | Placement | Caveat |
|---|---|---|
| **Assignment costs** | Soft affinity Score + hard feasibility ILP/heuristic | Soft costs cannot violate capacity/legality |
| **Routing** | ETA risk Score; constraints in solver | Don't replace VRP solver with Choice |
| **Priority queues** | Score urgency; FIFO/fairness policy in code | Starvation is a policy bug |

---

## 11. Epistemology & evidence standards

| Idea | Placement | Caveat |
|---|---|---|
| **Evidence levels** | Score strength-of-evidence; Noul "is this an RCT?" (mappings example) | Ontology errors (Kent) dominate |
| **Burden of proof** | Who must produce the probe? | Soft denial ≠ disproof |
| **Peer review vs measurement** | Choice venue fit; measurement owns claims | Citation Nouls check support, not truth |
| **Absence of evidence** | Empty Choice shortlist ≠ "no good option" | Retrieval recall separate from rerank |

**FM link:** Amazon "what must go right?" vs "what might go wrong?" — write positive invariants; soft brainstorming of failures is incomplete by construction.

---

## 12. Crossover metaphors as *life/business* frames

(See also FM §1 — same metaphors, non-SWE emphasis.)

| Metaphor | Everyday / business reading | Judgment slot |
|---|---|---|
| **NATM observational method** | Launch thin; instrument; thicken support only where gauges move | Soft metrics as gauges; capital spend as lining |
| **Snap-fit** | Hiring, partnerships, API contracts — designed lead-in & release force | Trial periods = lead-in; severance/refund = release |
| **Norman gulfs** | Consumer product & org process UX | Soft judgment reduces evaluation gulf; training/UI reduces execution gulf |
| **Leveson STAMP** | Hospital wards, airlines, trading firms | Map controllers; soft ML is one sensor |
| **Shirky situated software** | Internal tools for 30 people | Dense Jev loops OK; don't fake public scale |
| **Vanderburg Real SE** | Any craft under uncertainty | Models + measurements; slogans aren't engineering |
| **Debugging (Agans)** | Incidents & personal stuckness | See → stabilize → find evidence → fix → verify — Jev helps "see/classify," probes verify |

---

## 13. AI-systems placement map (non-FM)

| Layer | Soft judgment | Must stay hard |
|---|---|---|
| Retrieval | Rerank Score/Noul | Index completeness |
| Tools | Choice tool + arg judgments | AuthZ, schema, side-effect allowlist |
| Memory | Salience Score | Encryption, retention policy |
| Eval | Judge models as metrics | Human gold / outcome labels for promotion |
| Multi-agent | Local perception Choice | Global invariants, budgets, stop conditions |

---

## 14. Harm patterns that recur in every domain

1. **Laundering** — estimate presented as measurement.  
2. **TOCTOU** — soft check then irreversible act.  
3. **Unit fiction** — treating Scores as interchangeable currency.  
4. **Independence fiction** — multiplying Nouls as joint probability.  
5. **Threshold cargo-cult** — copying τ from a demo.  
6. **Ontology capture** — Choice set smuggles the conclusion.  
7. **Optimization on the judge** — Goodhart when Score is the objective.  
8. **Coverage theater** — "we classified everything" without probes.  
9. **Scale mismatch** — Web-School metrics on situated problems (and vice versa).  
10. **Vacuous assurance** — property or rubric that can't fail (Hillel vibing specs; Cauli vacuous models).

---

## 15. Augustus skill-card seeds (non-FM)

Add as Hypothesis cards with acceptance tests before promotion:

1. **VOI gate** — Noul/Score whether to buy more info; code owns budget.  
2. **MCDA scorecard** — fan-out criteria; Pareto UI.  
3. **Control loop with hysteresis** — dual thresholds; model never actuates.  
4. **Cost-curve ops** — publish FP/FN $ with every gate PR.  
5. **Assignment hybrid** — soft affinity + hard solver.  
6. **Evidence rubric** — Score evidence strength; hard citation checks separate.  
7. **Situated density** — allow aggressive soft loops only inside named community boundary.

Traverse with composition-algebra positions 1–11 × these constructs (application generator).

---

## 16. How this relates to formal methods

FM / semi-FM / DST (Antithesis, Resonate Lean+oracle+DST, Alloy, TLA+/Quint/P, Dafny, …) are the right pillar when **wrongness is intolerable and the model can be made precise**. Mental models above still apply: FM artifacts occupy the *probe / constraint / explorer* roles; Jev-class occupies *estimate / triage / UI / prior* roles. See `FORMAL-METHODS-SYSTEM-ONE.md`.
