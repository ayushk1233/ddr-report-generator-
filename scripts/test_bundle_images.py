from app.services.pipeline.ddr_pipeline import (
    DDRPipeline
)


def main():

    report = (
        DDRPipeline().run(
            inspection_pdf=
            "Sample Report.pdf",

            thermal_pdf=
            "Thermal Images.pdf"
        )
    )

    for bundle in report.evidence_bundles:

        print("\n")
        print(bundle.area)
        print(bundle.inspection_images)


if __name__ == "__main__":
    main()