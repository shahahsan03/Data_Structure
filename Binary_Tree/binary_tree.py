# Binary Tree:
# A binary tree is a special type of tree in which every node or vertex has either no child node or one child node or two child nodes. A binary tree is an important class of a tree data structure in which a node can have at most two children.

class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    
    def view(self):
        if self.left:
            self.left.view()
        print(self.data)
        if self.right:
            self.right.view()
        
root = Node(100)
root.left = Node(10)
root.right = Node(20)
root.view()