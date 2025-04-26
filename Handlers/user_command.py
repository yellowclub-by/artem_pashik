import asyncio
from aiogram.filters import CommandStart, Command
from aiogram import types, Router

user_router = Router()

@user_router.message(CommandStart())
async def start_cmd(message):
    await message.answer("Бот для покупки игр. Команды /buy - купить по жанру игры, /сatalog - выбрать из всего каталога")

@user_router.message(Command("buy"))
async def genre(message: types.Message):
    await message.answer("Выберите жанр игры")

@user_router.message(Command("catalog"))
async def catalog(message: types.Message):
    await message.answer("Выберите игру из всех доступных")

# @user_router.message(Command("Shooter"))
# async def katalog(message: types.Message):
#     await message.answer("Выберите игру из списка возможных:")
#
# @user_router.message(Command("Survival"))
# async def katalog(message: types.Message):
#     await message.answer("Выберите игру из списка возможных:")
#
# @user_router.message(Command("Horror"))
# async def katalog(message: types.Message):
#     await message.answer("Выберите игру из списка возможных:")
#
# @user_router.message(Command("Sandbox"))
# async def katalog(message: types.Message):
#     await message.answer("Выберите игру из списка возможных:")
#
# @user_router.message(Command("RPG"))
# async def katalog(message: types.Message):
#     await message.answer("Выберите игру из списка возможных:")
#
# @user_router.message(Command("Tower Defense"))
# async def katalog(message: types.Message):
#     await message.answer("Выберите игру из списка возможных:")
#
# @user_router.message(Command("Simulator"))
# async def katalog(message: types.Message):
#     await message.answer("Выберите игру из списка возможных:")
#
# @user_router.message(Command("Adventure"))
# async def katalog(message: types.Message):
#     await message.answer("Выберите игру из списка возможных:")
#
# @user_router.message(Command("Platformer"))
# async def katalog(message: types.Message):
#     await message.answer("Выберите игру из списка возможных:")
#
# @user_router.message(Command("Puzzle"))
# async def katalog(message: types.Message):
#     await message.answer("Выберите игру из списка возможных:")

@user_router.message()
async def echo(message: types.Message):
    # await message.answer("Lox")
    user_text = message.text
    await message.answer(user_text)
