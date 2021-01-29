import sys
from collections import deque

class MinHeap:
    def __init__(self):
        #Using nodes - either tuples (number of occurences, character) or multiple tuple values - ex: (2, h) and (1, w) or 3
        self.heap_list = [0]
        self.current_size = 0

    def sift_up(self, i):
        """Move the value to its appropriate position in the min heap (following the definition of a min heap)"""
        #While the element is not the min value (top) or the second value in the min heap
        while i // 2 > 0:
            # Swap the values if the current value is less than it's parent value
            if self.heap_list[i][0] < self.heap_list[i // 2][0]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
                # Move the index to the parent value (moving up the tree)
            i = i // 2

    def insert(self, k):
        """Add a new value to the min heap"""
        #Append the element to the min heap
        self.heap_list.append(k)
        #Increase the size of the min heap
        self.current_size += 1
        #Move the value to its appropriate position in the min heap (following the definition of a min heap)
        self.sift_up(self.current_size)

    def sift_down(self, i):
        """Move the passed in value to it's appropriate position in the min heap"""
        #If the current value has at least one child
        while (i * 2) <= self.current_size:
            #For the current value, get the index of the child with the least value (min child)
            mc = self.min_child(i)
            # If the current value is greater than it's "min child" value, swap the values
            if self.heap_list[i][0] > self.heap_list[mc][0]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        """Get the index of the child with the least value"""
        # If the current node only has one child, return the index of the unique child
        if (i * 2) + 1 > self.current_size:
            return i * 2
        else:
            # Herein the current node has two children
            # Return the index of the min child according to their values
            if self.heap_list[i * 2][0] < self.heap_list[(i * 2) + 1][0]:
                return i * 2
            else:
                return (i * 2) + 1

    def delete_min(self):
        """Return and remove the min value from the heap"""
        #The length is 1 because the heap list was initialized with 0
        if len(self.heap_list) == 1:
            return "Empty heap."

        #Store the min value of the heap
        top = self.heap_list[1]

        #Move the last value of the heap to the top
        self.heap_list[1] = self.heap_list[self.current_size]

        #Pop the last value from the heap (that was moved to the top)
        *self.heap_list, _ = self.heap_list

        # Decrease the size of the heap
        self.current_size -= 1

        #Move down the top value to the appropriate position (following the definition of a min heap)
        #The value is at index 1 since the heap list was initialized with 0) 
        self.sift_down(1)

        #Return the min value of the heap
        return top

    #Print the min heap as a string
    def __repr__(self):
        return str(self.heap_list)

class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"

class State(object):
    def __init__(self,node):
        self.node = node
        self.visited_left = False
        self.visited_right = False
        
    def get_node(self):
        return self.node
    
    def get_visited_left(self):
        return self.visited_left
    
    def get_visited_right(self):
        return self.visited_right
    
    def set_visited_left(self):
        self.visited_left = True
        
    def set_visited_right(self):
        self.visited_right = True
        
    def __repr__(self):
        s = f"""{self.node} visited_left: {self.visited_left} visited_right: {self.visited_right}"""
        return s

class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

class Node(object):
        
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"

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

    