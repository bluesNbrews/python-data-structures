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
		'''The main priority here is to remove a pointer to the tail (which is the Least Recently Used item in the cache)'''
		if self.tail == self.head:
			return
		new_tail = self.tail.prev
		self.tail.prev.next = None
		self.tail.prev = None
		self.tail = new_tail

	def get_LRU_value(self):
		'''Return the value of the Least Recently Used item in the cache'''
		if self.tail.value:
			return self.tail.value

	def update(self, value):
		'''Update the position of an item to be the Most Recently Used in the cache'''
		if self.head == None:
			return
		curr_node = self.head
		if curr_node.value == value:
			return
		while curr_node:
			if curr_node.value == value:
				if curr_node == self.tail:
					self.remove_LRU_item()
					self.prepend(value)
				else:
					curr_node.prev.next = curr_node.next
					curr_node.next.prev = curr_node.prev
					curr_node.next = self.head
					self.head.prev = curr_node
					curr_node.prev = None
					self.head = curr_node
					return 
			curr_node = curr_node.next

	def print(self):
		'''Iterate through the items and print'''
		if self.head == None:
			return
		curr_node = self.head
		while curr_node:
			print(curr_node.value)
			curr_node = curr_node.next

class LRU_Cache(object):

	def __init__(self, capacity=10):
		# Initialize class variables
		self.capacity = capacity
		self.hash_map = {}
		self.doubly_ll = Doubly_Linked_List()

	def get(self, key):
		'''Retrieve item provided key. Return -1 if nonexistent.'''
		if self.hash_map.get(key):
			#Update the item to be the Most Recently Used
			self.doubly_ll.update(self.hash_map[key])
			if len(self.hash_map) < self.capacity:
				print(self.hash_map[key])
				return self.hash_map[key]
		else:
			print("{} is not present in the cache.".format(key))
			return -1

	def set(self, key, value):
		'''Set the value if the key is not present in the cache. If the cache is at capacity, remove the oldest item.''' 
		if len(self.hash_map) < self.capacity and not self.hash_map.get(key):
			self.hash_map[key] = value
			self.doubly_ll.prepend(value)
		else:
			#For a full hash map, first iterate through the hash map to find the corresponding key and delete both key and value from hash map.
			for k,v in self.hash_map.items():
				if v == self.doubly_ll.get_LRU_value():
					remove_key = k
			del self.hash_map[remove_key]
			#Second, remove the LRU item in the list and then add the new desired node & key / item pair.
			self.doubly_ll.remove_LRU_item()
			self.doubly_ll.prepend(value)
			self.hash_map[key] = value
			return

def main():
	pass