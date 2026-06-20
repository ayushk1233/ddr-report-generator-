from pathlib import Path


def main():

    inspection_dir = Path(
        "app/storage/images/inspection"
    )

    thermal_dir = Path(
        "app/storage/images/thermal"
    )

    inspection = list(
        inspection_dir.glob("*")
    )

    thermal = list(
        thermal_dir.glob("*")
    )

    print(
        f"Inspection Images: {len(inspection)}"
    )

    print(
        f"Thermal Images: {len(thermal)}"
    )

    print("\nInspection Samples:\n")

    for image in inspection[:20]:
        print(image.name)

    print("\nThermal Samples:\n")

    for image in thermal[:20]:
        print(image.name)


if __name__ == "__main__":
    main()