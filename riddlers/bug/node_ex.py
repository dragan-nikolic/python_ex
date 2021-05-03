#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, name, parent=None):
        self.children = []
        self.name = name
        self.parent = parent
        if parent is not None:
            parent.children.append(self)
    
    def __str__(self):
        return self.name

def printer(node, level=0):
    print("  "*level + "|- " + node.name)
    for child in node.children:
        printer(child, level+1)

root = Node("Root")
node1 = Node("1",root)
node11 = Node("1-1", node1)
node12 = Node("1-2", node1)
node13 = Node("1-3", node1)
node14 = Node("1-4", node1)
node15 = Node("1-5", node1)
node2 = Node("2",root)
node21 = Node("2-1", node2)
node22 = Node("2-2", node2)
node23 = Node("2-3", node2)
node24 = Node("2-4", node2)
node25 = Node("2-5", node2)

printer(root)
