"""
Created on 2024-06-11

@author: dnikolic
"""

import mylogging
from my_module1 import MyModule1

mm1 = MyModule1()
mm1.foo()

logger = mylogging.get_logger(__name__)

logger.debug('This is debug message.')
logger.info('This is info message.')
logger.error('This is error message!')

