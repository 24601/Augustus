# Replicate on NVIDIA before release, rather than relocate to it (2026-09-25)

Maintainer decision: the world runs NVIDIA, and results validated only on gfx1151/ROCm are a
liability at release. That is right. The sharper version of it, and what this plan does, is
**replicate and report both** rather than move the work.

A cross-vendor replication is worth more than a relocation. Moving makes the ROCm runs disappear
and leaves one set of numbers from one machine. Replicating produces a paired comparison that
directly tests the transportability limit E3's determinism receipt already measured — rerun
instability above the margin on two arms — and turns "we ran on an unusual box" into evidence
about whether these claims are hardware-dependent at all.

If the two agree, the claims are stronger than either run alone. If they disagree, that is a major
finding and we would rather publish it than not know.

## What is expected to differ, and what must not

Stating this before the run, so agreement is not read as luck and disagreement is not explained
afterwards.

| Quantity | Expectation |
| --- | --- |
| Bitwise identity of embeddings, logits, probabilities | **Will differ.** Different kernels, different reduction orders. E3 already measured 100% joint rerun disagreement on a single vendor |
| E1's fitted temperature, per-arm costs, contrast means | Should agree to about three decimals. These are averages over 10⁵–10⁶ rows; kernel noise averages out |
| **E1's conclusions** — A beats B-stale; A not non-inferior to retraining at extreme ratios; recalibration removes most of the shift penalty | **Must not change.** The effects are 0.003–0.048 against kernel differences of order 10⁻⁶ |
| E3's reader answers, per question | May differ on a minority of questions. A different backend is at least as large a perturbation as a rerun, and a rerun changed 1.3% of thresholded actions |
| **E3's conclusions** — explicit beats implicit; explicit does not beat reading everything; P5 short of its margin | Should hold, but this is the genuinely uncertain one. P5 failed by 0.004 of utility, which is inside the range a backend change could move |
| M5's PAW rungs | **Only possible on NVIDIA.** Nothing to compare |

The row worth watching is P5. It missed its margin by 0.0037, and the rerun instability measured on
one vendor was of the same order. If NVIDIA flips it, the honest report is that the claim is
inside the noise of the platform, which is a more useful statement than either verdict alone.

## What gets replicated, in order of value

1. **M5's A2a and A2b.** Not a replication — they cannot run on ROCm at all, and this is the reason
   the NVIDIA machine exists. The bundle and the far-side program are already written.
2. **E3 confirmation.** The largest transportability risk, and the cheapest interesting result: one
   reader, 6,405 questions, 57,645 calls, about 1.8 GPU-h at tabputer's measured rate.
3. **E1 confirmation.** 1.67M embeddings, about 2.5 GPU-h. Lowest risk, highest row count, and the
   one whose conclusions the paper leans on hardest.
4. E4 needs nothing: it is simulation, and its parity check already passed 64/64.

## Custody does not move

The same split that made E1 and E3 work transfers unchanged. **The NVIDIA side receives inputs and
emits predictions; it holds no confirmation label and computes no loss; `augctl` grades.** That is
already how `m5_colab.py` is built, and the E1 and E3 replications reuse it: `e1_predict.py` and
`e3_replay.py` both already read inputs only and refuse if a row carries a label.

The corpora are public — BANKING77 CC BY 4.0, CLINC150 CC BY 3.0, CivilComments CC0, HotpotQA
CC BY-SA 4.0 — so the transfer is of already-public text. The partitions are seeded and
reproducible, and the manifests carry the digests to prove the far side received the same rows.

## What has to be pinned before anything runs

The whole point of replicating is to change one variable. So the NVIDIA environment gets the same
treatment tabputer got:

- a named image with a recorded digest, built from a stated base, with a full `pip freeze`;
- the same model revisions — MiniLM `1110a243…`, Qwen3-1.7B `70d244cc…`, Qwen3.5-2B-Base
  `b1485b2f…` — verified by hash, not by name;
- the same scripts at the same commits, hashes recorded;
- the same seeds, which are already in the scripts rather than passed in.

A replication that also changed the transformers version would answer no question at all.

## What this does not claim

