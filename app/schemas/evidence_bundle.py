from pydantic import BaseModel, Field

from app.schemas.observation import Observation
from app.schemas.thermal_finding import ThermalFinding


class EvidenceBundle(BaseModel):
    area: str

    observations: list[Observation]

    inspection_images: list[str]

    thermal_images: list[str]

    thermal_findings: list[ThermalFinding]

    evidence_refs: list[str] = Field(
        default_factory=list
    )