export type DefaultScene = {
  assemblies: Array<{ id: string; type: string; position: [number, number, number] }>;
  camera: { position: [number, number, number]; target: [number, number, number] };
  grid: { size: number; divisions: number };
  lightRig: { key: number; fill: number; ambient: number };
};

export class DefaultSceneLoader {
  load(): DefaultScene {
    return {
      assemblies: [{ id: "assembly-seed-001", type: "seed-block", position: [0, 0, 0] }],
      camera: { position: [8, 8, 8], target: [0, 0, 0] },
      grid: { size: 100, divisions: 20 },
      lightRig: { key: 0.8, fill: 0.45, ambient: 0.35 },
    };
  }
}

