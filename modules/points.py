from PIL import Image
import typing

from modules.func_tools import if_line_mode_is_not_rgba_than_convert_to_rgba
from modules.icons import Icon


class Island():
    """The Island island is the parent of the child classes """
    def __init__(self, _x: int, _y: int, owner=None) -> None:
        self.image: Image = Image
        self._x = _x
        self._y = _y
        self.owner = "noowner"
        if owner is not None:
            self.owner = owner
        self.events: typing.List[Icon] = []
        self.get_image()

    def get_image(self) -> None:
        """
        `self.image` sets on the Image Obse from the color of the team owner of the island.
        It is worth noting that the name of the class depends on the image of the island.
        """
        line = Image.open(f"textures/map/bases/{self.__class__.__name__.lower()}_line.png")
        overlay = Image.open(
            f"textures/map/bases/{self.owner}_{self.__class__.__name__.lower()}.png"
        )
        line = if_line_mode_is_not_rgba_than_convert_to_rgba(line)
        overlay = if_line_mode_is_not_rgba_than_convert_to_rgba(overlay)

        line.paste(overlay, (0, 0), mask=overlay)
        self.image = line

    def append_icon(self, icon: Icon) -> None:
        if len(self.events) >= 3:
            self.events.pop(0)

        if isinstance(icon, Icon):
            self.events.append(icon)


class Center(Island):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.owner = "noowner"
        super().__init__(x, y)


class Base_o(Island):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.owner = "noowner"
        super().__init__(x, y)


class Base(Island):
    def __init__(self, x: int, y: int, owner) -> None:
        self.x = x
        self.y = y
        self.owner = owner
        super().__init__(x, y, owner)
