'''
Created on 2011-07-25

@author: dnikolic
'''

"""
Example: Demonstrate how to use instance variables per class
"""

class B(object):
    def __init__(self):
        self.name = None
        self.b_name = None
        
    def get_name(self):
        if self.name is None:
            self.name = "This is Base"
        return self.name
    
    def get_b_name(self):
        if self.b_name is None:
            self.b_name = "This is Base"
        return self.b_name
    
    def print_b(self):
        print self.get_name()
        print self.get_b_name()


class D1(B):
    def __init__(self):
        super(D1, self).__init__()

    def get_name(self):
        if self.name is None:
            self.name = "This is Der1"
        return self.name
    
    def print_name(self):
        print self.get_name()


class D2(B):
    def __init__(self):
        super(D2, self).__init__()

    def get_name(self):
        if self.name is None:
            self.name = "This is Der2"
        return self.name

    def print_name(self):
        print self.get_name()


def example():
    d1obj = D1()
    d2obj = D2()
    
    d1obj.print_b()
    d1obj.print_name()

    d2obj.print_b()
    d2obj.print_name()

if __name__ == '__main__':
    print 'inheritance 03 example'
    example()
    
    """
    Output:
    inheritance 03 example
    This is Der1
    This is Base
    This is Der1
    This is Der2
    This is Base
    This is Der2
    """
        