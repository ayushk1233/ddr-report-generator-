from app.schemas.evidence_bundle import (
    EvidenceBundle
)

from app.schemas.root_cause import (
    RootCause
)


class RootCauseEngine:

    ROOT_CAUSE_MAP = {
        "Skirting Dampness":
            "Moisture ingress from adjacent wall or floor",

        "Seepage":
            "Water penetration through structure",

        "Wall Crack":
            "Structural settlement or material shrinkage",

        "Tile Hollowness":
            "Poor tile adhesion or substrate failure"
    }

    def generate(
        self,
        bundle: EvidenceBundle
    ) -> RootCause:

        issue = (
            bundle.observations[0].issue
        )

        cause = (
            self.ROOT_CAUSE_MAP.get(
                issue,
                "Further investigation required"
            )
        )

        rationale = (
            f"Observation '{issue}' "
            f"detected in {bundle.area}"
        )

        return RootCause(
            cause=cause,
            rationale=rationale,
            evidence_ids=[],
            confidence=0.80
        )