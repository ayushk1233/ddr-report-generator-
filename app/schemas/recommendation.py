from pydantic import BaseModel


class Recommendation(BaseModel):
    recommendation: str

    priority: str

    linked_issue: str