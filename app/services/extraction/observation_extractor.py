import re

from app.schemas.observation import Observation
from app.services.extraction.patterns import OBSERVATION_PATTERNS


class ObservationExtractor:

    def extract(
        self,
        text: str,
        page_number: int
    ) -> list[Observation]:

        observations: list[Observation] = []

        for pattern, area, issue in OBSERVATION_PATTERNS:

            if re.search(pattern, text, re.IGNORECASE | re.DOTALL):
                observations.append(
                    Observation(
                        area=area,
                        issue=issue,
                        description=text.strip(),
                        page_number=page_number,
                        confidence=0.80
                    )
                )

        return observations