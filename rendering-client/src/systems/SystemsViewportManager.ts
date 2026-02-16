export class SystemsViewportManager {
  private activeSystemDomain = "generic";

  setSystemDomain(domain: string): void {
    this.activeSystemDomain = domain;
  }

  getSystemDomain(): string {
    return this.activeSystemDomain;
  }
}
