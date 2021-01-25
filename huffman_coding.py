import sys
from collections import deque

class MinHeap:
    def __init__(self):
        #Using nodes - either tuples (number of occurences, character) or multiple tuple values - ex: (2, h) and (1, w) or 3
        self.heap_list = [0]
        self.current_size = 0

    def sift_up(self, i):
        pass

    def insert(self, k):
        pass

    def sift_down(self, i):
        pass

    def min_child(self, i):
        pass

    def delete_min(self):
        pass

    #Print the min heap as a string
    def __repr__(self):
        return str(self.heap_list)

class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        pass
        
    def pop(self):
        pass
        
    def top(self):
        pass
        
    def is_empty(self):
        pass
    
    def __repr__(self):
        pass

class State(object):
    def __init__(self,node):
        self.node = node
        self.visited_left = False
        self.visited_right = False
        
    def get_node(self):
        pass
    
    def get_visited_left(self):
        pass
    
    def get_visited_right(self):
        pass
    
    def set_visited_left(self):
        pass
        
    def set_visited_right(self):
        pass
        
    def __repr__(self):
        pass

class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        pass
        
    def deq(self):
        pass
    
    def __len__(self):
        pass
    
    def __repr__(self):
        pass

class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        pass
        
    def get_value(self):
        pass
        
    def set_left_child(self,left):
        pass
        
    def set_right_child(self, right):
        pass
        
    def get_left_child(self):
        pass
    
    def get_right_child(self):
        pass

    def has_left_child(self):
        pass
    
    def has_right_child(self):
        pass
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        pass
    
    def __str__(self):
        pass

class Tree():
    def __init__(self):
        self.root = None
        
    def set_root(self,value):
        pass
        
    def get_root(self):
        pass

    def pre_order_dfs(self):
        pass

    def print_dfs(self):
        pass

    def bfs(self):
        pass

    def print_bfs(self):
        pass
    
        return s
                        
    def __repr__(self):
        pass

def huffman_encoding(data):
    pass

def huffman_decoding(data,tree):
    pass

def print_tree(node):
    pass

if __name__ == "__main__":
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    #encoded_data, tree = huffman_encoding(a_great_sentence)

    #print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #print ("The content of the encoded data is: {}\n".format(encoded_data))

    #decoded_data = huffman_decoding(encoded_data, tree)

    #print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #print ("The content of the encoded data is: {}\n".format(decoded_data))

    