import React, { useMemo } from "react";
import { CADViewport } from "./CADViewport";
import { Sidebar } from "./Sidebar";
import { SystemHealthPanel } from "./SystemHealthPanel";
import { WorkspaceToolbar } from "./WorkspaceToolbar";
import { LiveFeedbackOverlay } from "./LiveFeedbackOverlay";
import { PresenceGlowOverlay } from "../../rendering-client/src/e7/PresenceGlowOverlay";
import { RuntimeBootstrapper } from "../bootstrap/RuntimeBootstrapper";

export function AppShell(): JSX.Element {
  const boot = useMemo(() => new RuntimeBootstrapper().boot(), []);
  return (
    <main style={{ display: "grid", gridTemplateColumns: "300px 1fr", gap: 12 }}>
      <section>
        <Sidebar />
        <SystemHealthPanel health={boot.health} />
      </section>
      <section style={{ position: "relative", minHeight: 420 }}>
        <WorkspaceToolbar />
        <CADViewport />
        <LiveFeedbackOverlay />
        <PresenceGlowOverlay viewportId="main-viewport" />
      </section>
    </main>
  );
}

