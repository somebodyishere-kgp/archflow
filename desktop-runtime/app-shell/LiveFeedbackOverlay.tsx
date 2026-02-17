import React from "react";

export function LiveFeedbackOverlay(): JSX.Element {
  return (
    <div
      style={{
        position: "absolute",
        inset: 0,
        pointerEvents: "none",
        border: "1px solid rgba(56, 189, 248, 0.12)",
        boxShadow: "inset 0 0 28px rgba(56, 189, 248, 0.08)",
      }}
    />
  );
}

