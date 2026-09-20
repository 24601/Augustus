#!/usr/bin/env python3
"""Since-last-look fingerprint helper.

Hourly diffs catalogued sources against the last look. A fingerprint
move is revisit HIGH. Star-noise is not a fold. This script does not
fetch the network. It does not treat a SHA move as a replica. It does
not invent equivalence.

Stored fingerprints (default):
  default_sha, pushed_at, description_hash, release_tag

Material change (inspect when fingerprints move, or when hourly already
saw the rewrite):
  README, API, release, calibration claim, serving port, bench rewrite

Star-noise (not a fold):
  stargazers_count, watchers_count, forks_count, likes

Usage:
  python3 research/revisit_fingerprints.py --self-test
  python3 research/revisit_fingerprints.py --classify stored.json observed.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Mapping

ROOT = Path(__file__).resolve().parents[1]
STORE = ROOT / "research" / "revisit_fingerprints.json"

STORED_FIELDS = (
    "default_sha",
    "pushed_at",
    "description_hash",
    "release_tag",
)

MATERIAL_SIGNALS = (
    "readme",
    "api",
    "release",
    "calibration_claim",
    "serving_port",
    "bench_rewrite",
)

STAR_NOISE_FIELDS = (
    "stargazers_count",
    "watchers_count",
    "forks_count",
    "likes",
)

GRADES = ("unchanged", "star_noise", "material")


def description_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def _fp(record: Mapping[str, Any]) -> dict[str, Any]:
    src = record.get("fingerprints", record)
    return {k: src.get(k) for k in STORED_FIELDS}


def classify(
    stored: Mapping[str, Any],
    observed: Mapping[str, Any],
    *,
    material_signals: tuple[str, ...] = (),
) -> dict[str, Any]:
    """Diff last-look fingerprints against this hour.

    Returns grade, reasons, and the densify action. Unknown material
    signal names fail closed (raise). Unknown grades cannot be returned.
    """
    reasons: list[str] = []
    before = _fp(stored)
    after = _fp(observed)
    for field in STORED_FIELDS:
        if before.get(field) != after.get(field):
            reasons.append(field)
    for signal in material_signals:
        if signal not in MATERIAL_SIGNALS:
            raise AssertionError(f"unknown material signal: {signal}")
        tag = f"material:{signal}"
        if tag not in reasons:
            reasons.append(tag)

    noise_moved: list[str] = []
    for field in STAR_NOISE_FIELDS:
        if field in stored or field in observed:
            if stored.get(field) != observed.get(field):
                noise_moved.append(field)

    if reasons:
        grade = "material"
        action = "revisit_high_like_novel_high"
    elif noise_moved:
        grade = "star_noise"
        action = "pulse_only"
        reasons = list(noise_moved)
    else:
        grade = "unchanged"
        action = "skip"

    if grade not in GRADES:
        raise AssertionError(f"unclassified grade {grade}")
    return {
        "grade": grade,
        "reasons": reasons,
        "action": action,
        "invents_equivalence": False,
    }


def densify_card_rules() -> tuple[str, ...]:
    return (
        "Keep the original notes.md section id. Append a dated densify card.",
        "Do not mint a sibling first-sighting section for the same source.",
        "Quote the new README/API/release *theirs*. Keep the prior quotes.",
        "Do not invent equivalence. SHA move is not a replica.",
        "Wire-compat is not a calibrated Noul. A new bench number is not Harbor.",
        "Namesake locks stay. Prior uniqueness locks stay one substring.",
        "Treat revisit HIGH like novel HIGH for Augustus.",
    )


def _hex12(value: Any) -> bool:
    return isinstance(value, str) and len(value) == 12 and all(
        c in "0123456789abcdef" for c in value
    )


def load_store(path: Path | None = None) -> dict[str, Any]:
    p = path or STORE
    data = json.loads(p.read_text(encoding="utf-8"))
    if data.get("stored_fields") != list(STORED_FIELDS):
        raise AssertionError("store stored_fields mismatch")
    looks = data.get("looks")
    if not isinstance(looks, list):
        raise AssertionError("store looks must be a list")
    for look in looks:
        fp = look.get("fingerprints") or {}
        look_id = look.get("id")
        for field in STORED_FIELDS:
            if field not in fp:
                raise AssertionError(f"look {look_id} missing {field}")
        digest = fp.get("description_hash")
        if digest is not None:
            if not _hex12(digest):
                raise AssertionError(
                    f"look {look_id} description_hash must be null or sha256[:12]"
                )
            readme = look.get("readme_sha")
            if isinstance(readme, str) and digest == readme[:12]:
                raise AssertionError(
                    f"look {look_id} description_hash is README SHA prefix; "
                    "README SHA is an optional extra, not a substitute"
                )
        sha = fp.get("default_sha")
        if isinstance(sha, str) and len(sha) == 12:
            raise AssertionError(
                f"look {look_id} default_sha is a 12-char prefix; store the full HEAD"
            )
    return data


def self_test() -> None:
    stored = {
        "id": "github:TheoLeeCJ/SemIf",
        "fingerprints": {
            "default_sha": "ca3ba65f142967030ecb453346e94d6f476a69df",
            "pushed_at": "2026-09-19T04:46:36Z",
            "description_hash": description_hash(
                "interface pattern reproduction with open models"
            ),
            "release_tag": None,
        },
        "stargazers_count": 2282,
        "likes": None,
    }
    same = classify(stored, dict(stored))
    assert same["grade"] == "unchanged" and same["action"] == "skip", same
    assert same["invents_equivalence"] is False

    stars = dict(stored)
    stars["stargazers_count"] = 2300
    noise = classify(stored, stars)
    assert noise["grade"] == "star_noise" and noise["action"] == "pulse_only", noise
    assert "stargazers_count" in noise["reasons"]

    likes = dict(stored)
    likes["likes"] = 58
    like_noise = classify(stored, likes)
    assert like_noise["grade"] == "star_noise", like_noise
    assert "likes" in like_noise["reasons"]

    forks = dict(stored)
    forks["forks_count"] = 141
    fork_noise = classify(stored, forks)
    assert fork_noise["grade"] == "star_noise", fork_noise
    assert "forks_count" in fork_noise["reasons"]

    sha = {
        "fingerprints": dict(stored["fingerprints"]),
        "stargazers_count": 2300,
    }
    sha["fingerprints"]["default_sha"] = "deadbeef0001"
    moved = classify(stored, sha)
    assert moved["grade"] == "material", moved
    assert moved["action"] == "revisit_high_like_novel_high", moved
    assert "default_sha" in moved["reasons"]
    assert moved["invents_equivalence"] is False

    trunc = {"fingerprints": dict(stored["fingerprints"])}
    trunc["fingerprints"]["default_sha"] = "ca3ba65f1429"
    assert classify(stored, trunc)["grade"] == "material"

    pushed = {"fingerprints": dict(stored["fingerprints"])}
    pushed["fingerprints"]["pushed_at"] = "2026-09-20T18:00:00Z"
    assert classify(stored, pushed)["grade"] == "material"

    desc = {"fingerprints": dict(stored["fingerprints"])}
    desc["fingerprints"]["description_hash"] = description_hash("new blurb")
    assert classify(stored, desc)["grade"] == "material"

    unknown_desc = {
        "fingerprints": {
            "default_sha": "ca3ba65f142967030ecb453346e94d6f476a69df",
            "pushed_at": "2026-09-19T04:46:36Z",
            "description_hash": None,
            "release_tag": None,
        }
    }
    saw_desc = {"fingerprints": dict(unknown_desc["fingerprints"])}
    saw_desc["fingerprints"]["description_hash"] = description_hash("live blurb")
    assert classify(unknown_desc, saw_desc)["grade"] == "material"
    assert classify(unknown_desc, dict(unknown_desc))["grade"] == "unchanged"

    tag = {"fingerprints": dict(stored["fingerprints"])}
    tag["fingerprints"]["release_tag"] = "v2.0.0"
    assert classify(stored, tag)["grade"] == "material"

    readme = classify(stored, dict(stored), material_signals=("readme", "bench_rewrite"))
    assert readme["grade"] == "material"
    assert "material:readme" in readme["reasons"]
    assert "material:bench_rewrite" in readme["reasons"]

    try:
        classify(stored, dict(stored), material_signals=("vibes",))
    except AssertionError:
        pass
    else:
        raise AssertionError("unknown material signal must fail closed")

    store = load_store()
    assert store["schema_version"] == 1
    by_id = {look["id"]: look for look in store["looks"]}
    assert "github:TheoLeeCJ/SemIf" in by_id
    assert "github:TianyuCodings/NanoJev" in by_id
    semif = by_id["github:TheoLeeCJ/SemIf"]["fingerprints"]
    assert semif["default_sha"] == "ca3ba65f142967030ecb453346e94d6f476a69df"
    assert semif["pushed_at"] == "2026-09-19T04:46:36Z"
    assert semif["description_hash"] is None
    assert semif["release_tag"] is None
    nano = by_id["github:TianyuCodings/NanoJev"]["fingerprints"]
    assert nano["default_sha"] == "618cea6d906d54e128360786d12f703fff2b1245"
    assert nano["pushed_at"] is None
    assert nano["description_hash"] is None
    assert nano["release_tag"] == "unified-games-v1"
    nano_readme = by_id["github:TianyuCodings/NanoJev"].get("readme_sha")
    assert isinstance(nano_readme, str) and nano_readme.startswith("4190093c64ee")
    semif_readme = by_id["github:TheoLeeCJ/SemIf"].get("readme_sha")
    assert isinstance(semif_readme, str) and semif_readme.startswith("74ab7f7f")
    rules = densify_card_rules()
    assert any("sibling first-sighting" in r for r in rules)
    assert any("revisit HIGH like novel HIGH" in r for r in rules)
    print("revisit-fingerprints self-test ok")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--classify", nargs=2, metavar=("STORED", "OBSERVED"))
    ap.add_argument(
        "--material",
        default="",
        help="comma-separated material signals (readme,api,release,"
        "calibration_claim,serving_port,bench_rewrite)",
    )
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.classify:
        stored = json.loads(Path(args.classify[0]).read_text(encoding="utf-8"))
        observed = json.loads(Path(args.classify[1]).read_text(encoding="utf-8"))
        signals = tuple(s for s in args.material.split(",") if s)
        print(json.dumps(classify(stored, observed, material_signals=signals), indent=2))
        return 0
    ap.error("need --self-test or --classify stored.json observed.json")
    return 2


if __name__ == "__main__":
    sys.exit(main())
