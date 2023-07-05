# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 08:56:25 2023

@author: My
"""

class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def prepend(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        # if the linked list is empty
        if (not self.tail):
            self.tail = new_node
    
    def append(self, data):
        new_node = Node(data, None)
        
        # if the linked list is empty
        if (not self.tail):
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next_node = new_node
        self.tail = new_node
    
    def find(self, data):
        current_node = self.head
        
        while(current_node):
            if (current_node.data == data):
                return current_node
            else:
                current_node = current_node.next_node
        
        # if the data is not found
        return None
    
    def delete_head(self):
        if (not self.head):
            return
        
        # if theres only one node
        if (not self.head.next_node):
            self.head = None
            self.tail = None
            return
        
        self.head = self.head.next_node
        
    def to_list(self):
        new_list = []
        current_node = self.head
        
        while (current_node):
            new_list.append(current_node.data)
            current_node = current_node.next_node
        
        return new_list
    

test = LinkedList()
test.append(5)
test.append(12)
test.prepend(4)
print(test.to_list())
print(test.find(4))
print(test.find(8))

        
        
        
        
        
        
        
    
        