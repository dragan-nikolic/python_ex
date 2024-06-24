"""
Created on 2024-06-22

@author: dnikolic
"""
import logging
import os

class Logger(logging.Logger):
  def __init__(self, name: str, logfile: str = 'myfile.log'):
    super().__init__(name, logging.NOTSET)

    c_handler = logging.StreamHandler()
    c_formatter = logging.Formatter('%(message)s')
    c_handler.setFormatter(c_formatter)
    c_handler.setLevel(logging.INFO)
    self.addHandler(c_handler)
    
    f_handler = logging.FileHandler(logfile)
    print(f'logfile path is: {os.path.abspath(logfile)}')
    f_formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s: %(message)s')
    f_handler.setFormatter(f_formatter)
    f_handler.setLevel(logging.DEBUG)
    self.addHandler(f_handler)
