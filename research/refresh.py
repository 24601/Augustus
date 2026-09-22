#!/usr/bin/env python3
"""Collect a read-only, bounded refresh receipt.

With ``--source github:OWNER/REPO`` this probes only repository metadata, the
current default-branch revision, and the latest release. With no sources it
probes TypeSafe documentation and eval-site availability only. It is not an
ecosystem census, discovery mechanism, authentication check, or model-status
claim. Discovery and interpretation remain separate research work.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any, Callable, Sequence
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


USER_AGENT = "Augustus-refresh-probe/1.0"
DEFAULT_TIMEOUT_SECONDS = 15
MAX_RESPONSE_BYTES = 256 * 1024
GITHUB_SOURCE_RE = re.compile(r"^github:([A-Za-z0-9](?:[A-Za-z0-9-]{0,38}))/([A-Za-z0-9][A-Za-z0-9._-]{0,99})$")
FULL_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
PROBES = ("https://docs.typesafe.ai/llms.txt", "https://evals.typesafe.ai/")


@dataclass(frozen=True)
class HttpResponse:
    status: int
    body: bytes


Fetch = Callable[[str, int, str], HttpResponse]


class RefreshError(RuntimeError):
    pass


def validate_source(value: str) -> tuple[str, str, str]:
    """Return a validated source id and GitHub path components.

    Only a GitHub owner/repository identifier is accepted: not a URL, shell
    fragment, local path, or arbitrary API endpoint.
    """
    match = GITHUB_SOURCE_RE.fullmatch(value)
    if match is None:
        raise ValueError("source must be github:OWNER/REPO with a valid GitHub owner and repository name")
    owner, repo = match.groups()
    return f"github:{owner}/{repo}", owner, repo


def fetch_url(url: str, timeout: int = DEFAULT_TIMEOUT_SECONDS, user_agent: str = USER_AGENT) -> HttpResponse:
    request = Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": user_agent})
    try:
        with urlopen(request, timeout=timeout) as response:  # nosec B310: URLs are fixed or validated GitHub paths.
            return HttpResponse(status=response.status, body=_read_limited(response.read))
    except HTTPError as exc:
        return HttpResponse(status=exc.code, body=_read_limited(exc.read))
    except URLError as exc:
        raise RefreshError(f"network error: {exc.reason}") from exc
    except TimeoutError as exc:
        raise RefreshError("network timeout") from exc
    except OSError as exc:
        raise RefreshError(f"network error: {exc}") from exc


def _read_limited(reader: Callable[[int], bytes]) -> bytes:
    body = reader(MAX_RESPONSE_BYTES + 1)
    if len(body) > MAX_RESPONSE_BYTES:
        raise RefreshError(f"response body exceeds {MAX_RESPONSE_BYTES} byte limit")
    return body


def _json(response: HttpResponse, context: str) -> dict[str, Any]:
    if not 200 <= response.status < 300:
        raise RefreshError(f"{context}: HTTP {response.status}")
    try:
        value = json.loads(response.body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RefreshError(f"{context}: invalid JSON response") from exc
    if not isinstance(value, dict):
        raise RefreshError(f"{context}: expected a JSON object")
    return value


def _description_hash(value: str | None) -> str | None:
    return None if value is None else hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]


def _utc_timestamp(value: Any, context: str) -> str:
    if not isinstance(value, str) or not value.endswith("Z"):
        raise RefreshError(f"{context}: expected a UTC ISO-8601 timestamp ending in Z")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise RefreshError(f"{context}: expected a UTC ISO-8601 timestamp ending in Z") from exc
    if parsed.tzinfo is None or parsed.utcoffset() != timedelta(0):
        raise RefreshError(f"{context}: expected a UTC ISO-8601 timestamp ending in Z")
    return value


def collect_github(source: str, fetch: Fetch = fetch_url) -> dict[str, Any]:
    source_id, owner, repo = validate_source(source)
    base = f"https://api.github.com/repos/{quote(owner, safe='')}/{quote(repo, safe='')}"
    metadata = _json(fetch(base, DEFAULT_TIMEOUT_SECONDS, USER_AGENT), "repository metadata")
    branch = metadata.get("default_branch")
    if not isinstance(branch, str) or not branch:
        raise RefreshError("repository metadata: missing default_branch")
    description = metadata.get("description")
    if description is not None and not isinstance(description, str):
        raise RefreshError("repository metadata: description must be text or null")
    pushed_at = _utc_timestamp(metadata.get("pushed_at"), "repository metadata pushed_at")
    full_name = metadata.get("full_name")
    node_id = metadata.get("node_id")
    if not isinstance(full_name, str):
        raise RefreshError("repository metadata: missing canonical full_name")
    canonical_id, _, _ = validate_source(f"github:{full_name}")
    if not isinstance(node_id, str) or not node_id:
        raise RefreshError("repository metadata: missing canonical node_id")

    ref = _json(fetch(f"{base}/git/ref/heads/{quote(branch, safe='')}", DEFAULT_TIMEOUT_SECONDS, USER_AGENT), "default branch reference")
    obj = ref.get("object")
    sha = obj.get("sha") if isinstance(obj, dict) else None
    if not isinstance(sha, str) or not FULL_SHA_RE.fullmatch(sha):
        raise RefreshError("default branch reference: expected a full lowercase 40-character SHA")

    release_response = fetch(f"{base}/releases/latest", DEFAULT_TIMEOUT_SECONDS, USER_AGENT)
    if release_response.status == 404:
        release_tag = None
    else:
        release = _json(release_response, "latest release")
        tag = release.get("tag_name")
        if not isinstance(tag, str) or not tag.strip():
            raise RefreshError("latest release: missing non-empty tag_name")
        release_tag = tag

    return {
        "id": canonical_id,
        "requested_id": source_id,
        "canonical_id": canonical_id,
        "canonical_full_name": full_name,
        "node_id": node_id,
        "status": "ok",
        "default_branch": branch,
        "fingerprints": {
            "default_sha": sha,
            "pushed_at": pushed_at,
            "description_hash": _description_hash(description),
            "release_tag": release_tag,
        },
        "review": "pending-review",
    }


def probe(url: str, fetch: Fetch = fetch_url) -> dict[str, Any]:
    try:
        response = fetch(url, DEFAULT_TIMEOUT_SECONDS, USER_AGENT)
        if 200 <= response.status < 400:
            return {"url": url, "status": "available", "http_status": response.status}
        return {"url": url, "status": "error", "http_status": response.status, "error": f"HTTP {response.status}"}
    except (RefreshError, OSError) as exc:
        return {"url": url, "status": "error", "error": str(exc)}


def collect(sources: Sequence[str], fetch: Fetch = fetch_url) -> tuple[dict[str, Any], bool]:
    receipt: dict[str, Any] = {
        "schema_version": 1,
        "collected_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "scope": "read-only availability and source metadata probe; not an ecosystem census, discovery result, or model-status claim",
        "sources": [],
    }
    failed = False
    if sources:
        entries = []
        for source in sources:
            try:
                entries.append(collect_github(source, fetch))
            except (ValueError, RefreshError, OSError) as exc:
                failed = True
                entries.append({"requested_id": source, "status": "error", "error": str(exc), "review": "pending-review"})
        receipt["sources"] = entries
    else:
        availability = [probe(url, fetch) for url in PROBES]
        receipt["availability"] = availability
        failed = any(entry["status"] == "error" for entry in availability)
    return receipt, failed


def _write_new(path: Path, payload: str) -> None:
    try:
        with path.open("x", encoding="utf-8") as output:
            output.write(payload)
    except FileExistsError as exc:
        raise RefreshError(f"refusing to overwrite existing output: {path}") from exc
    except OSError as exc:
        raise RefreshError(f"cannot write output {path}: {exc}") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", action="append", default=[], metavar="github:OWNER/REPO", help="read-only GitHub source probe; repeatable")
    parser.add_argument("--output", type=Path, help="create this receipt file once; refuses to overwrite")
    return parser


def main(argv: Sequence[str] | None = None, *, fetch: Fetch = fetch_url) -> int:
    args = build_parser().parse_args(argv)
    receipt, failed = collect(args.source, fetch)
    payload = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        sys.stdout.write(payload)
    else:
        try:
            _write_new(args.output, payload)
        except RefreshError as exc:
            receipt["output_error"] = str(exc)
            sys.stdout.write(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
            return 1
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
