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
    assert nano["default_sha"] == "76fdfc9ecdca45a9bcef17991a07d3041a87685a"
    assert nano["pushed_at"] == "2026-09-21T09:58:28Z"
    assert nano["description_hash"] == "92ce9454eeeb"
    assert nano["release_tag"] == "unified-games-v1"
    nano_readme = by_id["github:TianyuCodings/NanoJev"].get("readme_sha")
    assert isinstance(nano_readme, str) and nano_readme.startswith("a8f8afeb7e44")
    openjev = by_id["github:Zefan-Cai/Open-Jev"]["fingerprints"]
    assert openjev["default_sha"] == "ed45657bf726c3b77408942830e5578f99df904e"
    assert openjev["pushed_at"] == "2026-09-21T07:40:27Z"
    openjev_readme = by_id["github:Zefan-Cai/Open-Jev"].get("readme_sha")
    assert isinstance(openjev_readme, str) and openjev_readme.startswith("12e0f581e15d")
    assert by_id["hf:ZefanCai/Open-Jev-2B"]["fingerprints"]["default_sha"].startswith("0c7aa498b162")
    assert by_id["hf:ZefanCai/Open-Jev-9B"]["fingerprints"]["default_sha"].startswith("47e966881e48")
    assert by_id["hf:ds:ZefanCai/Open-Jev"]["fingerprints"]["default_sha"].startswith("c67699e13d0a")
    assert by_id["hf:ds:ZefanCai/Open-Jev"]["notes_section"] == "125"
    semif_readme = by_id["github:TheoLeeCJ/SemIf"].get("readme_sha")
    assert isinstance(semif_readme, str) and semif_readme.startswith("74ab7f7f")
    kev = by_id["github:jaredpalmer/kev"]["fingerprints"]
    assert kev["default_sha"].startswith("90990a5fac29")
    assert kev["description_hash"] == "47fc60928c90"
    assert kev["release_tag"] == "kev-family"
    assert kev["pushed_at"] == "2026-09-22T00:44:00Z"
    assert by_id["github:jaredpalmer/kev"]["notes_section"] == "45"
    kev_readme = by_id["github:jaredpalmer/kev"].get("readme_sha")
    assert isinstance(kev_readme, str) and kev_readme.startswith("d497d4b89427")
    tidy = by_id["github:AkhilBod/Tidy"]
    assert tidy["notes_section"] == "157"
    assert tidy["fingerprints"]["default_sha"] is None
    assert tidy["fingerprints"]["description_hash"] == "43bc19349316"
    assert tidy["fingerprints"]["pushed_at"] == "2026-09-22T00:31:44Z"
    for course in (
        "github:nadeemcite/jev-crash-course",
        "github:nadyth/jev-crash-course",
    ):
        card = by_id[course]
        assert card["notes_section"] == "150", course
        assert card["fingerprints"]["default_sha"] is None
        assert card["fingerprints"]["description_hash"] == "fc0f510875fa"
    kotoba = by_id["github:kotoba-lang/typed-decisions"]["fingerprints"]
    assert kotoba["default_sha"].startswith("ff7f84e74d04")
    cartpole = by_id["github:tinmanlab/cartpole-jev"]["fingerprints"]
    assert cartpole["default_sha"].startswith("922cc61490a0")
    ashare = by_id["github:xuboboo/ashare-trader"]["fingerprints"]
    assert ashare["default_sha"].startswith("26c7e95e6828")
    kevin = by_id["github:gauravsaini/kevin"]["fingerprints"]
    assert kevin["default_sha"].startswith("96336428dc15")
    jevlab = by_id["github:mjyoke1111/jev-lab"]["fingerprints"]
    assert jevlab["default_sha"].startswith("0bd66957283a")
    razor = by_id["github:razorback16/openjev"]["fingerprints"]
    assert razor["default_sha"].startswith("2050fdb8280d")
    razor_readme = by_id["github:razorback16/openjev"].get("readme_sha")
    assert isinstance(razor_readme, str) and razor_readme.startswith("d5322e16e565")
    assert by_id["github:TypeLLM/TypeLLM"]["fingerprints"]["release_tag"] == "v0.1.1"
    jevloop = by_id["github:zjunlp/JevLoop"]["fingerprints"]
    assert jevloop["default_sha"].startswith("56cbf2bd6b5d")
    typellm = by_id["github:TypeLLM/TypeLLM"]["fingerprints"]
    assert typellm["default_sha"].startswith("8a8b4aefd443")
    simple = by_id["github:featherless-ai/simple-jev"]["fingerprints"]
    assert simple["default_sha"].startswith("b02aa81c915a")

    browser = by_id["github:wy-coliney/jev-browser-use"]["fingerprints"]
    assert browser["default_sha"].startswith("f14b60e0ae1e")
    grouter = by_id["github:gargpratyush/jev-router"]["fingerprints"]
    assert grouter["default_sha"].startswith("38da6b84ea01")
    brouter = by_id["github:BillionsBobby/JevRouter"]["fingerprints"]
    assert brouter["default_sha"].startswith("7378f1d06b11")
    dasein = by_id["github:daseinlabs/open-jev"]["fingerprints"]
    assert dasein["default_sha"].startswith("8a4fbdf712e7")
    densify_original_ids = {
        "github:razorback16/openjev": "75",
        "github:wfzyx/von": "49",
        "github:Heman10x-NGU/openJev-verdict-2.0": "71",
        "github:jaredpalmer/kev": "45",
        "github:logan-markewich/jeff": "60",
        "github:TypeLLM/TypeLLM": "113",
        "github:TheoOliveira/pi-jev": "42",
        "github:tamaratran/jev-pruner": "53",
        "github:dtduc-git/jevassert": "70",
        "github:dtduc-git/jev-packs": "64",
        "github:Zefan-Cai/Open-Jev": "125",
        "hf:ZefanCai/Open-Jev-2B": "125",
        "hf:ZefanCai/Open-Jev-9B": "125",
        "hf:ds:ZefanCai/Open-Jev": "125",
        "github:alexwestco/llm-to-jev": "118",
        "github:kotoba-lang/typed-decisions": "130",
        "github:tinmanlab/cartpole-jev": "121",
        "github:xuboboo/ashare-trader": "120",
        "github:mjyoke1111/jev-lab": "106",
        "github:moritzkremb/jev-voice-browser": "82",
        "github:luantak/is-malicious": "17",
        "github:TianyuCodings/NanoJev": "115",
        "github:bespokelabsai/nimble": "35",
        "github:evoke-build/evoke": "139",
        "github:tyler-dot-earth/patdown": "121",
        "github:sumleo/prompt2jev": "141",
        "github:AbdelStark/awesome-typesafe-jev": "141",
        "hf:wayfind/metask-jev-4b-policy-mix": "134",
        "hf:ds:Praveenrajus/jev-bench": "125",
    }
    for look_id, section in densify_original_ids.items():
        assert look_id in by_id, look_id
        assert by_id[look_id]["notes_section"] == section, (
            look_id,
            by_id[look_id].get("notes_section"),
            section,
        )
    rules = densify_card_rules()
    assert any("sibling first-sighting" in r for r in rules)

    lcc = by_id["github:lucasmartins-ai/lcc"]["fingerprints"]
    assert lcc["default_sha"].startswith("a7e86fb60997")
    assert by_id["github:lucasmartins-ai/lcc"]["notes_section"] == "140"
    jevc = by_id["github:David-Lolly/Jev-Compatible"]["fingerprints"]
    assert jevc["default_sha"].startswith("e52e963d8539")
    any2 = by_id["github:hwfengcs/any2jev"]["fingerprints"]
    assert any2["default_sha"].startswith("719b0eb9eefe")
    traffic = by_id["github:Akhila14/jev-traffic-simulator"]["fingerprints"]
    assert traffic["default_sha"].startswith("7136542dffb5")
    assert by_id["github:Akhila14/jev-traffic-simulator"]["notes_section"] == "140"
    xiangqi = by_id["github:Zafer-Liu/jev-xiangqi"]["fingerprints"]
    assert xiangqi["default_sha"].startswith("7181fab5bb27")
    assert by_id["github:umgbhalla/jevx"]["notes_section"] == "140"
    nimble = by_id["github:bespokelabsai/nimble"]["fingerprints"]
    assert nimble["default_sha"].startswith("f136b3f75721")
    assert by_id["github:bespokelabsai/nimble"]["notes_section"] == "35"
    evoke = by_id["github:evoke-build/evoke"]["fingerprints"]
    assert evoke["default_sha"].startswith("50c9637ef11f")
    assert by_id["github:evoke-build/evoke"]["notes_section"] == "139"
    patdown = by_id["github:tyler-dot-earth/patdown"]["fingerprints"]
    assert patdown["default_sha"].startswith("8b2b2b591470")
    assert by_id["github:tyler-dot-earth/patdown"]["notes_section"] == "121"
    p2j = by_id["github:sumleo/prompt2jev"]["fingerprints"]
    assert p2j["default_sha"].startswith("f3b6bc763b74")
    assert by_id["github:sumleo/prompt2jev"]["notes_section"] == "141"
    assert by_id["github:lukstei/slop-grader"]["notes_section"] == "144"
    assert by_id["github:Andymulb/jev_the_philosopher"]["notes_section"] == "144"
    assert by_id["github:PerryLink/layacore"]["notes_section"] == "144"
    assert by_id["github:vericle/intellyweave"]["fingerprints"]["default_sha"].startswith("ff4152ce9d20")
    assert by_id["github:genai-craft/openvons"]["notes_section"] == "68"
    gliner = by_id["github:47thtechcorner/RayCodes_GLiNER_V1_Multi"]["fingerprints"]
    assert gliner["default_sha"].startswith("485cf8045f73")
    assert by_id["github:47thtechcorner/RayCodes_GLiNER_V1_Multi"]["notes_section"] == "141"
    awesome_jev = by_id["github:AbdelStark/awesome-typesafe-jev"]["fingerprints"]
    assert awesome_jev["default_sha"].startswith("d6ea2a0d6cf4")
    assert by_id["github:AbdelStark/awesome-typesafe-jev"]["notes_section"] == "141"
    jevcu = by_id["github:Sac-Y/Jev-cu"]["fingerprints"]
    assert jevcu["default_sha"].startswith("e2cc92d731fa")
    assert by_id["github:Sac-Y/Jev-cu"]["notes_section"] == "142"
    tax = by_id["github:kyotofin/tax-doc-classifier"]["fingerprints"]
    assert tax["default_sha"].startswith("3e95a77f763c")
    assert by_id["github:patryckalves/jev-no-enem"]["notes_section"] == "142"
    assert by_id["hf:wayfind/metask-jev-4b-policy-mix"]["notes_section"] == "134"
    assert by_id["hf:ds:Praveenrajus/jev-bench"]["notes_section"] == "125"
    assert any("revisit HIGH like novel HIGH" in r for r in rules)
    onesystem = by_id["github:rawwerks/one-system"]
    assert onesystem["notes_section"] == "155"
    os_fp = onesystem["fingerprints"]
    assert os_fp["default_sha"] == "1104500a0197737d25334472a42a5a790098105c"
    assert os_fp["release_tag"] == "v0.2.0"
    assert os_fp["description_hash"] == "4576d70e542f"
    assert os_fp["pushed_at"] == "2026-09-21T21:37:02Z"
    assert onesystem["readme_sha"].startswith("fd20bacaade7")
    fluid = by_id["github:FluidInference/FluidUse"]
    assert fluid["notes_section"] == "143"
    fl = fluid["fingerprints"]
    assert fl["default_sha"].startswith("e9e95935075b")
    assert fl["release_tag"] == "v0.2.0"
    assert fl["description_hash"] == "ddacb829949a"
    assert fl["pushed_at"] == "2026-09-21T22:18:09Z"
    assert fluid["readme_sha"].startswith("7d246df7270a")
    docjev = by_id["github:jerryjliu/docjev"]
    assert docjev["notes_section"] == "156"
    dj = docjev["fingerprints"]
    assert dj["default_sha"].startswith("7e6b48d3f7ee")
    assert dj["description_hash"] == "3dace90930ca"
    assert dj["release_tag"] is None
    assert dj["pushed_at"] == "2026-09-21T22:40:31Z"
    assert docjev["readme_sha"].startswith("2ce22c98a411")
    local = by_id["github:Argos1111/jev_local"]
    assert local["notes_section"] == "94"
    assert local["fingerprints"]["default_sha"].startswith("70a1ed6f197a")
    assert local["fingerprints"]["release_tag"] == "sarashina-llama-b11042-pre1"
    assert local["fingerprints"]["description_hash"] == "ea606aeb1f82"
    well = by_id["github:suraj-phanindra/wellposed"]
    assert well["notes_section"] == "46"
    assert well["fingerprints"]["default_sha"].startswith("86e6f8cb17e4")
    empty = by_id["github:DumoeDss/jev-demos"]
    assert empty["notes_section"] == "156"
    assert empty["fingerprints"]["default_sha"] is None
    shadow = by_id["github:jonkthomas/jev-shadow"]
    assert shadow["notes_section"] == "153"
    assert shadow["fingerprints"]["default_sha"].startswith("fd17ee44ecb2")
    inside = by_id["github:ChiyuSONG/inside-jev"]
    assert inside["notes_section"] == "154"
    assert inside["fingerprints"]["description_hash"] == "42d9e077390e"
    laya_ft = by_id["github:Alexander-Ollman/laya-ft"]
    assert laya_ft["notes_section"] == "148"
    assert laya_ft["fingerprints"]["default_sha"].startswith("32c1cb32557a")
    jimothy = by_id["github:AndrewPrifer/jimothy"]
    assert jimothy["notes_section"] == "159"
    jt = jimothy["fingerprints"]
    assert jt["default_sha"] == "f2ad9b40b88ea913d38fda758e564eac5f12fc0b"
    assert jt["pushed_at"] == "2026-09-21T02:37:21Z"
    assert jt["description_hash"] is None
    assert jt["release_tag"] is None
    assert jimothy["readme_sha"].startswith("124318338a4c")
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
