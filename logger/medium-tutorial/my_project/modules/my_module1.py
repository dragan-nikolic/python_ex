"""
Created on 2024-06-22

@author: dnikolic
"""
from utils.logging import Logger

logger = Logger(__name__)


class MyModule1:
    @staticmethod
    def foo():
        logger.debug('This is foo debug message.')
        logger.info('This is foo info message.')
        logger.error('This is foo error message!')
