from __future__ import annotations

import sys
from pathlib import Path

import httpx
from fastapi.testclient import TestClient

def _create_app():
    base = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(base))
    from api import create_app  # type: ignore

    return create_app


def test_intent_proposal_valid(monkeypatch):
    create_app = _create_app()

    class FakeResponse:
        def __init__(self, status_code: int):
            self.status_code = status_code

    def fake_get(self, url: str):
        return FakeResponse(200)

    monkeypatch.setattr(httpx.Client, "get", fake_get)

    app = create_app(twingraph_base_url="http://core-twingraph:8000")
    client = TestClient(app)

    payload = {
        "intent_type": "create_space",
        "parameters": {"type": "green_room", "count": 2, "relative_to": "stage_zone"},
    }
    response = client.post("/intent/propose", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["validation_status"] == "VALID"
    assert len(data["proposed_mutations"]) == 1

    audit = client.get("/intent/events/audit")
    assert audit.status_code == 200
    events = audit.json()["events"]
    assert events[-1]["event_name"] == "intent.proposed"
    assert events[-1]["payload"]["validation_status"] == "VALID"


def test_intent_proposal_blocked_on_missing_parameters(monkeypatch):
    create_app = _create_app()

    def fake_get(self, url: str):
        class FakeResponse:
            status_code = 200

        return FakeResponse()

    monkeypatch.setattr(httpx.Client, "get", fake_get)

    app = create_app(twingraph_base_url="http://core-twingraph:8000")
    client = TestClient(app)

    payload = {
        "intent_type": "tag_zone",
        "parameters": {"node_id": "zone-1"},
    }
    response = client.post("/intent/propose", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["validation_status"] == "BLOCKED"
    assert data["proposed_mutations"] == []
    assert any("Missing required parameter: zone_tag" in reason for reason in data["reasons"])
