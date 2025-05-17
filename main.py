import asyncio
from aiogram import Bot, Dispatcher

token = "7574376008:AAFp8i62jg6xMdaI4P-rDW-oGYLH8UbBhJw"
bot = Bot(token=token)
dp = Dispatcher()

from Handlers.user_command import user_router
dp.include_router(user_router)

from Handlers.Catalog import catalog_router
dp.include_router(catalog_router)

from Handlers.group_command import group_router
dp.include_router(group_router)

async def main():
    print("Бот запущен")
    await dp.start_polling(bot)

asyncio.run(main())


























































































