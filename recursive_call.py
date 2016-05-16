"""
Created on 2012-12-12

Execute this test 2 times.


@author: dnikolic
"""

import os
import sys
from subprocess import call
from time import sleep

TEMPFILE = 'envvartesttemp'

def test_call(args):
    print 'All argumnents are: %s' % str(args)
       
    # pause to be able to see output from 'start cmd /C' call (see below, this is recursive)
    sleep(2)

    if os.path.exists(TEMPFILE) is False:
        f = open(TEMPFILE, 'wb')
        f.write('\0')
        f.close()
        
        call('python recursive_call.py')
        call('start cmd /C python recursive_call.py', shell=True)
        
        # pause longer then first pause before deleting file, otherwise 'start cmd /C' call goes into endless loop
        sleep(3)
        os.remove(TEMPFILE)
        
if __name__ == '__main__':
    test_call(sys.argv)
