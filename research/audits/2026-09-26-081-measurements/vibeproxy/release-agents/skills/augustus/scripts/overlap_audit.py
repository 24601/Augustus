#!/usr/bin/env python3
"""Fail closed when training data touches confirmation data; never train or score.

Input is one JSON manifest with schema_version=1 and two or more named
partitions. Each partition lists items: an id, an optional exact text, an
optional normalized text, and an optional group. A partition is marked
`confirmation: true` when it is the untouched set an acceptance claim rests on.

Four ways a split leaks, all checked here:

1. Duplicate item ids across partitions.
2. Identical text across partitions, compared on the caller's own normalized
   text when supplied and on the exact text otherwise.
3. A shared group across partitions. Paraphrases, generation families, a
   person's several episodes and a page's several rows are one unit; splitting
   them randomly leaks the unit even when no two texts match.
4. An item declaring neither text nor group, which cannot be checked at all.

Fail closed means the last one is a failure, not a pass. A manifest that
supplies nothing to compare gets `unverifiable`, never `clean`: an audit that
cannot see a leak must not report its absence as evidence.

What this does NOT do
---------------------
It compares what the manifest declares. It does not read your data, detect
near-duplicates or translations, verify that a declared group is the real
sampling unit, or know that two different texts describe the same event. A
clean result bounds exact and declared-group overlap only.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path

SCHEMA_VERSION = 1


class ManifestError(ValueError):
    """A malformed manifest. Distinct from an audit finding."""


def _object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ManifestError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ManifestError(f"{name} must be nonempty text")
    return value


def _optional_text(value, name):
    if value is None:
        return None
    return _text(value, name)


def _partitions(document):
    raw = document.get("partitions")
    if not isinstance(raw, list) or len(raw) < 2:
        raise ManifestError("partitions must be a list of at least two partitions")
    partitions = {}
    for index, partition in enumerate(raw):
        if not isinstance(partition, dict):
            raise ManifestError(f"partition {index} must be an object")
        name = _text(partition.get("name"), f"partition {index} name")
        if name in partitions:
            raise ManifestError(f"duplicate partition name: {name}")
        confirmation = partition.get("confirmation", False)
        if not isinstance(confirmation, bool):
            raise ManifestError(f"partition {name} confirmation must be true or false")
        items = partition.get("items")
        if not isinstance(items, list) or not items:
            raise ManifestError(f"partition {name} items must be a nonempty list")
        parsed = []
        for position, item in enumerate(items):
            if not isinstance(item, dict):
                raise ManifestError(f"partition {name} item {position} must be an object")
            parsed.append({
                "id": _text(item.get("id"), f"partition {name} item {position} id"),
                "text": _optional_text(item.get("text"), f"partition {name} item {position} text"),
                "normalized_text": _optional_text(
                    item.get("normalized_text"), f"partition {name} item {position} normalized_text"),
                "group": _optional_text(item.get("group"), f"partition {name} item {position} group"),
            })
        partitions[name] = {"confirmation": confirmation, "items": parsed}
    return partitions


def _comparable(item):
    """The string this item is compared on, and which field supplied it.

    The caller's own normalized text wins when present: normalization is a
    decision about what counts as the same row, and it is not this tool's to
    make silently.
    """
    if item["normalized_text"] is not None:
        return item["normalized_text"], "normalized_text"
    if item["text"] is not None:
        return item["text"], "text"
    return None, None


def _collisions(partitions, key_of):
    """Keys appearing in more than one partition, with where they appeared."""
    where = defaultdict(lambda: defaultdict(list))
    for name, partition in partitions.items():
        for item in partition["items"]:
            key = key_of(item)
            if key is not None:
                where[key][name].append(item["id"])
    return {key: dict(seen) for key, seen in where.items() if len(seen) > 1}


def audit(document) -> dict:
    if not isinstance(document, dict):
        raise ManifestError("document must be an object")
    if type(document.get("schema_version")) is not int or document["schema_version"] != SCHEMA_VERSION:
        raise ManifestError(f"schema_version must be integer {SCHEMA_VERSION}")
    partitions = _partitions(document)
    confirmation_names = sorted(name for name, p in partitions.items() if p["confirmation"])
    if not confirmation_names:
        raise ManifestError("at least one partition must set confirmation: true")

    findings = []

    for key, seen in sorted(_collisions(partitions, lambda item: item["id"]).items()):
        findings.append({"kind": "duplicate_id", "key": key, "partitions": seen})

    text_hits = _collisions(partitions, lambda item: _comparable(item)[0])
    for key, seen in sorted(text_hits.items()):
        compared_on = sorted({
            _comparable(item)[1]
            for name in seen for item in partitions[name]["items"]
            if _comparable(item)[0] == key
        })
        findings.append({
            "kind": "identical_text", "partitions": seen, "compared_on": compared_on,
            # The text itself is not echoed: a leak report should not become a
            # second copy of the data it is reporting on.
            "text_sha256": hashlib.sha256(key.encode("utf-8")).hexdigest(),
        })

    for key, seen in sorted(_collisions(partitions, lambda item: item["group"]).items()):
        findings.append({"kind": "shared_group", "key": key, "partitions": seen})

    uncheckable = {}
    for name, partition in partitions.items():
        blind = [item["id"] for item in partition["items"]
                 if _comparable(item)[0] is None and item["group"] is None]
        if blind:
            uncheckable[name] = blind

    # Only overlap that actually touches a confirmation partition can invalidate
    # an acceptance claim. Overlap between two training partitions is reported,
    # because it inflates apparent data, but it is not a leak.
    def touches_confirmation(finding):
        return any(name in confirmation_names for name in finding["partitions"])

    leaks = [finding for finding in findings if touches_confirmation(finding)]
    other = [finding for finding in findings if not touches_confirmation(finding)]

    if leaks:
        assessment = "leak"
    elif uncheckable:
        assessment = "unverifiable"
    else:
        assessment = "clean"

    return {
        "schema_version": SCHEMA_VERSION,
        "assessment": assessment,
        "confirmation_partitions": confirmation_names,
        "partition_sizes": {name: len(p["items"]) for name, p in sorted(partitions.items())},
        "confirmation_leaks": leaks,
        "other_overlap": other,
        "uncheckable_items": uncheckable,
        "limits": [
            "Declared manifest only: no data is read, and a declared group is not verified to be the real sampling unit.",
            "Exact comparison on the caller's normalized text when supplied, otherwise the exact text. Near-duplicates, paraphrases and translations are not detected.",
            "`clean` bounds exact and declared-group overlap. It is not evidence of independence, and it does not establish that two different texts describe different events.",
            "`unverifiable` means an item supplied nothing to compare; absence of a finding there is not absence of a leak.",
            "Overlap between two non-confirmation partitions is reported separately, because it inflates apparent data without invalidating an acceptance claim.",
        ],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("manifest", type=Path, help="declared split manifest JSON")
    args = parser.parse_args(argv)
    try:
        raw = args.manifest.read_bytes()
        document = json.loads(raw, object_pairs_hook=_object)
        result = audit(document)
        result["input_sha256"] = hashlib.sha256(raw).hexdigest()
        print(json.dumps(result, indent=2, allow_nan=False))
    except (OSError, ValueError, RecursionError) as exc:
        parser.exit(2, f"error: {exc}\n")
    # Fail closed: only a clean audit exits 0, so a pipeline that ignores the
    # body still stops on a leak or an unverifiable manifest.
    return 0 if result["assessment"] == "clean" else 1


if __name__ == "__main__":
    raise SystemExit(main())
