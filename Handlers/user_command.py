import asyncio
from aiogram.filters import CommandStart, Command
from aiogram import types, Router, F
from aiogram.types import FSInputFile

from Keyboards import reply, InLine

user_router = Router()

@user_router.message(CommandStart())
async def start_cmd(message):
    await message.answer("Бот для покупки игр. Команды купить, /buy - купить по жанру игры, каталог, /сatalog - выбрать из всего каталога", reply_markup=reply.main_kb)

@user_router.message(F.text.lower() == "купить")
@user_router.message(Command("buy"))
async def genre(message: types.Message):
    await message.answer("Выберите жанр игры", reply_markup=reply.buy_kb)

@user_router.message(F.text.lower() == "каталог")
@user_router.message(Command("catalog"))
async def catalog(message: types.Message):
    await message.answer("Выберите игру из всех доступных", reply_markup=InLine.catalog_kb())

@user_router.callback_query(F.data.startswith("games"))
async def games_info(callback:types.CallbackQuery):
    query = callback.data.split("_")[1]
    if query == "1":
        photo = FSInputFile(r"images\catalog\cs2prev.jpeg")
        await callback.message.answer_photo(photo, caption="пж зарегай 2")
        await callback.message.answer("Отлично! Ваш выбор Counter Strike 2. Ожидайте ключ от игры в течении 5 минут.")
    elif query == "2":
        photo = FSInputFile(r"images\catalog\codprev.jpeg")
        await callback.message.answer_photo(photo, caption="калда")
        await callback.message.answer("Отлично! Ваш выбор Call of duty. Ожидайте ключ от игры в течении 5 минут.")
    elif query == "3":
        photo = FSInputFile(r"images\catalog\rustprev.jpeg")
        await callback.message.answer_photo(photo, caption="ржавчина")
        await callback.message.answer("Отлично! Ваш выбор Rust. Ожидайте ключ от игры в течении 5 минут.")
    elif query == "4":
        photo = FSInputFile(r"images\catalog\tfprev.jpeg")
        await callback.message.answer_photo(photo, caption="Ааааа монстри")
        await callback.message.answer("Отлично! Ваш выбор The forest. Ожидайте ключ от игры в течении 5 минут.")
    elif query == "5":
        photo = FSInputFile(r"images\catalog\grannyprev.jpeg")
        await callback.message.answer_photo(photo, caption="бабка")
        await callback.message.answer("Отлично! Ваш выбор Granny. Ожидайте ключ от игры в течении 5 минут.")
    elif query == "6":
        photo = FSInputFile(r"images\catalog\fnafprev.jpeg")
        await callback.message.answer_photo(photo, caption="мишка фнуфнер")
        await callback.message.answer("Отлично! Ваш выбор Fnaf 4. Ожидайте ключ от игры в течении 5 минут.")
    elif query == "7":
        photo = FSInputFile(r"images\catalog\gmodprev.jpeg")
        await callback.message.answer_photo(photo, caption="летающий унитаз")
        await callback.message.answer("Отлично! Ваш выбор Garry's mod. Ожидайте ключ от игры в течении 5 минут.")
    elif query == "8":
        photo = FSInputFile(r"images\catalog\wboxprev.jpeg")
        await callback.message.answer_photo(photo, caption="дадада")
        await callback.message.answer("Отлично! Ваш выбор World box. Ожидайте ключ от игры в течении 5 минут.")
    elif query == "9":
        photo = FSInputFile(r"images\catalog\v3prev.jpeg")
        await callback.message.answer_photo(photo, caption="?")
        await callback.message.answer("Отлично! Ваш выбор Vedmyak 3. Ожидайте ключ от игры в течении 5 минут.")
    elif query == "10":
        photo = FSInputFile(r"images\catalog\cyber2077prev.jpeg")
        await callback.message.answer_photo(photo, caption="комп не потянет скипай")
        await callback.message.answer("Отлично! Ваш выбор Cyberpunk 2077. Ожидайте ключ от игры в течении 5 минут.")
    elif query == "11":
        photo = FSInputFile(r"images\catalog\gdprev.jpeg")
        await callback.message.answer_photo(photo, caption="Крейзи тайм ыыы")
        await callback.message.answer("Отлично! Ваш выбор Geometry Dash. Ожидайте ключ от игры в течении 5 минут.")
    await callback.answer("Скинь на додеп")

@user_router.message(F.text.lower() == "shooter")
@user_router.message(Command("shooter"))
async def Shooter(message: types.Message):
    await message.answer("Выберите игру из списка возможных:", reply_markup=reply.shooter_kb)

@user_router.message(F.text.lower() == "survival")
@user_router.message(Command("survival"))
async def Survival(message: types.Message):
    await message.answer("Выберите игру из списка возможных шутеров:", reply_markup=reply.survival_kb)

@user_router.message(F.text.lower() == "horror")
@user_router.message(Command("horror"))
async def Horror(message: types.Message):
    await message.answer("Выберите игру из списка возможных хорроров:", reply_markup=reply.horror_kb)

@user_router.message(F.text.lower() == "sandbox")
@user_router.message(Command("sandbox"))
async def Sandbox(message: types.Message):
    await message.answer("Выберите игру из списка возможных песочниц:", reply_markup=reply.sandbox_kb)

@user_router.message(F.text.lower() == "rpg")
@user_router.message(Command("rpg"))
async def RPG(message: types.Message):
    await message.answer("Выберите игру из списка возможных рпг:", reply_markup=reply.rpg_kb)

@user_router.message(F.text.lower() == "platformer")
@user_router.message(Command("platformer"))
async def Platformer(message: types.Message):
    await message.answer("Выберите игру из списка возможных платформеров:", reply_markup=reply.platformer_kb)

@user_router.message(F.text.lower() == "назад")
@user_router.message(Command("назад"))
async def back(message: types.Message):
    await message.answer("Главное меню",reply_markup=reply.main_kb)

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
