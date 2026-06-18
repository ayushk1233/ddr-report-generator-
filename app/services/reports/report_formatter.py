from app.schemas.area_report_section import (
    AreaReportSection
)

from app.schemas.ddr_report import (
    DDRReport
)


class ReportFormatter:

    def format(
        self,
        report: DDRReport
    ) -> list[AreaReportSection]:

        sections = []

        for index, bundle in enumerate(
            report.evidence_bundles
        ):

            sections.append(
                AreaReportSection(
                    area=bundle.area,

                    observations=
                    bundle.observations,

                    thermal_findings=
                    bundle.thermal_findings,

                    root_cause=
                    report.root_causes[index],

                    severity=
                    report.severity_assessments[index],

                    recommendation=
                    report.recommendations[index],

                    evidence_refs=
                    bundle.evidence_refs
                )
            )

        return sections
