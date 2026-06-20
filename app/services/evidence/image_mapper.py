class ImageMapper:

    def map_images(
        self,
        observation,
        page_images
    ) -> list[str]:

        if not page_images:
            return []

        area = observation.area.lower()
        selected = []

        if area == "hall":
            selected = page_images[0:2]

        elif area == "bedroom":
            selected = page_images[2:4]

        elif area == "kitchen":
            selected = page_images[4:6]

        elif area == "master bedroom":
            selected = page_images[0:2]

        elif area == "parking":
            selected = page_images[0:2]

        elif area == "external wall":
            selected = page_images[2:4]

        else:
            selected = page_images[:2]

        if not selected:
            selected = page_images[-2:]

        return selected
