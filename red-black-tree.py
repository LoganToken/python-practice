# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 12:22:31 2023

@author: My
"""

class Node:
    # red = True, black = False
    RED = True
    BLACK = False
    
    def __init__(self, value, color=RED):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    # red = True, black = False
    RED = True
    BLACK = False
    
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        new_node = Node(value)
        if (not self.head):
            self.head = new_node
            self.head.color = self.BLACK
        pass
    
    def left_rotate(self, node):
        if (not node.right):
            raise ValueError("Cannot perform left rotation as the node has no right child.")
        
        new_parent = node.right
        new_right_child = new_parent.left
        node.right = new_right_child
        new_parent.left = node
        return new_parent