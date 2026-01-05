from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_state():
    response = client.get("/state")
    assert response.status_code == 200
    data = response.json()
    assert "x" in data
    assert "vx" in data


def test_get_history_empty():
    response = client.get("/history")
    assert response.status_code == 200
    assert response.json() == []
