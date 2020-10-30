from loguru import logger
import os
from aiogram import Dispatcher


async def on_startup_notify(dp: Dispatcher):
    if admin := os.getenv("TL_ADMIN_ID"):
        try:
            await dp.bot.send_message(admin, "Бот Запущен и готов к работе!")
        except Exception as err:
            logger.exception(err)
