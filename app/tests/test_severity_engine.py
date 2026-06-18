from app.services.reasoning.severity_engine import (
    SeverityEngine
)


def test_severity_engine_creation():

    engine = SeverityEngine()

    assert engine is not None