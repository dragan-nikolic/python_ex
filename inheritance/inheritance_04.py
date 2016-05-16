'''
Created on 2012-01-22

@author: dnikolic
'''

"""
Example: Demonstrate how to use static class level functions of a base class
"""
class B(object):
    """
    B
    """
    def __init__(self, name):
        print 'Running B.__init__ (called by: %s)' % (name)
        self.name = name
        
    def getname(self):
        return self.name
        
    @staticmethod
    def smeth(message):
        print message
        
        

class D1(B):
    """
    D1 doc
    """
    def __init__(self, name):
        super(D1, self).__init__(name)
        print 'Running %s.__init__ (called by: %s)' % (self.__class__.__name__, name)
        
    def fun1(self, message):
        B.smeth(message)
        
        
def example():
    d1obj = D1('this is d1 object')
    d1obj.fun1('fox and dog')
    
if __name__ == '__main__':
    print 'inheritance 04 example'
    example()
        