
from json import load
from PIL import Image
from modules.func_tools import if_line_mode_is_not_rgba_than_convert_to_rgba


TEAMS_COLOR_VARIATIONS = [
    "red",
    "yellow",
    "green",
    "blue",
    "noowner",
]
icons_titles:dict={}
with open("config/icons/icons.json", "r", encoding="utf-8") as f:
    icons_titles = load(f)

class TeamColorNotAllowedError(Exception):...


class Icon():
    def __init__(self, title, team_color: str, current_team_color: str, image) -> None:
        self.image = image
        self.title = title

    def __get_image(self, team_color: str, current_team_color: str, return_res=False) -> Image:
        if team_color not in TEAMS_COLOR_VARIATIONS:
            raise TeamColorNotAllowedError

        # Open images
        background = Image.open(f"textures/points/{team_color}_point.png")
        overlay = Image.open(f"textures/icons/{self.__class__.__name__.lower()}.png")
        background = if_line_mode_is_not_rgba_than_convert_to_rgba(background)
        overlay = if_line_mode_is_not_rgba_than_convert_to_rgba(overlay)

        # We calculate the coordinates to place the image in the center
        _x = (background.width - overlay.width) // 2
        _y = (background.height - overlay.height) // 2

        # Наносим прозрачное изображение на заднем плане
        if current_team_color == team_color:
            circle = Image.open("textures/points/circle.png")
            background.paste(circle, (0, 0), circle)
        background.paste(overlay, (_x, _y), overlay)
        self.image = background
        if return_res:
            return background


class Angry(Icon):
    def __init__(self, current_command, owner_of_event):
        self.image = super()._Icon__get_image(current_command, owner_of_event, True)
        super().__init__(icons_titles[self.__class__.__name__.lower()], current_command, owner_of_event, self.image)


class Alarm(Icon):
    def __init__(self, current_command, owner_of_event):
        self.image = super()._Icon__get_image(current_command, owner_of_event, True)
        super().__init__(icons_titles[self.__class__.__name__.lower()], current_command, owner_of_event, self.image)


class Fight(Icon):
    def __init__(self, current_command, owner_of_event):
        self.image = super()._Icon__get_image(current_command, owner_of_event, True)
        super().__init__(icons_titles[self.__class__.__name__.lower()], current_command, owner_of_event, self.image)


class Bow_Fight(Icon):
    def __init__(self, current_command, owner_of_event):
        self.image = super()._Icon__get_image(current_command, owner_of_event, True)
        super().__init__(icons_titles[self.__class__.__name__.lower()], current_command, owner_of_event, self.image)


class No_Provisions(Icon):
    def __init__(self, current_command, owner_of_event):
        self.image = super()._Icon__get_image(current_command, owner_of_event, True)
        super().__init__(icons_titles[self.__class__.__name__.lower()], current_command, owner_of_event, self.image)


class Point_Captured(Icon):
    def __init__(self, current_command, owner_of_event):
        self.image = super()._Icon__get_image(current_command, owner_of_event, True)
        super().__init__(icons_titles[self.__class__.__name__.lower()], current_command, owner_of_event, self.image)


class Breakthrough(Icon):
    def __init__(self, current_command, owner_of_event):
        self.image = super()._Icon__get_image(current_command, owner_of_event, True)
        super().__init__(icons_titles[self.__class__.__name__.lower()], current_command, owner_of_event, self.image)


class Captive(Icon):
    def __init__(self, current_command, owner_of_event):
        self.image = super()._Icon__get_image(current_command, owner_of_event, True)
        super().__init__(icons_titles[self.__class__.__name__.lower()], current_command, owner_of_event, self.image)


class Defense_Point(Icon):
    def __init__(self, current_command, owner_of_event):
        self.image = super()._Icon__get_image(current_command, owner_of_event, True)
        super().__init__(icons_titles[self.__class__.__name__.lower()], current_command, owner_of_event, self.image)


class Ender_Pearl_Alarm(Icon):
    def __init__(self, current_command, owner_of_event):
        self.image = super()._Icon__get_image(current_command, owner_of_event, True)
        super().__init__(icons_titles[self.__class__.__name__.lower()], current_command, owner_of_event, self.image)


class Fireball_Damage(Icon):
    def __init__(self, current_command, owner_of_event):
        self.image = super()._Icon__get_image(current_command, owner_of_event, True)
        super().__init__(icons_titles[self.__class__.__name__.lower()], current_command, owner_of_event, self.image)


class Freedom(Icon):
    def __init__(self, current_command, owner_of_event):
        self.image = super()._Icon__get_image(current_command, owner_of_event, True)
        super().__init__(icons_titles[self.__class__.__name__.lower()], current_command, owner_of_event, self.image)


class Go_To_Point(Icon):
    def __init__(self, current_command, owner_of_event):
        self.image = super()._Icon__get_image(current_command, owner_of_event, True)
        super().__init__(icons_titles[self.__class__.__name__.lower()], current_command, owner_of_event, self.image)


class Info(Icon):
    def __init__(self, current_command, owner_of_event):
        self.image = super()._Icon__get_image(current_command, owner_of_event, True)
        super().__init__(icons_titles[self.__class__.__name__.lower()], current_command, owner_of_event, self.image)


class Shears(Icon):
    def __init__(self, current_command, owner_of_event):
        self.image = super()._Icon__get_image(current_command, owner_of_event, True)
        super().__init__(icons_titles[self.__class__.__name__.lower()], current_command, owner_of_event, self.image)



