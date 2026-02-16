# Data Flow: XIII Realtime Intelligence

Input:
- Realtime intent stream fragments
- Interaction deltas from desktop/human-interface

Process:
- Co-design runtime builds delta context.
- Realtime reasoner requests incremental LLM suggestions.
- Reflective validator checks safety and contradiction risk.
- Rendering overlays show live suggestions and intent deltas.

Output:
- `design.suggestion.generated`
- realtime suggestion timeline data
