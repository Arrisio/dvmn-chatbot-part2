import signal
from sys import platform, exit

from loguru import logger


def sigterm_handler(_signo, _stack_frame):
    logger.debug("sigterm_handler executed, %s, %s" % (_signo, _stack_frame))
    exit(0)


signal.signal(signal.SIGTERM, sigterm_handler)
signal.signal(signal.SIGINT, sigterm_handler)
if platform != "win32":
    signal.signal(signal.SIGQUIT, sigterm_handler)
