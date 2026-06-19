from app.services.pipeline.ddr_pipeline import (
    DDRPipeline
)

from app.services.reports.report_formatter import (
    ReportFormatter
)


def main():

    report = DDRPipeline().run(
        inspection_pdf="Sample Report.pdf",
        thermal_pdf="Thermal Images.pdf"
    )

    sections = (
        ReportFormatter()
        .format(report)
    )

    print("\nAREA:")
    print(sections[0].area)

    print("\nNARRATIVE:")
    print(sections[0].narrative)


if __name__ == "__main__":
    main()