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

# The compiler's interface, read from programasweights/compiler source rather than guessed.
COMPILER_REPO = "https://github.com/programasweights/compiler"
COMPILER_CHECKPOINTS = {
    "standard": {"compiler": "programasweights/paw-4b-qwen3-0.6b", "revision": "20260407",
                 "interpreter": "Qwen/Qwen3-0.6B", "runtime_id": "qwen3-0.6b-q6_k"},
}
REFERENCE_MODEL = ("Qwen/Qwen3-4B-Instruct-2507", "cdbee75f17c01a7cc42f958dc650907174af0554")
# `compile.py` takes ONE spec string and has no examples argument: the reference model invents its
# own 3-6 pairs, and anything we want it to see must be inside that string. The prompt budget is
# 5,120 tokens, so a PAW program sees a handful of examples where R2a fits on thousands. That
# asymmetry is a property of the artifact form, not a shortcut taken here, and the count used is
# recorded so the comparison is read with it in view.
SPEC_EXAMPLE_COUNT = 24


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


def render_spec(task: str, spec: dict, options: list[str] | None = None) -> str:
    """The spec as one text, identical for every rung, so the rungs differ only in artifact form.

    `options` is the bundle's enumerated answer set, written out verbatim. Without it the spec
    names its options by reference — "one of the 77 BANKING77 intent labels" — which an arm that
    reads fit rows resolves for free and a compiled program cannot resolve at all.
    """
    cost = ", ".join(f"{name} {value}" for name, value in spec["cost"].items())
    text = (f"Task: {spec['task']}\n"
            f"Unit of decision: {spec['unit']}\n"
            f"Decision: {spec['decision']}\n"
            f"Answer must be: {spec['options']}\n"
            f"Cost of each outcome: {cost}\n"
            f"Guidance: {spec['guidance']}\n")
    if options:
        listed = "\n".join(f"- {option}" for option in options)
        text += (f"The answer must be exactly one of these {len(options)}, copied character for "
                 f"character, with nothing else in the output:\n{listed}\n")
    return text


def spec_with_examples(spec_text: str, examples: list[dict]) -> str:
    """The spec string the compiler actually receives.

    `compile.py` has no examples argument. Its reference model is prompted to invent its own 3-6
    input/output pairs and is told not to copy verbatim any that the spec contains. So examples
    reach the compiler only by being written into the spec, and only a few of them fit inside the
    5,120-token prompt budget. This is the honest shape of the A2 rungs and it is why their
    comparison against R2a is a comparison between artifact forms rather than between training
    sets.
    """
    lines = [spec_text, "", f"Worked examples ({len(examples)}), input then answer:"]
    for example in examples:
        text = " ".join(str(example["text"]).split())[:300]
        lines.append(f"- {text} -> {example['label']}")
    return "\n".join(lines)


def compile_program(rung: str, task: str, spec_text: str, examples: list[dict], workdir: Path):
    """Compile one program with the LOCAL single-GPU compiler. Returns the .paw path.

    `compile.py` never posts the spec: its only network traffic is a Hugging Face snapshot
    download of the reference model, the compiler checkpoint and the interpreter tokenizer. That
    is what makes A2a's local compile the one the design lock asks for.

    A2b is a different repository whose step 1 posts the spec to the hosted compiler by default.
    The design lock requires a local initial compile, so A2b is not implemented here rather than
    implemented with the default it forbids.
    """
    if rung != "A2a":
        raise NotImplementedError(
            "A2b is the compile-by-training recipe, whose first step posts the spec to the hosted "
            "compiler unless overridden, and which needs about 38 GiB. It is deliberately not "
            "implemented here; running it with the hosted default would violate the design lock.")

    checkout = workdir / "compiler"
    if not (checkout / "compile.py").exists():
        raise SystemExit(f"clone {COMPILER_REPO} to {checkout} before compiling")

    spec_file = workdir / f"{task}-{rung}.spec.txt"
    spec_file.write_text(spec_with_examples(spec_text, examples[:SPEC_EXAMPLE_COUNT]),
                         encoding="utf-8")
    output = workdir / f"{task}-{rung}.paw"
    result = subprocess.run(
        [sys.executable, "compile.py", "--spec-file", str(spec_file),
         "--compiler", "standard", "--output", str(output)],
        cwd=checkout, capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(f"{task} {rung}: compile.py exited {result.returncode}\n"
                         f"{result.stdout[-2000:]}\n{result.stderr[-2000:]}")
    if not output.exists():
        raise SystemExit(f"{task} {rung}: compile.py reported success but wrote no {output}")
    return output


def run_program(program, inputs: list[dict]) -> dict:
    """One action per confirmation id, through the SDK's local llama.cpp path.

    `offline=True` forbids all network, including the shared base-GGUF download, so the base must
    already be cached. That is deliberate: a run that could reach the network could also reach the
    hosted interpreter, and this side is supposed to be unable to do anything but predict.
    """
    import programasweights as paw

    function = paw.function(str(program), offline=True)
    return {row["id"]: function(row["text"]).strip() for row in inputs}


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
        spec_text = render_spec(task, block["spec"], block.get("options_enumerated"))
        # Worked examples are written in the same wording the options use, so the program is not
        # shown two spellings of one answer and asked to pick the graded one.
        surface = block.get("answer_surface") or {}
        examples = [{**example, "label": surface.get(str(example["label"]), example["label"])}
                    for example in block["fit_examples"]]
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
