"""
Call base class function from the derived class
"""

class B(object):
    def __init__(self):
        pass

    def bf(self, x):
        print("calling function f({})".format(x))


class D(B):
    def __init__(self):
        B.__init__(self)

    def df(self):
        self.bf("dragan")

d = D()
d.df()