# Linked lists are an ordered collection of objects. So what makes them different from normal lists? Linked lists differ from lists in the way that they store elements in memory. While lists use a contiguous memory block to store references to their data, linked lists store references as part of their own elements.

# ---------------------------------------------------------------

# Q: Why we use linked list rather than array?
# Ans: A linked list consists of a sequence of nodes, each containing a value and a pointer to the next node in the list. This makes linked lists more flexible than arrays, as they can be easily resized and modified without needing to move large amounts of data around.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
        
    def view(self):
        if self.start is None:
            print("List is empty")
        else:
            temp = self.start
            while temp is not None:
                print(temp.data)
                temp=temp.next
            
    def insertFirst(self, val):
        newNode = Node(val)
        newNode.next=self.start
        self.start = newNode
            
    def insertLast(self, val):
        newNode = Node(val)
        if self.start is None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
        
    def deleteFirst(self):
        if self.start is None:
            print("List is empty")        
        else:
            self.start = self.start.next
        
    def deleteLast(self):
        if self.start is None:
            print("List is Empty")
        elif self.start.next is None:
            self.start = None
        else:
            current = self.start
            while current.next.next is not None:
                current = current.next
            current.next = None


mylist = LinkedList()

print("View before deletion")
mylist.insertFirst(10)
mylist.insertFirst(20)
mylist.insertFirst(40)
mylist.insertFirst(30)
mylist.view()

print("View after deletion")
# mylist.deleteFirst()
# mylist.deleteLast()
# mylist.deleteLast()
mylist.view()

