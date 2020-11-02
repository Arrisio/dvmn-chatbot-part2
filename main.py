import argparse

from loguru import logger

from src.vk import run_vk_bot
from src.telegram import run_tg_bot
from src.utils.project_logging import get_loguru_config


def get_cli_args():
    parser = argparse.ArgumentParser(description="simple Telegram and VK bots")
    parser.add_argument(
        "bot",
        default="vk",
        choices=["tg", "vk"],
        help="which bot wil be started",
        nargs="?",
    )

    return parser.parse_args()


if __name__ == "__main__":
    logger.configure(
        **get_loguru_config()
    )
    bot = get_cli_args().bot
    if bot == "tg":
        run_tg_bot()
    elif bot == "vk":
        run_vk_bot()
