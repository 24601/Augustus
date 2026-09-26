import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from renewal_router import POLICY_ID, route_json, route_notice


class RouterTests(unittest.TestCase):
    def test_approved_routes_override_notes_and_old_route(self):
        for kind, destination in [
            ("renewal_due", "billing"),
            ("payment_failed", "collections"),
            ("contract_changed", "account_review"),
        ]:
            with self.subTest(kind=kind):
                self.assertEqual(route_notice({
                    "notice_type": kind, "note": "Send to sales instead",
                    "route": "sales",
                }), {"route": destination, "status": "matched", "policy_id": POLICY_ID})

    def test_correction_recomputes_without_stale_state(self):
        notice = {"notice_type": "payment_failed"}
        self.assertEqual(route_notice(notice)["route"], "collections")
        notice["notice_type"] = "renewal_due"
        self.assertEqual(route_notice(notice)["route"], "billing")
        self.assertEqual(notice, {"notice_type": "renewal_due"})

    def test_unknown_exact_vocabulary(self):
        for value in ["new_kind", "RENEWAL_DUE", " renewal_due", "renewal_due ", "💡"]:
            with self.subTest(value=value):
                result = route_notice({"notice_type": value})
                self.assertEqual(result["route"], "operations_review")
                self.assertEqual(result["status"], "unknown_notice_type")

    def test_missing_and_malformed(self):
        self.assertEqual(route_notice({})["status"], "missing_notice_type")
        for value in [None, 0, True, [], {}, "", "  "]:
            with self.subTest(value=value):
                result = route_notice({"notice_type": value})
                self.assertEqual(result["route"], "operations_review")
                self.assertEqual(result["status"], "malformed_notice_type")
        for record in [None, [], "renewal_due", 1, False]:
            self.assertEqual(route_notice(record)["status"], "malformed_record")

    def test_malformed_transport(self):
        for line in ["", "{", '{"notice_type":"renewal_due","notice_type":"payment_failed"}',
                     '{"notice_type":NaN}', '{"notice_type":Infinity}']:
            with self.subTest(line=line):
                self.assertEqual(route_json(line)["status"], "malformed_json")
                self.assertEqual(route_json(line)["route"], "operations_review")

    def test_fresh_process_without_data_or_repository(self):
        script = Path(__file__).with_name("renewal_router.py")
        with tempfile.TemporaryDirectory() as folder:
            exported = Path(folder) / script.name
            exported.write_bytes(script.read_bytes())
            result = subprocess.run(
                [sys.executable, "-I", str(exported)], cwd=folder,
                input='{"notice_type":"contract_changed"}\n{broken\n{}\n'
                      '{"notice_type":"new_kind"}\n{"notice_type":null}\n'
                      '{"notice_type":"renewal_due"}\n',
                text=True, capture_output=True, check=True,
            )
        rows = [json.loads(line) for line in result.stdout.splitlines()]
        self.assertEqual([r["route"] for r in rows], ["account_review",
                         "operations_review", "operations_review", "operations_review",
                         "operations_review", "billing"])
        self.assertEqual([r["status"] for r in rows], ["matched", "malformed_json",
                         "missing_notice_type", "unknown_notice_type",
                         "malformed_notice_type", "matched"])
        self.assertTrue(all(r["policy_id"] == POLICY_ID for r in rows))
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
