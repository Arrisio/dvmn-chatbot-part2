import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from src.telegram.loader import dp


# В этом хендлере мы ловим простое нажатие на команду /start, не прошедшее под условие выше


# В этом хендлере мы ловим простое нажатие на команду /start, не прошедшее под условие выше
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.debug('pure start command')
    await message.answer(f'you entered "start" command')
    # await message.answer(f'Список доступных сервисов:')