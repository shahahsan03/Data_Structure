# Palindromic Queue
from collections import deque

def palindromic(queue):
    while len(queue) > 1:
        if queue.popleft()!=queue.pop():
            return False
    return True

queue= deque(['r','o','t','o','r'])

print(palindromic(queue))