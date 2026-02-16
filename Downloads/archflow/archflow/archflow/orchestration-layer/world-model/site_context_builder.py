from __future__ import annotations


def build_site_context(site: dict) -> dict:
    lat = float(site.get("lat", 0))
    lng = float(site.get("lng", 0))
    return {"site_coordinates": {"lat": lat, "lng": lng}, "hemisphere": "north" if lat >= 0 else "south"}
