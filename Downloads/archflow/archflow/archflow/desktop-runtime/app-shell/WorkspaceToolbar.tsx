import React from "react";
import { DesignFlowBar } from "./DesignFlowBar";
import { FlowStageIndicator } from "./FlowStageIndicator";
import { FlowTransitionPanel } from "./FlowTransitionPanel";
import { type DesignFlowStage } from "../workspace/workspace_models";

export function WorkspaceToolbar(): JSX.Element {
  const stage: DesignFlowStage = "concept";
  return (
    <section>
      Workspace Toolbar
      <DesignFlowBar stage={stage} hint="Use concept mode for fast ideation." />
      <FlowStageIndicator stage={stage} lockActive={false} />
      <FlowTransitionPanel stageHistory={["concept", "layout"]} />
    </section>
  );
}
