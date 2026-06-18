from app.schemas.observation import (
    Observation
)

from app.schemas.thermal_finding import (
    ThermalFinding
)

from app.services.evidence.evidence_builder import (
    EvidenceBuilder
)


def test_builder_creation():

    builder = EvidenceBuilder()

    assert builder is not None