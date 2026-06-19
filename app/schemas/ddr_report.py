from pydantic import BaseModel

from app.schemas.evidence_bundle import EvidenceBundle
from app.schemas.metadata import ProcessingMetadata
from app.schemas.recommendation import Recommendation
from app.schemas.root_cause import RootCause
from app.schemas.severity import SeverityAssessment


class DDRReport(BaseModel):
    property_issue_summary: str

    evidence_bundles: list[EvidenceBundle]

    root_causes: list[RootCause]

    severity_assessments: list[SeverityAssessment]

    recommendations: list[Recommendation]

    area_narratives: list[str]

    additional_notes: list[str]

    missing_information: list[str]

    conflicts: list[str]

    metadata: ProcessingMetadata