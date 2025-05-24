from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def catalog_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Counter Strike 2", callback_data="games_1"),
                InlineKeyboardButton(text="Call of duty", callback_data="games_2"),
                InlineKeyboardButton(text="The forest", callback_data="games_3"),
                InlineKeyboardButton(text="Rust", callback_data="games_4"),
                InlineKeyboardButton(text="Granny", callback_data="games_5"),
                InlineKeyboardButton(text="Fnaf 4", callback_data="games_6"),
                InlineKeyboardButton(text="Garry's mod", callback_data="games_7"),
                InlineKeyboardButton(text="World box", callback_data="games_8"),
                InlineKeyboardButton(text="Vedmyak 3", callback_data="games_9"),
                InlineKeyboardButton(text="Cyberpunk 2077", callback_data="games_10"),
                InlineKeyboardButton(text="Geometry dash", callback_data="games_11"),
                width = 2
    )
    return builder.as_markup()














