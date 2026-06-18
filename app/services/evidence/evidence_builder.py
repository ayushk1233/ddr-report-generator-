from collections import defaultdict

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

            bundles.append(
                EvidenceBundle(
                    area=area,

                    observations=
                    area_observations,

                    inspection_images=[],

                    thermal_images=[],

                    thermal_findings=
                    area_thermal_findings,

                    evidence_refs=[
                        f"inspection_page_{obs.page_number}"
                        for obs in area_observations
                    ]
                )
            )

        return bundles