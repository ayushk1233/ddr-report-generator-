from pathlib import Path
from PIL import Image

images = sorted(
    Path(
        "app/storage/images/inspection"
    ).glob("*")
)

for image_path in images[:30]:

    try:

        image = Image.open(image_path)

        print(
            image_path.name,
            image.size
        )

    except Exception:
        pass