import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.api.routes import simulation


@pytest.fixture(autouse=True)
def reset_simulation():
    simulation.__init__()
    yield