"""Local renewal routing policy. Standard library only; no external effects."""

import json
import sys
from types import MappingProxyType

POLICY_ID = "renewal-authoritative-v1"
ROUTES = MappingProxyType({
    "renewal_due": "billing",
    "payment_failed": "collections",
    "contract_changed": "account_review",
})


def route_notice(record: object) -> dict[str, str]:
    """Return a destination, not an executed transfer. Notes cannot override policy."""
    result = {
        "route": "operations_review",
        "status": "malformed_record",
        "policy_id": POLICY_ID,
    }
    if not isinstance(record, dict):
        return result
    if "notice_type" not in record:
        result["status"] = "missing_notice_type"
        return result
    value = record["notice_type"]
    if not isinstance(value, str) or not value.strip():
        result["status"] = "malformed_notice_type"
    elif value in ROUTES:
        result.update(route=ROUTES[value], status="matched")
    else:
        result["status"] = "unknown_notice_type"
    return result


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError("non-JSON numeric constant")


def route_json(line: str) -> dict[str, str]:
    try:
        record = json.loads(line, object_pairs_hook=unique_object,
                            parse_constant=reject_constant)
    except (ValueError, RecursionError):
        return {"route": "operations_review", "status": "malformed_json",
                "policy_id": POLICY_ID}
    return route_notice(record)


def main() -> None:
    """One output per input line, including malformed lines; continue after errors."""
    for line in sys.stdin:
        print(json.dumps(route_json(line), allow_nan=False))


if __name__ == "__main__":
    main()
