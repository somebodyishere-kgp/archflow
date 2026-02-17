from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .db import PostGISAdapter
from .ingest import TwinGraphIngestService
from .transport.local import LocalEventTransport
from .views.geometry_view import GeometryViewAdapter
from .views.section_view import SectionViewAdapter


class QueryRequest(BaseModel):
    type: str | None = None
    limit: int = Field(default=50, ge=1, le=500)


class QueryResponse(BaseModel):
    nodes: list[dict[str, Any]]
    count: int
    queried_at: str


class SectionViewRequest(BaseModel):
    type: str | None = None
    limit: int = Field(default=50, ge=1, le=500)


def create_app(schema_path: Path, dsn: str) -> FastAPI:
    app = FastAPI(title="TwinGraph Core API", version="0.3.0")

    adapter = PostGISAdapter(dsn)
    transport = LocalEventTransport()
    ingest = TwinGraphIngestService(schema_path=schema_path, adapter=adapter, transport=transport)
    geometry_view = GeometryViewAdapter()
    section_view = SectionViewAdapter()
    ingest.ensure_ready()

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "module": "core-twingraph"}

    @app.get("/twingraph/node/{node_id}")
    def get_twingraph_node(node_id: str) -> dict[str, Any]:
        node = adapter.get_node(node_id)
        if node is None:
            raise HTTPException(status_code=404, detail="TwinGraph node not found.")
        return node

    @app.post("/twingraph/query", response_model=QueryResponse)
    def query_twingraph_nodes(request: QueryRequest) -> QueryResponse:
        filters = request.model_dump(exclude_none=True)
        nodes = adapter.query_nodes(filters)
        return QueryResponse(
            nodes=nodes,
            count=len(nodes),
            queried_at=datetime.now(UTC).isoformat(),
        )

    @app.get("/twingraph/view/geometry")
    def geometry_view_read(limit: int = 50, node_type: str | None = None) -> dict[str, Any]:
        bounded = geometry_view.clamp_limit(limit)
        nodes = adapter.query_nodes({"type": node_type, "limit": bounded} if node_type else {"limit": bounded})
        dto_rows = geometry_view.build(nodes)
        transport.emit(
            "view.refresh",
            {
                "view_type": "geometry",
                "count": len(dto_rows),
                "timestamp": datetime.now(UTC).isoformat(),
            },
        )
        return {
            "view": dto_rows,
            "count": len(dto_rows),
        }

    @app.post("/twingraph/view/section")
    def section_view_read(request: SectionViewRequest) -> dict[str, Any]:
        filters = request.model_dump(exclude_none=True)
        nodes = adapter.query_nodes(filters)
        dto_rows = section_view.build(nodes)
        transport.emit(
            "view.refresh",
            {
                "view_type": "section",
                "count": len(dto_rows),
                "timestamp": datetime.now(UTC).isoformat(),
            },
        )
        return {
            "view": dto_rows,
            "count": len(dto_rows),
        }

    @app.post("/twingraph/ingest")
    def ingest_twingraph_node(request: dict[str, Any]) -> dict[str, str]:
        node = request.get("node", request)
        proposal_id = request.get("proposal_id")
        execution_id = request.get("execution_id")
        intent_source = request.get("intent_source")
        parent_event_id = request.get("parent_event_id")
        if proposal_id or execution_id or intent_source:
            node["execution_metadata"] = {
                "proposal_id": proposal_id,
                "execution_id": execution_id,
                "intent_source": intent_source,
            }
        ingest.ingest_node(
            node,
            proposal_id=proposal_id,
            execution_id=execution_id,
            intent_source=intent_source,
            parent_event_id=parent_event_id,
        )
        return {"status": "accepted"}

    @app.get("/events/audit")
    def event_audit() -> dict[str, Any]:
        events = transport.snapshot()
        return {
            "count": len(events),
            "events": events,
        }

    return app
