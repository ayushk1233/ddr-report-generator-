from app.services.pipeline.ddr_pipeline import (
    DDRPipeline
)

from app.services.reports.html_renderer import (
    HTMLRenderer
)

from app.services.reports.pdf_exporter import (
    PDFExporter
)


pipeline = DDRPipeline()

report = pipeline.run(
    inspection_pdf="Sample Report.pdf",
    thermal_pdf="Thermal Images.pdf"
)

html = HTMLRenderer().render(
    report
)

output_file = PDFExporter().export(
    html,
    "app/outputs/real_ddr_report.pdf"
)

print(output_file)