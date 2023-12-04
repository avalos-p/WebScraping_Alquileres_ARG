from utils.utils import create_folder
from config.cfg import PATH_LOGS
from config.myHandler import MyFileHandler

import os
import logging
import logging.config


# Logging level:
# INFO: Confirmation that things are working as expected.
# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

def create_logger(name_logger, PATH_LOGS):
    """Create log file.
        name_logger (str): Name log.
        PATH_LOGS (str): Path to save the log file.
    Returns: Logger with custom configuration.
    """
    # Create logger folder.
    create_folder(PATH_LOGS)
    # Create logger and set name.
    logger = logging.getLogger(name_logger)
    # Set log level.
    logger.setLevel(logging.INFO)
    # Create formatter.
    formatter = logging.Formatter(
        # %d-%m-%Y - level_name - nombre_logger - mensaje
        fmt='%(asctime)s_%(levelname)s_%(name)s_%(message)s',
        datefmt='%d-%m-%Y')

    # Stream Handler (for console)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File Handler (for .log)
    fh = logging.FileHandler(
        filename="{0}/{1}.log".format(PATH_LOGS, name_logger),
        mode='a')  # 'a' continue, 'w' truncate.
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger


def create_logger_from_file(config: str) -> None:
    assert type(config) == str, "arg type must be string"
    # Create logger from .conf
    
    logging.handlers.MyFileHandler = MyFileHandler

    log_file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), 'config', config)

    logging.config.fileConfig(log_file_path)


def get_logger(name: str) -> logging.Logger:
    assert type(name) == str, "name must be string"
    # Get logger created before. 
    # name (str): logger name.
    # Returns return a logger with the specific name.
    return logging.getLogger(name)
