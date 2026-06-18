import re

from app.schemas.thermal_finding import (
    ThermalFinding
)


class ThermalExtractor:

    HOTSPOT_PATTERN = (
        r"Hotspot\s*:\s*([0-9.]+)"
    )

    COLDSPOT_PATTERN = (
        r"Coldspot\s*:\s*([0-9.]+)"
    )

    def extract(
        self,
        text: str,
        page_number: int,
        area: str | None = None
    ) -> ThermalFinding | None:

        hotspot_match = re.search(
            self.HOTSPOT_PATTERN,
            text,
            re.IGNORECASE
        )

        coldspot_match = re.search(
            self.COLDSPOT_PATTERN,
            text,
            re.IGNORECASE
        )

        if (
            hotspot_match is None
            or
            coldspot_match is None
        ):
            return None

        hotspot = float(
            hotspot_match.group(1)
        )

        coldspot = float(
            coldspot_match.group(1)
        )

        anomaly_type = (
            self.classify_anomaly(
                hotspot,
                coldspot
            )
        )

        return ThermalFinding(
            page_number=page_number,
            area=area,
            image_id="unknown",
            hotspot=hotspot,
            coldspot=coldspot,
            anomaly_type=anomaly_type,
            confidence=0.90
        )

    def classify_anomaly(
        self,
        hotspot: float,
        coldspot: float
    ) -> str:

        delta = hotspot - coldspot

        if delta >= 5:
            return "MOISTURE_PATTERN"

        if delta >= 3:
            return "COLD_ANOMALY"

        return "NO_ANOMALY"