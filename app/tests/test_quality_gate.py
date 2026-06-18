from app.services.reasoning.quality_gate import (
    QualityGate
)


def test_quality_gate_creation():

    gate = QualityGate()

    assert gate is not None
    