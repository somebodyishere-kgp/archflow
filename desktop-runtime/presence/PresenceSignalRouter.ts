import { type PresenceSignal, type PresenceSignalType } from "./presence_models";

type PresenceListener = (signal: PresenceSignal) => void;

export class PresenceSignalRouter {
  private listeners = new Map<PresenceSignalType, Set<PresenceListener>>();
  private trace: PresenceSignal[] = [];
  private readonly maxTrace = 128;

  subscribe(signalType: PresenceSignalType, listener: PresenceListener): () => void {
    const bucket = this.listeners.get(signalType) || new Set<PresenceListener>();
    bucket.add(listener);
    this.listeners.set(signalType, bucket);
    return () => {
      const active = this.listeners.get(signalType);
      if (!active) return;
      active.delete(listener);
      if (active.size === 0) this.listeners.delete(signalType);
    };
  }

  emit(signal: PresenceSignal): void {
    const listeners = this.listeners.get(signal.signalType);
    if (listeners) {
      listeners.forEach((listener) => listener(signal));
    }
    this.trace.push(signal);
    if (this.trace.length > this.maxTrace) {
      this.trace.shift();
    }
  }

  latestSignals(): PresenceSignal[] {
    return this.trace.map((item) => ({ ...item, metadata: item.metadata ? { ...item.metadata } : undefined }));
  }
}

