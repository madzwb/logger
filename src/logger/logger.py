import logging
import multiprocessing
import os
import sys

import logger.config as config

if config.LOG_MULTI:
    logger = multiprocessing.get_logger()
else:
    logger = logging.getLogger()

formatter = logging.Formatter("%(asctime)s [%(levelname)-8s] - %(message)s")
formatter_result = logging.Formatter("%(message)s")
formatter.default_msec_format = '%s.%03d'

def init():
    if not config.SCRIPT:
        return
    name = os.path.splitext(os.path.basename(config.SCRIPT))[0]
    if config.LOG_TO_TERMINAL:
        found = [handler for handler in logger.handlers if handler.name == "stderror"]
        if not found:
            stream_handler  = logging.StreamHandler()
            stream_handler.name = "stderror"
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)

    if config.LOG_TO_FILE and config.SCRIPT:
        found = [handler for handler in logger.handlers if handler.name == name + ".log"]
        if not found:
            filename = os.path.dirname(config.SCRIPT)
            filename += "/"
            filename += name#os.path.splitext(os.path.basename(config.SCRIPT))[0]
            filename += ".log"
            file_handler =  logging.FileHandler(filename)
            file_handler.name = name + ".log"
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    level = logging.DEBUG if config.DEBUG else logging.INFO
    logger.setLevel(level)

def truncate():
    if      config.LOG_FILE_TRUNCATE                                            \
        and config.SCRIPT                                                       \
        and (name := os.path.splitext(os.path.basename(config.SCRIPT))[0])  \
    :
        found = [handler for handler in logger.handlers if handler.name == name + ".log"]
        if not found:
            path = os.path.dirname(config.SCRIPT)
            full = (path + "/" + name + ".log")
            with open(full,"w") as file:
                pass
