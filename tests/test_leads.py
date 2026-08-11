from fastapi.testclient import TestClient


def test_leads_crud(client: TestClient, auth_headers: dict[str, str]) -> None:
    create = client.post(
        "/leads",
        headers=auth_headers,
        json={
            "name": "Maria",
            "empresa": "Acme",
            "email": "maria@acme.com",
            "telefone": "11999999999",
            "pontuacao": 80,
            "observacoes": "Interessada",
        },
    )
    assert create.status_code == 201
    lead_id = create.json()["id"]
    assert create.json()["name"] == "Maria"

    listed = client.get("/leads", headers=auth_headers)
    assert listed.status_code == 200
    assert len(listed.json()) == 1

    got = client.get(f"/leads/{lead_id}", headers=auth_headers)
    assert got.status_code == 200
    assert got.json()["empresa"] == "Acme"

    updated = client.patch(
        f"/leads/{lead_id}",
        headers=auth_headers,
        json={"pontuacao": 95, "status": False},
    )
    assert updated.status_code == 200
    assert updated.json()["pontuacao"] == 95
    assert updated.json()["status"] is False

    deleted = client.delete(f"/leads/{lead_id}", headers=auth_headers)
    assert deleted.status_code == 204

    missing = client.get(f"/leads/{lead_id}", headers=auth_headers)
    assert missing.status_code == 404


def test_leads_require_auth(client: TestClient) -> None:
    response = client.get("/leads")
    assert response.status_code == 401


def test_user_cannot_see_other_user_leads(client: TestClient) -> None:
    client.post("/auth/register", json={"email": "a@mail.com", "password": "senha123"})
    login_a = client.post("/auth/login", data={"username": "a@mail.com", "password": "senha123"})
    headers_a = {"Authorization": f"Bearer {login_a.json()['access_token']}"}

    client.post("/auth/register", json={"email": "b@mail.com", "password": "senha123"})
    login_b = client.post("/auth/login", data={"username": "b@mail.com", "password": "senha123"})
    headers_b = {"Authorization": f"Bearer {login_b.json()['access_token']}"}

    created = client.post(
        "/leads",
        headers=headers_a,
        json={
            "name": "Lead A",
            "empresa": "Empresa A",
            "email": "lead@a.com",
            "telefone": "11988887777",
        },
    )
    lead_id = created.json()["id"]

    forbidden = client.get(f"/leads/{lead_id}", headers=headers_b)
    assert forbidden.status_code == 404
