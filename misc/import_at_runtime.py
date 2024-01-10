"""
Demonstrates how to import a module at run time
"""

class TestClass:
    def __init__(self):
        self.datetime = __import__('datetime')
        
    def use_datetime(self):
        print 'Now is %s' % str(self.datetime.datetime.now())
        
        
if __name__ == '__main__':
    t = TestClass()
    t.use_datetime()
    