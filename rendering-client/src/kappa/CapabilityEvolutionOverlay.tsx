import { createElement } from "react";

type Props = {
  readonly proposalCount: number;
};

export function CapabilityEvolutionOverlay({ proposalCount }: Props) {
  return createElement("div", { "data-capability-evolution": true }, `Capability proposals: ${proposalCount}`);
}
