import React from "react";

export function AIGenerationPulse(props: { assemblyIds: string[]; active: boolean }): JSX.Element {
  return <section>AI Pulse {props.active ? "active" : "idle"}: {props.assemblyIds.join(", ")}</section>;
}
