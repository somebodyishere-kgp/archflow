from __future__ import annotations

from entity_abstraction_layer import abstract_entity
from relationship_engine import infer_relationships
from topology_generalizer import generalize_topology


def build_systems_graph(twingraph_nodes: list[dict], semantic_graph: dict | None = None) -> dict:
    abstract_nodes = [abstract_entity(node).model_dump() for node in twingraph_nodes]
    edges = [edge.model_dump() for edge in infer_relationships(twingraph_nodes)]
    topology = generalize_topology(abstract_nodes, edges)
    return {
        "systems_nodes": abstract_nodes,
        "systems_edges": edges,
        "topology": topology,
        "semantic_context": semantic_graph or {},
    }
