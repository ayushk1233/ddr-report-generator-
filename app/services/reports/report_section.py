from pydantic import BaseModel

from app.schemas.observation import Observation
from app.schemas.thermal_finding import ThermalFinding
from app.schemas.root_cause import RootCause
from app.schemas.severity import SeverityAssessment
from app.schemas.recommendation import Recommendation


class ReportSection(BaseModel):

    area: str

    observations: list[Observation]

    inspection_images: list[str]

    thermal_images: list[str]

    thermal_findings: list[ThermalFinding]

    root_cause: RootCause

    severity: SeverityAssessment

    recommendation: Recommendation

    evidence_refs: list[str]

    narrative: str = ""