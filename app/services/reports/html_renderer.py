from pathlib import Path

from jinja2 import Environment
from jinja2 import FileSystemLoader

from app.schemas.ddr_report import DDRReport


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
                "report_template.html"
            )
        )

    def render(
        self,
        report: DDRReport
    ) -> str:

        return self.template.render(
            report=report
        )