from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_status_endpoint_returns_snapshot():
    r = client.get("/status")
    assert r.status_code == 200
    data = r.json()
    assert "running" in data
    assert "step_count" in data
    assert "uptime_s" in data
