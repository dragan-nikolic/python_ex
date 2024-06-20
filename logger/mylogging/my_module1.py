"""
Created on 2024-06-11

@author: dnikolic
"""

import logger.mylogging.mylogging as mylogging

logger = mylogging.get_logger(__name__)


class MyModule1:
    @staticmethod
    def foo():
        logger.debug('This is foo debug message.')
        logger.info('This is foo info message.')
        logger.error('This is foo error message!')
