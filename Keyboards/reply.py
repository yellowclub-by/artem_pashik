from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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
    ],
    resize_keyboard=True,
    input_field_placeholder="lox pedalnyi"
)
