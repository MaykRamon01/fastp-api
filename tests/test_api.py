import pytest
from fastapi.testclient import TestClient

from app.db import USER
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_users():
    USER.clear()
    yield
    USER.clear()


def test_health_check():
    response = client.get("/health_check")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_user():
    response = client.post(
        "/api/v1/users/",
        json={"name": "Ana", "email": "ana@example.com"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Ana"
    assert data["email"] == "ana@example.com"
    assert "id" in data


def test_list_users():
    client.post(
        "/api/v1/users/",
        json={"name": "Ana", "email": "ana@example.com"},
    )
    client.post(
        "/api/v1/users/",
        json={"name": "Bia", "email": "bia@example.com"},
    )

    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["users"], list)
    assert len(data["users"]) == 2
