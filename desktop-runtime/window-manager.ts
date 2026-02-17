import { BrowserWindow, app } from "electron";

let lastBounds: Electron.Rectangle | null = null;

export function createWindow(): BrowserWindow {
  const window = new BrowserWindow({
    width: lastBounds?.width || 1440,
    height: lastBounds?.height || 900,
    x: lastBounds?.x,
    y: lastBounds?.y,
    webPreferences: {
      preload: `${app.getAppPath()}/desktop-runtime/preload.ts`,
      contextIsolation: true,
      nodeIntegration: false,
    },
    show: false,
  });

  window.once("ready-to-show", () => window.show());
  window.on("close", () => {
    lastBounds = window.getBounds();
  });
  return window;
}

