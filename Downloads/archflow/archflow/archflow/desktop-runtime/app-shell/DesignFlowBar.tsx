import React from "react";
import { type DesignFlowStage } from "../workspace/workspace_models";

export function DesignFlowBar(props: { stage: DesignFlowStage; hint: string }): JSX.Element {
  return <section>Design Flow: {props.stage} | hint: {props.hint}</section>;
}
