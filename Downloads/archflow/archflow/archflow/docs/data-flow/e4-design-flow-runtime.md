# E4 Design Flow Runtime

Feature: Guided single-user design flow orchestration

Input:
- local workspace stage changes
- interaction mode context
- panel/layout preference updates

Process:
- `DesignFlowController` resolves flow profile by stage
- `WorkspaceStateEngine` updates stage, history, and lock state
- `AIFocusModeManager` updates UI focus emphasis
- `ViewportStateIsolator` applies overlay profile and visibility matrix
- runtime scheduler advances through `design.flow.update`

Output:
- `design.flow.stage.changed`
- refreshed workspace state and overlay configuration

Validation:
- workspace/flow path must not call TwinGraph mutation APIs
- design flow must not trigger rebuild pipeline
- rendering remains read-only
