from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI

from kernel import RuntimeKernel


def create_app(event_log_path: Path) -> FastAPI:
    app = FastAPI(title="Runtime Kernel", version="0.1.0")
    kernel = RuntimeKernel(event_log_path)

    @app.get("/runtime/state")
    def runtime_state() -> dict:
        return kernel.runtime_state()

    return app
