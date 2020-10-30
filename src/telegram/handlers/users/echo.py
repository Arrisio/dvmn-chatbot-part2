import logging

from aiogram import types
from src.telegram.loader import dp

from src.dialogflow import get_response_text

@dp.message_handler()
async def bot_echo(message: types.Message):
    logging.debug('bot_echo')
    await message.answer(get_response_text(message.text))