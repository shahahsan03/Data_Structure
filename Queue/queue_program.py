# Queue Program

from collections import deque

def is_empty(queue):
    if len(queue)==0:
        print("Queue is empty")
    else:
        print("Queue is not empty")

def enqueue(queue, val):
    queue.append(val)
    print(val)

def dequeue(queue):
    if len(queue)==0:
        print("Queue is Empty")
    else:
        print(queue.popleft())

def display(queue):
    print(queue)

queue = deque()

print("--Please type the value of choice from 1-5--")
print("1 <-- Add Item")
print("2 <-- Delete Item")
print("3 <-- Display all items")
print("4 <-- Check if Queue is empty")
print("5 <-- Exit Program")

while True:
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        val = input("Enter value here: ")
        enqueue(queue, val)
    elif choice == 2:
        dequeue(queue)
    elif choice == 3:
        display(queue)
    elif choice == 4:
        is_empty(queue)
    elif choice == 5:
        print("Thanks for using our program.")
        break
    else:
        print("Please Enter number between 1-5")
