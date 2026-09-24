"""Tests for augrun's admission arithmetic and its live watchdog.

Stdlib only. The watchdog is tested against a fake process and a fake clock,
so a kill path can be exercised without pressuring host memory or wedging a
GPU, which is the point of plan v4's B18 and B20.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parent / "augrun"
SPEC = importlib.util.spec_from_loader(
    "augrun", importlib.machinery.SourceFileLoader("augrun", str(SCRIPT)))
augrun = importlib.util.module_from_spec(SPEC)
sys.modules["augrun"] = augrun
SPEC.loader.exec_module(augrun)


class FakeProcess:
    """A process that exits after `alive_polls` polls, or never."""

    def __init__(self, alive_polls=10**9, returncode=0):
        self.alive_polls = alive_polls
        self.returncode_when_done = returncode
        self.returncode = None
        self.signals = []
        self.killed = False

    def poll(self):
        if self.alive_polls <= 0:
            self.returncode = self.returncode_when_done
            return self.returncode
        self.alive_polls -= 1
        return None

    def send_signal(self, number):
        self.signals.append(number)
        self.alive_polls = 0
        self.returncode = -number

    def wait(self, timeout=None):
        self.alive_polls = 0
        if self.returncode is None:
            self.returncode = self.returncode_when_done
        return self.returncode

    def kill(self):
        self.killed = True
        self.alive_polls = 0


class AdmissionTests(unittest.TestCase):
    def test_paw_ft_needs_seventy_seven_gib_not_the_twenty_four_gib_floor(self):
        verdict = augrun.admit(38.0, 9.0, meminfo=lambda: 60.0)
        self.assertEqual(verdict["required_gib"], 77.0)
        self.assertFalse(verdict["admitted"])
        self.assertEqual(verdict["reason"], "aggregate_requirement_exceeds_available")
        self.assertEqual(verdict["shortfall_gib"], 17.0)

    def test_the_same_run_is_admitted_with_enough_headroom(self):
        verdict = augrun.admit(38.0, 9.0, meminfo=lambda: 114.0)
        self.assertTrue(verdict["admitted"])

    def test_a_service_free_run_sums_without_it(self):
        verdict = augrun.admit(14.0, 0.0, meminfo=lambda: 114.0)
        self.assertEqual(verdict["required_gib"], 44.0)
        self.assertTrue(verdict["admitted"])

    def test_the_absolute_floor_still_refuses_a_tiny_run(self):
        verdict = augrun.admit(0.0, 0.0, meminfo=lambda: 20.0)
        self.assertFalse(verdict["admitted"])
        self.assertEqual(verdict["reason"], "below_absolute_floor")


class WatchdogTests(unittest.TestCase):
    def supervise(self, process, *, memory, heartbeat_timeout_s=0.0, beats=None):
        """Run the watchdog with a fake clock and no real sleeping."""
        with tempfile.TemporaryDirectory() as directory:
            beat = Path(directory) / "beat"
            if beats:
                beat.write_text("0", encoding="utf-8")
            ticks = iter(range(1, 10_000))
            readings = iter(memory)

            def clock():
                return next(ticks) * 0.5

            def meminfo():
                try:
                    return next(readings)
                except StopIteration:
                    return memory[-1]

            original_sleep = augrun.time.sleep
            augrun.time.sleep = lambda _: None
            try:
                return augrun.supervise(
                    process, heartbeat=beat, heartbeat_timeout_s=heartbeat_timeout_s,
                    abort_floor_gib=augrun.RESERVE_GIB, meminfo=meminfo, now=clock)
            finally:
                augrun.time.sleep = original_sleep

    def test_a_run_that_finishes_reports_its_low_water_mark(self):
        result = self.supervise(FakeProcess(alive_polls=4), memory=[100.0, 80.0, 61.5, 70.0])
        self.assertEqual(result["outcome"], "completed")
        self.assertEqual(result["mem_available_low_water_gib"], 61.5)

    def test_crossing_the_reserve_kills_the_container_and_blocks(self):
        """B18: exercised by mocking the reading, never by consuming host memory."""
        process = FakeProcess()
        result = self.supervise(process, memory=[100.0, 40.0, 5.9])
        self.assertEqual(result["outcome"], "blocked(memory)")
        self.assertEqual(result["mem_available_gib"], 5.9)
        self.assertEqual(process.signals, [augrun.signal.SIGTERM])

    def test_a_silent_heartbeat_ends_the_run_as_a_gpu_fault(self):
        """B20: an injected stall, not a deliberately wedged device."""
        process = FakeProcess()
        result = self.supervise(process, memory=[100.0], heartbeat_timeout_s=2.0, beats=True)
        self.assertEqual(result["outcome"], "blocked(gpu_fault)")
        self.assertGreater(result["silent_for_s"], 2.0)
        self.assertIn("not recovered, reset or reloaded here", result["detail"])
        self.assertEqual(process.signals, [augrun.signal.SIGTERM])

    def test_no_heartbeat_check_when_the_timeout_is_zero(self):
        result = self.supervise(FakeProcess(alive_polls=6), memory=[100.0])
        self.assertEqual(result["outcome"], "completed")

    def test_a_nonzero_exit_is_reported_not_swallowed(self):
        result = self.supervise(FakeProcess(alive_polls=2, returncode=137), memory=[100.0])
        self.assertEqual(result["outcome"], "exit_137")
        self.assertEqual(result["returncode"], 137)


class CommandTests(unittest.TestCase):
    def test_the_hardened_profile_and_the_gpu_devices_are_both_present(self):
        parser_args = augrun.argparse.Namespace(
            image="sha256:pinned", gpu_budget_gib=14.0, gpu=True,
            stage=["/srv/aug/stage/parts/e1", "/srv/aug/stage/weights"],
            command=["python3", "run.py"])
        command = augrun.podman_command(parser_args, Path("/srv/aug/runs/r1"),
                                        Path("/srv/aug/runs/r1/heartbeat/beat"))
        for flag in ("--network=none", "--read-only", "--cap-drop=all",
                     "--security-opt=no-new-privileges", "--memory=16g",
                     "--memory-swap=16g", "--pids-limit=512", "--ipc=private"):
            self.assertIn(flag, command)
        self.assertIn("/srv/aug/stage/weights:ro", command)
        self.assertIn("AUG_GPU_BUDGET_GIB=14.0", command)
        self.assertIn("/dev/kfd", command)
        self.assertEqual(command[-2:], ["python3", "run.py"])

    def test_a_cpu_only_run_gets_no_devices(self):
        parser_args = augrun.argparse.Namespace(
            image="sha256:pinned", gpu_budget_gib=0.0, gpu=False, stage=[], command=["true"])
        command = augrun.podman_command(parser_args, Path("/srv/aug/runs/r2"),
                                        Path("/srv/aug/runs/r2/heartbeat/beat"))
        self.assertNotIn("/dev/kfd", command)


if __name__ == "__main__":
    unittest.main()
