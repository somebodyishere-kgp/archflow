import React from "react";
import { type RuntimeHealthSnapshot } from "../bootstrap/SystemHealthCheck";

export function SystemHealthPanel({ health }: { health: RuntimeHealthSnapshot }): JSX.Element {
  return (
    <section>
      <strong>System Health</strong>
      <div>OCCT: {health.occt.status}</div>
      <div>RuntimeKernel: {health.runtimeKernel}</div>
      <div>Feedback: {health.feedback}</div>
      <div>Presence: {health.presence}</div>
      {health.occt.status === "BLOCKED" ? <div>Solid editing tools are disabled. App continues in safe mode.</div> : null}
    </section>
  );
}

