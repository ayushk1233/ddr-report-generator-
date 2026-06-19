from app.schemas.observation import Observation
from app.schemas.root_cause import RootCause
from app.schemas.severity import (
    SeverityAssessment,
    SeverityLevel,
)
from app.schemas.recommendation import (
    Recommendation,
    RecommendationPriority,
)

from app.services.llm.narrative_generator import (
    NarrativeGenerator,
)


def main():

    observation = Observation(
        area="Hall",
        issue="Skirting Dampness",
        description="Dampness observed at skirting level.",
        page_number=1,
        confidence=0.95,
    )

    root_cause = RootCause(
        cause="Concealed plumbing leakage",
        rationale="Persistent moisture patterns observed.",
        evidence_ids=[],
        confidence=0.9,
    )

    severity = SeverityAssessment(
        level=SeverityLevel.HIGH,
        rule_triggered="Dampness + Moisture Evidence",
        supporting_evidence=[],
    )

    recommendation = Recommendation(
        recommendation="Inspect and repair plumbing lines.",
        priority=RecommendationPriority.HIGH,
        linked_issue="Skirting Dampness",
    )

    generator = NarrativeGenerator()

    result = generator.generate_area_narrative(
        observation=observation,
        root_cause=root_cause,
        severity=severity,
        recommendation=recommendation,
    )

    print("\nAREA:")
    print(result.area)

    print("\nNARRATIVE:")
    print(result.narrative)


if __name__ == "__main__":
    main()