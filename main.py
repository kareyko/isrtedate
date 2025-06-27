from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from bot import bot
from handlers import router
import asyncio
import os

TOKEN = os.getenv("TOKEN")
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")  # например: https://isrte-bot.onrender.com
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

async def on_startup(dispatcher: Dispatcher):
    await bot.set_webhook(WEBHOOK_URL)
    commands = [
        BotCommand(command="/start", description="Начать"),
        BotCommand(command="/help", description="Помощь")
    ]
    await bot.set_my_commands(commands)

async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await on_startup(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
