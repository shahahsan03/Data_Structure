# Stack:
# A stack is a data structure that stores a collection of items and follows the 'Last In, First Out' (LIFO) rule. This means the last item added to the stack is the first one to be removed. Think of it like a stack of books, where the book you put on top is the first one you can take off. Stacks are commonly used in computer programming for managing tasks, tracking function calls, and handling actions in a specific order.

# We can store different type of data in Stack

# By Default:
# In Python, both stacks and queues can be implemented using various data structures. However, Python does not have built-in classes or modules specifically named "stack" or "queue." Instead, you can use lists to implement both data structures

stack = []

stack.append('a')
stack.append('b')
stack.append('c')
print('Initial stack')

# Accessing the top element (last element added) using [-1]
print(f"{stack[-1]} <-- Top Element")
print(stack)

print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print('\nStack after elements are popped:')
print(stack)
