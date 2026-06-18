from app.schemas.ddr_report import (
    DDRReport
)

from app.schemas.metadata import (
    ProcessingMetadata
)

from app.services.reports.html_renderer import (
    HTMLRenderer
)

from app.services.reports.pdf_exporter import (
    PDFExporter
)


report = DDRReport(
    property_issue_summary=
    "Sample DDR Report",

    evidence_bundles=[],

    root_causes=[],

    severity_assessments=[],

    recommendations=[],

    additional_notes=[],

    missing_information=[],

    conflicts=[],

    metadata=
    ProcessingMetadata(
        extraction_time_seconds=1.0,
        model_version="v1",
        confidence=1.0
    )
)

html = HTMLRenderer().render(
    report
)

pdf_file = PDFExporter().export(
    html,
    "app/outputs/sample_ddr.pdf"
)

print(pdf_file)