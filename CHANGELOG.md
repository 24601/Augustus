# Changelog

All notable changes to Augustus are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versioning
follows [SemVer](https://semver.org/spec/v2.0.0.html).

Each release notes the [`typesafe-ai/skills`](https://github.com/typesafe-ai/skills)
revision it was written against. That skill owns integration contracts;
Augustus owns design judgment. Re-read live TypeSafe docs before treating a
pin as current API behavior.

Hourly uniqueness locks from folds after v0.3.0 were moved out of this
file so release notes stay scannable. Archive:
[`research/changelog-hourly.md`](research/changelog-hourly.md). Canonical
folds: `research/notes.md`.

## [Unreleased]

Hourly 0823 HIGH (`research/notes.md` §143 / composition items
697–712 / findings batch #125). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#66.
Do not amend released 0.5.0 (#42). Merged #66 owns §142. Merged #65
owns §141. Merged #64 owns §140.

### Added

- **Hourly 0823 HIGH (`notes.md` §143).** dohnuts densify MODEL_CARD.
  JevBench 65.80% vs Jev 86.58% / Laya multi 47.62% *theirs*. 78.21%
  macro accuracy *theirs*. 180,031 decisions *theirs*. same-species
  serving not an 18th scoring row. densify §137 not a sibling first
  sighting. FluidUse field→value match among supplied options not free
  text. Screenshots aren't uploaded. Jev is the only model. not fully
  offline. JSON 0.909 letters 0.907 *theirs*. model=jev-auto. AG News
  0.910 *theirs*. Fastest and cheapest web agent *theirs*. densify
  description rewrite. skip-thin empty SHA. Futureppo/typesafe_register
  key-farming skip.
  Evaluator: dohnuts JevBench 65.80% is not Harbor / FluidUse
  field→value is not free text / same-species serving is not an 18th
  scoring row / Cua-S1 is not TypeSafe / densify §137 not sibling.
  uniqueness_gate.py now checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 +
  1049 + 1143 + 1248 + 1340 + 1441 + 1542 + 1643 + 1746 + 1843 + 1936 +
  Open-Jev densify + 1946 + 2049 + 2146 + 2246 + 2347 + 0049 + 0151 +
  0248 + 0348 + 0445 + 0551 + 0707 + 0823.
  Composition items 697–712 / batch #125.
  **HARD RULE:** do not reopen or amend PR #23–#66. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat JevBench
  65.80% as Harbor, same-species serving as an 18th scoring row, or
  field→value form fill as free text. With Augustus: *theirs* not
  Harbor; field→value match among supplied options not free text;
  densify §137 not a sibling first sighting; Cua-S1 ≠ TypeSafe;
  Screenshots aren't uploaded; softmax over letters ≠ calibrated Noul.


Hourly 0707 HIGH (`research/notes.md` §142 / composition items
681–696 / findings batch #124). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#65.
Do not amend released 0.5.0 (#42). Merged #65 owns §141. Merged #64
owns §140. Merged #63 owns §139.

### Added

- **Hourly 0707 HIGH (`notes.md` §142).** Jev-cu text-only CU.
  只传文字，不传截图. Text only no screenshots. tax-doc 100% of our tax
  document corpus at $0.001 per page. TaxCalcBench 0 strict errors
  *theirs*. blank IRS 38 strict errors 5.05% *theirs*. 100% of corpus
  *theirs* not Harbor. The model does not receive screenshots. game
  success ≠ calibrated Noul. 21 seconds for 9 actions *theirs*. A
  completed booking is not demonstrated. The field guide to typed
  decisions. densify §141 not a sibling first sighting.
  hf:Praveenrajus/jev-bench HTTP 401 was 200. ENEM 2025 *theirs* not
  Harbor. skip-thin empty SHA.
  Evaluator: text-only CU is not screenshots / 100% of corpus is not
  Harbor / Mario game success is not Noul / completed booking is not
  demonstrated / ENEM bench is not Harbor.
  uniqueness_gate.py now checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 +
  1049 + 1143 + 1248 + 1340 + 1441 + 1542 + 1643 + 1746 + 1843 + 1936 +
  Open-Jev densify + 1946 + 2049 + 2146 + 2246 + 2347 + 0049 + 0151 +
  0248 + 0348 + 0445 + 0551 + 0707.
  Composition items 681–696 / batch #124.
  **HARD RULE:** do not reopen or amend PR #23–#65. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat text-only CU
  as screenshots, 100% of a tax corpus as Harbor, or a Mario win as a
  Noul. With Augustus: Text only no screenshots; 100% of corpus *theirs*
  not Harbor; game success ≠ calibrated Noul; A completed booking is not
  demonstrated; densify §141 not a sibling first sighting; *theirs* not
  Harbor.


Hourly 0551 HIGH (`research/notes.md` §141 / composition items
665–680 / findings batch #123). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#64.
Do not amend released 0.5.0 (#42). Merged #64 owns §140. Merged #63
owns §139. Merged #62 owns §138.

### Added

- **Hourly 0551 HIGH (`notes.md` §141).** kev Night-2 densify.
  locked OOD 0.684/0.837/0.852 *theirs*. v7-base tags. Night-2
  sign-off. Nimble densify: did not distill from Jev. Publish
  original 2676 training examples and frozen 324 holdout. APUS-OpenJev
  9B 85.0% vs Jev API 82.5% *theirs* not Harbor. Frozen80 n=80.
  Candidate probabilities are not calibrated confidence. Jev-Vision
  Hub LoRA. evoke densify: Jev is the first adapter the design is
  bound to no engine. GLiNER Zero Hallucinations marketing. Locate ≠
  decide. catalog ≠ endorsement. skip-thin empty SHA.
  Evaluator: kev Night-2 OOD is not Harbor / Nimble did not distill /
  APUS Frozen80 is not Harbor / Jev-Vision hard overconfidence is not
  calibrated / GLiNER Locate ≠ decide.
  uniqueness_gate.py now checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 +
  1049 + 1143 + 1248 + 1340 + 1441 + 1542 + 1643 + 1746 + 1843 + 1936 +
  Open-Jev densify + 1946 + 2049 + 2146 + 2246 + 2347 + 0049 + 0151 +
  0248 + 0348 + 0445 + 0551.
  Composition items 665–680 / batch #123.
  **HARD RULE:** do not reopen or amend PR #23–#64. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat Night-2
  OOD 0.852 as Harbor, Frozen80 85.0% as TypeSafe, or GLiNER locate as
  a decision head. With Augustus: temperature scaling ≠ ECE unless
  measured; Candidate probabilities are not calibrated confidence;
  Locate ≠ decide; densify §45 not a sibling first sighting; *theirs*
  not Harbor.


Hourly 0445 HIGH (`research/notes.md` §140 / composition items
649–664 / findings batch #122). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#63.
Do not amend released 0.5.0 (#42). Merged #63 owns §139. Merged #62
owns §138. Merged #61 owns §137.

### Added

- **Hourly 0445 HIGH (`notes.md` §140).** lcc real Laya keep-all.
  Token reduction alone is not cost reduction. keeps essentially every
  block 0.0%/−0.5% *theirs*. mock Laya = Jev −22.6% on XL withdrawn.
  Chat 1282.3 ms vs gateway 232.1 ms ~1/5.5 *theirs*. Softmax over
  candidate logprobs. any2jev acc 0.796 ECE 0.027 *theirs*. How you
  ask mattered more. Calibration is not yet measured. NanoJev densify
  JevHarness §115. Awesomejev 691→802 quote watch not re-derive.
  serving substrate ≠ calibrated replica. skip-thin empty SHA.
  Remainder densify: traffic sim is not a digital twin; xiangqi Score
  fan-out ≠ chess engine; KorWF-Pi Jev cannot waive a failing check.
  Evaluator: lcc keep-all is not cost reduction / softmax gateway is
  not logit-equiv / acc 0.796 ECE 0.027 *theirs* / How you ask mattered
  more / Calibration is not yet measured / not a digital twin / Score
  fan-out ≠ chess engine / Jev cannot waive a failing check.
  uniqueness_gate.py now checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 +
  1049 + 1143 + 1248 + 1340 + 1441 + 1542 + 1643 + 1746 + 1843 + 1936 +
  Open-Jev densify + 1946 + 2049 + 2146 + 2246 + 2347 + 0049 + 0151 +
  0248 + 0348 + 0445.
  Composition items 649–664 / batch #122.
  **HARD RULE:** do not reopen or amend PR #23–#63. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat lcc keep-all
  as cost reduction, 232.1 ms as logit-equiv, ECE 0.027 as Harbor, or
  arcade 70/80 as calibrated Noul. With Augustus: Token reduction alone
  is not cost reduction; wire-compat ≠ logit-equiv; Softmax over options
  ≠ calibrated Noul; How you ask mattered more; Calibration is not yet
  measured; densify §115 not a sibling first sighting; *theirs* not Harbor.


Hourly 0348 HIGH (`research/notes.md` §139 / composition items
633–648 / findings batch #121). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#62.
Do not amend released 0.5.0 (#42). Merged #62 owns §138. Merged #61
owns §137. Merged #60 owns §136.

### Added

- **Hourly 0348 HIGH (`notes.md` §139).** open-cricket BYOM Qwen2.5-1.5B.
  wire-compat ≠ logit-equiv. Qwen2.5 ≠ Archer. replica ≠ TypeSafe.
  Greedy 0.90 vs Oracle 0.82 *theirs*. Random conf 0.00 still 20.5%
  *theirs*. confidence ≠ P(correct). seed 42 n=1 is not Harbor.
  8,400 calls $0.39 *theirs*. Noul 0.7 true 44% *theirs*.
  JevBench 81.65 *theirs* not Harbor. WindTunnel 49/49 *theirs* not Harbor.
  0-byte Mandelbrot is not a replica. training not complete.
  OpenJev-Kit IS meijustory123/openjev (same GitHub id 1379187719).
  Compose meaning like state. A clean report is not proof.
  does not sandbox. skip-thin empty SHA.
  Evaluator: open-cricket wire-compat ≠ logit-equiv / Greedy 0.90 is not
  P(correct) / Noul 0.7 true 44% *theirs* / JevBench 81.65 *theirs* not
  Harbor / training not complete / 0-byte Mandelbrot is not a replica.
  uniqueness_gate.py now checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 +
  1049 + 1143 + 1248 + 1340 + 1441 + 1542 + 1643 + 1746 + 1843 + 1936 +
  Open-Jev densify + 1946 + 2049 + 2146 + 2246 + 2347 + 0049 + 0151 +
  0248 + 0348.
  Composition items 633–648 / batch #121.
  **HARD RULE:** do not reopen or amend PR #23–#62. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat open-cricket
  as TypeSafe, Greedy 0.90 as P(correct), JevBench 81.65 as Harbor, or a
  clean scanner report as a sandbox. With Augustus: wire-compat ≠
  logit-equiv; confidence ≠ P(correct); seed 42 n=1 is not Harbor;
  *theirs* not Harbor; 0-byte Mandelbrot is not a replica; A clean report
  is not proof; does not sandbox.

Hourly 0248 HIGH (`research/notes.md` §138 / composition items
617–632 / findings batch #120). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#61.
Do not amend released 0.5.0 (#42). Merged #61 owns §137. Merged #60
owns §136. Merged #59 owns §135.

### Added

- **Hourly 0248 HIGH (`notes.md` §138).** GLiClass knowledgator Hub
  family class-peer catalog not Jev equivalent. instruct-large sha
  825e5478c1bf. typed-decision-leaderboard *theirs* not Harbor. JEV
  0.7350 ZTC 27B 0.7289 *theirs*. Jevbridge ACP and MCP adapter.
  wire-compat ≠ logit-equiv. Cut the slop. Not a Cua binding. open
  reproductions of the shape. 82.3% ECE 0.017 *theirs*. serving
  substrate ≠ calibrated replica. skip-thin empty SHA.
  Evaluator: GLiClass class-peer ≠ Jev replica / typed-decision-leaderboard
  *theirs* not Harbor / Jevbridge wire-compat ≠ logit-equiv / Not a Cua
  binding.
  uniqueness_gate.py now checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 +
  1049 + 1143 + 1248 + 1340 + 1441 + 1542 + 1643 + 1746 + 1843 + 1936 +
  Open-Jev densify + 1946 + 2049 + 2146 + 2246 + 2347 + 0049 + 0151 + 0248.
  Composition items 617–632 / batch #120.
  **HARD RULE:** do not reopen or amend PR #23–#61. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat Hub GLiClass
  as a Jev replica, 0.7350 as Harbor, Jevbridge as logit-equiv, or LiteRT
  as calibrated Noul. With Augustus: GLiClass class-peer catalog not Jev
  equivalent; typed-decision-leaderboard *theirs* not Harbor; wire-compat
  ≠ logit-equiv; serving substrate ≠ calibrated replica; Not a Cua
  binding.


Hourly 0151 HIGH (`research/notes.md` §137 / composition items
601–616 / findings batch #119). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#60.
Do not amend released 0.5.0 (#42). Merged #60 owns §136. Merged #59
owns §135. Merged #58 owns §134.

### Added

- **Hourly 0151 HIGH (`notes.md` §137).** Open-Jev v3 densify HEAD
  ed45657bf726 / README SHA 12e0f581e15d. v3 data prepared ≠ retrained
  released models. held-out protocol ≠ Harbor. 1,280-row panel ≠ Harbor.
  finite training loss ≠ quality improvement. website redesign ≠
  calibration. jev-wide naive throws away 83% *theirs*. certo KL 0.008
  acc 0.844 ECE 0.004 *theirs*. first-instinct 63.3%→78.1% *theirs* not
  Harbor. Jev is a gate not a generator. community port ≠ TypeSafe.
  skip-thin empty SHA.
  Evaluator: v3 prepared ≠ retrained / held-out protocol ≠ Harbor /
  1,280-row panel ≠ Harbor / finite loss ≠ quality / website redesign ≠
  calibration / naive merge throws 83.
  uniqueness_gate.py now checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 +
  1049 + 1143 + 1248 + 1340 + 1441 + 1542 + 1643 + 1746 + 1843 + 1936 +
  Open-Jev densify + 1946 + 2049 + 2146 + 2246 + 2347 + 0049 + 0151.
  Composition items 601–616 / batch #119.
  **HARD RULE:** do not reopen or amend PR #23–#60. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat v3 rows as a
  released replica, a held-out protocol as Harbor, 83% as Harbor, or Jev
  as a Lean writer. With Augustus: v3 data prepared ≠ retrained released
  models; held-out protocol ≠ Harbor; 1,280-row panel ≠ Harbor; finite
  training loss ≠ quality improvement; website redesign ≠ calibration;
  Jev is a gate not a generator; *theirs* not Harbor.
  Same split for any Choice/Score/Noul-style head, not only hosted Jev.


Hourly 0049 HIGH (`research/notes.md` §136 / composition items
585–600 / findings batch #118). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#59.
Do not amend released 0.5.0 (#42). Merged #59 owns §135. Merged #58
owns §134. Merged #57 owns §133. Merged #56 owns §132.

### Added

- **Hourly 0049 HIGH (`notes.md` §136).** Open-Jev JevBench public-subset
  densify HEAD f46ff604f794 / README SHA e32c4bbd519c. public-subset ≠
  Harbor. 231 ≠ 534. kev 35B densify HEAD e0bcf50153f1 / README SHA
  unchanged. PLAN correct 35B MMLU-Pro (0.550). evaluate.load honour
  weights_dtype=bf16. wy-coliney/jev-browser-use 282★ 5-10× *theirs*
  not Harbor. gargpratyush/jev-router fail-open routing ≠ permission.
  BillionsBobby/JevRouter 38% 44% vs 24% *theirs* not Harbor. ordered
  routing ≠ end-to-end. daseinlabs/open-jev softmax next-token ≠
  calibrated Noul. potential_match ≠ hiring decision. AntonioCoppe/jev-harness
  already carded. skip-thin empty SHA.
  Evaluator: JevBench public-subset ≠ Harbor / 231 ≠ 534 / MMLU-Pro 0.550
  *theirs* / evaluate.load bf16 honour / 5-10× is not Harbor.
  uniqueness_gate.py now checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 +
  1049 + 1143 + 1248 + 1340 + 1441 + 1542 + 1643 + 1746 + 1843 + 1936 +
  Open-Jev densify + 1946 + 2049 + 2146 + 2246 + 2347 + 0049.
  Composition items 585–600 / batch #118.
  **HARD RULE:** do not reopen or amend PR #23–#59. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat 231 as the
  full 534, 0.550 as Harbor, 5-10× as a replica, or fail-open routing as
  a grant. With Augustus: public-subset ≠ Harbor; 231 ≠ 534; evaluate.load
  honour bf16; 5-10× *theirs* not Harbor; routing ≠ permission;
  softmax next-token ≠ calibrated Noul; *theirs* not Harbor.
  Same split for any Choice/Score/Noul-style head, not only hosted Jev.

Hourly 2347 HIGH (`research/notes.md` §135 / composition items
569–584 / findings batch #117). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#58.
Do not amend released 0.5.0 (#42). Merged #58 owns §134. Merged #57
owns §133. Merged #56 owns §132.

### Added

- **Hourly 2347 HIGH (`notes.md` §135).** openjev MLX densify HEAD
  2050fdb8280d / README SHA d5322e16e565. MLX backend steps>1/think/text
  gen + image Qs. dual serving is not generate. Hosted Codiv ≠ TypeSafe.
  wire-compat ≠ logit-equiv. TypeLLM Release v0.1.1 densify HEAD
  8a8b4aefd443 / README SHA unchanged. GitHub Release v0.1.1.
  Constrained AR ≠ calibrated Noul. PyPI packaging ≠ calibrated Noul.
  JevLoop 6★ independent not affiliated. WANLI-256 74.6% *theirs*.
  option order 0.188 or 0.542 *theirs*. jevtok 0 mismatches *theirs*
  not Harbor. ockev 35ms 95.8% TomatoEggBench *theirs* not Harbor.
  n=8 is not Harbor. Evaluator: MLX text gen ≠ calibrated Noul /
  GitHub Release v0.1.1 ≠ calibrated Noul / n=8 is not Harbor /
  ranking before lossless condensation.
  uniqueness_gate.py now checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 +
  1049 + 1143 + 1248 + 1340 + 1441 + 1542 + 1643 + 1746 + 1843 + 1936 +
  Open-Jev densify + 1946 + 2049 + 2146 + 2246 + 2347.
  Composition items 569–584 / batch #117.
  **HARD RULE:** do not reopen or amend PR #23–#58. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat MLX text
  gen as a calibrated replica, a GitHub Release as a Noul, n=8 as Harbor,
  or option-order 0.188 as gold. With Augustus: dual serving is not
  generate; Hosted Codiv ≠ TypeSafe; wire-compat ≠ logit-equiv; Constrained
  AR ≠ calibrated Noul; PyPI packaging ≠ calibrated Noul; n=8 is not
  Harbor; option order can change an answer; *theirs* not Harbor.
  Same split for any Choice/Score/Noul-style head, not only hosted Jev.



Hourly 2246 HIGH (`research/notes.md` §134 / composition items
553–568 / findings batch #116). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#57.
Do not amend released 0.5.0 (#42). Merged #57 owns §133. Merged #56
owns §132. Merged #55 owns §131. Merged #54 owns §130. Merged #53
owns Open-Jev densify on §125.

### Added

- **Hourly 2246 HIGH (`notes.md` §134).** Open-Jev TREC densify HEAD
  48346d0630f1 / README SHA unchanged. TREC prep ≠ completed Open-Jev
  TREC / context proof ≠ nDCG / CPU tests ≠ GPU scores / 79 CPU tests
  *theirs* / Open-Jev TREC pending. TypeLLM PyPI densify HEAD
  8a8b4aefd443 / typellm 0.1.1 / PyPI packaging ≠ calibrated Noul /
  Constrained AR ≠ calibrated Noul. simple-jev 408★ first card /
  logits are not calibrated probabilities of correctness /
  wire-compat ≠ logit-equiv. jev-directory catalog ≠ endorsement.
  Jev-Mem 11.0% 6.6× 36.7% *theirs* not Harbor.
  FogMoe/necro abandoned LoRA retrospective.
  Evaluator: TREC prep ≠ completed Open-Jev TREC / context proof ≠
  nDCG / PyPI packaging ≠ calibrated Noul / logits are not calibrated
  probabilities of correctness.
  uniqueness_gate.py now checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 +
  1049 + 1143 + 1248 + 1340 + 1441 + 1542 + 1643 + 1746 + 1843 + 1936 +
  Open-Jev densify + 1946 + 2049 + 2146 + 2246.
  Composition items 553–568 / batch #116.
  **HARD RULE:** do not reopen or amend PR #23–#57. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat a CPU-passing
  TREC prep as completed Open-Jev nDCG, a PyPI wheel as a calibrated Noul,
  next-token logits as P(correct), a 50-eval directory as endorsement,
  or LoCoMo 11.0% as Harbor. With Augustus: TREC prep ≠ completed
  Open-Jev TREC; context proof ≠ nDCG; CPU tests ≠ GPU scores; PyPI
  packaging ≠ calibrated Noul; Constrained AR ≠ calibrated Noul;
  logits are not calibrated probabilities of correctness;
  wire-compat ≠ logit-equiv; catalog ≠ endorsement; *theirs* not Harbor.
  Same split for any Choice/Score/Noul-style head, not only hosted Jev.


Hourly 2146 HIGH (`research/notes.md` §133 / composition items
537–552 / findings batch #115). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#56.
Do not amend released 0.5.0 (#42). Merged #56 owns §132. Merged #55
owns §131. Merged #54 owns §130. Merged #53 owns Open-Jev densify on §125.

### Added

- **Hourly 2146 HIGH (`notes.md` §133).** Open-Jev provider quality
  densify HEAD a00559ea0ab2 / README SHA unchanged.
  provider pipeline ≠ completed Open-Jev quality / CPU tests ≠ GPU
  scores / 65/76 72/76 66/76 60/76 71/76 *theirs* / Open-Jev TREC
  pending. cartpole Kev flip HEAD 922cc61490a0 / fine-tuned Kev ≠
  TypeSafe Jev / one record of 64 / 81.25% 52/64 *theirs*. ashare
  rewrite HEAD 26c7e95e6828 / QMT mock/dry default no orders / AUC
  0.532 *theirs* / does not execute. kevin Playwright + Onyx first
  card / 3.69ms *theirs* not Harbor. metask-jev-4b 79.6% / 80.1%
  *theirs*. cutoff 95% still soft.
  Evaluator: provider pipeline ≠ completed Open-Jev quality / CPU
  tests ≠ GPU scores / fine-tuned Kev ≠ TypeSafe Jev / one record of
  64 / QMT mock/dry default no orders / cutoff 95% still soft.
  uniqueness_gate.py now checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 +
  1049 + 1143 + 1248 + 1340 + 1441 + 1542 + 1643 + 1746 + 1843 + 1936 +
  Open-Jev densify + 1946 + 2049 + 2146.
  Composition items 537–552 / batch #115.
  **HARD RULE:** do not reopen or amend PR #23–#56. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat a
  CPU-passing provider eval as GPU scores, CartPole as hosted Jev, a
  QMT sidecar as live orders, 3.69ms as Harbor, 80.1% as gold, or 95%
  as a hard gate. With Augustus: provider pipeline ≠ completed Open-Jev
  quality; CPU tests ≠ GPU scores; fine-tuned Kev ≠ TypeSafe Jev; one
  record of 64; softmax ≠ calibrated Noul; QMT mock/dry default no
  orders; does not execute; cutoff 95% still soft; option order can
  change an answer; catalog ≠ endorsement; *theirs* not Harbor. Same
  split for any Choice/Score/Noul-style head, not only hosted Jev.

Hourly 2049 HIGH (`research/notes.md` §132 / composition items
521–536 / findings batch #114). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#55.
Do not amend released 0.5.0 (#42). Merged #55 owns §131. Merged #54
owns §130. Merged #53 owns Open-Jev densify on §125.

### Added

- **Hourly 2049 HIGH (`notes.md` §132).** kev night-2 densify HEAD
  c096660c8da2 / PLAN SHA 8d77dd271c66 / README SHA unchanged.
  KEV_TEMPERATURE T≈2.0 / Brier 0.291→0.267 ECE 0.105→0.039 *theirs* /
  grouped T rejected / Qwen3.6-35B-A3B smoke 0.812 *theirs* /
  Hub --revision night2-du / MMLU-Pro 1000 Kev-9B 0.511 Jev 0.829
  *theirs*. kotoba OpenJev runtime densify HEAD ff7f84e74d04 /
  generated_text: False / trained runtime ≠ TypeSafe.
  Evaluator: temperature scaling ≠ ECE unless measured /
  Hub --revision is a pin not a replica / grouped T rejected /
  trained runtime ≠ TypeSafe / generated_text: False / Qwen3.6 ≠ Archer.
  uniqueness_gate.py now checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 +
  1049 + 1143 + 1248 + 1340 + 1441 + 1542 + 1643 + 1746 + 1843 + 1936 +
  Open-Jev densify + 1946 + 2049.
  Composition items 521–536 / batch #114.
  **HARD RULE:** do not reopen or amend PR #23–#55. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat T≈2.0 as
  Harbor ECE, a Hub `--revision` pin as hosted Jev, or a trained OpenJev
  runtime as TypeSafe. With Augustus: temperature scaling ≠ ECE unless
  measured; Hub --revision is a pin not a replica; grouped T rejected;
  trained runtime ≠ TypeSafe; generated_text: False; Qwen3.6 ≠ Archer.
  Same split for any Choice/Score/Noul-style head, not only hosted Jev.

Hourly 1946 HIGH (`research/notes.md` §131 / composition items
505–520 / findings batch #113). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#52.
Do not amend released 0.5.0 (#42). Merged #53 owns Open-Jev densify on §125. Merged #54 owns §130. Merged #52 owns §129.

### Added

- **Hourly 1946 HIGH (`notes.md` §131).** X-sentiment does not execute /
  heyjunpenn 485 catalog ≠ endorsement / jev-arena 62.69% vs 67.26%
  *theirs* not gold / one seed-0 robot trial *theirs* /
  10.59× systems ≠ ECE / Spanish −6.4 pp XNLI *theirs* /
  llm-to-jev description rewrite SHA unchanged.
  Evaluator: does not execute / AI-reviewed ≠ gold / one-trial ≠ Harbor /
  10.59× ≠ ECE / agreement ≠ accuracy / desc rewrite ≠ SHA.
  uniqueness_gate.py now checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 +
  1049 + 1143 + 1248 + 1340 + 1441 + 1542 + 1643 + 1746 + 1843 + 1936 + Open-Jev densify + 1946.
  Composition items 505–520 / batch #113.
  **HARD RULE:** do not reopen or amend PR #23–#52. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat a dashboard
  Choice as a fill, a catalog as a grant, AI-reviewed labels as gold, a
  one-trial robot run as Harbor, 10.59× as ECE, or a description rewrite
  as a SHA change. With Augustus: does not execute; catalog ≠ endorsement;
  AI-reviewed labels ≠ gold; one-trial robot ≠ Harbor; 10.59× systems ≠
  ECE; desc rewrite ≠ SHA/behavior change. Same split for any
  Choice/Score/Noul-style head, not only hosted Jev.

Open-Jev densify (`research/notes.md` §125). Does **not** bump the
0.5.0 pin. Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#52.
Do not amend released 0.5.0 (#42). Merged #52 owns §129.

### Added

- **Open-Jev densify (`notes.md` §125).** HEAD 4933ee84951f /
  README SHA ce1a587219e4 / Astra TREC commit 1dd56990be7e.
  LoRA + scalar head + calibration temperature. not merged base
  models. customer-service P50 85.03 vs Jev 295.26 *theirs*.
  1024/32 slower 1015.90 vs 301.37 *theirs*. systems latency ≠
  semantic equivalence. Open-Jev TREC pending. hard acc ≠
  calibrated Noul. type-valid ≠ exact. LoRA ≠ RLCD replica.
  Evaluator: systems latency ≠ semantic equivalence / hard acc ≠
  Noul / LoRA pack ≠ merged base / prefix cache off / TREC pending.
  uniqueness_gate.py now checks 0843 + 0915 + jcr + 0922 + 0940 +
  0947 + 1049 + 1143 + 1248 + 1340 + 1441 + 1542 + 1643 + 1746 +
  1843 + Open-Jev densify. Densify original section. Do not mint
  a sibling first sighting.
  **HARD RULE:** do not reopen or amend PR #23–#52. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat 85 ms as
  parity, 94.71% as a Noul, or a LoRA pack as a merged RLCD replica.
  With Augustus: systems latency ≠ semantic equivalence; hard acc ≠
  calibrated Noul; LoRA ≠ RLCD replica; not merged base models;
  Open-Jev TREC pending. Same split for any Choice/Score/Noul-style
  head, not only hosted Jev.
User-provided 1936 HIGH (`research/notes.md` §130 / composition items
497–504 / findings batch #112). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#52.
Do not amend released 0.5.0 (#42). Merged #52 owns §129. Merged #51 owns §128.

### Added

- **User-provided 1936 HIGH (`notes.md` §130).** sgoedecke/system-one
  first-sighting / SystemOne.from_pretrained /
  TypeSafe-compatible ≠ TypeSafe replica /
  mithalouni/system-one-open first-sighting / 76.7% vs Jev 86.9% *theirs* /
  replica ≠ TypeSafe / kotoba-lang/typed-decisions first-sighting /
  DeBERTa-v3-large 0.855 / 42 ms *theirs* /
  kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions /
  aisearchio 15-link census catalog ≠ endorsement.
  Soft scores ≠ hard gates. SHA move is not a replica.
  Evaluator: TypeSafe-compatible ≠ TypeSafe replica / replica ≠ TypeSafe /
  kotoba ≠ laya-typed-decisions / census ≠ endorsement.
  uniqueness_gate.py now checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 +
  1049 + 1143 + 1248 + 1340 + 1441 + 1542 + 1643 + 1746 + 1843 + 1936.
  Composition items 497–504 / batch #112.
  **HARD RULE:** do not reopen or amend PR #23–#52. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat
  TypeSafe-compatible as a replica, 76.7% as Harbor, 0.855 as a hard
  gate, kotoba as Laya HF, or a 15-link list as an endorsement. With
  Augustus: TypeSafe-compatible ≠ TypeSafe replica; replica ≠ TypeSafe;
  catalog ≠ endorsement; *theirs* not Harbor. Same split for any
  Choice/Score/Noul-style head, not only hosted Jev.

Hourly 1843 HIGH (`research/notes.md` §129 / composition items
481–496 / findings batch #111). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#51. 
Do not amend released 0.5.0 (#42). Merged #51 owns §128. Merged #50 owns §127.

### Added

- **Hourly 1843 HIGH (`notes.md` §129).** kev own-data JSONL densify /
  --init_from warm-start LoRA/head PR #9 / Kev-0.8B 4B 9B Qwen3.5 family /
  from-scratch ≠ warm-start / JSONL labels ≠ Harbor /
  reconstruction ≠ replica / assay-001 split verdict /
  catalogs as indexes. 4B new-source 0.794/0.832 *theirs*.
  9B new-source 0.812/0.837 *theirs*. 0.33 vs 0.84 vs 0.83/0.88 *theirs*.
  wire-compat is not logit-equiv. SHA move is not a replica.
  Evaluator: from-scratch ≠ warm-start / JSONL labels ≠ Harbor /
  reconstruction ≠ replica. uniqueness_gate.py now
  checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 + 1049 + 1143 +
  1248 + 1340 + 1441 + 1542 + 1643 + 1746 + 1843. Composition items 481–496 /
  batch #111.
  **HARD RULE:** do not reopen or amend PR #23–#51. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat a from-scratch
  fine-tune as equal to a warm start, a JSONL file as Harbor, a random-
  weight reconstruction as a replica, or a catalog as a grant. With
  Augustus: from-scratch ≠ warm-start; JSONL labels ≠ Harbor;
  reconstruction ≠ replica; catalog ≠ endorsement. Same split for any
  Choice/Score/Noul-style head, not only hosted Jev.

Hourly 1746 HIGH (`research/notes.md` §128 / composition items
465–480 / findings batch #110). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#50. Do not amend released 0.5.0
(#42). Merged #50 owns §127. Merged #49 owns §126.

### Added

- **Hourly 1746 HIGH (`notes.md` §128).** TypeLLM truncated thinking densify /
  qwen35_small 0.8B thinking On 0/18 *theirs* / forced closure 20/20 type-valid
  *theirs* / Constrained AR ≠ calibrated Noul / Kev-0.8B completes family /
  4B 0.794/0.832 *theirs* / 9B 0.812/0.837 *theirs* / transfer-v9 5%/9%/26%
  *theirs* / Canny facts-block / Jev never blocks / five-lines 0.80 still soft /
  kev-ane 155/155 argmax *theirs*. Qwen3.5 ≠ Archer. SHA move is not a replica.
  Evaluator: truncated thinking ≠ Noul / type-valid ≠ exact / facts block /
  Jev never blocks / ANE argmax ≠ logit-equiv / 0.80 still soft.
  uniqueness_gate.py now checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 +
  1049 + 1143 + 1248 + 1340 + 1441 + 1542 + 1643 + 1746. Composition items
  465–480 / batch #110.
  **HARD RULE:** do not reopen or amend PR #23–#50. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat truncated thinking
  as a Noul, 0.8B 0/18 as Harbor, 0.812 as a replica, a done-claim Noul as a
  block, or 155/155 argmax as logit-equiv. With Augustus: Constrained AR ≠
  calibrated Noul; type-valid ≠ exact; Facts go to code. Judgments go to Jev.
  Only facts can block; Jev never blocks; serving substrate ≠ calibrated
  replica. Same split for any Choice/Score/Noul-style head, not only hosted Jev.




Hourly 1643 HIGH (`research/notes.md` §127 / composition items
449–464 / findings batch #109). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#49. Do not amend released 0.5.0
(#42). Merged #49 owns §126. Merged #48 owns §125.

### Added

- **Hourly 1643 HIGH (`notes.md` §127).** openjev release 0.3.0 densify /
  re-pin vLLM PR #57250 restructured head / MODEL_VERSION stays openjev-0.1 /
  uv.lock hygiene / clean-code-review typed judgments / JMP route vs generate /
  jevbus thresholds are policy / JevCanvas json-render boundary /
  jevtrafficsim game success ≠ Noul. restructured vLLM head ≠ logit-equiv.
  dual serving is not generate. Hosted Codiv ≠ TypeSafe.
  documentation is read not judged. Thresholds are policy not model.
  wire-compat is not logit-equiv. SHA move is not a replica.
  Evaluator: restructured vLLM head ≠ logit-equiv / thresholds are policy /
  documentation is read not judged / json-render boundary / empty repo
  ≠ serving substrate. uniqueness_gate.py now
  checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 + 1049 + 1143 +
  1248 + 1340 + 1441 + 1542 + 1643. Composition items 449–464 / batch #109.
  **HARD RULE:** do not reopen or amend PR #23–#49. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat a serving pin
  as logit-equiv, JMP as one model, jevbus thresholds as the judge, Luna
  prose as the judgment, diffusion as structure, or a traffic win rate as
  ECE. With Augustus: restructured vLLM head ≠ logit-equiv; dual serving
  is not generate; Thresholds are policy not model; documentation is
  read not judged; json-render is the only renderer; game success ≠
  calibrated Noul. Same split for any Choice/Score/Noul-style head, not
  only hosted Jev.



Hourly 1542 HIGH (`research/notes.md` §126 / composition items
433–448 / findings batch #108). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#48. Do not amend released 0.5.0
(#42). Merged #48 owns §125. Merged #47 owns §124.

### Added

- **Hourly 1542 HIGH (`notes.md` §126).** TypeLLM README densify 3k→12k B /
  Batch 5.8x *theirs* / Constrained AR ≠ calibrated Noul / kev family
  new-source *theirs* / fail-closed routing / fail-open test selection /
  classifier ≠ authorizer / estimates not Harbor. JEV_THRESHOLD 0.65
  still soft. threshold 0.90 still soft. ask_below 0.7 still soft.
  8.2% ≥0.9 on wrong *theirs*. 76/81 vs 77/81 *theirs*. wire-compat is not
  logit-equiv. SHA move is not a replica.
  Evaluator: Constrained AR ≠ Noul / fail-closed never auto-allows /
  fail-open uncertainty means RUN / routing threshold still soft /
  classifier ≠ authorizer / estimates not Harbor. uniqueness_gate.py now
  checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 + 1049 + 1143 +
  1248 + 1340 + 1441 + 1542. Composition items 433–448 / batch #108.
  **HARD RULE:** do not reopen or amend PR #23–#48. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat constrained
  AR as a Noul, 5.8x as Harbor, 0.65 as a hard gate, fail-open RUN as
  fail-closed, estimates as Harbor, or a catalog as endorsement. With
  Augustus: Constrained AR ≠ calibrated Noul; Batch 5.8x *theirs*;
  JEV_THRESHOLD 0.65 still soft; fail-open uncertainty means RUN;
  classifier ≠ authorizer; estimates not Harbor. Same split for any
  Choice/Score/Noul-style head, not only hosted Jev.


Hourly 1441 HIGH (`research/notes.md` §125 / composition items
417–432 / findings batch #107). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#47. Do not amend released 0.5.0
(#42). Merged #47 owns §124. Merged #46 owns §123.

### Added

- **Hourly 1441 HIGH (`notes.md` §125).** vLLM NVIDIA + MLX Apple
  Silicon / Codiv hosted free endpoint / dual serving densify /
  jev-visual *theirs* / jev-mcp advisory / litjev uncalibrated /
  Open-Jev LoRA / jeq pipe / laya-coreai serving substrate.
  dual serving is not generate. Hosted Codiv ≠ TypeSafe.
  candidate probabilities are relative not correctness.
  recommendation is advisory. LoRA ≠ RLCD replica.
  pass-min 0.8 still soft. 37.30s → 2.40s at 64 decisions *theirs*.
  2B 94.71% 9B 97.54% hard test *theirs*. wire-compat is not
  logit-equiv. SHA move is not a replica.
  Evaluator: dual serving is not generate / Hosted Codiv ≠ TypeSafe /
  candidate probabilities relative / MCP advisory / LoRA ≠ RLCD /
  pass-min 0.8 still soft. uniqueness_gate.py now
  checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 + 1049 + 1143 +
  1248 + 1340 + 1441. Composition items 417–432 / batch #107.
  **HARD RULE:** do not reopen or amend PR #23–#47. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat a hosted
  Codiv URL as TypeSafe, `/v1/chat/completions` as decide, 37.30s →
  2.40s as Harbor, a LoRA adapter as an RLCD replica, or pass-min 0.8
  as a hard gate. With Augustus: dual serving is not generate; Hosted
  Codiv ≠ TypeSafe; candidate probabilities are relative not
  correctness; recommendation is advisory; LoRA ≠ RLCD replica;
  pass-min 0.8 still soft. Same split for any Choice/Score/Noul-style
  head, not only hosted Jev.


Hourly 1340 HIGH (`research/notes.md` §124 / composition items
401–416 / findings batch #106). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#46. Do not amend released 0.5.0
(#42). Merged #46 owns §123. Merged #45 owns §122.

### Added

- **Hourly 1340 HIGH (`notes.md` §124).** typesafe-sdk 0.7 Pydantic
  response models / msgspec dropped / MLX 400 error contract /
  PLAN_Qwen35 densify / GLiNER locate class members / Jev-Vision
  *theirs* / 0.971 F1 *theirs*. Pydantic response models ≠
  logit-equiv. msgspec dropped is not a replica. Error contract is
  not a Noul. Locate ≠ decide. coverage-at-error-budget *theirs*
  not Harbor. ~160 ms *theirs* not Harbor. 0.971 F1 *theirs* not
  Harbor. wire-compat is not logit-equiv. SHA move is not a replica.
  Evaluator: pydantic 0.7 ≠ logit-equiv / MLX 400 same contract as
  vLLM / coverage-at-error-budget *theirs*. uniqueness_gate.py now
  checks 0843 + 0915 + jcr + 0922 + 0940 + 0947 + 1049 + 1143 +
  1248 + 1340. Composition items 401–416 / batch #106.
  **HARD RULE:** do not reopen or amend PR #23–#46. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat a Pydantic
  0.7 client model as logit-equiv, a 400 SchemaError as a Noul, 0.971
  F1 as Harbor, or PLAN_Qwen35 as a shipped port. With Augustus:
  Pydantic response models ≠ logit-equiv; error contract is not a
  Noul; GLiNER locate ports are class members; third-party benches
  stay *theirs*; PLAN_Qwen35 is still a proposal for review. Same
  split for any Choice/Score/Noul-style head, not only hosted Jev.


Hourly 1248 HIGH (`research/notes.md` §123 / composition items
385–400 / findings batch #105). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#45. Do not amend released 0.5.0
(#42). Merged #45 owns §122. Merged #44 owns §121.

### Added

- **Hourly 1248 HIGH (`notes.md` §123).** decide is not generate /
  GLiNER-GLiClass class members / third-party benches *theirs* /
  openjev 0.2.1 densify / von Option-Marker densify / verdict Heaven
  74.9 densify / kev tarballs + PLAN_Qwen35 / jeff JevBench / TypeLLM
  thinking. decide is not generate. GLiNER/GLiClass ports are class
  members not Jev replicas. 93.5% *theirs* not Harbor. 74.9 *theirs*
  not Harbor. 8.7x *theirs* not Harbor. wire-compat is not logit-equiv.
  SHA move is not a replica. Evaluator: 400 error-contract /
  theirs-not-harbor / decide-is-not-generate / DeltaNet isolation /
  thinking mode is constrained AR. uniqueness_gate.py now checks
  0843 + 0915 + jcr + 0922 + 0940 + 0947 + 1049 + 1143 + 1248.
  Composition items 385–400 / batch #105.
  **HARD RULE:** do not reopen or amend PR #23–#45. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat tryDecide
  as a chat completion, a Swift GLiNER port as Jev, 93.5% as Harbor,
  or Docker 0.2.1 as logit-equiv. With Augustus: decide is not
  generate; ports are class members; third-party benches stay
  *theirs*; wire-compat is not logit-equiv. Same split for any
  Choice/Score/Noul-style head, not only hosted Jev.


Revisit / since-last-look protocol (`research/notes.md` §122).
Does **not** bump the 0.5.0 pin. Catalogued repos get a densify
card when fingerprints move. Star-noise is not a fold. Treat
revisit HIGH like novel HIGH. uniqueness_gate.py checks the
protocol substring in the skill and research files (not a
21-overlay dump). Do not reopen or amend PR #23–#44. Merged #44
owns §121.

### Added

- **Revisit / since-last-look protocol (`notes.md` §122).** Store
  fingerprints `default_sha`, `pushed_at`, `description_hash`,
  `release_tag` so hourly can diff. Material change is README /
  API / release / calibration claim / serving port / bench
  rewrite. Star-noise is stars / likes / forks alone. Densify
  the prior notes section; do not mint a sibling first
  sighting; do not invent equivalence; SHA move is not a
  replica. Treat revisit HIGH like novel HIGH for Augustus.
  Helper: `research/revisit_fingerprints.py`. Checklist:
  `research/revisit-checklist.md`. **HARD RULE:** do not reopen
  or amend PR #23–#44. Does **not** bump 0.5.0.

Hourly 1143 HIGH (`research/notes.md` §121 / composition items
369–384 / findings batch #104). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#43. Do not amend released 0.5.0
(#42). Merged #43 owns §120.

### Added

- **Hourly 1143 HIGH (`notes.md` §121).** open recreation / semantic
  lint sensor / third-party benches *theirs* / Laya serving densify /
  catalogs. open recreation ≠ calibrated replica. semantic lint is a
  sensor not a proof. cutoff 0.8 still soft. paired bootstrap CIs
  *theirs*. Same accuracy, 35x faster *theirs*. systems comparison ≠
  semantic equivalence. permission ≠ confidence. catalog ≠ endorsement.
  Evaluator: paired-CI / same-accuracy speedup / lint-cutoff still
  soft. uniqueness_gate.py now checks 0843 + 0915 + jcr + 0922 + 0940
  + 0947 + 1049 + 1143. Composition items 369–384 / batch #104.
  **HARD RULE:** do not reopen or amend PR #23–#43. Does **not** bump
  0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: treat a Qwen3.5-4B
  recreation as TypeSafe Jev, fire a 0.8 lint cutoff as a proof, or
  quote 35x as semantic equivalence. With Augustus: open recreation ≠
  calibrated replica; semantic lint is a sensor not a proof; paired
  bootstrap CIs stay *theirs*; serving substrate ≠ calibrated replica.
  Same split for any Choice/Score/Noul-style head, not only hosted Jev.

Hourly 1049 HIGH (`research/notes.md` §120 / composition items
353–368 / findings batch #103). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#42. Do not amend released 0.5.0
(#42). Merged #41 owns §119.

### Added

- **Hourly 1049 HIGH (`notes.md` §120).** ggmlc GGUF serving /
  option-order / exact-p Minesweeper / adapters / catalogs.
  ggmlc GGUF is not llama.cpp. Serving substrate is not a
  calibrated replica. Qwen3.5-9B ≠ Archer. planner writes
  JEV selects. pick_by_id vs pick_second. Soft scores ≠ hard
  gates. catalog ≠ endorsement. Evaluator: option-order
  trap. uniqueness_gate.py now checks 0843 + 0915 + jcr +
  0922 + 0940 + 0947 + 1049. Composition items 353–368 /
  batch #103. **HARD RULE:** do not reopen or amend PR
  #23–#42. Does **not** bump 0.5.0.

- **Recipe (class, not Jev-only).** Without Augustus: load a
  GGUF or ONNX graph and treat the new bottle as a replica,
  or pick whatever sits second in a shuffled menu. With
  Augustus: serving substrate ≠ calibrated replica; measure
  option-order with pick_by_id vs pick_second; keep exact-p
  oracles in code; adapters stay class members. Same split
  for any Choice/Score/Noul-style head, not only hosted Jev.

Hourly 0947 HIGH (`research/notes.md` §119 / composition items
337–352 / findings batch #102). Does **not** bump the 0.5.0 pin.
Uniqueness dumps live in
[`research/changelog-hourly.md`](research/changelog-hourly.md).
Do not reopen or amend PR #23–#40. Do not amend released 0.5.0
(#42).

### Added

- **Hourly 0947 HIGH (`notes.md` §119).** jev-as-judge /
  OneForward readout / catalogs / replay / RLCD heads.
  Fast and cheap agent evals. jev as judge. 18,041 skills
  from the 200 most-starred repos. Not a security scanner.
  semantic_compatibility: false. candidate_mass. softmax
  over A–H ≠ Noul. Qwen3.5-2B ≠ Archer. Qwen3.5-4B ≠
  Archer. Status: no model yet. Exit 1 is not a proof.
  75% cheaper and 18% faster withdrawn. Brier 0.342 →
  0.378; more accurate and more overconfident. catalog ≠
  endorsement. judge ≠ actuator. Evaluator:
  candidate_mass renormalization trap. uniqueness_gate.py
  now checks 0843 + 0915 + jcr + 0922 + 0940 + 0947.
  Composition items 337–352 / batch #102. **HARD RULE:**
  do not reopen or amend PR #23–#40. Does **not** bump 0.5.0.

## [0.5.0] - 2026-09-20

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12). Live HEAD of that repo is still this commit,
the only tagged official-skill revision.

Nine commits on `main` after the v0.4.0 tag (merged #33 README map,
#31 Harbor-jevals, #34 Pages layout, #35 hysteresis/ECE, #36 NanoJev,
#38 jcr, #37 SemIf, #40 llm-to-jev, #39 0843 hygiene). Open #41
(0947 fold) is in flight on another branch and is not part of this
release. Verbose hourly locks stay in
[`research/changelog-hourly.md`](research/changelog-hourly.md).

### Added

- **Pages / onboarding.** Custom site layout (nav, comparison, install,
  pillars). With vs without Augustus on the homepage and README
  (`docs/assets/with-without-augustus.svg`): call-then-act vs
  place-then-judge. Jev is the exemplar, not the monopoly.

- **README.** Scannable skill map (one line per file). The living catalog
  stays in the reference cards and `research/notes.md`, not a README wall.

- **Recipes (class, not Jev-only).** Same with/without split for any
  Choice/Score/Noul-style or typed probabilistic judgment tool. Full
  cards: [`docs/release-notes-v0.5.0.md`](docs/release-notes-v0.5.0.md).
  Shape, not invented scores:
  - **Encoder (GLiNER / GLiClass):** without — swap locate/categorize for
    a decision head and hard-gate spans. With — species map; remainder
    after extractive spans. Measure span quality separately from ECE.
  - **Open heads (Laya, SemIf, kev, Jeff-1):** without — treat wire-compat
    or argmax agree as a replica. With — softmax over options ≠ calibrated
    Noul; systems timing ≠ semantic equivalence. Measure ECE/Brier on
    held-out, not only speed or top-1.
  - **NanoJev:** without — game wins as calibration. With — specialist
    gameplay S1; local boolean ≠ TypeSafe noul. Measure held-out game
    success separately from ECE.
  - **llm-to-jev:** without — ship converted prompts as equivalent
    behavior. With — heuristic on-ramp; review Score rubric; prose stays
    with the LLM. heuristic conversion ≠ calibrated Noul.
  - **jcr:** without — run what the capability tree found. With — lookup
    returns context and **does not execute**. Routing ≠ permission;
    docs ≠ authority to run.
  - **localjev / prompted JSON:** without — parse generated JSON as a
    Noul. With — schema-valid ≠ picked-right; prompted JSON ≠ structured
    logit read.

- **Class / migration.** llm-to-jev conversion on-ramp (`notes.md` §118).
  SemIf rename + MLX densify (`§117`; formerly OpenJev, independent).
  NanoJev unified-games densify (`§115`). jcr capability resolver
  (`§116`; docs ≠ execute).

- **Measurement honesty.** 0843: hysteresis `{enter, exit}` is policy
  attached to a probability, not a model property; instruct-tuning can
  wreck ECE while accuracy stays flat; equal-width ECE ≠ quantile ECE;
  hop-ECE is permutation-invariant (trajectory soundness theater);
  ranking ≠ calibration. 0743: Harbor-jevals practice (schema-pass ≠
  joint fields; skip-and-call-a-tool); Verdict linear ECE floor ≠
  TypeSafe replica; DecisionOps ACT / REVIEW / FALLBACK (a provider
  failure is **not** a policy outcome). Evaluator reports both ECEs,
  AUC, accuracy@0.5, cost-optimal threshold, hysteresis, and hop-ECE
  invariance.

### Changed

- Marketplace plugin version and SKILL YAML pin: 0.4.0 → 0.5.0.
- Homepage / README / CITATION.cff / SECURITY supported line follow 0.5.0.
- CHANGELOG Unreleased dump folded into this cut. Verbose hourly locks
  remain in `research/changelog-hourly.md`.
- Evaluator hop-ECE self-test covers reverse and even/odd interleave
  (permutation invariance is not reverse-only). uniqueness_gate checks
  Pages strings (`LICENSE` in the #34 layout) and refuses CHANGELOG/README
  dump walls. `docs/ecosystem.md` 0843 blurb cites `notes.md` §114.

### Security

- `SECURITY.md`: supported line is 0.5.x. Report via GitHub Security
  Advisories. No invented Scorecard number.

## [0.4.0] - 2026-09-20

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12). Live HEAD of that repo is still this commit,
the only tagged official-skill revision.

Twenty-eight commits on `main` after the v0.3.0 tag (merged #2–#30,
through Merve §112). Open #31 (0743 fold) is in flight on another
branch and is not part of this release.

### Added

- **Class breadth.** TypeSafe Jev remains the documented exemplar, not
  the monopoly. Folded class peers and cousins: Laya (open head), kev
  family (Archer-arch fidelity; replica honesty), OpenJev `/v1/decide`
  (not a TypeSafe drop-in), TypeAR / constrained-AR, GLiNER species
  (locate vs categorize vs safety-schema vs local multi-head), Decision
  Graph Protocol (frame→assess→commit; app retains permissions/effects),
  encoder zero-shot classifiers.
- **Encoder / ZS lineage (Merve Noyan, `notes.md` §112).** Institutional
  HF voice: BERTForXYZ → DeBERTa → ModernBERT. Many problems solved with
  LLMs could have been solved with zero-shot classifiers. It was a
  skill issue. Prefer DeBERTa and ModernBERT heads. Jev vs GPT-5.6
  bakeoffs are a category error. Softmax / ZS scores still ≠ calibrated
  Noul; soft scores ≠ hard gates. Multimodal image↔text ZS is a
  perception front-end, not a decision model. Quote *theirs*; no
  invented accuracy numbers.
- **Measurement honesty.** Harbor / jevals practice: ranking ≠ calibration;
  Score is a 0..n−1 expectation, not 0–1; Noul has no confidence field;
  ECE ≠ an edge; treating 0.85 / minProbability as a hard Harbor gate is
  theater; soft Noul ≠ hard gate; VERIFY must acquire discriminating
  evidence, never same-pool confidence-only rescoring. Calibration is
  not alpha. Compaction default 0.5 is not safety.
- **Composition / placement.** Decision Graph Protocol envelope;
  meaning-grep (proposition ≠ embedding; AND/OR/NOT after threshold;
  not a gate); gut cost-of-error overlay (thresholds from costs, not
  hard-coded); fail-open vs fail-closed per action; prune ≠ deny;
  hard-gating DGP as safety theater.
- **Pages landing** at https://24601.github.io/Augustus/ (`docs/`) plus
  community-health stubs (`SECURITY.md`, `CONTRIBUTING.md`, brief
  `CODE_OF_CONDUCT.md`), `CITATION.cff`, and
  `.github/workflows/scorecard.yml` so an OpenSSF Scorecard can appear.
  No invented Scorecard number.
- Formal methods pillar unchanged in spirit: a Noul is a SENSOR; never
  launder it as a proof (soundness theater).

### Changed

- Marketplace plugin version and SKILL YAML pin: 0.3.0 → 0.4.0.
- README / Pages SEO: one-liner, homepage, install paths, "not a
  TypeSafe product" clarity, [`rh-guard`](https://github.com/24601/rh-guard)
  companion pointer.
- CHANGELOG restored to Keep a Changelog. The hourly uniqueness dump
  lives in `research/changelog-hourly.md`.

### Security

- `SECURITY.md`: supported line is 0.4.x; report via GitHub Security
  Advisories / private vulnerability reporting. Dependabot security
  updates, secret scanning, and push protection stay enabled.
- `.gitignore` covers common secret filenames.

## [0.3.0] - 2026-09-18

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12).

### Added

- Mixed-architecture card: default placement is judgment-class model +
  generator + code, not stack replacement. Covers cost-sensitive prefilter
  (fail-open vs fail-closed per action), tool/skill routing, AGENTS.md
  preference lint, a placement gallery from the 2026-09-18 X+GH hour, and
  an explicit answer to "Jev is just classification"
- Protocol branch and mapping-index rows for those four placements
- Non-negotiable: classification is not the product; typed judgment is a
  software primitive placed beside generation
- Hourly research archive for this pass (X theme digest + `topic:jev` movers)
  under `research/archive/hourly/2026-09-18T14/`
- Research note on Laya (`convaiinnovations/laya`): open Choice/Score/Noul
  head as a self-hosted *typed judgment provider*; vendor benches labeled
  claims; TypeSafe remains the default path
- Applied-mapping cards: context sieve, exact-text keep/drop, env/harness
  triage, moderation/ranking, skill/tool routing (`applied-mappings.md`)
- FAQ card for "it's just classification", stack replacement, Jev vs open
  head, and Augustus vs neighbor how-to skills
- Judgment-class card: Augustus covers the whole class of fast/cheap
  categorization-classification-scoring models (Jev is exemplar, not
  monopoly). Families: closed decision API, open System-1 heads (Laya),
  GLiNER/GLiClass encoder family (locate vs categorize vs local
  multi-head), listwise/pairwise rankers, vision scorers.
  Species map in `judgment-class.md`; GLiNER is a peer, not a footnote.
  Fork of listwise discriminative vs decision/proper-scoring objectives;
  four vision scoring patterns; seven portents for agent architecture.
  FAQ rows for family choice, GLiNER vs GLiClass vs Jev vs cross-encoder, and
  CLIP/SigLIP gating. No invented APIs.
- Formal-methods card: judgment vs proof ownership (sensor / constraint /
  searchlight); Alloy Analyzer vs Apalache (model finder ≠ SMT BMC ≠
  inductiveness); TLA+/Quint/P/NuSMV/PRISM/Event-B; Dafny/JML/
  Frama-C/SPARK; DST trio (Antithesis hypervisor, Resonate Lean+oracle+
  SDK, PufferLib env+seed / Ocean trainer contracts); harms
  (TOCTOU-of-Noul, soundness theater, AI×FM / Hillel vibing specs);
  crossover metaphors (NATM, snap-fit, Norman gulfs, Leveson STAMP/STPA).
  Curriculum archived at `research/archive/curriculum/FORMAL-METHODS-SYSTEM-ONE.md`;
  named rows folded here. One-screen alias: `formal-semi-formal.md`.
  Non-negotiable: never launder a Noul as a proof.
- One-screen `references/formal-semi-formal.md` (curriculum 1-pager)
- Hypothesis mapping cards (do not promote without an acceptance test):
  VOI / gather; SDT/ROC; Leveson sensor≠constraint; search/control
  outside SWE; spec property pipeline; Alloy instance loop; runtime
  assurance sandwich; DST multiverse triage; durable agent control;
  assignment hybrid; situated density (`mappings.md` §6–§16)
- Input-brittleness and structural-prove ∩ remainder cards
  (`mappings.md` §17–§18): paraphrase pairs → Chow abstain; allowlist /
  text-layer first, judge leftovers (jevgate / doc-router *shapes*
  Empirical; domain-general reading Hypothesis). FAQ: GLiNER vs Jev,
  LLM-as-judge (Langfuse framing), allowlist-then-judge
- GLiGuard as an Empirical encoder peer (`judgment-class.md`,
  `notes.md` §30): one-pass safety-schema classify on GLiNER2, not a
  Jev weight clone; FAQ "is GLiGuard Jev?"; README OR/refusal
  aggregation left as existing policy-in-code. LLM I/O safety is not
  a coding-agent tool gate
- Hourly 10:07 Boise fold (`research/notes.md` §25–§26): GLiNER2.5 local
  peer; openjev-lm 92.9% / 6 vCPU teacher-distill; jevgate; doc-router
  1.74× $; pi-jev-context; jevscope next to jevals; Han Xiao trolley
  (listwise ≠ decide); James Ward dual orchestration; JevLint
- Constrained-AR surface, not a sixth species (`judgment-class.md`):
  TypeAR puts a typed interface on a pretrained generator (next-token
  constraint ≠ proper-scoring head). Archer Hume's open-weight drop
  stays **Watch** (`research/notes.md` §31, §32)
- Hourly ~11:02 Boise fold (`research/notes.md` §33): Archer
  clarifications still Watch (27B dense one-forward-pass, multimodal
  generalization report, AU healthcare residency not anti-TypeSafe,
  prefers "decision models"); when-to-use table (proprietary Jev vs
  Archer vs TypeAR vs encoder DeBERTa vs LoRA distill); HF novel
  (jev-gate-student-b 148k corpus, jp-sns-jev7 ONNX, open-jev-deberta,
  mini-jev-runs 27.9k logits, jev-tree-choice-cap); device/harness
  (jev-mobile MCP, jev-macos-loop, jev-harness, routeKit); HacksonClark
  SREGym-Lite 20/50→24/50: rank tests, do not diagnose
- Hourly ~11:59 Boise fold (`research/notes.md` §42): Archer still
  Watch. Three open paths (encoder / AR constrained decode / trained
  decision-only). Native constrained serving
  ([pcdServer](https://github.com/stephanj/pcdServer), TypeAR-class,
  2–256 enums, Apple+Linux GGUF). Meta-VOI hook
  (typesafe-jev-tools 149-row: Haiku more accurate, Jev confidence
  monotonic). jev-mode latency-class split (token ratio durable;
  accuracy is parity). OpenSmoke env-break vs policy-break +
  pre-mortem. jevql store-as-decision-surface. jot topology B with a
  closed catalog. openevals online full-traffic. hermes north-star
  two-layer finish gate. pi-jev (not pi-jev-context). jev-plays-games
  option-order probe. joxide jump-by-description. laya-typed-decisions
  companion packaging. No wrapper.
- Effect-oriented loops (`notes.md` §28, `mappings.md` §19): Ward's
  ZIO client keeps Jev as the outer Choice and the handler as the
  effect. Not Effect.ts. GLiNER author: GLiNER2 "like jev" is GLiGuard
  schema-conditioned categorize, not a Noul.
- Boundary-audit stop conditions for TOCTOU-of-Noul and vacuous specs;
  FAQ rows for Alloy vs Apalache and PufferLib-as-DST-trio
- Research pointer to [dayhaysoos/jevals](https://github.com/dayhaysoos/jevals):
  local MIT workbench for Jev questions vs labeled Noul/Choice/Score cases
  (compare runs, WebMCP + agent skill). Empirical acceptance-test surface
  for Hypothesis mapping cards; complements `evaluate_decisions.py`. Not a
  jevals how-to (`research/notes.md` §24; one sentence in `validation.md`)
- Mental-models card: Augustus is design judgment across AI, SWE,
  business, knowledge work, and life, not SWE-only. Pillars: expected
  utility / selective classification, calibration and cost-sensitive
  thresholds, VOI, MCDA, search/control substitutions, signal detection,
  Leveson org/safety, NATM/snap-fit/Norman/Kent/Shirky as general
  intuition. Domain gallery labeled Hypothesis except launch-week
  Empirical SWE rows.
- Archer Hume architecture reconstruction (17 Sep 2026 essay, ~10k
  probes of `jev-1.13.0`): direct readout vs generated confidence,
  isolated questions, listwise IIA and order sensitivity, confidence as
  arithmetic on the distribution. Independent envelope probe; does not
  override live TypeSafe docs. Announced open-weight drop is **WATCH**
  (27B dense, AU healthcare residency, prefers "decision models"; still
  no Hub weights). `research/notes.md` §31, §33; `judgment-class.md`
  when-to-use table; FAQ confidence / surfaces questions.
- Entropy as allocator (**Hypothesis**, `judgment-class.md`): Atallah's
  low / medium / high buckets place System One on typed decisions and a
  frontier decoder on high-entropy synthesis, same axis as marginals
  vs joint and as VOI. "Review this PR" as medium is still partly
  generative; "first model ever" is a claim. `research/notes.md` §38
- Marginals, not a probabilistic program (`judgment-class.md`, FAQ):
  Erik Meijer: Jev is a cool API and not a PPL; Kleisli qualifications
  exaggerate; "Jev gives you the marginals; a decoder gives you the
  joint." Joints and invariants stay with TLA+ / Alloy / contracts.
  `research/notes.md` §34
- Bespoke Nimble: open contrastive recipe, not a Jev distill. Model
  card Apache-2.0 LoRA on Qwen3.5-9B (repo license absent). Their
  324-example holdout is a named receipt (Nimble 90.12%, Jev 1.13.0
  93.21%), not a ranking. 9B-vs-Jev on your labels stays Hypothesis.
  `research/notes.md` §35; one sentence in `validation.md`
- djev-spark: third compute graph (diffusion structured reads,
  Jev-shaped I/O, image-in). Empirical as the public interface;
  Hypothesis that it beats a decision head on your task. Archer's
  multimodal drop stays WATCH. `research/notes.md` §36
- Perception specialist then judgment specialist vs shared multimodal
  System One (**Hypothesis**): SAM 3.1 (masks and tracks) or an ASR
  transcript, then typed decisions on that state, is an application
  pattern, not native omni. Information dies at the interface. Prefer
  a shared multimodal decision model when the joint matters (Archer
  Watch, not Empirical; djev-spark images; future audio). Basit ask,
  primary post not retrieved. `research/notes.md` §39
- Perception→decision pipeline, measure, and hill-climb
  (**Hypothesis**, `validation.md`): stages with a versioned state
  contract; stage metrics plus a frozen taskset; HoH changes one stage
  or one interface. DSPy/Ax only on LM-program knobs; jevals and
  calibration for the decision slice; Harbor names product
  end-to-end, not a tutorial. `research/notes.md` §41
- Eval & hill-climb (`validation.md`): jevals decision-stage hygiene
  (independent keys, correctness is not confidence, held-out, immutable
  runs) and Harbor as the product taskset substrate; one composition
  table. `research/notes.md` §40

### Changed

- Skill description rewritten as trigger conditions (mixed architecture,
  prefilter, routing, preference lint, classification skepticism, family
  choice including GLiNER/GLiClass/listwise/vision) plus an explicit `not_for`
  against the official `typesafe-ai` skill
- Identity lock vs neighbor skills (`typesafe-ai`, `tenbin`, `decision-first`)
  so Augustus stays the design-judgment layer, class-wide, not TypeSafe-only
- Design cards name hole, family, and typed judgment provider (Jev default;
  other family only with self-eval)
- Protocol fan-out step is family-aware (Jev batch, GLiClass one-pass,
  dual-encoder prompt scoring); ranking vs decision fail policy is a
  non-negotiable
- Protocol and FAQ branch for "formally verify with Jev"; methods-catalog
  and composition-algebra verifier position point at the ownership split
- Skill mission and description are domain-general (AI / SWE / business /
  knowledge work / life); FAQ "is this only for software?"; mappings.md
  beyond-SWE examples labeled Hypothesis; boundary-audit red flags for
  TOCTOU-of-Noul and vacuous specs; formal-methods expanded with Alloy vs
  Apalache and the DST trio including PufferLib; GLiNER promoted from
  cousin footnote to species-map peer

### Fixed

Adversarial review of the whole skill against its own non-negotiables
(findings in `research/notes.md` §27).

- Gate fail policy is per action, not universally open
  (`composition-algebra.md` position 3, `agent-self-assessment.md`):
  advisory guards fail open *because* an interlock sits underneath;
  selection and authorization gates fail closed
- Dual-orchestration topology A selects from a closed catalog instead of
  "planning" MCP calls, which contradicted the standing planner rejection
- Species map applied to the skill's own advice: GLiClass (categorize) is
  the large-catalog substitute for a 255-option Choice; GLiNER spans are
  not (`SKILL.md`, `judgment-class.md`, `applied-mappings.md`)
- Han Xiao trolley relabeled an Empirical **rejection** (one tweet, no
  repo), not a recipe
- openjev-lm caveat moved to the figure it belongs to: 92.9% is against 70
  hand-labelled gold, 98.1% is teacher *agreement*
- Contract surface removed from design cards: the Ax constructor call and
  the `instructions` key enumeration point at live docs instead
  (`optimizer-integration.md`, `question-design.md`)
- `mappings.md` preamble no longer claims uniform Hypothesis where card
  bodies say Contract/Empirical; §17 forbids reusing jevgate's ≤0.18 as a
  constant; all Hypothesis-range references aligned to §6–§19
- Ownership split labeled Contract in `toolbox-mapping.md`, matching
  `mappings.md` §8; done-check splits structure from the Noul

Second pass on `7b3a0c3` (`research/notes.md` §43). Zero blockers.
Dropped the unpublished `npx jevals` line; SAM and ASR are upstream
producers, not the perceive species; removed two call shapes from
`optimizer-integration.md`; tagged the $0.042/MTok cell as a vendor
figure; marked GodsBoy 94.4% exploratory.
- Skill description gained trigger terms for boundary audit, question
  diagnosis, agent self-supervision, and optimizer placement

## [0.2.0] - 2026-09-18

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12).

### Added

- Boundary-audit card for existing systems: three-way split (exact /
  bounded judgment / generation), code-smell catalog, fit test, opportunity
  map, smallest-viable-boundary rule, Jev-around-LLM sandwich, centralized
  policy + raw-judgment retention, red flags, completion questions
- Protocol branch: audit a codebase/PR before inventing mappings; per-action
  risk gates; keep questions/thresholds in one reviewable module
- Skill description trigger terms for brittle parsers, prompt-to-JSON
  classifiers, and agent loops that are really bounded decisions

## [0.1.0] - 2026-09-18

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12), the only tagged revision of the official skill at
Augustus launch.

### Added

- Skill protocol, decision-design card, and evidence labels (Contract /
  Empirical recipe / Hypothesis)
- Classical-method mappings: features/utility, selective decisions, decision
  circuits, bounded rerank, hierarchy/beam search
- Agent self-assessment, optimizer coupling (Ax, DSPy, ProgramAsWeights)
- Toolbox sweep, named-methods catalog, 11-position composition algebra,
  question-design diagnosis
- Validation gates and `scripts/evaluate_decisions.py`
- Launch-week evidence archive (187 repos) and public ecosystem index
- Claude Code marketplace manifest; public GitHub mirror at
  [`24601/Augustus`](https://github.com/24601/Augustus)

### Research log (pre-tag)

The dated passes below are how 0.1.0 was assembled.

### 2026-09-18 (refresh pass 2)
- Research: Gemini Deep Research report retrieved and archived (interaction ID
  saved in jev-archive/state); GitHub census doubled to ~60 Jev repos +
  framework integrations (LiteLLM, LangChain, Vercel AI, Mastra, Eliza, Ax,
  Composio); all 87 repos cloned to /home/user/workspace/jev-archive for
  hourly refresh.
- New measured recipes added to notes.md: foreman supervision loop, pi-jev
  gate thresholds, pi-warden 6→0 paired-run result, winnow relevance sieve,
  fast-jev-compaction two-noul rule, skill-router gates (0.30/0.40, shortlist
  3, 94.4% vs 70.8%), calibration ECE 0.0313 vs 32% OOD collapse (Archer
  Hume), Every 777-judgment eval, Near Here moderation numbers.
- Skill: added references/agent-self-assessment.md (agent self-supervision
  lifecycle, grounding/citation checks, skill callability testing) and two
  mapping-index rows; validation.md dogfooding section still canonical.

### 2026-09-17/18 (initial)
- Baseline research archive (sources.json, notes.md), augustus skill with
  mappings + validation references, evaluator script, hourly refresh script,
  Claude plugin marketplace manifest.

### 2026-09-18 (topic-index pass 3)
- Fixed census method: exact GitHub search paginated (700 repos created since
  09-14 captured; 700-result cap noted) + topics/jev crawl → ~80 additional
  repos; archive now 184 clones. Miss-cause documented: earlier star-sorted
  limit-40 search cut the low-star tail (incl. both MCTS repos).
- Skill: MCTS mapping promoted experimental → empirical recipe (grounded vs
  speculative fidelity in types; probes-only concession; measured 24/24 vs
  1/24 greedy); agent-self-assessment.md gains the judge-variance recipe
  (Jev judge 224-279x more consistent than LLM judge over 100 reps).

### 2026-09-18 (pass 4 — optimizers + official skills + clone audit)
- ax Jev support documented from source (native adapter details, trueThreshold
  semantics, fail-closed mapping validation); new reference
  optimizer-integration.md covering Ax + DSPy typesafeify + jev-dspy-lab.
- typesafeainate/dspy-typesafeify cloned; official typesafe-ai/skills already
  archived and layered-on (never duplicated).
- Clone audit: repos.txt deduped (185 unique), 0 missing on disk, no failures.

### 2026-09-18 (pass 5 — toolbox sweep meta-method)
- New references/toolbox-mapping.md: the how-to-find-approaches-and-
  applications procedure (judgment-shaped-hole substitution, newly-feasible
  classification via economics inversion, standing rejections list); wired
  into SKILL.md central model + index row.

### 2026-09-18 (pass 6 — named-methods + operators/theorems tier)
- references/methods-catalog.md: ~20 named algorithms (CatBoost row is
  Empirical via autoresearch cookbook) + operators/theorems tier with
  precondition-carrying rule; wired into SKILL.md index and toolbox sweep.

### 2026-09-18 (pass 7 — composition algebra as application generator)
- references/composition-algebra.md: 11-position grammar of Jev-vs-construct
  relations, logical-operator combination rules, and the position×construct
  traversal as the systematic application generator; wired into SKILL.md
  index + toolbox sweep.

