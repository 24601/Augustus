#!/usr/bin/env python3
"""M5: partition the real-text tasks, publish INPUTS, retain labels. Runs as `augctl`.

Three tasks, and only two of them need partitioning here:

  T2a  BANKING77, 77-way routing with an abstain option. Partitioned from the two upstream CSVs
       W2 acquired, which together hold 13,083 human-written queries.
  T2b  CLINC150 plus OOS. **Reuses E1's seeded partition unchanged** — the design lock says so, and
       re-splitting it would silently create a second population with the same name.
  T2c  CivilComments, from the M5 pool M4 already published, which is disjoint from E1's splits.

The same two-principal split as E1 and E3, for the same reason: the label is what the acceptance
gate scores against, so the training principal must not hold the confirmation labels and cannot
score itself.

The one judgement this program makes, and it is fixed here rather than later: T2c's confirmation is
published at its full 60,000, and the analysis lock decides by the n(σ̂) rule how many of them are
read. Publishing 40,000 and expanding later would mean deciding the population after seeing a
sigma-hat; publishing 60,000 and fixing n before reading does not, because the order is seeded and
the prefix is determined before any label is touched.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
import unicodedata
from pathlib import Path

SEED = 80_501
BANKING_CONFIRMATION = 6_000
BANKING_CALIBRATION = 2_000
CIVIL_CONFIRMATION = 60_000
CIVIL_CALIBRATION = 15_000
BANKING_EXPECTED = 13_083


def normalize(text: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def digest(rows: list[dict]) -> str:
    payload = json.dumps(rows, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def read_banking(paths: list[Path]) -> list[dict]:
    """The upstream CSVs, in the order given, with ids that record which file a row came from."""
    rows = []
    for path in paths:
        with path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None or "text" not in reader.fieldnames:
                raise SystemExit(f"{path.name}: expected a text column, found {reader.fieldnames}")
            label_field = "category" if "category" in reader.fieldnames else reader.fieldnames[-1]
            for index, row in enumerate(reader):
                rows.append({"id": f"b77-{path.stem}-{index}",
                             "text": row["text"], "label": row[label_field]})
    return rows


def split(rows: list[dict], confirmation_n: int, calibration_n: int, seed: int) -> dict:
    """Seeded, and confirmation is drawn first so its size never depends on what is left over."""
    deduped, seen = [], set()
    for row in rows:
        key = normalize(row["text"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(row)
    order = list(range(len(deduped)))
    random.Random(seed).shuffle(order)
    shuffled = [deduped[i] for i in order]
    confirmation = shuffled[:confirmation_n]
    calibration = shuffled[confirmation_n:confirmation_n + calibration_n]
    fit = shuffled[confirmation_n + calibration_n:]
    if not fit:
        raise SystemExit("nothing left to fit on; the confirmation and calibration sizes are "
                         f"{confirmation_n} and {calibration_n} against {len(deduped)} rows")
    return {"confirmation": confirmation, "calibration": calibration, "fit": fit,
            "rows_in": len(rows), "rows_after_dedup": len(deduped),
            "exact_duplicates_dropped": len(rows) - len(deduped)}


def publish(task: str, parts: dict, stage: Path, labels: Path) -> dict:
    summary = {}
    for name in ("fit", "calibration", "confirmation"):
        subset = parts[name]
        inputs = [{"id": row["id"], "text": row["text"]} for row in subset]
        held = [{"id": row["id"], "label": row["label"]} for row in subset]
        target = stage / f"{task}-{name}"
        try:
            target.mkdir(parents=True, exist_ok=True)
        except PermissionError:
            # The staging tree is root-owned and augctl holds execute only, by design. Say what
            # has to happen rather than emitting a traceback the operator has to decode.
            raise SystemExit(
                f"cannot create {target}: the staging tree is root-owned and this principal has "
                "execute only. Have root precreate the six partition directories under the same "
                "custody as the other parts, then rerun. Do not widen augctl's access to the tree.")
        (target / "rows.json").write_text(json.dumps(inputs, ensure_ascii=False), encoding="utf-8")
        labels.mkdir(parents=True, exist_ok=True)
        # Fit and calibration labels are published too: the training principal needs them. Only the
        # confirmation labels are withheld, which is the whole of the custody argument.
        if name == "confirmation":
            (labels / f"{task}-confirmation-labels.json").write_text(
                json.dumps(held, ensure_ascii=False), encoding="utf-8")
        else:
            (target / "labels.json").write_text(json.dumps(held, ensure_ascii=False),
                                                encoding="utf-8")
        summary[name] = {"rows": len(inputs), "inputs_digest": digest(inputs),
                         "labels_digest": digest(held),
                         "labels_location": "augctl only" if name == "confirmation" else "staged"}
    return summary


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--banking-csv", type=Path, action="append", required=True,
                        help="the upstream BANKING77 CSVs, train then test")
    parser.add_argument("--civil-pool", type=Path, required=True,
                        help="the published civil-m5_pool rows.json, which carries labels")
    parser.add_argument("--stage", type=Path, required=True)
    parser.add_argument("--labels", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args(argv)

    banking = read_banking(args.banking_csv)
    if len(banking) != BANKING_EXPECTED:
        raise SystemExit(f"expected {BANKING_EXPECTED} BANKING77 rows, read {len(banking)}; "
                         "W2 recorded 10,003 train and 3,080 test and this is not that")
    banking_parts = split(banking, BANKING_CONFIRMATION, BANKING_CALIBRATION, SEED)

    pool = json.loads(args.civil_pool.read_text(encoding="utf-8"))
    if any("label" not in row for row in pool):
        raise SystemExit("the civil pool has no labels; M5 needs the labelled pool, not the inputs")
    civil = [{"id": row["id"], "text": row["text"], "label": row["label"]} for row in pool]
    civil_parts = split(civil, CIVIL_CONFIRMATION, CIVIL_CALIBRATION, SEED + 1)

    manifest = {
        "experiment": "M5",
        "seed": SEED,
        "tasks": {
            "T2a": {"corpus": "BANKING77", "unit": "one query",
                    "cost": {"misroute": 1, "abstain": 0.3, "correct": 0},
                    **{k: v for k, v in banking_parts.items()
                       if k in ("rows_in", "rows_after_dedup", "exact_duplicates_dropped")},
                    "partitions": publish("b77", banking_parts, args.stage, args.labels)},
            "T2b": {"corpus": "CLINC150 + OOS", "unit": "one query",
                    "partitions": "reuses E1's seeded CLINC partition unchanged; not re-split here",
                    "note": "Re-splitting would create a second population with the same name."},
            "T2c": {"corpus": "CivilComments, the E1-disjoint M5 pool", "unit": "one comment",
                    "cost": {"c_fp": 1, "c_fn": 4},
                    **{k: v for k, v in civil_parts.items()
                       if k in ("rows_in", "rows_after_dedup", "exact_duplicates_dropped")},
                    "partitions": publish("civil-m5", civil_parts, args.stage, args.labels)},
        },
        "limits": [
            "T2c's confirmation is published at its full 60,000. The analysis lock fixes how many are read by the n(sigma-hat) rule over the seeded order, before any confirmation label has been SCORED against a prediction. This program does read labels, because holding them back is its job; the claim is about the order of the split being fixed independently of any outcome, not about labels being untouched.",
            "Only confirmation labels are withheld. Fit and calibration labels are staged, because the training principal needs them and withholding them would prevent the experiment rather than protect it.",
            "Deduplication is on exact normalized text and does not catch paraphrases.",
            "T2b is E1's partition. Its confirmation labels already sit with augctl and are not rewritten here.",
        ],
    }
    args.manifest.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    print(f"\nmanifest sha256: {hashlib.sha256(args.manifest.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
