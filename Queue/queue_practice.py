# Queue:

# A queue is a data structure that works like a line of people waiting for something. It follows the "first-in, first-out" (FIFO) principle, which means the first person to join the line is the first to get served or processed. In a queue, you can add (enqueue) people to the back of the line and remove (dequeue) people from the front of the line. It's like waiting in line at a store: the person who arrives first is the first to be helped, and as more people join, they get in line behind the others.

# A queue is like a line of people; the first person to join is the first to leave. It follows a "first-in, first-out" (FIFO) order.

# You can use different types of data in a queue, just like you can in other Python data structures such as lists.

from collections import deque

queue = deque()

queue.append(1) # Enqueue
queue.append(2)
queue.append(3)
queue.append(4)

print(queue)

queue.popleft() # Dequeue
queue.popleft()
queue.popleft()

print(queue)

import queue

q = queue.Queue()
q.put(1) # Enqueue
q.put(2)
q.put(3)
print(q)

q.get() # Dequeue
q.get()
q.get()
print(q)


# The key difference between the two queues is that collections.deque is a general-purpose double-ended queue suitable for single-threaded applications, while queue.Queue is explicitly designed for multi-threaded programs, offering built-in thread safety. The choice between them depends on your specific use case and whether you need thread safety or not. For most single-threaded applications, collections.deque is a more efficient choice for implementing a queue.
