from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Secure Agent"
    environment: str = "development"

    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 30
    jwt_issuer: str = "secure-agent"
    jwt_audience: str = "secure-agent-api"

    nemo_config_path: str = "config/nemo"

    redis_url: str = "redis://localhost:6379/0"

    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "secure_agent_docs"

    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "qwen3:8b"

    max_input_chars: int = 12000
    max_output_chars: int = 12000
    max_agent_steps: int = 8
    max_tool_calls: int = 8

    rate_limit_per_minute: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()