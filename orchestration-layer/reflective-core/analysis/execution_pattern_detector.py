from __future__ import annotations


def detect_patterns(pipelines: list[dict]) -> list[dict]:
    patterns = []
    for pipeline in pipelines:
        capabilities = tuple(sorted(pipeline.get("capabilities", [])))
        patterns.append(
            {
                "pipeline_id": pipeline.get("pipeline_id", "unknown"),
                "pattern_signature": "|".join(capabilities),
            }
        )
    return patterns
