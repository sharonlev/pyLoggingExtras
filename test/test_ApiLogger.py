__author__ = 'Sharon Lev'
__email__ = 'sharon_lev@yahoo.com'
__date__ = '10/26/16'

import sys
from logging import basicConfig, getLogger, StreamHandler, Formatter
from src.loggingextras import ApiLogger
from src.loggingextras.apilog import apilog_debug
from .OutputSetter import OutputSetter


class mock_class(object):
    """
    a class with a logger and a decorated method
    """
    def __init__(self):
        basicConfig(level=1, format="%(funcName)s:%(message)s")
        self.logger = getLogger('regular')

    @apilog_debug
    def decorated_method(self):
        return 0

class mock_class_api(mock_class):
    """
    a child class with an ApiLogger that will hide the 'decorator' method name and log the calling method name instread
    """
    def __init__(self):
        basicConfig(level=1)
        self.logger = ApiLogger('apifriendly', level=1)
        formatter = Formatter("%(funcName)s:%(message)s")
        handler = StreamHandler(stream=sys.stdout)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)


class test_ApiLogger(OutputSetter):
    """
    """

    def setUp(self):
        self.regular_log_class = mock_class()
        self.api_log_class = mock_class_api()

    def test__api_logger_improved(self):
        calling_method = self.id().split('.')[-1]
        self.regular_log_class.decorated_method()
        self.assertNotIn(calling_method, sys.stdout.getvalue())
        sys.stdout.truncate()
        self.api_log_class.decorated_method()
        self.assertIn(calling_method, sys.stdout.getvalue())

