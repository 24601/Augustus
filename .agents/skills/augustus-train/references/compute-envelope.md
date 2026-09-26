# Compute envelope: measured, and it does not generalize

What hardware a rung needs has no single answer across artifact forms. These figures are first-party
measurements from `research/080/receipts/m5-grading-2026-09-25.md` and the source cards beside it,
on rented Colab cards.

## Two artifacts, opposite constraints

**A fine-tune that outgrows its own preflight.** A LoRA fine-tune printed a 38 GiB requirement and
used **69 GiB** at its own batch of 48, measured at 71,035 MiB of 81,559 on an H100. It OOMed a 40
GB A100 before step 1 and OOMed the 80 GB card on the longest task. Gradient accumulation —
micro-batch 12, accumulation 4, same effective batch, same steps, same examples — brought it to
**24,457 MiB**. The honest requirement is 24 GiB, not 69 and not the 38 it publishes, and the
configuration that fits a mid-range card is not the one it ships with.

**A server that is indifferent to the card.** A 4B decision model served at batch 1 took **328 ms
per row on an L4 and 328 ms on an A100** — identical, because one short forward pass with
single-token option codes is launch-bound rather than FLOP-bound. Merging the LoRA reached 292 ms.
The lever was concurrency: three unmodified replicas on one GPU scaled near-linearly to 8.2 rows/s.

**Conclusion:** measure before renting. A bigger card fixes one of these and does nothing for the
other.

## CPU is a rate, not a yes/no

Same VM, same weights, same prompts, only the device changed: **41.84 rows/s on an L4 against
0.2592 rows/s on CPU, a factor of 161.** The model does run on CPU, which is what its card says. At
that rate a 60,000-row pass takes 64 hours. "Runs on CPU" and "is usable on CPU" are different
claims and only the second needs a number.

## Defaults that cost more than they save

- **`torch.compile`** on one decision engine: 14.30 rows/s against 41.84 without, end to end. About
  six minutes of inductor work per (batch, length) bucket for roughly 1.4× steady state, plus an
  OOM at batch 64.
- **A from-source CUDA build** produced a package with no CUDA backend at all — no
  `libggml-cuda.so`, every layer on CPU — while the project's **prebuilt CUDA wheel** shipped the
  backend and put 29 of 29 layers on the device. `--no-binary` guarantees a fresh compile, not a
  complete one.
- **An installer that silently reuses a cached build.** Two `uv` installs with `GGML_CUDA=on` left
  offload false on an image with `nvcc` present; `pip` with `--no-binary --no-cache-dir --no-deps`
  built it correctly. Same image, same flags, opposite result.

## Inference rates worth budgeting from

Measured on an L4 unless noted, at the option counts stated:

| artifact | 2 options | 77 options |
| --- | --- | --- |
| Logistic head on frozen MiniLM | 831–1,411 rows/s | 400 rows/s |
| Decoder hidden-state readout | 32–67 rows/s | 48 rows/s |
| GLiNER2 fine-tune | 100–563 rows/s | 26 rows/s |
| Compiled 0.6B program (llama.cpp, CUDA) | 22–26 rows/s | 19–20 rows/s |
| 4B decision model, batch 1 | 8–42 rows/s | 2.1 rows/s |
| Zero-label readout with cyclic shifts | 37–61 rows/s | **0.63 rows/s** |

The last row is the price of order-invariance: shifts multiply prefills by the option count, so a
77-option question costs 81 prefills per row.

## Rented-runtime discipline

Reclaimed VMs were routine — one thread lost six, at 20 to 65 minutes, regardless of detachment or
keep-alive. What made losses cost minutes instead of hours:

- write results incrementally, not at the end of a task
- copy them off the VM every few minutes
- resume keyed on a row id, so no row runs twice and none is dropped
- print progress, because a log that only prints on completion cannot tell you how far a dead run got
- hash artifacts before and after every transfer

An expensive artifact — a fine-tuned program, a set of synthesized examples — should leave the VM
the moment it exists. Re-seeding a cache from files costs a copy; regenerating it cost 70 minutes.
