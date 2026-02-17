export type GeometryEngineRuntimeStatus = "READY" | "BLOCKED";

export type GeometryEngineStatusSnapshot = {
  status: GeometryEngineRuntimeStatus;
  runtime: string;
  reason?: string;
};

export function fromOcctProbe(probe: { status: string; runtime?: string; diagnostics?: Record<string, unknown> }): GeometryEngineStatusSnapshot {
  const status: GeometryEngineRuntimeStatus = probe.status === "READY" ? "READY" : "BLOCKED";
  const reason = typeof probe?.diagnostics?.error === "string" ? probe.diagnostics.error : undefined;
  return {
    status,
    runtime: probe.runtime || "OCP",
    reason,
  };
}

export function toolAvailability(status: GeometryEngineStatusSnapshot): Record<string, boolean> {
  const enabled = status.status === "READY";
  return {
    solidEdit: enabled,
    booleanOps: enabled,
    constraintPreview: true,
  };
}

