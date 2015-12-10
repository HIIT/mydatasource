import time
from logging import Formatter

class GMTFormatter(Formatter):
    """
    convert to UCT time
    """
    converter = time.gmtime