"""
How to use *args and **kwargs in Python
Created on 2012-08-11

Examples from http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/

@author: dnikolic
"""


def test_var_args(farg, *args):
    print("formal arg:", farg)
    print(args)
    if args:
        for arg in args:
            print("another arg:", arg)
    else:
        print('no extra arguments provided!')

def test_var_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    print('keyword arg myarg2:', kwargs['myarg2'])
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))

def simple_function(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

def test_call_simple_function_using_args1():
    print("test f(*(a1, a2, a3))")
    args = (1, "two", 3)
    simple_function(*args)
    simple_function(*(1, "two", 3))

def test_call_simple_function_using_args2():
    print("test f(a1, *(a2, a3))")
    args = ("two", 3)
    simple_function(1, *args)

def test_call_simple_function_using_kwargs():
    kwargs = {"arg3": 3, "arg2": "two"}
    simple_function(1, **kwargs)

def test_using_kwargs(**kwargs):
    """
    This function except argument 'arg1'
    """
    print('arg1: ', kwargs['arg1'])

if __name__ == '__main__':
    test_var_args(1, "two", 3)
    test_var_args(2)
    
    test_var_kwargs(farg=1, myarg2="two", myarg3=3)
    test_var_kwargs(2, myarg2="two", myarg3=3)

    test_call_simple_function_using_args1()
    test_call_simple_function_using_args2()
    test_call_simple_function_using_kwargs()
    
    test_using_kwargs(arg1='i am arg1')
    
    pass
