__author__ = 'Sharon Lev'
__email__ = 'sharon_lev@yahoo.com'
__date__ = '10/25/16'

import sys
from .OutputSetter import OutputSetter
from logging import DEBUG, ERROR, basicConfig
from src.loggingextras import NoneLogger

class test_NoneLogger(OutputSetter):
    """
    a test class to validate NoneLogger does not print anything out to stdout
    """
    def test__no_logging(self):
        basicConfig(level=DEBUG)
        logger = NoneLogger("mylog", level=DEBUG)
        logger.debug("some debug message")
        logger.info("some info message")
        logger.warning("warning")
        logger.error("error")
        logger.critical("critical")
        logger.exception("a message")
        logger.log(level=ERROR, msg="an error message using log")
        self.assertEqual("", sys.stdout.getvalue())

        #validate the following is the only thing being printed out
        somethingelse = "something else to validate stdout gets printed content"
        print somethingelse
        self.assertEqual(somethingelse, sys.stdout.getvalue().strip())
