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
