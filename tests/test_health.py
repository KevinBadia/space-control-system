from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_info_check():
    response = client.get("/info")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"info": "info aqui"}