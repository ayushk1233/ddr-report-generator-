from collections import defaultdict

from app.services.evidence.thermal_correlator import (
    ThermalCorrelator
)

from app.schemas.evidence_bundle import (
    EvidenceBundle
)

from app.schemas.observation import (
    Observation
)

from app.schemas.thermal_finding import (
    ThermalFinding
)


class EvidenceBuilder:

    def build(
        self,
        observations: list[Observation],
        thermal_findings: list[ThermalFinding]
    ) -> list[EvidenceBundle]:

        grouped: dict[
            str,
            list[Observation]
        ] = defaultdict(list)

        for observation in observations:

            grouped[
                observation.area
            ].append(
                observation
            )

        bundles: list[
            EvidenceBundle
        ] = []

        for area, area_observations in grouped.items():

            area_thermal_findings = [
                finding
                for finding in thermal_findings
                if finding.area == area
            ]

            if not area_thermal_findings:

                area_thermal_findings = [
                    f for f in thermal_findings
                    if f.area is None
                ]

            correlator = ThermalCorrelator()
            
            mapping = correlator.correlate(
                area_observations,
                area_thermal_findings
            )
            
            correlated_findings = []
            for findings in mapping.values():
                for f in findings:
                    if f not in correlated_findings:
                        correlated_findings.append(f)

            inspection_images = []

            for observation in area_observations:

                for image in observation.image_ids:

                    if image not in inspection_images:

                        inspection_images.append(
                            image
                        )

            bundles.append(
                EvidenceBundle(
                    area=area,

                    observations=
                    area_observations,

                    inspection_images=
                    inspection_images[:1],

                    thermal_images=[],

                    thermal_findings=
                    correlated_findings,

                    evidence_refs=[
                        f"inspection_page_{obs.page_number}"
                        for obs in area_observations
                    ]
                )
            )

        return bundles