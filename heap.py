# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 09:46:01 2023

@author: My
"""

# This will be a max heap
class Heap:
    def __init__(self):
        self.list = []
        
    def insert(self, value):
        index = len(self.list)
        self.list.append(value)
        self.heapify_up(index)
    
    def delete(self, index):
        self.swap_nodes(index, len(self.list) - 1)
        self.list.pop()
        self.heapify_down(index)
    
    def heapify_up(self, index):
        if (index <= 0):
            return
        
        parent_index = self.get_parent_index(index)
        val = self.list[index]
        parent_val = self.list[parent_index]
        if (parent_val > val):
            return
        elif (parent_val < val):
            self.swap_nodes(index, parent_index)
            return self.heapify_up(parent_index)
        else:
            raise "comparison error"
    
    def heapify_down(self, index):
        # if no children
        if (len(self.list) < 2*index + 2):
            return 
        
        child1, child2 = self.get_child_indices(index)
        # if one child
        if (child2 >= len(self.list)):
            self.swap_nodes(index, child1)
            return
        
        child1_val = self.list[child1]
        child2_val = self.list[child2]
        target_child = child1
        # target the larger child
        if (child2_val > child1_val):
            target_child = child2
        target_val = self.list[target_child]
        if (target_val > self.list[index]):
            self.swap_nodes(index, target_child)
            self.heapify_down(target_child)
        return
    
    def get_parent_index(self, index):
        return (index - 1) // 2
    
    def swap_nodes(self, index1, index2):
        val1 = self.list[index1]
        val2 = self.list[index2]
        self.list[index1] = val2
        self.list[index2] = val1
        
    def get_child_indices(self, index):
        return (2*index + 1, 2*index + 2)

heap = Heap()
heap.insert(5)
heap.insert(3)
heap.insert(7)
heap.insert(1)
heap.insert(12)
heap.insert(4)
heap.insert(55)
heap.insert(0)
heap.insert(19)
heap.insert(222)
print(heap.list)
heap.list[0] = -1
heap.heapify_down(0)
print(heap.list)
heap.delete(0)
print(heap.list)
