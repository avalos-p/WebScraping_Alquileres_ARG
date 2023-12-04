import logging.handlers
import os
import sys
from datetime import datetime

from utils.utils import create_folder


class MyFileHandler(logging.handlers.TimedRotatingFileHandler):

    def __init__(self, path, fileName, when, interval, encode):
        """Custom FileHandler inherits from TimedRotatingFileHandler.
        Rotating happens based on the product of when and interval.
        Args:
            path (str): relative path to save log.
            fileName (str): name for the log.
            when (char): type of interval (seconds, minutes, days, ...)
            interval (int): number of times to rotate.
            encode (str): type of log encode.
        """
        # Format today date.
        date = datetime.today().strftime('%m-%Y') 
        # Create logs folder if doesnt exist.
        path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),  path)
        create_folder(path)

        # Create log name.
        fileName = fileName + date
        name = os.path.join(path, fileName+'.log')
        super(MyFileHandler, self).__init__(
            filename=name, when=when, interval=interval, encoding=encode)
