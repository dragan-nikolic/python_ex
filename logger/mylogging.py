'''
Created on 2024-06-11

@author: dnikolic
'''

import logging


def get_logger(module_name: str):
    # Create a custom logger
    logger = logging.getLogger(module_name)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create stream handler
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.DEBUG)
    c_handler.setFormatter(c_format)

    # Create file handler
    f_handler = logging.FileHandler('file.log', 'a')
    f_handler.setLevel(logging.DEBUG)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger
