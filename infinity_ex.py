"""
Created on 2017-10-08

@author: dnikolic
"""
int_value = 5
float_value = 3.14

value = int_value
print("{}: {} > float('inf'): {}".format(type(value), value, value > float('inf')))
print("{}: {} < float('inf'): {}".format(type(value), value, value < float('inf')))
print("{}: {} > -float('inf'): {}".format(type(value), value, value > -float('inf')))
print("{}: {} < -float('inf'): {}".format(type(value), value, value < -float('inf')))

value = float_value
print("{}: {} > float('inf'): {}".format(type(value), value, value > float('inf')))
print("{}: {} < float('inf'): {}".format(type(value), value, value < float('inf')))
print("{}: {} > -float('inf'): {}".format(type(value), value, value > -float('inf')))
print("{}: {} < -float('inf'): {}".format(type(value), value, value < -float('inf')))
