from app.schemas.evidence_bundle import (
    EvidenceBundle
)

from app.schemas.severity import (
    SeverityAssessment,
    SeverityLevel
)


class SeverityEngine:

    def assess(
        self,
        bundle: EvidenceBundle
    ) -> SeverityAssessment:

        issues = {
            observation.issue
            for observation in bundle.observations
        }

        anomalies = {
            finding.anomaly_type
            for finding in bundle.thermal_findings
        }

        if (
            "Skirting Dampness" in issues
            and
            "MOISTURE_PATTERN" in anomalies
        ):
            return SeverityAssessment(
                level=SeverityLevel.HIGH,
                rule_triggered=(
                    "Dampness confirmed "
                    "by thermal anomaly"
                ),
                supporting_evidence=
                bundle.evidence_refs
            )

        if (
            "Wall Crack" in issues
        ):
            return SeverityAssessment(
                level=SeverityLevel.HIGH,
                rule_triggered=(
                    "Structural crack detected"
                ),
                supporting_evidence=
                bundle.evidence_refs
            )

        if (
            "Tile Hollowness" in issues
        ):
            return SeverityAssessment(
                level=SeverityLevel.MEDIUM,
                rule_triggered=(
                    "Localized flooring issue"
                ),
                supporting_evidence=
                bundle.evidence_refs
            )

        return SeverityAssessment(
            level=SeverityLevel.LOW,
            rule_triggered=(
                "No high-risk indicators"
            ),
            supporting_evidence=
            bundle.evidence_refs
        )