from app.services.extraction.observation_extractor import (
    ObservationExtractor
)


def test_extractor_creation():

    extractor = ObservationExtractor()

    assert extractor is not None