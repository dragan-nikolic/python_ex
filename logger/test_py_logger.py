'''
Created on 2012-04-19

@author: dnikolic
'''

import logging

#create logger
logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)
#logger.setLevel(logging.NOTSET)  # same as WARNING
#logger.setLevel(logging.WARNING)
#logger.setLevel(logging.INFO)

#create console handler and set level to error
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

#create file handler and set level to debug
fh = logging.FileHandler("spam.log")
fh.setLevel(logging.DEBUG)

#create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
   
#add formatter to ch and fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)

#add ch and fh to logger
logger.addHandler(ch)
logger.addHandler(fh)

#"application" code
logger.debug("debug message")
logger.info("info message", html=True)
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")
