import inspect_lib
import os

def print_frames():
    inspect_lib.print_frames()
    
def f():
    print 'this is myfunction'
    cf = inspect.currentframe()
    print str(cf)
    print str(inspect.getmodulename(__file__))
    print os.path.abspath(__file__)
    print cf.f_globals
    print cf.f_locals
    print __file__
    #print __module__
    return 'myfunction receives %s' % str(x)
    
if __name__ == '__main__':
    #print_frames()
    print inspect_lib.get_modulename()
    #print inspect_lib.get_filename()
    print 'file %s is located in %s' % inspect_lib.sys_get_filedir()
    