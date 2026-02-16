import React from "react";

export type GhostMesh = {
  node_id: string;
  opacity: number;
  source: string;
};

export function GhostMeshRenderer(props: { meshes: GhostMesh[] }): JSX.Element {
  return <section>Ghost Meshes: {props.meshes.map((mesh) => `${mesh.node_id}@${mesh.opacity}`).join(", ")}</section>;
}
