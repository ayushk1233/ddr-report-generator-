from app.services.llm.gemini_client import GeminiClient
from app.services.llm.prompts import (
    EXECUTIVE_SUMMARY_PROMPT,
)


class ExecutiveSummaryGenerator:

    def __init__(self):
        self.client = GeminiClient()

    def generate(
        self,
        area_findings: list[str],
    ) -> str:

        findings_text = "\n".join(
            area_findings
        )

        prompt = (
            EXECUTIVE_SUMMARY_PROMPT.format(
                area_findings=findings_text
            )
        )

        return self.client.generate(
            prompt=prompt,
            temperature=0.2,
        )