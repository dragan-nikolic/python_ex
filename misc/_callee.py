"""
Created on 2012-12-12

To be called by caller.py


@author: dnikolic
"""

import sys
import time

print 'callee arguments are %s' % str(sys.argv)

cmd = ''
try:
    cmd, value = sys.argv[1].split('=')
except:
    pass

if str(cmd) == 'delay':
    time.sleep(float(value))

