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
    
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"

class Tree():
    """For this program, the Tree object is the only node in the min heap (root of the Tree) which has pointers to other nodes and values"""
    def __init__(self):
        self.root = None
        
    def set_root(self,value):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

    def get_encoded_values(self):
        """Get encoded values for each node in the tree (store in a dictionary)"""
        stack = Stack()
        visit_order = []
        node = self.get_root().get_value()[1]
        visit_order.append(node)
        state = State(node)
        stack.push(state)
        count = 0
        encoded_value = ""
        ecv = {}

        while(node):
            count += 1

            if node.has_left_child() and not state.get_visited_left():
                encoded_value += "0"
                state.set_visited_left()
                node = node.get_left_child()[1]
                if type(node) == str:
                    node = Node(node)
                visit_order.append(node.get_value())
                state = State(node)
                stack.push(state)
                ecv[node] = encoded_value

            elif node.has_right_child() and not state.get_visited_right():
                encoded_value += "1"
                state.set_visited_right()
                node = node.get_right_child()[1]
                if type(node) == str:
                    node = Node(node)
                visit_order.append(node.get_value())
                state = State(node)
                stack.push(state)
                ecv[node] = encoded_value

            else:
                stack.pop()
                if not stack.is_empty():
                    state = stack.top()
                    node = state.get_node()
                else:
                    node = None
                if ecv.get(node):
                    encoded_value = ecv[node]
                else:
                    encoded_value = ""

        return ecv

    def get_decoded_value(self, encoded_s):
        """Get the decoded string from the encoded string. The decoded string is obtained by performing a Depth First Search on the tree"""
        stack = Stack()
        node = self.get_root().get_value()[1]
        state = State(node)
        stack.push(state)
        count = 0
        decoded_s = ""
        
        while node and count < len(encoded_s):
            if encoded_s[count] == '0':
                if type(node) == str:
                    decoded_s += node
                    node = self.get_root().get_value()[1]
                if node.has_left_child(): 
                    node = node.get_left_child()[1]
                    # Handle case for the last character found from the encoded string
                    if count == len(encoded_s) - 1:
                        decoded_s += node
                    count += 1
            else: # Go to right node
                if type(node) == str:
                    decoded_s += node
                    node = self.get_root().get_value()[1]
                if node.has_right_child():    
                    node = node.get_right_child()[1]
                    # Handle case for the last character found from the encoded string
                    if count == len(encoded_s) - 1:
                        decoded_s += node
                    count += 1

        return decoded_s 

    def bfs(self):
        """Get the visit order of the tree using a Breadth First Search"""
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node.get_value()[1],level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if type(node) == str:
                q.enq( (None, level +1) )
                q.enq( (None, level +1) )
                continue
            if node.has_left_child():
                q.enq( (node.get_left_child()[1], level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child()[1], level +1 ))
            else:
                q.enq( (None, level +1) )

        return visit_order

    def print_bfs(self):
        """Take the visit order from the Breadth First Search and print out the tree"""
        visit_order = self.bfs()
        s = "Tree (from BFS)\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level
    
        return s
                      
    def __repr__(self):
        """Print the tree when an instance of the Tree object is called"""
        s = self.print_bfs()
        return s

