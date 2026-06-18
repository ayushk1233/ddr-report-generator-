from pprint import pprint

from app.services.pipeline.ddr_pipeline import (
    DDRPipeline
)


pipeline = DDRPipeline()

report = pipeline.run(
    inspection_pdf="Sample Report.pdf",
    thermal_pdf="Thermal Images.pdf"
)

print("\n========== SUMMARY ==========\n")

print(
    report.property_issue_summary
)

print("\n========== COUNTS ==========\n")

print(
    "Evidence Bundles:",
    len(report.evidence_bundles)
)

print(
    "Root Causes:",
    len(report.root_causes)
)

print(
    "Severity Assessments:",
    len(report.severity_assessments)
)

print(
    "Recommendations:",
    len(report.recommendations)
)

print(
    "Conflicts:",
    len(report.conflicts)
)

print(
    "Missing Information:",
    len(report.missing_information)
)

print("\n========== METADATA ==========\n")

pprint(
    report.metadata.model_dump()
)

print("\n========== ROOT CAUSES ==========\n")

for item in report.root_causes:

    pprint(
        item.model_dump()
    )

print("\n========== RECOMMENDATIONS ==========\n")

for item in report.recommendations:

    pprint(
        item.model_dump()
    )