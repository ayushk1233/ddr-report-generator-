from app.schemas.recommendation import (
    Recommendation,
    RecommendationPriority
)

from app.schemas.root_cause import (
    RootCause
)

from app.schemas.severity import (
    SeverityAssessment,
    SeverityLevel
)


class RecommendationEngine:

    RECOMMENDATION_MAP = {
        "Skirting Dampness":
            "Inspect waterproofing and repair moisture ingress pathways.",

        "Wall Crack":
            "Conduct structural assessment and repair affected wall sections.",

        "Tile Hollowness":
            "Replace affected tiles and inspect substrate bonding.",

        "Seepage":
            "Investigate water entry points and improve drainage protection."
    }

    def generate(
        self,
        issue: str,
        root_cause: RootCause,
        severity: SeverityAssessment
    ) -> Recommendation:

        recommendation_text = (
            self.RECOMMENDATION_MAP.get(
                issue,
                "Further specialist inspection recommended."
            )
        )

        priority_map = {
            SeverityLevel.LOW:
                RecommendationPriority.LOW,

            SeverityLevel.MEDIUM:
                RecommendationPriority.MEDIUM,

            SeverityLevel.HIGH:
                RecommendationPriority.HIGH,

            SeverityLevel.CRITICAL:
                RecommendationPriority.CRITICAL
        }

        return Recommendation(
            recommendation=recommendation_text,
            priority=priority_map[
                severity.level
            ],
            linked_issue=issue
        )