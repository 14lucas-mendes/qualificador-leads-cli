# Qualificador de Leads — API FastAPI

API completa com banco, autenticação JWT, CRUD de leads, testes e deploy no Render.

## Subir local

```powershell
uv venv .venv311 --python 3.11
.\.venv311\Scripts\Activate.ps1
uv pip install -r requirements.txt
uvicorn app.main:app --reload
```

Abra: http://127.0.0.1:8000/docs

## Endpoints

| Método | Rota | Auth | O que faz |
|--------|------|------|-----------|
| GET | `/health` | não | health check |
| POST | `/auth/register` | não | cria usuário `{email, password}` |
| POST | `/auth/login` | não | form `username`+`password` → JWT |
| GET | `/auth/me` | sim | usuário logado |
| POST | `/leads` | sim | cria lead |
| GET | `/leads` | sim | lista leads do usuário |
| GET | `/leads/{id}` | sim | detalhe |
| PATCH | `/leads/{id}` | sim | atualiza campos |
| DELETE | `/leads/{id}` | sim | remove |

## Fluxo no /docs

1. `POST /auth/register`
2. `POST /auth/login` → copie `access_token`
3. **Authorize** → cole o token
4. Use `/leads`

## Testes

```powershell
.\.venv311\Scripts\python.exe -m pytest -q
```

## Deploy no Render

1. Suba o repo no GitHub
2. Render → **New → Blueprint** → este repo (`render.yaml`)
3. Cria web service + Postgres; `SECRET_KEY` e `DATABASE_URL` entram sozinhas
4. A app escuta em `0.0.0.0:$PORT`

Docker local:

```powershell
docker build -t leads-api .
docker run -p 8000:8000 -e SECRET_KEY=dev -e DATABASE_URL=sqlite:///./leads.db leads-api
```

## Arquivos (ordem de leitura)

1. `app/main.py` — sobe a app
2. `app/schemas.py` — contratos Pydantic
3. `app/models.py` — tabelas
4. `app/auth.py` — senha + JWT
5. `app/services.py` + `app/routers/*` — regras e rotas
6. `tests/*` — comportamento esperado
7. `render.yaml` — deploy
