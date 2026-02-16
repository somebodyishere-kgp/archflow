import { type InteractionState } from "../app-shell/InteractionStateMachine";

export type FeedbackSnapMode = "grid" | "axis" | "assembly-anchor" | "parametric-guide";

export type FeedbackAnchor = {
  id: string;
  point: { x: number; y: number; z: number };
  axis?: "x" | "y" | "z";
};

export type SnapPrediction = {
  mode: FeedbackSnapMode;
  anchorId: string;
  distance: number;
  glowIntensity: number;
  axisGuides: string[];
  constraintHints: string[];
};

export type GhostPreviewState = {
  previewId: string;
  source: "transform" | "ai-proposal" | "constraint-adjust";
  nodeIds: string[];
  opacity: number;
  persistent: false;
};

export type ConstraintVisualState = {
  distanceLines: Array<{ from: string; to: string; valueMm: number }>;
  alignmentBars: Array<{ axis: "x" | "y" | "z"; ids: string[] }>;
  hierarchyHighlights: Array<{ parentId: string; childIds: string[] }>;
};

export type InteractionMicroAnimation = {
  interactionState: InteractionState;
  easing: "linear" | "ease-out" | "ease-in-out";
  fadeMs: number;
  gizmoInertia: number;
  snapPulseMs: number;
};
