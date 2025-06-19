'''
Created on 2011-07-19

@author: dnikolic
'''

"""
Example: Demonstrate how to call constructor of the base class
"""
class B1(object):
    def __init__(self, name, number):
        print 'Running B1.__init__ (%s, %d)' % (name, number)
        self.name = name
        self.number = number
        
    def getname(self):
        return self.name

    def getnumber(self):
        return self.number


class B2(object):
    def __init__(self, name):
        print 'Running B2.__init__ (%s)' % (name)
        self.name = name
        
    def getname(self):
        return self.name
        

class B3():
    def __init__(self, name):
        print 'Running B3.__init__ (%s)' % (name)
        self.name = name
        
    def getname(self):
        return self.name


class D1(B1, B3):
    '''
    Calls constructor using 'super'
    '''
    def __init__(self, name, number1, number2):
        super(D1, self).__init__(name, number1)
        print 'Running D1.__init__ (%s, %d, %d)' % (name, number1, number2)


class D2(B1, B2, B3):
    '''
    Calls base classes constructors explicitly
    '''
    def __init__(self, name, number1, number2):
        B1.__init__(self, name, number1)
        B2.__init__(self, name)
        B3.__init__(self, name)
        print 'Running D2.__init__ (%s, %d, %d)' % (name, number1, number2)

def example():
    print "Use 'super' to call base class constructor"
    d1_1 = D1('d1_1', 1, 2)
    d1_2 = D1('d1_2', 3, 4)
    print 'd1_1.name is: %s' % d1_1.getname()
    print 'd1_2.name is: %s' % d1_2.getname()
    print
    
    print "Call base class constructors explicitly "
    d2_1 = D2('d2_1', 5, 6)
    d2_2 = D2('d2_2', 7, 8)
    print 'd2_1.name is: %s' % d2_1.getname()
    print 'd2_2.name is: %s' % d2_2.getname()
    print


if __name__ == '__main__':
    print 'inheritance 02 example'
    example()
        