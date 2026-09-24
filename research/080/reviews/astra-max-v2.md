# Astra v2 review of plan v2

Extracted from the final `codex` block of the Codex session log. Requested `gpt-6-astra`, `model_reasoning_effort=max`; the Codex header reported the same (CLI configuration, not proof of the serving model).

Requested routing: gpt-6-astra, model_reasoning_effort=max (codex exec)

**NOT ACCEPTED — 1 P0, 5 P1, 2 P2.**

Reviewed [plan-v2.md](research/080/plan-v2.md), SHA-256 prefix `727bb39eb175`, its dispositions, both original reviews, and the existing Fable re-review. All plan line references below refer to that unchanged revision.

Verification used local files, Git records, permission metadata and independent stdlib arithmetic. No files were written, credentials read, network requests made, or isolation workloads executed. “Resolved” below means resolved in the plan’s specification; it does not establish an implemented control.

1. **P0 — Protecting `.local/` leaves confidential copies and credential files reachable by the candidate account.**

   **Quote:** §4.1, L596: “`chmod 700 .local` therefore gates both the patrol and E4c.” §4.4, L665–667: “No sandbox is claimed” and “unreadable to the candidate’s macOS user, `augcand`.”

   **Failure path:** I verified that the maintainer’s home permits `staff` traversal, the relevant `.codex/sessions/` directories are 755, and the `01a0cf8f…` transcript is 644 and contains the exact v2 plan title and patrol section. The Hugging Face token file is also 644 beneath traversable directories; its contents were not inspected.

   After the prescribed `.local/` chmod, the direct-path boundary test can pass while unrestricted candidate code running as a standard `staff` account reads the transcript or token file. `HF_HUB_OFFLINE=1` does not prevent arbitrary code from making network requests. The reviewer’s restricted file tools do not protect the separate candidate execution path.

   **Minimum correction:** Before M3 or M7, deny both task accounts access to the maintainer’s private home, including transcript and credential copies, and stage their permitted inputs separately. Test that boundary under both identities. Give candidate execution an enforced network policy. Protecting only the original plan and grader paths is insufficient.

2. **P1 — M5 still lacks a coherent, reachable acceptance decision.**

   **Quote:** §3.3, L434–438: “one-sided 95% UCB(Δ) < +0.01”; “non-inferior on T1 and T2”; “About 470 paired items per task detect 5 pp.” §2.4, L181–182: “Proxy or fixture evidence cannot support a margin.”

   **Failure path:** The specified T1 route is a generator with fact–text checks labeled fixture evidence; no eligible real T1 confirmation source is identified. Nevertheless, M5 requires T1 to satisfy the margin. Following the eligibility rule prevents that decision; bypassing it manufactures acceptance from fixtures.

   Separately, 470 items for detecting a 5-point superiority effect does not establish feasibility for a 1-point non-inferiority margin. With the helper’s `[0,1]` loss bound and even the optimistic `K=1`, Hoeffding’s radius at 470 is **0.11291**. At zero observed delta, approximately **59,915** items are needed for a radius below 0.01. The alternative bound and its required sample size remain unspecified.

   **Minimum correction:** Separate T1’s fixture result from eligible confirmation, or identify its real confirmation population. Recompute feasibility for the actual method, margin and family. Add an explicit inconclusive outcome that makes no rung recommendation. Do not weaken a workload’s margin merely to obtain a result.

   The earlier Fable re-review overstates this as universally unreachable: a sufficiently large genuine improvement can pass non-inferiority. That does not repair the planned equality-case comparison.

3. **P1 — E1’s controls classify legitimate scientific outcomes as pipeline faults.**

   **Quote:** §2.7, L253: “A positive control that fails to fire marks a pipeline fault.” E1, L267: “a stale threshold of 0.5 … must test worse than A” and “A built from a second, equal-size fit subsample must not test superior or inferior to A.”

   **Failure path:** A is explicitly an estimated plug-in policy, so it need not beat the stale threshold. For example, with estimated probability 0.20, actual positive frequency 0.05, and costs `C_FP=0.1`, `C_FN=0.9`, A predicts positive and incurs expected loss **0.095**; the stale threshold predicts negative and incurs **0.045**. That is meaningful evidence against the implementation, not necessarily a broken pipeline.

   Independently fitted heads are also not a known null: their realized population losses can differ. A powerful, correct test can detect that difference and fail the proposed negative control.

   **Minimum correction:** Use planted, analytically known effects and an identical frozen policy for machinery controls. Keep stale-threshold and independently fitted comparisons as experimental outcomes. Their results must be allowed to reject or narrow the claim.

   Also complete the comparison table before treating E1 as prespecified: L268 requires B-equivalence tests absent from L265, and L269 requires shift-equivalence tests not specified there. State the full family size and recompute planning n. At α=0.05, the advertised approximately 8,100 uses `m=5`, although the C/C*/E equivalence comparisons alone number nine.

