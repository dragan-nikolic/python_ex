"""
The utility for renaming all the files in a directory which name contains 
PATTERN_IN_ORIGINAL_NAME text.

New name will be NAME_PREFIX + PATTERN_IN_NEW_NAME + NAMME_SUFFIX.

Examples:
    old.E23.name.mp4 -> new_E23_name.m4v
"""
import os
import sys
import re

# --- Modify these variables to customize the renaming ---
PATTERN_IN_ORIGINAL_NAME = '\.E\d\d\.'
PATTERN_IN_NEW_NAME = 'E\d\d'
NAME_PREFIX = 'new_'
NAME_SUFFIX = '_name.m4v'
# --------------------------------------------------------

try:
    dir_name = sys.argv[1]
except:
    dir_name = "."

def find_pattern_in_string(pattern, string):
    '''Returns string that satisfies pattern if found
    Otherwise returns None 
    '''
    res = None
    
    try:
        res = re.compile(pattern).search(string).group()
    except:
        res = None    

    return res

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)


for root, dirs, files in os.walk(dir_name):
    for filename in files:
        filepath = os.path.abspath(os.path.join(root, filename))
        print(filepath)

        filepath_parts = os.path.split(filepath)
        filename = filepath_parts[1]
        print(filename)
        print(type(filename))

        result = find_pattern_in_string(PATTERN_IN_ORIGINAL_NAME, filename)
        print('result1: ', result)
        print(type(result))
        result = find_pattern_in_string(PATTERN_IN_NEW_NAME, result)
        print('result2: ', result)
        if result:
            rename_file(filepath, os.path.join(filepath_parts[0], NAME_PREFIX + result + NAME_SUFFIX))
