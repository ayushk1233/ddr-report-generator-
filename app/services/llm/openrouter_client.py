from openai import OpenAI

from app.core.config import settings
from app.core.logging import logger


class OpenRouterClient:

    def __init__(self):

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=settings.openrouter_api_key,
        )

        self.model = settings.openrouter_model

    def generate(
        self,
        prompt: str,
        temperature: float = 0.2,
    ) -> str:

        try:

            response = (
                self.client.chat.completions.create(
                    model=self.model,
                    temperature=temperature,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )
            )

            return (
                response
                .choices[0]
                .message
                .content
                .strip()
            )

        except Exception as exc:

            logger.exception(
                f"OpenRouter generation failed: {exc}"
            )

            return (
                "Narrative generation unavailable."
            )