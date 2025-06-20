'''
Created on 2011-08-12

@author: dnikolic
'''
import os

def os_path_example():
    """
    os.path functions
    """
    
    pathname1 = os.path.join('c:', 'program files', 'videolan', 'vlc')
    print('join: absolute path on C: drive: ' + pathname1)
    
    pathname2 = os.path.join('c:', os.sep, 'program files', 'videolan', 'vlc')
    pathname3 = os.path.join('c:\\', 'program files', 'videolan', 'vlc')  
    print('join: absolute path using os.sep: ' + pathname2)
    print('join: same path without os.sep: ' + pathname3)
    
    filepath1 = os.path.join(pathname2, 'image_01.png')
    dirname1 = os.path.dirname(filepath1)
    print('basename(%s) is: %s' % (filepath1, os.path.basename(filepath1)))
    print('dirname(%s) is: %s' % (filepath1, dirname1))
    print('dirname(%s) is: %s' % (dirname1, os.path.dirname(dirname1)))
    print('abspath(%s) is: %s' % (pathname1, os.path.abspath(pathname1)))
    
    (root, ext) = os.path.splitext(filepath1)
    print('splitext(%s) = (%s, %s)' % (filepath1, root, ext))
    
    (root, ext) = os.path.splitext('c:\\my.dir\\file.01.txt')
    print('splitext(%s) = (%s, %s)' % ('c:\\my.dir\\file.01.txt', root, ext))
    
    local_folder = os.path.abspath('.')
    print('local_folder is %s' % local_folder)
    

def check_path_type(filepath):
    if os.path.isabs(filepath):
        print('Absolute path: %s' % filepath)
    else:
        print('Relative path: %s' % filepath)

def print_working_dir():
    print(f'Working directory is: {os.getcwd()}')


if __name__ == '__main__':
    os_path_example()
    
    check_path_type('relative\\path\\file.ext')
    check_path_type('c:\\absolute\\path\\file.ext')

    print_working_dir()