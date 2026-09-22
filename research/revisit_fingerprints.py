#!/usr/bin/env python3
"""Since-last-look fingerprint helper.

Fingerprints are observations, not capability claims. A changed complete
fingerprint asks for a review of the diff; only an independently observed
material signal requests a densified material revisit. Missing or null values
are unknown, never evidence that a capability changed. Star-like counters are
pulse noise when no review/material reason exists.

Stored fingerprint fields: default_sha, pushed_at, description_hash,
release_tag. This script is local-only and never fetches a source.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Mapping


ROOT = Path(__file__).resolve().parents[1]
STORE = ROOT / "research" / "revisit_fingerprints.json"
STORED_FIELDS = ("default_sha", "pushed_at", "description_hash", "release_tag")
MATERIAL_SIGNALS = (
    "readme",
    "api",
    "release",
    "calibration_claim",
    "serving_port",
    "bench_rewrite",
)
STAR_NOISE_FIELDS = ("stargazers_count", "watchers_count", "forks_count", "likes")
GRADES = ("unchanged", "star_noise", "review", "material")


def description_hash(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("description text must be a string")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def _hex12(value: Any) -> bool:
    return isinstance(value, str) and len(value) == 12 and all(
        char in "0123456789abcdef" for char in value
    )


def _validate_fingerprint(fp: Mapping[str, Any]) -> None:
    sha = fp["default_sha"]
    if sha is not None and (
        not isinstance(sha, str)
        or len(sha) != 40
        or any(char not in "0123456789abcdef" for char in sha)
    ):
        raise ValueError("default_sha must be null or a full 40-character lowercase SHA")

    pushed_at = fp["pushed_at"]
    if pushed_at is not None:
        if (
            not isinstance(pushed_at, str)
            or "T" not in pushed_at
            or not pushed_at.endswith("Z")
        ):
            raise ValueError("pushed_at must be null or an ISO-8601 UTC timestamp")
        try:
            parsed = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
        except ValueError as exc:
            raise ValueError("pushed_at must be null or an ISO-8601 UTC timestamp") from exc
        if parsed.tzinfo is None or parsed.utcoffset() != timedelta(0):
            raise ValueError("pushed_at must be null or an ISO-8601 UTC timestamp")

    digest = fp["description_hash"]
    if digest is not None and not _hex12(digest):
        raise ValueError("description_hash must be null or sha256[:12]")

    tag = fp["release_tag"]
    if tag is not None and (not isinstance(tag, str) or not tag.strip()):
        raise ValueError("release_tag must be null or a non-empty string")


def _fp(record: Mapping[str, Any]) -> dict[str, Any]:
    if not isinstance(record, Mapping):
        raise ValueError("fingerprint record must be an object")
    source = record.get("fingerprints", record)
    if not isinstance(source, Mapping):
        raise ValueError("fingerprints must be an object")
    missing = [field for field in STORED_FIELDS if field not in source]
    if missing:
        raise ValueError(f"fingerprint record missing {', '.join(missing)}")
    result = {field: source[field] for field in STORED_FIELDS}
    _validate_fingerprint(result)
    return result


def classify(
    stored: Mapping[str, Any],
    observed: Mapping[str, Any],
    *,
    material_signals: tuple[str, ...] = (),
) -> dict[str, Any]:
    """Classify a last-look comparison without inferring source capability.

    Any valid fingerprint difference produces ``review`` / ``inspect_diff``.
    Material signals are evidence from inspection and therefore upgrade the
    result to ``material`` / ``densify``. Null is an unknown value; its change
    still requests review but never becomes a capability assertion.
    """
    if not isinstance(stored, Mapping) or not isinstance(observed, Mapping):
        raise ValueError("stored and observed records must be objects")
    stored_has_id = "id" in stored
    observed_has_id = "id" in observed
    if stored_has_id != observed_has_id:
        raise ValueError("stored and observed ids must both be present or both be absent")
    if stored_has_id:
        stored_id = stored["id"]
        observed_id = observed["id"]
        if not isinstance(stored_id, str) or not stored_id:
            raise ValueError("stored id must be a non-empty string when present")
        if not isinstance(observed_id, str) or not observed_id:
            raise ValueError("observed id must be a non-empty string when present")
    else:
        stored_id = observed_id = None
    if stored_id != observed_id:
        raise ValueError("stored and observed ids differ; refusing cross-source diff")

    for name, record in (("stored", stored), ("observed", observed)):
        if "node_id" in record and (not isinstance(record["node_id"], str) or not record["node_id"]):
            raise ValueError(f"{name} node_id must be a non-empty string when present")
    if "node_id" in stored and "node_id" in observed and stored["node_id"] != observed["node_id"]:
        raise ValueError("stored and observed node_id values differ; refusing cross-source diff")

    before = _fp(stored)
    after = _fp(observed)
    fingerprint_reasons = [
        field for field in STORED_FIELDS if before[field] != after[field]
    ]

    if isinstance(material_signals, str) or not isinstance(material_signals, (tuple, list)):
        raise ValueError("material_signals must be a sequence of signal names")
    material_reasons = []
    for signal in material_signals:
        if signal not in MATERIAL_SIGNALS:
            raise ValueError(f"unknown material signal: {signal}")
        tag = f"material:{signal}"
        if tag not in material_reasons:
            material_reasons.append(tag)

    noise_reasons = [
        field for field in STAR_NOISE_FIELDS
        if field in stored or field in observed
        if stored.get(field) != observed.get(field)
    ]
    reasons = fingerprint_reasons + material_reasons
    if material_reasons:
        grade, action = "material", "densify"
    elif fingerprint_reasons:
        grade, action = "review", "inspect_diff"
    elif noise_reasons:
        grade, action, reasons = "star_noise", "pulse_only", noise_reasons
    else:
        grade, action = "unchanged", "skip"
    if grade not in GRADES:
        raise RuntimeError(f"unclassified grade {grade}")
    return {
        "grade": grade,
        "reasons": reasons,
        "action": action,
        "capability_change_claimed": False,
    }


def densify_card_rules() -> tuple[str, ...]:
    return (
        "Keep the original notes section id and append a dated densify card.",
        "Do not mint a sibling first-sighting section for the same source.",
        "Keep prior evidence and quote inspected new source material.",
        "A fingerprint move requests review; it does not establish equivalence.",
    )


def load_store(path: Path | None = None) -> dict[str, Any]:
    """Validate every persisted fingerprint record without pinning its values."""
    source = path or STORE
    try:
        data = _read_json(source)
    except (OSError, ValueError, RecursionError) as exc:
        raise ValueError(f"cannot read fingerprint store: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("store must be a JSON object")
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        raise ValueError("store schema_version must be 1")
    if data.get("stored_fields") != list(STORED_FIELDS):
        raise ValueError("store stored_fields mismatch")
    looks = data.get("looks")
    if not isinstance(looks, list):
        raise ValueError("store looks must be a list")
    seen_ids = set()
    for look in looks:
        if not isinstance(look, dict):
            raise ValueError("store looks entries must be objects")
        look_id = look.get("id")
        if not isinstance(look_id, str) or not look_id:
            raise ValueError("store look id must be a non-empty string")
        if look_id in seen_ids:
            raise ValueError(f"duplicate store look id {look_id!r}")
        seen_ids.add(look_id)
        try:
            fingerprint = _fp(look)
        except ValueError as exc:
            raise ValueError(f"look {look_id}: {exc}") from exc
        readme_sha = look.get("readme_sha")
        if fingerprint["description_hash"] is not None and isinstance(readme_sha, str):
            if fingerprint["description_hash"] == readme_sha[:12]:
                raise ValueError(
                    f"look {look_id} description_hash is a README SHA prefix, not a description hash"
                )
    return data


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object)


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def _synthetic_record(**overrides: Any) -> dict[str, Any]:
    fingerprint = {
        "default_sha": "a" * 40,
        "pushed_at": "2026-01-01T00:00:00Z",
        "description_hash": description_hash("synthetic description"),
        "release_tag": None,
    }
    fingerprint.update(overrides)
    return {"id": "source:synthetic", "fingerprints": fingerprint, "stargazers_count": 1}


def self_test() -> None:
    """Exercise generic classification and validate every current store record."""
    stored = _synthetic_record()
    assert classify(stored, dict(stored))["grade"] == "unchanged"

    stars = _synthetic_record()
    stars["stargazers_count"] = 2
    assert classify(stored, stars)["grade"] == "star_noise"

    moved = _synthetic_record(default_sha="b" * 40)
    review = classify(stored, moved)
    assert review["grade"] == "review" and review["action"] == "inspect_diff"
    assert review["capability_change_claimed"] is False

    unknown = _synthetic_record(description_hash=None)
    assert classify(stored, unknown)["grade"] == "review"
    material = classify(stored, moved, material_signals=("readme",))
    assert material["grade"] == "material" and material["action"] == "densify"

    try:
        classify(stored, moved, material_signals=("unknown",))
    except ValueError:
        pass
    else:
        raise AssertionError("unknown material signal must fail")

    load_store()
    print("revisit-fingerprints self-test ok")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--classify", nargs=2, metavar=("STORED", "OBSERVED"))
    parser.add_argument(
        "--material",
        default="",
        help="comma-separated inspected signals: readme,api,release,calibration_claim,serving_port,bench_rewrite",
    )
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.classify:
        try:
            stored = _read_json(Path(args.classify[0]))
            observed = _read_json(Path(args.classify[1]))
            signals = tuple(signal.strip() for signal in args.material.split(",") if signal.strip())
            result = classify(stored, observed, material_signals=signals)
        except (OSError, ValueError, RecursionError) as exc:
            parser.error(str(exc))
        print(json.dumps(result, indent=2))
        return 0
    parser.error("need --self-test or --classify stored.json observed.json")
    return 2


if __name__ == "__main__":
    sys.exit(main())
