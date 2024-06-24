"""
Created on 2024-06-22

@author: dnikolic
"""

from utils.logging import Logger
from modules.my_module1 import MyModule1

logger = Logger(__name__)

logger.debug('This is debug message.')
logger.info('This is info message.')
logger.error('This is error message!')

mm1 = MyModule1()
mm1.foo()
