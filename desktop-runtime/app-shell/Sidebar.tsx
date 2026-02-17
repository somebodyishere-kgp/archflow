import React from "react";
import { DesignFlowBar } from "./DesignFlowBar";
import { FocusModeIndicator } from "./FocusModeIndicator";
import { FlowStageIndicator } from "./FlowStageIndicator";
import { FlowTransitionPanel } from "./FlowTransitionPanel";
import { LayoutSwitcher } from "./LayoutSwitcher";
import { WorkspaceToolbar } from "./WorkspaceToolbar";
import { type AIFocusMode, type DesignFlowStage, type WorkspaceLayoutPreset } from "../workspace/workspace_models";

export function Sidebar(): JSX.Element {
  const mode: AIFocusMode = "design-mode";
  const layout: WorkspaceLayoutPreset = "single-3d";
  const stage: DesignFlowStage = "concept";
  return (
    <aside>
      ArchFlow Desktop Runtime
      <WorkspaceToolbar />
      <DesignFlowBar stage={stage} hint="Progress stage to unlock guided overlays." />
      <FlowStageIndicator stage={stage} lockActive={false} />
      <FlowTransitionPanel stageHistory={["concept"]} />
      <LayoutSwitcher activeLayout={layout} />
      <FocusModeIndicator mode={mode} />
    </aside>
  );
}
