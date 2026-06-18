from app.schemas.evidence_bundle import (
    EvidenceBundle
)


class QualityGate:

    def detect_conflicts(
        self,
        bundle: EvidenceBundle
    ) -> list[str]:

        conflicts: list[str] = []

        has_dampness = any(
            obs.issue == "Skirting Dampness"
            for obs in bundle.observations
        )

        has_no_anomaly = any(
            finding.anomaly_type
            == "NO_ANOMALY"
            for finding in bundle.thermal_findings
        )

        if (
            has_dampness
            and
            has_no_anomaly
        ):
            conflicts.append(
                "Inspection indicates dampness "
                "but thermal evidence shows "
                "no anomaly."
            )

        return conflicts

    def detect_missing_information(
        self,
        bundle: EvidenceBundle
    ) -> list[str]:

        missing: list[str] = []

        if not bundle.observations:

            missing.append(
                "No inspection observations."
            )

        if not bundle.thermal_findings:

            missing.append(
                "No thermal findings."
            )

        if not bundle.evidence_refs:

            missing.append(
                "No evidence references."
            )

        return missing