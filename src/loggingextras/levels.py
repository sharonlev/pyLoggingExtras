__author__ = 'Sharon Lev'
__email__ = 'sharon_lev@yahoo.com'
__date__ = '10/25/16'

from logging import addLevelName, CRITICAL, ERROR, WARNING, INFO, DEBUG
FINE = DEBUG / 2
FINER = FINE / 2
FINEST = FINER / 2
addLevelName(FINE, 'FINE')
addLevelName(FINER, 'FINER')
addLevelName(FINEST, 'FINEST')