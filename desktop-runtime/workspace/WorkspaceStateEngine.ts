import { type WorkspaceState, type WorkspaceLayoutPreset, type AIFocusMode, type DesignFlowStage } from "./workspace_models";

export class WorkspaceStateEngine {
  private state: WorkspaceState = {
    activeTool: "select",
    layoutPreset: "single-3d",
    selectedAssemblies: [],
    aiFocusMode: "design-mode",
    flowStage: "concept",
    flowStageHistory: ["concept"],
    flowTransitionLock: false,
    panelVisibility: {},
    viewportLayouts: ["main-viewport"],
  };

  getState(): WorkspaceState {
    return {
      ...this.state,
      selectedAssemblies: [...this.state.selectedAssemblies],
      panelVisibility: { ...this.state.panelVisibility },
      viewportLayouts: [...this.state.viewportLayouts],
      flowStageHistory: [...this.state.flowStageHistory],
    };
  }

  setActiveTool(tool: string): WorkspaceState {
    this.state = { ...this.state, activeTool: tool };
    return this.getState();
  }

  setLayoutPreset(layoutPreset: WorkspaceLayoutPreset, viewportLayouts: string[]): WorkspaceState {
    this.state = { ...this.state, layoutPreset, viewportLayouts: [...viewportLayouts] };
    return this.getState();
  }

  setSelection(selectedAssemblies: string[]): WorkspaceState {
    this.state = { ...this.state, selectedAssemblies: [...selectedAssemblies] };
    return this.getState();
  }

  setAIFocusMode(aiFocusMode: AIFocusMode): WorkspaceState {
    this.state = { ...this.state, aiFocusMode };
    return this.getState();
  }

  setPanelVisibility(panelName: string, visible: boolean): WorkspaceState {
    this.state = { ...this.state, panelVisibility: { ...this.state.panelVisibility, [panelName]: visible } };
    return this.getState();
  }

  transitionFlowStage(nextStage: DesignFlowStage): WorkspaceState {
    if (this.state.flowTransitionLock) return this.getState();
    if (this.state.flowStage === nextStage) return this.getState();
    this.state = {
      ...this.state,
      flowStage: nextStage,
      flowStageHistory: [...this.state.flowStageHistory, nextStage],
    };
    return this.getState();
  }

  setFlowTransitionLock(locked: boolean): WorkspaceState {
    this.state = { ...this.state, flowTransitionLock: locked };
    return this.getState();
  }
}
