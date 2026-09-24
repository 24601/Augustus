# Review dispositions for Augustus 0.8.0 plan v3

**Confidential and local only.**

**Inputs**

- `reviews/fable-5.1-xhigh-v2.md` (Fable v2). Requested `claude-fable-5-1` at xhigh; observed
  "Fable 5.1"; effort unknown.
- The final `codex` block of `reviews/astra-max-v2.raw.log` (Astra v2, session `01a0cf9f…`).
  Requested `gpt-6-astra` at max. The header is CLI configuration, not proof of the serving model.
- Plan: `plan-v3.md`; section numbers below refer to it.

**Coverage.** All 21 findings are dispositioned: Fable v2 P0-1, P1-1 to P1-4 and P2-1 to P2-8, and
Astra v2 1 to 8. The coordinator's task text listed Astra "1..7"; the review itself numbers eight
findings (1 P0, 5 P1, 2 P2), so number 8 (sibling isolation) is included.

**Disposition values**

- **Accepted:** the correction is adopted as proposed.
- **Modified:** the defect is accepted, but the fix differs.
- **Rejected:** the defect is not accepted.

**Result.** None rejected. Where the reviewers overlap, one fix covers both, and the rows point to
each other. Two reviewer claims are adopted only with the other reviewer's qualification:

- Fable P1-3 said M5 was "unreachable at any n". Astra 2 notes that a genuinely better rung can
  pass.
- Fable P1-4 said extreme-ratio power was impossible. Astra notes it depends on the pilot σ.

**Coordinator facts and maintainer decisions** used below are labeled [Coord] in the plan.

**Arithmetic.** Every reviewer number checked was re-derived with `calc/calc_v3.py` (sha256
`2b8fc816…`; output `calc/calc_v3.out.txt`, sha256 `b04af194…`):

- 224/4,000 passes v2's E4a rule (lower bound 0.0491);
- 228 → 2.472% per cell, and 52.8% over 30 cells;
- Astra's plug-in counterexample: 0.095 vs 0.045;
- E3: v2's 880 is a superiority n at δ = 0.03 and m = 3;
- M5: Hoeffding needs 59,915 rows for a 0.01 radius at K = 1.

**One convention differs from the reviewers.** v3's family rule reads every claim type from a
two-sided (1 − α/m) CI. At m = 6, σ = 0.30 and δ = 0.02, that gives an E3 n of 3,457 at 80% power,
against 3,040 under the reviewers' (1 − 2α/m) TOST interval. The half-width at 1,200 is 0.0228
(0.0207 under their interval). Both exceed the margin, so the finding stands either way.

## Fable v2

