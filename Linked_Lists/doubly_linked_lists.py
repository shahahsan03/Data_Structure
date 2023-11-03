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

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

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