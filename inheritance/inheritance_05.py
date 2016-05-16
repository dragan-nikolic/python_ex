'''
Created on 2012-11-16

@author: dnikolic
'''

"""
Example: Demonsrates how base class function calls derived class function
"""

class B(object):
    def __init__(self):
        pass
        
    def foo(self):
        self.goo()


class D(B):
    def __init__(self):
        super(D, self).__init__()

    def goo(self):
        print 'I am goo!'

def example():
    dobj = D()
    dobj.foo()

if __name__ == '__main__':
    print 'inheritance 05 example'
    example()
    
    """
    Output:
    inheritance 05 example
    I am goo!
    """
        