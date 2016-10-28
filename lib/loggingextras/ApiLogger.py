__author__ = 'Sharon Lev'
__email__ = 'sharon_lev@yahoo.com'
__date__ = '10/26/16'

import sys
from logging import os, Logger, currentframe, _srcfile

class ApiLogger(Logger):
    """
    A logging.Logger class that hides apilog in the trace and shows the calling method in the logged format for funcName
    """

    def findCaller(self):
        """
        Find the stack frame of the caller so that we can note the source
        file name, line number and function name.
        """
        f = currentframe()
        #On some versions of IronPython, currentframe() returns None if
        #IronPython isn't run with -X:Frames.
        if f is not None:
            f = f.f_back
        rv = "(unknown file)", 0, "(unknown function)"
        while hasattr(f, "f_code"):
            co = f.f_code
            filename = os.path.normcase(co.co_filename)
            if filename == _srcfile or __package__.replace('.', '/') in filename:
                f = f.f_back
                continue
            rv = (co.co_filename, f.f_lineno, co.co_name)
            break
        return rv