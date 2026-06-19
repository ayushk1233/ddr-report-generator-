from pydantic import BaseModel


class Narrative(BaseModel):
    area: str
    content: str