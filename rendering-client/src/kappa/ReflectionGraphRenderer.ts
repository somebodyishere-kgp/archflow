export type ReflectionNode = { id: string; label: string };

export function renderReflectionGraph(nodes: ReflectionNode[]): string[] {
  return nodes.map((node) => `${node.id}:${node.label}`).sort();
}
