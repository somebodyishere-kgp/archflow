import React from "react";
import { type DesignFlowStage } from "../workspace/workspace_models";

export function FlowStageIndicator(props: { stage: DesignFlowStage; lockActive: boolean }): JSX.Element {
  return <section>Flow Stage: {props.stage} {props.lockActive ? "(transition lock)" : ""}</section>;
}
