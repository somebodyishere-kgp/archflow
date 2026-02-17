export type SnapMode = "grid" | "axis" | "assembly-anchor" | "parametric-guide";

export type SnapIntent = {
  mode: SnapMode;
  source: string;
  target?: string;
  point: { x: number; y: number; z: number };
};

export class SnapManager {
  private enabledModes = new Set<SnapMode>(["grid", "axis"]);
  private modePriority: Record<SnapMode, number> = {
    axis: 4,
    "assembly-anchor": 3,
    "parametric-guide": 2,
    grid: 1,
  };

  setModeEnabled(mode: SnapMode, enabled: boolean): void {
    if (enabled) this.enabledModes.add(mode);
    else this.enabledModes.delete(mode);
  }

  isEnabled(mode: SnapMode): boolean {
    return this.enabledModes.has(mode);
  }

  emitSnapIntent(intent: SnapIntent): SnapIntent | null {
    if (!this.enabledModes.has(intent.mode)) return null;
    return {
      ...intent,
      target: intent.target || `priority-${this.modePriority[intent.mode]}`,
    };
  }

  sortModesByPriority(modes: SnapMode[]): SnapMode[] {
    return [...modes].sort((a, b) => this.modePriority[b] - this.modePriority[a]);
  }
}
