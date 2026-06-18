from datetime import datetime
from pydantic import BaseModel
from uuid import UUID, uuid4


class Document(BaseModel):
    id: UUID = uuid4()
    type: str
    filename: str
    pages: int
    processed_at: datetime | None = None