# -*- coding=utf8 -*-

__author__ = 'Sharon Lev'
__email__ = 'sharon_lev@yahoo.com'
__date__ = '10/25/16'

import sys
from .OutputSetter import OutputSetter
from src.loggingextras.apilog import apilog_debug, apilog_finer

@apilog_debug
def method_debug(param_a=None, param_b=None, param_c=None):
    print 'params:', param_a, param_b, param_c
    assert param_b != "exception", 'failed something'

@apilog_debug
def method_debug_output(param_a=None):
    print 'params:', param_a
    return param_a


@apilog_finer
def method_finer(param_a=None, param_b=None, param_c=None):
    print 'params:', param_a, param_b, param_c
    assert param_b != "exception", 'failed something'


class test_apilog_methods(OutputSetter):
    """
    validation of apilog functionality on non-class methods
    """
    def test__apilog_debug(self, level='DEBUG', method='apilog'):
        method_debug()
        self.validate_output(level, method, None)

    def test__apilog_debug_unnamed_param(self, level='DEBUG', method='apilog'):
        method_debug(9)
        self.validate_output(level, method, None, 9)

    def test__apilog_debug_named_param(self, level='DEBUG', method='apilog'):
        method_debug(param_a=8)
        self.validate_output(level, method, None, param_a=8)

    def test__apilog_debug_unnamed_and_named_param(self, level='DEBUG', method='apilog'):
        method_debug('x', param_c=8)
        self.validate_output(level, method, None, 'x', param_c=8)

    def test__apilog_debug_exception(self, level='DEBUG', method='apilog'):
        self.assertRaises(AssertionError, method_debug, param_b='exception')
        output = self.validate_output(level, method, None, param_b='exception')
        self.assertIn("AssertionError", output[2][2])

    def test__apilog_debug_output_primitive(self, level='DEBUG', method='apilog'):
        expected_output = 6
        method_debug_output(expected_output)
        self.validate_output(level, method, expected_output)

    def test__apilog_debug_output_array(self, level='DEBUG', method='apilog'):
        expected_output = [1, 2, 3]
        method_debug_output(expected_output)
        self.validate_output(level, method, expected_output)

    def test__apilog_debug_output_dict(self, level='DEBUG', method='apilog'):
        expected_output = dict(k1=1, k2=2)
        method_debug_output(expected_output)
        self.validate_output(level, method, expected_output)

    def test__apilog_finer_named_param(self, level='FINER', method='apilog'):
        method_finer(param_b='something')
        self.validate_output(level, method, None, param_b='something')

    def test_apilog_debug_non_ascii(self, level='DEBUG', method='apilog'):
        method_debug('㆒㆓㆔㆕', param_b='㆕㆔㆓㆒')
        self.validate_output(level, method, None, '㆒㆓㆔㆕', param_b='㆕㆔㆓㆒')

    def test_apilog_debug_output_non_ascii(self, level='DEBUG', method='apilog'):
        method_debug_output(param_a='㆒㆓㆔㆕')
        self.validate_output(level, method, '㆒㆓㆔㆕', param_a='㆒㆓㆔㆕')
