from fastapi import FastAPI, HTTPException

app = FastAPI(title="MEP Agent", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "phase": "sprint-0"}


@app.post("/v1/mep/route")
def mep_route(payload: dict) -> dict:
    if not isinstance(payload, dict):
        raise HTTPException(status_code=400, detail="Invalid JSON payload.")
    raise HTTPException(
        status_code=501,
        detail="BLOCKED: ISSUE-0005 deterministic MEP route solver not integrated.",
    )
