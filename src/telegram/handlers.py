import logging

from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from .users import dp

__all__ = ["dp"]

from ..loader import dp
from ...dialogflow import get_response_text


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.debug("pure start command")
    await message.answer(f'you entered "start" command')


@dp.message_handler()
async def dialogflow_response(message: types.Message):
    logging.debug("dialogflow_response")
    await message.answer(get_response_text(message.text))