#!/usr/bin/env python3
"""Compile and run M5's PAW rungs on an NVIDIA machine. Written for Colab; holds no label.

A2a and A2b cannot be fitted on tabputer's gfx1151: the PAW compiler requires an NVIDIA GPU with
BF16 support of Ampere or newer. This is the far side of that split. It reads the export bundle,
compiles one program per task per rung, freezes and hashes each program BEFORE it sees a
confirmation input, runs them, and writes actions.

**It cannot score itself.** The bundle carries no confirmation label, so nothing here can compute a
loss, and the actions go back to `augctl` to be graded against labels that never left the host.
That is the same split E1 used between the principal that predicts and the one that grades, and it
is the reason this program can run on a machine nobody controls.

**This program is UNTESTED against the real compiler.** It was written on a machine with no NVIDIA
accelerator and no `paw` package, so its plumbing is verified by `--dry-run` and its compiler calls
are not. Where the compiler's interface differs from what is written here, the honest response is
to report the exact error and fix this file, not to improvise around it on the far side. Every
compile and inference call is isolated in `compile_program` and `run_program` for that reason.

Order of operations, which is the part that matters and must not be rearranged:

  1. verify the bundle hash
  2. compile from the spec and the FIT examples only
  3. freeze the program, hash it, record the hash
  4. only then read confirmation inputs and produce actions
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import subprocess
import sys
import time
from pathlib import Path

RUNGS = ("A2a", "A2b")


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def environment() -> dict:
    """What ran this, recorded because a result from an unnamed machine is not reproducible."""
    report = {"python": sys.version.split()[0], "platform": platform.platform()}
    try:
        import torch
        report["torch"] = torch.__version__
        report["cuda_available"] = torch.cuda.is_available()
        if torch.cuda.is_available():
            properties = torch.cuda.get_device_properties(0)
            report["gpu"] = properties.name
            report["gpu_total_mib"] = properties.total_memory // 2 ** 20
            report["bf16_supported"] = torch.cuda.is_bf16_supported()
    except ImportError:
        report["torch"] = None
    try:
        report["nvidia_smi"] = subprocess.run(
            ["nvidia-smi", "--query-gpu=name,memory.total,driver_version",
             "--format=csv,noheader"], capture_output=True, text=True, timeout=30).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        report["nvidia_smi"] = None
    return report


def render_spec(task: str, spec: dict) -> str:
    """The spec as one text, identical for every rung, so the rungs differ only in artifact form."""
    cost = ", ".join(f"{name} {value}" for name, value in spec["cost"].items())
    return (f"Task: {spec['task']}\n"
            f"Unit of decision: {spec['unit']}\n"
            f"Decision: {spec['decision']}\n"
            f"Answer must be: {spec['options']}\n"
            f"Cost of each outcome: {cost}\n"
            f"Guidance: {spec['guidance']}\n")


def compile_program(rung: str, task: str, spec_text: str, examples: list[dict], workdir: Path):
    """Compile one program. Isolated because it is the only part that is untested here.

    A2a is PAW-standard: compile the spec and examples with the local single-GPU compiler.
    A2b is PAW-ft: an initial local compile, then teacher-generated examples and a fine-tune of the
    0.6B interpreter. The recipe's step 1 posts the spec to the hosted compiler by default; the
    design lock says A2b uses a LOCAL initial compile, so that default must be overridden and the
    override recorded. If it cannot be overridden, stop and report it rather than posting.
    """
    raise NotImplementedError(
        f"{rung} compilation is not implemented against the real compiler interface. "
        "Clone github.com/programasweights/compiler, read its entry point, and fill this in; "
        "report the interface you found so the file can be corrected rather than patched locally.")


def run_program(program, inputs: list[dict]) -> dict:
    """One action per confirmation id. Also isolated, and also untested."""
    raise NotImplementedError(
        "inference is not implemented against the real runtime. The SDK's local path is llama.cpp "
        "over GGUF-LoRA; record the call you used.")


def dry_run_program(rung: str, task: str, spec_text: str, examples: list[dict]):
    """A stand-in that exercises every step except the two that need the compiler.

    It is deliberately useless as a decision: it returns the most common fit label for every row.
    That makes an accidental dry-run result obvious rather than plausible, which is the property
    worth having in a placeholder.
    """
    counts = {}
    for example in examples:
        counts[example["label"]] = counts.get(example["label"], 0) + 1
    majority = max(counts, key=lambda label: (counts[label], str(label)))
    body = json.dumps({"rung": rung, "task": task, "spec": spec_text, "constant": majority},
                      sort_keys=True)
    return {"kind": "dry-run placeholder", "constant": majority, "body": body}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--expect-sha256", required=True,
                        help="the bundle hash recorded on the host before it was transferred")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--workdir", type=Path, default=Path("./m5-work"))
    parser.add_argument("--dry-run", action="store_true",
                        help="exercise every step except the compile and the inference")
    args = parser.parse_args(argv)

    actual = sha256_of(args.bundle)
    if actual != args.expect_sha256:
        parser.exit(2, f"error: bundle sha256 is {actual}, expected {args.expect_sha256}; "
                       "refusing to run on a bundle that is not the one that was exported\n")
    bundle = json.loads(args.bundle.read_text(encoding="utf-8"))
    if bundle.get("contains_confirmation_labels"):
        parser.exit(2, "error: the bundle declares that it contains confirmation labels; "
                       "this program must never hold one\n")

    args.workdir.mkdir(parents=True, exist_ok=True)
    started = time.time()
    report = {
        "experiment": "M5",
        "side": "compile and predict; holds no label and cannot score",
        "bundle_sha256": actual,
        "spec_version": bundle["spec_version"],
        "spec_digest": bundle["spec_digest"],
        "environment": environment(),
        "dry_run": args.dry_run,
        "programs": {},
        "actions": {},
    }

    for task, block in bundle["tasks"].items():
        spec_text = render_spec(task, block["spec"])
        examples = block["fit_examples"]
        for rung in RUNGS:
            key = f"{task}|{rung}"
            if args.dry_run:
                program = dry_run_program(rung, task, spec_text, examples)
                frozen = json.dumps(program, sort_keys=True).encode("utf-8")
            else:
                program = compile_program(rung, task, spec_text, examples, args.workdir)
                frozen = Path(program).read_bytes() if isinstance(program, (str, Path)) \
                    else json.dumps(program, sort_keys=True).encode("utf-8")

            # Frozen and hashed BEFORE a confirmation input is read. The order is the control.
            program_sha = hashlib.sha256(frozen).hexdigest()
            report["programs"][key] = {
                "rung": rung, "task": task, "program_sha256": program_sha,
                "bytes": len(frozen), "fit_examples_used": len(examples),
                "spec_sha256": hashlib.sha256(spec_text.encode("utf-8")).hexdigest(),
                "frozen_before_confirmation": True,
            }

            inputs = block["confirmation_inputs"]
            if args.dry_run:
                actions = {row["id"]: program["constant"] for row in inputs}
            else:
                actions = run_program(program, inputs)
            if set(actions) != {row["id"] for row in inputs}:
                parser.exit(2, f"error: {key} produced {len(actions)} actions for "
                               f"{len(inputs)} inputs; every id needs exactly one action\n")
            report["actions"][key] = actions

    report["wall_clock_s"] = round(time.time() - started, 1)
    report["limits"] = [
        "This side holds no confirmation label and computes no loss. Anything resembling a score here would be a bug.",
        "Every program was frozen and hashed before any confirmation input was read; the hashes are above.",
        "A dry run returns a constant, the majority fit label, so an accidental dry-run result is obvious rather than plausible.",
        "The environment block records the machine because a result from an unnamed machine is not reproducible.",
    ]
    args.out.write_text(json.dumps(report), encoding="utf-8")
    summary = {k: v for k, v in report.items() if k != "actions"}
    summary["action_counts"] = {key: len(value) for key, value in report["actions"].items()}
    print(json.dumps(summary, indent=2))
    print(f"\nactions sha256: {sha256_of(args.out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
