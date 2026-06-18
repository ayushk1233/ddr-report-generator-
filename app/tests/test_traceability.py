from app.schemas.observation import (
    Observation
)

from app.schemas.thermal_finding import (
    ThermalFinding
)

from app.services.evidence.evidence_builder import (
    EvidenceBuilder
)


def test_evidence_references():

    builder = EvidenceBuilder()

    bundles = builder.build(
        observations=[
            Observation(
                area="Hall",
                issue="Skirting Dampness",
                description="test",
                page_number=5,
                confidence=1.0
            )
        ],
        thermal_findings=[
            ThermalFinding(
                page_number=7,
                image_id="1",
                hotspot=28.8,
                coldspot=23.4,
                anomaly_type="MOISTURE_PATTERN",
                confidence=0.9
            )
        ]
    )

    assert (
        bundles[0].evidence_refs[0]
        ==
        "inspection_page_5"
    )
