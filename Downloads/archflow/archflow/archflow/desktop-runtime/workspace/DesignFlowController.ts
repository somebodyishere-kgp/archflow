import { transitionInteraction, type InteractionContext } from "../app-shell/InteractionStateMachine";
import { AIFocusModeManager } from "./AIFocusModeManager";
import { WorkspaceStateEngine } from "./WorkspaceStateEngine";
import { FLOW_STAGE_PROFILES, type FlowStageProfile } from "./design_flow_models";
import { type DesignFlowStage, type WorkspaceLayoutPreset } from "./workspace_models";

function layoutForBehavior(behavior: FlowStageProfile["preferredViewportBehavior"]): WorkspaceLayoutPreset {
  if (behavior === "quad") return "quad-viewport";
  if (behavior === "split") return "plan-section-split";
  return "single-3d";
}

export class DesignFlowController {
  constructor(
    private workspace: WorkspaceStateEngine,
    private focusManager: AIFocusModeManager,
  ) {}

  transitionStage(stage: DesignFlowStage, interaction: InteractionContext): {
    profile: FlowStageProfile;
    interaction: InteractionContext;
  } {
    const profile = FLOW_STAGE_PROFILES[stage];
    this.workspace.setFlowTransitionLock(true);
    this.focusManager.setMode(profile.focusMode);
    this.workspace.setAIFocusMode(profile.focusMode);

    const preset = layoutForBehavior(profile.preferredViewportBehavior);
    const viewportLayouts =
      preset === "quad-viewport"
        ? ["perspective", "top", "front", "right"]
        : preset === "plan-section-split"
          ? ["plan-view", "section-view"]
          : ["main-3d"];
    this.workspace.setLayoutPreset(preset, viewportLayouts);
    this.workspace.setActiveTool(profile.toolPreset);
    this.workspace.transitionFlowStage(stage);
    this.workspace.setFlowTransitionLock(false);

    const nextInteraction = transitionInteraction(interaction, "select");
    return { profile, interaction: nextInteraction };
  }
}
