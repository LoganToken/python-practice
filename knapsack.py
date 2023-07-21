# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:25:10 2023

@author: My
"""
import random
import math

def generate_knapsack_problem(num_items = 10, max_weight = 100, max_value = 100):
    items = []
    total_weight = 0
    for i in range(num_items):
        weight = random.randint(1, max_weight)
        value = random.randint(1, max_value)
        items.append((i, weight, value))
        total_weight += weight
    
    # make knapsack hold between 30% and 70% of total weight
    fraction = random.uniform(0.3, 0.7)
    knapsack_capacity = math.floor(fraction * total_weight)
    
    return items, knapsack_capacity

def solve_knapsack(items, capacity):
    max_values = [0] * (capacity + 1)
    for item in items:
        _, item_weight, value = item
        for weight in range(capacity, item_weight - 1, -1):
            best_possible = value + max_values[weight - item_weight]
            max_values[weight] = max(max_values[weight], best_possible)
    return max_values[capacity]

items, capacity = generate_knapsack_problem(1000, 100, 100)
#print(items)
print(capacity)
print(solve_knapsack(items, capacity))
    
    
    
    