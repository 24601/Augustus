# Question design & diagnosis mechanics (Contract — distilled from dbreunig/building-with-jev-skill, doc-grounded for jev-1.13; cross-checked against then-current docs 2026-09)

This card is the mechanics layer: how to write questions, state, and answer
composition, and how to diagnose a failing question. The mental-model and
substitution cards (mappings.md, toolbox-mapping.md) assume you are already
asking well-formed questions; this is how you get there.

The design rules here are portable. The **numbers and field names are not
this card's to own**: envelope sizes, option/level limits, and the accepted
shape of a request body are contract surface, pinned below to jev-1.13 as
of 2026-09. Re-read the live docs (or `typesafe-ai`) before you write a
request, and treat a stale pin as a prior, never a setting.

## The workflow (doc-grounded)

1. List the decisions your code must make; write each as a branch, threshold, or ranking.
2. One question per judgment. Split any question that weighs two properties.
3. Pick the primitive whose answer code acts on directly.
4. Build the smallest state that answers every question; compute in code whatever code can compute.
5. Put every question sharing the state into **one request** (speculative fan-out — parallel questions cost little latency; code ignores unneeded answers). Second requests only when later data depends on an earlier answer. Extractive / pointer: number the candidates in **code**; ask per-id Noul/Choice; copy verbatim. "Not found" is an option. The model never writes the quote (`applied-mappings.md` §2; `notes.md` §48).
6. Combine in code: branches, weights, confidence gates.
7. Test on labeled examples; read `probabilities` on the misses; revise one or two questions at a time.

## Hard facts to design around

- Budget: state + all questions share **64k tokens**; state plus the longest single question must fit in **32k**.
- A **Noul has no confidence field** — its distance from 0.5 plays that role. Noul 0.5 means unsure, not "medium."
- `confidence` measures how **peaked** the distribution is — a property of the model's answer, not a correctness guarantee.
- `score` is the probability-weighted mean of level numbers; 1.0 can mean certainty at level 1 or a split. Levels are weakly calibrated as numbers: threshold, rank, or round — **do not interpolate quantities** from a Score.
- Jev does not count or do arithmetic or date math. Ask per-item Nouls in one request and sum in code; extract date parts with Choices (with a "not stated" option) and compare in code.
- Every answer stays inside the supplied options — code never parses prose. **Conflict ≠ ignorance:** a Noul has nowhere to put "both and neither." Name those states as Choice options or the model will collapse them (typed-evaluation-collapse; `notes.md` §69). Same family as missing `other` → confident wrong.
- Questions on one request never see each other's answers.
- Text in the state can steer the answer; Jev does not treat state as hostile. State in criteria what counts; test injected and self-describing content before deployment.

## Instruction shape

