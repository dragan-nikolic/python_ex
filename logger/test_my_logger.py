'''
Created on 2011-07-15

@author: dnikolic
'''

import my_logger

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.logger = my_logger.my_logger()
    
    def doo(self):
        self.logger.debug('Debug message from doo() function.')

    def ioo(self):
        self.logger.info('Info message from ioo() function.')

    def woo(self):
        self.logger.warning('Warning message from woo() function.')

    def eoo(self):
        self.logger.error('Error message from eoo() function.')

    def hoo(self):
        self.logger.html_img('dragan.png')


def test():
    my_logger.print_logging_levels()
    obj = MyClass()
    obj.doo()
    obj.ioo()
    obj.woo()
    obj.eoo()
    obj.hoo()
    
            
if __name__ == '__main__':
    test()
