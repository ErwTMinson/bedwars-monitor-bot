import typing
from json import load

from PIL import Image
from modules.points import Base, Base_o, Center, Island

from modules.icons import TEAMS_COLOR_VARIATIONS


def get_island(island_index: str) -> Island:
    if not isinstance(island_index, str):
        raise ValueError()

    if island_index.startswith("base"):
        if island_index == "base_o":
            return Base_o(1, 1)
        elif island_index.replace("base_", "") in TEAMS_COLOR_VARIATIONS:
            return Base(1, 1, island_index.replace("base_", ""))
    elif island_index == "center":
        return Center(1, 1)


class Map():
    def __init__(self, name: str) -> None:
        with open(f"config/maps/{name}.json", "r") as f:
            map_json: typing.List[typing.Dict[str, typing.List[str]]] = load(f)

        self.map: typing.Dict[str, Island] = {}
        for i in map_json:
            for (key, value) in i.items():
                for j in value:

                    if key not in self.map:
                        self.map[key] = {}

                    if len(self.map[key]) == 0:
                        self.map[key] = {}
                    self.map[key][j] = get_island(j)

    def update(self) -> Image:
        sky = Image.open("textures/map/map.png")
        content = Image.new('RGBA', (640, 624), (0, 0, 0, 0))
        if sky.mode != "RGBA":
            sky = sky.convert("RGBA")

        xx=0
        yy=0
        x = (sky.width - content.width) // 2
        y = (sky.height - content.height) // 2

        # Update all islands images
        for (_, value) in self.map.items():
            for (_, i) in value.items():
                if i is not None:
                    i.get_image()
                    i._x = xx*256
                    i._y = yy*256
                    content.paste(i.image, (i._x, i._y), mask=i.image)

                    if len(i.events) > 0:
                        padding = 0
                        icons = Image.new('RGBA', (len(i.events)*80, 64), (0, 0, 0, 0))
                        for _e in i.events:
                            icons.paste(
                                _e.image,
                                (padding*80, 0),
                                mask=_e.image
                            )
                            padding+=1

                        icons_bar_x = (i.image.width - icons.width) // 2 + 10 + i._x + x
                        icons_bar_y = (i.image.height - icons.height) // 2 - 80  + i._y + y

                        sky.paste(icons, (icons_bar_x, icons_bar_y), mask=icons)
                xx+=1

            yy+=1
            xx=0

        sky.paste(content, (x, y), mask=content)
        sky.save("map1.png")
