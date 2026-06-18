from app.services.pdf.pdf_service import PDFService
from app.services.extraction.thermal_extractor import (
    ThermalExtractor
)
from app.services.extraction.observation_extractor import (
    ObservationExtractor
)
from app.services.evidence.evidence_builder import (
    EvidenceBuilder
)

pdf = PDFService()

thermal_extractor = ThermalExtractor()

observation_extractor = ObservationExtractor()

builder = EvidenceBuilder()


inspection_pages = pdf.extract_pages(
    "Sample Report.pdf"
)

thermal_pages = pdf.extract_pages(
    "Thermal Images.pdf"
)

print("\nOBSERVATIONS\n")

observations = []

for page in inspection_pages:

    extracted = observation_extractor.extract(
        page.text,
        page.page_number
    )

    observations.extend(extracted)

print(
    "Observation Count:",
    len(observations)
)

print("\nTHERMAL FINDINGS\n")

thermal_findings = []

for page in thermal_pages:

    finding = thermal_extractor.extract(
        text=page.text,
        page_number=page.page_number
    )

    if finding:

        thermal_findings.append(
            finding
        )

print(
    "Thermal Findings:",
    len(thermal_findings)
)

for finding in thermal_findings:

    print(
        finding
    )

bundles = builder.build(
    observations,
    thermal_findings
)

print("\nBUNDLES\n")

for bundle in bundles:

    print(
        bundle.area,
        len(bundle.thermal_findings)
    )