import logging

import colorlog


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    logger.handlers = []

    formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s - %(levelname)s - %(filename)s::%(funcName)s - %(message)s',  #noqa: E501
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.setLevel(logging.INFO)
    logger.info('Logger initialized')

    return logger


logger = get_logger(__name__)
