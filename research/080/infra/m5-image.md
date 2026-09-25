# The M5 image, as a recipe rather than a tarball (2026-09-25)

The second pinned image for M5. The first is untouched and stays the image E1 and E3 ran in.

| Item | Value |
| --- | --- |
| Base | `docker.io/vllm/vllm-openai-rocm@sha256:e5e47f6aaab675c252c381f0dac237b31b10d87bb74d092b07fb4065efd7f5a1` |
| Built image | `localhost/aug-m5-setfit:20260925`, digest `sha256:0692bcaeffd6a2e84aaece95d597929f072d014255a6cad1e1dafcc01df11dd2`, 35.8 GB |
| Method | four wheels fetched on the host through the proxy, then installed **offline** inside the new image with `--no-deps --no-index` |
| Build principal | `augexp`, rootless |
| `pip freeze` | 267 lines, sha256 `df3bb8ab…`, at `/srv/aug/receipts/m5-image-20260925T0133Z/pip-freeze.txt` |

## The four wheels, which are the whole delta

| Wheel | sha256 |
| --- | --- |
| `setfit-1.2.0-py3-none-any.whl` | `dcf9292f073f47252c3fea73b141c4f43dc1d01789e0c8e2de017337e0428e34` |
| `scikit_learn-1.9.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl` | `e5d7b18a5b9dca241a74695f3275fa4c895a9dadc72b3d8df5fa9d1083c9b83e` |
| `sentence_transformers-6.1.0-py3-none-any.whl` | `eb8122f4d180f552eda26dc3d77e84e8c11dc2b1d456a406b9f24abb70ceeadd` |
| `threadpoolctl-3.7.0-py3-none-any.whl` | `cd8b60b5641b45c67bbf73c64c843235fc2d8a480c87389f52f5dbee893b86be` |

`threadpoolctl` was the only transitive dependency not already present. **No `torch`, no `triton`,
no `nvidia-*` package was installed**, which was the point of the exercise.

## Why a recipe and not a tarball

`podman save` of a 35.8 GB image stalled twice — about 77 MB written, then no growth, inherited
idle scheduling that a `renice` did not fix; a redirected save reached roughly 21 GB and stalled
the same way. Both partial files were deleted rather than hashed, and no tar sits beside the
first one.

That is not a gap worth forcing. **A base digest plus four wheel hashes and an offline
`--no-deps --no-index` install is a stronger record than a 36 GB opaque archive**: it is exactly
reproducible, it is diffable, it fits in a commit, and it states precisely what changed. The
tarball's only advantage is surviving a wipe of the rootless store without a proxy window, and
rebuilding from these four wheels costs one short window.

The risk this accepts, stated plainly: if `augexp`'s rootless store is wiped, the image is gone
until it is rebuilt. Nothing depends on the image that cannot be rebuilt from this page.

## Verification inside the built image, with GPU devices mounted

- `torch` **2.12.0+git6bbd260**, imports, `cuda` True — the ROCm build, not a PyPI CUDA wheel
- `transformers` **5.16.1**, imports
- `vllm` metadata **0.29.0+rocm723**; the freeze line is still the local wheel,
  `vllm @ file:///install/vllm-0.29.0+rocm723-cp312-cp312-linux_x86_64.whl`. `vllm.__version__`
  prints the shorter `0.29.0`, which is not treated as evidence of a replacement
- `triton` is still the local `3.7.1+gitf0b55c07` wheel
- `setfit`, `sklearn` 1.9.1 and `sentence_transformers` 6.1.0 all import

A first `vllm` import without GPU devices failed with "No CUDA GPUs are available" after printing
the three versions. That is the probe lacking a device, not a version move; the GPU-mounted rerun
imported cleanly.

## What this image does and does not unblock

It makes **R3a**, M5's comparator, reachable — `setfit` was the whole of its miss. It does nothing
for A2a and A2b, which are unreachable on this accelerator in principle
(`sources/paw-rap-2026-09-23.md`), and nothing for R1 and R2b, which need Qwen3.5-2B-Base staged.

## The trap this build was shaped to avoid

A dependency resolution that pins `torch==2.12.0` from PyPI gets a **stock CUDA wheel** with
`cuda-toolkit`, `triton` and the `nvidia-*` CUDA 13 packages. That is a different artifact from
the image's `2.12.0+git6bbd260` ROCm build despite an identical version string, and installing it
would have replaced the environment E1 and E3 ran in while looking, in a log, like nothing
changed. Stock `vllm 0.29.0` also depends on `torch==2.13.0`, so constraining the image's local
`+rocm723` build against the PyPI package conflicts immediately. Hence `--no-deps`, an explicit
transitive list, and an offline install.
