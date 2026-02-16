export type ViewportState = {
  viewportId: string;
  camera: { x: number; y: number; z: number };
  selectedNodeIds: string[];
  previewNodeIds?: string[];
  snapOverlayBatchCount?: number;
  interactionFrameThrottleMs?: number;
  frameBudgetMs?: number;
  lodState?: "high" | "medium" | "low";
  overlayDensity?: number;
  overlayConfig?: Record<string, boolean>;
  flowStageOverlayProfile?: "minimal" | "assembly-guides" | "systems-insight" | "spatial-cognition" | "clean-render";
};

export class ViewportStateIsolator {
  private states = new Map<string, ViewportState>();
  private workspaceViewportRegistry = new Map<string, string[]>();
  private viewportFocusSignals = new Map<string, string>();
  private overlayVisibilityMatrix = new Map<string, Record<string, boolean>>();

  setState(state: ViewportState): void {
    this.states.set(state.viewportId, { ...state, selectedNodeIds: [...state.selectedNodeIds] });
  }

  getState(viewportId: string): ViewportState | null {
    const state = this.states.get(viewportId);
    return state ? { ...state, selectedNodeIds: [...state.selectedNodeIds] } : null;
  }

  setWorkspaceViewports(workspaceId: string, viewportIds: string[]): void {
    this.workspaceViewportRegistry.set(workspaceId, [...viewportIds]);
  }

  getWorkspaceViewports(workspaceId: string): string[] {
    return [...(this.workspaceViewportRegistry.get(workspaceId) || [])];
  }

  setViewportFocusSignal(viewportId: string, signal: string): void {
    this.viewportFocusSignals.set(viewportId, signal);
  }

  getViewportFocusSignal(viewportId: string): string | null {
    return this.viewportFocusSignals.get(viewportId) || null;
  }

  setFlowStageOverlayProfile(
    viewportId: string,
    profile: "minimal" | "assembly-guides" | "systems-insight" | "spatial-cognition" | "clean-render",
  ): void {
    const current = this.getState(viewportId) || {
      viewportId,
      camera: { x: 0, y: 0, z: 10 },
      selectedNodeIds: [],
    };
    this.setState({ ...current, flowStageOverlayProfile: profile });
  }

  setOverlayVisibilityMatrix(viewportId: string, matrix: Record<string, boolean>): void {
    this.overlayVisibilityMatrix.set(viewportId, { ...matrix });
  }

  getOverlayVisibilityMatrix(viewportId: string): Record<string, boolean> {
    return { ...(this.overlayVisibilityMatrix.get(viewportId) || {}) };
  }

  applyFlowStageProfile(
    viewportId: string,
    stage: "concept" | "layout" | "systems" | "spatial" | "presentation",
  ): void {
    const profiles: Record<string, { profile: ViewportState["flowStageOverlayProfile"]; visibility: Record<string, boolean> }> = {
      concept: { profile: "minimal", visibility: { guides: false, systems: false, cognition: false } },
      layout: { profile: "assembly-guides", visibility: { guides: true, systems: false, cognition: false } },
      systems: { profile: "systems-insight", visibility: { guides: true, systems: true, cognition: false } },
      spatial: { profile: "spatial-cognition", visibility: { guides: true, systems: false, cognition: true } },
      presentation: { profile: "clean-render", visibility: { guides: false, systems: false, cognition: false } },
    };
    const selected = profiles[stage];
    this.setFlowStageOverlayProfile(viewportId, selected.profile || "minimal");
    this.setOverlayVisibilityMatrix(viewportId, selected.visibility);
  }
}

export function isolatePreviewState(
  state: ViewportState,
  previewNodeIds: string[],
  snapOverlayBatchCount: number,
): ViewportState {
  return {
    ...state,
    previewNodeIds: [...previewNodeIds],
    snapOverlayBatchCount,
  };
}

export function throttleInteractionFrames(state: ViewportState, throttleMs: number): ViewportState {
  return { ...state, interactionFrameThrottleMs: throttleMs };
}

export function applyFrameBudget(state: ViewportState, frameBudgetMs: number): ViewportState {
  return { ...state, frameBudgetMs };
}

export function applyOverlayDensity(state: ViewportState, overlayDensity: number): ViewportState {
  return { ...state, overlayDensity };
}
