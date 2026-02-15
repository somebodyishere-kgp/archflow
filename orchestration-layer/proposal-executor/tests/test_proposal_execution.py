from __future__ import annotations

import json
import sys
from pathlib import Path

import httpx


def _schema_file() -> Path:
    return (
        Path(__file__).resolve().parents[3]
        / "spec"
        / "event-schemas"
        / "intent.proposed.json"
    )


def _load_executor():
    base = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(base))
    from executor import ProposalExecutor  # type: ignore

    return ProposalExecutor


def test_valid_proposal_executes_and_emits_lineage(monkeypatch):
    ProposalExecutor = _load_executor()

    intent_events = {
        "events": [
            {
                "event_name": "intent.proposed",
                "payload": {
                    "proposal_id": "proposal-001",
                    "intent_type": "create_space",
                    "proposed_mutations": [
                        {
                            "action": "create_node",
                            "target": "twingraph.node",
                            "payload": {
                                "id": "space-green-room-1",
                                "type": "space",
                                "geometry": {
                                    "type": "surface",
                                    "wkb": "0101000000000000000000F03F0000000000000040",
                                },
                                "properties": {"material_layers": []},
                                "relations": [],
                            },
                        }
                    ],
                    "validation_status": "VALID",
                    "timestamp": "2026-02-16T00:00:00Z",
                },
            }
        ]
    }

    class FakeResponse:
        def __init__(self, data=None, status_code=200):
            self._data = data or {}
            self.status_code = status_code

        def json(self):
            return self._data

        def raise_for_status(self):
            if self.status_code >= 400:
                raise httpx.HTTPStatusError("boom", request=None, response=None)

    def fake_get(self, url):
        return FakeResponse(data=intent_events)

    posted_payloads = []

    def fake_post(self, url, json=None):
        posted_payloads.append(json)
        return FakeResponse(data={"status": "accepted"})

    monkeypatch.setattr(httpx.Client, "get", fake_get)
    monkeypatch.setattr(httpx.Client, "post", fake_post)

    executor = ProposalExecutor(
        twingraph_base_url="http://core-twingraph:8000",
        intent_gateway_base_url="http://intent-gateway:8001",
        intent_schema_path=_schema_file(),
    )
    events = executor.run_once()

    assert len(posted_payloads) == 1
    assert events[-1]["event_name"] == "proposal.executed"
    payload = events[-1]["payload"]
    assert payload["proposal_id"] == "proposal-001"
    assert payload["execution_status"] == "EXECUTED"
    assert payload["execution_id"]
    assert payload["timestamp"]


def test_blocked_proposal_is_skipped(monkeypatch):
    ProposalExecutor = _load_executor()

    intent_events = {
        "events": [
            {
                "event_name": "intent.proposed",
                "payload": {
                    "proposal_id": "proposal-002",
                    "intent_type": "tag_zone",
                    "proposed_mutations": [],
                    "validation_status": "BLOCKED",
                    "timestamp": "2026-02-16T00:00:00Z",
                },
            }
        ]
    }

    class FakeResponse:
        def __init__(self, data=None, status_code=200):
            self._data = data or {}
            self.status_code = status_code

        def json(self):
            return self._data

        def raise_for_status(self):
            if self.status_code >= 400:
                raise httpx.HTTPStatusError("boom", request=None, response=None)

    def fake_get(self, url):
        return FakeResponse(data=intent_events)

    monkeypatch.setattr(httpx.Client, "get", fake_get)

    def fail_post(self, url, json=None):
        raise AssertionError("POST /twingraph/ingest must not be called for BLOCKED proposals")

    monkeypatch.setattr(httpx.Client, "post", fail_post)

    executor = ProposalExecutor(
        twingraph_base_url="http://core-twingraph:8000",
        intent_gateway_base_url="http://intent-gateway:8001",
        intent_schema_path=_schema_file(),
    )
    events = executor.run_once()
    payload = events[-1]["payload"]
    assert payload["proposal_id"] == "proposal-002"
    assert events[-1]["event_name"] == "proposal.blocked"
    assert payload["reasons"]
