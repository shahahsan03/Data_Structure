class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
        
class doubleLinkedList:
    def __init__(self):
        self.start = None
    
    def InsertToFirst(self, val):
        newNode = Node(val)
        newNode.next = self.start
        self.start = newNode          

    def InsertToEnd(self, val):
        if self.start is None:
            newNode = Node(val)
            self.start = newNode
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            newNode = Node(val)
            temp.next = newNode
            newNode.prev = temp
            
    def deleteAtFirst(self):
        if self.start is None:
            print('Linked List is empty, no element to delete.')
        elif self.start.next is None:
            self.start = None
        else:
            self.start = self.start.next
            self.start.prev = None
    
    def deleteAtLast(self):
        if self.start is None:
            print('Linked List is empty, no element to delete')
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start   
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def viewListForward(self):
        if self.start is None:
            print('List is empty')
        else:
            temp = self.start
            while temp is not None:
                print(temp.data)
                temp = temp.next
    
    def viewListBackward(self):
        if self.start is None:
            print('List is empty')
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next

            while temp is not None:
                print(temp.data)
                temp = temp.prev

print("--Please type the value of choice from 1-7--")
print("1 <-- Insert an Element to Start")
print("2 <-- Insert an Element to End")
print("3 <-- Delete an Element at Start")
print("4 <-- Delete an Element at End")
print("5 <-- View List Forward")
print("6 <-- View List Backward")
print("7 <-- Exit Program")

newList = doubleLinkedList()

while True:
    choice = int(input("Enter Choice: "))
    if choice == 1:
        val = input("Enter an Elment to Start: ")
        newList.InsertToFirst(val)
    elif choice == 2:
        val = input("Enter an Elment to End: ")
        newList.InsertToEnd(val)
    elif choice == 3:
        newList.deleteAtFirst()
    elif choice == 4:
        newList.deleteAtLast()
    elif choice == 5:
        newList.viewListForward()
    elif choice == 6:
        newList.viewListBackward()
    elif choice == 7:
        print('Thanks for using our program')
        break
    else:
        print("Please Enter Choice between 1-6")
