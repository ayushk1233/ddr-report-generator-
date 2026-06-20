from app.services.extraction.image_extractor import (
    ImageExtractor
)


def main():

    extractor = ImageExtractor()

    inspection_images = (
        extractor.extract_images(
            pdf_path="Sample Report.pdf",
            output_dir="app/storage/images/inspection"
        )
    )

    thermal_images = (
        extractor.extract_images(
            pdf_path="Thermal Images.pdf",
            output_dir="app/storage/images/thermal"
        )
    )

    print(
        f"Inspection Images: {len(inspection_images)}"
    )

    print(
        f"Thermal Images: {len(thermal_images)}"
    )

    print("\nFirst 5 Images:\n")

    for image in (
        inspection_images[:5]
        +
        thermal_images[:5]
    ):
        print(image)


if __name__ == "__main__":
    main()