'''
Created on 2011-06-08

@author: dnikolic
'''

import global_data

"""
Example: Demonstrate how to use static class level variable of a base class
         to exchange information between objects of the derived  classes
"""
class B(object):
    """
    B
    """
    shared_var = None
    
    def __init__(self, name):
        print 'Running B.__init__ (called by: %s)' % (name)
        self.name = name
        
    def getname(self):
        return self.name
        
    def set_shared_var(self, value):
        print 'set_shared_var by ' + self.name + '. Value: ' + value
        B.shared_var = value
        
    def get_shared_var(self):
        print 'get_shared_var(%s) by %s.' % (B.shared_var, self.name)
        return B.shared_var
        
    def set_global(self, value):
        global_data.global_variable = value

    def print_global(self):
        print 'Global variable is: %d' % global_data.global_variable

class D1(B):
    """
    D1 doc
    """
    def __init__(self, name):
        super(D1, self).__init__(name)
        print 'Running %s.__init__ (called by: %s)' % (self.__class__.__name__, name)
        
class D2(B):
    def __init__(self, name):
        super(D2, self).__init__(name)
        print 'Running %s.__init__ (called by: %s)' % (self.__class__.__name__, name)
        
def example():
    d1obj = D1('d1obj')
    d1obj.set_shared_var('go cunacks go')
    d2obj = D2('d2obj')
    shared_var = d2obj.get_shared_var()
    print 'd2obj value for shared_var is: %s' % shared_var
    
    print 'd1obj name is: %s' % d1obj.getname()
    print 'd2obj name is: %s' % d2obj.getname()
    
    d1obj.set_global(5)
    d2obj.print_global()

    d2obj.set_global(8)
    d1obj.print_global()

if __name__ == '__main__':
    print 'inheritance 01 example'
    example()
        