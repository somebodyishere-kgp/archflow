import { contextBridge, ipcRenderer } from "electron";

const runtimeApi = {
  getRuntimeStatus: () => ipcRenderer.invoke("archflow:get-runtime-status"),
  getWorkspaceState: () => ipcRenderer.invoke("archflow:get-workspace-state"),
  sendPresenceSignal: (signal: { type: string; intensity: number }) =>
    ipcRenderer.invoke("archflow:send-presence-signal", signal),
};

contextBridge.exposeInMainWorld("archflow", {
  runtime: runtimeApi,
  workspace: {
    getWorkspaceState: runtimeApi.getWorkspaceState,
  },
  viewport: {
    sendPresenceSignal: runtimeApi.sendPresenceSignal,
  },
});

