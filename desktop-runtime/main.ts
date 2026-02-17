import { app, ipcMain } from "electron";
import { createWindow } from "./window-manager";
import { RuntimeBootstrapper } from "./bootstrap/RuntimeBootstrapper";

let runtimeState = {
  kernel: "ACTIVE",
  feedback: "INACTIVE",
  presence: "INACTIVE",
  workspace: { activeTool: "select", flowStage: "concept", layoutPreset: "single-3d" },
};

function registerIpc() {
  ipcMain.handle("archflow:get-runtime-status", async () => ({
    kernel: runtimeState.kernel,
    feedback: runtimeState.feedback,
    presence: runtimeState.presence,
  }));
  ipcMain.handle("archflow:get-workspace-state", async () => ({ ...runtimeState.workspace }));
  ipcMain.handle("archflow:send-presence-signal", async (_event, signal: { type: string; intensity: number }) => ({
    accepted: typeof signal?.type === "string" && typeof signal?.intensity === "number",
  }));
}

async function bootDesktop() {
  app.commandLine.appendSwitch("enable-gpu-rasterization");
  const win = createWindow();
  registerIpc();

  const boot = new RuntimeBootstrapper().boot();
  runtimeState = {
    kernel: "ACTIVE",
    feedback: boot.health.feedback,
    presence: boot.health.presence,
    workspace: {
      activeTool: boot.workspace.getState().activeTool,
      flowStage: boot.workspace.getState().flowStage,
      layoutPreset: boot.workspace.getState().layoutPreset,
    },
  };

  // Lightweight host page keeps boot deterministic and non-blocking.
  await win.loadURL(
    "data:text/html;charset=utf-8," +
      encodeURIComponent(
        "<!doctype html><html><body><div id='root'>ArchFlow booted. Runtime active.</div></body></html>",
      ),
  );
}

app.whenReady().then(bootDesktop);

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});

