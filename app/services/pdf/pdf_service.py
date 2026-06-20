from pathlib import Path

import fitz

from app.schemas.page_content import PageContent

from app.services.extraction.image_extractor import (
    ImageExtractor
)


class PDFService:

    def extract_pages(
        self,
        pdf_path: str
    ) -> list[PageContent]:

        document = fitz.open(pdf_path)

        pages: list[PageContent] = []

        image_extractor = ImageExtractor()

        all_images = image_extractor.extract_images(
            pdf_path=pdf_path,
            output_dir="app/storage/images/inspection"
        )

        for page_index in range(len(document)):

            page = document[page_index]

            text = page.get_text()

            page_number = page_index + 1

            page_images = [
                image
                for image in all_images
                if f"page_{page_number}_" in image
            ]

            page_images = [
                image
                for image in page_images
                if image.lower().endswith(".jpeg")
            ]

            page_images.sort()

            inspection_candidates = []

            for image in page_images:

                image_name = image.split("/")[-1]

                try:
                    image_number = int(
                        image_name
                        .split("_image_")[1]
                        .split(".")[0]
                    )

                    # Skip thermal captures that tend
                    # to appear later in the sequence
                    if image_number <= 5:
                        inspection_candidates.append(
                            image
                        )

                except Exception:
                    continue

            page_images = inspection_candidates

            pages.append(
                PageContent(
                    page_number=page_number,
                    text=text,
                    image_paths=page_images
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