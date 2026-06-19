from app.schemas.ddr_report import (
    DDRReport
)

from app.schemas.evidence_bundle import (
    EvidenceBundle
)

from app.schemas.metadata import (
    ProcessingMetadata
)

from app.schemas.recommendation import (
    Recommendation
)

from app.schemas.root_cause import (
    RootCause
)

from app.schemas.severity import (
    SeverityAssessment
)


class DDRAssembler:

    def assemble(
        self,
        summary: str,
        bundles: list[EvidenceBundle],
        root_causes: list[RootCause],
        severities: list[SeverityAssessment],
        recommendations: list[Recommendation],
        area_narratives: list[str],
        conflicts: list[str],
        missing_information: list[str],
        metadata: ProcessingMetadata
    ) -> DDRReport:

        return DDRReport(
            property_issue_summary=summary,

            evidence_bundles=bundles,

            root_causes=root_causes,

            severity_assessments=
            severities,

            recommendations=
            recommendations,

            area_narratives=
            area_narratives,

            additional_notes=[],

            missing_information=
            missing_information,

            conflicts=
            conflicts,

            metadata=metadata
        )