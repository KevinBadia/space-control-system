from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_step_advances_time():
    r1 = client.get("/state").json()
    client.post("/step", json={"dt": 1.0})
    r2 = client.get("/state").json()

    assert r2["t"] == r1["t"] + 1.0

def test_command_force_affects_next_step():
    client.post("/command", json={"type": "apply_force", "fx": 2.0, "fy": 0.0})
    client.post("/step", json={"dt": 1.0})
    s = client.get("/state").json()
    assert s["vx"] >= 1.0  # allow slight float tolerance