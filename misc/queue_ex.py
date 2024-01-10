"""
Created on 2017-09-13

@author: dnikolic

The best is to use 'collections.deque' Python 'list' supports opperations but is much
less efficient (https://stackoverflow.com/questions/1296511/efficiency-of-using-a-python-list-as-a-queue)
"""
import collections
from queue import PriorityQueue

def print_queue(_q, message):
    print(message)
    for item in _q:
        print(item)

def demo_deque():
    q = collections.deque([2])
    print_queue(q, 'initial')

    q.append(3)
    q.append(1)
    print_queue(q, 'after adding 3 and 1')

    q.popleft()
    print_queue(q, 'after removing first element')

def demo_priority_queue():
    pq = PriorityQueue()
    pq.put('t')
    pq.put('c')
    pq.put('x')
    print("PQ size is {}".format(pq.qsize()))
    print("smallest element is {}".format(pq.get()))
    print("PQ size is {}".format(pq.qsize()))

#demo_deque()
demo_priority_queue()