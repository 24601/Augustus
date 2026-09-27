"""Replay the already-revealed application audit, not new confirmation."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
script = ROOT / '.agents/skills/augustus-train/scripts/policy_receipt.py'
spec = importlib.util.spec_from_file_location('policy_receipt', script)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
source = ROOT / 'research/audits/2026-09-27-application-climb/selection'
history = json.loads((source / 'public/rows.json').read_text())
future = json.loads((source / 'future.json').read_text())
results = {}
for name, rows in [('all_history', history), ('current_history', [r for r in history if r['day'] >= 90]),
                   ('revealed_future_audit', future)]:
    data = dict(population=dict(name=name, selection='day >= 90' if name == 'current_history'
                                else 'all rows of named source', ids=[r['request_id'] for r in rows]),
                rows=[dict(id=r['request_id'], score=r['scores']['compact'], y=r['fraud']) for r in rows],
                threshold=.07036600000000001, shift=.01, cost_fp=1, cost_fn=8)
    results[name] = m.receipt(data)
assert results['all_history']['reports'][0]['positive_actions'] == 555
assert results['current_history']['reports'][0]['positive_actions'] == 44
assert results['current_history']['population']['n'] == 300
future_reports = results['revealed_future_audit']['reports']
assert [r['mean_loss'] for r in future_reports[:3]] == [.20325, .34275, .154]
print(json.dumps(results, indent=2))
