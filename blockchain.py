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

    def append(self, data=''):
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

if __name__ == "__main__":

    bc = Blockchain()
    #Test Cases 1-. The time will vary as to when this is run. I believe the hash values will vary as well. 
    bc.append('123xyz')
    bc.append('321zyx')
    bc.append()
    bc.append('456stu')
    bc.append('654uts')
    bc.print()
    '''
    Expected output (example):
    06:18:53 31 Jan 2021 UTC, 123xyz, 0, 6a6cd536035e87176af9fce1b91cf9c9e2ba665c8f28df77135db881b388387b
    06:18:53 31 Jan 2021 UTC, 321zyx, 6a6cd536035e87176af9fce1b91cf9c9e2ba665c8f28df77135db881b388387b, 2ad78df58fdb5d7d79b5dab31573e23be70ebafa4b8139984564778cfab8c8be
    06:18:53 31 Jan 2021 UTC, , 2ad78df58fdb5d7d79b5dab31573e23be70ebafa4b8139984564778cfab8c8be, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    06:18:53 31 Jan 2021 UTC, 456stu, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855, be66970dfa2e7fe733817d26ed948b2cc00cfb92ce4794a4bf3265ef0739449a
    06:18:53 31 Jan 2021 UTC, 654uts, be66970dfa2e7fe733817d26ed948b2cc00cfb92ce4794a4bf3265ef0739449a, cfcf44387f35b60539b2ee8f4759e081b71595727cd3e7d95f782589588eec9f
    '''