# Independent adversarial re-review of the Augustus 0.8.0 plan (plan-v2.md)

Requested routing: claude-fable-5-1, effort xhigh

Observed identity: my environment states, verbatim, "You are powered by the model named Fable 5.1. The exact model ID is claude-fable-5-1." No effort level is stated anywhere in my environment; effort is Unknown from my side.

Reviewer provenance. Read in full: `plan-v2.md`, `plan-v2-dispositions.md`, `plan-v1.md`, `design-brief.md`, `reviews/fable-5.1-xhigh.md`, the final `codex` block of `reviews/astra-max.raw.log` (lines 13581–13718), and the lane passages behind every number I checked. Read-only local checks, run from the worktree at `.claude/worktrees/agent-a902684ec7c1376a8` after `git fetch origin`: `git log`/`git ls-tree -l` at `7118537`, `333397d`, `v0.7.2` and `origin/main`; `.gitignore` at `origin/main`; `claude --help` (2.1.280) and string search of the 2.1.280 binary; `ls -ld`/`ls -lde`/`stat` on the home directory, `.local`, `~/.codex`, `~/.claude`, `~/.cache`, dotfiles and the scratchpad; `id` and `dscl . -list /Users UniqueID`; `typst fonts`; `which`; `df`; `sysctl`; the lane's `calc_v2.py` (re-run) and my own stdlib script (appendix). Only credential file *names* and modes were inspected; no secret value was read or printed. No network beyond `git fetch`, no third-party code, nothing edited except this file, nothing posted.

Confidential. Local only.

---

## Verdict

**NOT ACCEPTED.** One P0 (the separate-user isolation that v2 introduces exposes the plan and the maintainer's credentials on this machine, and the plan's own boundary test cannot see it), four P1, eight P2. The v2 revision is a large, mostly correct response to the 38 prior findings: 31 are resolved as claimed. The remaining defects are concentrated in two places: the OS-level premise under §4.1–4.4, and sample-size arithmetic that makes three pre-registered outcomes unreachable while their opposites stay reachable.

---

## Verification of prior P0/P1 dispositions

