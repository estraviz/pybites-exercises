"""
Bite 192. Some logging practice
"""


import logging
from typing import Callable

DEBUG = logging.Logger.debug
INFO = logging.Logger.info
WARNING = logging.Logger.warning
ERROR = logging.Logger.error
CRITICAL = logging.Logger.critical


def log_it(level: Callable, msg: str) -> None:
    logger = logging.getLogger('pybites_logger')
    level(logger, msg)


if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")
