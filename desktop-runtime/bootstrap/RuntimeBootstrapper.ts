import { CADInteractionEngine } from "../app-shell/CADInteractionEngine";
import { LiveFeedbackController } from "../feedback/LiveFeedbackController";
import { DesignPresenceRuntime } from "../presence/DesignPresenceRuntime";
import { PresenceSignalRouter } from "../presence/PresenceSignalRouter";
import { SnapManager } from "../../rendering-client/src/interactions/SnapManager";
import { WorkspaceStateEngine } from "../workspace/WorkspaceStateEngine";
import { DefaultSceneLoader, type DefaultScene } from "./DefaultSceneLoader";
import { SystemHealthCheck, type RuntimeHealthSnapshot } from "./SystemHealthCheck";
import { BootPerformanceProfiler, type BootMetrics } from "./BootPerformanceProfiler";

export type RuntimeBootState = {
  health: RuntimeHealthSnapshot;
  workspace: WorkspaceStateEngine;
  feedback: LiveFeedbackController;
  presence: DesignPresenceRuntime;
  interaction: CADInteractionEngine;
  scene: DefaultScene;
  metrics: BootMetrics;
};

export class RuntimeBootstrapper {
  private profiler = new BootPerformanceProfiler();

  boot(): RuntimeBootState {
    this.profiler.mark("boot.start");
    const health = new SystemHealthCheck().run();
    const workspace = new WorkspaceStateEngine();
    this.profiler.mark("runtime.kernel.ready");
    this.profiler.mark("window.open");
    this.profiler.mark("viewport.mount");

    const snapManager = new SnapManager();
    const feedback = new LiveFeedbackController(snapManager);
    const router = new PresenceSignalRouter();
    const presence = new DesignPresenceRuntime(router, "local-workspace", "main-viewport");
    feedback.attachPresenceRouter(router);
    const interaction = new CADInteractionEngine(feedback, presence);

    presence.start();
    const scene = new DefaultSceneLoader().load();
    this.profiler.mark("first.frame");

    const metrics = this.profiler.buildMetrics();
    return { health: { ...health, feedback: "ACTIVE", presence: "ACTIVE" }, workspace, feedback, presence, interaction, scene, metrics };
  }
}

