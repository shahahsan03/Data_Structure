class DoublyLinkedLists:
    def __init__(self, data):
       self.previous = None
       self.data = data 
       self.next = None
    
a = DoublyLinkedLists(10)
b = DoublyLinkedLists(20)
c = DoublyLinkedLists(30)


b.previous = a
b.next = c

c.previous = b
a.next = b

print()