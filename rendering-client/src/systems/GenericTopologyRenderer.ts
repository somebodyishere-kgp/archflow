export type GenericNode = { id: string; type: string };
export type GenericEdge = { source: string; target: string };

export function renderTopology(nodes: GenericNode[], edges: GenericEdge[]): string {
  return `nodes=${nodes.length};edges=${edges.length}`;
}
