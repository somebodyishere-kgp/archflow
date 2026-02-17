import { type WorkspaceState } from "./workspace_models";

export class WorkspacePresetManager {
  private presets = new Map<string, WorkspaceState>();

  savePreset(name: string, state: WorkspaceState): void {
    this.presets.set(name, {
      ...state,
      selectedAssemblies: [...state.selectedAssemblies],
      panelVisibility: { ...state.panelVisibility },
      viewportLayouts: [...state.viewportLayouts],
      flowStageHistory: [...state.flowStageHistory],
      workspacePresetName: name,
    });
  }

  restorePreset(name: string): WorkspaceState | null {
    const preset = this.presets.get(name);
    if (!preset) return null;
    return {
      ...preset,
      selectedAssemblies: [...preset.selectedAssemblies],
      panelVisibility: { ...preset.panelVisibility },
      viewportLayouts: [...preset.viewportLayouts],
      flowStageHistory: [...preset.flowStageHistory],
    };
  }

  listPresets(): string[] {
    return Array.from(this.presets.keys());
  }
}
