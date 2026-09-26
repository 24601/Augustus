#!/usr/bin/env python3
"""Compatibility entry point for the former uniqueness-overlay gate.

The historical overlay corpus is preserved by the research archive manifest;
runtime quality now has bounded structural checks instead of copying archive
substrings into every public overlay.
"""

from __future__ import annotations

from pathlib import Path
import sys


SCRIPT = Path(__file__).resolve()
ROOT = SCRIPT.parents[4] if len(SCRIPT.parents) > 4 else None
if ROOT is None or not (ROOT / "scripts/check_repo.py").is_file():
    raise SystemExit(
        "This is a repository-maintainer check, not an installed-skill tool. "
        "Run make check from an Augustus repository checkout."
    )
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.check_repo import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())
