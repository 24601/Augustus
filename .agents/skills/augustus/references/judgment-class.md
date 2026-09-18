# The judgment-model class (Jev is exemplar, not monopoly)

Augustus designs for the whole class of **fast, cheap
categorization / classification / scoring models** that return a bounded
answer software can act on — not only TypeSafe Jev. Jev is the documented
exemplar (typed Choice / Score / Noul, calibrated decision objective, live
docs). Neighbors in the class are substitutes or cousins, not a reason to
fork this skill into an install guide.

Integration contracts for Jev stay in `typesafe-ai` + live docs. Other
families own their own cards/READMEs. This file is **which family fits the
hole**, what the objective implies, and what that does to agent
architecture.

Status: **Contract** only for TypeSafe docs you re-read live; everything
else here is **Empirical recipe** (named paper/repo) or **Hypothesis**.

## The class

A model is in-class when most of these hold:

- Input is language, structured text, or (for vision scorers) an image plus
  a closed label/region set.
- Output is a score, a distribution, or a label — not a paragraph.
- Latency/cost is in the "run per chunk / per hunk / per frame" band, not
  "one call per user turn."
- Code, not the model, owns side effects.

Out of class: generative LLMs used as classifiers (prompt → JSON);
regexes/lookups that already work; trained heads on a frozen labeled
taxonomy with enough of *your* data (XGBoost still wins there —
`faq.md`).

## Families

