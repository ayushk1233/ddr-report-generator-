import json

from app.services.llm.openrouter_client import (
    OpenRouterClient
)

from app.schemas.intelligence_result import (
    IntelligenceResult
)


class DDRIntelligenceGenerator:

    def __init__(self):
        self.client = OpenRouterClient()

    def generate(
        self,
        findings: list[dict]
    ) -> IntelligenceResult:

        prompt = f"""
You are a professional building diagnostics consultant.

Generate:

1. Executive Summary
2. One narrative for each finding

Return ONLY valid JSON.

Schema:

{{
  "executive_summary": "...",
  "area_narratives": [
    "...",
    "..."
  ]
}}

Findings:

{json.dumps(findings, indent=2)}
"""

        response = self.client.generate(
            prompt=prompt,
            temperature=0.2
        )

        # Strip markdown formatting if present
        cleaned_response = response.strip()
        if cleaned_response.startswith("```json"):
            cleaned_response = cleaned_response[7:-3].strip()
        elif cleaned_response.startswith("```"):
            cleaned_response = cleaned_response[3:-3].strip()

        try:
            data = json.loads(cleaned_response)
        except json.JSONDecodeError:
            print(f"FAILED TO PARSE JSON. RAW RESPONSE:\\n{response}")
            raise

        return IntelligenceResult(
            executive_summary=
            data["executive_summary"],

            area_narratives=
            data["area_narratives"]
        )
