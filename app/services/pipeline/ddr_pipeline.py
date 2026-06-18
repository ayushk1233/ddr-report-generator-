from time import perf_counter

from app.schemas.metadata import (
    ProcessingMetadata
)

from app.services.pdf.pdf_service import (
    PDFService
)

from app.services.extraction.observation_extractor import (
    ObservationExtractor
)

from app.services.extraction.thermal_extractor import (
    ThermalExtractor
)

from app.services.evidence.evidence_builder import (
    EvidenceBuilder
)

from app.services.reasoning.root_cause_engine import (
    RootCauseEngine
)

from app.services.reasoning.quality_gate import (
    QualityGate
)

from app.services.reasoning.severity_engine import (
    SeverityEngine
)

from app.services.reasoning.recommendation_engine import (
    RecommendationEngine
)

from app.services.reports.ddr_assembler import (
    DDRAssembler
)


class DDRPipeline:

    def __init__(self):

        self.pdf_service = PDFService()

        self.observation_extractor = (
            ObservationExtractor()
        )

        self.thermal_extractor = (
            ThermalExtractor()
        )

        self.evidence_builder = (
            EvidenceBuilder()
        )

        self.root_cause_engine = (
            RootCauseEngine()
        )

        self.quality_gate = (
            QualityGate()
        )

        self.severity_engine = (
            SeverityEngine()
        )

        self.recommendation_engine = (
            RecommendationEngine()
        )

        self.ddr_assembler = (
            DDRAssembler()
        )

    def run(
        self,
        inspection_pdf: str,
        thermal_pdf: str
    ):

        start = perf_counter()

        observations = []

        inspection_pages = (
            self.pdf_service.extract_pages(
                inspection_pdf
            )
        )

        for page in inspection_pages:

            observations.extend(
                self.observation_extractor.extract(
                    page.text,
                    page.page_number
                )
            )

        thermal_findings = []

        thermal_pages = (
            self.pdf_service.extract_pages(
                thermal_pdf
            )
        )

        for page in thermal_pages:

            finding = (
                self.thermal_extractor.extract(
                    text=page.text,
                    page_number=page.page_number
                )
            )

            if finding:

                thermal_findings.append(
                    finding
                )

        bundles = (
            self.evidence_builder.build(
                observations,
                thermal_findings
            )
        )

        root_causes = []

        severities = []

        recommendations = []

        conflicts = []

        missing_information = []

        for bundle in bundles:

            root_cause = (
                self.root_cause_engine.generate(
                    bundle
                )
            )

            severity = (
                self.severity_engine.assess(
                    bundle
                )
            )

            recommendation = (
                self.recommendation_engine.generate(
                    issue=
                    bundle.observations[0].issue,

                    root_cause=
                    root_cause,

                    severity=
                    severity
                )
            )

            root_causes.append(
                root_cause
            )

            severities.append(
                severity
            )

            recommendations.append(
                recommendation
            )

            conflicts.extend(
                self.quality_gate.detect_conflicts(
                    bundle
                )
            )

            missing_information.extend(
                self.quality_gate
                .detect_missing_information(
                    bundle
                )
            )

        metadata = (
            ProcessingMetadata(
                extraction_time_seconds=
                perf_counter() - start,

                model_version=
                "v1",

                confidence=0.80,

                failures=[]
            )
        )

        return self.ddr_assembler.assemble(
            summary=
            "Automated DDR generated.",

            bundles=bundles,

            root_causes=
            root_causes,

            severities=
            severities,

            recommendations=
            recommendations,

            conflicts=
            conflicts,

            missing_information=
            missing_information,

            metadata=
            metadata
        )