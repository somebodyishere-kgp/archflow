from __future__ import annotations


def estimate_sun_path(latitude: float) -> dict:
    tilt = 23.5
    solar_band = "high" if abs(latitude) < 25 else "moderate"
    return {"solar_band": solar_band, "axial_tilt_deg": tilt}
