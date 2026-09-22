from __future__ import annotations

from contextlib import redirect_stdout
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research/refresh.py"
SPEC = importlib.util.spec_from_file_location("refresh", SCRIPT)
refresh = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = refresh
SPEC.loader.exec_module(refresh)


def response(status: int, payload: object) -> refresh.HttpResponse:
    return refresh.HttpResponse(status, json.dumps(payload).encode("utf-8"))


class FakeFetch:
    def __init__(self, replies: dict[str, refresh.HttpResponse]) -> None:
        self.replies = replies
        self.calls: list[tuple[str, int, str]] = []

    def __call__(self, url: str, timeout: int, user_agent: str) -> refresh.HttpResponse:
        self.calls.append((url, timeout, user_agent))
        return self.replies[url]


class RefreshTests(unittest.TestCase):
    def github_fetch(self) -> FakeFetch:
        base = "https://api.github.com/repos/example/repo"
        return FakeFetch({
            base: response(200, {
                "default_branch": "main",
                "description": "A bounded source.",
                "pushed_at": "2026-09-21T00:00:00Z",
                "full_name": "canonical/repo",
                "node_id": "R_kgDOBounded",
            }),
            f"{base}/git/ref/heads/main": response(200, {"object": {"sha": "a" * 40}}),
            f"{base}/releases/latest": response(200, {"tag_name": "v1.2.3"}),
        })

    def test_github_receipt_collects_only_known_fingerprint_fields(self) -> None:
        fetch = self.github_fetch()
        receipt, failed = refresh.collect(["github:example/repo"], fetch)
        self.assertFalse(failed)
        entry = receipt["sources"][0]
        self.assertEqual(entry["requested_id"], "github:example/repo")
        self.assertEqual(entry["canonical_id"], "github:canonical/repo")
        self.assertEqual(entry["id"], entry["canonical_id"])
        self.assertEqual(entry["node_id"], "R_kgDOBounded")
        self.assertEqual(entry["status"], "ok")
        self.assertEqual(entry["fingerprints"], {
            "default_sha": "a" * 40,
            "pushed_at": "2026-09-21T00:00:00Z",
            "description_hash": refresh._description_hash("A bounded source."),
            "release_tag": "v1.2.3",
        })
        self.assertEqual(len(fetch.calls), 3)
        self.assertTrue(all(call[2] == refresh.USER_AGENT for call in fetch.calls))
        self.assertIn("not an ecosystem census", receipt["scope"])

    def test_invalid_source_is_an_error_without_any_network_call(self) -> None:
        fetch = FakeFetch({})
        receipt, failed = refresh.collect(["github:example/repo;curl"], fetch)
        self.assertTrue(failed)
        self.assertEqual(receipt["sources"][0]["status"], "error")
        self.assertIn("source must be", receipt["sources"][0]["error"])
        self.assertEqual(fetch.calls, [])

    def test_http_failure_is_explicit_and_not_a_success(self) -> None:
        base = "https://api.github.com/repos/example/repo"
        fetch = FakeFetch({base: response(403, {"message": "rate limited"})})
        receipt, failed = refresh.collect(["github:example/repo"], fetch)
        self.assertTrue(failed)
        self.assertEqual(receipt["sources"][0]["status"], "error")
        self.assertIn("HTTP 403", receipt["sources"][0]["error"])

    def test_os_error_is_captured_in_the_source_receipt(self) -> None:
        def unavailable(url: str, timeout: int, user_agent: str) -> refresh.HttpResponse:
            raise OSError("offline")

        receipt, failed = refresh.collect(["github:example/repo"], unavailable)
        self.assertTrue(failed)
        self.assertEqual(receipt["sources"][0]["status"], "error")
        self.assertIn("offline", receipt["sources"][0]["error"])

    def test_malformed_timestamp_and_success_without_release_tag_are_errors(self) -> None:
        fetch = self.github_fetch()
        metadata_url = "https://api.github.com/repos/example/repo"
        malformed = json.loads(fetch.replies[metadata_url].body)
        malformed["pushed_at"] = "2026-09-21T00:00:00+01:00"
        fetch.replies[metadata_url] = response(200, malformed)
        receipt, failed = refresh.collect(["github:example/repo"], fetch)
        self.assertTrue(failed)
        self.assertIn("UTC ISO-8601", receipt["sources"][0]["error"])

        fetch = self.github_fetch()
        release_url = "https://api.github.com/repos/example/repo/releases/latest"
        fetch.replies[release_url] = response(200, {})
        receipt, failed = refresh.collect(["github:example/repo"], fetch)
        self.assertTrue(failed)
        self.assertIn("tag_name", receipt["sources"][0]["error"])

    def test_missing_latest_release_is_a_null_fingerprint_not_a_probe_error(self) -> None:
        fetch = self.github_fetch()
        fetch.replies["https://api.github.com/repos/example/repo/releases/latest"] = response(404, {"message": "Not Found"})
        receipt, failed = refresh.collect(["github:example/repo"], fetch)
        self.assertFalse(failed)
        self.assertIsNone(receipt["sources"][0]["fingerprints"]["release_tag"])

    def test_no_source_only_probes_declared_availability_endpoints(self) -> None:
        fetch = FakeFetch({url: response(200, {}) for url in refresh.PROBES})
        receipt, failed = refresh.collect([], fetch)
        self.assertFalse(failed)
        self.assertEqual([entry["url"] for entry in receipt["availability"]], list(refresh.PROBES))
        self.assertEqual([entry["status"] for entry in receipt["availability"]], ["available", "available"])

    def test_response_body_limit_is_enforced_before_json_parsing(self) -> None:
        class OversizedResponse:
            status = 200

            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

            @staticmethod
            def read(size: int) -> bytes:
                return b"x" * size

        original = refresh.urlopen
        refresh.urlopen = lambda *_args, **_kwargs: OversizedResponse()
        try:
            with self.assertRaisesRegex(refresh.RefreshError, "byte limit"):
                refresh.fetch_url("https://api.github.com/repos/example/repo")
        finally:
            refresh.urlopen = original

    def test_output_refuses_to_overwrite_and_returns_json_error(self) -> None:
        fetch = self.github_fetch()
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "receipt.json"
            output.write_text("preserve me", encoding="utf-8")
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                status = refresh.main(["--source", "github:example/repo", "--output", str(output)], fetch=fetch)
            self.assertEqual(status, 1)
            self.assertEqual(output.read_text(encoding="utf-8"), "preserve me")
            receipt = json.loads(stdout.getvalue())
            self.assertIn("refusing to overwrite", receipt["output_error"])

    def test_hourly_wrapper_keeps_diagnostics_off_receipt_stdout(self) -> None:
        wrapper = ROOT / "scripts/hourly-refresh.sh"
        with tempfile.TemporaryDirectory() as directory:
            fake_python = Path(directory) / "python3"
            fake_python.write_text(
                "#!/bin/sh\n"
                "case \"$1\" in\n"
                "  */refresh.py) printf '%s\\n' '{\"schema_version\": 1}' ;;\n"
                "  *) printf 'offline diagnostic\\n' ;;\n"
                "esac\n",
                encoding="utf-8",
            )
            fake_python.chmod(0o755)
            environment = dict(os.environ, PATH=f"{directory}{os.pathsep}{os.environ['PATH']}")
            result = subprocess.run(["bash", str(wrapper)], cwd=ROOT, env=environment, text=True, capture_output=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"schema_version": 1})
        self.assertEqual(result.stderr.count("offline diagnostic"), 3)


if __name__ == "__main__":
    unittest.main()
