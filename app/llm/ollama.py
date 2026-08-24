import httpx

from app.core.config import settings


class OllamaClient:

    def __init__(self) -> None:
        self.base_url = settings.ollama_base_url
        self.model = settings.ollama_model

    async def chat(
        self,
        messages: list[dict[str, str]],
    ) -> str:

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
        }

        async with httpx.AsyncClient(
            timeout=120
        ) as client:

            response = await client.post(
                f"{self.base_url}/api/chat",
                json=payload,
            )

            response.raise_for_status()

            data = response.json()

        return data["message"]["content"]