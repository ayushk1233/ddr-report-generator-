from app.schemas.ddr_report import DDRReport

from app.services.reports.report_section import (
    ReportSection
)


class ReportFormatter:

    def format(
        self,
        report: DDRReport
    ) -> list[ReportSection]:

        sections: list[
            ReportSection
        ] = []

        for index, bundle in enumerate(
            report.evidence_bundles
        ):

            sections.append(
                ReportSection(
                    area=bundle.area,

                    observations=
                    bundle.observations,

                    thermal_findings=
                    bundle.thermal_findings,

                    root_cause=
                    report.root_causes[index],

                    severity=
                    report.severity_assessments[
                        index
                    ],

                    recommendation=
                    report.recommendations[
                        index
                    ],

                    evidence_refs=
                    bundle.evidence_refs,

                    narrative=
                    report.area_narratives[index]
                )
            )

        return sections