from pydantic import BaseModel


class RootCause(BaseModel):
    cause: str
    rationale: str

    evidence_ids: list[str]

    confidence: float