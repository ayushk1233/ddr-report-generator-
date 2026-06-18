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

        thermal_pool = (
            thermal_findings
        )

        for area, area_observations in grouped.items():

            bundles.append(
                EvidenceBundle(
                    area=area,

                    observations=
                    area_observations,

                    inspection_images=[],

                    thermal_images=[],

                    thermal_findings=
                    thermal_pool
                )
            )

        return bundles