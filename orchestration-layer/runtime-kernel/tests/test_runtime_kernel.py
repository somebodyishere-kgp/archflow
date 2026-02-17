from pathlib import Path
import sys


def _load():
    base = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(base))
    from kernel import RuntimeKernel  # type: ignore

    return RuntimeKernel


def test_runtime_kernel_cycle_and_state(tmp_path):
    RuntimeKernel = _load()
    kernel = RuntimeKernel(tmp_path / "runtime-events.jsonl")
    event = kernel.start_cycle("intent.proposed", {"proposal_id": "p-1"})
    assert event["event_name"] == "intent.proposed"
    state = kernel.runtime_state()
    assert state["runtime_cycle_id"].startswith("cycle-")
    assert state["event_queue_depth"] >= 1