| Prior ID | Claimed | Verified? | Evidence / residual |
|---|---|---|---|
| Fable P0-1 / Astra 1 (patrol exfiltration) | Modified: two-stage collector/reviewer, code allowlist, separate user, `chmod 700 .local` | **Partially.** The URL-control and tool-surface redesign is right. The confidentiality leg rests on a false premise on this Mac | See **P0-1** below. `--restricted`, `--bare`, `--permission-mode dontAsk`, `--permission-prompts none`, `--strict-mcp-config`, `--max-budget-usd`, `--effort`, `--no-session-persistence` all exist in 2.1.280 [Rep, `--help`]. `--restricted` also "confines the file tools to the working directories", which the plan does not mention but which helps |
| Fable P1-1 (stale baseline) | Accepted: re-derived to `7118537` | **Not resolved; recurred.** `origin/main` was `7a94072` (0.7.2 released, #104–#106, 12:20–12:23 MDT) when plan-v2 was written (12:36 MDT) | See **P1-1** |
| Fable P1-2 (G4 public patch inside a no-publish plan) | Superseded by the maintainer's separate 0.7.2 | **Resolved**, and 0.7.2 has now shipped (`v0.7.2` → `30b6033`). Plan text still describes it as pending | Folded into P1-1 |
| Fable P1-3 / Astra 6 (X2 unfalsifiable; refuse-all passes) | X2 is [C]; sub-claim needs matched task success and workflow cost | **Resolved** (§2.3 row X2, L151; preamble L145) | — |
| Fable P1-4 / Astra 8 (E1 procedure, n, power, predetermined arm, no shift arm) | TOST, n rule, C\*, shift S, "narrows" | **Mostly resolved.** Residual: the relative margin makes equivalence untestable at extreme ratios, so the outcome table is asymmetric again; arm B duplicates the positive control; B-retrain is underspecified | See **P1-4** |
| Fable P1-5 / Astra 7 (GRPO/KTO, DPO boundary, P7) | Modified | **Resolved** (§2.5, arm E, decision 10) | — |
| Fable P1-6 / Astra 10 (M5 unreachable; NI undefined) | Scoped to R0–R3a; Δ, margin and method defined | **Not resolved.** The arms are now reachable; the margin is not, with any offered method at any feasible n | See **P1-3** |
| Fable P1-7 / Astra 4 (E4 miscalibrated; no executor) | E4a–E4d | **Resolved.** Binomials, MC SE, boundary nulls, Clopper–Pearson and canaries all check [Rep, appendix] | — |
| Fable P1-8 (MCA §2.3(b) on the skill itself) | Decision 12 at M0; M9 exit | **Resolved** | — |
| Fable P1-9 / Astra 12 (terms gate vs synthetic rules; supplied verdict) | §3.4 teacher route; §3.6 graph, declared-only limit | **Resolved.** `SargeDev/jev-distill-corpus` is a real lane sighting (`tmp/trainer/hf/`) | — |
| Fable P1-10 / Astra 13 (maintenance gap, killed runs, confirmations, commits) | §4.2 spend, §4.3 receipts and liveness | **Resolved**, with two nits (first-run receipt; observed model source) | P2-1 |
| Astra 2 (`sign_exact` approves higher loss) | Binary superiority at m = 0 only; E4b fixture | **Resolved** (24×0.01 vs 9×1: p = 0.0068, mean +0.0292 [Rep]) | P2-6 asks for its decision rule to be written |
| Astra 3 (inclusion probabilities) | `equal_probability` only; E4b 50/950 fixture | **Resolved** (−0.667 vs +0.9 [Rep]) | — |
| Astra 5 (ambiguous classifications; absorb default) | §2.2 three properties; unknown states; retain | **Resolved** | — |
| Astra 9 (X5 observability vs identification) | X5a/X5b; `insufficient_causal_evidence` | **Resolved**; `validation.md` L156–160 unchanged at `origin/main` [Rep] | — |
| Astra 11 (WANLI) | BANKING77 with provenance check | **Resolved** | — |

All prior P2s are resolved as stated in the dispositions, with the residuals noted under P2 below.

---

## P0

### P0-1. The separate-user isolation v2 introduces exposes the confidential plan and the maintainer's credentials on this Mac; the plan's own precondition and boundary tests would pass while that exposure persists

**Plan text.** §4.1 L593–596: "The home directory is 750 with group `staff`. `~/Developer`, the checkout, `.local` and `.local/080` are 755, and the files are 644. macOS normally puts standard users in `staff`, so a second local user could read this plan today. `chmod 700 .local` therefore gates both the patrol and E4c." §4.2 L610: "Confidential tree unreadable | The maintainer's `.local/` is mode 700 … | As `augpatrol`, reading `research/080/plan-v2.md` fails with EACCES; no readable `.local/080` path exists." §4.2 L609: "`augpatrol`: no admin, SSH keys, git credential helper, gh/hf/cloud tokens or keychain items." §4.4 L665–667: "The grader and confirmation data are mode 700, unreadable to the candidate's macOS user, `augcand`." §4.4 L664: "No sandbox is claimed." Decision 16: "`chmod 700` now."

**What I found [Rep, `ls -ld`, `stat`, `grep -c`, `id`].** The lane looked at the right modes and drew the boundary too narrowly. With the home directory at `drwxr-x---` (group `staff`) and default umask 022, every non-700 path under it is readable by any `staff` member. Today that includes:

- `~/.codex/sessions/2026/09/23/rollout-2026-09-23T11-59-51-01a0cf6c-…jsonl` (mode 644, 4.7 MB): the Astra v1 review session, containing the plan text (15 hits for `plan-v1`, 2 for "Confidential and local only"). `~/.codex` 755, `~/.codex/sessions` 755, `2026/`, `09/`, `23/` all 755.
- `~/.codex/sessions/2026/09/23/rollout-2026-09-23T12-37-59-01a0cf8f-…jsonl` (mode 644, 2.0 MB and growing at 12:46): a session reading plan-v2 (36 hits for `plan-v2`, 9 for `augpatrol`).
- [Credential-file inventory (file paths, modes and variable names) redacted for publication, 2026-09-23. The finding stands: several credential files on the Mac were readable by a second local account at the time.]

A second local account already exists (uid 501, gid 20 `staff`, also in `admin`), so "could read this plan today" is "can". The planned `augpatrol` and `augcand` would be non-admin `staff` members with exactly this read access.

**Failure path.** (1) The M7a boundary test "reading `research/080/plan-v2.md` fails with EACCES" passes after `chmod 700 .local`, while `cat ~basitmustafa/.codex/sessions/2026/09/23/*.jsonl` succeeds as `augpatrol` and yields the plan. The reviewer's `--restricted` cwd confinement is the only thing between the reviewer and that file, and CONTRIBUTING says not to treat CLI-level read restrictions as an enforced sandbox. (2) Worse, `augcand` runs LLM-authored candidate code with no network restriction ("No sandbox is claimed"); as written it can read `~/.zshrc` and `~/.cache/huggingface/token` and publish with the maintainer's own credentials. E4c tests only "the candidate reads confirmation data → OS permission denied"; it never tests a read of the maintainer's home. Executing the plan as written therefore creates a credential-exfiltration path that the plan's own tests certify as closed. (3) The claimed premise of §4.2 row 1, that `augpatrol` "holds no credentials", is true of its own home and false of what it can reach.

**Minimum correction.**
1. Before any new user is created: `chmod 700 ~` (the modern macOS default; nothing in the plan needs a second user to traverse the maintainer's home). Additionally `chmod -R go-rwx ~/.codex ~/.cache/huggingface ~/.claude` and `chmod 600 ~/.zshrc ~/.zprofile ~/.bashrc ~/.claude/settings.json`, because a 750 home can be restored by a future account migration. Consider whether keys that have sat in a 644 `.zshrc` on a multi-account Mac need rotation; that is the maintainer's call.
2. Replace the §4.2 L610 test with one that does not enumerate paths: as `augpatrol` and as `augcand`, `find ~` must return nothing readable (`sudo -u augpatrol find ~ -type f -print 2>/dev/null | wc -l` = 0), and a grep of every readable file on the machine outside their own homes for "Confidential and local only", `plan-v2` and the strings `_API_KEY=` must be empty.
3. State the implications: the pinned `claude` 2.1.280 binary lives under `~/.local/share/claude/` (700), so `augpatrol` needs its own per-user install of the pinned version; the candidate's inputs (venv, fit and calibration data) must be staged where `augcand` can read them (its own home or `/Users/Shared`, which is 1777), not under the maintainer's home; and `augcand` egress should be blocked with a pf `user` rule or the candidate must be run with network disabled, since a candidate with network and any readable credential is the exfiltration channel.
4. M7a and M3 cannot start until (1)–(2) pass. Add both to M0.

---

## P1

### P1-1. The baseline is stale again, this time at authorship; 0.7.2 has shipped without the `.gitignore` change that decision 16 assigns to it

**Plan text.** Provenance table L14: "Public baseline [Rep, local git] | `origin/main` = `7118537` (#96–#103)". L15: "0.7.2 branch | `skill/072-provider-terms` (`333397d`, `0.7.2-dev`): references 173,472 B; `SKILL.md` 10,747 B". §0 L31: "The `optimizer-integration.md` distillation fix ships as public 0.7.2." §6 row P L786: "0.7.2 public patch from public `main` (separate) | — | — | Released; the 0.8.0 branch rebased on its tag". Decision 16 L843: "Add `.local/` to `.gitignore` in 0.7.2." §3.1 L376: "(10,747 of 16,000 B after 0.7.2)". Sources L854: "Rows 1–31 of the v1 Sources table in `plan-v1.md` carry over unchanged."

**What I found [Rep, `git fetch` + `git log --format=%ci`].** `#104` (0.7.2-dev, 12:20:36 MDT), `#105` "Release Augustus 0.7.2" (12:22:04 MDT, tag `v0.7.2` → `30b6033`) and `#106` (12:23:55 MDT, `origin/main` = `7a94072`) all precede plan-v2's 12:36 MDT save. The lane's `git refs and byte sums` were taken from an unfetched local `origin/main`. At `v0.7.2`: references 16 files, 173,472 B; `SKILL.md` 10,743 B, not 10,747 (the 10,747 figure belongs to `333397d`, whose references total 173,425 B, not 173,472). `origin/main:.gitignore` does not contain `.local/`; the only rule is still `.git/info/exclude:7`. v1 Sources row 2 pins the repo at `4236a60`, which v2 carries over "unchanged".

**Failure path.** A maintainer following §6 row P looks for a 0.7.2 to release that already exists; the rebase target is a tag, not the branch the plan names; decision 16's vehicle has left, so `.local/` stays unprotected against a re-clone; and the provenance table, which the plan holds up as [Rep], was wrong 13 minutes after it was written for the same reason P1-1 was raised on v1. The disposition's "Re-derived" was a re-read of a stale ref.

**Minimum correction.** Re-baseline to `v0.7.2` = `30b6033` and `origin/main` = `7a94072`; mark row P done; move the `.gitignore` addition to a 0.7.3 or the first 0.8.0 commit and say which; correct the byte figures; replace Sources row 2 rather than carrying it over. Add to the lane's own check list: "`git fetch origin` before quoting `origin/main`", since the plan labels these numbers [Rep].

### P1-2. E3's sample plan contradicts its own margin and family; the equivalence half of E3 cannot fire at n = 1,200

**Plan text.** E3 L282: "Margin 0.02 utility (about 2 EM points). TOST and superiority tests as in E1. Primary family m = 6 (λ = 0.1 × 2 models × 3 contrasts)". L283: "n rule | σ from a 100-question pilot. Planning [Rep calc]: σ = 0.30, δ = 0.03, α/3 gives about 880. Plan 400 search + 1,200 confirmation questions". L285: "Rejects | Implicit or a constant equivalent to the best explicit arm; **or** (vi) equivalent to (vii); …". §2.7 common rules L252: "'Supports' requires a significant pre-registered result."

**What I found [Rep, appendix, and the lane's own `calc_v2.py`].** The "about 880" is `n_sup(σ=0.30, δ=0.03, α=0.05/3)` in `calc_v2.py`: a one-sided *superiority* n at 80% power, at a δ (0.03) that is not the margin (0.02), at a family (3) that is not the declared family (6). The same script also printed `n_sup(0.30, 0.02, 0.05/3) = 1,984`, which the plan did not use. Under the plan's own E1 rule with the E3 margin and family: n ≈ 3,040 (80% TOST power) or 3,670 (90%). More directly: the (1 − 2α/m) paired CI half-width at n = 1,200, σ = 0.30, m = 6 is 2.394 × 0.30/√1200 = **0.0207 > 0.02**, so the TOST CI cannot lie inside ±0.02 even when the true Δ is exactly zero. At m = 3 it is 0.0184, which passes only at Δ ≈ 0 with roughly 50% power.

**Failure path.** Every E3 "Rejects" disjunct that is an equivalence claim ("implicit or a constant equivalent"; "(vi) equivalent to (vii)") is unreachable at the planned n, while the superiority-based "supports" contrasts remain reachable. That is the asymmetric design Fable P1-4 flagged for E1, reproduced in E3 by arithmetic. The compute cap (L286) and the "drop the 4B reader before cutting n" rule are planned around the wrong n. The common rule "declared underpowered before confirmation is read" would rescue honesty, but then E3 could never reject P5/P6, and the plan presents 1,200 as adequate.

**Minimum correction.** Recompute n from the E1 rule with δ = 0.02 and m = 6 (≈3,000–3,700 at σ = 0.30; HotpotQA dev has 7,405, so 400 search + ≥3,100 confirmation is feasible), recompute the compute cap (≈37,000–44,000 calls, then the timing pilot decides), or widen the margin and say why 0.03 utility is still meaningful, or pre-declare which contrasts are superiority-only and drop "equivalent" from their reject rows. State the power target (0.8 or 0.9) once; the E1 rule's `z₀.₉` term is 80% power for TOST and 90% for one-sided superiority, and the plan uses both readings.

### P1-3. The M5 non-inferiority margin (+0.01) is unreachable with any offered method at any feasible n, and T1 evidence cannot support a margin under the plan's own eligibility rule

**Plan text.** §3.3 L434: "Test | Non-inferiority: one-sided 95% UCB(Δ) < +0.01, using the method E4a qualifies". L433: "Δ = policy loss(low rung) − policy loss(R3a), in normalized cost per case at a fixed cost matrix". L438: "n | About 470 paired items per task detect 5 pp at 15% discordance [R, lane]. M2 recomputes this for non-inferiority". L435: "If R1 or R2 is non-inferior on T1 and T2 | The Mac-first recommendation stops at R2". §3.5 L463–466: methods are `hoeffding`, `empirical_bernstein`, `sign_exact` (superiority, m = 0 only). §2.4 L181–182: "Proxy or fixture evidence cannot support a margin." §3.4 L456: T2 is "A BANKING77 20-way subset".

**What I found [Rep, appendix].** Normalized cost per case lies in [0, 1], so paired differences have range 2. One-sided 95% Hoeffding radius: n = 470 → 0.113; n = 3,400 → 0.042; radius 0.01 needs n ≈ 59,900. Empirical Bernstein (Maurer–Pontil, range 2) at n = 470: 0.049 even at an empirical σ of 0.10; radius 0.01 needs n ≈ 3,300 in that best case. BANKING77 has about 13,000 queries over 77 intents [R, dataset card; recheck at M2], so a 20-way subset is roughly 3,400 rows in total, before any fit/calibration split. `sign_exact` refuses non-inferiority by design. The lane's 470 was a McNemar power calculation for detecting a 5 pp *superiority*, which the plan acknowledges but does not act on. Separately, T1 is the generated task (M3 "T1 generator"), so its confirmation rows are `fixture_evidence_only` and, by §2.4 test 2, cannot support the margin at all.

**Failure path.** "UCB(Δ) < +0.01" is a rule that cannot return true on T2 with the shipped methods, and cannot return an eligible true on T1 at any n. M5's exit criterion "§3.3 rule applied" is then met by an outcome the table does not list (inconclusive), and the Mac-first recommendation is fixed by omission, which is the defect Fable P1-6 and Astra 10 described, now caused by arithmetic instead of missing arms. "M2 recomputes this" defers a calculation that needs no data: Hoeffding is distribution-free and the arithmetic is above.

**Minimum correction.** Pick a margin the data can certify and say why it is meaningful: at n ≈ 2,000 real T2 confirmation rows, EB certifies about 0.015–0.03 depending on σ; Hoeffding certifies 0.05 at 2,397 (the lane's own "Hoeffding n = 2,397" figure). Add an "inconclusive" row to the M5 table whose consequence is stated (the default remains the procedure, with no rung recommendation). Label T1's M5 result as fixture evidence that informs the recipe text but cannot satisfy the rule. Do this now, in the plan, not at M2.

### P1-4. E1's outcome table is asymmetric again: the relative margin makes equivalence untestable at extreme ratios, arm B is the positive control under another name, and B-retrain is underspecified

**Plan text.** E1 L264: "Margin δ_r = 2% of A's cost at ratio r, measured on calibration and frozen". L266: "σ = 0.10 and δ = 0.004 give n ≈ 8,100". L268: "Rejects X1 on the task | B equivalent to A at every off-training ratio, **or** …". L269: "Narrows | C\* or E equivalent to A at every held-out ratio **and** under S …". L270: "Supports | A superior to B off-ratio, **and** A-recal non-inferior to B-retrain under S with no more labels, **and** the positive control fired". L262: "**B:** cost-weighted head at 1:1". L267: "Positive: a stale threshold of 0.5 at r ≠ 1:1 must test worse than A". L263: "**B-retrain** retrains with the same 200 labels at the new cost".

**What I found [Rep, appendix].** (a) δ = 0.004 is 2% of an A cost of 0.20. At 1:49 (C_FP = 0.02) A's normalized cost is far smaller; at A cost 0.05 the margin is 0.001 and n ≈ 156,000 (m = 13); at 0.03, n ≈ 433,000. CivilComments' 97k test split cannot supply that, so the 1:49 TOST is declared underpowered under L249–251. (b) A cost-weighted logistic head at 1:1 is the unweighted head thresholded at 0.5 on the same calibrated scores, which is exactly the "stale threshold of 0.5" positive control; "A superior to B off-ratio" is therefore implied by "the positive control fired". (c) The planning n uses m = 5 (α/5 reproduces 8,136; α/6 gives 8,443), while the family described in L265 has at least 13 members per dataset. (d) "Retrains with the same 200 labels" does not say whether B-retrain sees the fit split; a head trained from scratch on 200 rows loses to a recalibrated full-data head by construction.

**Failure path.** "Rejects X1" and "Narrows" both require equivalence "at every" held-out ratio; one underpowered ratio makes both unreachable while "Supports" needs only superiority plus the shift-S non-inferiority. One of the three "Supports" conjuncts is tautological. B-retrain can be a straw arm. This is the residual of Fable P1-4(a)–(b) and Astra 8, after v2's genuine fixes.

**Minimum correction.** Define δ_r as an absolute normalized-cost margin (0.004) or as a fraction of the constant-policy cost, and compute n per ratio from the pilot σ_r; restate the outcome rows as "at every ratio where the TOST was powered", and report "supports" only over the same set of ratios. Either drop B or define it as "retrained at the deployment ratio with the fit data", which is the real endogenous alternative and makes "A superior to B" a test. Specify B-retrain as the strongest cheap retrain: fit data reweighted to the new prior plus the same 200 labels. State m for the planning n.

---

## P2

### P2-1. Reviewer profile details that the M7a test will hit, and the observed-model source

§4.2 L611 quotes the command with `--output-format stream-json` and no `--verbose`. The 2.1.280 binary contains the string "stream-json requires --verbose" [Rep, string search]; add `--verbose` or expect the first launch to fail. L612 requires that `lsof -i` show "only the inference endpoint"; Claude Code also makes telemetry, error-reporting and update connections unless `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` (or `DISABLE_TELEMETRY`, `DISABLE_ERROR_REPORTING`, `DISABLE_AUTOUPDATER`) is set; all four names are in the binary. Without them the test fails for a benign reason and the temptation is to widen the allowed hosts. 1-second `lsof` sampling misses short-lived connections; use a pf log rule or `tcpdump` filtered on the user for the duration of the injection test. §4.3 L635 takes "Model … observed" from the init event, which reports the CLI's configuration (the same caveat the plan applies to the Codex header at L12); take the observed model from the `model` field of assistant messages in the stream. §4.3 L639–640: the first run has no previous receipt and will write `failed(previous_run_missing)`; seed receipt 0 at M7a.

### P2-2. `augcand` is created nowhere, sibling-run isolation has no working mechanism, and candidate network is unspecified

§4.4 L665 and E4c L294 depend on a second standard user `augcand`; decision 15 (L842) creates only `augpatrol`, and M0/M3 do not mention it. E4c's "a sibling-run read → mode-700 directories under a separate user" cannot work if every candidate runs as the same uid: a directory a candidate can write to is readable by the next candidate under that uid. Either run candidates strictly sequentially (then there is no sibling and the fixture tests nothing), give each run its own uid, or have the controller own run directories and hand each candidate a group-writable one. Say which. State the candidate's network policy (see P0-1 item 3).

### P2-3. Pre-registration needs a second lock point

§2.7 L236–237: "Each pre-registration is hashed … before any download or data read." L259: "Fit, calibration and confirmation splits are seeded and hashed." L248: "σ for the n rule comes from a calibration-split pilot." L264: "δ_r … measured on calibration and frozen." Split manifests, σ, n and δ_r cannot be in a hash produced before download. Name the two locks explicitly: a design lock (estimand, arms, rules, seeds, α, power, margin rule) before download, and an analysis lock (split manifest hashes, σ, n, δ_r per ratio, underpowered declarations) after calibration and before any confirmation read, both dated in `research/080/prereg/` per decision 17. Otherwise the numbers that decide reachability are adjustable without a record.

### P2-4. The plan's arithmetic artifact is in an ephemeral directory

Sources L864 cites "`calc_v2.py` (scratchpad)" as reproducing "every binomial, sign-test, sampling and sample-size number". The scratchpad is `<session-scratch>`, which macOS clears on reboot and periodic cleanup. Copy it, with its sha256, into `research/080/tmp/` beside `sim_exogeneity.py` and the v1 scripts (Sources row 5), and cite the persistent path. AGENTS.md: preserve research provenance. The same applies to my appendix script, which is why it is inlined below.

### P2-5. E3 compute-cap arithmetic omits the search set

L286: "At most 6 calls per question per model, so about 14,400 calls." 1,200 × 6 × 2 = 14,400 covers confirmation only; with the 400 search questions it is 19,200, and after P1-2's correction about 37,000–44,000. Restate the cap after the n is fixed.

### P2-6. `sign_exact` has no UCB; write its decision rule

§2.4 L178 defines superiority as "UCB(Δ) < −m" for every method, but a sign test produces a p-value on discordant pairs, not an upper confidence bound on Δ. State the rule as "one-sided exact binomial p ≤ α/K on discordant pairs, losses in {0, 1}, m = 0", and have `--help` say that it certifies direction only (§3.5 already says it refuses other input).

### P2-7. Minor provenance and consistency nits

- §2.2 arm-class table (L134–138) omits A_tuned; classify it.
- E1 L265 "Monotonicity violations are a hard criterion" does not say monotone in what (decision vs cost ratio at fixed score, presumably).
- §4.3 L642 "Cadence: daily" and §4.3 success "7 receipts" are consistent, but the freshness LaunchAgent's "grace" is unstated; give it a number.
- §5.5 grid row gives "12px outer" gutters on mobile against a 16px convention elsewhere in the repo's design guidance; confirm intentionally or align.
- Sources row 41 marks 2201.05955 "Not re-read by this lane"; the paper is cited as [C] in §3.4. Either read it before M2 or keep the label "C (via reviewer)" in the plan body.

### P2-8. The `.claude/` untracked directory and worktrees

`git status` shows `?? .claude/` in the main checkout, holding `worktrees/agent-…`. No plan copies live there today [Rep, `find`], but review lanes run from those worktrees and can write there. Add `.claude/` to the same ignore rule as `.local/` and to the P0-1 boundary grep.

---

## What v2 gets right (so the fixes do not over-correct)

- The two-stage collector/reviewer split with a code-level allowlist, identifier-only URL construction, typesafe.ai hard-deny, no exec/network tools in the reviewer, receipts outside every checkout and OS-log-based success criteria is the correct shape; keep it and fix the OS premise under it.
- X2 as a commitment with a bounded sub-claim; X5a/X5b; the three-property definition (ownership, implementation, enforcement); "retain" as an outcome; and "narrows" as a first-class E1 result all answer the v1 findings squarely.
- E4a–E4d is now a calibration study with boundary nulls, Monte Carlo uncertainty, positive controls, canaries and a correctly computed binomial smoke test; every number I re-derived reproduces (appendix).
- The provenance graph (§3.6), derived `evidence_kind`, equal-probability-only confirmation, and the declared-only disclaimer are consistent with each other and with AGENTS.md.
- The design section is specific, testable, and matches the brief and `.stitch/DESIGN.md` tokens [Rep]; STIX Two Text/Math are installed [Rep, `typst fonts`]; Jekyll is absent and system Ruby is 2.6.10 [Rep].

## Not covered

No network beyond `git fetch`. I did not re-read the arXiv sources; every arXiv ID in v2 appears in at least two lane files [Rep, grep], and the CapScope, verifier-tax, toy-regret, drift and GEPA numbers trace to the lane passages I read. BANKING77 and HotpotQA sizes are from memory of their dataset cards and are marked for M2 recheck. I did not test `--restricted` or `--permission-mode dontAsk` behavior by running the CLI, only their presence in `--help`. I did not run `make check`.

---

## Appendix: arithmetic script (stdlib; run with Python 3.14.7)

```python
"""Independent arithmetic for the v2 re-review. Stdlib only."""
from math import comb, log, sqrt
from statistics import NormalDist

N = NormalDist()
z = N.inv_cdf

print("== E4d binomial (n=20, p=.05)")
tail = lambda n, p, k: sum(comb(n, i) * p**i * (1 - p) ** (n - i) for i in range(k, n + 1))
print(f"  P(>=3)={tail(20,.05,3):.4f}  power@.20={tail(20,.20,3):.3f}  zero-in-20 upper95={1-0.05**(1/20):.3f}")
print(f"  E4a MC SE at 5%, R=4000: {sqrt(.05*.95/4000):.4f}")

print("== E4b sign case: 24 wins of 0.01 vs 9 losses of 1 in n=300")
p_one_sided = sum(comb(33, k) for k in range(0, 10)) / 2**33
print(f"  one-sided p={p_one_sided:.4f}; mean loss delta=+{(9-0.24)/300:.4f}")
print(f"  G0: 20 discordant all wins p={0.5**20:.2e}")

print("== E1 n rule: n=((z_{1-a/m}+z_0.9)*sigma/delta)^2, sigma=.10")
for m in (4, 5, 6, 13, 26):
    for d in (0.004, 0.002, 0.001):
        n = ((z(1 - 0.05 / m) + z(0.9)) * 0.10 / d) ** 2
        print(f"  m={m:2d} delta={d}: n={n:,.0f}")

print("== E3: sigma=.30; declared margin 0.02; declared family m=6; plan n_conf=1,200")
for label, m, d, zp in (("plan text 'a/3, delta .03'", 3, 0.03, z(0.8)),
                        ("same at 90% power", 3, 0.03, z(0.9)),
                        ("margin .02, m=3, 80%", 3, 0.02, z(0.8)),
                        ("margin .02, m=6, 80% (TOST at true 0)", 6, 0.02, z(0.9)),
                        ("margin .02, m=6, 90% TOST", 6, 0.02, z(0.95))):
    n = ((z(1 - 0.05 / m) + zp) * 0.30 / d) ** 2
    print(f"  {label:40s}: n={n:,.0f}")
for m in (3, 6):
    hw = z(1 - 0.05 / m) * 0.30 / sqrt(1200)
    print(f"  (1-2a/m) CI half-width at n=1200, m={m}: {hw:.4f}")
print(f"  compute: 1200*6*2={1200*6*2:,}; (400+1200)*6*2={(1600)*6*2:,}")

print("== M5 non-inferiority at +0.01, normalized cost per case in [0,1] (paired diff range 2)")
a = 0.05
for n in (470, 800, 2000, 3400):
    hoeff = 2 * sqrt(log(1 / a) / (2 * n))
    def eb(s, n=n, R=2):
        return s * sqrt(2 * log(2 / a) / n) + 7 * R * log(2 / a) / (3 * (n - 1))
    print(f"  n={n:5d}: Hoeffding radius={hoeff:.3f}; EB radius s=.10: {eb(.10):.3f}, s=.20: {eb(.20):.3f}, s=.30: {eb(.30):.3f}")
print(f"  Hoeffding n for radius 0.01: {4*log(1/a)/(2*0.01**2):,.0f}; for 0.05: {4*log(1/a)/(2*0.05**2):,.0f}")
n = 470
while True:
    s = .10
    r = s * sqrt(2 * log(2 / a) / n) + 7 * 2 * log(2 / a) / (3 * (n - 1))
    if r <= 0.01:
        break
    n += 10
print(f"  EB n for radius 0.01 at s=.10 (best case): {n:,}")

print("== E1 relative margin at extreme ratios: delta_r = 2% of A's cost")
for costA in (0.20, 0.10, 0.05, 0.03):
    d = 0.02 * costA
    n = ((z(1 - 0.05 / 13) + z(0.9)) * 0.10 / d) ** 2
    print(f"  A cost {costA:.2f} -> delta {d:.4f} -> n (m=13, sigma .10)={n:,.0f}")
```

Output (2026-09-23, this lane):

```
== E4d binomial (n=20, p=.05)
  P(>=3)=0.0755  power@.20=0.794  zero-in-20 upper95=0.139
  E4a MC SE at 5%, R=4000: 0.0034
== E4b sign case: 24 wins of 0.01 vs 9 losses of 1 in n=300
  one-sided p=0.0068; mean loss delta=+0.0292
  G0: 20 discordant all wins p=9.54e-07
== E1 n rule: n=((z_{1-a/m}+z_0.9)*sigma/delta)^2, sigma=.10
  m= 5 delta=0.004: n=8,136      m= 6 delta=0.004: n=8,443      m=13 delta=0.004: n=9,736
  m= 5 delta=0.002: n=32,542     m=13 delta=0.001: n=155,775    m=26 delta=0.004: n=10,879
== E3: sigma=.30; declared margin 0.02; declared family m=6; plan n_conf=1,200
  plan text 'a/3, delta .03'              : n=882
  same at 90% power                       : n=1,163
  margin .02, m=3, 80%                    : n=1,984
  margin .02, m=6, 80% (TOST at true 0)   : n=3,040
  margin .02, m=6, 90% TOST               : n=3,670
  (1-2a/m) CI half-width at n=1200, m=3: 0.0184
  (1-2a/m) CI half-width at n=1200, m=6: 0.0207
  compute: 1200*6*2=14,400; (400+1200)*6*2=19,200
== M5 non-inferiority at +0.01, normalized cost per case in [0,1] (paired diff range 2)
  n=  470: Hoeffding radius=0.113; EB radius s=.10: 0.049, s=.20: 0.062, s=.30: 0.074
  n=  800: Hoeffding radius=0.087; EB radius s=.10: 0.031, s=.20: 0.041, s=.30: 0.050
  n= 2000: Hoeffding radius=0.055; EB radius s=.10: 0.015, s=.20: 0.021, s=.30: 0.027
  n= 3400: Hoeffding radius=0.042; EB radius s=.10: 0.010, s=.20: 0.014, s=.30: 0.019
  Hoeffding n for radius 0.01: 59,915; for 0.05: 2,397
  EB n for radius 0.01 at s=.10 (best case): 3,280
== E1 relative margin at extreme ratios: delta_r = 2% of A's cost
  A cost 0.20 -> delta 0.0040 -> n (m=13, sigma .10)=9,736
  A cost 0.10 -> delta 0.0020 -> n (m=13, sigma .10)=38,944
  A cost 0.05 -> delta 0.0010 -> n (m=13, sigma .10)=155,775
  A cost 0.03 -> delta 0.0006 -> n (m=13, sigma .10)=432,709
```
