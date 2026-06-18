from pydantic import BaseModel, Field


class PageContent(BaseModel):
    page_number: int

    text: str

    image_paths: list[str] = Field(default_factory=list)