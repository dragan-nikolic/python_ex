import os
import sys
import inspect

def print_frames():
    current_frame = inspect.currentframe()
    print 'current frame is: %s' % frame_info(current_frame)
    outer_frames = inspect.getouterframes(current_frame)
    ix = 1
    for frame in outer_frames:
        print '%d outer frame is %s' % (ix, frame)
        ix = ix + 1

def frame_info(frame):
    return(
        'code: %s, '
        ''
        '' % frame.f_code)
    
def get_frame(level=0):
    return inspect.getouterframes(inspect.currentframe())[level]
    
def get_modulename():
    return inspect.getmodulename(inspect.getouterframes(inspect.currentframe())[1][1])

def get_filename():
    return os.path.abspath(inspect.getouterframes(inspect.currentframe())[1][1])
    
def sys_get_filename(level=0):
    """returns name of the file containing the caller function at the
    specified stack level"""
    return sys._getframe(level + 1).f_code.co_filename
    
def sys_get_filedir(level=0):
    filename = sys_get_filename(1)
    return (filename, os.path.dirname(os.path.realpath(filename)))


if __name__ == '__main__':
    #print_frames()
    print 'file %s is located in %s' % sys_get_filedir()
    