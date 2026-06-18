import re

from app.schemas.observation import Observation


class ObservationExtractor:

    AREA_PATTERNS = [
        "Hall",
        "Bedroom",
        "Master Bedroom",
        "Kitchen",
        "Common Bathroom",
        "Parking",
        "External Wall"
    ]

    ISSUE_PATTERNS = [
        "Dampness",
        "Leakage",
        "Seepage",
        "Crack",
        "Cracks",
        "Tile Hollowness",
        "Efflorescence",
        "Plumbing Issue"
    ]

    def extract(
        self,
        text: str,
        page_number: int
    ) -> list[Observation]:

        observations: list[Observation] = []

        for area in self.AREA_PATTERNS:

            if area.lower() not in text.lower():
                continue

            for issue in self.ISSUE_PATTERNS:

                if issue.lower() not in text.lower():
                    continue

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