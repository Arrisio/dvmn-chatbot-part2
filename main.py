import argparse

from loguru import logger

from src.vk import main as run_vk_bot
from src.telegram import run_tg_bot
from src.utils.project_logging import get_loguru_config
from src.utils.system_signals_handle import register_system_handlers


def get_cli_args():
    parser = argparse.ArgumentParser(description="simple Telegram and VK bots")
    parser.add_argument(
        "bot",
        default="tg",
        choices=["tg", "vk"],
        help="which bot wil be started",
        nargs="?",
    )

    return parser.parse_args()


if __name__ == "__main__":
    logger.configure(**get_loguru_config())
    register_system_handlers()

    bot = get_cli_args().bot
    if bot == "tg":
        run_tg_bot()
    elif bot == "vk":
        run_vk_bot()
