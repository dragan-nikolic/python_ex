"""
Created on 2011-07-15

@author: dnikolic
"""

import logging


class MyHandler(logging.Handler):
    def __init__(self):
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

        
class MyLogger(logging.Logger):
    def __init__(self):
        logging.Logger.__init__(
                            self, 
                            self.__class__.__name__, 
                            level=logging.DEBUG)
        self.addHandler(MyHandler())
        
    def html_img(self, image):
        self.log(logging.INFO, '%s <img src="%s" />' % (image, image))


def print_logging_levels():
    print(f'DEBUG: {logging.DEBUG}')
    print(f'INFO: {logging.INFO}') 
    print('WARNING: %d' % logging.WARNING)
    print('ERROR: %d' % logging.ERROR)
    print('CRITICAL: %d' % logging.CRITICAL)
