# Data Flow: E8 Runtime Boot Sequence

Feature: Unified Desktop Runtime Boot

Input:
- Desktop app start (`electron .`)
- Boot profile from `BootPerformanceProfiler`
- OCCT probe from geometry adapter status check

Process:
- Main process initializes window and IPC bridge.
- Bootstrapper performs deterministic startup ordering.
- Health snapshot is assembled for read-only UI display.
- Default scene is loaded synchronously into viewport host state.

Output:
- Desktop runtime active state
- Read-only runtime/workspace/presence bridge methods
- Boot metrics artifact (`e8-boot-performance.json`)

Validation Layers:
- CI verifies E8 boot files and bootstrap modules are present.
- Guard checks reject TwinGraph mutation calls from desktop boot layers.
- Guard checks reject blocking-loop patterns in presence and boot runtime modules.

