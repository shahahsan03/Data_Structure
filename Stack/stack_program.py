# Stack Program

def is_empty(stack):
    if len(stack)==0:
        print("Stack is Empty!")
    else:
        print("Stack is not Empty")

def pushing(stack, item):
    stack.append(item)
    print(f"{item} <-- Added Item")

def popping(stack):
    if len(stack)==0:
        print('Stack is Empty')
    else:
        print(f"{stack.pop()}  <-- Deleted Item")

def peek(stack):
    if len(stack)==0:
        print("Stack is empty")
    else:
        print(f"{stack[-1]} <-- Top Item")

def display(stack):
    print(stack)

# Main_Function
stack = []
print("--Please type the value of choice from 1-6--")
print("1 <-- Add Item")
print("2 <-- Delete Item")
print("3 <-- Top Item")
print("4 <-- Display all items")
print("5 <-- Check if Stack is empty")
print("6 <-- Exit Program")

while True:
    ch = int(input("Enter Your Choice: "))
    if ch==1:
        val = input("Enter a value: ")
        pushing(stack,val)
    elif ch==2:
        popping(stack)
    elif ch==3:
        peek(stack)
    elif ch==4:
        display(stack)
    elif ch==5:
        is_empty(stack)
    elif ch==6:
        print("Thanks for using our program.")
        break
    else:
        print("Please Enter Value between 1-5")

