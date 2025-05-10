import asyncio

from aiogram.filters import CommandStart, Command
from aiogram import types, Router, F

group_router = Router()

restricted_words = ["Негр", "Nigga", "Гей", "Натурал", "Даун", "Пасхалко", "Квадробоберы", "Гномики", "Паровозик", "п0шел в0н"]
@group_router.message(F.text)
async def cleaner(message: types.Message):
    wlst = message.text.split(" ")
    for word in wlst:
        if word in restricted_words:
            await message.delete()
            await message.answer(f"{message.from_user.first_name} АХ ТЫ **, НЕХОРОШИЙ ЧЕЛОВЕК")
