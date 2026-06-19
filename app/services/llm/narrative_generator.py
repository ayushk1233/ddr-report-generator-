from pydantic import BaseModel

from app.schemas.observation import Observation
from app.schemas.root_cause import RootCause
from app.schemas.severity import SeverityAssessment
from app.schemas.recommendation import Recommendation

from app.services.llm.gemini_client import GeminiClient
from app.services.llm.prompts import AREA_NARRATIVE_PROMPT


class NarrativeResult(BaseModel):
    area: str
    narrative: str


class NarrativeGenerator:
    """
    Converts structured findings into
    client-friendly narratives.
    """

    def __init__(self):
        self.client = GeminiClient()

    def generate_area_narrative(
        self,
        observation: Observation,
        root_cause: RootCause,
        severity: SeverityAssessment,
        recommendation: Recommendation,
    ) -> NarrativeResult:

        prompt = AREA_NARRATIVE_PROMPT.format(
            area=observation.area,
            issue=observation.issue,
            description=observation.description,
            root_cause=root_cause.cause,
            root_cause_rationale=root_cause.rationale,
            severity=severity.level.value,
            recommendation=recommendation.recommendation,
        )

        narrative = self.client.generate(
            prompt=prompt,
            temperature=0.2,
        )

        return NarrativeResult(
            area=observation.area,
            narrative=narrative,
        )