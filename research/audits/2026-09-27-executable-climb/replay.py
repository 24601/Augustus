"""Offline parent verification; runs frozen submissions, never calls a model."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parent
ARCHIVE_SHA = 'ff68b00f5553102341e5aaca83d63128abc1d302584e92549e39d22ad59b8950'
PREFIX = 'Before implementing, load augustus-train and apply its relevant guidance.\n\n'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert digest(ROOT / 'initial-results.tar.gz') == ARCHIVE_SHA
for line in (ROOT / 'frozen-sha256.txt').read_text().splitlines():
    expected, name = line.split('  ', 1)
    relative = name.split('2026-09-27-executable-climb/', 1)[1]
    assert digest(ROOT / relative) == expected, relative

records = []
with tempfile.TemporaryDirectory() as temporary:
    with tarfile.open(ROOT / 'initial-results.tar.gz') as archive:
        for entry in archive.getmembers():
            path = PurePosixPath(entry.name)
            assert not path.is_absolute() and '..' not in path.parts
            assert entry.isfile() or entry.isdir(), entry.name
        archive.extractall(temporary, filter='data')
    root = Path(temporary) / 'climb1-initial-results'
    manifest = (root / 'SHA256SUMS').read_text().splitlines()
    for line in manifest:
        expected, relative = line.split('  ', 1)
        assert digest(root / relative) == expected, relative
    observed = json.loads((root / 'observations.json').read_text())
    for record in observed['records']:
        run = root / 'climb1-state/runs' / record['id']
        task, arm = record['task'], record['arm']
        assert record['status'] == 'done' and not record['protocolErrors']
        assert (run / 'artifacts/TASK.md').read_bytes() == (ROOT / 'tasks' / task / 'prompt.md').read_bytes()
        events = [json.loads(line) for line in (run / 'trace.jsonl').read_text().splitlines()]
        init = next(e for e in events if e['type'] == 'system' and e.get('subtype') == 'init')
        skills = {s for s in init['skills'] if s.startswith('.agents:')}
        assert skills == (set() if arm == 'none' else {'.agents:augustus', '.agents:augustus-train'})
        calls = [b for e in events if e['type'] == 'assistant'
                 for b in e.get('message', {}).get('content', [])
                 if b.get('type') == 'tool_use' and b.get('name') == 'Skill']
        assert [c['input']['skill'] for c in calls] == (
            ['.agents:augustus-train'] if arm == 'explicit' else [])
        if arm == 'explicit':
            assert any('# Augustus Train' in b.get('text', '') for e in events if e['type'] == 'user'
                       for b in e.get('message', {}).get('content', []))
        result = next(e for e in reversed(events) if e['type'] == 'result')
        assert not result['is_error'] and result['total_cost_usd'] == record['cost']
        source = run / 'artifacts/solution.py'
        assert digest(source) == record['solutionSha256']
        graded = subprocess.run([sys.executable, str(ROOT / 'grade.py'), task, str(source)],
                                capture_output=True, text=True, timeout=30)
        assert graded.returncode == 0, (record['id'], graded.stderr)
        score = json.loads(graded.stdout)
        records.append(dict(id=record['id'], cost=record['cost'], **score))
    for task in ('data', 'planning', 'training'):
        runs = root / 'climb1-state/runs'
        prompts = {arm: (runs / f'release-{task}-{arm}/prompt.txt').read_text()
                   for arm in ('none', 'auto', 'explicit')}
        assert prompts['none'] == prompts['auto']
        assert prompts['explicit'] == PREFIX + prompts['auto']
print(json.dumps(dict(verified_archive_files=len(manifest), records=records,
                      total_reported_cost=sum(r['cost'] for r in records),
                      decision='retain 0.8.1: saturated development; holdout unopened'), indent=2))
