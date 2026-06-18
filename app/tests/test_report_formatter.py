from app.schemas.ddr_report import DDRReport
from app.schemas.evidence_bundle import EvidenceBundle
from app.schemas.root_cause import RootCause
from app.schemas.severity import SeverityAssessment, SeverityLevel
from app.schemas.recommendation import Recommendation, RecommendationPriority
from app.schemas.metadata import ProcessingMetadata
from app.services.reports.report_formatter import ReportFormatter

def test_report_formatter_formats_sections():
    report = DDRReport(
        property_issue_summary="Test Summary",
        evidence_bundles=[
            EvidenceBundle(
                area="Hall",
                observations=[],
                inspection_images=[],
                thermal_images=[],
                thermal_findings=[],
                evidence_refs=[]
            )
        ],
        root_causes=[
            RootCause(
                cause="Test Cause",
                rationale="Test",
                evidence_ids=[],
                confidence=1.0
            )
        ],
        severity_assessments=[
            SeverityAssessment(level=SeverityLevel.LOW, rule_triggered="Test", supporting_evidence=[])
        ],
        recommendations=[
            Recommendation(recommendation="Test Rec", priority=RecommendationPriority.LOW, linked_issue="Test")
        ],
        additional_notes=[],
        missing_information=[],
        conflicts=[],
        metadata=ProcessingMetadata(
            extraction_time_seconds=1.0,
            model_version="v1",
            confidence=0.8
        )
    )

    formatter = ReportFormatter()
    sections = formatter.format(report)

    assert len(sections) == len(report.evidence_bundles)
    assert sections[0].area == "Hall"
