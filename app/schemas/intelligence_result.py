from pydantic import BaseModel


class IntelligenceResult(BaseModel):
    executive_summary: str
    area_narratives: list[str]
