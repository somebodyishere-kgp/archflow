# E5 Feedback Runtime Flow

Feature: Live Design Feedback + CAD Interaction Stabilization

Input:
- pointer movement and selection events
- snap intents and anchor proximity
- transform drag state and constraint sets

Process:
- `CADInteractionEngine` routes interaction to feedback pipeline
- `PredictiveSnapFeedback` computes anchor prediction and hints
- `GhostPreviewManager` + `ghost_preview_pipeline.py` generate temporary mesh previews
- `ConstraintVisualizer` builds visual overlays for constraints
- `kernel_feedback_adapter` coordinates `feedback.update` before `geometry.execution`

Output:
- `feedback.snap.predicted`
- `feedback.preview.updated`
- `feedback.constraint.visualized`

Validation:
- feedback phase cannot call rebuild pipeline directly
- preview payloads are non-persistent
- rendering path is read-only
