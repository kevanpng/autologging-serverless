# https://pythonhosted.org/Autologging/examples-traced.html
from autologging import traced, TRACE

import logging
import sys
logging.basicConfig(
        level=TRACE, stream=sys.stdout,
        format='%(levelname)s:%(name)s:%(funcName)s:%(message)s')


@traced
def foo(x, y):
    a = x + y
    return a


foo(1, 2)
