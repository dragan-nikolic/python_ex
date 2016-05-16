"""
Created on 2012-12-12


@author: dnikolic
"""

import os
import sys
from subprocess import call

def test_call(args):
       
    call('python _callee.py delay=1')
    call('python _callee.py one two three')
    call('start cmd /C python _callee.py delay=5 aaa bbb ccc ddd', shell=True)
    call(
        [
            'start',
            'cmd',
            '/C',
            'python',
            '_callee.py',
            'delay=10',
            'xxx'],
        shell=True)
        
if __name__ == '__main__':
    test_call(sys.argv)
