from pathlib import Path

import fitz


class ThermalPageRenderer:

    def render_pages(
        self,
        pdf_path: str,
        output_dir: str
    ) -> list[str]:

        output_path = Path(output_dir)

        output_path.mkdir(
            parents=True,
            exist_ok=True
        )

        rendered_pages = []

        document = fitz.open(pdf_path)

        for page_index in range(
            len(document)
        ):

            page = document[page_index]

            pixmap = page.get_pixmap(
                matrix=fitz.Matrix(
                    2,
                    2
                )
            )

            output_file = (
                output_path
                /
                f"thermal_page_"
                f"{page_index + 1}.png"
            )

            pixmap.save(
                output_file
            )

            rendered_pages.append(
                str(output_file)
            )

        document.close()

        return rendered_pages
        