# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:21:02 2023

@author: My
"""

from collections import defaultdict
import math

class Node:
    
    def __init__(self, char=None, probability=0):
        self.char = char
        self.zero = None
        self.one = None
        self.probability = probability
        
class Tree:
    
    def __init__(self, root=None):
        self.root = root

def make_frequency_dictionary(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    return frequency

def make_node_list(frequency, total):
    node_list = []
    for key in frequency:
        probability = frequency[key]/total
        node = Node(char=key, probability=probability)
        node_list.append(node)
    return node_list

def make_hamming_tree(text):
    frequency = make_frequency_dictionary(text)
    node_list = make_node_list(frequency, len(text))
    while len(node_list) >= 2:
        node_list.sort(key = lambda x: x.probability, reverse=True)
        node_zero = node_list.pop()
        node_one = node_list.pop()
        total_probability = node_zero.probability + node_one.probability
        parent_node = Node(probability=total_probability)
        parent_node.zero = node_zero
        parent_node.one = node_one
        node_list.append(parent_node)
    return node_list[0]

def make_hamming_map(hamming_tree):
    char_to_bin = {}
    bin_to_char = {}
    
    def dfs(node, bin_string):
        if node.char:
            char_to_bin[node.char] = bin_string
            bin_to_char[bin_string] = node.char
            return
        zero_string = bin_string + '0'
        dfs(node.zero, zero_string)
        one_string = bin_string + '1'
        dfs(node.one, one_string)
    
    dfs(hamming_tree, '')
    return char_to_bin, bin_to_char

def hamming_encode(text):
    hamming_tree = make_hamming_tree(text)
    encoder, decoder = make_hamming_map(hamming_tree)
    message = ''
    for char in text:
        message += encoder[char]
    return message, decoder

def hamming_decode(message, decoder):
    decoded_message = ''
    index = 0
    code = ''
    while index < len(message):
        code += message[index]
        if code in decoder:
            decoded_message += decoder[code]
            code = ''   
        index += 1
    return decoded_message

def calculate_entropy(text):
    frequency = make_frequency_dictionary(text)
    node_list = make_node_list(frequency, len(text))
    entropy = 0
    for node in node_list:
        entropy += node.probability * math.log2(1 / node.probability)
    return entropy

def calculate_bits_required(number):
    return math.ceil(math.log2(number))

def analyze_efficiency(text):
    entropy = calculate_entropy(text)
    theoretical_min = math.ceil(entropy * len(text))
    message, decoder = hamming_encode(text)
    hamming_length = len(message)
    num_unique_chars = len(decoder)
    num_fixed_length_bits = calculate_bits_required(num_unique_chars)
    fixed_length_total = num_fixed_length_bits * len(text)
    print(f"""
          Text: {text}\n
          Fixed length encoding length: {fixed_length_total}\n
          Entropy Minimum: {theoretical_min}\n
          Hamming Length: {hamming_length}\n
          """)
        
        

text = "peter piper picked a patch of pickled peppers"

analyze_efficiency(text)
        