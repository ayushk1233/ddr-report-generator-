from app.schemas.observation import Observation
from app.schemas.thermal_finding import ThermalFinding
from app.services.evidence.evidence_builder import EvidenceBuilder

def test_thermal_finding_correlation():
    builder = EvidenceBuilder()

    observations = [
        Observation(
            area="Hall",
            issue="Skirting Dampness",
            description="Dampness near skirting",
            page_number=1,
            confidence=0.9
        ),
        Observation(
            area="Kitchen",
            issue="Seepage",
            description="Seepage in kitchen sink area",
            page_number=2,
            confidence=0.8
        )
    ]

    thermal_findings = [
        ThermalFinding(
            area="Hall",
            image_id="hall_thermal_1",
            hotspot=30.0,
            coldspot=22.0,
            anomaly_type="MOISTURE_PATTERN",
            page_number=3,
            confidence=0.95
        )
    ]

    bundles = builder.build(
        observations=observations,
        thermal_findings=thermal_findings
    )

    hall_bundle = next((b for b in bundles if b.area == "Hall"), None)
    kitchen_bundle = next((b for b in bundles if b.area == "Kitchen"), None)

    assert hall_bundle is not None
    assert kitchen_bundle is not None

    # Hall thermal finding should only be in Hall bundle
    assert len(hall_bundle.thermal_findings) == 1
    assert hall_bundle.thermal_findings[0].area == "Hall"

    # Kitchen bundle should have no thermal findings
    assert len(kitchen_bundle.thermal_findings) == 0
