from fastapi.testclient import TestClient


def test_health(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_register_and_me(client: TestClient) -> None:
    register = client.post(
        "/auth/register",
        json={"email": "ana@example.com", "password": "senha123"},
    )
    assert register.status_code == 201
    assert register.json()["email"] == "ana@example.com"

    login = client.post(
        "/auth/login",
        data={"username": "ana@example.com", "password": "senha123"},
    )
    assert login.status_code == 200
    token = login.json()["access_token"]

    me = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert me.status_code == 200
    assert me.json()["email"] == "ana@example.com"


def test_login_invalid(client: TestClient) -> None:
    client.post(
        "/auth/register",
        json={"email": "bob@example.com", "password": "senha123"},
    )
    response = client.post(
        "/auth/login",
        data={"username": "bob@example.com", "password": "errada"},
    )
    assert response.status_code == 401
