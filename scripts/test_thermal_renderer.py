from app.services.extraction.thermal_page_renderer import (
    ThermalPageRenderer
)


def main():

    pages = (
        ThermalPageRenderer()
        .render_pages(
            pdf_path="Thermal Images.pdf",
            output_dir=
            "app/storage/rendered_thermal"
        )
    )

    print(
        f"Rendered: {len(pages)}"
    )

    print(
        pages[:5]
    )


if __name__ == "__main__":
    main()