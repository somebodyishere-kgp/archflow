from __future__ import annotations

import json
from typing import Any

import psycopg
from psycopg.rows import dict_row


class PostGISAdapter:
    """Minimal deterministic PostgreSQL + PostGIS adapter."""

    def __init__(self, dsn: str) -> None:
        self.dsn = dsn

    def _connect(self) -> psycopg.Connection[Any]:
        return psycopg.connect(self.dsn, row_factory=dict_row)

    def ensure_schema(self) -> None:
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute("CREATE EXTENSION IF NOT EXISTS postgis;")
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS twingraph_nodes (
                        id TEXT PRIMARY KEY,
                        node_type TEXT NOT NULL,
                        geometry_type TEXT NOT NULL,
                        geometry_wkb TEXT NOT NULL,
                        geom geometry,
                        properties JSONB NOT NULL DEFAULT '{}'::jsonb,
                        relations JSONB NOT NULL DEFAULT '[]'::jsonb,
                        execution_metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
                        version TIMESTAMPTZ,
                        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                        updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
                    );
                    """
                )
            conn.commit()

    def upsert_node(self, node: dict[str, Any]) -> dict[str, Any] | None:
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id, geometry_wkb FROM twingraph_nodes WHERE id = %s;",
                    (node["id"],),
                )
                previous = cur.fetchone()
                cur.execute(
                    """
                    INSERT INTO twingraph_nodes (
                        id, node_type, geometry_type, geometry_wkb, geom,
                        properties, relations, execution_metadata, version, updated_at
                    )
                    VALUES (
                        %(id)s, %(node_type)s, %(geometry_type)s, %(geometry_wkb)s,
                        ST_GeomFromWKB(decode(%(geometry_wkb)s, 'hex')),
                        %(properties)s::jsonb, %(relations)s::jsonb, %(execution_metadata)s::jsonb, %(version)s, NOW()
                    )
                    ON CONFLICT (id)
                    DO UPDATE SET
                        node_type = EXCLUDED.node_type,
                        geometry_type = EXCLUDED.geometry_type,
                        geometry_wkb = EXCLUDED.geometry_wkb,
                        geom = EXCLUDED.geom,
                        properties = EXCLUDED.properties,
                        relations = EXCLUDED.relations,
                        execution_metadata = EXCLUDED.execution_metadata,
                        version = EXCLUDED.version,
                        updated_at = NOW();
                    """,
                    {
                        "id": node["id"],
                        "node_type": node["type"],
                        "geometry_type": node["geometry"]["type"],
                        "geometry_wkb": node["geometry"]["wkb"],
                        "properties": json.dumps(node.get("properties", {})),
                        "relations": json.dumps(node.get("relations", [])),
                        "execution_metadata": json.dumps(node.get("execution_metadata", {})),
                        "version": node.get("version"),
                    },
                )
            conn.commit()
            return previous

    def get_node(self, node_id: str) -> dict[str, Any] | None:
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id, node_type, geometry_type, geometry_wkb, properties, relations, execution_metadata, version
                    FROM twingraph_nodes
                    WHERE id = %s;
                    """,
                    (node_id,),
                )
                row = cur.fetchone()
                if row is None:
                    return None
                return self._to_node(row)

    def query_nodes(self, filters: dict[str, Any]) -> list[dict[str, Any]]:
        node_type = filters.get("type")
        limit = int(filters.get("limit", 50))
        if limit < 1 or limit > 500:
            raise ValueError("Query limit must be between 1 and 500.")

        sql = """
        SELECT id, node_type, geometry_type, geometry_wkb, properties, relations, execution_metadata, version
        FROM twingraph_nodes
        """
        params: list[Any] = []
        if node_type:
            sql += " WHERE node_type = %s"
            params.append(node_type)
        sql += " ORDER BY id ASC LIMIT %s;"
        params.append(limit)

        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, tuple(params))
                rows = cur.fetchall()
                return [self._to_node(row) for row in rows]

    @staticmethod
    def _to_node(row: dict[str, Any]) -> dict[str, Any]:
        return {
            "id": row["id"],
            "type": row["node_type"],
            "geometry": {
                "type": row["geometry_type"],
                "wkb": row["geometry_wkb"],
            },
            "properties": row["properties"],
            "relations": row["relations"],
            "execution_metadata": row["execution_metadata"],
            "version": row["version"].isoformat() if row["version"] else None,
        }
