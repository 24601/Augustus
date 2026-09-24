from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / ".agents/skills/augustus/scripts/provenance_gate.py"
SPEC = importlib.util.spec_from_file_location("provenance_gate", SCRIPT)
gate = importlib.util.module_from_spec(SPEC)
sys.modules["provenance_gate"] = gate
SPEC.loader.exec_module(gate)


def graph(*, nodes, edges, use="train a routing head", artifact="checkpoint-1", **extra):
    return {
        "schema_version": 1, "use": use, "training_artifact": artifact,
        "nodes": [{"id": artifact, "kind": "checkpoint"}] + list(nodes),
        "edges": list(edges), **extra,
    }


def jev(identity="jev", provider="typesafe"):
    return {"id": identity, "kind": "external_model", "provider": provider,
            "model": "jev-1.13", "revision": "2026-09-19", "channel": "hosted_api"}


class ProvenanceGateTests(unittest.TestCase):
    def verdicts(self, document):
        return {(f["node"], f["verdict"]) for f in gate.resolve(document)["findings"]}

    def test_a_jev_labeled_corpus_is_refused_by_declared_provider(self):
        document = graph(
            nodes=[{"id": "corpus", "kind": "corpus"}, jev()],
            edges=[{"type": "trained_on", "from": "checkpoint-1", "to": "corpus"},
                   {"type": "labeled_by", "from": "corpus", "to": "jev"}],
        )
        result = gate.resolve(document)
        self.assertEqual(result["assessment"], "refused")
        finding = result["findings"][0]
        self.assertEqual(finding["reason"], "typesafe_output_in_training_path")
        self.assertIn("2.3(b)", finding["clause"])
        self.assertEqual(finding["path_to_training_artifact"],
                         ["checkpoint-1", "-trained_on->", "corpus", "-labeled_by->", "jev"])

    def test_every_training_use_edge_reaches_the_refusal_not_only_labeling(self):
        """Reward, preference and relabel edges are training uses too."""
        for edge in ("rewarded_by", "preferred_by", "relabeled_by", "selected_by",
                     "filtered_by", "featurized_by", "generated_by"):
            with self.subTest(edge=edge):
                document = graph(
                    nodes=[{"id": "corpus", "kind": "corpus"}, jev()],
                    edges=[{"type": "trained_on", "from": "checkpoint-1", "to": "corpus"},
                           {"type": edge, "from": "corpus", "to": "jev"}],
                )
                self.assertEqual(gate.resolve(document)["assessment"], "refused")

    def test_identity_resolves_by_lineage_not_by_name(self):
        """A model named Jev with a declared non-TypeSafe base is not TypeSafe;
        a human label in a field named jev is a human label."""
        document = graph(
            nodes=[
                {"id": "corpus", "kind": "corpus"},
                {"id": "jev-omni", "kind": "external_model", "provider": "akhilaaa3",
                 "model": "Jev-Omni", "revision": "c050d513", "channel": "open_weights"},
                {"id": "jev", "kind": "label", "labeler": "human adjudication panel"},
            ],
            edges=[{"type": "trained_on", "from": "checkpoint-1", "to": "corpus"},
                   {"type": "derived_from", "from": "corpus", "to": "jev-omni"},
                   {"type": "labeled_by", "from": "corpus", "to": "jev"}],
        )
        result = gate.resolve(document)
        self.assertNotEqual(result["assessment"], "refused")
        self.assertIn(("jev-omni", "recorded"), self.verdicts(document))

    def test_a_jev_omni_style_model_with_undisclosed_parents_is_unknown(self):
        document = graph(
            nodes=[{"id": "corpus", "kind": "corpus", "parents_complete": False},
                   {"id": "jev-omni", "kind": "external_model", "provider": "akhilaaa3",
                    "model": "Jev-Omni", "revision": "c050d513", "channel": "open_weights"}],
            edges=[{"type": "trained_on", "from": "checkpoint-1", "to": "corpus"},
                   {"type": "derived_from", "from": "corpus", "to": "jev-omni"}],
        )
        result = gate.resolve(document)
        self.assertEqual(result["assessment"], "unknown_lineage")
        self.assertIn(("corpus", "unknown"), self.verdicts(document))

    def test_a_named_hosted_non_typesafe_teacher_passes_with_provenance_recorded(self):
        """Decision 12: pass through, record, and assert no terms."""
        document = graph(
            nodes=[{"id": "corpus", "kind": "corpus"},
                   {"id": "teacher", "kind": "external_model", "provider": "openai",
                    "model": "some-teacher", "revision": "2026-08-01", "channel": "hosted_api"}],
            edges=[{"type": "trained_on", "from": "checkpoint-1", "to": "corpus"},
                   {"type": "labeled_by", "from": "corpus", "to": "teacher"}],
        )
        result = gate.resolve(document)
        self.assertEqual(result["assessment"], "declared_provenance_recorded")
        finding = next(f for f in result["findings"] if f["node"] == "teacher")
        self.assertEqual(finding["verdict"], "recorded")
        self.assertEqual(finding["declared"]["revision"], "2026-08-01")
        self.assertIn("no provider terms are read or asserted except TypeSafe's", finding["note"])

    def test_an_unnamed_teacher_is_unknown_because_nothing_can_be_recorded(self):
        document = graph(
            nodes=[{"id": "corpus", "kind": "corpus"},
                   {"id": "teacher", "kind": "external_model", "provider": "unstated",
                    "model": "roughly 4B class", "channel": "hosted_api"}],
            edges=[{"type": "trained_on", "from": "checkpoint-1", "to": "corpus"},
                   {"type": "labeled_by", "from": "corpus", "to": "teacher"}],
        )
        result = gate.resolve(document)
        self.assertEqual(result["assessment"], "unknown_lineage")
        finding = next(f for f in result["findings"] if f["node"] == "teacher")
        self.assertEqual(finding["missing"], ["revision"])

    def test_an_absent_declared_parent_is_a_lineage_gap_not_a_malformed_graph(self):
        document = graph(
            nodes=[{"id": "corpus", "kind": "corpus"}],
            edges=[{"type": "trained_on", "from": "checkpoint-1", "to": "corpus"},
                   {"type": "derived_from", "from": "corpus", "to": "upstream-we-never-saw"}],
        )
        result = gate.resolve(document)
        self.assertEqual(result["assessment"], "unknown_lineage")
        finding = next(f for f in result["findings"] if f["node"] == "corpus")
        self.assertEqual(finding["missing_parents"], ["upstream-we-never-saw"])

    def test_nodes_outside_the_training_artifact_ancestry_are_not_judged(self):
        """A Jev comparator that never feeds training is not a training use."""
        document = graph(
            nodes=[{"id": "corpus", "kind": "corpus"}, jev(),
                   {"id": "eval-record", "kind": "corpus"}],
            edges=[{"type": "trained_on", "from": "checkpoint-1", "to": "corpus"},
                   {"type": "generated_by", "from": "eval-record", "to": "jev"}],
        )
        result = gate.resolve(document)
        self.assertEqual(result["assessment"], "declared_provenance_recorded")
        self.assertEqual(result["reachable_nodes"], 2)

    def test_a_declared_cycle_terminates(self):
        document = graph(
            nodes=[{"id": "a", "kind": "corpus"}, {"id": "b", "kind": "corpus"}],
            edges=[{"type": "trained_on", "from": "checkpoint-1", "to": "a"},
                   {"type": "derived_from", "from": "a", "to": "b"},
                   {"type": "derived_from", "from": "b", "to": "a"}],
        )
        self.assertEqual(gate.resolve(document)["reachable_nodes"], 3)

    def test_malformed_graphs_are_errors_not_verdicts(self):
        cases = {
            "schema_version": {"schema_version": 2},
            "kind": {"nodes": [{"id": "checkpoint-1", "kind": "not-a-kind"}]},
            "type": {"edges": [{"type": "inspired_by", "from": "checkpoint-1", "to": "checkpoint-1"}]},
            "duplicate node id": {"nodes": [{"id": "checkpoint-1", "kind": "checkpoint"},
                                            {"id": "checkpoint-1", "kind": "corpus"}]},
            "training_artifact is not a node": {"training_artifact": "absent"},
        }
        for message, override in cases.items():
            with self.subTest(case=message):
                document = graph(nodes=[], edges=[])
                document.update(override)
                with self.assertRaisesRegex(ValueError, message):
                    gate.resolve(document)

    def test_cli_reports_the_input_hash_and_fails_cleanly(self):
        document = graph(nodes=[{"id": "corpus", "kind": "corpus"}],
                         edges=[{"type": "trained_on", "from": "checkpoint-1", "to": "corpus"}])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "graph.json"
            path.write_text(json.dumps(document), encoding="utf-8")
            run = subprocess.run([sys.executable, str(SCRIPT), str(path)],
                                 capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(json.loads(run.stdout)["input_sha256"],
                             __import__("hashlib").sha256(path.read_bytes()).hexdigest())
            path.write_text("{not json", encoding="utf-8")
            broken = subprocess.run([sys.executable, str(SCRIPT), str(path)],
                                    capture_output=True, text=True)
            self.assertEqual(broken.returncode, 2)
            self.assertNotIn("Traceback", broken.stderr)


if __name__ == "__main__":
    unittest.main()
