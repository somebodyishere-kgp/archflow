export type InteractionState =
  | "idle"
  | "select"
  | "transform"
  | "parametric-edit"
  | "codesign-preview"
  | "constraint-adjust";

export type InteractionContext = {
  state: InteractionState;
  selectedIds: string[];
  hoverId?: string;
  snapPrediction?: { axis: string; score: number };
  constraintDragPreview?: string[];
  transformInertiaMs?: number;
};

const ALLOWED_TRANSITIONS: Record<InteractionState, InteractionState[]> = {
  idle: ["select", "codesign-preview"],
  select: ["idle", "transform", "parametric-edit", "constraint-adjust"],
  transform: ["select", "idle", "constraint-adjust"],
  "parametric-edit": ["select", "idle"],
  "codesign-preview": ["idle", "select"],
  "constraint-adjust": ["select", "transform", "idle"],
};

export function transitionInteraction(
  context: InteractionContext,
  next: InteractionState,
): InteractionContext {
  const allowed = ALLOWED_TRANSITIONS[context.state];
  if (!allowed.includes(next)) return context;
  return { ...context, state: next };
}

export function setInteractionHover(context: InteractionContext, hoverId?: string): InteractionContext {
  return { ...context, hoverId };
}

export function setSnapPrediction(
  context: InteractionContext,
  snapPrediction?: { axis: string; score: number },
): InteractionContext {
  return { ...context, snapPrediction };
}

export function setConstraintDragPreview(context: InteractionContext, preview: string[]): InteractionContext {
  return { ...context, constraintDragPreview: [...preview] };
}

export function setTransformInertia(context: InteractionContext, transformInertiaMs: number): InteractionContext {
  return { ...context, transformInertiaMs };
}