| ID | Sev | Finding | Disposition | Where in v3 | Notes |
|---|---|---|---|---|---|
| P0-1 | P0 | Separate-user isolation on the Mac exposes the plan copies in `~/.codex` transcripts and the credentials in `~/.zshrc` and the HF token. The boundary test enumerates paths, and `augcand` has network | **Modified** | Provenance rows "Mac" and "tabputer-1"; §0.1; §4.1–4.6; §5.2; M0; M3 depends on B1–B14 | Item 1 (chmod of the home and dotfiles) was done by the maintainer [Coord]. Rather than rely on it, v3 makes **no isolation claim on the Mac**, because an admin account (uid 501) can sudo-read everything, and it deletes `augpatrol` and `augcand`. All experiments and candidate code move to tabputer-1: unprivileged `augexp` and `augctl`, rootless podman with `--network=none`, and a skuid nftables drop. Item 2 becomes a machine-wide readable-file sweep plus credential-marker grep (B3, B5), run as each principal. Item 3: staging lives under `/srv/aug/stage`, not the maintainer's home; egress is enforced (§4.2). Item 4: M3 and M4 cannot start before B1–B14 pass. Key rotation is left to the maintainer, as Fable framed it; the only other Mac account is an admin that could read those files at any mode |
| P1-1 | P1 | Baseline stale again; 0.7.2 shipped without the `.gitignore` change | Accepted | Provenance "Baseline"; §3.1; decision 13; Sources rows 43 and 47 | Baseline now `d8dc848` / `v0.7.2` → `30b6033` / 173,472 B / 10,743 B [Coord], cross-checked on local refs by this lane and labeled "not fetched". Row P is deleted, since 0.7.2 is done. M1 branches from `origin/main` after `git fetch origin`. The `.gitignore` line (with `.claude/`) moves to the first 0.8.0 commit, with an optional public housekeeping PR. v1 row 2 and v2 row 34 are marked superseded |
| P1-2 | P1 | E3's n uses the wrong margin, family and test; equivalence cannot fire at 1,200 | Accepted | §2.7 E3 (family, margin, n, calls, cap, outcomes) | m = 6, δ = 0.02 and power 0.8, stated once. n = 3,457 at σ = 0.30; plan 1,000 search plus 3,500 confirmation; n_conf = min(6,405, n(σ̂)) at the analysis lock. Unpowered equivalence rows are declared before confirmation. The prespecified narrowing drops the 4B reader (m = 3, n = 3,040). The margin is never changed |
| P1-3 | P1 | The M5 +0.01 margin is unreachable with the offered methods; T1 is fixture evidence and cannot support a margin | **Modified** | §3.3 M5 table; §3.4 last row | The margin is kept at 0.01 (Astra 2: do not weaken it). Instead, M5 gets real-text tasks large enough for it: T2a BANKING77 77-way, T2b CLINC150 and T2c CivilComments (100k, disjoint from E1). EB is the method, with K = 3 and intersection-union across tasks. Computed n: EB 5,025–18,136 for σ 0.10–0.30; Hoeffding about 87k–97k. T1 is `fixture_evidence_only` and informs guard text only. An explicit inconclusive row makes no rung recommendation. Astra's qualification is recorded: a genuinely better rung can pass, but only powered tasks count toward outcomes |
| P1-4 | P1 | E1's relative margin is untestable at extreme ratios; B duplicates the positive control; B-retrain is underspecified; m is misstated | **Modified** | §2.2 arm table; §2.7 E1 (family, margin, planning n, outcome rows, controls) | (a) The relative margin is kept, because 2% of the plug-in's cost is the substantive scale. Reachability comes from the full CivilComments data (about 1.6M confirmation rows): synthetic planning n is 12k–271k [H]. A powered-set rule applies, "Supports" and "Rejects" range over the same powered ratios, and "Supports" needs at least 2 of the 3. Astra's point that the real power depends on σ̂ is adopted. (b) The stale-threshold positive control is removed; B-stale is the experimental comparison, and B-retrain_r is added as the real endogenous alternative. (c) m = 19 per dataset, enumerated. (d) B-retrain_S is fit data importance-reweighted to the new prior plus the same 200 labels |
| P2-1 | P2 | Reviewer CLI details: `--verbose`, nonessential traffic, sampling limits, observed-model source, receipt 0 | Accepted as a deferred prerequisite | §5.2 table | The patrol is dropped [Coord]. Every item is carried into the prerequisites for any future unattended patrol |
| P2-2 | P2 | `augcand` is never created; sibling isolation has no mechanism; candidate network unspecified | **Modified** | §4.2 principals and containers; B6, B10 and B14; M0 | Replaced by `augexp` and `augctl` on tabputer-1, provisioned at M0. Each candidate gets its own container and `/work`, with no shared writable mount, and runs sequentially until B14 passes. Candidate network is `--network=none` plus the skuid drop. The grader runs as `augctl` |
| P2-3 | P2 | Pre-registration needs a second lock point | Accepted | §2.7 common rules; decision 14 | The design lock comes before download. The analysis lock (manifests, σ̂, numeric margins, n, powered set, frozen hashes) comes before any confirmation read, and the `augctl` grader enforces it |
| P2-4 | P2 | The arithmetic artifact sits in an ephemeral scratchpad | Accepted | Provenance "Checks"; Sources 46; `calc/` | `calc_v2.py` (sha256 `5d3a6d23…`) and Fable's appendix script (`e75b6308…`) were copied into `research/080/calc/`. New arithmetic is `calc/calc_v3.py`, with its saved output |
| P2-5 | P2 | The E3 compute cap omits the search set | Accepted | §2.7 E3 "Calls"; §4.5 | 9 calls per question per reader, counting search. 81,000 planned; 133,290 maximum; 36,360 fallback. v2's 1,600 questions were 19,200 calls at its own 6 per question, not 14,400; v3 counts 9. Cap: 24 GPU-hours |
| P2-6 | P2 | `sign_exact` has no UCB | Accepted | §2.4 item 1; §3.5 | Rule: losses in {0, 1}; m = 0; one-sided exact binomial p ≤ α/K on discordant pairs; certifies direction only |
| P2-7 | P2 | Nits: A_tuned; monotonicity; freshness grace; 12px gutter; WANLI label | Accepted | §2.2 table; E1 "Monotonicity"; §5.2; §6.5 grid; §3.4 last row | A_tuned is classed as exogenous, tuned closed-form (descriptive). Monotonicity is defined as at most one switch along the ordered ratios. The freshness grace becomes a deferred-patrol prerequisite. Gutters are 16px. WANLI is labeled "C via reviewer" |
| P2-8 | P2 | `.claude/` untracked, and worktrees | Accepted | Decision 13; §3.1; §4.1 transfers | `.claude/` is added to the ignore rule. Bundles are built from an explicit file list, so `.claude/` content never reaches tabputer-1. The Mac boundary grep Fable proposed is moot, since there is no Mac isolation claim |

## Astra v2