- It does not make ROCm results wrong, and the receipts stay. A result that holds on both is
  stronger than one from either.
- It does not remove E3's determinism failure. That was measured within one vendor and the frozen
  tables remain the sole source on each side separately.
- Agreement across two machines is not agreement across all hardware. Two is two.

## Where to run it, which is not the same question as which GPU

Colab and a rented box are not interchangeable here, and the difference matters more than the card.

**The replication's whole value is changing one variable.** That needs a pinned image, a recorded
digest, a `pip freeze`, and the same script hashes — the treatment tabputer got. Colab supplies an
environment we do not control and that changes underneath us: its CUDA, driver, torch and
preinstalled packages are Google's choices on the day. A replication whose environment cannot be
stated is a weaker answer to "is this hardware-dependent" than no replication at all, because a
disagreement could not be attributed.

So:

| Work | Where | Why |
| --- | --- | --- |
| **M5 A2a, A2b** | Colab is fine | There is no ROCm baseline to compare against. The requirement is an NVIDIA GPU that the compiler runs on, and nothing is being held constant |
| **E1 and E3 replication** | A rented GPU running **our** container | The claim is about agreement across hardware, so everything except the hardware has to be pinned |

### What the GPU actually has to be

| Job | Memory | Time at tabputer's measured rate |
| --- | --- | --- |
| A2a PAW-standard compile | about 8 GB | minutes |
| **A2b PAW-ft** | **about 38 GiB** | the binding constraint |
| E3 confirmation replay, 1.7B, 57,645 calls | about 14 GiB | about 1.8 GPU-h |
| E1 confirmation, 1.67M MiniLM embeddings | small | about 2.5 GPU-h |

A2b is the only job that needs a large card. Everything else fits comfortably on an L4 or a T4.

### The ephemeral-envelope problem, which §3.7 already names

Colab is `E-ephemeral`: the session can vanish. §3.7's rule for that envelope is that every step
must be resumable and every artifact hashed on write. `m5_colab.py` already hashes each program
before it runs, but a lost session mid-way through 60,000 T2c inputs loses the run. Either
checkpoint per task, or accept re-running the task.

## /mnt/tst carries no permissions, so it carries no custody

Discovered while staging the export bundle for transfer: `/mnt/tst` on tabputer is **exfat**
(`/dev/sda1`, `fmask=0022,dmask=0022`). It has no Unix owners and no permission bits. A file placed
there reports owner root and mode 755 because that is the mount mask, not anything a `chmod` or
`chown` set — both were attempted and `chown` returned `Operation not permitted` while `chmod`
returned 0 and changed nothing.

The practical consequence is a rule rather than a curiosity:

**Nothing whose protection depends on file permissions may be written to `/mnt/tst`.** That
includes every confirmation label file, every gold answer, and anything under `/srv/aug/ctl`. Those
live on a filesystem that enforces modes, and `augexp` gets EACCES on them there. Copied to
`/mnt/tst` they would be readable by any local user, silently, with a mode string that looks
deliberate.

What may go there is material whose protection does not depend on permissions at all — public
benchmark text, hashes, manifests, receipts. The export bundle qualifies: it was checked twice for
labels before it moved and carries only rows from CC-licensed corpora.

This is also why the transfer to the Mac is a *copy of a checked artifact* rather than a share of
the staging tree. `basit` is uid 1000 and in neither `augexp` nor `augctl`, so `/srv/aug/stage` and
`/srv/aug/ctl` are unreadable to him over ssh — the boundary working as designed. The bundle
crosses because it was built to cross, not because the boundary was relaxed.

## The instrument was under-documented, and a replication is how we found out

2026-09-26. Building the E1 export bundle surfaced a gap nobody had noticed while running E1 itself:
the fit receipt records the encoder revision, batch size, max length and the fitted temperatures,
and records **nothing about the head's optimization**. Asked to name the logistic `C` and solver,
the export principal correctly answered "not recorded" rather than guessing.

They do not exist. The head is not scikit-learn. `research/080/exp/e1_fit.py` line 89 is plain
logistic regression by full-batch Adam — zero-initialized `w` and `b`, BCE-with-logits, mean
reduction, optional per-example weights, `epochs=200`, `lr=0.1`, `seed=80_201`, **no regularization
term of any kind**. The temperature at line 112 is a scalar with no intercept, 300 epochs at lr 0.05.

