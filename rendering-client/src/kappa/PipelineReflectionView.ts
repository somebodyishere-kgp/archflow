export function formatReflectionInsight(insight: { pipeline_id: string; capability_count: number; pattern_signature: string }): string {
  return `${insight.pipeline_id} :: ${insight.capability_count} :: ${insight.pattern_signature}`;
}
