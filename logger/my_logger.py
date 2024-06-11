'''
Created on 2011-07-15

@author: dnikolic
'''

import logging

class my_handler(logging.Handler):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        logging.Handler.__init__(self, level=logging.DEBUG)

    def emit(self, record):
        print(self.format(record))
    
    def format(self, record):
        self.formatter = logging.Formatter(
                '*%(levelname)s* '
                '[Module: %(module)s] '
                '[Func: %(funcName)s] '
                '[Line: %(lineno)d] '
                '%(message)s')
        return self.formatter.format(record)

        
class my_logger(logging.Logger):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        logging.Logger.__init__(
                            self, 
                            self.__class__.__name__, 
                            level=logging.DEBUG)
        self.addHandler(my_handler())
        
    def html_img(self, image):
        self.log(logging.INFO, '%s <img src="%s" />' % (image, image))


def print_logging_levels():
    print(f'DEBUG: {logging.DEBUG}')
    print('WARNING: %d' % logging.WARNING)
    print(f'INFO: {logging.INFO}') 
    print('ERROR: %d' % logging.ERROR)
    print('CRITICAL: %d' % logging.CRITICAL)
