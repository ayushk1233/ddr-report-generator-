from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class Observation(BaseModel):
    observation_id: UUID = uuid4()

    area: str
    issue: str
    description: str

    page_number: int

    image_ids: list[str] = Field(default_factory=list)

    confidence: float