from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class ThermalFinding(BaseModel):
    finding_id: UUID = Field(default_factory=uuid4)

    page_number: int

    area: str | None = None

    image_id: str

    hotspot: float

    coldspot: float

    anomaly_type: str

    confidence: float

    thermal_image_path: str | None = None

    visible_image_path: str | None = None