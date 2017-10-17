"""
Passa rgs by reference or by value
Created on 2017-10-01

@author: dnikolic
"""

def foo(x, y):
    x = y

def simple_arg():
    print('simple arg cannot be passed by ref')
    u = 5
    foo(u, 3)
    print('u={}'.format(u))

def goo(x, y):
    x[0] = y

def list_arg():
    print('list arg can be passed by ref')
    u = [5]
    goo(u, 3)
    print('u={}'.format(u))


simple_arg()
list_arg()