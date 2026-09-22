#!/usr/bin/env bash
# Read-only receipt collector. Discovery and research interpretation are
# separate work; this script never edits a baseline, Git state, or archive.
set -euo pipefail

AUGUSTUS_ROOT="$(CDPATH='' cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
exec python3 "$AUGUSTUS_ROOT/research/refresh.py" "$@"
