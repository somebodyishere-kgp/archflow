# E4 Design Flow Engine

Program E4 upgrades the single-user workspace into a guided design flow runtime.

## Flow Stages
- concept
- layout
- systems
- spatial
- presentation

## Core Module
- `desktop-runtime/workspace/DesignFlowController.ts`
- `desktop-runtime/workspace/design_flow_models.ts`

The controller orchestrates focus mode, tool presets, and viewport behavior by stage while remaining local and non-destructive.

## Boundaries
- No TwinGraph writes in flow/workspace modules.
- No rendering mutations.
- No geometry rebuild trigger from `design.flow.update`.
- No multi-user logic.
