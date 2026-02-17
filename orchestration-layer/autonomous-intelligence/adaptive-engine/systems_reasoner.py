from __future__ import annotations

from context_generalizer import generalize_context
from domain_inference_engine import infer_domain
from proposal_strategy_builder import build_strategy


def build_adaptive_reasoning(systems_graph: dict) -> dict:
    domain = infer_domain(systems_graph)
    context = generalize_context(systems_graph)
    strategy = build_strategy(domain, context)
    return {
        "domain_inference": domain,
        "context": context,
        "strategy": strategy,
    }