4. **P1 — E3’s sample calculation uses a different margin, family and test from its stated experiment.**

   **Quote:** §2.7, L282: “Margin 0.02 utility” and “Primary family m = 6.” L283: “σ = 0.30, δ = 0.03, α/3 gives about 880. Plan … 1,200 confirmation questions.”

   **Failure path:** The 880 calculation is for 80% one-sided superiority power at margin 0.03 and family size three. It does not support the specified equivalence experiment.

   Using E1’s normal planning rule with `σ=0.30`, margin 0.02 and `m=6` gives approximately **3,040 confirmation items for 80% TOST power**, or **3,670 for 90%**. At 1,200, the corresponding planning CI half-width is **0.02073**, already wider than the entire permitted half-margin. Thus the planning assumptions make equivalence-based rejection unavailable while sufficiently large superiority results remain possible.

   The 14,400-call estimate at L286 also omits search: the stated 400 search plus 1,200 confirmation questions require up to **19,200 calls**, before pilots.

   **Minimum correction:** Reconcile margin, family, power and sample allocation, then recompute the complete call budget. If the compute cap prevents the required experiment, prespecify narrower claims or an inconclusive result. The existing underpowered-result rule protects reporting honesty but does not correct this design arithmetic.

5. **P1 — E4a treats failure to detect miscalibration as qualification, while introducing another multiple-testing failure rule.**

   **Quote:** §2.7, L292: “Clopper–Pearson 95% intervals” and “No cell’s lower bound exceeds α.”

   **Failure path:** A lower confidence bound below α does not establish that the false-adoption rate is at most α. For example, **224/4,000 = 5.6%** passes the stated criterion against α=5%.

   Conversely, checking separate unadjusted intervals and failing on *any* cell can reject valid machinery frequently. At a true 5% rate, the specified two-sided interval fails this condition from 228 adoptions upward, with probability approximately **2.472% per cell**. Thirty independent cells operating at that nominal rate would have approximately **52.8%** probability of at least one failure. This is a property of the qualification rule, not an assertion that the proposed conservative methods attain 5% in every cell.

   **Minimum correction:** Separate the mathematical coverage claim from Monte Carlo diagnostics. Prespecify a diagnostic tolerance and simultaneous error budget. If simulations qualify a rate, use simultaneous upper bounds against the declared tolerance; if they only detect gross implementation defects, say so. Preserve the positive controls.

6. **P1 — The baseline and the vehicle for the confidentiality ignore rule are stale again.**

   **Quote:** Provenance L14: “`origin/main` = `7118537`.” §6, L786 lists the 0.7.2 release as a dependency. Decision 16, L843: “Add `.local/` to `.gitignore` in 0.7.2.”

   **Failure path:** Existing local Git records contain:

   - `v0.7.2` → `30b6033`, followed by publication receipt commit `7a94072`;
   - `origin/main` → `7a94072`;
   - no `.local/` entry in that revision’s committed `.gitignore`.

   The operative ignore rule remains `.git/info/exclude:7`. The assigned release vehicle has already passed without the change.

   The provenance table also mixes revisions: `333397d` contains **173,425** reference bytes, whereas released 0.7.2 contains **173,472**. Released `SKILL.md` is **10,743** bytes, not the development branch’s 10,747.

   **Minimum correction:** Record the released dependency accurately, verify the separate rebase step, and assign the ignore change to a concrete unreleased commit. Correct the revision-specific counts. Do not modify the published tag.

