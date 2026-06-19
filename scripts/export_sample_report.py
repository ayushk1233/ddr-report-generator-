from app.services.pipeline.ddr_pipeline import (
    DDRPipeline
)

pipeline = DDRPipeline()

report = pipeline.run(
    "Sample Report.pdf",
    "Thermal Images.pdf"
)

from app.services.reports.html_renderer import (
    HTMLRenderer
)

from app.services.reports.pdf_exporter import (
    PDFExporter
)

html = HTMLRenderer().render(
    report
)

pdf_file = PDFExporter().export(
    html,
    "app/outputs/sample_ddr.pdf"
)

print(pdf_file)