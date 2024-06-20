"""
Created on 2024-06-11

@author: dnikolic
"""

import logger.mylogging.mylogging as mylogging
from logger.mylogging.my_module1 import MyModule1

logger = mylogging.get_logger(__name__)

logger.debug('This is debug message.')
logger.info('This is info message.')
logger.error('This is error message!')

mm1 = MyModule1()
mm1.foo()
