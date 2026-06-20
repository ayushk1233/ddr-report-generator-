from pathlib import Path

from app.services.extraction.image_filter import (
    ImageFilter
)


def main():

    inspection = [
        str(path)
        for path in Path(
            "app/storage/images/inspection"
        ).glob("*")
    ]

    thermal = [
        str(path)
        for path in Path(
            "app/storage/images/thermal"
        ).glob("*")
    ]

    image_filter = ImageFilter()

    inspection_filtered = (
        image_filter.filter_images(
            inspection
        )
    )

    thermal_filtered = (
        image_filter.filter_images(
            thermal
        )
    )

    print(
        f"Inspection: {len(inspection_filtered)}"
    )

    print(
        f"Thermal: {len(thermal_filtered)}"
    )


if __name__ == "__main__":
    main()