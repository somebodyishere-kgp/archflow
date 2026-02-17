# Kappa Reflection Flow

1. Runtime pipeline executes via self-assembly runtime.
2. Reflective analysis engine inspects pipeline shape and capability usage.
3. Reflection insight emitted as `reflection.insight.generated`.
4. Capability refactor engine proposes structural graph changes via `reflection.capability.proposed`.
5. Blueprint feedback adapter ingests proposal and updates assembly rules deterministically.
6. Rendering overlays visualize capability evolution and reflection graph read-only.
