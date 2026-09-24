#!/usr/bin/env python3
"""Turn the analysis lock into the scorer's contrast list. Derived, not assembled by hand.

`e1_score.py` needs, per contrast, the two arms to difference, the registered mode, the numeric
margin and whether the contrast is powered. Every one of those is already fixed in the analysis
lock. Writing them out by hand at scoring time would be a chance to choose, which is the thing the
lock exists to remove, so this reads the lock and emits exactly the 19 primary contrasts.

Arm keys match the prediction file's `ratio|arm` form, so a contrast that names an arm the
prediction run did not write fails loudly here rather than silently later.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

M_FAMILY = 19


def arms_of(contrast: str) -> tuple[str, str]:
    """The two arm names, left minus right, from the contrast's own name."""
    left, _, right = contrast.partition(" - ")
    if not right:
        raise ValueError(f"{contrast!r} is not a paired difference")
    return left, right


def build(lock: dict) -> list[dict]:
    rows = []
    for row in lock["contrasts"]:
        if not row["held_out"]:
            continue
        left, right = arms_of(row["contrast"])
        ratio = row["ratio"]
        rows.append({
            "name": f"{ratio} {row['contrast']}",
            "ratio": ratio,
            "arms": [f"{ratio}|{left}", f"{ratio}|{right}"],
            "mode": row["mode"],
            "margin": row["margin"],
            "powered": row["powered"],
        })
    if len(rows) != M_FAMILY:
        raise SystemExit(f"the lock has {len(rows)} primary contrasts, not {M_FAMILY}")
    return rows


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--lock", type=Path, required=True, help="the analysis lock JSON")
    parser.add_argument("--predictions", type=Path,
                        help="check every named arm exists in this prediction file")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)

    lock = json.loads(args.lock.read_text(encoding="utf-8"))
    rows = build(lock)

    if args.predictions:
        written = set(json.loads(args.predictions.read_text(encoding="utf-8"))["arms"])
        missing = sorted({arm for row in rows for arm in row["arms"]} - written)
        if missing:
            raise SystemExit(f"the prediction file has no arm for: {', '.join(missing)}")

    args.out.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print(json.dumps(rows, indent=2))
    print(f"\n{len(rows)} contrasts, {sum(1 for r in rows if r['powered'])} powered. "
          "The shift rows also need --shift-target-prior, which the prediction report records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
