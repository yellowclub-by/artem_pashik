import asyncio
from aiogram.filters import CommandStart, Command
from aiogram import types, Router, F
from aiogram.types import FSInputFile
from random import randint
key = randint(10000000, 100000000)

from Keyboards import reply, InLine

user_router = Router()

@user_router.message(CommandStart())
async def start_cmd(message):
    await message.answer("Бот для покупки игр. Команды купить, /buy - купить по жанру игры, каталог, /сatalog - выбрать из всего каталога", reply_markup=InLine.main_kb())

# @user_router.message(F.text.lower() == "каталог")
# @user_router.message(Command("catalog"))
@user_router.callback_query(F.data.startswith("catalog"))
async def catalog(callback:types.CallbackQuery):
    await callback.message.answer("Выберите игру из всех доступных", reply_markup=InLine.catalog_kb())

@user_router.callback_query(F.data.startswith("games"))
async def games_info(callback:types.CallbackQuery):
    query = callback.data.split("_")[1]
    if query == "1":
        photo = FSInputFile(r"images\catalog\cs2prev.jpeg")
        await callback.message.answer_photo(photo, caption="пж зарегай 2")
        await callback.message.answer(f"Отлично! Ваш выбор Counter Strike 2. Ключ от игры - {key}")
    elif query == "2":
        photo = FSInputFile(r"images\catalog\codprev.jpeg")
        await callback.message.answer_photo(photo, caption="калда")
        await callback.message.answer(f"Отлично! Ваш выбор Call of duty. Ключ от игры - {key}")
    elif query == "3":
        photo = FSInputFile(r"images\catalog\rustprev.jpeg")
        await callback.message.answer_photo(photo, caption="ржавчина")
        await callback.message.answer(f"Отлично! Ваш выбор Rust. Ключ от игры - {key}")
    elif query == "4":
        photo = FSInputFile(r"images\catalog\tfprev.jpeg")
        await callback.message.answer_photo(photo, caption="Ааааа монстри")
        await callback.message.answer(f"Отлично! Ваш выбор The forest. Ключ от игры - {key}")
    elif query == "5":
        photo = FSInputFile(r"images\catalog\grannyprev.jpeg")
        await callback.message.answer_photo(photo, caption="бабка")
        await callback.message.answer(f"Отлично! Ваш выбор Granny. Ключ от игры - {key}")
    elif query == "6":
        photo = FSInputFile(r"images\catalog\fnafprev.jpeg")
        await callback.message.answer_photo(photo, caption="мишка фнуфнер")
        await callback.message.answer(f"Отлично! Ваш выбор Fnaf 4. Ключ от игры - {key}")
    elif query == "7":
        photo = FSInputFile(r"images\catalog\gmodprev.jpeg")
        await callback.message.answer_photo(photo, caption="летающий унитаз")
        await callback.message.answer(f"Отлично! Ваш выбор Garry's mod. Ключ от игры - {key}")
    elif query == "8":
        photo = FSInputFile(r"images\catalog\wboxprev.jpeg")
        await callback.message.answer_photo(photo, caption="дадада")
        await callback.message.answer(f"Отлично! Ваш выбор World box. Ключ от игры - {key}")
    elif query == "9":
        photo = FSInputFile(r"images\catalog\v3prev.jpeg")
        await callback.message.answer_photo(photo, caption="?")
        await callback.message.answer(f"Отлично! Ваш выбор Vedmyak 3. Ключ от игры - {key}")
    elif query == "10":
        photo = FSInputFile(r"images\catalog\cyber2077prev.jpeg")
        await callback.message.answer_photo(photo, caption="комп не потянет скипай")
        await callback.message.answer(f"Отлично! Ваш выбор Cyberpunk 2077. Ключ от игры - {key}")
    elif query == "11":
        photo = FSInputFile(r"images\catalog\gdprev.jpeg")
        await callback.message.answer_photo(photo, caption="Крейзи тайм ыыы")
        await callback.message.answer(f"Отлично! Ваш выбор Geometry Dash. Ключ от игры - {key}")
    await callback.answer("Скинь на додеп")

