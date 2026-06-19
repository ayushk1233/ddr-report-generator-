from app.services.reports.report_formatter import ReportFormatter
from app.tests.sample_report import build_sample_report

def test_report_formatter_formats_sections():
    report = build_sample_report()

    formatter = ReportFormatter()
    sections = formatter.format(report)

    assert len(sections) == len(report.evidence_bundles)
    assert sections[0].area == "Hall"
