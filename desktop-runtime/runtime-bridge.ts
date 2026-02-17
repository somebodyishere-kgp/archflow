export type RuntimeBridgeApi = {
  getRuntimeStatus: () => Promise<{ kernel: string; feedback: string; presence: string }>;
  getWorkspaceState: () => Promise<{ activeTool: string; flowStage: string; layoutPreset: string }>;
  sendPresenceSignal: (signal: { type: string; intensity: number }) => Promise<{ accepted: boolean }>;
};

declare global {
  interface Window {
    archflow: {
      runtime: RuntimeBridgeApi;
      workspace: Pick<RuntimeBridgeApi, "getWorkspaceState">;
      viewport: Pick<RuntimeBridgeApi, "sendPresenceSignal">;
    };
  }
}

export const runtimeBridge: RuntimeBridgeApi = {
  async getRuntimeStatus() {
    return window.archflow.runtime.getRuntimeStatus();
  },
  async getWorkspaceState() {
    return window.archflow.runtime.getWorkspaceState();
  },
  async sendPresenceSignal(signal) {
    return window.archflow.runtime.sendPresenceSignal(signal);
  },
};

