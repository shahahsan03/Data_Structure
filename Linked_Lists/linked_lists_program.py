# Linked Lists Program

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
    
    def viewList(self):
        if self.start is None:
            print("List is empty")
        else:
            temp = self.start
            while temp is not None:
                print(temp.data)
                temp = temp.next
    
    def insertFirst(self,val):
        newNode = Node(val)
        newNode.next=self.start
        self.start = newNode
    
    def insertLast(self,val):
        newNode = Node(val)
        if self.start is None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next is not None:
                temp= temp.next
            temp.next = newNode
    
    def deleteFirst(self):
        if self.start is None:
            print('List is Empty')
        else:
            self.start = self.start.next         
    
    def deleteLast(self):
        if self.start is None:
            print('List is Empty')
        elif self.start.next is None:
            self.start = None
        else:
            current = self.start
            while current.next.next is not None:
                current = current.next
            current.next = None      
        
            
myList = LinkedList()

print("<---Enter Choice between 1-5--->")
print("<---Enter 1 to Insert element at the First--->")
print("<---Enter 2 to Insert element at the Last--->")
print("<---Enter 3 to delete element at the First--->")
print("<---Enter 4 to delete element at the Last--->")
print("<---Enter 5 to View the List--->")
print("<---Enter 6 to Exit the program--->")


myList = LinkedList()

while True:
    ch = int(input("Enter your choice: "))

    if ch==1:
        element = input("Enter Element: ")
        myList.insertFirst(element)

    elif ch==2:
        element = input("Enter Element: ")
        myList.insertLast(element)
    
    elif ch==3:
        myList.deleteFirst()
    
    elif ch==4:
        myList.deleteLast()
    
    elif ch==5:
        myList.viewList()
    
    elif ch==6:
        print("<---Thanks for using our program.--->")
        break
    else:
        print("<---Please Enter a number between 1-5--->")