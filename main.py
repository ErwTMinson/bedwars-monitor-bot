from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from PIL import Image


from modules.func_tools import if_line_mode_is_not_rgba_than_convert_to_rgba
from modules.icons import icons_titles, Fight, Bow_Fight, Angry, No_Provisions, Point_Captured, \
    Fireball_Damage, Alarm
import modules.points
from modules.map import Map


# our_command = "ыы"
# icons = {
#     "Тревога": "alarm.png",
#     "Бой с использованием луков": "bow_fight.png",
#     "Пёрловая тревога": "ender_pearl_alarm.png",
#     "Идёт бой": "fight.png",
#     "Нанесен фаербольный удар": "fireball_damage.png",
#     "Сбор игроков к точке": "go_to_point.png",
#     "Точка захвачена": "point_captured.png",
#     "Команда отрезана от снабжения": "shears.png",
#     "Команда заключила мир": "freedom.png",
#     "Команда накаляет обстановку": "angry.png",
#     "Информация": "info.png",
#     "Тим остался на вражеской территории": "captive.png",
#     "Приказ защищать точку": "defense_point.png",
#     "Прорыв": "breakthrough.png",
# }

# points_on_map = {
#     "Точка О1": {"island_name": "blue_base_o", "news": [{"news": "fight", "made": "yellow"}]},
#     "Точка К": {"island_name": "red_base", "news": []},
#     "Точка О2": {"island_name": "blue_base_o", "news": []},
#     "Точка Ж": {"island_name": "yellow_base", "news": []},
#     "Точка Ц": {"island_name": "red_center", "news": []},
#     "Точка С": {"island_name": "blue_base", "news": []},
#     "Точка О3": {"island_name": "blue_base_o", "news": []},
#     "Точка З": {"island_name": "green_base", "news": []},
#     "Точка О4": {"island_name": "blue_base_o", "news": []},
# }

# def add(point):
# 	if len(points_on_map[point]) >= 3:
# 		del points_on_map[point][0]
# 	points_on_map[point] =




# for (key, value) in icons.items():
#     # Открываем изображения
#     background = Image.open("textures/points/green_point.png")
#     overlay = Image.open(f"textures/icons/{value}")

#     # Рассчитываем координаты для размещения изображения по центру
#     x = (background.width - overlay.width) // 2
#     y = (background.height - overlay.height) // 2

#     # Наносим прозрачное изображение на заднем плане
#     print(background.filename)
#     if our_command in background.filename:
#         circle = Image.open("textures/points/circle.png")
#         background.paste(circle, (0, 0), circle)
#     background.paste(overlay, (x, y), overlay)

#     # Сохраняем результат
#     background.save(f"icons/{value}.png")

bot = Bot(token='5946938437:AAFTnAFxCMxbOjZ7PNZcLRs6WKpflYiDGnQ')
dp = Dispatcher(bot)


events_keyboard = []
print(icons_titles)
for (key, value) in icons_titles.items():
    print(value["title"])
    events_keyboard.append(KeyboardButton(value["title"]))


class ChooseAction(StatesGroup):
    action = State()
    point = State()
    event = State()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message, state: FSMContext):
    m = Map("temple")

    # Создаем кнопки
    self_event = KeyboardButton('Свое действие')
    event_of_other_team = KeyboardButton('Чужое действие')

    # Создаем клавиатуру и добавляем кнопки
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).row(self_event, event_of_other_team)

    a = m.map["2"]["center"]
    a.owner = "yellow"
    a.append_icon(Point_Captured("green", "green"))
    a.append_icon(Point_Captured("yellow", "green"))
    a.append_icon(Bow_Fight("yellow", "green"))

    a = m.map["1"]["base_red"]
    a.append_icon(Fight("red", "green"))
    a.append_icon(Point_Captured("yellow", "green"))
    a.owner = "yellow"

    a = m.map["2"]["base_yellow"]
    a.append_icon(Fireball_Damage("green", "green"))

    a = m.map["2"]["base_blue"]
    a.owner = "yellow"
    a.append_icon(Point_Captured("green", "green"))
    a.append_icon(Point_Captured("yellow", "green"))

    a = m.map["3"]["base_green"]
    a.append_icon(Fireball_Damage("yellow", "green"))
    a.append_icon(Alarm("green", "green"))
    a.append_icon(Fight("yellow", "green"))
    a.append_icon(Alarm("green", "green"))
    a.append_icon(Fight("yellow", "green"))

    a = m.map["3"]["base_o"]
    a.append_icon(Point_Captured("yellow", "green"))
    a.owner = "yellow"

    a = m.map["1"]["base_o"]
    a.owner = "yellow"


    m.update()
    with open('map1.png', 'rb') as photo:
        await message.reply_photo(photo=photo, reply_markup=keyboard)



@dp.message_handler(text=["Свое действие", "Чужое действие"])
async def handle_action(message: Message, state: FSMContext):

    point_o1 = KeyboardButton('Точка О')
    point_r = KeyboardButton('🟥Точка К')
    point_o2 = KeyboardButton('Точка О')

    point_y = KeyboardButton('🟨Точка Ж')
    point_c = KeyboardButton('Точка Ц')
    point_b = KeyboardButton('🟦Точка С')

    point_o3 = KeyboardButton('Точка О')
    point_thet = KeyboardButton('🟩Точка З')
    point_o4 = KeyboardButton('Точка О')

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).row(point_o1, point_r, point_o2).row(point_y, point_c, point_b).row(point_o3, point_thet, point_o4)

    await message.reply('Выберете точку', reply_markup=keyboard)

@dp.message_handler(text=["Точка О", "🟥Точка К", "🟨Точка Ж", "Точка Ц", "🟦Точка С", "🟩Точка З"])
async def handle_point(message: Message, state: FSMContext):
    reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)

    row = []
    for button in events_keyboard:
        button.text = button.text.replace("[$choosed_comand_name]", "red")
        button.text = button.text.replace("$[current_command]", "green")
        button.text = button.text.replace("$[tg_user_name]", message.from_user.first_name)

        print(button.text)
        row.append(button)
        if len(row) == 2:
            reply_markup.row(*row)
            row = []

    # Add any remaining buttons to the last row
    if row:
        reply_markup.row(*row)
    await message.reply('Действите выбрано.\nТеперь нужно выбрать комманду которая создала событие:', reply_markup=reply_markup)


@dp.message_handler(text=list(events_keyboard.keys()))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