# @user_router.message(F.text.lower() == "купить")
# @user_router.message(Command("buy"))
@user_router.callback_query(F.data.startswith("buy"))
async def genre(callback:types.CallbackQuery):
    await callback.message.answer("Выберите жанр игры", reply_markup=InLine.buy_kb())

@user_router.callback_query(F.data.startswith("genre"))
async def genre_info(callback: types.CallbackQuery):
    query = callback.data.split("_")[1]
    text="Шутеры"
    textt = "Выживания"
    texttt = "Хорроры"
    textttt = "Песочницы"
    texttttt = "РПГ"
    textttttt = "Платформеры"
    if query == "1":
        await callback.message.answer(text, caption="Шутеры")
        await callback.message.answer("Выберите из всех шутеров", reply_markup=InLine.shooter_kb())
    elif query == "2":
        await callback.message.answer(textt, caption="Выживания")
        await callback.message.answer("Выберите из всех выживаний", reply_markup=InLine.survival_kb())
    elif query == "3":
        await callback.message.answer(texttt, caption="Хорроры")
        await callback.message.answer("Выберите из всех хорроров", reply_markup=InLine.horror_kb())
    elif query == "4":
        await callback.message.answer(textttt, caption="Песочницы")
        await callback.message.answer("Выберите из всех песочниц", reply_markup=InLine.sandbox_kb())
    elif query == "5":
        await callback.message.answer(texttttt, caption="РПГ")
        await callback.message.answer("Выберите из всех рпг", reply_markup=InLine.rpg_kb())
    elif query == "6":
        await callback.message.answer(textttttt, caption="Платформеры")
        await callback.message.answer("Выберите из всех платформеров", reply_markup=InLine.platformer_kb())
#@user_router.message(F.text.lower() == "survival")
#@user_router.message(Command("survival"))
#async def Survival(message: types.Message):
 #   await message.answer("Выберите игру из списка возможных шутеров:", reply_markup=reply.survival_kb)

#@user_router.message(F.text.lower() == "horror")
#@user_router.message(Command("horror"))
#async def Horror(message: types.Message):
  #  await message.answer("Выберите игру из списка возможных хорроров:", reply_markup=reply.horror_kb)

#@user_router.message(F.text.lower() == "sandbox")
#@user_router.message(Command("sandbox"))
#async def Sandbox(message: types.Message):
  #  await message.answer("Выберите игру из списка возможных песочниц:", reply_markup=reply.sandbox_kb)

#@user_router.message(F.text.lower() == "rpg")
#@user_router.message(Command("rpg"))
#async def RPG(message: types.Message):
   # await message.answer("Выберите игру из списка возможных рпг:", reply_markup=reply.rpg_kb)

#@user_router.message(F.text.lower() == "platformer")
#@user_router.message(Command("platformer"))
#async def Platformer(message: types.Message):
   # await message.answer("Выберите игру из списка возможных платформеров:", reply_markup=reply.platformer_kb)

#@user_router.message(F.text.lower() == "назад")
#@user_router.message(Command("назад"))
#async def back(message: types.Message):
 #   await message.answer("Главное меню",reply_markup=reply.main_kb)

#@user_router.message(F.text.lower() == "rr")
#@user_router.message(F.text)
#@user_router.message(F.photo)
#@user_router.message(F.text.lower().contains("да"))
#@user_router.message(F.text.lower().startswith("ку"))
#@user_router.message(F.text.lower().endswith("бб"))
# @user_router.message(F.text.lower().startswith("ку"), F.text.lower().endswith("бб"))
#@user_router.message(F.text.lower().startswith("ку") | F.text.lower().startswith("ук"))
#async def echo(message: types.Message):
    # await message.answer("Lox")
    #user_text = message.text
    #await message.answer(user_text)
