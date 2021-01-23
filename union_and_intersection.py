class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        '''Add a new node to the end of the linked list'''
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail= new_node
            return

    def size(self):
        '''Calculate the size / length of the linked list'''
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def traverse(self):
        '''Iterate through a linked list using a generator'''
        if self.head == None:
            return
        curr_node = self.head
        while curr_node:
            yield curr_node.value
            curr_node = curr_node.next

def union(llist_1, llist_2):
    '''Combine all values in two linked lists into a new linked list'''    
    new_list = LinkedList()

    my_gen1 = llist_1.traverse()
    for node in range(llist_1.size()):
        new_list.append(next(my_gen1))

    my_gen2 = llist_2.traverse()
    for node in range(llist_2.size()):
        new_list.append(next(my_gen2))

    return new_list

def intersection(llist_1, llist_2):
    '''Find the values that exist in both lists and add to a new linked list'''
    new_list = LinkedList()
    my_gen1 = llist_1.traverse()
    intersection_values = set()

    for node in range(llist_1.size()):
        llist_1_value = next(my_gen1)
        my_gen2 = llist_2.traverse()
        for node in range(llist_2.size()):
            llist_2_value = next(my_gen2)
            if llist_1_value == llist_2_value:
                intersection_values.add(llist_1_value)

    for value in intersection_values:
        new_list.append(value)

    return new_list

