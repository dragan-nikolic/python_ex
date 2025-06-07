"""
Created on 2025-02-25

@author: dnikolic
"""

def sort_string():
    s = 'dragan'

    ss = sorted(s)
    print(f"sorted('dragan') = {ss}")

    ssj = ''.join(ss)
    print(f"sorted(''.join(ss) = {ssj}")

def sort_strings():
    l = ['bob', 'charlie', 'alice']

    sl = sorted(l)
    print(f"sorted({l}) = {sl}")

sort_string()
sort_strings()