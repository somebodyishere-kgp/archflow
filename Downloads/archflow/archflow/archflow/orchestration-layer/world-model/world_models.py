from __future__ import annotations

from pydantic import BaseModel


class WorldContextMetrics(BaseModel):
    solar_priority_index: float
    wind_exposure_score: float
    urban_porosity: float
    public_flow_intensity: float
