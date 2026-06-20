from pathlib import Path

from PIL import Image


class ImageFilter:

    def filter_images(
        self,
        image_paths: list[str],
        min_dimension: int = 300
    ) -> list[str]:

        valid_images = []

        for image_path in image_paths:

            try:

                image = Image.open(
                    image_path
                )

                width, height = (
                    image.size
                )

                if (
                    width >= min_dimension
                    and
                    height >= min_dimension
                ):
                    valid_images.append(
                        image_path
                    )

            except Exception:
                continue

        return valid_images