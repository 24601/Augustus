"""Offline replay of reviewed, frozen submissions; no inference or network calls.

Not an adversarial-code sandbox. Mac isolation evidence is retained in the archive.
"""
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import statistics
import subprocess
import sys
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parent
ARCHIVE_SHA = '32bd19ed08e45dc8ff020b811023b8cd7efd14c9cc71c26784b7151066e4b1ed'
PREFIX = 'Before implementing, load augustus-train and apply its relevant guidance.\n\n'
ARMS = ['none', 'old-explicit', 'new-explicit']


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha(ROOT / 'results.tar.gz') == ARCHIVE_SHA
records = []
with tempfile.TemporaryDirectory() as tmp:
    with tarfile.open(ROOT / 'results.tar.gz') as archive:
        for member in archive.getmembers():
            path = PurePosixPath(member.name)
            assert not path.is_absolute() and '..' not in path.parts
            assert member.isfile() or member.isdir()
        archive.extractall(tmp, filter='data')
    root = Path(tmp) / 'reporting-confirmation-results'
    manifest = (root / 'SHA256SUMS').read_text().splitlines()
    for line in manifest:
        expected, relative = line.split('  ', 1)
        assert sha(root / relative) == expected, relative
    assert sha(ROOT / 'contract.md') == '619c9e6172db659c8fb5e090456e17eec8f0350625bc874f9e61d34f72fd2c46'
    assert sha(root / 'confirmation-public-tasks.tar') == '365a86e44abc921231a82eb0f321724cb6e40e4863ac739709190e9df033b0b9'
    assert sha(root / 'confirmation-private-grader.tar') == 'aeea3fcf1cfca89340b7d395d22c191d3e1d5b205fa1c068b2fc480bcb0c171a'
    observed = json.loads((root / 'observations.json').read_text())
    order = []
    for repeat in range(1, 4):
        for offset, task in enumerate(('task_1', 'task_2')):
            start = (repeat - 1 + offset) % 3
            order += [f'confirmation-{task}-r{repeat}-{ARMS[(start+i)%3]}' for i in range(3)]
    assert [r['id'] for r in observed['records']] == order
    for record in observed['records']:
        task, arm = record['task'], record['arm']
        run = root / 'state/runs' / record['id']
        assert record['status'] == 'done' and not record['timedOut'] and not record['protocolErrors']
        for name, original in [('TASK.md', f'{task}/PROMPT.md'),
                               ('input.json', f'{task}/input.json'), ('README.md', 'README.md')]:
            assert (run / 'artifacts' / name).read_bytes() == (root / 'packet/public' / original).read_bytes()
        for name, digest in record['files'].items():
            assert sha(run / 'artifacts' / name) == digest
        execution = json.loads((run / 'execution.json').read_text())
        command = execution['command']
        assert command[command.index('--max-turns')+1] == '20'
        assert command[command.index('--effort')+1] == 'medium'
        assert execution['timeoutSeconds'] == 180
        events = [json.loads(line) for line in (run / 'trace.jsonl').read_text().splitlines()]
        init = next(e for e in events if e['type'] == 'system' and e.get('subtype') == 'init')
        assert {s for s in init['skills'] if s.startswith('.agents:')} == (
            set() if arm == 'none' else {'.agents:augustus', '.agents:augustus-train'})
        messages = [e['message'] for e in events if e['type'] == 'assistant']
        assert all(m['model'] == 'claude-opus-5-5' for m in messages)
        calls = [b for m in messages for b in m['content'] if b.get('type') == 'tool_use']
        loads = [b['input']['skill'] for b in calls if b['name'] == 'Skill']
        assert loads == ([] if arm == 'none' else ['.agents:augustus-train'])
        helper_calls = [b for b in calls if 'policy_receipt.py' in json.dumps(b['input'])]
        assert not helper_calls
        if arm != 'none':
            assert any('# Augustus Train' in b.get('text', '') for e in events if e['type'] == 'user'
                       for b in e.get('message', {}).get('content', []))
        result = next(e for e in reversed(events) if e['type'] == 'result')
        assert not result['is_error'] and result['total_cost_usd'] == record['cost']
        candidate = Path(tmp) / 'candidate' / task
        candidate.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(run / 'artifacts/solution.py', candidate / 'solution.py')
        graded = subprocess.run([sys.executable, '-B', str(root / 'packet/private/grade.py'),
                                 str(candidate.parent), '--task', task], capture_output=True,
                                text=True, timeout=60, cwd=candidate,
                                env={'PATH': '/usr/bin:/bin', 'PYTHONDONTWRITEBYTECODE': '1'})
        report = json.loads(graded.stdout)
        expected = json.loads((root / 'grading/runs' / record['id'] / 'stdout.json').read_text())
        assert report == expected, record['id']
        passed = report[task]['failed'] == 0
        assert graded.returncode == (0 if passed else 1)
        records.append(dict(id=record['id'], task=task, arm=arm, passed=passed,
                            report=report[task], reported_cost=record['cost'],
                            agent_wall_seconds=record['durationSeconds'], trainer_loads=len(loads)))
    for task in ('task_1', 'task_2'):
        for repeat in range(1, 4):
            prompts = {a: (root / 'state/runs' / f'confirmation-{task}-r{repeat}-{a}' /
                           'prompt.txt').read_text() for a in ARMS}
            assert prompts['old-explicit'] == prompts['new-explicit'] == PREFIX + prompts['none']
summary = []
for arm in ARMS:
    subset = [r for r in records if r['arm'] == arm]
    summary.append(dict(arm=arm, passes=sum(r['passed'] for r in subset), runs=len(subset),
                        reported_cost=sum(r['reported_cost'] for r in subset),
                        mean_agent_wall_seconds=statistics.mean(r['agent_wall_seconds'] for r in subset)))
print(json.dumps(dict(verified_archive_files=len(manifest), records=records, summary=summary,
                      total_reported_cost=sum(r['reported_cost'] for r in records)), indent=2))
