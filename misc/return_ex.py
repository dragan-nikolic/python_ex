"""
Created on 2024-03-23

@author: dnikolic
"""

def return_two_values():    
    return_value =  'first_arg::second_arg'.split('::')
    print(return_value)
    return return_value

x, y = return_two_values()
print(x)
print(y)
