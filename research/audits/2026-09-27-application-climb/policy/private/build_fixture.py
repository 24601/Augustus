"""One-time deterministic synthetic evidence generation; never run by grade.py."""

import copy
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
PUBLIC = HERE.parent / "public"


def truth(row, ground_transit, cold_transit):
    """Independent operational simulator: count exposed hours, not ref formulas."""
    approved = sorted((x for x in row["certificates"] if x["signed"]),
                      key=lambda x: x["revision"], reverse=True)
    allowed = ["hold"]
    costs = {"hold": 35 + row["order_value"] / 4}
    for mode, handling, actual, fee in (
        ("ground", 1, ground_transit, 4 + row["weight_kg"]),
        ("cold", 3, cold_transit, 12 + 2 * row["weight_kg"]),
    ):
        route = row[mode]
        dose = 0
        for hour in range(1, handling + route["max_hours"] + 1):
            if mode == "ground" or hour > row["cold_protection_hours"]:
                dose += row["ambient_units_per_hour"]
        okay = bool(approved) and approved[0]["status"] == "released"
        if okay:
            okay = dose <= approved[0]["remaining_units"]
        okay = okay and route["open"] and (mode != "cold" or row["cold_boxes_available"])
        if okay:
            allowed.append(mode)
        late = actual + handling > row["deadline_hours"]
        costs[mode] = fee + (50 + row["order_value"] / 2 if late else 0)
    return {"allowed": allowed, "loss": costs,
            "actual_transit": {"ground": ground_transit, "cold": cold_transit}}


def base():
    return {
        "order_id": "anchor", "order_value": 100, "weight_kg": 2,
        "deadline_hours": 8, "legacy_risk_score": 0.92,
        "ambient_units_per_hour": 2, "cold_protection_hours": 7,
        "cold_boxes_available": True,
        "ground": {"open": True, "min_hours": 3, "max_hours": 7},
        "cold": {"open": True, "min_hours": 2, "max_hours": 4},
        "certificates": [{"revision": 1, "signed": True,
                          "status": "released", "remaining_units": 16}],
    }


def anchors():
    # Expectations below were derived by hand, not from truth() or reference.py.
    cases = []

    def add(name, row, allowed, losses, action, gt=7, ct=4):
        row["order_id"] = name
        cases.append({"name": name, "row": row, "ground_transit": gt,
                      "cold_transit": ct, "allowed": allowed,
                      "loss": dict(zip(("hold", "ground", "cold"), losses)),
                      "reference_action": action})

    add("ground-equality", base(), ["hold", "ground", "cold"], [60, 6, 16], "ground")
    r = base()
    r["certificates"][0]["remaining_units"] = 15
    add("one-unit-short", r, ["hold", "cold"], [60, 6, 16], "cold")
    r = base()
    r["certificates"].extend([
        {"revision": 3, "signed": False, "status": "released", "remaining_units": 1000},
        {"revision": 2, "signed": True, "status": "revoked", "remaining_units": 16}])
    add("signed-revocation-over-draft", r, ["hold"], [60, 6, 16], "hold")
    r = base()
    r["certificates"] = [
        {"revision": 8, "signed": True, "status": "released", "remaining_units": 16},
        {"revision": 4, "signed": True, "status": "quarantine", "remaining_units": 0}]
    add("signed-recovery-not-last-array-entry", r, ["hold", "ground", "cold"], [60, 6, 16], "ground")
    r = base()
    r["certificates"][0]["signed"] = False
    add("unsigned-only", r, ["hold"], [60, 6, 16], "hold")
    r = base()
    r["certificates"][0]["remaining_units"] = 15
    r["cold_boxes_available"] = False
    add("box-outage", r, ["hold"], [60, 6, 16], "hold")
    r = base()
    r["ground"]["open"] = False
    add("ground-outage", r, ["hold", "cold"], [60, 6, 16], "cold")
    r = base()
    r["deadline_hours"] = 4
    add("lucky-arrival-not-expected-cost", r, ["hold", "ground", "cold"], [60, 6, 116], "hold", gt=3, ct=2)
    r = base()
    r["deadline_hours"] = 7
    add("cold-deadline-equality", r, ["hold", "ground", "cold"], [60, 106, 16], "cold")
    r = base()
    r["cold_protection_hours"] = 6
    r["certificates"][0]["remaining_units"] = 1
    add("cold-protection-exhausted", r, ["hold"], [60, 6, 16], "hold")
    r = base()
    r["cold_protection_hours"] = 6
    r["certificates"][0]["remaining_units"] = 2
    add("cold-dose-equality", r, ["hold", "cold"], [60, 6, 16], "cold")
    return cases


