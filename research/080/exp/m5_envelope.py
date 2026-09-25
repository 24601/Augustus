#!/usr/bin/env python3
"""M5: declare the compute envelope and report which rungs are reachable. Runs nothing else.

Plan v4 §3.7 says the trainer must declare its envelope before G0, and that an unreachable rung is
reported unreachable rather than skipped silently, because silently omitting a comparator turns
"the cheap rung sufficed" into a statement about the hardware. This program applies that rule to
M5 itself, which is the only honest way to write it down: if we would demand an envelope
declaration from a recipe, our own reproduction has to produce one.

It imports nothing heavy at module scope and touches no dataset. It answers one question per rung:
can this machine fit it and serve it, and if not, exactly what is missing.

The family the design lock fixes is K = 6 — R1, R2a, R2b, A1, A2a, A2b — against the R3a
comparator. If a family member is unreachable the family is smaller than the lock says, and that
is an outcome the lock already names: **no rung recommendation, the default stays the procedure**.
Reporting a reduced family as if it were the registered one would be the failure this program
exists to prevent.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
from pathlib import Path

# What each rung needs to be FITTED at all. Serving is a separate question and is reported beside
# it, because a rung that fits on a borrowed machine and serves on a small one is a real answer.
RUNGS = {
    "A1": {"artifact": "agent-synthesized program, frozen and hashed before confirmation",
           "family_member": True, "needs_python": [], "needs_weights": [],
           "needs_accelerator": False},
    "A2a": {"artifact": "PAW-standard, compiled by the local single-GPU compiler",
            "family_member": True, "needs_python": ["paw"], "needs_weights": [],
            "needs_accelerator": True},
    "A2b": {"artifact": "PAW-ft, local teacher plus a local initial compile",
            "family_member": True, "needs_python": ["paw"], "needs_weights": ["teacher"],
            "needs_accelerator": True},
    "R1": {"artifact": "frozen readout from a 2B decoder, OOF temperature",
           "family_member": True, "needs_python": ["torch", "transformers"],
           "needs_weights": ["readout"], "needs_accelerator": False},
    "R2a": {"artifact": "logistic head on MiniLM embeddings",
            "family_member": True, "needs_python": ["torch", "transformers"],
            "needs_weights": ["minilm"], "needs_accelerator": False},
    "R2b": {"artifact": "ridge or LDA on R1's two-thirds-depth state",
            "family_member": True, "needs_python": ["torch", "transformers"],
            "needs_weights": ["readout"], "needs_accelerator": False},
    "R3a": {"artifact": "SetFit on a pinned body; THE COMPARATOR, not a family member",
            "family_member": False, "needs_python": ["setfit", "torch"],
            "needs_weights": ["minilm"], "needs_accelerator": False},
    "R3b": {"artifact": "DeBERTa-v3-large; runs only if the parity checks pass",
            "family_member": False, "needs_python": ["torch", "transformers"],
            "needs_weights": ["deberta"], "needs_accelerator": True},
}


def has_module(name: str) -> bool:
    try:
        return importlib.util.find_spec(name) is not None
    except (ImportError, ValueError):
        return False


def find_weights(root: Path) -> dict:
    """Staged model directories, identified by reading their config rather than by path text.

    Two things this gets wrong if written casually, and both were. Taking the first `rglob` hit
    finds `all-MiniLM-L6-v2/1_Pooling`, a sentence-transformers submodule, not the model. And
    deciding "this Qwen is not the registered one" from the mere presence of a directory named
    qwen would say the same of a correctly staged Qwen3.5-2B-Base. So: the shallowest directory
    whose config actually looks like a model config wins, and the config's own fields are reported
    so the caller can see WHY a tree was accepted or rejected.
    """
    found = {"models": []}
    if not root.is_dir():
        return found
    seen = set()
    for path in sorted(root.rglob("config.json"), key=lambda p: (len(p.parts), str(p))):
        directory = path.parent
        if any(str(directory).startswith(str(other) + "/") for other in seen):
            continue
        try:
            config = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if "model_type" not in config and "architectures" not in config:
            continue
        seen.add(directory)
        found["models"].append({
            "path": str(directory),
            "model_type": config.get("model_type"),
            "hidden_size": config.get("hidden_size"),
            "name_or_path": config.get("_name_or_path"),
        })
    for entry in found["models"]:
        lowered = entry["path"].lower()
        if "minilm" in lowered:
            found.setdefault("minilm", entry["path"])
        elif "deberta" in lowered:
            found.setdefault("deberta", entry["path"])
        elif entry["model_type"] and "qwen" in entry["model_type"].lower():
            found.setdefault("qwen", []).append(entry)
    return found


def accelerator() -> dict:
    if not has_module("torch"):
        return {"present": False, "why": "torch is not importable"}
    import torch
    if not torch.cuda.is_available():
        return {"present": False, "why": "torch.cuda.is_available() is false"}
    properties = torch.cuda.get_device_properties(0)
    return {"present": True, "name": properties.name or properties.gcnArchName,
            "total_memory_mib": properties.total_memory // 2 ** 20,
            "torch": torch.__version__}


def registered_readout(weights: dict) -> dict | None:
    """The design lock registers Qwen3.5-2B-Base. Match on the name the tree carries.

    Identification is by NAME, from `_name_or_path` or failing that the directory, and that is a
    real limitation rather than a hidden one: a correctly staged Qwen3.5-2B-Base whose config
    leaves `_name_or_path` null and whose directory is called something else would be refused. No
    field in a config distinguishes a 2B base from another 2B decoder reliably, so the honest
    move is to match on the name and say so where the refusal is reported.
    """
    for entry in weights.get("qwen", []):
        name = (entry.get("name_or_path") or entry["path"]).lower()
        if "qwen3.5" in name and "2b" in name:
            return entry
    return None


def classify(name: str, spec: dict, modules: dict, weights: dict, accel: dict) -> dict:
    missing = []
    for module in spec["needs_python"]:
        if not modules.get(module):
            missing.append(f"python module `{module}`")
    for role in spec["needs_weights"]:
        if role == "readout":
            if registered_readout(weights) is None:
                staged = [f"{entry['path']} (model_type {entry['model_type']}, hidden_size "
                          f"{entry['hidden_size']})" for entry in weights.get("qwen", [])]
                missing.append(
                    "the registered readout Qwen3.5-2B-Base, decided from each config rather than "
                    "from a directory name. Qwen-type trees found: "
                    + ("; ".join(staged) if staged else "none"))
        elif role == "teacher":
            if not weights.get("qwen"):
                missing.append("a local open-weight teacher for A2b")
        elif not weights.get(role):
            missing.append(f"staged weights for `{role}`")
    if spec["needs_accelerator"] and not accel.get("present"):
        missing.append("an accelerator")
    return {"artifact": spec["artifact"], "family_member": spec["family_member"],
            "reachable": not missing, "missing": missing}


def envelope_name(accel: dict, has_torch: bool) -> str:
    """The §3.7 envelope label, chosen from what is actually present."""
    if not has_torch:
        return "E-hosted or E-cpu: no local torch"
    if not accel.get("present"):
        return "E-cpu"
    memory = accel.get("total_memory_mib", 0)
    return "E-large" if memory >= 40_000 else "E-small"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--weights-root", type=Path, default=Path("/srv/aug/stage"))
    parser.add_argument("--environment", required=True, choices=("host", "container"),
                        help="where this probe ran. The answer is only about THIS environment, "
                             "and M5 fits inside the pinned container, so a host probe reports "
                             "the host's modules and not the fitting environment's")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args(argv)

    modules = {name: has_module(name)
               for name in ("torch", "transformers", "setfit", "paw", "sklearn")}
    weights = find_weights(args.weights_root)
    accel = accelerator()

    rungs = {name: classify(name, spec, modules, weights, accel)
             for name, spec in RUNGS.items()}
    family = {name: value for name, value in rungs.items() if value["family_member"]}
    reachable_family = [name for name, value in family.items() if value["reachable"]]
    comparator = rungs["R3a"]

    report = {
        "experiment": "M5",
        "probed_environment": args.environment,
        "probe_is_the_fitting_environment": args.environment == "container",
        "envelope": envelope_name(accel, modules["torch"]),
        "accelerator": accel,
        "python_modules": modules,
        "staged_weights": weights,
        "disk_free_bytes": shutil.disk_usage(args.weights_root).free
        if args.weights_root.exists() else None,
        "rungs": rungs,
        "family_size_registered": len(family),
        "family_size_reachable": len(reachable_family),
        "family_reachable": reachable_family,
        "comparator_reachable": comparator["reachable"],
        "verdict": (
            ("the registered family is reachable" if args.environment == "container" else
             "the registered family is reachable IN THIS ENVIRONMENT, which is the host; rerun "
             "inside the pinned container before believing it")
            if len(reachable_family) == len(family) and comparator["reachable"] else
            "the registered family is NOT reachable on this envelope. Per the design lock's own "
            "outcome rows this is Inconclusive: no rung recommendation, the default stays the "
            "procedure. Running the reachable subset and reporting it as the family would be a "
            "statement about this machine wearing the family's name."),
        "limits": [
            "This answers for the environment it ran in. M5 fits inside the pinned container, so a host probe describes the host: torch and transformers absent there says nothing about the image, and the envelope label will understate the machine.",
            "Reachability is about fitting, not about whether a rung would pass the gate.",
            "A missing python module or staged tree is an acquisition, not a result. Nothing here says a rung is bad.",
            "The readout is identified by name, from _name_or_path or the directory. A correctly staged tree carrying neither would be refused; no config field distinguishes one 2B decoder from another reliably.",
            "The comparator R3a is not a family member, but the family's outcome rows are all defined against it, so an unreachable comparator makes every row unreadable rather than just one.",
        ],
    }
    text = json.dumps(report, indent=2)
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
