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
5. Put every question sharing the state into **one request** (speculative fan-out — parallel questions cost little latency; code ignores unneeded answers). Second requests only when later data depends on an earlier answer. Extractive / pointer: number the candidates in **code**; ask per-id Noul/Choice; copy verbatim. "Not found" is an option. The model never writes the quote. **Evidence-synthesis scale ([choxos/jev-reviewer](https://github.com/choxos/jev-reviewer), ≠ egma-ai):** fan-out every question over shared chunks, then a **second** absolute Noul ("does this line itself answer?") for multi-row tables; human tick never overwritten (`applied-mappings.md` §2; `notes.md` §48, §74).
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
- **Sentence as rule:** a natural-language sentence can *be* the criterion when a matcher already extracted the subject ([jev-lint](https://github.com/mizchi/jev-lint) is [jevlint](https://github.com/mizchi/jevlint) rename; ast-grep `rule:` × Jev `ask:`). Do not pack two properties into the sentence. Mechanical defects stay with the compiler; contradiction of a declared contract is the System One hole. Not SWE-only: any artifact that names itself (policy, checklist, form, recipe) can be a subject × a sentence. Qualify vs huntedman/JevLint. `notes.md` §70, §100.

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
| Naming/comment "rule" as a paragraph the linter cannot prove | The sentence is the criterion; AST/ast-grep already extracted the subject | Put the sentence in `ask:`; matcher silent-fail vs Jev loud; fail-open if no verdict ([mizchi/jev-lint](https://github.com/mizchi/jev-lint) is jevlint rename; ≠ huntedman/JevLint). `notes.md` §70, §100 |
| Catalog tagged "because it mentioned AI" | Criteria omitted what *doesn't* count | Add one exclusion sentence; 36/100 → 6/100 *theirs* ([jev-cookbook](https://github.com/nexibeo/jev-cookbook) TemplatesGrokBot). `notes.md` §71 |
| One severity Score bunches in the middle | "How bad" hides several yes/no properties | Split into concrete Nouls (cookbook log triage 4/7 → 7/7 *theirs*). `notes.md` §71 |
| Gateway returns no `confidence` | The statistic is missing, not "uncalibrated" | Reconstruct margin; lower the bar on *that* backend; tune on your traffic ([jev-use](https://github.com/shitianfang/jev-use) 17/20 → 0/20). `notes.md` §71 |
| README badge ECE vs a different channel | Like-for-like channels; n and CI | Dual-channel ECE is a design fork; do not put correctness-head 1.44% beside distribution 21.40% ([openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0) PR #1). `notes.md` §71 |
| Coverage 1.00, wrong `__none__` | Format-mass ≠ correctness; small-n theater | Measure `__none__` gold and shuffle/mix; do not threshold coverage ([chakuho](https://github.com/taku-me/chakuho) 8B 3/30 vs 27B 29/30). `notes.md` §72 |
| English checkpoint on Khmer/Hebrew | Confident-wrong OOD; p never drops | Route by **script before** the forward pass; do not wait for gating ([laya-multilingual](https://huggingface.co/convaiinnovations/laya-multilingual)). `notes.md` §72 |
| Commit "0.4, so pass" | Middle band is not a verdict | Report `"review"`; Nouls decide, Choice headlines ([commitjev](https://github.com/yodablocks/commitjev)). `notes.md` §72 |
| Plugin named Jev, key is Agnes | Branding ≠ backend | Read the client ([hermes-plugin-jev](https://github.com/Mrmimee/hermes-plugin-jev) is chat-completions). `notes.md` §72 |
| Quoted F1 without eval/README | `/benchmark` is tracked JSON; n=7 train-on-test | Read eval/README first; ~0.03 is a coin flip ([classifier-dev](https://github.com/mrmps/classifier-dev)). `notes.md` §73 |
| Docs say 0.800, serving 0.546 | Silent fallback is a lie about the instrument | Mark `FALLBACK`; rh-guard owns the gate ([classifier-dev](https://github.com/mrmps/classifier-dev) granite *theirs*). `notes.md` §73 |
| Escalate every multi-label on smart | Re-judge made it worse (23 s) | Smart is single-label <0.7 only; 0.7 is *theirs*. `notes.md` §73 |
| Paraphrased "quote" from a paper | Generator invented the excerpt | Point at line ids; copy verbatim; *Not found* is an answer ([choxos/jev-reviewer](https://github.com/choxos/jev-reviewer), ≠ egma-ai). `notes.md` §74 |
| One pass on a table with two Age rows | Relative Choice is not an absolute check | Two-pass: which-line Choice, then "does this line itself answer?" Noul. `notes.md` §74 |
| Unchecked extraction entered the review | Human tick skipped as chrome | Checked answers never overwritten; tick is the product. `notes.md` §74 |
| LocalJev JSON p used as a Noul | Self-reported vector ≠ logit read | Calibrate on *your* labels; wire-compat ≠ logit-equiv ([githubnext/localjev](https://github.com/githubnext/localjev), ≠ kunchenguid/local-jev). `notes.md` §75 |
| "localjev" without the owner | Namesake collision | Always **githubnext/localjev** (Bun Chat Completions) vs **kunchenguid/local-jev** (ONNX ModernBERT). `notes.md` §75 |
| 77-option Choice at default Laya head budget | ~3–4 tokens/label; labels collide | Hierarchical Choice, or a head that owns 255 options (Jev). Quote the token-budget fact; do not copy `head_max_len` ([NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)). `notes.md` §76 |
| Auto-act because Laya conf ≥ 0.85 | Recipe ≠ Harbor cal; gating misses script OOD | Route by script first; fit T; pick τ on *your* labels. 0.85 is *theirs*. `notes.md` §76 |
| Treat 0.766 / 0.081 as zero-shot / raw ECE | Fine-tune on that split; post-T | Base ckpts below majority. Name the temperature. Jev rows unpublished-here. `notes.md` §76 |
| Rank openjevs from the census tweet | A list is not a bake-off | Use the scored sibling §78; still ≠ v1.1. Watch [jev-models](https://benchmarkheaven.com/jev-models). `notes.md` §77, §78 |
| Collapse GLiNER2 / routers into NAR clones because they are on the list | Class-boundary | Locate/categorize and route are placements, not replicas. Needle 3 already not Jev-class. `notes.md` §77 |
| Treat missing Laya/localjev/kev as out of class | Census lag | Incomplete ≠ our watch wrong. Completeness is a board watch item. `notes.md` §77 |
| Quote 15 likes as quality | Engagement is ephemeral | SIGNAL ~417/9; this pass 564/15. Do not copy Stripe. `notes.md` §77 |
| Mix v1.1 87.6 with v1.2 75.3 | Different tiers and scoring | Cal now ON the composite. Hard 220 new. `notes.md` §67, §78 |
| Treat Luna I=97 as rank #1 | Weak Cost axis (28.2) | Geo-mean product; rank #7 *theirs*. `notes.md` §78 |
| Ignore ×2 latency / est. costs | Assumption, not measurement | Harbor honesty; ranks are configuration-specific. `notes.md` §78 |
| Treat Qwen3.8 27B as Archer | Official Qwen / Chutes TEE | Partial; Cost 0 from price. Archer still Watch. `notes.md` §78 |
| Read Laya absence as quality | Gap, not a named exclusion | Absent from table **and** exclusion list. `notes.md` §78 |
| Reverse A/B on a small yes/no rebuild and quote one number | Option-order 72%→21% | Rank with author's order; keep both runs. Cousin of paraphrase brittleness. `notes.md` §78 |
| Re-card localjev / classifier.dev / Laya / choxos / census because they reappear on the hourly | Already folded | Apply the five as a recipe; skip thin noise. `notes.md` §79 |
| Fail CI / stamp quality from a Noul | Soft sensor as a hard seal | Attend or escalate; exact envelope proves the irreversible act. Qualify [totally-tim/jev-gate](https://github.com/totally-tim/jev-gate) ≠ jev-gateway / MongLong0214/jev-gate. `notes.md` §79 |
| Stall the reflex waiting for S2 / let S2 fly | Planner as executor | S1 keeps the stick; S2 is one-use advice. [khordoo/jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab). `notes.md` §80 |
| Treat S2 arrival as consumed guidance | Telemetry conflates bar with decision | Purple confidence = used; purple S2 bar = arrived; red = fail. `notes.md` §80 |
| Call the lab's Local controller "localjev" | Namesake collision | Rule-based built-in **≠** githubnext/localjev **≠** kunchenguid/local-jev. `notes.md` §80 |
| Hard-act at the 20% starting gate / treat seed as replay | Soft slider as interlock; geometry as DST | 20% *theirs* still soft; schema-safe ≠ correct. Seed repeats layout, not timing. `notes.md` §80 |
| Send pixels or planner prose into the reflex | Omni / stale bearings | No graphical input; code never labels safest; physics owns collisions. Skip Archer. `notes.md` §80 |
| Assume confidence = selected probability | SDK field smuggled as the app contract | Application contracts ≠ TypeSafe methods. `notes.md` §80 |
| Overlapping CU actions / one 255-way soup | Confidence collapse; noise in the kind | Exclusive set; split kind/item/site ([typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)). `notes.md` §81 |
| Ship pixels to Jev for the click | Omni CU | OCR+AX text-state; answer-reader capture ≠ the Choice. Skip Archer. `notes.md` §81 |
| Quote 155× as a Harbor score / 0.4 as τ | One screenshot; product copy | Re-measure. schema-safe ≠ correct. `notes.md` §81 |
| Ship audio to Jev / treat 27/27 as Harbor | Omni voice; fixtures as a board | Transcript text-state; integration on captured pages *theirs*. [jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser). `notes.md` §82 |
| Truncate free-text on a partial / spoken confirm as auth | Wait-policy collapse; soft Noul as interlock | Closed-set may fire; search/type wait. Confirm is convenience. `notes.md` §82 |
| Call a second model for "two" / collapse into jev-voice-control | Extra generation; namesake | Numbered overlay is exact. **≠** chris-wozniczek **≠** nikolas-j **≠** OCR §81. `notes.md` §82 |
| Let the model skip the wrap / silent ASK | Advisory sidecar; HITL skipped | Wrap *is* execution; ASK throws. [AgentGhost](https://github.com/reddpy/AgentGhost). `notes.md` §83 |
| Treat AUTO_APPROVE as auth / wrap hosted tools | Demo hatch; out-of-reach actuators | Provider tools stay unwrapped. rh-guard owns the gate. `notes.md` §83 |
| Collapse AgentGhost into actiongate / toolgate / jev-use / namesakes | Slogan mix; fail polarity | Wrap ≠ evidence-only; fail-closed ≠ jev-use fail-open. **≠** jwen5419807 **≠** vventirozos. `notes.md` §83 |
| Paste JP atlas ★ as a bake-off | Research-time stars as scores | Genre list, not verified evals. [@studio_yebisu](https://x.com/studio_yebisu/status/2101065176069886152). **≠** §77 **≠** §78. `notes.md` §84 |
| Quote 200× / 400× as Harbor / “cannot hallucinate” | Marketing multiples; schema as correctness | TypeSafe ceiling *theirs*. schema-safe ≠ correct. [@akshay_pachaar](https://x.com/akshay_pachaar/status/2101037514945597645). `notes.md` §85 |
| Compare Jev against GPT-5.6 as same-class | Category error; decoder-only vs encoder ZS | people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows. encoder / ZS classifiers. `notes.md` §112 |
| Treat Hub ZS softmax 0.504 as a Noul / copy `pipeline()` | Uncalibrated entailment; recipe dump | softmax/ZS scores still ≠ calibrated Noul. opt for DeBERTa and ModernBERT ones. do not invent accuracy numbers. `notes.md` §112 |
| Copy the explainer’s Python / collapse into a wrap how-to | Recipe dump; product mix | Independent pedagogy. **≠** official docs **≠** Flavio **≠** AgentGhost §83. `notes.md` §85 |
| Treat topical cosine as “customer is asking” | Embedding as proposition | Contrast-set: all six about refund; only asking pass. [jev-semgrep](https://github.com/uehaj/jev-semgrep). `notes.md` §86 |
| Multiply parallel meaning Nouls / negative-query tricks | Independence; set-diff theater | Threshold each Noul, boolean-compose bits in code. ≠ jev-combinators metaphor. `notes.md` §86 |
| Call jev-semgrep Semgrep.dev / a merge gate | Namesake; soundness theater | **≠** [semgrep.dev](https://semgrep.dev). Ranking fail-open; not a gate. `notes.md` §86 |
| Paste 0.94/0.98 or ★42/51 as Harbor | LLM-as-judge / ephemeral stars | 10 cases × 51-line corpus *theirs*. Stars research-time. `notes.md` §86 |
| Let Jev invent UI prose / treat valid A2UI as quality | Pointer UI; schema-safe ≠ correct | Derive → select → compile. [gram-render](https://github.com/wei-b0/gram-render) / [jev2ui](https://github.com/dglazkov/jev2ui). `notes.md` §87 |
| Round 0.67 into a test pass / 0.85 as a product proof | Ambiguous band; still-soft τ | Fails both polarities. Exact stays in `toContain`. [jevtest](https://github.com/realZachi/jevtest). `notes.md` §87 |
| Default jeff for numeric state / invent Laya in anima3 | Family mismatch; user-brief ≠ README | Qwen logprob default; a11y tree. Skip Archer. `notes.md` §87 |
| Treat JevFind windows as functions / 0.25 as Harbor τ | Overlapping windows; still soft | Pointer search. Keyword still wins exact strings. `notes.md` §87 |
| Paste 72.5% as a class ceiling / use Jev `confidence` | One run; field mix | Top of `probabilities`. ChaosNLI JS worse than uniform. **≠** frontier-100. `notes.md` §87 |
| GLiClass vs Jev as architecture duel / skip majority | Product bakeoff; floor 49% | Flattened encoder. 40% < 49% is the finding. `notes.md` §87 |
| Skip the 0.947 floor / treat ECE as ranking | Rare positives; calibration ≠ discrimination | Fitted tfidf wins. llm_local ECE 0.947. `notes.md` §87 |
| Authorship Choice as evidence / binary “is this AI?” | Named escape; soundness theater | `uncertain` exists. Not a seal. `notes.md` §87 |
| HA writes without envelope / collapse into HA-Jev | Leveson; namesake | HA remains execution. [ha-switchboard](https://github.com/grayslawson/ha-switchboard). `notes.md` §87 |
| Silent-best-route n8n at 0.5 / treat as official | Abstention; unofficial | Low Confidence output. Arithmetic in Code/IF. `notes.md` §87 |
| Mix fast-jev-compaction-pi / compact / compaction | Three namesakes | Always write **zaycruz/fast-jev-compaction-pi**. `notes.md` §87 |
| Quote jevloop mock quality / treat p as unused | Control-loop demo; value function | No LLM in the loop. Full distributions. `notes.md` §87 |
| Quote laya-vision `score` / call it Archer | Untrained axis; family lock | SmolVLM. CC-BY-NC-SA. **≠** blackwood. `notes.md` §87 |
| Cerebellum `base_url` drop-in / endorse 94.92% | Wire ≠ TypeSafe; competing NAR | `/v1/decide`. Separate Harbor axes. `notes.md` §87 |
| Swap laya-grounded into phishing / temperature-scale | Not a drop-in; no bias term | Platt. Entropy-confidence ≠ max_prob. `notes.md` §87 |
| Collapse Jeff-1 into logan-markewich/jeff / “better ECE” | Namesake; acc≠cal | LoRA Qwen3-4B. 0.8183/0.0807 vs 0.8283/0.0932 *theirs*; set reused. `notes.md` §88 |
| Empty stanley findings as approval / auto-promote | Coverage ledger; human actuator | `notChecked`. 0.6/0.55/0.15 still soft. `notes.md` §88 |
| findme beam as identity / collapse into JevFind | Ranking ≠ proof; species | NL memory → listed names. **≠** path-then-window. `notes.md` §88 |
| Swap conversation model / quote jevsubrouter $ | Cache envelope; unmeasured | Price workers. Fail-open. Counts ≠ dollars. `notes.md` §88 |
| Treat `.feels()` 0.5 as a bool if / new language | Noul-0.5-never-rounded; namesake | Keep p with `.how()`. **≠** hunch **≠** Probably. `notes.md` §89 |
| Collapse apa-harness into jev-harness / copy `@aipersona` | Namesake; unpublished npm | “Mathematically fulfilled” overclaim. 0.85 still soft. `notes.md` §89 |
| Quote grok-bot-jev 13.0× as tokens / skill forces the bot | Proxies; honor | Not a token-savings claim. Top-five cap. `notes.md` §89 |
| Let Essentiel Jev send / skip human | Never authority | 0.75 provisional. **≠** jevmail **≠** mailjay. `notes.md` §89 |
| Collapse enzo-mcp into jev-sift / skip UNKNOWN | Atomize ≠ filter | Deterministic evidence first. Prior sensor never fed back. `notes.md` §89 |
| Treat pigeonhole OTHER as a move / 0.6 as Harbor τ | Named escape; still soft | Skip. autoOnSave off. **≠** jev-semgrep. `notes.md` §89 |
| Treat HF playground as live Jev / classifier.dev | Static sandbox | No network. Sibling jev-decisions pointer only. `notes.md` §89 |
| Quote jev-reliability as accuracy | Consistency ≠ correctness | Nothing about accuracy. noul-gate 0.0%/12.5%/3.6% *theirs*. **≠** dinostomp. `notes.md` §89 |
| Collapse clduab11/jev-test into jevtest / paste bars | Namesake; bars ≠ scores | “Nothing runs yet.” **≠** realZachi/jevtest. `notes.md` §89 |
| Paste “Jev wins” from jev-rag-benchmark | Assumption forbidden | Plumbing. `max_budget_usd` 0. **≠** Jev-RAG. `notes.md` §89 |
| Collapse dairui1/jev-lab into BrendanH18 / re-card jev-desktop | Namesake; already MED | 91% vs 79% *theirs* synthetic. Fan-out vs `CLICK:3`. `notes.md` §89 |
| Treat jevmail as mailordinal / mailjay as read-only | Inbox species | `gmail.readonly` vs archive/trash after review. `notes.md` §89 |
| Collapse ZHUBoer/ego-jev into jiangkoumo / treat `completed` as success | Namesake; verifier | ZHUBoer/ego-jev reserved `__none__`. runWorkflow completed ≠ success. `notes.md` §90 |
| Treat jsort logits as frequencies / Choice as the scale | Ranking ≠ calibration | jsort scores are relative. Noul not Choice for scale. `notes.md` §90 |
| Paste groundedness Macro-F1 as “Jev wins quality” | Axis; namesake | groundedness-judge-bench native vs schema-guided. implicit_true included in yes. `notes.md` §90 |
| Quote jev_playground 83% / promote from authored bars | Plumbing; 0 promotions | jev_playground 0 promotions. routing-backtest 0.0447%. `notes.md` §90 |
| Copy `jev-latest` on Zen / collapse into GodsBoy | Model pin; namesake | yuyang2230/jev-agent-skill jev-1.13-free. `notes.md` §90 |
| Treat techstack ranks as a generated stack | Classifier not generator | jev-techstack-classifier stack_config.json only. `notes.md` §90 |
| Collapse s1_ruby into hunch/feelings / `is?` as a proof | Collapse late | s1_ruby collapse late. `undecided?` abstain. `notes.md` §90 |
| Treat judgement as jevql / confidence as winner p | Unofficial CLI | 2389-research/judgement license null. confidence ≠ winner p. `notes.md` §90 |
| Treat the Rust community SDK as official / a new species | Unofficial; packaging | typesafeai-sdk-community not a new species. `notes.md` §90 |
| Collapse tpellet/hunch into carldaws/hunch / skip exit 3 | Namesake; abstain | tpellet/hunch exit 3. never-execute list. `notes.md` §90 |
| Quote file-search 15 matches as recall / collapse into JevFind | Uncalibrated; species | jev-file-search scores not calibrated accuracy. `notes.md` §90 |
| Treat linkmap referee as gold / let Jev see S2 prose | Rubric rewrite | jev-linkmap Jev never sees S2 prose. `notes.md` §90 |
| Treat jev-mail as jevmail / tidy OTHER as a move | Inbox/file species | muhammedilyasy/jev-mail metadata only. tidy none-of-folders stay. `notes.md` §90 |
| Close pinned/audio/current tabs / skip Show | Life fail-open | tab-bouncer pinned/audio/current never closed. lkclean Show fail-open. jev-yt-time-saver Show anyway. `notes.md` §90 |
| Let ORIGIN LLM decide / continue without Jev | Pause-if-no-Jev | ORIGIN pause-if-no-Jev. validResponse sums-to-1. `notes.md` §90 |
| Gate crawlers on raw `bug_likely` / skip verify | Ranking ≠ bug p | jev-crawlers risk bands never raw boolean. `notes.md` §90 |
| Sell jevbrain AUTO_ACT as a Noul / paste 95.2% | Local overlap ≠ Jev | jevbrain AUTO_ACT is not a Noul. `notes.md` §90 |
| Treat judgekit 97.7% n=130 as a class ceiling | Mini-set; harness ≠ bench | judgekit YAML classify/score/route/verify. `notes.md` §91 |
| Treat openrouter-jev-mcp as TypeSafe first-party | Independent Decision-as-Plugin | ctmx/openrouter-jev-mcp Decision-as-Plugin. Native keys not supported. `notes.md` §91 |
| Threshold on self-confidence / skip `combine()` | Verdict-in-code | typed-judge-kit verdict-in-code. `notes.md` §91 |
| Quote decide 0.8 as 80% accuracy | Packing VOI; still soft | alsoleg89/decide packing VOI. 0.8 ≠ 80% accuracy. `notes.md` §91 |
| Act on arena Brier / collapse into jev-arena | Never acts; namesake | jev-calibration-arena never acts. `notes.md` §91 |
| Skip Platt / treat Choice 50–95% as accuracy | Calibration as product | Jev-Calibration Platt ECE 0.117→0.052. `notes.md` §91 |
| Collapse FrancoisChastel/jev-code into stanley npm | Namesake; placeholder | FrancoisChastel/jev-code ≠ npm jev-code. `notes.md` §91 |
| Marketplace Jev on the hot path / fail-closed missing key | Event-boundary; polarity | claudecode-jev-marketplace fail-open not hot path. `notes.md` §91 |
| Invent `ask_jev` | Closed catalog | pedroknigge/mcp_jev packs not ask_jev. `notes.md` §91 |
| Treat jevtypesafeai.com as TypeSafe | Independent host | codaaiteam/jev-skill jevtypesafeai.com ≠ TypeSafe. `notes.md` §91 |
| Treat `ts_safety` as a Noul / skip deadband | Deterministic safety | cyrusasco/typesafe-mcp noul deadband 0.35–0.65. `notes.md` §91 |
| Collapse hermes-switchyard into Agnes / auto-load skills | Advisory; namesake | hermes-switchyard ≠ hermes-jev-router ≠ hermes-plugin-jev. `notes.md` §91 |
| Paste nanoprune 0 hallucination / treat as hosted Jev | Theater; distill ≠ Noul | nanoprune 2.8MB ECE 2.58%. `notes.md` §91 |
| Collapse jev-browser-agent into ZHUBoer / DONE as proof | Namesake; verifier | smartdio/jev-browser-agent ≠ ZHUBoer/ego-jev. Dakai/omp-jev-web DONE ≠ proof. `notes.md` §91 |
| Collapse hari007sh/jev into dannote/jev | Namesake | hari007sh/jev ≠ dannote/jev. `notes.md` §91 |
| Treat system-one-skills as a judge | Name ≠ species | 0thernet/system-one-skills deterministic verify. `notes.md` §91 |
| Hard-argmax typed-gate / 0.51 as a yes | Band is refusal | typed-gate band [0.40,0.60] is refusal. `notes.md` §91 |
| Treat pi-jev-gate as fail-open / restore ask | Polarity; binary | pi-jev-gate fail-closed; choice is the verdict. `notes.md` §91 |
| Paste Foq 100%/ECE 0.2% as a class ceiling | Local exam; still *theirs* | Foq ~25ms/2.2GB local. `notes.md` §92 |
| Quote rev `latency_ms` 32.4 as a bench | Sample JSON | rev prefill-only + HF jev-0.5b. `notes.md` §92 |
| Treat robfrase/jev as running code / collapse into dannote | Planning memo | robfrase/jev planning memo. `notes.md` §92 |
| Treat 27/27 as Harbor / skip Confirm | Probe; Confirm is the gate | typesafe_agent_gates 27/27 / 31/31. pastepilot Confirm before act. `notes.md` §92 |
| Treat safe-sh as pre-exec allow | Static remainder | EpicEric/safe-sh static remainder. `notes.md` §92 |
| Quote Reranker 0.1667 as live Jev | Offline lexical | Jev-Reranker live Jev not yet measured. `notes.md` §92 |
| Fail-closed sessionwise if Jev is down | Opt-in; fail-open | sessionwise opt-in relevance. `notes.md` §92 |
| Treat jev-search scores as truth / collapse into kazuhideoki | Pointer sieve; namesake | jev-search pointer sieve. **savka777/jev-search ≠ kazuhideoki/jev-search ≠ superagents-lab/jev-search**. `notes.md` §92 |
| Paste 400 ms as an SLA | Demo timestamps | 400ms Salesforce WebMCP. `notes.md` §92 |
| Let scheduler plugin place Pods | Advisory | typesafe-scheduler-diagnostics advisory. `notes.md` §92 |
| Send Android screenshots for the decision | AX observe | droidjev screenshot-free. `notes.md` §92 |
| Treat jevcu as closed-vote | Planner still writes | Tewoto1 jevcu planner still writes. `notes.md` §92 |
| Collapse ha-conversation-jev into HA-Jev / copy OAuth client_id | Hybrid leftover | ha-conversation-jev Jev→Grok. `notes.md` §92 |
| Let dsh-jev widen tools | Can only gate | dsh-jev can only gate. `notes.md` §92 |
| Paste $0.46 as a measured classification run | Specified not run | jev-classification-benchmark specified not run. `notes.md` §92 |
| Auto-page from luna-pagerduty 1.000 | Synthetic; rh-guard | jev-luna-pagerduty p≥0.50. `notes.md` §92 |
| Quote akpsahan vs-Jev as a new measure / treat as Archer | Hub copy | akpsahan/laya ≠ Archer. meldltd/meldecision laya-go ONNX. laya-doom never pixels. logixism/laya-api empty README. `notes.md` §92 |
| Let Jev own chess / AV / customs Post / API Victory | Engine / sim / taxonomy | choxos/jevchess engine owns truth. jev-drive sim not AV. story-arc Jev never authors. jev-hs-assistant HS6. golergka/jev-plays-starcraft-2 UI-verified ≠ API Victory. `notes.md` §92 |
| Treat typesafe-go as official / likes as eval | Unofficial; catalog | Nibir1/typesafe-go ≠ official. awesome-jev-use-cases catalog. `notes.md` §92 |
| Treat a ledger HIT as correctness / collapse into kushals256 | HIT ≠ truth; namesake | fingerprint after redact; recall vs decide. Cache hit ≠ correctness. hyperspaceai/jevcache ≠ kushals256/jevcache. `notes.md` §93 |
| Auto-accept GEPA on a rising training score / collapse into caiovicentino | Human taste gate; namesake | human labels only; score never auto-accepts; production capture flywheel. sutro-sh/jev-align ≠ caiovicentino/jev-align. `notes.md` §93 |
| Hard-gate enzyme `when asked` / treat catalysts as summaries | Guidance ≠ hook; index ≠ summary | guidance ≠ hook; catalysts ≠ summaries; compile-time System One. hosted bootstrap ≠ silent TypeSafe. `notes.md` §94 |
| Treat unofficial JA ModernBERT as TypeSafe / skip format_version | Unofficial; lock | unofficial ≠ TypeSafe; format_version modernbert-jev/1. Argos1111/jev_local ≠ us/jev-local ≠ kunchenguid/local-jev. LFM default ≠ ModernBERT backend. `notes.md` §94 |
| Treat enzyme hosted bootstrap / anonymous broker as TypeSafe Jev | Silent FALLBACK | hosted bootstrap ≠ silent TypeSafe. Name which backend answered. `notes.md` §94 |
| Collapse Argos1111/jev_local into the JA Hub card / treat LFM vision as unofficial JA softmax | Dual-backend | LFM default ≠ ModernBERT backend. Default is LFM text/vision logprob; JA ModernBERT is optional text-only. `notes.md` §94 |
| Treat Nemotron_Jev as calibrated Jev / collapse djev-dev into djev-spark | Interface ≠ identity | Nemotron ≠ TypeSafe Jev; not a calibrated replacement; djev-dev complements djev-spark; images as Choice options. `notes.md` §94 |
| Paste Laya essay vs-Jev as a new bake-off / treat Khmer 0.952 as competence | Already §76; OOD | Laya essay numbers *theirs*; Router/OOD confidence. `notes.md` §94 |
| Treat orchestrator “difficulty” as a live Score | Description ≠ code | difficulty + policy thresholds + JSONL trace. `notes.md` §95 |
| Treat jev-codex-pilot as a bake-off | Thin overlay | jev-codex-pilot model + reasoning depth. `notes.md` §95 |
| Treat keep as failure / force BERT onto Jev | Cost gate; keep is a win | keep/shadow/hybrid/reject. `notes.md` §95 |
| Summarize quarry pages / fail-closed if Jev is down | Pointer; fail-open | quarry evidence projection. `notes.md` §95 |
| Collapse Frank-ZY-Dou into walidboulanouar / paste $ as a rate | Atlas; seed-0 | Frank-ZY-Dou/awesome-jev robotics/3D/control. `notes.md` §95 |
| Invent one-dollar-tahoe ASR/FPR / copy attacks | No numbers; demo | one-dollar-tahoe TypeSafe Jev defense eval. `notes.md` §95 |
| Collapse jevguard into jevcache / skip the escape | Namesake; calibrator | jevguard calibrator/cache/escape. `notes.md` §95 |
| Skip CI from skip_below 0.05 | Shadow default | jev-ci-selector CI shadow mode. `notes.md` §95 |
| Treat llama-jev softmax as a Noul | Format ≠ proper scoring | llama-jev llama.cpp replica. `notes.md` §95 |
| Collapse OpenCode jev-pruner into tamaratran / fast-jev-opencode | Host port; different job | OpenCode jev-pruner context sieve. host port of tamaratran/jev-pruner. **≠** nrdz-labs/fast-jev-opencode. `notes.md` §96 |
| Treat zen-chat as a Noul / paste 24/24 onto OpenCode | Approximation; not this bench | zen-chat ≠ Noul. jev-zen / jev-1.13-free. `notes.md` §96 |
| Hard-gate keepThreshold 0.5 / fail-closed the turn | Sensor; hook fail-open | fail-open original. keepScore >0.1 floor. `notes.md` §96 |
| Invent jev-webagent-bench scores / boolean @ 0.5 as a proof | Empty stub; decoder | jev-webagent-bench empty stub. Kiln-AI/jev_jsonschema noul_threshold 0.5. NSStudent/JevSwiftSDK unofficial. `notes.md` §96 |
| Treat gliner-native-runtime as TypeSafe / Fastino / a Noul | Locate; unofficial | GLiNER2 native Apple path. not Choice/Score/Noul. not TypeSafe. shershah1024/gliner-native-runtime ≠ Fastino. `notes.md` §97 |
| Collapse it into compaction / ultrafast / Eran-BA / JevSwiftSDK / jevmlx | Namesake lock | ≠ gliner25-compaction ≠ gliner2-ultrafast ≠ Eran-BA/Jev_from_GLiNER2 ≠ NSStudent/JevSwiftSDK ≠ jevmlx. honesty locks. `notes.md` §97 |
| Paste README 0.99 as Harbor / hard-gate 0.1 | Fixture; sensor | default threshold 0.1 still soft. `notes.md` §97 |
| File it as keep/drop / position 4 Selector | Locate; position 10 | schema→spans. Not keep/drop of held candidates. Not Selector of F. `notes.md` §97 |
| Treat DGP as official TypeSafe / assessment p as a grant / receipt as proof | Protocol envelope; sensor ≠ constraint | Decision Graph Protocol frame→assess→commit. app retains permissions/effects. Jev-first assessor-neutral. guarded commit / receipt/next frame. numerous-com/dgp ≠ TypeSafe official. `notes.md` §98 |
| Hard-gate DGP as a safety proof / collapse ThreadDesk mocks into live Jev | Safety theater | hard-gating DGP as safety theater. assessment batching. Mock resolver ≠ Jev. `notes.md` §98 |
| Collapse can1357/jegrep into jevgrep or jev-semgrep / paste 79% | Namesake lock | can1357/jegrep ≠ Bentlybro/jevgrep ≠ uehaj/jev-semgrep. jegrep calibrated path+range Nouls. no embeddings/index/daemon. `notes.md` §98 |
| Hard-gate 0.4/0.2 as “concept absent” / paste $0.01–0.03 as a ceiling | Ranking fail-open; sensor | ~$0.01–0.03 typical. agent --json. Soft Noul ≠ hard safety. `notes.md` §98 |
| Treat OpenRouter/TypeSafe auto-failover as one Noul / later-round auto-τ as a 0.4 proof | Silent FALLBACK; sensor | Pin `--endpoint`. Auto-τ-lowering is ranking fail-open. rh-guard owns the cousin. `notes.md` §98 |
| Treat kev OOD 0.76 as Jev / isolation as identity / wire as a Noul | Replica honesty | Archer-arch fidelity. kev family OOD 0.76–0.77 vs Jev 0.86. block-causal isolation. pointer/readout CE-trained. /v1/systemone drop-in. replica honesty. Score confidence is a stand-in (*theirs*). Do not rewrite §45. `notes.md` §98 |
| Treat Archer as landed / kev-8b as the 27B drop | Watch | Tracker likes 51; lastModified UNCHANGED. Hub 401. `notes.md` §98 |
| Treat gut/judge as new class-table species / hard-gate 0.038 as a proof / treat `on_unsure="raise"` as a System One hard gate / let UNSURE become False | Overlay; sensor; app policy | cost-sensitive decision theory × System One probabilities → control flow. thresholds derived from costs not hard-coded. YES / NO / UNSURE from cost_false_yes / cost_false_no / cost_human. auto-batching same-object questions. Default `on_unsure="raise"` is app policy, not a System One hard gate. Kungie/gut ≠ tpellet/hunch ≠ carldaws/hunch. `notes.md` §99 |
| Collapse Illusion47586/judge into judgekit / dump the SDK / run multiple callbacks speculatively | Namesake; judgment vs generation | judgment vs generation. deterministic execution after probabilistic judgment. exactly one app-owned callback. explicit uncertain branch. Illusion47586/judge ≠ lexingtonhibiki/judgekit ≠ Ascurse/typed-judge-kit. `notes.md` §99 |
| Treat jev-forge as a sixth species / clone Hub weights / paste 0.579 as Harbor | Class-architecture; sensor | variable-N option scoring as the trainable object. dynamic candidate bags not fixed label sets. zwliJay/jev-forge ≠ NanoJev. `notes.md` §99 |
| Merge von Needle 52.6% with n=78 93% / treat sub-15ms as the 62 ms table / dump von-1.0 weights | Replica honesty | NAR local drop-in. open replica economics / latency vs closed Jev. wfzyx/von late-catch HIGH. competing NAR claims / replica honesty. `notes.md` §99 |
| Paste “Jev wins guardrailing” / treat llm-vs-jev as Harbor / fold steer suffixes here | Pareto; rh-guard | typed judgments vs chat judges on guardrailing. nothing wins outright. can be argued out of guarding. ishaannk/llm-vs-jev cross-note only. deeper integrity fold is rh-guard. `notes.md` §99 |
| Treat Probably as hunch / feelings / gut / Judge / tidymodels/probably / hard-gate `feels` 80% / treat playground recordings as live inference | Language primitive; sensor | Jev IS the if-statement. judgments/probabilities drive branches. text model only writes prose. interpreter owns variables/loops/budgets/replay. otherwise maybe / confidence gate. chaos samples after the gate. southpolesteve/probably ≠ carldaws/hunch ≠ feelings ≠ Kungie/gut ≠ Illusion47586/judge ≠ tidymodels/probably. `notes.md` §100 |
| Auto-accept GEPA because the score rose / re-dump §93 / collapse into caiovicentino | HITL; live-star delta | 133★ / forks 10 live. build calibrated classifiers from human feedback. `notes.md` §100 |
| Retrieve by resemblance / paste 17/18 as Harbor / treat a miss as absence | SDT; extractable-from-state | retrieve by relevance not resemblance. one calibrated yes/no per memory in one request. pointer mode 17/18 19/20 *theirs*. embedding resemblance misses the allergy. samdotmak/jev-recall ≠ jev-search ≠ jev-sift ≠ carryforward ≠ chopratejas/invalidate. `notes.md` §100 |
| Hard-gate 0 of 157 / treat questions as evidence / adapter owns the store | Leveson; sensor | memory leases ended by new evidence. six Nouls then fixed rules in code. 0 of 157 false invalidations. questions/plans/directives are not evidence. unsure → review queue. host keeps the store. `notes.md` §100 |
| Treat jev-lint rename as a second product / fail CI on a shipped warning / collapse into JevLint | Rename; fail-open | name↔body / comment truth / test-claims. mizchi/jev-lint is mizchi/jevlint rename. no shipped rule has severity error. ~1 in 5 findings wrong *theirs*. mizchi/jev-lint ≠ huntedman/JevLint ≠ MichitoSugawara/jev-lint. `notes.md` §100 |
| Treat boolean @ 0.5 as a proof / hide remaining bad properties | Decoder not a gate | JSON Schema → typed JSON via Jev. noul_threshold 0.5 decoder not a proof. IncompatibleSchemaError lists every bad property. `notes.md` §100 |
| Paste ANE 4.98 ms as “beats Jev” / claim 10× / `cpu_ne` as the experiment | Replica honesty | on-device Laya CoreML ANE. ~5 ms P50 short decisions. 189/189 FP16 checkpoint parity. 10× not achieved. mizorewww/laya-coreml ≠ gliner-native-runtime ≠ jevmlx ≠ NandhaKishorM/laya. `notes.md` §100 |
| Treat softmax as a Noul / paste 87.7 vs 81.2 as identity / collapse into localjev | Replica honesty | softmax over allowed tokens ≠ Noul. question-first cache. Micha0827/snapjudge ≠ githubnext/localjev ≠ jevmlx ≠ cendress/SnapJudge. `notes.md` §100 |
| Treat 62 tests as quality / collapse into jevpilot / invent CandidateSource | Wiring ≠ quality | Jev-first Pi agent loop. slow-LLM fallback. explicit action menu / CandidateSource unimplemented. 62 tests wiring not quality. direwolfiy/JevPi ≠ standardagents/jevpilot ≠ pi-jev-control. `notes.md` §100 |
| Treat a zero binary name gap as a fairness certificate / collapse into BBQ | SDT; audit | resume-screening bias audit methodology. name×resume factorial independent Nouls. callback determined by resume quality. mean-probability name gaps operationally negligible. natemoo-re/bias-bench ≠ BBQ. `notes.md` §101 |
| Let Jev emit pass\|review\|block / pack seats into one goodness Noul | MCDA; code-owned | Plan/PRD panel → code-owned pass|review|block. cheerleading out of scope. austindixson/planalyzer ≠ single-goodness Noul. `notes.md` §101 |
| Ask Jev to generate the next model / prestige-route | EU; decide vs do | cost-aware multi-model routing/escalation. decide vs do. successful-task cost. cannacre8ive/switchboard-ai ≠ ha-switchboard ≠ hermes-switchyard. `notes.md` §101 |
| Unfreeze PROTOCOL after seeing test numbers / skip contamination | Frozen protocol | frozen-protocol zero-shot bench. TypeSafe Jev vs PrismNLI vs Laya. contamination caveat. elcronos/jev-vs-open-decision-models ≠ JevBench ≠ DMB. `notes.md` §101 |
| One fail polarity for every jevusher lens / treat J7 pass as obey | VOI; per-lens | context-window admission control. VOI gate which tokens are worth the expensive model. fail polarity per lens. on small inputs lenses lose money. cvsgireesh/jevusher ≠ jev-sift ≠ winnow. `notes.md` §101 |
| Treat a receipt as a grant / pack identity into the question | Leveson | typed decision control plane. receipt ≠ authorization. historical-v0 zero retained cases. MokiMeow/jev-fabric ≠ jev-forge ≠ dgp. `notes.md` §101 |
| Fifteen chat completions per pause / hide Cost vs desc price | Scoring economics | live 15-dim typed rubric re-score per pause. scoring economics exemplar. OpenJev/Codiv ≠ TypeSafe hosted. jose-troche/live-rubric ~$0.000004 desc / ~$0.000006 README. `notes.md` §101 |
| Choose predictions after seeing data / gate on confidence ≥0.95 | Pre-registration | adversarial pre-registered Jev eval. 28 predictions before data. 123,805 requests. confidence does not track ignorance. polite injection 65% / crude 0%. willkelly/jev-evaluation ≠ jevals ≠ jev-baselines-eval. `notes.md` §101 |
| Treat system_one_sdk as a new species / as TypeSafe official | Class infrastructure | provider-neutral Elixir/BEAM Noul/Choice/Score SDK. class infrastructure. nshkrdotcom/system_one_sdk ≠ typesafe_sdk ≠ dannote/jev. `notes.md` §101 |
| Treat a clean jevq run as measured separation / fail CI on a warn / collapse into tenbin | Question lint | question-linting of Jev questions themselves. nine jaggedness rules, no API key, no labelled data. static lint ≠ measured separation. yodablocks/jevq ≠ tenbin ≠ JevLint ≠ commitjev. `notes.md` §102 |
| Treat laya_ex as TypeSafe official / copy mix backends | Class binding | open-weights Laya as class exemplar (binding). Nx/Bumblebee runtime. host chooses backend. ChristianAlexander/laya_ex ≠ system_one_sdk ≠ dannote/jev ≠ NandhaKishorM/laya. `notes.md` §102 |
| Let a Score grant Tx / treat 62 tests as Laya parity | Leveson; on-chain | on-chain/edge Laya deploy. parity_verified stays false. model output never grants Tx. humandebri/IC-Laya ≠ laya_ex. `notes.md` §102 |
| Paste AUROC as a phishing win / treat unpaired 0.577 as identity | Replica honesty | auditable weekend replica. Jev outputs never used for training. unpaired 0.577 vs 0.727. agilabs-ai/jev48 ≠ JevBench ≠ Mapika/decider. `notes.md` §102 |
| Ask absolute “should red plant” / inject class priors as help | Framing | adversarial dual-judge / framing attack surface. comparative framing is the usable judgment. prior injection crowds out evidence. copyleftdev/ember ≠ ember.js. `notes.md` §102 |
| Paste sequence counts as trained quality / “never hallucinates” | Pipeline | Laya specialist fine-tune pipeline. training still GPU-pending. PIXELZX0/XERON ≠ convaiinnovations/laya. `notes.md` §102 |
| Re-paste copied vs-Jev as a 2145 bake-off | Packaging | Hub Laya replica drop. daliborsb/laya ≠ convaiinnovations/laya ≠ NandhaKishorM/laya. `notes.md` §102 |
| Distill Jev as teacher of record / treat missing student as shipped | Distill economics | System One student distillation corpus. gold is programmatic. teacher is closed-API clone. MagaBitmex/jev-4b-distill-data ≠ missing student checkpoint. `notes.md` §102 |
| Paste maze 1.00 as a general System One / collapse into douglance/jevon | Non-LLM | non-LLM VIN System One. planning depth not chat. lewislululu/jevon ≠ douglance/jevon. `notes.md` §102 |
| Treat exit 0 as claim truth / matching quote as a proof / collapse into jonathanavis96 Airlock | Evidence ≠ authority | source-bound evidence checks. local quote mismatch needs no API. exit 0 ≠ claim truth. WaynezProg/jev-kit ≠ jonathanavis96/jev-kit (Airlock) ≠ jev-use ≠ jev-mcp. `notes.md` §102 |
| Promote a catalog `reported` row to `reproduced` / collapse nineteen records into one leaderboard | Evidence catalog | independent System One evidence catalog. 19 reviewed records. scores not one leaderboard. no external record currently reproduced. TokenTrim no-Jev matched hybrid 62.4%. reachjalil/system-one-bench ≠ mallahyari/system-one-benchmark. `notes.md` §103 |
| Treat constructed GitHub scenes as production logs / collapse SivletLabs into willkelly | Freeze hygiene | 21 tasks · 134 items · 208 questions. scenes from public GitHub contracts, not production logs. SivletLabs/jev-eval ≠ willkelly/jev-evaluation ≠ 4esv/jev-eval ≠ xxkuboxx/jev-eval ≠ onlyoneaman/jev-eval ≠ dayhaysoos/jevals. `notes.md` §103 |
| Let sibling options attend each other / treat Hub OWNER as shipped | Option isolation | option isolation (sibling-blind). permutation-equivariant. Hub OWNER not published. nafisazizir/hev ≠ jaredpalmer/kev. `notes.md` §103 |
| Treat entropy-confidence as P(correct) / quote 93.25% as family-disjoint | Replica honesty | frozen local LLM logits, no trained decision head. residual-head 9,222-param decreased 73/96→67/96. confidence = 1−normalized entropy, not P(correct). yuki-oshio/mini-jev ≠ r-ms/mini-jev. `notes.md` §103 |
| Ask Jev to free-generate the next token / treat “kinda works” as a language model | Anti-pattern | Jev classifier as autoregressive next-token predictor. ChatJev-style soundness theater. erik-dunteman/ChatJev ≠ dannote/jev ≠ jev-gpt. `notes.md` §103 |
| Ask a Noul to discharge a Lean goal / treat timeout as “not a sample” | Formal compose | calibrated decision head × AlphaProof value head. implementation-layer isomorphism, semantic difference. timeout = censoring. do not launder Noul as proof. `notes.md` §103 |
| Ask independent rank-k questions and expect a permutation | Algorithmic scoring | parallel rank-prediction vs serial selection. independent questions can conflict. zzzzzec/jevsort ≠ keltokhy/jsort. `notes.md` §103 |
| Paste a curated list’s von/4esv line as an Augustus receipt | Catalog ≠ bake-off | curated open System One ecosystem catalog. rupeshpoojary9/awesome-open-system-one ≠ AnotiaWang/awesome-jev. `notes.md` §103 |
| Hard-threshold P(True) 0.5 as “not relevant” / mark failed evals seen | Ranking ≠ calibration | arXiv paper radar with Jev relevance scoring. ranking ≠ calibration / 0.5 still soft. fail-open failed evals not marked seen. `notes.md` §103 |
| Treat a GitHub description as a trained ~27M checkpoint / paste Colvin as hyusi | Replica honesty | train calibrated ~27M from scratch. typed Q→prob dist / one forward pass / no LLM decode. hyusi2003/MiniSystemOne ≠ Colvin0315/MiniSystemOne. description-only stub / size 5. `notes.md` §104 |
| Treat 20NG six-gate pass as graded-IR ORDER BY safety | Ranking ≠ calibration | ESCI hard probe fails four of six. jev_bool ECE 0.242 inversion 0.255. do not re-fold §60 six-gates as new. `notes.md` §104 |
| Distill Jev as teacher of record / treat size-1 UI as a student | Anti-pattern | Jairik/jev-distiller size 1. distill-Jev UI stub / do not distill Jev as teacher of record. `notes.md` §104 |
| Treat Jev self-scores as a product roadmap | Independent gold | post-launch scored use-case map / Jev self-scores then human curation. licensedsaucer9-web/jev-opportunities. `notes.md` §104 |
| Treat jevinize as TypeSafe hosted | Namesake / backend | Jev-inize a use case into classifier/router. gavinHuang/jevinize → simple-jev not TypeSafe. featherless-ai/simple-jev. `notes.md` §104 |
| Treat a fixture exit 1 as a class regression | Instrument not score | compare saved decisions / same label can still change the branch. not tested with a live Jev API key. VihaanAgarwal/jev-diff ≠ Saik0s/diffusiongemma-jev-macos. `notes.md` §104 |
| Treat constrained logprob + temp/Platt as a Noul / paste openjev-sglang as own | Constrained-AR ≠ decision head | constrained logprob + temp/Platt ≠ Noul. OpenJevPro pastes openjev-sglang JevBench as own. zhangcy122/OpenJevPro ≠ IamBusy/OpenJev ≠ ekzhang/openjev-sglang. PolyForm Noncommercial. `notes.md` §104 |
| Quote SmolLM 67 ms / 2.1% ECE as Jev identity / treat 0.5052 as calibration | Replica honesty | SmolLM-135M / sub-70ms / 0 output tokens. demo P(True) 0.5052 / Choice conf 0.2872 / Score conf 0.0055. README claims MIT / GitHub license null / no LICENSE file. `notes.md` §104 |
| Paste awesome-jev-projects listed numbers / collapse into AnotiaWang | Catalog ≠ bake-off | source-backed Awesome Jev radar / 306+ commit-pinned. auto GitHub sync / Issue-only submissions. logicrw/awesome-jev-projects ≠ AnotiaWang/awesome-jev ≠ yibie/awesome-jev ≠ cobanov/awesome-jev ≠ rupeshpoojary9/awesome-open-system-one. `notes.md` §104 |
| Quote jevbetter 0.916 as a class ceiling / treat rival-aware as option isolation | Replica honesty | hashed n-gram encoder / rival-aware attention. olanotolu/jevbetter vs jevlike starter. shuffled-context control 0.335. `notes.md` §104 |
| Show only the argmax / round Score to an integer | Distribution > argmax | structured probability readouts. distribution > argmax. Noul 0.5 midpoint. score is expectation not integer. bare HTTP not SDK. Arohtea/jev-readout. `notes.md` §105 |
| Treat schema-valid ordinary-model JSON as a Noul | Adapter ≠ replica | Jev-style Choice/Score/Noul from ordinary models. optional DSH plugin. schema-valid ≠ calibrated. gulagala001/jevify ≠ Mintzs/jevify. `notes.md` §105 |
| Quote 40.3% without the constant-answer | Open-weight measurement | Laya RLCD benchmark. 40.3% below constant-answer. open-weight measurement. mourad-ghafiri/laya-rlcd-benchmark ≠ yibie/laya-jev-lab. `notes.md` §105 |
| Let Jev be the only routing signal / hard-gate fused p | Second signal not sole | cheap fail-open semantic edge. second signal not sole. FastLoopError catch. SupremeDreamZ/jev-fastloop ≠ jev-ultrafast. `notes.md` §105 |
| Assume packed questions never move probes / treat 0.0000 sd as physics | Fan-out hygiene | asking more questions in one call. 0.980 at every N. nearly not fully deterministic. TheWebDevel/jev-fanout. `notes.md` §105 |
| Ask the VLM to pick the act / clone teacher actions | Perceive ≠ decide | Qwen3-VL perception + Jev decisions train RL. 0 model calls at deployment. VLM alone 1.7 vs +Jev 4.4. harneet2512/reflexrl ≠ khordoo/jev-reflex-autonomy-lab. `notes.md` §105 |
| Ask noul for politeness / hard-gate cascade 0.60 | Facts not judgements | independent Jev API vs Laya. cascade 0.60 matches 78% at 1.8×. noul facts not judgements. yibie/laya-jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab. `notes.md` §105 |
| Feed dict-shaped instructions to Laya / ask engines for NER spans | Locate vs decide | GLiNER vs GLiFormer vs Laya vs Jev. extractors ≠ decision engines. Laya dict-instructions collapse 58.3%. umstek/zero-shot-ie-bench. `notes.md` §105 |
| Compare raw snake points as intelligence | Throughput not intelligence | decisions-per-minute & cost. 204 moves vs 73. throughput not intelligence. angelgalvisc/snake-arena-jev-vs-llms ≠ vtrivedy/jev-plays-games. `notes.md` §105 |
| Treat a raw 0.94 as a release / pin `jev-latest` | Behavioral contracts | behavioral contracts. pin expectations eval upgrades. raw 0.94 is not a release. sathariels/jevcheck ≠ dayhaysoos/jevals ≠ SivletLabs/jev-eval. `notes.md` §105 |
| Let Jev emit filenames / treat no_direct_evidence as merge-safe | Evidence-linked remainder | evidence-linked dependency upgrade. Jev never generates filenames. no_direct_evidence ≠ safe to merge. GaneshVG18/upgrade-radar ≠ LYchoon/paper-radar-jev. `notes.md` §105 |
| One giant “what is this song about?” / treat theme as music theory | Atomic batched questions | discography theme/mood/complexity. five atomic questions one call. lirantal/discoprint. `notes.md` §105 |
| Treat a GitHub two-liner as a trained any-LLM Jev / amend PR #23 | Replica honesty | Turn any open LLM into System-One Jev. uspraveen/Jevify ≠ Mintzs/jevify ≠ gulagala001/jevify. description-only stub / size 0. do not reopen or amend PR #23. `notes.md` §106 |
| Paste Colvin 90.5s / 29.2% as hyusi / treat 26.89M as quickstart | Replica honesty | scratch-trained calibrated decision model. typed Q → probability dists. Colvin0315/MiniSystemOne ≠ hyusi2003/MiniSystemOne. no published weights download URL. p_i/p_j independent of other candidates. `notes.md` §106 |
| Treat JSON parse of generated text as a Noul / Journal Entry Voucher | Replica honesty | System-1 decision engine for local LLMs. structured choices only. JSON parse of generated text ≠ Noul. TypefAI JEV / Journal Entry Voucher. tapsin/jev-local ≠ us/jev-local ≠ Argos1111/jev_local. `notes.md` §106 |
| Quote 46x / 91.1% / 92.58% / 84.8 as class ceilings | Sensors not identity | 46x speedup / accuracy identical. ECE 0.624 sentiment catastrophe. 91.1 % / ECE 0.022 *theirs*. RewardBench v1 92.58%. classifier.dev fast tier 84.8 is Jev behind its own API. `notes.md` §106 |
| Treat classifier.dev #1 as a better model / re-fold §78 as new | Densify ≠ re-fold | JevBench v1 — smart/cheap/fast/reliable. I/C/S/K 25% geometric mean. do not re-fold §78 v1.2 board as new. Laya (421M) 70.1 now on board. `notes.md` §106 |
| Ask Jev to perform budget arithmetic / treat XState as Jev | Formal compose | hard budget filter before Jev. Jev never asked to perform budget arithmetic. Jev judges the next state, XState enforces transitions. simulation uses synthetic keyword fixtures. `notes.md` §106 |
| Paste catalog ★ as eval / treat SPLADE as TypeSafe Jev / empty Space as a win | Catalog / port honesty | catalog gravity. ★339 live REST. curation is not endorsement. query-side encoders, not a Jev replica. This Space contains no benchmark result yet. 12-case plumbing fixture. transformers.js AutoModel cannot load this graph. `notes.md` §106 |
| Quote 62.3% without the 4.5pp miss / let Jev sum prices | Sensors not identity | Benchmark-driven Jev router and judge. cheap alone is not success. Jev does not write, sum prices, or claim accuracy %. Sol 94.2 / Luna 83.9 / Jev path 89.7. erendikmenn/jev-llm-router-benchmark ≠ jev-rag-benchmark ≠ ryantsai/jev-llm-router. `notes.md` §107 |
| Collapse ticket-router into Sarath / hard-gate 0.6 / treat mock keyword as production | Formal compose | Express + node:sqlite. mock and Jev decision engines. previous_ticket_count >= 3 is code. MIN_CONFIDENCE 0.6 still soft. substring false positives. aesaganda/jev-ticket-router ≠ SarathChandraBellam/jev-vs-llm-ticket-router. `notes.md` §107 |
| Hard-gate figure 0.85 as FAST_PATH / let generative AI author scientific plots | Soundness theater | Universal Figure & Diagram Router. confidence ≥ 0.85 hard-gate is theater. generative AI banned from scientific plots. six visual branches. `notes.md` §107 |
| Collapse jev-bench into jevbench / quote unpublished baselines as Harbor | Feedstock ≠ board | human-labeled (state, question, label). 166,054 rows / 22 configs. soft_label for human uncertainty. Praveenrajus/jev-bench ≠ fstandhartinger/jevbench. `notes.md` §107 |
| Treat 100/100 easy T/F as Harbor / treat label_mass as correctness / collapse Nicolai spellings | Replica honesty | ternary bonsai System One GGUF. openjev's mechanism, Bonsai's weights. Hub does not ship weights. 100/100 easy T/F is not Harbor. label_mass ≠ correctness. stock llama.cpp Q2_0 silently gibberish. NicolaiMTLassen/open-bonzi-jev ≠ NicolaiLassen. `notes.md` §107 |
| Collapse DeBERTa ONNX into Qwen scorer ONNX / re-card source as new | Port honesty | transformers.js DeBERTa ONNX. source:com-kotobalabs/open-jev-deberta-v3-large. temperature 1.05. AutoModel from_pretrained works. onnx-community/open-jev-deberta-v3-large-ONNX ≠ system-one-qwen3.5-4b-scorer-ONNX. `notes.md` §107 |
| Re-fold §71 as a beat / treat 151M vs 149.6M as two models / treat closed PR #1 as verified | Densify ≠ beat | 107★ densify. GH 151M vs README 149.6M. PR #1 now closed unmerged. do not re-fold §71 claim-audit as a beat. `notes.md` §107 |
| Treat jev-study mock as live API / treat structured as correct | Study densify | typed decisions, RLCD, confidence-gated routing. structured ≠ correct. mock not live API. 26 tests. wjdjdakf17/jev-study ≠ baekenough/jev-study. `notes.md` §107 |
| Treat WANLI-256 / easy100 as Harbor / treat Hub family cards as shipping weights | Replica honesty | bonzi-27b-v2 / ternary-8b / 27b-v1 GGUF family densify. WANLI-256 74.6% / 65.2% / 71.1% *theirs*. Hub still does not ship weights. ternary still needs PrismML fork. Bonsai 1 27B Q1_0 runs on stock llama.cpp. `notes.md` §108 |
| Collapse stock Q1_0 into §107 Q2_0 gibberish | Family split | Bonsai 1 27B Q1_0 runs on stock llama.cpp. Do **not** collapse stock Q1_0 into “stock llama.cpp Q2_0 silently gibberish”. `notes.md` §108 |
| Treat HF twin as a weights drop / likes 5 as GH 107★ | Densify ≠ beat | hf:heman10x/openJev-verdict-2.0 twin tokenizer-only. `notes.md` §108 |
| Treat CLEVR joint 0% as vision Jev works / 294,912 as independent samples | Perceive honesty | OpenJev Vision image classification + uncertainty. CLEVR-4 held-out joint 0%. hfdataset:IamBusy/OpenJev-Vision-Research-v0.1 12,832. 294,912 derived targets not independent samples. `notes.md` §108 |
| Treat ONNX 63/63 as ECE | Port honesty | Laya multilingual ONNX WebGPU typed-decisions port. 63/63 selected answers / 5.1e-4 CPU / 1.2e-2 WebGPU. `notes.md` §108 |
| Treat UpHash as a new species / quote 93.25% as Harbor | Transfer densify | UpHash-Network/mini-jev is yuki-oshio transfer. residual-head 9,222-param decreased 73/96→67/96. `notes.md` §108 |
| Hard-gate injection ECE 0.058 / route 0.5–0.9 as frequency | Ranking ≠ calibration | jev-injection-bench 11,900 labelled prompts. Jev best ranking / Haiku better ECE 0.021 vs 0.058. 0.5–0.9 band is where Jev's numbers do not mean what they say. Prompt wording moves panic 28%. `notes.md` §108 |
| Treat dspy-bench as a quality claim / merge gate | Similarity never GT | manojlds/jev-dspy-bench ≠ dspachos/jev-dspy ≠ jmanhype/jev-dspy-lab. Jev agreement is similarity, never ground truth. no aggregate quality grade or merge gate. `notes.md` §108 |
| Quote AbstentionBench rank 1 without question-asymmetry / 2025 field | Asked-to-abstain ≠ saw-bare-question | AbstentionBench-on-Jev rank 1 of 20 vs 2025 field. question-asymmetry. forward-looking 0.465 never extreme. `notes.md` §108 |
| Treat openkev as a runtime / T as transferable / inf as a bug | Calibration layer | openkev calibration layer not a runtime. ECE vs coverage independent. select_threshold returns inf. escalation catches uncertainty not ignorance. misakaikato/openkev ≠ jaredpalmer/kev. `notes.md` §108 |
| Hard-gate pdf-race 12/12 / treat titles as generated | Parser owns clock | pdf-race Docling→Jev vs Gemini. parser owns the wall clock. 12/12 tie is a tie. titles selected not generated. `notes.md` §108 |
| Treat atlas listed counts as eval | Catalog ≠ endorsement | ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas. `notes.md` §108 |
| Hard-gate flopcheck composite / let Jev count em dashes | Mechanical tells in code | flopcheck 16 calibrated tweet judgments. mechanical tells in code. `notes.md` §108 |
| Ship 40-row T / treat T as changing argmax / confidence as top-label p | T never changes argmax | Laya calibration lab Gradio MCP. T never changes argmax. confidence ≠ top-label p. easy probe set refused. 40–48 rows too small to ship T. `notes.md` §108 |
| Collapse kushalpatil into Mintzs / gulagala001 / uspraveen / treat LoRA stubs as eval | Replica honesty | Gemma-4 26B-A4B jevify classification+calibration. Hub jevify merged LoRA ships weights. LoRA adapter twin not independent eval. GH kushalpatil07/jevify 404. `notes.md` §109 |
| Treat WANLI-256 64.5/60.2/52.0 as Harbor / re-card §108 27B | Family fill | bonzi Bonsai-8B v1 GGUF densify. Bonsai-1.7B v1. Bonsai-4B v1. rank #4 / #5 / #6 of 6. `notes.md` §109 |
| Treat thin README scaffolding as a Harbor harness / collapse JulesHuisman into SivletLabs | Scaffolding | JulesHuisman/jev-eval scaffolding / README SHA c356a584 (was empty e69de29b). `notes.md` §109 |
| Quote 40-band 0/10 without 7-band | Menu resolution | 7 bands 6/10 vs 40 bands 0/10. `notes.md` §109 |
| Quote 32/32 as production / hard-gate 0.8 | Smoke | source receipts + confidence slider re-policy without re-inference. 32/32 synthetic is smoke not production. `notes.md` §109 |
| Use roadus2 / paste vs-Jev as this-fork win | Watch misspelling | roadus2 watch misspelling; lock roadius2/ultra_laya. ultra_laya REVIEW defects. default branch claude/laya-jev-review-gg5ppo. `notes.md` §109 |
| Treat MASSIVE as equal / ignore p_max identity | Language OOD | XNLI EN 88.3% ECE 0.032 → RU 77.3% ECE 0.096. MASSIVE no detectable difference at n=600. confidence is function of p_max (r=1.000). `notes.md` §109 |
| Treat jev-llm as a generator | Pointer-not-generator | pointer-not-generator 400 human-authored responses. `notes.md` §109 |
| Treat proposed as authorized / gated 100% as production | Evidence ≠ authority | proposed ≠ authorized. gated 100% (95/95) coverage 59.375%. `notes.md` §109 |
| Treat /judge 0.5 as truth | 0.5 still soft | judge-jev 0.5 still soft. `notes.md` §109 |
| Treat A/B/C as Harbor / Awesomejev 656 as eval | Catalog ≠ endorsement | 947 repos scored; A 273 / B 302 / C 372. LLM rubric ≠ benches. No benchmark winner is claimed. Awesomejev 656 entries / 38,160 stars. `notes.md` §109 |
| Copy npm install for a Cargo crate | README honesty | README npm global; repo is Rust. `notes.md` §109 |
| Treat 11% as a person verdict | Code owns count | git-confess code owns counting/blame/ratio. httpx exhibit 11% (13/119) *theirs*. `notes.md` §109 |
| Treat +12.40% as edge | Honest negative | 90d trend +12.40% vs random +12.75% vs BH +41.71%. 5m win rate 25%. `notes.md` §109 |

| Treat Blackwood tracker-absent as landed / Hub Meanblock as new species | Census densify | Blackwood tracker ABSENT; likes 2 gated manual. GH Meanblock 404; lock leesk212/JEV-CPU. softmax over letter slots ≠ Noul. `notes.md` §110 |
| Treat ECE 0.021 as a hard gate / Independent as Choice | RLCD / Independent | r = c - p_a. ECE 0.021; acc 0.807 vs warmup 0.746. Independent primitive. default path is pretrained Gemma probs not trained RLCD head. `notes.md` §110 |
| Distill Jev as teacher / 3-way NLI as Noul | Teacher-copy vs gold vs zeroshot | do not distill Jev as teacher of record (they distilled Haiku). priority 0.464 = majority floor. banking77 contaminated. raw margins not probabilities. 3-way NLI ≠ Noul. WANLI 0.741 vs openjev v2 0.77 *theirs*. `notes.md` §110 |
| Treat 0.9 as one number / collapse into Praveenrajus | Ranking ≠ calibration | “0.9 is not one number”. ranking ≠ calibration. banking77 0.8–0.9 stated 0.86 actual 0.73 over-confident *theirs*. ≠ Praveenrajus/jev-bench ≠ fstandhartinger/jevbench. `notes.md` §110 |
| Treat circulating $0.0004 as measured / Score as 0–1 / Noul.confidence as existing | Measurement honesty | $0.0000153–$0.0000226 vs circulating $0.0004 (~20×). Score is 0..n-1 expectation not 0–1. Noul has no confidence field. type reliability is not a reason to choose Jev (json_schema 5/5). `notes.md` §110 |
| Treat 8/8 as conversion lift / 200-row as ranking | Designed cases / pilot | Function-only 5/8 vs hybrid 8/8. 4/8 without Jev. 8 designed cases not conversion lift. 200-row pilot Jev 86.5% 173/200 vs Gemini Flash-Lite 86.0% 172/200 vs Pro 87.0% 174/200 *theirs*. not a ranking. `notes.md` §110 |
| Collapse joshhu into realZachi / treat 64× Space as Harbor | Namesake / synthetic | 情緒測謊器. ≠ realZachi/jevtest. 8-example Jev vs GPT-5.6 Sol ~64× cost 5.4× latency *theirs*. synthetic; no inference. ≠ JevBench v1.2 §78. `notes.md` §110 |
| Treat listed counts as eval / paste APA overclaim | Catalog ≠ endorsement | Judged 3317 / listed 2560. Jev judges, code applies policy. APA “microsecond policy / zero hallucination” overclaim. `notes.md` §110 |
| Treat selecting an option as permission / LSP as a proof | User decides / pattern exact | Jev judges / agent reasons / user decides. selecting an option is not permission to implement. degraded fallback. pattern exact, judgement must clear floor. no matching pattern → no model call. not a correctness oracle. `notes.md` §110 |
| Treat 0.85 as 85% / minProbability as Harbor / same-pool rescoring | Soundness theater | Spec vs artifact remainder. treating 0.85 as 85% / minProbability hard-gate as Harbor. VERIFY acquires discriminating evidence, never same-pool confidence-only rescoring. fast/full/max are ceilings not sizes. Solar writes, Jev chooses NEXT ACTION. `notes.md` §110 |


| Treat ECE as alpha | Calibration ≠ edge | Calibration is not alpha. NO CURRENT ALPHA CANDIDATE. `notes.md` §111 |
| Treat 0.5 compaction as safety | Threshold theater | default 0.5 keeps zero non pinned. judges results it never sees. `notes.md` §111 |
| Collapse sgr-judge-bench into jev-judge-bench | Sibling lock | slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench. paired Jev accuracy-difference intervals include zero. not evidence of equivalence. `notes.md` §111 |
| Treat softmax A/B/C as Noul | Wire-compat ≠ replica | prefill plus exactly one decode. softmax over A/B/C ≠ Noul. overconfident. `notes.md` §111 |
| Collapse jasonkneen into pngwn | Namesake | jasonkneen/open-jev ≠ pngwn/open-jev. same sha d41dc3cd. encode the state once, decide everything in parallel. `notes.md` §111 |
| Treat 0.8 nlgrep as 80% / 40-line as proof | Soft threshold | YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep. default threshold 0.8 still soft. 40-line windows cannot prove whole function. `notes.md` §111 |
| Treat contract_passed as truth / Wilson 0.85 as proof | Soundness theater | contract_passed is not a claim of guaranteed factual truth. Wilson lower bound 0.85 floor. fixture mode no savings claim. `notes.md` §111 |
| Treat 97.0% as Harbor / five messages as bake-off | Synthetic / handful | 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22. synthetic repository benchmark. handful of hand-written examples, not a benchmark. Jev judged exactly what it was given. `notes.md` §111 |

Hourly 0646 uniqueness lock: Calibration is not alpha; NO CURRENT ALPHA CANDIDATE; ΔR² approximately +0.00084; Brier 0.2131387; ECE 0.0421875; Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05; default 0.5 keeps zero non pinned; keepResult median 0.14 to 0.17; keepCall median 0.28 to 0.35; usable range is about 0.10 to 0.25; 7.8% to 57.9%; judges results it never sees; task-finish eval not built yet; $0.002 per compaction; slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench; Jev 108/120 $0.083 0.34 s; Luna SGR 114/120; paired Jev accuracy-difference intervals include zero; not evidence of equivalence; GLM SGR 26/120 93 format failures; Terra-planned Jev hybrid 55/120; rule-based by default, optionally Jev-backed; empty README; missing key cannot break the experience; prefill plus exactly one decode; softmax over A/B/C ≠ Noul; BBQ 9,053/10,000 (90.53%); ECE 0.0890; Mean confidence 0.9943; overconfident; score and noul not implemented; DGUI 12 rows (was 6); INSTRUCT 119 rows likes 2; encode the state once, decide everything in parallel; 0.740 accuracy against a 0.508 majority; ECE 0.047; fine-tune's advantage ends where its 384-token training data does; jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd; Space does not call Jev; recomputes routing from saved probabilities; 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22; synthetic repository benchmark; Jev evaluations are advisory; YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; default threshold 0.8 still soft; 40-line windows cannot prove whole function; token-native sequential start/end Choice; Gemini/Haiku stubs not configured yet; handful of hand-written examples, not a benchmark; Jev judged exactly what it was given; laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills; contract_passed is not a claim of guaranteed factual truth; Wilson lower bound 0.85 floor; fixture mode no savings claim; SemIf 2207★ (+21 vs §110 2186); jevlike 1043★ (+5 vs 1038); TypeAR 15★ (+1 vs 14); AnotiaWang 97★ (+1 vs 96); yibie/awesome-jev 506★ (+16 vs 490); Laya likes 822 (was 802); tracker likes 64 flat, lastModified UNCHANGED; do not reopen or amend PR #23/#24/#25/#26/#27/#28.

User-provided 0806 uniqueness lock: people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 415 / 179; impressions 34844 / 9238; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29.

Hourly 0541 uniqueness lock: calibration beyond ~500 tokens unmeasured; 11.57s vs 54.10s · 4.67× · 120/128 *theirs*; GH jev-haiku-benchmarking 404; TCP floor 198.8 ms; gateway tax not one number; ≠ RadRebelSam/awesome-jev; NLI Tetris argmax P(entail)−P(contradict); 1q 396ms / 30q 567ms; ±0.03; 33q $0.000045 vs Gemini ~5× slower ~60× cost *theirs*; catalog ≠ endorsement; Client-side quiz; pointer from held docs; scanned-PDF warn; CSP only api.typesafe.ai; $0.00022 vs chat $0.00306 *theirs*; SemIf 2186★ (+20 vs §109 2166); jevlike 1038★ (+7 vs 1031); TypeAR 14★ flat; AnotiaWang 96★ (+1 vs 95); yibie/awesome-jev 490★; Laya likes 802 (was 783); tracker likes 64 flat, lastModified UNCHANGED; do not reopen or amend PR #23/#24/#25/#26/#27.

| Each answer right, decision wrong | Policy wrong | Change weights/thresholds in code, leave questions alone |

## Revision discipline

- Change one or two questions per revision; probabilities shift unpredictably — leave good discriminators untouched.
- Judge revisions on labeled data; higher confidence alone proves nothing.
- Keep the answer space stable once code depends on it (changing levels/opts rewrites every earlier answer's meaning).
- General rules in instructions/criteria; specific names/values only in `examples`.

Confidence-gated routing (doc defaults): act / confirm-or-flag / hand off, floors 0.5–0.6, 0.85–0.9 for high-stakes — starting points, not constants (calibration must be re-measured per dataset; see validation.md).
