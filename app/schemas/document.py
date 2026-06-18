from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from uuid import UUID, uuid4

class DocumentType(str, Enum):
    INSPECTION = "INSPECTION"
    THERMAL = "THERMAL"

class Document(BaseModel):
    id: UUID = uuid4()
    type: DocumentType
    filename: str
    pages: int
    processed_at: datetime | None = None