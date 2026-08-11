import requests

BASE_URL = "http://127.0.0.1:8000"


def login(email: str, password: str) -> str | None:
    response = requests.post(
        f"{BASE_URL}/auth/login",
        data={"username": email, "password": password},
        timeout=30,
    )
    data = response.json() if response.content else {}
    if not isinstance(data, dict):
        return None
    return data.get("access_token")


def listar_leads(token: str) -> list[dict]:
    response = requests.get(
        f"{BASE_URL}/leads",
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )
    data = response.json() if response.content else []
    if not isinstance(data, list):
        # API às vezes devolve {"detail": "..."} em erro
        return []
    return [normalizar_lead(item) for item in data if isinstance(item, dict)]


def obter_lead(token: str, lead_id: int) -> dict | None:
    response = requests.get(
        f"{BASE_URL}/leads/{lead_id}",
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )
    data = response.json() if response.content else {}
    if not isinstance(data, dict) or "id" not in data:
        return None
    return normalizar_lead(data)


def normalizar_lead(raw: dict) -> dict:
    return {
        "id": raw.get("id"),
        "name": raw.get("name") or raw.get("nome") or "",
        "empresa": raw.get("empresa") or "",
        "email": raw.get("email") or "",
        "telefone": raw.get("telefone") or raw.get("phone") or "",
        "status": raw.get("status", True),
        "pontuacao": raw.get("pontuacao", raw.get("score", 0)),
        "observacoes": raw.get("observacoes") or raw.get("notes") or "",
        "owner_id": raw.get("owner_id"),
        "created_at": raw.get("created_at"),
    }


def main() -> None:
    email = "ana@example.com"
    password = "senha123"

    token = login(email, password)
    if not token:
        print("Falha no login (sem access_token).")
        return

    leads = listar_leads(token)
    for lead in leads:
        print(
            f"#{lead.get('id')} | {lead.get('name')} | "
            f"{lead.get('empresa')} | score={lead.get('pontuacao')}"
        )


if __name__ == "__main__":
    main()
