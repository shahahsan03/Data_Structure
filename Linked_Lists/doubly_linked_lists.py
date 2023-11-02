class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
# The append function is used to add a new node with the given data to the end of the doubly linked list.
# It starts by creating a new node, new_node, with the provided data.

# If the list is empty (both self.head and self.tail are None), it sets both self.head and self.tail to the new node. This is because in an empty list, the new node becomes both the head and the tail.

# If the list is not empty, it updates the references:
# new_node.prev is set to the current tail, which establishes the previous node's reference to the new node.
# self.tail.next is set to the new node, connecting the current tail to the new node.

# Finally, it updates self.tail to point to the new node, making the new node the new tail of the list.

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

# The prepend function is used to add a new node with the given data to the beginning of the doubly linked list.

# Similar to the append function, it starts by creating a new node, new_node, with the provided data.

# If the list is empty (both self.head and self.tail are None), it sets both self.head and self.tail to the new node. In an empty list, the new node becomes both the head and the tail.

# If the list is not empty, it updates the references:

# new_node.next is set to the current head, which establishes the new node's reference to the old head.
# self.head.prev is set to the new node, connecting the old head to the new node.

# Finally, it updates self.head to point to the new node, making the new node the new head of the list.

    def display_forward(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


    def display_backward(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev

dll = DoublyLinkedList()
dll.append(3)
dll.append(1)
dll.append(2)
dll.prepend(5)
print('Display Forward')
dll.display_forward()
print('Display Backward')
dll.display_backward()

# null <- prev | data | next -> null
#                |      |
#                V      V
#            prev | data | next
#                |      |
#                V      V
#            prev | data | next
#                |      |
#                V      V
#            prev | data | next
#                |      |
#                V      V
#           null <- prev | data | next -> null