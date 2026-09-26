"""Alternative routing for authoritative notice types."""
import json
from pathlib import Path


def load_routes(path):
    return json.loads(Path(path).read_text())


def route(routes, notice):
    kind = notice.get('notice_type') if isinstance(notice, dict) else None
    return routes.get(kind, 'operations') if isinstance(kind, str) else 'operations'
