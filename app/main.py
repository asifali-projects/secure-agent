from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.auth import router as auth_router
from app.api.v1.health import router as health_router
from app.core.logging import configure_logging
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.agent import router as agent_router


configure_logging()


app = FastAPI(
    title="Secure Agent",
    version="1.0.0",
    description=(
        "Production-oriented secure AI agent "
        "with authentication, authorization, "
        "tenant isolation, guardrails and "
        "controlled tool execution."
    ),
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)





app.include_router(
    health_router,
    prefix="/api/v1",
)

app.include_router(
    auth_router,
    prefix="/api/v1",
)

app.include_router(
    agent_router,
    prefix="/api/v1",
)


@app.get("/")
async def root():

    return {
        "service": "Secure Agent",
        "status": "running",
        "version": "1.0.0",
    }