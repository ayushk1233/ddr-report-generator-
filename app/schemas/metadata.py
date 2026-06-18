from pydantic import BaseModel, Field


class ProcessingMetadata(BaseModel):
    extraction_time_seconds: float

    model_version: str

    confidence: float

    failures: list[str] = Field(default_factory=list)