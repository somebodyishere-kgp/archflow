export type MicroAnimationFrame = {
  easingValue: number;
  alpha: number;
  pulse: number;
};

export function computeMicroFrame(
  elapsedMs: number,
  fadeMs: number,
  inertia: number,
  pulseMs: number,
): MicroAnimationFrame {
  const t = Math.min(1, elapsedMs / Math.max(1, fadeMs));
  const pulse = 0.5 + 0.5 * Math.sin((elapsedMs / Math.max(1, pulseMs)) * Math.PI * 2);
  const safeInertia = Math.min(0.95, Math.max(0, inertia));
  return {
    easingValue: t * (2 - t) * (1 - safeInertia),
    alpha: t,
    pulse,
  };
}
