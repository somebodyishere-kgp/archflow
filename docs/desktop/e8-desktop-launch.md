# E8 Desktop Launch & Unified Runtime Boot

E8 completes desktop launch readiness by wiring a deterministic startup sequence for the existing E3-E7 runtime stack.

## Launch command
- `npm run archflow`

## Boot sequence
1. `SystemHealthCheck`
2. Runtime kernel startup marker
3. `WorkspaceStateEngine` initialization
4. Rendering host mount path via `AppShell`
5. `CADInteractionEngine` attachment
6. `LiveFeedbackController` attachment
7. `DesignPresenceRuntime` start
8. `DefaultSceneLoader` load

## Safety behavior
- If OCCT runtime is unavailable, desktop boot continues.
- Solid-edit tools are represented as disabled in health state.
- Runtime bridge exposes read-only status and presence signal channels only.

## E8 files
- `desktop-runtime/main.ts`
- `desktop-runtime/preload.ts`
- `desktop-runtime/runtime-bridge.ts`
- `desktop-runtime/window-manager.ts`
- `desktop-runtime/bootstrap/*`
- `desktop-runtime/app-shell/AppShell.tsx`
- `desktop-runtime/app-shell/SystemHealthPanel.tsx`

