import os
import sys
import re

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

        result = find_pattern_in_string('\.E\d\d\.', filename)
        print('result: ', result)
        if result:
            print('result: ', result[1:-1])
            rename_file(filepath, os.path.join(filepath_parts[0], 'new_' + result[1:-1] + '_name.m4v'))
