"""
Created on 2012-12-12

Execute this test 2 times.


@author: dnikolic
"""

import os
from subprocess import call
from time import sleep

def get_envvar(var_name):
    return os.environ[var_name]
    
def set_envvar(var_name, var_value):
    os.environ[var_name] = var_value
    
ENVVAR_NAME = 'PCOIP_TYPE'
ENVVAR_VALUE = 'Zero Client'

TEMPFILE = 'envvartesttemp'

def test_envvar():
    # check if ENVVAR_NAME variable is defined
    if ENVVAR_NAME in os.environ:
        print '%s is defined!' % ENVVAR_NAME
    else:
        print '%s is NOT defined!' % ENVVAR_NAME
        
        # define ENVVAR_NAME
        os.environ[ENVVAR_NAME] = ENVVAR_VALUE
        
    # check again if ENVVAR_NAME variable is defined
    if ENVVAR_NAME in os.environ:
        print '%s is defined!' % ENVVAR_NAME
    else:
        print '%s is NOT defined!' % ENVVAR_NAME
       
    # pause to be able to see output from 'start cmd /C' call (see below, this is recursive)
    sleep(2)

    if os.path.exists(TEMPFILE) is False:
        f = open(TEMPFILE, 'wb')
        f.write('\0')
        f.close()
        
        call('python envvars.py')
        call('start cmd /C python envvars.py', shell=True)
        
        # pause longer then first pause before deleting file, otherwise 'start cmd /C' call goes into endless loop
        sleep(3)
        os.remove(TEMPFILE)
        

    
if __name__ == '__main__':
    test_envvar()
