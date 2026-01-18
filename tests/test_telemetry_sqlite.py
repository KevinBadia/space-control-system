import os
from pathlib import Path

from app.application.services import SimulationService
from app.application.commands import Command


def test_sqlite_persists_rows(tmp_path, monkeypatch):
    # Force DB into temp path for test isolation
    db_path = tmp_path / "telemetry.db"

    # Monkeypatch repository path by creating repo with custom path
    service = SimulationService()
    service.telemetry_repo.db_path = db_path
    service.telemetry_repo.db_path.parent.mkdir(parents=True, exist_ok=True)
    service.telemetry_repo._init_db()

    # Step a few times
    service.step(1.0)
    service.step(1.0)

    rows = service.telemetry_repo.fetch_last(limit=10)
    assert len(rows) == 2
    assert rows[0]["id"] > 0
    assert rows[0]["t"] >= 1.0
