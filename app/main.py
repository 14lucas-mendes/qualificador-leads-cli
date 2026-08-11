from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import database
from app.routers import auth, leads


@asynccontextmanager
async def lifespan(_: FastAPI):
    database.Base.metadata.create_all(bind=database.engine)
    yield


app = FastAPI(
    title="Qualificador de Leads API",
    description="API FastAPI com banco, autenticação JWT, CRUD de leads e docs automáticas.",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(auth.router)
app.include_router(leads.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
