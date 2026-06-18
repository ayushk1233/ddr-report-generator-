from app.services.reasoning.root_cause_engine import (
    RootCauseEngine
)


def test_engine_creation():

    engine = RootCauseEngine()

    assert engine is not None