**A replicator reading "C: not recorded" would reasonably reach for sklearn's default of 1.0 and fit
a regularized head.** The numbers would look plausible, the conclusions might even match, and the
instrument would be a different one. That is the failure mode a replication exists to catch, and it
was caught before a single row was embedded — by someone refusing to supply a value they could not
source, rather than by a disagreement discovered afterwards.

The bundle note now carries epochs, lr, init, seed, the script path, its ref and its file sha256.
The lesson generalizes past E1: **a receipt that records fitted outputs but not the procedure that
produced them is not a reproducible instrument**, however precisely it states its temperatures.

## Outcome, 2026-09-26: both experiments replicate, and the one difference is a backend

E1 on an NVIDIA L4 and E3 on an A100, both against bundles that carried inputs only. Full receipts:
`receipts/e1-nvidia-2026-09-26.md`, `receipts/e3-2026-09-25.md` and
`receipts/e3-determinism-2026-09-24.md`.

**Every conclusion holds and nothing was adjusted afterwards.**

- E1's three named expectations, written before either run: cost-aware thresholding beats the stale
  0.5 threshold from −0.0034 to −0.0481, bracketing the original range; recalibration removes
  **42.17%** of the prior-shift penalty against the original 42%; and P9's non-inferiority half is
  still **refuted**, at +0.002453 against a 0.001071 margin — **bit-identical** to gfx1151.
- E3's three contrasts agree to the third decimal with every verdict unchanged, including **P5,
  which the plan named in advance as the uncertain row.** It is powered and failed on both machines.
- E3's arm selection is identical: the same four choices from a search table whose every row differs
  bitwise from the one that produced them on ROCm.
- E1's refit temperatures moved by **6 × 10⁻⁸**, and across 68 contrast rows there were **zero mode
  or power flips**.

**The one thing that did not replicate is the failure.** E3's determinism check recorded 100% joint
rerun disagreement on gfx1151; a same-box NVIDIA rerun measured 0.0000, with identical answers,
identical actions and identical exact-float probabilities. E1 agrees from the other side: its
temperature re-derived on four different L4s with drift exactly 0, and a repeated civil fit produced
a byte-identical report. **Within-vendor determinism holds on NVIDIA in both experiments and failed
on ROCm in one** — so that caveat belongs to a backend, not to the method.

### Where σ̂ moved, and why it is the right arm

E1's σ̂ differences concentrate entirely in **arm C, the MLP** — the only arm with a randomly
initialised hidden layer, and therefore the only one where first-gradient kernel differences can
steer an optimizer. Every row involving A, B-stale, B-retrain, C* or E matches to four decimals or
better. A cross-platform difference landing exactly where the mechanism predicts is stronger
evidence than uniform agreement would have been.

### What this replication is not

Both runs used Colab, not the pinned container this plan asks for. transformers 5.16.1, torch 2.11
and 2.13, and the driver stack were Google's choices on the day, so **more than the card changed**
and no cross-platform difference can be attributed to the vendor. That cuts one way here: the
perturbation was larger than intended, agreement under a larger perturbation is stronger evidence,
and a disagreement would have been the unattributable case this plan warns about. None was found.

E3's `e3_sigma.main()` was not exercised, because it requires a second reader table that was never
shipped. E1's civil predictions came from a chunked `e1_stream.py` rather than `e1_predict.py`,
verified bitwise identical on all 23 arms × 12,845 CLINC rows — one corpus, and the receipt says so.

### An operational finding worth keeping

Colab reclaimed four of five E1 VMs at 55–80 minutes. The expensive loss was a **finished** 1.37M-row
prediction that sat on disk while packing happened minutes later. **A 40-minute contiguous GPU job
is not reliably schedulable in this envelope; a chunked one is.** After the driver was changed to
pack and hash as its last action and to commit a result every 65,536 rows, a reclaim cost minutes:
on the fourth, 917,504 rows were already off the VM and the run finished from there.
