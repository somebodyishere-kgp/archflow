export type WorkspaceLayoutPreset = "single-3d" | "plan-section-split" | "quad-viewport" | "ai-analysis-mode";

export type AIFocusMode =
  | "design-mode"
  | "analysis-mode"
  | "spatial-mode"
  | "systems-mode"
  | "world-context-mode";

export type DesignFlowStage = "concept" | "layout" | "systems" | "spatial" | "presentation";

export type WorkspaceState = {
  activeTool: string;
  layoutPreset: WorkspaceLayoutPreset;
  selectedAssemblies: string[];
  aiFocusMode: AIFocusMode;
  flowStage: DesignFlowStage;
  flowStageHistory: DesignFlowStage[];
  flowTransitionLock: boolean;
  panelVisibility: Record<string, boolean>;
  viewportLayouts: string[];
  workspacePresetName?: string;
};
