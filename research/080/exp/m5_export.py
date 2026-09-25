#!/usr/bin/env python3
"""Package exactly what an NVIDIA machine needs to compile and run the PAW rungs. Runs as `augctl`.

A2a and A2b cannot be fitted on gfx1151: the PAW compiler requires an NVIDIA GPU with BF16 support
of Ampere or newer. The maintainer authorized running them on Colab, so this program exports a
bundle and nothing more. It is deliberately the narrowest thing that works.

What goes in the bundle:

  the specs, hashed, so a compile that used different words is detectable
  the FIT examples with their labels, which are public rows and are what a compile learns from
  the CONFIRMATION inputs, ids and text only

What never goes in, and the program refuses rather than filters:

  confirmation labels, from any task

That last line is the whole design. The Colab side compiles the programs, freezes and hashes them,
and runs them over the confirmation inputs to produce actions. It cannot score itself, because it
holds no outcome. The actions come back here and `augctl` scores them against labels that never
left, exactly as E1's prediction and scoring runs were split.

Every row exported is from a public benchmark — BANKING77 CC BY 4.0, CLINC150 CC BY 3.0,
CivilComments CC0 — so this is a transfer of already-public text, and the bundle records that.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import m5_specs

FIT_EXAMPLE_CAP = 2_000  # what a compile reads; the whole fit split is neither needed nor cheap


def digest(payload) -> str:
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, sort_keys=True,
                   separators=(",", ":")).encode("utf-8")).hexdigest()


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def collect(stage: Path, task: str, prefix: str) -> dict:
    """Fit examples with labels, and confirmation inputs without them."""
    fit_inputs = load(stage / f"{prefix}-fit" / "rows.json")
    fit_labels = {row["id"]: row["label"]
                  for row in load(stage / f"{prefix}-fit" / "labels.json")}
    examples = [{"id": row["id"], "text": row["text"], "label": fit_labels[row["id"]]}
                for row in fit_inputs[:FIT_EXAMPLE_CAP]]

    confirmation = load(stage / f"{prefix}-confirmation" / "rows.json")
    leaked = [row for row in confirmation if "label" in row]
    if leaked:
        raise SystemExit(f"{task}: {len(leaked)} confirmation rows carry a label; refusing to "
                         "export. This is a custody failure, not an export problem.")
    inputs = [{"id": row["id"], "text": row["text"]} for row in confirmation]

    return {
        "task": task,
        "spec": m5_specs.SPECS[task],
        "fit_examples": examples,
        "fit_examples_digest": digest(examples),
        "confirmation_inputs": inputs,
        "confirmation_inputs_digest": digest(inputs),
        "confirmation_n": len(inputs),
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--stage", type=Path, default=Path("/srv/aug/stage/parts"))
    parser.add_argument("--task", action="append", required=True, metavar="TASK=PREFIX",
                        help="for example T2a=b77, T2c=civil-m5")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)

    bundle = {
        "experiment": "M5",
        "purpose": "compile and run the PAW rungs (A2a, A2b) on an NVIDIA machine",
        "spec_version": m5_specs.SPEC_VERSION,
        "spec_digest": digest(m5_specs.SPECS),
        "fit_example_cap": FIT_EXAMPLE_CAP,
        "tasks": {},
        "contains_confirmation_labels": False,
        "licences": {
            "BANKING77": "CC BY 4.0", "CLINC150": "CC BY 3.0", "CivilComments": "CC0",
            "note": "Every exported row is from a public benchmark. This is a transfer of "
                    "already-public text, and the confirmation labels are not in it.",
        },
        "what_the_far_side_may_not_do": [
            "It cannot score itself: it holds no confirmation label and no gold answer.",
            "It must freeze and hash each compiled program BEFORE running it over confirmation inputs, and report those hashes.",
            "It must emit one action per confirmation id per arm, and nothing else.",
        ],
    }
    for spec in args.task:
        task, _, prefix = spec.partition("=")
        if task not in m5_specs.SPECS:
            raise SystemExit(f"{task} has no spec in m5_specs.py")
        bundle["tasks"][task] = collect(args.stage, task, prefix)

    # Belt and braces: the bundle is serialized, then re-read and searched for any label key under
    # a confirmation block. A refusal here means the code above changed and this check earned its
    # keep; it costs one pass over a file we are writing anyway.
    text = json.dumps(bundle, ensure_ascii=False)
    reloaded = json.loads(text)
    for task, block in reloaded["tasks"].items():
        if any("label" in row for row in block["confirmation_inputs"]):
            raise SystemExit(f"{task}: a label reached the serialized bundle; refusing to write")

    args.out.write_text(text, encoding="utf-8")
    summary = {
        "spec_version": bundle["spec_version"], "spec_digest": bundle["spec_digest"],
        "tasks": {task: {"fit_examples": len(block["fit_examples"]),
                         "fit_examples_digest": block["fit_examples_digest"],
                         "confirmation_n": block["confirmation_n"],
                         "confirmation_inputs_digest": block["confirmation_inputs_digest"]}
                  for task, block in bundle["tasks"].items()},
        "bytes": args.out.stat().st_size,
        "bundle_sha256": hashlib.sha256(args.out.read_bytes()).hexdigest(),
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
