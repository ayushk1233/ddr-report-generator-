import os
import platform

if platform.system() == "Darwin" and platform.machine() == "arm64":
    os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = "/opt/homebrew/lib:" + os.environ.get("DYLD_FALLBACK_LIBRARY_PATH", "")

from pathlib import Path

from weasyprint import HTML


class PDFExporter:

    def export(
        self,
        html_content: str,
        output_path: str
    ) -> str:

        output_file = Path(
            output_path
        )

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        HTML(
            string=html_content
        ).write_pdf(
            output_file
        )

        return str(
            output_file
        )