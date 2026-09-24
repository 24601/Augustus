#!/usr/bin/env python3
"""Partition the E1 corpora exactly as the design lock says, and hash the result.

Runs as `augctl` on the host, never in a container, because it is the step that
separates confirmation labels from everything else. It reads the acquired
dataset, applies the locked seeds and proportions, and writes:

  * fit, fit-B, calibration and the M5 pool WITH labels, for augexp;
  * confirmation INPUTS with the label column removed, for augexp;
  * confirmation LABELS, which stay under /srv/aug/ctl.

The partition is deterministic given the seed, so the split manifest hash in
the analysis lock is reproducible from this file plus the acquisition manifest.

Dedup happens BEFORE partitioning, on exact normalized text, because a
duplicate that straddles the confirmation boundary is a leak no downstream
audit can undo.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import unicodedata
from pathlib import Path

# Fixed by the E1 design lock. Changing any of these changes the experiment.
SEED_PARTITION = 80_101
CIVIL = {"fit": 200_000, "fit_b": 200_000, "calibration": 100_000, "m5_pool": 100_000}
CLINC = {"fit": 8_000, "calibration": 3_000}


def normalize(text: str) -> str:
    """Exact-normalized text for dedup: NFKC, collapsed whitespace, casefolded.

    Deliberately conservative. It does not stem, translate or paraphrase,
    because a dedup rule that merges genuinely different rows silently shrinks
    the population instead of protecting it.
    """
    folded = unicodedata.normalize("NFKC", text).casefold()
    return " ".join(folded.split())


def dedup(rows, text_key: str):
    """Keep the first occurrence of each normalized text. Returns kept rows and
    the number dropped, because the drop count belongs in the manifest."""
    seen = set()
    kept = []
    dropped = 0
    for row in rows:
        key = normalize(row[text_key])
        if key in seen:
            dropped += 1
            continue
        seen.add(key)
        kept.append(row)
    return kept, dropped


def partition(rows, sizes: dict, seed: int) -> dict:
    """Seeded, equal-probability partition. The remainder is confirmation."""
    order = list(range(len(rows)))
    random.Random(seed).shuffle(order)
    out = {}
    cursor = 0
    for name, size in sizes.items():
        if cursor + size > len(order):
            raise ValueError(f"{name} needs {size} rows; only {len(order) - cursor} remain")
        out[name] = [rows[i] for i in order[cursor:cursor + size]]
        cursor += size
    out["confirmation"] = [rows[i] for i in order[cursor:]]
    return out


def digest(rows) -> str:
    payload = json.dumps(rows, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def build(rows, text_key: str, label_key: str, sizes: dict, seed: int) -> dict:
    kept, dropped = dedup(rows, text_key)
    parts = partition(kept, sizes, seed)
    manifest = {
        "rows_in": len(rows),
        "rows_after_dedup": len(kept),
        "exact_duplicates_dropped": dropped,
        "seed": seed,
        "text_key": text_key,
        "label_key": label_key,
        "partitions": {},
    }
    for name, part in parts.items():
        manifest["partitions"][name] = {"rows": len(part), "sha256": digest(part)}
    # The confirmation partition is split here, not later: the inputs and the
    # labels are different artifacts with different custody from this point on.
    confirmation_inputs = [{k: v for k, v in row.items() if k != label_key}
                           for row in parts["confirmation"]]
    confirmation_labels = [{"id": row["id"], label_key: row[label_key]}
                           for row in parts["confirmation"]]
    manifest["partitions"]["confirmation_inputs"] = {
        "rows": len(confirmation_inputs), "sha256": digest(confirmation_inputs),
        "label_column_removed": label_key}
    manifest["partitions"]["confirmation_labels"] = {
        "rows": len(confirmation_labels), "sha256": digest(confirmation_labels),
        "custody": "augctl only"}
    leaked = sorted({k for row in confirmation_inputs if label_key in row for k in [label_key]})
    if leaked:
        raise ValueError(f"the label column survived the split: {leaked}")
    return {"manifest": manifest, "parts": parts,
            "confirmation_inputs": confirmation_inputs,
            "confirmation_labels": confirmation_labels}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--rows", type=Path, required=True,
                        help="JSON list of rows, each with id, the text key and the label key")
    parser.add_argument("--corpus", choices=("civil", "clinc"), required=True)
    parser.add_argument("--text-key", default="text")
    parser.add_argument("--label-key", default="label")
    parser.add_argument("--stage", type=Path, default=Path("/srv/aug/stage/parts"))
    parser.add_argument("--ctl", type=Path, default=Path("/srv/aug/ctl/labels"))
    parser.add_argument("--manifest", type=Path, help="where to write the split manifest")
    parser.add_argument("--dry-run", action="store_true",
                        help="report the manifest and write nothing")
    args = parser.parse_args(argv)

    rows = json.loads(args.rows.read_text(encoding="utf-8"))
    sizes = CIVIL if args.corpus == "civil" else CLINC
    built = build(rows, args.text_key, args.label_key, sizes, SEED_PARTITION)
    manifest = built["manifest"]
    manifest["corpus"] = args.corpus

    if not args.dry_run:
        for name, part in built["parts"].items():
            if name == "confirmation":
                continue  # published as inputs and labels, separately
            target = args.stage / f"{args.corpus}-{name}"
            target.mkdir(parents=True, exist_ok=True)
            (target / "rows.json").write_text(json.dumps(part, indent=0, sort_keys=True),
                                              encoding="utf-8")
        target = args.stage / f"{args.corpus}-confirmation-inputs"
        target.mkdir(parents=True, exist_ok=True)
        (target / "rows.json").write_text(
            json.dumps(built["confirmation_inputs"], indent=0, sort_keys=True), encoding="utf-8")
        args.ctl.mkdir(parents=True, exist_ok=True)
        (args.ctl / f"{args.corpus}-confirmation-labels.json").write_text(
            json.dumps(built["confirmation_labels"], indent=0, sort_keys=True), encoding="utf-8")

    text = json.dumps(manifest, indent=2)
    if args.manifest:
        args.manifest.write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
