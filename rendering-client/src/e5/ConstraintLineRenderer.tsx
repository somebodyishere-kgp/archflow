import React from "react";

export function ConstraintLineRenderer(props: { lines: Array<{ from: string; to: string; valueMm: number }> }): JSX.Element {
  const label = React.useMemo(
    () => props.lines.map((line) => `${line.from}-${line.to}:${line.valueMm}`).join(", "),
    [props.lines],
  );
  return <section>Constraint Lines: {label}</section>;
}
