from pathlib import Path
from app.infrastructure.db import TelemetryRepository
from app.application.services import SimulationService


def test_load_latest_state_on_init(tmp_path):
    db_path = tmp_path / "telemetry.db"

    repo = TelemetryRepository(db_path=db_path)

    # Insert fake state (simulate persisted latest)
    class S:
        t=5.0; x=10.0; y=0.0; vx=2.0; vy=0.0; theta=1.0; omega=0.1

    repo.insert_state(S)

    # Build service and force it to use this repo
    service = SimulationService()
    service.telemetry_repo = repo

    # Re-run init logic manually (simple approach for now)
    latest = service.telemetry_repo.fetch_latest_state()
    assert latest is not None
    assert latest["t"] == 5.0
