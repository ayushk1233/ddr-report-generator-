from app.services.extraction.observation_extractor import ObservationExtractor


def test_observation_parsing():

    extractor = ObservationExtractor()

    text = "Hall Skirting level Dampness"

    observations = extractor.extract(
        text=text,
        page_number=1
    )

    assert len(observations) == 1

    observation = observations[0]

    assert observation.area == "Hall"
    assert observation.issue == "Skirting Dampness"
