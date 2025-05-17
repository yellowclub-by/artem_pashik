from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_button = KeyboardButton(text="Назад")

main_kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Купить"), KeyboardButton(text="Каталог")],
    ],
    resize_keyboard=True,
    input_field_placeholder="lox pedalnyi"
)
buy_kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Shooter"), KeyboardButton(text="Survival")],
        [KeyboardButton(text="Horror"), KeyboardButton(text="Sandbox")],
        [KeyboardButton(text="RPG"), KeyboardButton(text="Tower Defense")],
        [KeyboardButton(text="Simulator"), KeyboardButton(text="Adventure")],
        [KeyboardButton(text="Platformer"), KeyboardButton(text="Puzzle")],
        [back_button]
    ],
    resize_keyboard=True,
    input_field_placeholder="lox pedalnyi"
)
shooter_kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Counter strike 2"), KeyboardButton(text="Call of duty")],
        [back_button]
    ],
        resize_keyboards=True
)
survival_kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="The Forest"), KeyboardButton(text="Rust")],
        [back_button]
    ],
        resize_keyboards=True
)
horror_kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Granny"), KeyboardButton(text="Fnaf 4")],
        [back_button]
    ],
        resize_keyboards=True
)
sandbox_kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Garry's mod"), KeyboardButton(text="World Box")],
        [back_button]
    ],
        resize_keyboards=True
)
rpg_kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="The Vedmyak 3"), KeyboardButton(text="Cyberpunk 2077")],
        [back_button]
    ],
        resize_keyboards=True
)
tower_defence_kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Bloons TD 6"), KeyboardButton(text="Forts")],
        [back_button]
    ],
        resize_keyboards=True
)
survival_kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="The Forest"), KeyboardButton(text="Rust")],
        [back_button]
    ],
        resize_keyboards=True
)
survival_kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="The Forest"), KeyboardButton(text="Rust")],
        [back_button]
    ],
        resize_keyboards=True
)
survival_kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="The Forest"), KeyboardButton(text="Rust")],
        [back_button]
    ],
        resize_keyboards=True
)
survival_kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="The Forest"), KeyboardButton(text="Rust")],
        [back_button]
    ],
        resize_keyboards=True
)
