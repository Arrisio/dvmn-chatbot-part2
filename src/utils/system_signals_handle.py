import signal
from sys import platform, exit

from loguru import logger



def _sigterm_handler(_signo, _stack_frame):
    logger.debug("sigterm_handler executed, %s, %s" % (_signo, _stack_frame))
    exit(0)


def register_system_handlers():
    """
        Register default system signals handlers is necessary to gracefully stopping program in Docker
    :return:
    """
    signal.signal(signal.SIGTERM, _sigterm_handler)
    signal.signal(signal.SIGINT, _sigterm_handler)
    if platform != "win32":
        signal.signal(signal.SIGQUIT, _sigterm_handler)
