import { fromOcctProbe, type GeometryEngineStatusSnapshot } from "../status/GeometryEngineStatus";

export type RuntimeHealthSnapshot = {
  occt: GeometryEngineStatusSnapshot;
  runtimeKernel: "ACTIVE" | "INACTIVE";
  feedback: "ACTIVE" | "INACTIVE";
  presence: "ACTIVE" | "INACTIVE";
};

export class SystemHealthCheck {
  run(): RuntimeHealthSnapshot {
    // Boot-time probe is read-only and never blocks boot.
    const occtProbe = { status: "BLOCKED", runtime: "OCP", diagnostics: { error: "Probe unavailable in desktop host" } };
    return {
      occt: fromOcctProbe(occtProbe),
      runtimeKernel: "ACTIVE",
      feedback: "INACTIVE",
      presence: "INACTIVE",
    };
  }
}

