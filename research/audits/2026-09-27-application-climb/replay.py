"""Offline outcome replay and trace checks. No inference or network calls."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import statistics
import subprocess
import sys
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parent
ARCHIVE_SHA = 'ea599e46d960c8d3353178868be81dff42211b2aa196456283390388ab5da304'
FREEZE_SHA = 'b1b85d9bad7eea749ccb824661483a35980967883455c908cbcf8ea3f3b7a8da'
PREFIX = 'Before implementing, load augustus-train and apply its relevant guidance.\n\n'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha(ROOT / 'initial-results.tar.gz') == ARCHIVE_SHA
assert sha(ROOT / 'frozen-sha256.txt') == FREEZE_SHA
for line in (ROOT / 'frozen-sha256.txt').read_text().splitlines():
    expected, relative = line.split('  ', 1)
    assert sha(ROOT / relative) == expected, relative

records = []
with tempfile.TemporaryDirectory() as temporary:
    with tarfile.open(ROOT / 'initial-results.tar.gz') as archive:
        for member in archive.getmembers():
            path = PurePosixPath(member.name)
            assert not path.is_absolute() and '..' not in path.parts
            assert member.isfile() or member.isdir(), member.name
        archive.extractall(temporary, filter='data')
    root = Path(temporary) / 'climb2-application-results'
    manifest = (root / 'SHA256SUMS').read_text().splitlines()
    for line in manifest:
        expected, relative = line.split('  ', 1)
        assert sha(root / relative) == expected, relative
    observed = json.loads((root / 'observations.json').read_text())
    expected_order = []
    arms = ['none', 'auto', 'explicit']
    for repeat in range(1, 4):
        for offset, task in enumerate(('selection', 'policy')):
            start = (repeat - 1 + offset) % 3
            expected_order += [f'release-{task}-r{repeat}-{arms[(start+i)%3]}' for i in range(3)]
    assert [r['id'] for r in observed['records']] == expected_order
    for record in observed['records']:
        task, arm, repeat = record['task'], record['arm'], record['repeat']
        run = root / 'application-state/runs' / record['id']
        assert record['status'] == 'done' and not record['timedOut'] and not record['protocolErrors']
        for name in ('prompt.md', 'operations.md', 'rows.json', 'config.json'):
            actual = 'TASK.md' if name == 'prompt.md' else name
            assert (run / 'artifacts' / actual).read_bytes() == (ROOT / task / 'public' / name).read_bytes()
        events = [json.loads(line) for line in (run / 'trace.jsonl').read_text().splitlines()]
        init = next(e for e in events if e['type'] == 'system' and e.get('subtype') == 'init')
        skills = {s for s in init['skills'] if s.startswith('.agents:')}
        assert skills == (set() if arm == 'none' else {'.agents:augustus', '.agents:augustus-train'})
        messages = [e['message'] for e in events if e['type'] == 'assistant']
        assert all(m['model'] == 'claude-opus-5-5' for m in messages)
        calls = [b['input']['skill'] for m in messages for b in m['content']
                 if b.get('type') == 'tool_use' and b.get('name') == 'Skill']
        assert calls == (['.agents:augustus-train'] if arm == 'explicit' else [])
        if arm == 'explicit':
            assert any('# Augustus Train' in b.get('text', '') for e in events if e['type'] == 'user'
                       for b in e.get('message', {}).get('content', []))
        result = next(e for e in reversed(events) if e['type'] == 'result')
        assert not result['is_error'] and result['total_cost_usd'] == record['cost']
        source = run / 'artifacts/solution.py'
        assert sha(source) == record['solutionSha256']
        grader = ROOT / task / ('private/grade.py' if task == 'policy' else 'grade.py')
        graded = subprocess.run([sys.executable, str(grader), str(source)],
                                capture_output=True, text=True, timeout=65)
        outcome = json.loads(graded.stdout.splitlines()[-1])
        expected = json.loads((ROOT / 'grades' / (record['id'] + '.json')).read_text())
        assert outcome == expected, (record['id'], outcome, expected)
        passed = outcome['pass'] if task == 'policy' else outcome['passed']
        assert graded.returncode == (0 if passed else 1)
        records.append(dict(id=record['id'], task=task, arm=arm, repeat=repeat,
                            cost=record['cost'], passed=passed,
                            loss=outcome['cost'] if task == 'policy' else outcome['mean_loss']))
    for task in ('selection', 'policy'):
        for repeat in range(1, 4):
            runs = root / 'application-state/runs'
            prompts = {a: (runs / f'release-{task}-r{repeat}-{a}/prompt.txt').read_text() for a in arms}
            assert prompts['none'] == prompts['auto']
            assert prompts['explicit'] == PREFIX + prompts['auto']
summary = []
for task in ('selection', 'policy'):
    for arm in arms:
        subset = [r for r in records if r['task'] == task and r['arm'] == arm]
        summary.append(dict(task=task, arm=arm, passed=sum(r['passed'] for r in subset),
                            runs=len(subset), median_loss=statistics.median(r['loss'] for r in subset),
                            mean_loss=statistics.mean(r['loss'] for r in subset),
                            reported_cost=sum(r['cost'] for r in subset)))
print(json.dumps(dict(verified_archive_files=len(manifest), records=records, summary=summary,
                      total_reported_cost=sum(r['cost'] for r in records)), indent=2))
