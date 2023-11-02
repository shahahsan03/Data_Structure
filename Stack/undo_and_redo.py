def pushing(stack, val):
    stack.append(val)
    print(stack)    

def undo(stack, redo_stack):
    if len(stack)==0:
        print("No more actions to undo")
    else:
        redo_stack.append(stack.pop())
        print(stack)

def redo(stack, redo_stack):
    if len(redo_stack)==0:
        print("No moew actions to redo")
    else:
        stack.append(redo_stack.pop())
        print(stack)

# Main_Function

stack = []
redo_stack = []

print("--Please type the value of choice from 1-4--")
print("1 <-- Push Item")
print("2 <-- Undo")
print("3 <-- Redo")
print("4 <-- Exit")

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        val = input("Enter value: ")
        pushing(stack, val)
    elif choice == 2:
        undo(stack,redo_stack)
    elif choice == 3:
        redo(stack, redo_stack)
    elif choice == 4:
        print("---Thanks for using our program---")
        break
    else:
        print("---Enter a value between 1-4---")