__author__ = 'Sharon Lev'
__email__ = 'sharon_lev@yahoo.com'
__date__ = '10/25/16'

from logging import Logger, NOTSET

class NoneLogger(Logger):
    """
    A class that supports the logging interface, but does not perform any logging (Null Object Design Pattern)
    """
    def __init__(self, name, level=NOTSET):
        pass

    def debug(self, msg, *args, **kargs):
        pass

    def info(self, msg, *args, **kargs):
        pass

    def warning(self, msg, *args, **kargs):
        pass

    def error(self, msg, *args, **kargs):
        pass

    def critical(self, msg, *args, **kwargs):
        pass

    def log(self, level, msg, *args, **kwargs):
        pass