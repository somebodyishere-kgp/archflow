from fastapi import FastAPI, HTTPException

app = FastAPI(title="Structure Agent", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "phase": "sprint-0"}


@app.post("/v1/structure/size")
def structure_size(payload: dict) -> dict:
    if not isinstance(payload, dict):
        raise HTTPException(status_code=400, detail="Invalid JSON payload.")
    raise HTTPException(
        status_code=501,
        detail="BLOCKED: ISSUE-0003 deterministic structural solver not integrated.",
    )
