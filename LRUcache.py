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
		'''Insert new node at the front of the list (as the Most Recently Used item in the cache)'''
		if self.head == None:
			self.head = Double_Node(value)
			self.tail = self.head
			return
		else:
			new_node = Double_Node(value)
			new_node.next = self.head
			self.head.prev = new_node
			new_node.prev = None
			self.head = new_node
			return

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