import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research/revisit_fingerprints.py"
SPEC = importlib.util.spec_from_file_location("revisit_fingerprints", SCRIPT)
fingerprints = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(fingerprints)


def record(**overrides):
    fp = {
        "default_sha": "a" * 40,
        "pushed_at": "2026-09-21T00:00:00Z",
        "description_hash": fingerprints.description_hash("original"),
        "release_tag": None,
    }
    fp.update(overrides)
    return {"id": "github:example/source", "fingerprints": fp}


class RevisitFingerprintTests(unittest.TestCase):
    def test_classify_rejects_missing_and_truncated_fingerprints(self):
        missing = record()
        del missing["fingerprints"]["release_tag"]
        with self.assertRaisesRegex(ValueError, "missing release_tag"):
            fingerprints.classify(record(), missing)

        with self.assertRaisesRegex(ValueError, "40-character"):
            fingerprints.classify(record(), record(default_sha="a" * 12))

    def test_classify_rejects_cross_source_and_malformed_timestamps(self):
        other = record()
        other["id"] = "github:example/other"
        with self.assertRaisesRegex(ValueError, "ids differ"):
            fingerprints.classify(record(), other)

        with self.assertRaisesRegex(ValueError, "ISO-8601"):
            fingerprints.classify(record(), record(pushed_at="not-a-time"))

        with self.assertRaisesRegex(ValueError, "ISO-8601 UTC"):
            fingerprints.classify(record(), record(pushed_at="2026-01-01Z"))

    def test_classify_requires_complete_matching_identity_or_bare_fingerprints(self):
        observed = record()
        del observed["id"]
        with self.assertRaisesRegex(ValueError, "both be present or both be absent"):
            fingerprints.classify(record(), observed)

        null_id = record()
        null_id["id"] = None
        with self.assertRaisesRegex(ValueError, "stored id must be a non-empty string"):
            fingerprints.classify(null_id, record())

        bare = record()["fingerprints"]
        self.assertEqual(fingerprints.classify(bare, dict(bare))["grade"], "unchanged")

    def test_fingerprint_move_requests_review_and_signal_makes_it_material(self):
        moved = fingerprints.classify(record(), record(default_sha="b" * 40))
        self.assertEqual(moved["grade"], "review")
        self.assertEqual(moved["action"], "inspect_diff")
        self.assertFalse(moved["capability_change_claimed"])

        material = fingerprints.classify(
            record(), record(default_sha="b" * 40), material_signals=("readme",)
        )
        self.assertEqual(material["grade"], "material")
        self.assertEqual(material["action"], "densify")

        before = record()
        before["stargazers_count"] = 1
        after = record()
        after["stargazers_count"] = 2
        noise = fingerprints.classify(before, after)
        self.assertEqual(noise["grade"], "star_noise")
        self.assertEqual(noise["action"], "pulse_only")

    def test_node_identity_conflict_cannot_be_classified_as_unchanged(self):
        stored = dict(record(), node_id="R_original")
        with self.assertRaisesRegex(ValueError, "node_id.*differ"):
            fingerprints.classify(stored, dict(record(), node_id="R_replacement"))
        self.assertEqual(fingerprints.classify(stored, dict(stored))["grade"], "unchanged")
        # Legacy stores may lack a node ID. Absence is not a contradiction.
        self.assertEqual(fingerprints.classify(record(), stored)["grade"], "unchanged")
        for invalid in (None, "", True, 5):
            with self.subTest(invalid=invalid), self.assertRaisesRegex(ValueError, "node_id"):
                fingerprints.classify(stored, dict(record(), node_id=invalid))

    def test_store_schema_version_requires_integer_not_bool_or_float(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "store.json"
            for version in (True, 1.0, "1"):
                path.write_text(json.dumps({"schema_version": version,
                                           "stored_fields": list(fingerprints.STORED_FIELDS),
                                           "looks": []}))
                with self.subTest(version=version), self.assertRaisesRegex(ValueError, "schema_version"):
                    fingerprints.load_store(path)

    def test_duplicate_store_keys_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "store.json"
            content = json.dumps({"schema_version": 1, "stored_fields": list(fingerprints.STORED_FIELDS), "looks": []})
            path.write_text(content[:-1] + ',"schema_version":1}')
            with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
                fingerprints.load_store(path)

    def test_unknown_fingerprint_value_requests_review_without_capability_claim(self):
        unknown = fingerprints.classify(record(), record(description_hash=None))
        self.assertEqual(unknown["grade"], "review")
        self.assertFalse(unknown["capability_change_claimed"])

    def test_current_store_is_schema_valid_without_pinned_observations(self):
        store = fingerprints.load_store()
        self.assertIsInstance(store["looks"], list)

    def test_description_hash_requires_text(self):
        with self.assertRaisesRegex(ValueError, "must be a string"):
            fingerprints.description_hash(None)


if __name__ == "__main__":
    unittest.main()
