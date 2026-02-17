export type PresenceSignalType =
  | "hover.idle"
  | "snap.proximity"
  | "constraint.tension"
  | "ai.intent.idle"
  | "viewport.focus.shift";

export type PresenceSignalSource = "interaction" | "design-flow" | "feedback" | "workspace";

export type PresenceSignal = {
  signalType: PresenceSignalType;
  source: PresenceSignalSource;
  workspaceId: string;
  viewportId: string;
  intensity: number;
  timestampMs: number;
  metadata?: Record<string, string | number | boolean>;
};

export type PresenceFrameState = {
  hoverId?: string;
  snapDistance?: number;
  constraintHints: string[];
  stage: "concept" | "layout" | "systems" | "spatial" | "presentation";
  focusMode:
    | "design-mode"
    | "analysis-mode"
    | "spatial-mode"
    | "systems-mode"
    | "world-context-mode";
  pointerVelocity: number;
};

export type IdleFeedbackSample = {
  frameId: number;
  pulse: number;
  overlayFade: number;
  timestampMs: number;
};

