from pathlib import Path

from jinja2 import Environment
from jinja2 import FileSystemLoader

from app.schemas.ddr_report import DDRReport
from app.services.reports.report_formatter import (
    ReportFormatter
)


class HTMLRenderer:

    def __init__(self) -> None:

        template_directory = (
            Path(__file__)
            .parent.parent.parent
            / "templates"
        )

        environment = Environment(
            loader=FileSystemLoader(
                template_directory
            )
        )

        self.template = (
            environment.get_template(
                "report_template_v3.html"
            )
        )

    def render(
        self,
        report: DDRReport
    ) -> str:

        sections = (
            ReportFormatter()
            .format(report)
        )

        return self.template.render(
            report=report,
            sections=sections
        )