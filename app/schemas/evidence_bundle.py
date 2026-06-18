from pydantic import BaseModel

from app.schemas.observation import Observation
from app.schemas.thermal_finding import ThermalFinding


class EvidenceBundle(BaseModel):
    area: str

    observations: list[Observation]

    inspection_images: list[str]

    thermal_images: list[str]

    thermal_findings: list[ThermalFinding]