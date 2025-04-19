import asyncio
from aiogram.filters import CommandStart
from aiogram import Bot, Dispatcher, types
token = "7574376008:AAFp8i62jg6xMdaI4P-rDW-oGYLH8UbBhJw"
bot = Bot(token=token)
dp = Dispatcher()
@dp.message(CommandStart())
async def start_cmd(message):
    await message.answer("Ку, короч он делает то, что ты делаешь. Короч ты пон, бб.")

@dp.message()
async def echo(message: types.Message):
    # await message.answer("Lox")
    user_text = message.text
    await message.answer(user_text)
async def main():
    print("Бот запущен")
    await dp.start_polling(bot)

asyncio.run(main())


























































































