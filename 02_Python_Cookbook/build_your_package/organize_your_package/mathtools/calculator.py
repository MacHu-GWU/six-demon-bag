from .chengfa.times_X import *
from .jiafa.plus_X import *

class Calculator(object):
    def __init__(self):
        pass
    
    def run(self, cmd, num):
        print eval(cmd + '(%s)' % num)