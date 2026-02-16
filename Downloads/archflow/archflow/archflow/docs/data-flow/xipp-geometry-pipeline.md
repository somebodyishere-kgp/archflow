# Data Flow: XI++ Geometry Pipeline

Input:
- `design.intent.generated`
- Program/zoning requirements

Process:
- Synthesis resolves hierarchy, density, and egress.
- Geometry execution derives auditorium, room clusters, circulation, structural grid, and assemblies.
- Drawing engine emits mm-accurate plan/section/elevation DTOs.

Output:
- `geometry.execution.proposed`
- `assembly.generated`
- proposal payload for executor boundary
