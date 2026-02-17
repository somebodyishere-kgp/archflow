export type SelectionState = {
  selectedIds: string[];
  activeId?: string;
  hoverId?: string;
  snapPredictionBuffer?: string[];
};

export function updateSelection(
  state: SelectionState,
  targetId: string,
  mode: "replace" | "toggle" = "replace",
): SelectionState {
  if (mode === "replace") {
    return { ...state, selectedIds: [targetId], activeId: targetId };
  }
  const selected = new Set(state.selectedIds);
  if (selected.has(targetId)) {
    selected.delete(targetId);
  } else {
    selected.add(targetId);
  }
  const selectedIds = Array.from(selected);
  return { ...state, selectedIds, activeId: selectedIds[selectedIds.length - 1] };
}

export function setHover(state: SelectionState, hoverId?: string): SelectionState {
  return { ...state, hoverId };
}

export function updateSnapPredictionBuffer(state: SelectionState, buffer: string[]): SelectionState {
  return { ...state, snapPredictionBuffer: [...buffer] };
}