- State the exact condition; Jev reads scoping words, negations, and implied conditions at face value. Crisp beats evaluative ("Does the resume state the candidate used Python at work?" not "Is this candidate strong in Python?").
- Name the judged state path in backticks (`` `ticket.messages[0].text` ``).
- One property per question — hidden second judgments lower accuracy and confidence.
- Keep numerals-for-levels out of instructions ("Rate from 0 to 2" gives nothing to match); write the full question in `instructions` (the question ID never reaches the model); keep decision policy out of questions (policy lives in code).
- Instructions accept prose or a structured form (the live docs own which keys that form accepts — do not write them from this page). The design rule is what transfers: name the sub-parts of the judgment explicitly instead of packing them into one sentence, and pass schemas/taxonomies as JSON, not as serialized strings.
- When you catch yourself explaining what you meant after a wrong answer — that explanation is the missing half of the instruction. Add it.
- **Sentence as rule:** a natural-language sentence can *be* the criterion when a matcher already extracted the subject ([jevlint](https://github.com/mizchi/jevlint) ast-grep `rule:` × Jev `ask:`). Do not pack two properties into the sentence. Mechanical defects stay with the compiler; contradiction of a declared contract is the System One hole. Not SWE-only: any artifact that names itself (policy, checklist, form, recipe) can be a subject × a sentence. Qualify vs huntedman/JevLint. `notes.md` §70.

## Criteria shape

- Criteria are an extension of the instruction and must ask the same thing, in the same direction (a Noul whose `true` side describes "no" performs worse).
- Choice options: contrastive `what` / `not_for` / short concrete `examples` (instances, not descriptions of instances). Add an `other` / `none-of-the-above` when the list may not cover inputs. Skipping that hatch is not a style nit: the model will pick a listed option at confidence 1.00, and no downstream gate will see a problem (`notes.md` §46). Request-shape lint (wellposed / `tenbin`) puts the hatch on the offered set; **training must confront it as a wrong alternative too**, with varied wording, or the model learns "this wording ⇒ pick it" ([kev](https://github.com/jaredpalmer/kev) first-run shortcut; dedicated `none_of_the_above` eval; `notes.md` §45 delta). Corpus-scale cousin (maker claim, not re-run): SEO internal-link audit **584** placed / **139** refused because nothing honestly fit — Choice-with-`other` at catalog scale (`notes.md` §45–§46, §56). Computer-use cousin: Stagehand pick asks `best` (no none) **and** `strict` (with none; vetoes above 0.9); ambiguity **stops rather than guesses** (`notes.md` §57).
- Score levels (2–10): describe **situations**, one dimension each, each standing alone (Jev sees neither the level's number nor its neighbors — "worse than previous" means nothing). No numerals. Levels may be objects `{"summary", "signals"}`. Give a rare extreme its own level when code treats it differently.
- Composite scoring: one Score per dimension, normalize by `len(criteria)-1`, weight and combine in code. Change policy by changing weights — never by rewriting questions.
- Taxonomy walk: one Choice per tree level, walk in code; each option's value is its subtree (direct children + sample leaves); follow several branches when probabilities are close.

## Diagnosis table (symptom → cause → fix)

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Wrong answers, high confidence | Instruction read literally | State exact condition; put boundary cases in criteria |
| Wrong answers, high confidence, **nothing in state that could answer** | Bare recall / missing evidence | **Retrieve first**; put the passage in `state`. Atlas history: wrong@0.90 without context → right@0.97 with passage. Confidence gating on recall is not enough (Case A was 0.90 *and wrong*). `notes.md` §49 |
| Wrong answers, **dangerous-high** ECE on overlapping labels | Population calibration failed (blurred categories) | Do not threshold. DAIR Emotion: 48% acc / mean conf 0.819 / 16% p(correct)=0. Plot reliability on *your* labels |
| Wrong answers, **confidence ~1.00**, no `other` | Forced pick: the offered set does not cover the input; the model *must* choose | Add `other` / none-of-the-above. **Confidence gating cannot catch this** ([wellposed](https://github.com/suraj-phanindra/wellposed) live probe: unsubscribe email → `"support issue"` at 1.00 without `other`, `"other"` at 0.93 with it). Overlapping options collapse confidence (loud). `notes.md` §46. `tenbin` owns the lint skill |
| Residual `"other"` always picked (or never) | Training saw none-of-the-above only as the true label — a wording shortcut | Confront the hatch as a *wrong* alternative too; vary wording; eval present-vs-removed ([kev](https://github.com/jaredpalmer/kev) `none_of_the_above`; `notes.md` §45 delta). wellposed still owns request-shape lint |
| Question names a state path that does not exist | Dead reference; the API still answers | Lint the request (walk JSON). Structural, not semantic. wellposed recipe; do not copy the CLI |
| Low-confidence Choice | Options overlap / none fits | `what`/`not_for`/`examples`; add `other` |
| Low-confidence Score | Overlapping levels, two dimensions, thin state | Distinct-situation levels; split question; add state field |
| Scores cluster mid-scale | Levels are degrees/numbers | One concrete situation per level; remove numerals |
| Top-of-scale cases look alike | Extreme case has no level | Add a level for the extreme |
| Noul hovers ~0.5 | Vague condition | Crisp condition; add `true`/`false` criteria with examples |
| Accuracy falls as inputs grow | Irrelevant state detail | Filter in code; send only needed fields |
| Errors on counts/sums/dates | Jev is doing arithmetic | Move arithmetic to code |
| Errors on nested/negated questions | Too much indirection | Direct question, named path, split + combine in code |
| Answer follows state text | Content steers the model | Tighten criteria; adversarial tests; confidence-gate the action |
| Rewording trades one error for another | One question, several properties | Split into atomic questions |
| Synonymous wording swings p / the act | Stimulus includes question text; no invariance promised | Paraphrase-pair eval; abstain or raise t; rewrite (`mappings.md` §17) |
| Question has no answer yet (edit 1 of 12) | Observation window is wrong: a turn-level property asked at edit time | Name when the evidence exists. Edit-phase vs turn-phase is a question-design cut, not a hook detail ([Abide](https://github.com/coldteadotai/abide): "added more than asked" is a turn rule). `notes.md` §47 |
| Review is green on the diff; the rest of the repo violates the stated intent | Observation window is the *diff*, not the places the intent applies | Search the whole repo after the change; one small question per place; **UNKNOWN** is cheaper than a false VERIFIED. Empty search ≠ proof ([jev-intent-review](https://github.com/yottayoshida/jev-intent-review)). `notes.md` §70 |
| Naming/comment "rule" as a paragraph the linter cannot prove | The sentence is the criterion; AST/ast-grep already extracted the subject | Put the sentence in `ask:`; matcher silent-fail vs Jev loud; fail-open if no verdict ([mizchi/jevlint](https://github.com/mizchi/jevlint); ≠ huntedman/JevLint). `notes.md` §70 |
| Catalog tagged "because it mentioned AI" | Criteria omitted what *doesn't* count | Add one exclusion sentence; 36/100 → 6/100 *theirs* ([jev-cookbook](https://github.com/nexibeo/jev-cookbook) TemplatesGrokBot). `notes.md` §71 |
| One severity Score bunches in the middle | "How bad" hides several yes/no properties | Split into concrete Nouls (cookbook log triage 4/7 → 7/7 *theirs*). `notes.md` §71 |
| Gateway returns no `confidence` | The statistic is missing, not "uncalibrated" | Reconstruct margin; lower the bar on *that* backend; tune on your traffic ([jev-use](https://github.com/shitianfang/jev-use) 17/20 → 0/20). `notes.md` §71 |
| README badge ECE vs a different channel | Like-for-like channels; n and CI | Dual-channel ECE is a design fork; do not put correctness-head 1.44% beside distribution 21.40% ([openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0) PR #1). `notes.md` §71 |
| Each answer right, decision wrong | Policy wrong | Change weights/thresholds in code, leave questions alone |

## Revision discipline

- Change one or two questions per revision; probabilities shift unpredictably — leave good discriminators untouched.
- Judge revisions on labeled data; higher confidence alone proves nothing.
- Keep the answer space stable once code depends on it (changing levels/opts rewrites every earlier answer's meaning).
- General rules in instructions/criteria; specific names/values only in `examples`.

Confidence-gated routing (doc defaults): act / confirm-or-flag / hand off, floors 0.5–0.6, 0.85–0.9 for high-stakes — starting points, not constants (calibration must be re-measured per dataset; see validation.md).
