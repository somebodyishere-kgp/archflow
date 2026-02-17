# Open Source Integration Rationale

## Selection Principles
- Must fit a defined ArchFlow module boundary
- Must preserve TwinGraph as source of truth
- Must not introduce file-first CAD workflows
- Must remain CI-reproducible in containerized pipelines

## Integrated / Planned Baseline

### OpenCascade
- Layer: `geometry-kernel`
- Reason: robust B-Rep operations and deterministic geometry processing
- Integration Pattern: C++ service container, optional WASM wrapper for client constraints
- License Note: verify compliance in packaged distributions

### IfcOpenShell + IFC.js
- Layer: BIM parsing and adapters
- Reason: deterministic extraction and web adapter compatibility
- Integration Pattern: parser service emits typed events and TwinGraph mutation payloads
- License Note: monitor LGPL obligations in release artifacts

### Three.js / React Three Fiber
- Layer: rendering-client
- Reason: mature scene graph and query-driven visualization capabilities
- Integration Pattern: render-only views generated from TwinGraph queries

### NATS
- Layer: event bus
- Reason: low-latency pub/sub with simple operations for modular agents
- Integration Pattern: typed JSON payload validation before publish/subscribe

### Qdrant
- Layer: semantic retrieval
- Reason: efficient vector indexing for document and clause retrieval support
- Integration Pattern: isolated microservice adapter with version-pinned container

## Blocked / Deferred Integrations
- EnergyPlus, Radiance, and acoustic simulation wrappers are deferred to deterministic CI-ready containers in later sprints and tracked as blockers in `docs/status/system-status.md`.
