"""
Simple example to demo walk funciton

Usage: $ python walk_ex.py <folder> (default is current dir)
"""

import os
import sys

try:
    dir_name = sys.argv[1]
except:
    dir_name = "."

for root, dirs, files in os.walk(dir_name):
    for filename in files:
        filepath = os.path.abspath(os.path.join(root, filename))
        print('*** %s' % filepath)
