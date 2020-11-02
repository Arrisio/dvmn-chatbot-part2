import logging

from aiogram import types
from src.telegram.loader import dp

from src.dialogflow import get_response_text


@dp.message_handler()
async def dialogflow_response(message: types.Message):
    logging.debug("dialogflow_response")
    await message.answer(get_response_text(message.text))
