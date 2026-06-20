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



            correlator = ThermalCorrelator()
            
            mapping = correlator.correlate(
                area_observations,
                area_thermal_findings
            )
            
            correlated_findings = []

            for findings in mapping.values():

                for finding in findings:

                    if finding not in correlated_findings:

                        correlated_findings.append(
                            finding
                        )

            inspection_images = []

            for observation in area_observations:

                for image in observation.image_ids:

                    if image not in inspection_images:

                        inspection_images.append(
                            image
                        )

            thermal_images = []

            for finding in correlated_findings:

                if (
                    finding.thermal_image_path
                    and
                    finding.thermal_image_path
                    not in thermal_images
                ):
                    thermal_images.append(
                        finding.thermal_image_path
                    )

            bundles.append(
                EvidenceBundle(
                    area=area,

                    observations=
                    area_observations,

                    inspection_images=
                    inspection_images[:3],

                    thermal_images=thermal_images,

                    thermal_findings=
                    correlated_findings,

                    evidence_refs=[
                        f"inspection_page_{obs.page_number}"
                        for obs in area_observations
                    ]
                )
            )

        return bundles