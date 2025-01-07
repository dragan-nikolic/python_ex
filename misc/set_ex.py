"""
Created on 2025-01-07

@author: dnikolic
"""

def access_set_elements():
    myset = {'a', 'b', 'c', 'd', 'e'}

    print(f'set is {myset}')
    print(f'len(myset) = {len(myset)}')

    print('set elements')
    for e in myset:
        print(f'element: {e}')

def join_using_union():
    s1 = set(('a', 'b', 'c'))
    s2 = set(('d', 'e', 'c'))
    print(f's1: {s1}')
    print(f's2: {s2}')

    s3 = s1.union(s2)

    print(f's3 is combined: {s3}')
    print(f's1 is unchanged: {s1}')

def join_using_update():
    s1 = set(('a', 'b', 'c'))
    s2 = set(('d', 'e', 'c'))
    print(f's1: {s1}')
    print(f's2: {s2}')

    s1.update(s2)

    print(f's1 is changed: {s1}')

if __name__ == '__main__':
    access_set_elements()
    join_using_union()
    join_using_update()