def huffman_encoding(data):
    """Encode the sentence using Huffman Coding"""
    if data == "" or data == None:
        print("Please provide data to encode.")
        return None, None
    codes = {}
    #Create a dictionary from the sentence (characters:number of occurences)
    for letter in data:
        if codes.get(letter):
            codes[letter] += 1
        else:
            codes[letter] = 1

    #Create a min heap from the dictionary
    my_heap = MinHeap()
    for k,v in codes.items():
        my_heap.insert((v,k))

    #Remove two min values (character ) in the heap from the heap and consolidate
    for i in range(my_heap.current_size - 1):
        elem1 = my_heap.delete_min()
        elem2 = my_heap.delete_min()

        new_node = Node(elem1[0] + elem2[0])
        new_node.set_left_child(elem1)
        new_node.set_right_child(elem2)

        my_heap.insert((new_node.get_value(), new_node))

    #Remove the min value from the min heap and set as the root of the tree. This min value will be a node that has combined valued of it's child nodes. 
    root = my_heap.delete_min()
    my_tree = Tree()
    my_tree.set_root(root)

    #Get the encoded values for each character as a dictionary
    encoded_values = my_tree.get_encoded_values()
    encoded_string = ""

    #Add the encoded value to the other dictionary that contains each character and it's frequency 
    for key, value in encoded_values.items():
        if key.get_value() in codes:
            codes[key.get_value()] = (codes[key.get_value()], value)

    #Generate and return the encoded string based on the passed in sentence
    for letter in data:
        if letter in codes:
            encoded_string += codes[letter][1]

    return encoded_string, my_tree

def huffman_decoding(data,tree):
    """Decode the sentence using Huffman Coding"""
    if data == "" or data == None:
        print("Please provide data to decode.")
        return 
    if tree == None:
        print("Please provide data to decode.")
        return
    decoded_string = ""
    decoded_data = tree.get_decoded_value(data)

    return decoded_data

if __name__ == "__main__":
    #Test Case 1
    a_great_sentence1 = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence1)))
    print ("The content of the data is: {}\n".format(a_great_sentence1))

    encoded_data, tree = huffman_encoding(a_great_sentence1)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    '''
    Expected output:
    The size of the data is: 69

    The content of the data is: The bird is the word

    The size of the encoded data is: 36

    The content of the encoded data is: 0100011100111101100000111001110001101111111010011100111101001010011100

    The size of the decoded data is: 69

    The content of the decoded data is: The bird is the word
    '''
    #Test Case 2
    a_great_sentence2 = "Music is the universal language"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence2)))
    print ("The content of the data is: {}\n".format(a_great_sentence2))

    encoded_data, tree = huffman_encoding(a_great_sentence2)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    '''
    Expected output:
    The size of the data is: 80

    The content of the data is: Music is the universal language

    The size of the encoded data is: 40

    The content of the encoded data is: 110001111001111001101101111000110111001100110001011111011111101001000001100001010100010110000100111110111110101101000

    The size of the decoded data is: 80

    The content of the decoded data is: Music is the universal language
    '''
    #Test Case 3
    a_great_sentence3 = "This is a sentence with weird characters: !@#$%^&*(), 1234567890"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence3)))
    print ("The content of the data is: {}\n".format(a_great_sentence3))

    encoded_data, tree = huffman_encoding(a_great_sentence3)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    '''
    Expected output:
    The size of the data is: 113

    The content of the data is: This is a sentence with weird characters: !@#$%^&*(), 1234567890

    The size of the encoded data is: 68

    The content of the encoded data is: 011000000010101001010101010010100010010100111101101111111111011011000111100100111010101111100000100111011101010111101000000100001000000101111000100001111111110111101001100001010110100110001001100001101011010110010001111110011001110100011110000010101100101101011111100010011110110101011011101111101110011001

    The size of the decoded data is: 113

    The content of the decoded data is: This is a sentence with weird characters: !@#$%^&*(), 1234567890
    '''
    # Test Case 4 
    a_great_sentence4 = ""
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence4)))
    print ("The content of the data is: {}\n".format(a_great_sentence4))

    encoded_data, tree = huffman_encoding(a_great_sentence4)

    decoded_data = huffman_decoding(encoded_data, tree)
    '''
    The size of the data is: 49

    The content of the data is: 

    Please provide data to encode.
    Please provide data to decode.
    '''
    # Test Case 5
    a_great_sentence5 = None
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence5)))
    print ("The content of the data is: {}\n".format(a_great_sentence5))

    encoded_data, tree = huffman_encoding(a_great_sentence5)

    decoded_data = huffman_decoding(encoded_data, tree)
    '''
    The size of the data is: 16

    The content of the data is: None

    Please provide data to encode.
    Please provide data to decode.
    '''