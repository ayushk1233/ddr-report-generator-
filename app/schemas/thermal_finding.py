from pydantic import BaseModel
from uuid import UUID, uuid4


class ThermalFinding(BaseModel):
    finding_id: UUID = uuid4()

    page_number: int

    image_id: str

    hotspot: float

    coldspot: float

    anomaly_type: str

    confidence: float