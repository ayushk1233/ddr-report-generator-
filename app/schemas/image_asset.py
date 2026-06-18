from pydantic import BaseModel
from uuid import UUID, uuid4


class ImageAsset(BaseModel):
    image_id: UUID = uuid4()
    source_document: str
    page_number: int
    file_path: str
    image_type: str
    confidence: float