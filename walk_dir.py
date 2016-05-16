import os
import sys
 
def is_ini_file(filepath):
    return True

def convert_testbed_spec(filepath):
    fp = None
    try:
        fp = open(filepath, 'r')
        file_lines = fp.readlines()
        for file_line in file_lines:
            if file_line.
            print file_line
    except Exception, e:
        raise e
    finally:
        if fp:
            fp.close()
    
    
 
 
for root, _, files in os.walk(sys.argv[1]):
    for filename in files:
        filepath = os.path.abspath(os.path.join(root, filename))
        print '*** %s' % filepath
        if is_ini_file(filepath):
            convert_testbed_spec(filepath)