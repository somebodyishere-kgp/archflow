import { type AIFocusMode, type DesignFlowStage } from "./workspace_models";

export type FlowStageProfile = {
  stage: DesignFlowStage;
  focusMode: AIFocusMode;
  overlayProfile: "minimal" | "assembly-guides" | "systems-insight" | "spatial-cognition" | "clean-render";
  toolPreset: string;
  preferredViewportBehavior: "single" | "split" | "quad";
};

export const FLOW_STAGE_PROFILES: Record<DesignFlowStage, FlowStageProfile> = {
  concept: {
    stage: "concept",
    focusMode: "design-mode",
    overlayProfile: "minimal",
    toolPreset: "concept-toolkit",
    preferredViewportBehavior: "single",
  },
  layout: {
    stage: "layout",
    focusMode: "design-mode",
    overlayProfile: "assembly-guides",
    toolPreset: "layout-toolkit",
    preferredViewportBehavior: "split",
  },
  systems: {
    stage: "systems",
    focusMode: "systems-mode",
    overlayProfile: "systems-insight",
    toolPreset: "systems-toolkit",
    preferredViewportBehavior: "quad",
  },
  spatial: {
    stage: "spatial",
    focusMode: "spatial-mode",
    overlayProfile: "spatial-cognition",
    toolPreset: "spatial-toolkit",
    preferredViewportBehavior: "split",
  },
  presentation: {
    stage: "presentation",
    focusMode: "analysis-mode",
    overlayProfile: "clean-render",
    toolPreset: "presentation-toolkit",
    preferredViewportBehavior: "single",
  },
};
