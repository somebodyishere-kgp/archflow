import React from "react";
import { DesignFlowBar } from "./DesignFlowBar";
import { FlowStageIndicator } from "./FlowStageIndicator";
import { InteractionModeIndicator } from "./InteractionModeIndicator";
import { ViewportLayoutManager } from "./ViewportLayoutManager";
import { ViewportTabs } from "./ViewportTabs";
import { type SelectionState } from "./SelectionSystem";
import { type TransformState } from "./TransformGizmo";
import { type InteractionContext } from "./InteractionStateMachine";
import { type DesignFlowStage, type WorkspaceLayoutPreset } from "../workspace/workspace_models";

export function CADViewport(): JSX.Element {
  const selection: SelectionState = { selectedIds: [] };
  const transform: TransformState = { mode: "translate", snapMm: 100, enabled: true };
  const interaction: InteractionContext = { state: "select", selectedIds: selection.selectedIds };
  const layoutPreset: WorkspaceLayoutPreset = "single-3d";
  const stage: DesignFlowStage = "concept";
  const tabs = ["main-3d", "plan-view", "section-view"];
  return (
    <section>
      CAD Viewport (intent-driven) - selected {selection.selectedIds.length} - gizmo {transform.mode}
      <InteractionModeIndicator mode={interaction.state} />
      <DesignFlowBar stage={stage} hint="Concept stage enables minimal overlays." />
      <FlowStageIndicator stage={stage} lockActive={false} />
      <ViewportLayoutManager preset={layoutPreset} />
      <ViewportTabs tabs={tabs} activeTab="main-3d" />
    </section>
  );
}
