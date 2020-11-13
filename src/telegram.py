import logging
import os

from aiogram import Dispatcher, Bot, types
from aiogram.dispatcher.filters import CommandStart, BoundFilter
from aiogram.utils import executor
from loguru import logger

from src.dialogflow import get_response_text


def run_tg_bot():
    logger.info("telegram service started")
    executor.start_polling(dp, on_startup=on_startup_notify)
    logger.info("service service stopped")


async def on_startup_notify(dp: Dispatcher):
    if admin := os.getenv("TG_ADMIN_ID"):
        try:
            await dp.bot.send_message(admin, "Бот Запущен и готов к работе!")
        except Exception as err:
            logger.exception(err)


dp = Dispatcher(Bot(token=os.environ["TG_BOT_TOKEN"], parse_mode=types.ParseMode.HTML))


class IsPrivate(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type == types.ChatType.PRIVATE


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.debug("pure start command")
    await message.answer(f'you entered "start" command')


@dp.message_handler(IsPrivate())
async def dialogflow_response(message: types.Message):
    logging.debug("dialogflow_response")
    await message.answer(
        get_response_text(message.text, session_id=f"tg-{message.from_user.id}")
    )
