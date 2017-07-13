"""apilog"""
import sys
from datetime import datetime
from logging import NOTSET, Logger, basicConfig, getLogger
from ..levels import *
from json import dumps

__author__ = 'Sharon Lev'
__email__ = 'sharon_lev@yahoo.com'
__date__ = '10/25/16'


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class BasicLogger(Logger):
    __metaclass__ = Singleton
    _logger = None

    def __init__(self, name, level=NOTSET):
        try:
            sys.stderr.write("using : %s\n" % sys.stdout)
        except:
            pass
        basicConfig(level=1, stream=sys.stdout)
        super(BasicLogger, self).__init__(name, level)


def getBasicLogger():
    basicConfig(level=1, stream=sys.stdout)
    return getLogger('apilog')


def apilog(method, level=NOTSET):
    """
    a decorator for logging methods usage
    :param method: decorated method
    :param level: logging level to use for logging
    :return: decorated method returned value
    """
    def decorator(self=None, *wargs, **kwargs):
        exit_message = ''
        time_end = None
        method_name = method.__name__
        is_class_method = method_name in dir(self) if self else False
        logger = getattr(self, 'logger', None) if is_class_method else None
        logger = logger or getBasicLogger()  # BasicLogger(name='apilog', level=1)

        time_start = datetime.now()
        logger.log(
            level,
            'entering %s with wargs=%s, kwargs=%s' %
            (
                method_name,
                dumps(
                    [
                        repr(arg) for arg in wargs
                    ] if is_class_method or not self else tuple([self] + [repr(arg) for arg in wargs]),
                    ensure_ascii=False
                ),
                dumps(kwargs, ensure_ascii=False)
            )
        )
        try:
            retval = method(self, *wargs, **kwargs) if self else method(*wargs, **kwargs)
            time_end = datetime.now()
            exit_message = retval
            return retval
        except BaseException as e:
            time_end = datetime.now()
            exit_message = '[%s: %s]' % (e.__class__.__name__, e)
            raise
        finally:
            try:
                logger.log(
                    level, 'exiting %s with %s in [%s]' % (
                        method_name, dumps(exit_message, ensure_ascii=False), time_end - time_start
                    )
                )
            except:
                logger.log(
                    level, 'exiting %s with %s in [%s]' % (
                        method_name, str(exit_message), time_end - time_start
                    )
                )

    return decorator


def apilog_finest(method):
    return apilog(method, FINEST)


def apilog_finer(method):
    return apilog(method, FINER)


def apilog_fine(method):
    return apilog(method, FINE)


def apilog_debug(method):
    return apilog(method, DEBUG)


def apilog_info(method):
    return apilog(method, INFO)


def apilog_warning(method):
    return apilog(method, WARNING)


def apilog_error(method):
    return apilog(method, ERROR)


def apilog_critical(method):
    return apilog(method, CRITICAL)
