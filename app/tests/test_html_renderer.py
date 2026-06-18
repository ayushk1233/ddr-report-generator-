from app.schemas.ddr_report import DDRReport
from app.schemas.metadata import ProcessingMetadata

from app.services.reports.html_renderer import (
    HTMLRenderer
)


def test_renderer_returns_html():

    renderer = HTMLRenderer()

    report = DDRReport(
        property_issue_summary=
        "Test Summary",

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

    html = renderer.render(
        report
    )

    assert "Test Summary" in html