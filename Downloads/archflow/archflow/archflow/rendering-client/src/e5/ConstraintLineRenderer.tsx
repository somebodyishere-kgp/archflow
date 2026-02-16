import React from "react";

export function ConstraintLineRenderer(props: { lines: Array<{ from: string; to: string; valueMm: number }> }): JSX.Element {
  return <section>Constraint Lines: {props.lines.map((line) => `${line.from}-${line.to}:${line.valueMm}`).join(", ")}</section>;
}
