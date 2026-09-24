#!/usr/bin/env python3
"""Fetch pinned files of one Hugging Face model revision with the stdlib, verifying every hash.

Runs as ``augexp`` on tabputer-1 during an open setup window. HTTPS_PROXY must point at the
local augproxy, because the nft table drops everything else. Each file is checked against the
revision's API metadata: sha256 for LFS/Xet files, and the git blob sha1 for small files. The
output directory receives MANIFEST.json with the repo, revision, per-file sizes and hashes.
No token is read or sent, and no third-party package is used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import urllib.request
from urllib.parse import quote

API = "https://huggingface.co/api/models/{repo}/revision/{rev}?blobs=true"
RESOLVE = "https://huggingface.co/{repo}/resolve/{rev}/{path}"


def get(url: str, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": "augustus-080-hf-fetch/1"})
    return urllib.request.urlopen(req, timeout=timeout)


def git_blob_sha1(path: str) -> str:
    h = hashlib.sha1()
    h.update(b"blob %d\0" % os.path.getsize(path))
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 22), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--rev", required=True, help="full 40-hex commit sha")
    ap.add_argument("--out", required=True)
    ap.add_argument("--files", nargs="+", required=True)
    args = ap.parse_args()
    if len(args.rev) != 40 or any(c not in "0123456789abcdef" for c in args.rev):
        raise SystemExit("--rev must be a full commit sha")
    if not os.environ.get("HTTPS_PROXY", os.environ.get("https_proxy", "")).startswith("http://127.0.0.1:3128"):
        raise SystemExit("HTTPS_PROXY must be http://127.0.0.1:3128")
    with get(API.format(repo=args.repo, rev=args.rev)) as r:
        meta = json.load(r)
    if meta.get("sha") != args.rev:
        raise SystemExit(f"API returned revision {meta.get('sha')}, not {args.rev}")
    siblings = {s["rfilename"]: s for s in meta["siblings"]}
    os.makedirs(args.out, exist_ok=True)
    manifest = {"repo": args.repo, "revision": args.rev, "files": {}}
    for path in args.files:
        s = siblings.get(path)
        if s is None:
            raise SystemExit(f"{path} is not in {args.repo}@{args.rev}")
        dest = os.path.join(args.out, path)
        os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
        part = dest + ".part"
        url = RESOLVE.format(repo=args.repo, rev=args.rev, path=quote(path))
        with get(url, timeout=120) as r, open(part, "wb") as f:
            for chunk in iter(lambda: r.read(1 << 22), b""):
                f.write(chunk)
        size = os.path.getsize(part)
        want_size = s.get("size")
        lfs = s.get("lfs") or {}
        rec = {"size": size}
        if want_size is not None and size != want_size:
            os.unlink(part)
            raise SystemExit(f"{path}: size {size} != {want_size}")
        if lfs.get("sha256"):
            got = sha256(part)
            if got != lfs["sha256"]:
                os.unlink(part)
                raise SystemExit(f"{path}: sha256 mismatch")
            rec["sha256"] = got
        elif s.get("blobId"):
            got = git_blob_sha1(part)
            if got != s["blobId"]:
                os.unlink(part)
                raise SystemExit(f"{path}: git blob sha1 mismatch")
            rec["git_sha1"] = got
            rec["sha256"] = sha256(part)
        else:
            os.unlink(part)
            raise SystemExit(f"{path}: API gave no hash to verify against")
        os.replace(part, dest)
        manifest["files"][path] = rec
        print(f"ok {path} {size}", flush=True)
    with open(os.path.join(args.out, "MANIFEST.json"), "w") as f:
        json.dump(manifest, f, indent=1, sort_keys=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
