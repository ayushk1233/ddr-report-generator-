from pathlib import Path

from app.services.reports.pdf_exporter import (
    PDFExporter
)


def test_pdf_exporter_creates_file():

    exporter = PDFExporter()

    output_file = (
        Path("app/outputs")
        / "test_export.pdf"
    )

    exporter.export(
        "<h1>Hello</h1>",
        str(output_file)
    )

    assert output_file.exists()

    output_file.unlink()