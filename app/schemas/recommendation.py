from enum import Enum

from pydantic import BaseModel


class RecommendationPriority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class Recommendation(BaseModel):
    recommendation: str

    priority: RecommendationPriority

    linked_issue: str