7. **P2 — The patrol’s evidence cannot establish its stated URL and connection guarantees.**

   **Quote:** §4.2, L600: “the model never controls a URL.” L614: “The next collector run takes only regex-valid IDs.” L612 specifies “`lsof -i` sampling (1 s)” and “Add a pf user rule if workable [U].”

   **Failure path:** The reviewer still controls URL components through proposed identifiers. Syntax validation does not establish that an identifier came from an authorized source; valid path or identifier characters can carry encoded content. The listed malformed-URL tests miss that channel.

   One-second socket sampling also misses connections opened and closed between samples, so it cannot establish L648’s “zero non-allowlisted connections.”

   **Minimum correction:** Bind automatic fetch requests to trusted source identities or explicitly review that channel; test syntactically valid payload-bearing requests. Use complete connection-event evidence and an enforced egress boundary where the guarantee requires prevention. Describe sampled observations with their actual limits.

8. **P2 — A shared candidate UID does not provide sibling-run isolation.**

   **Quote:** E4c, L294: “a sibling-run read → mode-700 directories under a separate user.” §4.4, L666–667 identifies the candidate user as `augcand`.

   **Failure path:** Mode 700 distinguishes owners, not runs. If candidate work directories belong to the same `augcand` UID, one candidate can read another’s directory. Separating candidates from the maintainer protects controller-owned files but does not establish the claimed isolation between candidates.

   **Minimum correction:** Specify per-run isolation—distinct principals, isolated execution environments, or controller-owned artifacts exposed only through a bounded interface—and test an actual sibling read. Include provisioning of the required candidate identity in the milestone prerequisites.

The original severe findings resolve as follows. **F** means the original Fable review; **A** means the original Astra review.

| Prior finding | Verification against v2 |
|---|---|
| F P0-1; A1 | **Open.** Tool restrictions and no-commit rules improve the design; findings 1 and 7 prevent closure. |
| F P1-1 | **Open/recurred.** Finding 6. |
| F P1-2 | **Resolved in scope.** The public patch is a separate dependency, outside confidential 0.8.0 work; its status needs finding 6’s correction. |
| F P1-3; A6 | **Resolved.** X2 is a commitment with a task-success/cost sub-claim; X3’s falsifier includes adaptation cost, L145–152. |
| F P1-4; A8 | **Partially resolved.** Plug-in naming, C*, shift testing and TOST are present. Finding 3 prevents accepting the experiment. |
| F P1-5; A7 | **Resolved.** GRPO/KTO receive credit, the hypothesis is bounded, learned proposers remain allowed, and P7 is discussion only, L190–230. |
| F P1-6; A10 | **Partially resolved.** Authorized comparators and the NI sign convention are corrected; finding 2 remains. |
| F P1-7; A4 | **Partially resolved.** Boundary nulls, separate test layers and scripted adversaries replace the original A/A error. Findings 5 and 8 remain. |
| F P1-8 | **Resolved as a decision gate.** Decision 12 and M9 require an answer or explicit risk acceptance; no legal conclusion is established. |
| F P1-9; A12 | **Resolved in specification.** The graph covers selection, filtering, inheritance and channels; missing permission evidence is rejected and declared-only limits are explicit, L500–542. |
| F P1-10; A13 | **Resolved in specification.** Receipts, separate review timestamps, missed-dispatch detection, numeric caps and the maintenance-claim restriction are present, L617–657 and L841. |
| A2 | **Resolved.** `sign_exact` is restricted to paired binary, zero-margin superiority; the magnitude counterexample is explicitly refused, L293 and L466. |
| A3 | **Resolved.** Unsupported unequal-probability confirmation is refused, L467 and L571. |
| A5 | **Resolved.** Ownership, implementation and enforcement are separated; unknown and retain outcomes are explicit, L109–169. |
| A9 | **Resolved in specification.** Observability and identification are separate conditions; unsupported causal comparisons stop, L154–155 and L572. |
| A11 | **Resolved in specification.** BANKING77 provenance must be checked; WANLI is an optional generated-text stress test, L456. |

For the existing **Fable v2** review: its P0-1, P1-1 and P1-2 are corroborated by findings 1, 6 and 4. Its P1-3 is corroborated with the reachability qualification in finding 2. Its P1-4 is only partly established: the incomplete comparison family and controls need correction, but actual extreme-ratio power depends on the calibration pilot; holding an assumed variance fixed does not prove those comparisons necessarily impossible.
hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
