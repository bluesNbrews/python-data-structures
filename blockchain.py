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
        pass

    def print(self):
        pass