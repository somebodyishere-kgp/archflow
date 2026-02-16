from __future__ import annotations


def apply_reflection_feedback(assembly_blueprint: dict, reflection_proposal: dict) -> dict:
    # Deterministic blueprint update proposal application.
    next_blueprint = dict(assembly_blueprint)
    next_blueprint.setdefault("reflection_feedback", []).append(reflection_proposal)
    return next_blueprint
