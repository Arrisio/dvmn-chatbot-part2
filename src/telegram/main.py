from aiogram import executor
from loguru import logger

from src.telegram.handlers import dp
from src.telegram.utils import on_startup_notify
from src.utils.project_logging import get_loguru_config


async def on_startup(dp):
    await on_startup_notify(dp)


def run_tg_bot():
    logger.info("telegram service started")
    executor.start_polling(dp, on_startup=on_startup)
    logger.info("service service stopped")


if __name__ == "__main__":

    logger.configure(
        **get_loguru_config(use_default_prod_configuration=False, level="DEBUG")
    )
    run_tg_bot()
