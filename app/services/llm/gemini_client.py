from google import genai

from app.core.config import settings
from app.core.logging import logger


class GeminiClient:
    """
    Thin wrapper around Gemini API.

    Responsibilities:
    - Configure Gemini client
    - Generate text
    - Handle failures gracefully

    Non-responsibilities:
    - DDR logic
    - Prompt construction
    - Report generation
    """

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

        self.model = settings.gemini_model

    def generate(
        self,
        prompt: str,
        temperature: float = 0.2
    ) -> str:
        """
        Generate text using Gemini.

        Args:
            prompt: Input prompt
            temperature: Creativity control

        Returns:
            Generated text response
        """

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config={
                    "temperature": temperature
                }
            )

            if response.text:
                return response.text.strip()

            return "Narrative generation unavailable."

        except Exception as exc:
            logger.exception(
                f"Gemini generation failed: {exc}"
            )

            return "Narrative generation unavailable."