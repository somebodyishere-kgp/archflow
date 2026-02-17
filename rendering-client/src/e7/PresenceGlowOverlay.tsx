import { useEffect, useMemo, useState } from "react";
import { ViewportPulseScheduler, type PresencePulse } from "./ViewportPulseScheduler";

export type PresenceGlowOverlayProps = {
  viewportId: string;
};

export function PresenceGlowOverlay({ viewportId }: PresenceGlowOverlayProps) {
  const scheduler = useMemo(() => new ViewportPulseScheduler(), []);
  const [pulse, setPulse] = useState<PresencePulse>({
    viewportId,
    glow: 0,
    tension: 0,
    idleFade: 1,
    focusShift: 0,
    timestampMs: 0,
  });

  useEffect(() => {
    const unsubscribe = scheduler.subscribe((next) => {
      if (next.viewportId === viewportId) setPulse(next);
    });
    scheduler.start(viewportId);
    return () => {
      unsubscribe();
      scheduler.stop();
    };
  }, [scheduler, viewportId]);

  return (
    <div
      data-presence-overlay="true"
      style={{
        pointerEvents: "none",
        position: "absolute",
        inset: 0,
        opacity: 0.25 + pulse.idleFade * 0.25,
        background:
          "radial-gradient(circle at 50% 50%, rgba(96, 165, 250, 0.10), rgba(30, 41, 59, 0.02) 55%, transparent 100%)",
        boxShadow: `inset 0 0 ${24 + pulse.glow * 18}px rgba(59,130,246,${0.08 + pulse.glow * 0.16})`,
        transition: "opacity 100ms linear",
      }}
    />
  );
}

