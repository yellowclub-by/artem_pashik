from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def main_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Купить", callback_data="buy"),
                InlineKeyboardButton(text="Каталог", callback_data="catalog"),
        width=2
    )
    return builder.as_markup()

def catalog_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Counter Strike 2", callback_data="games_1"),
                InlineKeyboardButton(text="Call of duty", callback_data="games_2"),
                InlineKeyboardButton(text="The forest", callback_data="games_4"),
                InlineKeyboardButton(text="Rust", callback_data="games_3"),
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

# links_kb = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="?", url="https://ru.wikipedia.org/wiki/Counter-Strike_2")],
#         [InlineKeyboardButton(text="Мой профиль", url="tg://resolve?domain=FNFrozeN2700")],
#     ]
# )


def buy_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Shooter", callback_data="genre_1"),
                InlineKeyboardButton(text="Survival", callback_data="genre_2"),
                InlineKeyboardButton(text="Horror", callback_data="genre_3"),
                InlineKeyboardButton(text="Sandbox", callback_data="genre_4"),
                InlineKeyboardButton(text="RPG", callback_data="genre_5"),
                InlineKeyboardButton(text="Platformer", callback_data="genre_6"),
                width = 1
    )
    return builder.as_markup()

def shooter_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Counter Strike 2", callback_data="gengam_1"),
                InlineKeyboardButton(text="Call of duty", callback_data="gengam_2"),
                width = 1
    )
    return builder.as_markup()

def survival_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Counter Strike 2", callback_data="gengam_1"),
                InlineKeyboardButton(text="Call of duty", callback_data="gengam_2"),
                width = 1
    )
    return builder.as_markup()

def horror_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Counter Strike 2", callback_data="gengam_1"),
                InlineKeyboardButton(text="Call of duty", callback_data="gengam_2"),
                width = 1
    )
    return builder.as_markup()

def sandbox_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Counter Strike 2", callback_data="gengam_1"),
                InlineKeyboardButton(text="Call of duty", callback_data="gengam_2"),
                width = 1
    )
    return builder.as_markup()

def rpg_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Counter Strike 2", callback_data="gengam_1"),
                InlineKeyboardButton(text="Call of duty", callback_data="gengam_2"),
                width = 1
    )
    return builder.as_markup()

def platformer_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Counter Strike 2", callback_data="gengam_1"),
                InlineKeyboardButton(text="Call of duty", callback_data="gengam_2"),
                width = 1
    )
    return builder.as_markup()

