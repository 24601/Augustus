"""Development-only known-good implementation. Not distributed to task agents."""


def fit(rows, config):
    return dict(config)


def decide(artifact, row):
    c = artifact
    prices = {"hold": c["hold_base"] + c["hold_value_fraction"] * row["order_value"]}
    signed = [r for r in row["certificates"] if r["signed"]]
    cert = max(signed, key=lambda r: r["revision"]) if signed else None
    if not cert or cert["status"] != "released":
        return "hold"
    for action in ("ground", "cold"):
        route = row[action]
        if not route["open"] or (action == "cold" and not row["cold_boxes_available"]):
            continue
        handling = c[action + "_handling_hours"]
        exposure = handling + route["max_hours"]
        if action == "cold":
            exposure = max(0, exposure - row["cold_protection_hours"])
        if exposure * row["ambient_units_per_hour"] > cert["remaining_units"]:
            continue
        arrivals = range(route["min_hours"] + handling, route["max_hours"] + handling + 1)
        late = sum(t > row["deadline_hours"] for t in arrivals) / len(arrivals)
        prices[action] = (
            c[action + "_base"] + c[action + "_per_kg"] * row["weight_kg"]
            + late * (c["late_base"] + c["late_value_fraction"] * row["order_value"])
        )
    return min(prices, key=lambda action: (prices[action], action))
