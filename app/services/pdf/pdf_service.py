from pathlib import Path

import fitz

from app.schemas.page_content import PageContent


class PDFService:

    def extract_pages(
        self,
        pdf_path: str
    ) -> list[PageContent]:

        document = fitz.open(pdf_path)

        pages: list[PageContent] = []

        for page_index in range(len(document)):

            page = document[page_index]

            text = page.get_text()

            pages.append(
                PageContent(
                    page_number=page_index + 1,
                    text=text,
                    image_paths=[]
                )
            )

        document.close()

        return pages

    def get_page_count(
        self,
        pdf_path: str
    ) -> int:

        document = fitz.open(pdf_path)

        count = len(document)

        document.close()

        return count

    def validate_pdf(
        self,
        pdf_path: str
    ) -> bool:

        path = Path(pdf_path)

        if not path.exists():
            return False

        if path.suffix.lower() != ".pdf":
            return False

        return True