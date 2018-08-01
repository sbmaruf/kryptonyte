from __future__ import absolute_import

import logging
import os
# logger = logging.getLogger()


def build_logger(log_file_address=None, level=logging.INFO):
    log_format = logging.Formatter("[%(asctime)s %(levelname)s] %(message)s")
    logger = logging.getLogger()
    logger.setLevel(level)
    if log_file_address and log_file_address != '':
        file_handler = logging.FileHandler(log_file_address)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.handlers = [console_handler]
    return logger
