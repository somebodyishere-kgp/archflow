export type IntentZone = { id: string; intensity: number };

export function computeIntentZoneGlow(ids: string[], baseIntensity = 0.6): IntentZone[] {
  return ids.map((id, index) => ({
    id,
    intensity: Math.max(0.2, baseIntensity - index * 0.05),
  }));
}
