
from app.services.pdf.image_extractor import ImageExtractor


def test_image_extractor_creation():

    extractor = ImageExtractor()

    assert extractor is not None