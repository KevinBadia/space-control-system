from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_export_telemetry_csv_returns_text():
    r = client.get("/telemetry/export?limit=10&format=csv")
    assert r.status_code == 200
    assert "text/csv" in r.headers.get("content-type", "")