| ID | Sev | Finding | Disposition | Where in v3 | Notes |
|---|---|---|---|---|---|
| 1 | P0 | Protecting `.local/` leaves transcript copies and credentials reachable by the candidate account; `HF_HUB_OFFLINE` is not a network policy | **Modified** (with Fable P0-1) | §4.1–4.6; B2–B11; M0 | Task accounts no longer exist on the Mac. On tabputer-1, the candidate cannot reach the maintainer's home (B3) or other workloads (B4), and a sweep finds no credentials (B5). Inputs are staged separately and read-only, and both identities are tested. Candidate execution has an enforced network policy (`--network=none` plus the skuid drop, B10). `HF_HUB_OFFLINE` is kept only as a cache setting, not counted as a control |
| 2 | P1 | M5 lacks a reachable, coherent decision; T1 fixtures versus eligibility; the 470 figure | Accepted (with Fable P1-3) | §3.3 | T1 is separated as fixture evidence; eligible confirmation is real text (T2a–T2c). Feasibility is recomputed for EB with K = 3 at the 0.01 margin. An explicit inconclusive row makes no rung recommendation. The margin is not weakened |
| 3 | P1 | E1 controls misclassify scientific outcomes as pipeline faults; the comparison table is incomplete; m is wrong | Accepted | §2.7 common rules ("Controls test machinery only"); E1 "Controls", "Outcomes, not controls", "Family" and "Narrows" | Machinery controls are now an identical frozen A (Δ ≡ 0) and semi-synthetic planted analytic effects (equal-cost thresholds, 1.5δ, δ) over 200 redraws. The stale threshold and the independent fit are experimental outcomes. "B-stale superior to A" is a prespecified *implementation* narrowing, using Astra's 0.095 vs 0.045 example. All 19 contrasts are enumerated, including B-stale equivalence and the S equivalences |
| 4 | P1 | E3's n uses a different margin, family and test; the call budget omits search | Accepted (with Fable P1-2 and P2-5) | §2.7 E3 | As in Fable P1-2 and P2-5. When compute binds, the prespecified outcome is the narrowing (drop 4B), then inconclusive equivalence rows |
| 5 | P1 | E4a treats failure to detect miscalibration as qualification; unadjusted any-cell failure | Accepted | §2.7 E4a | The coverage claim (theorems and exact-rational tests) is separated from the Monte Carlo diagnostic. Tolerance α + τ = 0.055 with a simultaneous Bonferroni CP upper bound over C = 108 cells and R = 40,000. The diagnostic's properties are stated: ≤ 4.5% fails with probability 2e-9; exactly 5% fails with 0.128; ≥ 6% is detected with probability ≈ 1. It is described as a gross-defect detector. Positive controls are kept: planted gross defects must fail, and power is reported per cell |
| 6 | P1 | Baseline and ignore-rule vehicle stale; mixed revision counts | Accepted (with Fable P1-1) | Provenance; §3.1; decision 13 | As in Fable P1-1. The released counts (173,472 / 10,743) replace the mixed `333397d` figures. The plan states that no published tag changes |
| 7 | P2 | Patrol evidence cannot establish its URL and connection guarantees | Accepted as a deferred prerequisite | §5.2 | The patrol is dropped [Coord]. Trusted-source binding of fetch IDs, tests with payload-bearing valid IDs, complete connection-event evidence and enforced egress are listed as prerequisites. The same evidence standard is applied now to the setup proxy (connection log plus nft counters, B9–B10) |
| 8 | P2 | A shared candidate UID does not give sibling-run isolation | Accepted (with Fable P2-2) | §4.2 containers; B14; M0 | Per-run containers with their own `/work`, no shared writable mounts, and controller-owned artifacts exposed only through prediction files that the `augctl` grader parses strictly. An actual sibling read is tested (B14). Provisioning is part of M0 |

## Astra's verification table (prior findings marked partial or open)

| Prior finding | Astra v2 status | v3 closure |
|---|---|---|
| F P0-1 / A1 | Open | Fable v2 P0-1 / Astra v2 1 and 7 above |
| F P1-1 | Open (recurred) | Fable v2 P1-1 / Astra v2 6 |
| F P1-4 / A8 | Partial | Fable v2 P1-4 / Astra v2 3 |
| F P1-6 / A10 | Partial | Fable v2 P1-3 / Astra v2 2 |
| F P1-7 / A4 | Partial | Astra v2 5 and 8 |

## Items v3 adds that neither review raised

| Item | Where | Reason |
|---|---|---|
| The family CI rule: two-sided (1 − α/m), with every claim type read from it | §2.7 | Directional and equivalence claims are read from the same interval; this keeps the false-claim rate across the family at α |
| Powered-set rule: unpowered contrasts count toward no outcome in either direction | §2.7; E1; E3; M5 | Keeps the outcome rows symmetric after the analysis lock |
| Margins never widened or narrowed after n is known | §2.7 | Maintainer decision (2) [Coord] |
| E1 confirmation uses the full CivilComments data (about 1.6M rows), not the 97k test split | §2.7 E1 | Makes E1 reachable at a substantive margin without changing it |
| The grader refuses to score without the analysis-lock hash | §2.7; §4.2 | Enforces the lock mechanically |
| Candidate code gets no GPU devices | §4.2; §4.6 | `render` access widens the driver attack surface |
| The Jekyll build runs in a container on tabputer-1 | §6.6; decision 3 | Keeps third-party gems off the Mac |
| Scenario S12 (a 1 pp margin at 3k rows) | §3.7 | Tests that the skill shows n and does not widen the margin |
| New decisions 21–24; decisions 11, 14 and 15 withdrawn | §9 | tabputer-1, memory, the ROCm wheel, Colab; the patrol and GPU spend are resolved |
