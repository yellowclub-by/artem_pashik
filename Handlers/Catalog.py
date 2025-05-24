import asyncio
from aiogram.filters import CommandStart, Command
from aiogram import types, Router, F
from aiogram.types import FSInputFile
from Keyboards import reply

catalog_router = Router()
@catalog_router.message(F.text.lower() == "counter strike 2")
async def cs2(message: types.Message):
    photo = FSInputFile(r"images\catalog\cs2prev.jpeg")
    await message.answer_photo(photo, caption="пж зарегай 2")
    await message.answer("Отлично! Ваш выбор Counter Strike 2. Ожидайте ключ от игры в течении 5 минут.")

@catalog_router.message(F.text.lower() == "call of duty")
async def cod(message: types.Message):
    photo = FSInputFile(r"images\catalog\codprev.jpeg")
    await message.answer_photo(photo, caption="калда")
    await message.answer("Отлично! Ваш выбор Call of duty. Ожидайте ключ от игры в течении 5 минут.")








