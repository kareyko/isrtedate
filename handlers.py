from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from translations import get_text
from keyboards import get_main_menu_keyboard

router = Router()

@router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(get_text("welcome", "ru"), reply_markup=get_main_menu_keyboard())
