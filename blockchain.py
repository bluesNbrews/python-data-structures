import hashlib
from time import gmtime, strftime
import time

class Block(object):

    def __init__(self, data='', previous_hash=0):
        # Initialize class variables
        self.timestamp = time.strftime("%I:%M:%S %d %b %Y %Z", time.gmtime())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)
        self.next = None

    def calc_hash(self, data):
        '''Calculate SHA-256 hash for the Greenwich Mean Time when the block was created, and text strings as the data.'''
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __str__(self):
       '''Return attribute values as a string for Block object'''
       return "{}, {}, {}, {}".format(self.timestamp, self.data, self.previous_hash, self.hash)

class Blockchain(object):

    def __init__(self):
        # Initialize class variables
        self.head = None
        self.tail = None

    def append(self, data):
        '''Add a new block to the end of the Blockchain'''
        if self.head == None:
            self.head = Block(data)
            self.tail = self.head
            return
        else:
            new_block = Block(data)
            self.tail.next = new_block
            new_block.previous_hash = self.tail.hash
            self.tail = new_block
            return 

    def print(self):
        '''Iterate through the entire Blockchain (starting with the head) and print the attribute values'''    
        if self.head == None:
            return
        curr_node = self.head
        while curr_node:
            print(curr_node)
            curr_node = curr_node.next