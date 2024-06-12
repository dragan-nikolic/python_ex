# logging_example.py

import custom_logging

# Create a custom logger
logger = custom_logging.get_logger(__name__)

logger.debug('This is a debug message.')
logger.info('This is an info message.')
logger.warning('This is a warning!')
logger.error('This is an error!')