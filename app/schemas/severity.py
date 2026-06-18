from enum import Enum

from pydantic import BaseModel


class SeverityLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class SeverityAssessment(BaseModel):
    level: SeverityLevel

    rule_triggered: str

    supporting_evidence: list[str]