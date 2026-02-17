import React from "react";
import { type DesignFlowStage } from "../workspace/workspace_models";

export function FlowTransitionPanel(props: { stageHistory: DesignFlowStage[] }): JSX.Element {
  return <section>Flow History: {props.stageHistory.join(" -> ")}</section>;
}
