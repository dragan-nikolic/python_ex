class Shape(object):
    def __init__(self, color):
        self.color = color
    
    def area(self):
        print 'shape %s does not know how to calculate area!' % self.__class__.__name__

class Circle(Shape):
    def __init__(self, color, radius):
        super(Circle, self).__init__(color)
        self.radius = radius

    def whoami(self):
        print 'I am %s %s with radius %d' % (self.color, self.__class__.__name__, self.radius) 

class Rectangle(Shape):
    def __init__(self, color, a, b):
        super(Rectangle, self).__init__(color)
        self.a = a
        self.b = b

    def whoami(self):
        print 'I am %s %s with sides %d and %d' % (self.color, self.__class__.__name__, self.a, self.b) 

    def area(self):
        print '%s area is %d' % (self.__class__.__name__, self.a*self.b)


class ShapeFactoryA(object):
    def __new__(klass, shape, *args, **kwargs):
        return shape(*args, **kwargs)
        
class ShapeFactoryB(object):
    def __init__(self, shape, *args, **kwargs):
        self.shape = shape(*args, **kwargs)

    def __getattr__(self, method):
        return getattr(self.shape, method)

if __name__ == '__main__':
    s1 = ShapeFactoryA(Circle, 'green', 5)
    s1.whoami()
    s1.area()
    
    s2 = ShapeFactoryB(Rectangle, b=7, color='yellow', a=8)
    s2.whoami()
    s2.area()
    
    s3 = ShapeFactoryB(Rectangle, 'red', b=4, a=9)
    s3.whoami()
    s3.area()
    
    print 'object s1 is %s' % str(s1)
    print 's1 type is %s, identity is %s' % (type(s1), id(s1))
