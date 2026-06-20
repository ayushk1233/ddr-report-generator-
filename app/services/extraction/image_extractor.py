from pathlib import Path
import fitz


class ImageExtractor:

    def extract_images(
        self,
        pdf_path: str,
        output_dir: str
    ) -> list[str]:

        output_path = Path(output_dir)

        output_path.mkdir(
            parents=True,
            exist_ok=True
        )

        extracted_images: list[str] = []

        with fitz.open(pdf_path) as document:

            for page_index in range(len(document)):

                page = document[page_index]

                image_list = page.get_images(
                    full=True
                )

                for image_index, image in enumerate(image_list):

                    xref = image[0]

                    image_data = document.extract_image(
                        xref
                    )

                    image_bytes = image_data["image"]

                    extension = image_data["ext"]

                    image_filename = (
                        f"page_{page_index + 1}"
                        f"_image_{image_index + 1}"
                        f".{extension}"
                    )

                    image_file = (
                        output_path /
                        image_filename
                    )

                    image_file.write_bytes(
                        image_bytes
                    )

                    extracted_images.append(
                        str(image_file)
                    )

        return extracted_images