class Stack:
    def __init__(self):
        self.items = []
        self.redo = []
    def pushing(self,val):
        self.items.append(val)
        print(self.items)
    def undo_element(self):
        self.redo.append(self.items.pop())
        print(self.items)
    def redo_element(self):
        self.items.append(self.redo.pop())
        print(self.items)


stack = Stack()

stack.pushing(10)
stack.pushing(20)
stack.pushing(30)
stack.pushing(40)
stack.undo_element()
stack.redo_element()