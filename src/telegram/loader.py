import os

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=os.environ["TG_BOT_TOKEN"], parse_mode=types.ParseMode.HTML)
# storage = RedisStorage2(
#     host=os.getenv("REDIS_HOST", "localhost"),
#     port=os.getenv("REDIS_PORT", 6379),
# )
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)
