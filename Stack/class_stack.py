class Stack:
    
    def __init__(self):
        self.items = []
    
    def pushing(self, item):
        self.items.append(item)
        print(f'{item} <-- Push Item')

    def popping(self):
        if len(self.items)==0:
            print('Stack is Empty')
        else:
            print(f'{self.items.pop()} <-- Pop Element')
        
    def peek(self):
        if len(self.items)==0:
            print('Stack is Empty')
        else:
            print(self.items[-1])
            
    def display(self):
        if len(self.items)==0:
            print('Stack is empty')
        else:
            print(self.items)
            

stack = Stack()



while True:
    choice = int(input("Enter Value Between 1-5: "))

    if choice == 1:
        value = input("Enter Value: ")
        stack.pushing(value)
    elif choice == 2:
        stack.popping()
    elif choice == 3:
        stack.peek()
    elif choice == 4:
        stack.display()
    elif choice == 5:
        break