import sys
import os
import inspect

def LINE(back = 0):
    return sys._getframe( back + 1 ).f_lineno
def FILE(back = 0):
    return sys._getframe( back + 1 ).f_code.co_filename
def FUNC(back = 0):
    return sys._getframe( back + 1 ).f_code.co_name
    
def get_module_name(object):
    s = inspect.stack()
    print s
    return inspect.getmodule(object)

def my_function():
    print 'Function name is: %s' % FUNC()
    
class MyClass:
    def my_class_method(self):
        print 'Class: %s' % self.__class__.__name__
        print 'Method name is: %s' % FUNC()
        print 'This is line: %s (%s/%s)' % (FUNC(), FILE(), LINE())
        

print 'what is this %s?' % get_module_name(LINE) 
    
    
if __name__ == '__main__':
    my_function()
    
    c = MyClass()
    c.my_class_method()
    print 'c is instance of class: %s' % c.__class__.__name__
    print 'what is this %s?' % get_module_name(LINE) 
    
    