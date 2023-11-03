class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linked_Lists:
    
    def __init__(self):
        self.start = None
        
    def insertFirst(self, val):
        newNode=Node(val)
        newNode.next = self.start
        print(newNode.next)
        self.start = newNode
        
    def insertLast(self,val):
        newNode = Node(val)
        if self.start is None:
            self.start = newNode
        elif self.start.next is None:
            self.start.next = newNode
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    
    def deleteFirst(self):
        if self.start is None:
            print("List is empty!")
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
            
    def viewList(self):
        if self.start is None:
            print('List is empty')
        else:
            temp = self.start
            while temp is not None:
                print(temp.data)
                temp=temp.next


print("<---Enter Choice between 1-6--->")
print("<---Enter 1 to Insert element at the start--->")
print("<---Enter 2 to Insert element at the Last--->")
print("<---Enter 3 to Erase the element at the start--->")
print("<---Enter 4 to Erase element at the Last--->")
print("<---Enter 5 to View the List--->")
print("<---Enter 6 to Exit the program--->")     
            
my_list = Linked_Lists()      

while True:
    choice = int(input("Enter Choice: "))
    if choice == 1:
        val = input("Enter value to insert in First: ")
        my_list.insertFirst(val)
        print(f"<---The value '{val}' has been added at the start of the list--->")
    elif choice == 2:
        val = input("Enter a value to insert in Last: ")
        my_list.insertLast(val)
        print(f"<---The value '{val}' has been added at the last of the list--->")
    elif choice == 3:
        my_list.deleteFirst()
    elif choice == 4:
        my_list.deleteLast()
    elif choice == 5:
        my_list.viewList()
    elif choice == 6:
        print("<---Thanks for using our program.--->")
        break
    else:
        print("Please Enter choice between 1-6")