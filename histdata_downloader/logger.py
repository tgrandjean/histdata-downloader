import logging
from logging.handlers import RotatingFileHandler
import os
import re
import sys
import traceback

from datetime import datetime


def set_root_logger(loglevel=logging.INFO):
    """Setup the root logger.
    Loaded in main process."""
    rootlogger = logging.getLogger()
    rootlogger.setLevel(loglevel)
    return rootlogger

def log_setup(loglevel, logfile):
    """Initial log set up."""
    numeric_loglevel = get_loglevel(loglevel)
    root_loglevel = numeric_loglevel
    rootlogger = set_root_logger(loglevel=root_loglevel)
    log_format = logging.Formatter("%(asctime)s %(module)-15s %(funcName)-25s"
                                   "%(levelname)-8s %(message)s",
                                   datefmt="%d/%m/%Y %H:%M:%S")
    f_handler = file_handler(numeric_loglevel, logfile, log_format)
    s_handler = stream_handler(numeric_loglevel)

    rootlogger.addHandler(f_handler)
    rootlogger.addHandler(s_handler)
    disable_existing_logger()
    logging.info("Log level set to: %s", loglevel.upper())

def get_loglevel(loglevel):
    """ Check valid log level supplied and return numeric log level """
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % loglevel)

    return numeric_level


def file_handler(loglevel, logfile, log_format):
    """ Add a logging rotating file handler """
    log_file = RotatingFileHandler(logfile, 'a', 10e6, backupCount=1)
    log_file.setFormatter(log_format)
    log_file.setLevel(loglevel)
    return log_file


def stream_handler(loglevel):
    """ Add a logging cli handler """
    log_format = logging.Formatter("%(asctime)s %(levelname)-8s %(message)s",
                                   datefmt="%d/%m/%Y %H:%M:%S")
    log_console = logging.StreamHandler(sys.stdout)
    log_console.setFormatter(log_format)
    log_console.setLevel(loglevel)
    return log_console

def disable_existing_logger():
    """disable_existing_logger"""
    logger_to_disable = ['urllib3', 'urllib3.connectionpool', 'numexpr.utils']
    for _ in logger_to_disable:
        logging.getLogger(_).setLevel(logging.CRITICAL)
