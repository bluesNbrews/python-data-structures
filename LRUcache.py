class Double_Node(object):

	def __init__(self, value=None):
		# Initialize class variables
		self.value = value
		self.next = None
		self.prev = None

class Doubly_Linked_List(object):

	def __init__(self):
		# Initialize class variables
		self.head = None
		self.tail = None

	def prepend(self, value):
		pass

	def remove_LRU_item(self):
		pass

	def get_LRU_value(self):
		pass

	def update(self, value):
		pass

	def print(self):
		pass

class LRU_Cache(object):

	def __init__(self, capacity=10):
		# Initialize class variables
		self.capacity = capacity
		self.hash_map = {}
		self.doubly_ll = Doubly_Linked_List()

	def get(self, key):
		pass

	def set(self, key, value):
		pass

def main():
	pass