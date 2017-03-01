__author__ = 'Sharon Lev'
__email__ = 'sharon_lev@yahoo.com'
__date__ = '10/25/16'

import sys
from .OutputSetter import OutputSetter
from src.loggingextras.apilog import apilog_debug, apilog_finer
from logging import basicConfig, getLogger

class decorated_class_without_logger(object):

    @apilog_debug
    def method_debug(self, param_a=None, param_b=None, param_c=None):
        print 'params:', param_a, param_b, param_c
        assert param_b != "exception", 'failed something'

    @apilog_finer
    def method_finer(self, param_a=None, param_b=None, param_c=None):
        print 'params:', param_a, param_b, param_c
        assert param_b != "exception", 'failed something'


class decorated_class_with_logger(object):

    def __init__(self):
        basicConfig(level=1, stream=sys.stdout)
        self.logger = getLogger('decorated_class')

    @apilog_debug
    def method_debug(self, param_a=None, param_b=None, param_c=None):
        print 'params:', param_a, param_b, param_c
        assert param_b != "exception", 'failed something'

    @apilog_finer
    def method_finer(self, param_a=None, param_b=None, param_c=None):
        print 'params:', param_a, param_b, param_c
        assert param_b != "exception", 'failed something'


class test_apilog_class_methods(OutputSetter):
    """
    validation of apilog functionality on class methods with and without a class.logger
    """
    def setUp(self):
        super(test_apilog_class_methods, self).setUp()
        self.deco = decorated_class_with_logger()
        self.deco_without = decorated_class_without_logger()

    def test__apilog_debug_with_logger(self, level='DEBUG', method='decorated_class'):
        self.deco.method_debug()
        self.validate_output(level, method, None)

    def test__apilog_finer_named_param_with_logger(self, level='FINER', method='decorated_class'):
        self.deco.method_finer(param_b='something')
        self.validate_output(level, method, None, param_b='something')

    def test__apilog_debug_without_logger(self, level='DEBUG', method='apilog'):
        self.deco_without.method_debug()
        self.validate_output(level, method, None)

    def test__apilog_finer_named_param_without_logger(self, level='FINER', method='apilog'):
        self.deco_without.method_finer(param_b='something')
        self.validate_output(level, method, None, param_b='something')