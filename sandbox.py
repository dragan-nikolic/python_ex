"""
Created on 2011-05-11

@author: dnikolic
"""

import os
import datetime
import errno
import shutil

try:
    from sikuli import Sikuli
except ImportError:
    Sikuli = None
    
if Sikuli:
    print 'Sikuli is installed!'
else:
    print 'No Sikuli :('


def copy_file(src, dst):
    """
    Copy file ensuring that destination directory exists.
    """

    try:
        os.makedirs(os.path.dirname(dst))
    except OSError, exception:
        print 'errno is: %s' % exception.errno
        print 'strerror is: %s' % exception.strerror
        if (exception.errno != 0) and (exception.errno != errno.EEXIST):
            raise
    shutil.copy(src, dst)

def while_test():
    done = False
    counter = 1
    while not done:
        print counter
        if (counter == 3):
            done = True
        counter += 1
        
def if_tests(input):
    if input:
        print "%s is evaluated True (by if)" % input
    else:
        print "%s is evaluated False (by if)" % input
        
    if input and input != '': 
        print "%s != '' is evaluated True (by if)" % input
    else:
        print "%s != '' is evaluated False (by if)" % input
        

def create_unique_name(prefix="", suffix=""):
    now = datetime.datetime.now()
    unique_name =  prefix + now.strftime('%Y-%m-%d_%H-%M-%S') + suffix
    print 'Unique name is: %s' % unique_name
    
    
def string_as_iterable():
    my_string = 'dragan'
    for c in my_string:
        print c


def print_long_string(message, region):
    print message
    print region

def test_print_long_string():
    text = 'Hello there!'
    print_long_string(
        'This is veryyyyyyyyyyyyyyyyyyyyy looooooooooong '
            'string. It is split into multiple lines. %s ' %
            text,
        'SCREEN')
        
def print_percent_char():
    scalling = 90
    print 'Scaliing=%d%%' % scalling # prints 'Scalling=90%'
    print 'Scaliing=%d%' % scalling # generates exception 'ValueError: incomplete format'
    
import socket
def get_fqdn():
    return socket.getfqdn()
    
class Clients:
    vdi_soft_client      = 'vmware view client'
    teradici_soft_client = 'teradici client'
    tera1_client         = 'tera1 client'
    tera2_client         = 'tera2 client'
    tera2lc              = 'tera2 LC'
    
def inspect_class(cls):
    print dir(cls)

class MyClass:
    def __init__(self):
        self.subobj = None
    
def test_class_init():
    obj = MyClass()
    if obj:
        print 'OK: %s-%s' % (type(obj), str(obj))
    else:
        print 'Fail'
    if obj.subobj:
        print 'OK: %s-%s' % (type(obj.subobj), str(obj.subobj))
    else:
        print 'Subobj Fail'
        
            
if __name__ == '__main__':
    #create_unique_name()
    #string_as_iterable()
    #test_print_long_string()
    #copy_file('c:\\mytemp\\test.bat', 'c:\\mytemp\\dir2\\test.bat')
    #print_percent_char()
    #while_test()
    #print get_fqdn()
    #if_tests('')
    #if_tests(None)
    #if_tests('dragan')
    #inspect_class(Clients)
    test_class_init()
    pass
