#!/usr/bin/env bash
# A scheduler may choose cadence. This wrapper performs deterministic offline
# validation, then emits a read-only refresh receipt; it never writes Git or
# research baselines unless the caller explicitly asks the collector for a new
# receipt path.
set -euo pipefail

AUGUSTUS_ROOT="$(CDPATH='' cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$AUGUSTUS_ROOT/scripts/check_repo.py" >&2
python3 "$AUGUSTUS_ROOT/.agents/skills/augustus/scripts/evaluate_decisions.py" --self-test >&2
python3 "$AUGUSTUS_ROOT/research/revisit_fingerprints.py" --self-test >&2
exec "$AUGUSTUS_ROOT/scripts/refresh-jev-research.sh" "$@"
