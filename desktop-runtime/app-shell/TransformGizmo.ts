export type TransformMode = "translate" | "rotate" | "scale";

export type TransformState = {
  mode: TransformMode;
  snapMm: number;
  enabled: boolean;
  dragPreview?: { x: number; y: number; z: number };
  constraintDragPreview?: string[];
};

export function setTransformMode(state: TransformState, mode: TransformMode): TransformState {
  return { ...state, mode };
}

export function toggleTransform(state: TransformState): TransformState {
  return { ...state, enabled: !state.enabled };
}

export function applyTransformDragPreview(
  state: TransformState,
  point: { x: number; y: number; z: number },
): TransformState {
  const snapped = {
    x: Math.round(point.x / state.snapMm) * state.snapMm,
    y: Math.round(point.y / state.snapMm) * state.snapMm,
    z: Math.round(point.z / state.snapMm) * state.snapMm,
  };
  return { ...state, dragPreview: snapped };
}

export function setConstraintDragPreview(state: TransformState, preview: string[]): TransformState {
  return { ...state, constraintDragPreview: [...preview] };
}
