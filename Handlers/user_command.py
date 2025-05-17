import asyncio
from aiogram.filters import CommandStart, Command
from aiogram import types, Router, F
from Keyboards import reply

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
    await message.answer("Выберите игру из всех доступных")

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

@user_router.message(F.text.lower() == "tower defense")
@user_router.message(Command("tower defense"))
async def TD(message: types.Message):
    await message.answer("Выберите игру из списка возможных тавер дефенсов:", reply_markup=reply.tower_defence_kb)

@user_router.message(F.text.lower() == "simulator")
@user_router.message(Command("simulator"))
async def Simulator(message: types.Message):
    await message.answer("Выберите игру из списка возможных симуляторов:")

@user_router.message(F.text.lower() == "adventure")
@user_router.message(Command("adventure"))
async def Adventure(message: types.Message):
    await message.answer("Выберите игру из списка возможных приключений:")

@user_router.message(F.text.lower() == "platformer")
@user_router.message(Command("platformer"))
async def Platformer(message: types.Message):
    await message.answer("Выберите игру из списка возможных платформеров:")

@user_router.message(F.text.lower() == "puzzle")
@user_router.message(Command("puzzle"))
async def Puzzle(message: types.Message):
    await message.answer("Выберите игру из списка возможных головоломок:")

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
