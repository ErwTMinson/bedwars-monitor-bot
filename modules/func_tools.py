from PIL import Image


def if_line_mode_is_not_rgba_than_convert_to_rgba(image: Image) -> Image:
    """
    This function execute method `convert("RGBA")` to argument `image`
    if `image` mode is not "RGBA"

    return: (Image) here image is an argument.
    """
    if image.mode != "RGBA":
        image = image.convert("RGBA")
        return image
    return image