| Family | What it optimizes | Typical output | Use when | Watch |
|---|---|---|---|---|
| **Closed decision API** (TypeSafe Jev) | Calibrated decision (proper-scoring / RLCD lineage) | Choice / Score / Noul + distributions | Default when you need act/abstain, fan-out, documented envelope | Cloud, pin version, re-measure on your data |
| **Open System-1 head** (Laya, openjev, LightJev, openjev-lm) | Same *shape* as Jev, you host it | Same primitives or logits-as-options | Air-gap, $0/token, inspectable weights | Self-eval duty; Laya text-only, 512 tok; vendor vs-Jev tables are claims (`notes.md` §18). Distill of a *teacher* (openjev-lm 92.9% on 70 gold) is not independent gold (`notes.md` §25) |
| **GLi\* encoder family** (GLiNER locate / GLiClass categorize / GLiNER2.5 local multi-head) | One-pass labels-in-encoder; spans, sequence labels, or both | Spans + types; per-label sigmoid/softmax; optional relations/records | Laptop/local; large or changing label sets; "what's *in* the text" vs "what *is* the text" | Affinities are not automatically a gateable P(permit). Species map below. Not a Jev how-to and not a GLiNER install |
| **Listwise / pairwise discriminative ranker** | Order of a list (nDCG, softmax-over-list) | Relevance scores, not P(relevant) | Rerank a retrieved shortlist | Translation-invariant listwise losses are **not** calibrated for thresholds ([listwise vs pointwise](https://doi.org/10.48550/arxiv.2208.06164); [RCR](https://arxiv.org/html/2211.01494v2)). Fail **open** (keep retrieval order) |
| **Vision scorer** | Image–text affinity or region Choice | Cosine/sigmoid affinity, or a closed region/label pick | Perception as classification over *candidates you extracted* | CLIP softmax = competition in the offered set; SigLIP sigmoid = pairwise affinity, not class-conditional p ([SigLIP](https://huggingface.co/docs/transformers/v4.39.2/en/model_doc/siglip)). Not a VLM captioner |

Pick the family from the **hole**, then pick a vendor. Do not start from a
logo.

## Species map (GLiNER is a peer, not a footnote)

The class is several *species* that share "fast cheap bounded answer,
code owns side effects." They are not aliases.

```text
locate      GLiNER (span NER)              what's *in* the text
categorize  GLiClass (sequence labels)     what *is* the text
decide      Jev / Laya / openjev           Choice / Score / Noul over a state
rank        listwise / cross-encoder       order a retrieved shortlist
perceive    CLIP / SigLIP / region Choice  score candidates you extracted
```

- **Locate.** [GLiNER](https://arxiv.org/abs/2311.08526) (Zaratiana et al.,
  NAACL 2024): bidirectional encoder; open entity types in one forward
  pass; output is *spans*. Mental model: keep/drop over candidates the
  encoder proposed (`applied-mappings.md` §2), not a Noul over the
  document. Downstream code still owns policy.
- **Categorize.** [GLiClass](https://arxiv.org/abs/2508.07662)
  (Knowledgator): GLiNER's architecture adapted to sequence
  classification. Labels interact in one pass (not sequential
  cross-encoder pairs). Good for large/changing tag sets. Cousins:
  NLI zero-shot, SetFit, ModernBERT heads.
- **Local multi-head.** [GLiNER2.5](https://github.com/fastino-ai/gliner2)
  (fastino-ai; 74M/194M/287M, CPU-first): entities + classification +
  records + relations in one schema. Discourse (2026-09-18): same
  *agentic decision* jobs as Jev, local / free / laptop; a 36× Browser
  Use cost claim is a tweet, not a re-run (`notes.md` §25).
- **Decide.** Typed Choice/Score/Noul with a decision/proper-scoring
  objective. That is Jev's product claim. Open heads copy the *shape*;
  distillation copies the *teacher* (openjev-lm).

A GLiNER span is not a drop-in Noul. A GLiNER2.5 classification head can
*sit in* the decide hole on a laptop only after *your* ECE and a fail
policy. Spans that authorize an irreversible act are the rejected design
(same as CLIP-as-gate). Do not copy extract APIs into this skill.

## Listwise discriminative vs decision objectives

This is the fork that decides fail-open vs fail-closed.

**Discriminative / ranking objective.** Pairwise or listwise losses
(RankNet, ListNet softmax-over-list) improve *order*. Logits measure
relative relevance. Many such losses are translation-invariant: adding a
constant does not change the ranking and **destroys** any reading of the
number as P(click) / P(relevant). Cross-encoders (monoBERT, Cohere-style
rerank) are usually this family even when they emit a "score."

**Decision objective.** Pointwise proper scoring rules (log/Brier/
spherical; RLCD) train the model so a number *means* a belief you can
threshold. Abstention, per-action bars, and "permit ≠ confidence" only
make sense here. Jev's product claim lives on this side. Open heads that
copy Choice/Score/Noul without a proper-scoring train loop may *look*
like Jev and still be uncalibrated — measure.

**GLi\* sits beside decide, not inside it by default.** Locate (GLiNER)
proposes spans; categorize (GLiClass) fires document labels; local
multi-head (GLiNER2.5) can do both plus relations. Classification
sigmoid/softmax *can* be a cheap multi-label sieve. It is not, without
your calibration plot, a decision API. Great for "which of these 80
tags fire" or "which spans are the allergy / the amount / the verb";
not a silent fail-closed authorize. The 255-option Choice limit is
Jev's, not the class's — this family is why.

Rule of composition (`applied-mappings.md` §4):

```text
ranking error  → quality  → fail open (keep the retrieved order)
selection/auth → control  → fail closed, needs a decision-shaped number
```

A listwise reranker plus a decision gate is a valid mixed stack. A
listwise reranker *as* the gate is the rejected design.

**Empirical recipe (Han Xiao trolley, 2026-09-18).** Wrapping
[jina-reranker-v3.5](https://x.com/hxiao/status/2100973209114075330) in a
Jev-style API and asking the trolley problem: it **always pulls the
lever**, whether one person dies or one billion. Relevancy ≠ decision
rationality. I/O compatibility ("it returns a Choice") is not an
objective match. Never treat a listwise retrieval scorer as an
ethics/value Choice without a policy that is *not* the ranker.

## Vision scoring patterns

Perception is candidate generation plus scoring — the same keep/drop card
(`applied-mappings.md` §2), with pixels or an accessibility tree as the
parser.

1. **Pixel-free (preferred when the environment is already structured).**
   RAM / AX tree / object JSON → closed action or region set → Choice.
   Prices and dates stay in code. Launch-week recipes: typesafe-mario,
   jev-drone (classical CV → symbols, Jev advisory), lizard-agent
   (visible elements only). The model never sees a screenshot.

2. **Region / label Choice over extracted boxes.** Perception (detector,
   grid, SAM, OCR boxes) proposes candidates; a scorer picks. `hr98w/jev-visual`:
   Breakout only worked after reducing control to "which region holds the
   ball" — decomposition in miniature. Do not ask a vision model to
   *invent* the paddle command.

3. **Dual-encoder affinity (CLIP / SigLIP / cousins).** Argmax over prompt
   templates is zero-shot classification. CLIP-family softmax induces
   competition among the offered labels; SigLIP's pairwise sigmoid is an
   affinity, flatter closed-set margins, weaker as a probability
   ([posture-classification note](https://arxiv.org/html/2510.13364v1)).
   Calibrate or conformalize before a safety gate; class-conditional
   coverage can collapse under shift even when marginal coverage looks
   fine ([VLM conformal audit](https://arxiv.org/html/2608.19376v1)).

4. **VLM-as-judge.** A captioning/chat model asked "is this safe?" is
   *generation*. Verbal scores are not calibrated. Use it to *propose*
   labels or describe, then score with a class model — or don't.

Laya's card is text-only / 512 tok: a vision hole is not "run Laya on a
caption." Either pixel-free the state or pick a vision-family scorer.

## Portents for agent architecture

Cheap judgment as a **control plane** around a generator is the
capability shift, independent of vendor:

1. **Full-traffic, not sampled.** Per-step, per-hunk, per-line, per-frame
   judgments were known and too expensive. They are now the default
   design (OpenSmoke, jevprune, git-jev-stage, firehose). Agents that
   still LLM-judge 2% of traces are leaving the economics on the table.
2. **Skills and tools become a catalog + decision**, not a stuffed
   system prompt. Rank-then-verify, reject-all first-class
   (`applied-mappings.md` §5). Large label sets may prefer a GLi\*
   one-pass (GLiClass tags, GLiNER spans) over a 255-option Choice —
   that limit is Jev's, not the class's.
3. **Two numbers, two jobs.** Ranking scores order context. Decision
   scores authorize. Harnesses that collapse them will either stall
   (fail-closed on a listwise number) or leak (fail-open on a gate).
4. **Perception is not narration.** Computer-use and robotics that
   caption the world then plan in prose are on the wrong side of the
   class. Extract candidates, score, act; generate text only when
   something must be typed.
5. **Open heads and GLi\* make the control plane local.** Air-gap /
   on-device / laptop (GLiNER2.5 74M–287M CPU-first; openjev-lm 0.5B
   LoRA overnight on 6 vCPU) become newly feasible *if* you accept
   self-eval and envelope limits. They do not make calibration optional.
   Distilling a hosted teacher is not independent gold.
6. **Cross-modal is still thin.** Discourse, GLiNER/GLiClass, and Laya
   are text-first. Vision is a scoring pattern (above), not a shipped
   omni decision API. Treat "Jev but for images" as a hole to fill with
   the vision-scorer family, not as a slogan. Locate (spans on a
   screenshot OCR) is still locate, not perceive.
7. **The agent that only has a generator is incomplete.** The missing
   organ is a judgment-class model plus policy in code — not another
   prompt. The agent that only has a ranker is also incomplete: it can
   sort, it cannot abstain.

None of these portents require TypeSafe. They require picking a family
whose *objective* matches the action's fail policy, then falsifying on
your labels.

## Decision-design extras for class choice

When the request is "Jev vs GLiNER vs GLiClass vs CLIP vs a cross-encoder":

```text
Hole (sieve / keep-drop / triage / rank / route / gate / perceive):
Family (from the table) and why the objective matches the fail policy:
What the generator is still for:
Envelope (tokens, modality, label-set size, latency budget):
Self-eval duty (closed API vs open weights vs affinity scores):
Smallest experiment that could reject this family, not just this vendor:
```

Propose two families if the hole is mixed (e.g. listwise rerank +
decision gate). Do not invent a hybrid API.
