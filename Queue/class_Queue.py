from collections import deque

class Queue:
    
    def __init__(self):
        self.items = deque()
        
    def enqueue(self,val):
        self.items.append(val)
        print(self.items)
    
    def dequeue(self):
        if len(self.items)==0:
            print('Queue is empty')
        else:
            self.items.popleft()
            print(self.items)
    
    def isEmpty(self):
        if len(self.items)==0:
            print('Queue is Empty')
        else:
            print('Queue is not empty')


myQueue = Queue()
myQueue.isEmpty()
myQueue.enqueue(10)
myQueue.isEmpty()
myQueue.dequeue()
myQueue.isEmpty()

