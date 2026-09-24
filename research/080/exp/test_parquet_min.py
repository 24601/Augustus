"""Check the stdlib Parquet reader against pyarrow, which is the only oracle worth having.

Skipped when pyarrow is absent, which is the whole reason the reader exists: on
tabputer-1 `augctl` has no pyarrow, may not install one, and may not run a
container. It is NOT skipped here to be convenient — a reader that has never
been compared against a real implementation has no business touching a corpus
whose labels decide an experiment.

Run where pyarrow is available:
    python3 -m unittest research.080.exp.test_parquet_min   (or directly)
"""

from __future__ import annotations

import importlib.util
import random
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "parquet_min.py"
SPEC = importlib.util.spec_from_file_location("parquet_min", SCRIPT)
parquet_min = importlib.util.module_from_spec(SPEC)
sys.modules["parquet_min"] = parquet_min
SPEC.loader.exec_module(parquet_min)

try:
    import pyarrow as pa
    import pyarrow.parquet as pq
except ImportError:  # pragma: no cover
    pa = None


def sample_table(n: int = 5_000):
    rng = random.Random(11)
    return pa.table({
        # repeated values so the writer chooses dictionary encoding, and
        # non-ASCII so a byte-level mistake shows up rather than hiding
        "text": [f"comment {rng.randrange(400)} ünïcødé ✓ {i}" for i in range(n)],
        "toxicity": [round(rng.random(), 4) for _ in range(n)],
        "row_id": list(range(n)),
        "flag": [rng.random() < 0.3 for _ in range(n)],
        "opt": [None if rng.random() < 0.1 else f"maybe-{i}" for i in range(n)],
    })


@unittest.skipIf(pa is None, "pyarrow is unavailable; nothing to check against")
class ParquetReaderTests(unittest.TestCase):
    def assert_round_trip(self, table, path, columns=None):
        got = parquet_min.read_table(path, columns)
        for name in (columns or table.column_names):
            want = table.column(name).to_pylist()
            if name == "toxicity":
                for a, b in zip(got[name], want):
                    self.assertAlmostEqual(a, b, places=9)
            else:
                self.assertEqual(got[name], want, f"column {name}")

    def test_every_codec_and_encoding_matches_pyarrow(self):
        table = sample_table()
        for compression in ("snappy", "gzip", "none"):
            for use_dictionary in (True, False):
                with self.subTest(compression=compression, dictionary=use_dictionary):
                    with tempfile.TemporaryDirectory() as directory:
                        path = Path(directory) / "t.parquet"
                        pq.write_table(table, path, compression=compression,
                                       version="1.0", use_dictionary=use_dictionary)
                        self.assert_round_trip(table, path)

    def test_multiple_row_groups_concatenate_in_order(self):
        table = sample_table()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "rg.parquet"
            pq.write_table(table, path, compression="snappy", row_group_size=700)
            self.assert_round_trip(table, path, ["text", "row_id"])

    def test_nulls_in_an_optional_column_land_in_the_right_places(self):
        table = sample_table()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "n.parquet"
            pq.write_table(table, path, compression="snappy")
            got = parquet_min.read_table(path, ["opt"])["opt"]
            want = table.column("opt").to_pylist()
            self.assertEqual([i for i, v in enumerate(got) if v is None],
                             [i for i, v in enumerate(want) if v is None])

    def test_a_missing_column_is_refused_by_name(self):
        table = sample_table(100)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "m.parquet"
            pq.write_table(table, path)
            with self.assertRaises(parquet_min.ParquetUnsupported):
                parquet_min.read_table(path, ["no_such_column"])

    def test_a_nested_schema_is_refused_rather_than_guessed_at(self):
        """A silently misread nested column would corrupt a label, and no
        downstream check would catch it."""
        nested = pa.table({"outer": [{"inner": 1}, {"inner": 2}]})
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nested.parquet"
            pq.write_table(nested, path)
            with self.assertRaises(parquet_min.ParquetUnsupported):
                parquet_min.read_table(path)

    def test_a_non_parquet_file_is_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "not.parquet"
            path.write_bytes(b"this is not a parquet file")
            with self.assertRaises(parquet_min.ParquetUnsupported):
                parquet_min.read_table(path)


if __name__ == "__main__":
    unittest.main()
