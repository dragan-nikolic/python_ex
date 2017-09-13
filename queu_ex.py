"""
Created on 2017-09-13

@author: dnikolic
"""
import collections

def print_queue(_q, message):
    print(message)
    for item in _q:
        print(item)

q = collections.deque([1])
print_queue(q, 'initial')

q.append(2)
q.append(3)
print_queue(q, 'after adding 2 and 3')

q.popleft()
print_queue(q, 'after removing 1')
