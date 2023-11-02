class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.start = None

    def insertFirst(self, val):
        newNode = Node(val)
        newNode.next = self.start
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
            print("List is empty")
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
                 
    
    def ViewList(self):
        if self.start is None:
            print("List is empty")
        else:
            temp = self.start
            while temp is not None:
                print(temp.data)
                temp  = temp.next


newList = linkedList()

newList.insertFirst(10)
newList.insertFirst(20)
newList.insertFirst(30)
newList.insertFirst(40)
newList.ViewList()
print()
newList.deleteFirst()
newList.deleteLast()
newList.deleteFirst()
newList.ViewList()