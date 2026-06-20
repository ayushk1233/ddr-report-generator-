from pathlib import Path
from PIL import Image


def inspect(folder):

    images = list(Path(folder).glob("*"))

    print(f"\n{folder}\n")

    for image_path in images[:20]:

        try:

            image = Image.open(image_path)

            print(
                image_path.name,
                image.size
            )

        except Exception:
            pass


inspect(
    "app/storage/images/inspection"
)

inspect(
    "app/storage/images/thermal"
)