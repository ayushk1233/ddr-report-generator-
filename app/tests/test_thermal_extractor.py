from app.services.extraction.thermal_extractor import (
    ThermalExtractor
)


def test_thermal_extractor_creation():

    extractor = ThermalExtractor()

    assert extractor is not None