def random_row(rng, index):
    r = base()
    r["order_id"] = f"order-{index:05d}"
    r["order_value"] = rng.choice([40, 80, 120, 200, 320])
    r["weight_kg"] = rng.choice([1, 2, 4, 7])
    r["legacy_risk_score"] = round(rng.random(), 3)
    r["deadline_hours"] = rng.randint(5, 20)
    r["ambient_units_per_hour"] = rng.choice([1, 2, 3, 5])
    r["cold_protection_hours"] = rng.choice([5, 8, 12, 16])
    r["cold_boxes_available"] = rng.random() > 0.15
    for mode, lower, upper in (("ground", 3, 14), ("cold", 1, 8)):
        minimum = rng.randint(lower, upper)
        r[mode] = {"open": rng.random() > 0.08, "min_hours": minimum,
                   "max_hours": minimum + rng.randint(0, 5)}
    budget = rng.choice([0, 5, 10, 20, 40, 80, 150])
    # Most lots are certified; corrections and draft revisions are substantial.
    status = rng.choices(["released", "quarantine", "revoked"], [90, 6, 4])[0]
    r["certificates"] = [
        {"revision": 1, "signed": True, "status": "released", "remaining_units": 150},
        {"revision": 2, "signed": True, "status": status, "remaining_units": budget}]
    if rng.random() < 0.35:
        r["certificates"].append({"revision": 3, "signed": False,
                                  "status": "released", "remaining_units": 150})
    if rng.random() < 0.04:
        r["certificates"] = []
    rng.shuffle(r["certificates"])
    return r


def main():
    history_rng = random.Random(73191)
    future_rng = random.Random(928417)
    history = []
    for i in range(480):
        r = random_row(history_rng, i)
        gt = history_rng.randint(r["ground"]["min_hours"], r["ground"]["max_hours"])
        ct = history_rng.randint(r["cold"]["min_hours"], r["cold"]["max_hours"])
        t = truth(r, gt, ct)
        action = "hold"
        if r["legacy_risk_score"] < 0.55:
            preferred = "cold" if r["order_value"] >= 120 else "ground"
            handling = 3 if preferred == "cold" else 1
            if preferred in t["allowed"] and r[preferred]["max_hours"] + handling <= r["deadline_hours"]:
                action = preferred
        transit = {"ground": gt, "cold": ct}.get(action)
        r.update(historical_action=action, observed_transit_hours=transit,
                 observed_on_time=None if transit is None else transit + (3 if action == "cold" else 1) <= r["deadline_hours"])
        history.append(r)
    frozen = []
    for i in range(1200):
        r = random_row(future_rng, i + 9000)
        gt = future_rng.randint(r["ground"]["min_hours"], r["ground"]["max_hours"])
        ct = future_rng.randint(r["cold"]["min_hours"], r["cold"]["max_hours"])
        frozen.append({"row": r, **truth(r, gt, ct)})
    for a in anchors():
        frozen.append({"row": a["row"], **truth(a["row"], a["ground_transit"], a["cold_transit"])})
    # Repeated identity with changing state catches decisions cached by order ID.
    recovery = base()
    recovery["order_id"] = "repeat-order-recovery"
    recovery["ground"]["open"] = True
    recovery["cold_boxes_available"] = False
    for stage in range(4):
        r = copy.deepcopy(recovery)
        if stage == 1:
            r["ground"]["open"] = False
        if stage == 2:
            r["certificates"].append({"revision": 2, "signed": True,
                                      "status": "revoked", "remaining_units": 16})
        if stage == 3:
            r["certificates"].extend([
                {"revision": 2, "signed": True, "status": "revoked", "remaining_units": 16},
                {"revision": 3, "signed": True, "status": "released", "remaining_units": 16}])
        frozen.append({"row": r, **truth(r, 7, 4)})
    (PUBLIC / "rows.json").write_text(json.dumps(history, indent=2) + "\n")
    (HERE / "future.json").write_text(json.dumps(frozen, separators=(",", ":")) + "\n")
    (HERE / "anchors.json").write_text(json.dumps(anchors(), indent=2) + "\n")


if __name__ == "__main__":
    main()
