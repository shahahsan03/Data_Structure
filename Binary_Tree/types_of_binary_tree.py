# Types of Binary Trees

# * Binary Search Tree (BST):

# This tree is a binary search tree because for each node, all nodes in the left subtree have values less than or equal to the node's value, and all nodes in the right subtree have values greater than the node's value.

#     10
#    /  \
#   5   15
#  / \    \
# 3   7   18

# code:

class binarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def viewList(self):
        print(self.data)
        if self.left:
            self.left.viewList()
        if self.right:
            self.right.viewList()

print('Binary Search Tree')
binary_search_root = binarySearchTree(10)
binary_search_root.left = binarySearchTree(5)
binary_search_root.left.left = binarySearchTree(3)
binary_search_root.left.right = binarySearchTree(7)
binary_search_root.right = binarySearchTree(15)
binary_search_root.right.right = binarySearchTree(18)
binary_search_root.viewList()


# * Complete Binary Tree:

# In a complete binary tree, all levels are filled from left to right. The last level may not be completely filled, but all nodes are as far to the left as possible.

#     1
#    / \
#   2   3
#  / \  /
# 4  5 6

# code: 

class completeBinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def viewList(self):
        print(self.data)
        if self.left:
            self.left.viewList()
        if self.right:
            self.right.viewList()
        
print('Complete Binary Tree')
complete_root = completeBinaryTree(1)
complete_root.left = completeBinaryTree(2)
complete_root.right = completeBinaryTree(3)
complete_root.left.left = completeBinaryTree(4)
complete_root.left.right = completeBinaryTree(5)
complete_root.right.left = completeBinaryTree(6)

complete_root.viewList()

# * Full Binary Tree:

# In a full binary tree, every node has either 0 or 2 children. There are no nodes with only one child.

#     1
#    / \
#   2   3
#  / \
# 4   5

# code:

class fullBinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def viewList(self):
        print(self.data)
        if self.left:
            self.left.viewList()
        if self.right:
            self.right.viewList()

print('Full Binary Tree')
full_binary_root = fullBinaryTree(1)
full_binary_root.left = fullBinaryTree(2)
full_binary_root.right = fullBinaryTree(3)
full_binary_root.left.left = fullBinaryTree(4)
full_binary_root.left.right = fullBinaryTree(5)
full_binary_root.viewList()

# * Perfect Binary Tree:

# In a perfect binary tree, all levels are completely filled, and all nodes have two children. The number of nodes is a power of 2.

#     1
#    / \
#   2   3
#  / \ / \
# 4  5 6  7

# code:

class perfectBinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def viewList(self):
        print(self.data)
        if self.left:
            self.left.viewList()
        if self.right:
            self.right.viewList()
            
print('Perfect Binary Tree')
perfect_binary_root = perfectBinaryTree(1)
perfect_binary_root.left = perfectBinaryTree(2)
perfect_binary_root.right = perfectBinaryTree(3)
perfect_binary_root.left.left = perfectBinaryTree(4)
perfect_binary_root.left.right = perfectBinaryTree(5)
perfect_binary_root.right.left = perfectBinaryTree(6)
perfect_binary_root.right.right = perfectBinaryTree(7)
perfect_binary_root.viewList()

# * Degenerate Tree (Linked List):

# In a degenerate tree, each parent node has only one associated child node, effectively forming a linked list. The height of the tree is equal to the number of nodes, making it highly unbalanced.

# 1
#  \
#   2
#    \
#     3
#      \
#       4

# code:

class degenerateTree:
    def __init__(self,data):
        self.data = data
        self.right = None

    def viewList(self):
        print(self.data)
        if self.right:
            self.right.viewList()

print('Degenerate Tree')
degenerate_root = degenerateTree(1)
degenerate_root.right = degenerateTree(2)
degenerate_root.right.right = degenerateTree(3)
degenerate_root.right.right.right = degenerateTree(4)
degenerate_root.viewList()

# * Binary Heap (Min-Heap):

# A binary heap is a complete binary tree with the property that the value of each node is less than or equal to the values of its children (in the case of a min-heap).

#     1
#    / \
#   3   2
#  / \ / \
# 5  4 7  6

# code:

class binaryHeap:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def viewList(self):
        print(self.data)
        if self.left:
            self.left.viewList()
        if self.right:
            self.right.viewList()

print('Binary Heap')
binary_heap_root = binaryHeap(1)
binary_heap_root.left = binaryHeap(3)
binary_heap_root.right = binaryHeap(2)
binary_heap_root.left.left = binaryHeap(5)
binary_heap_root.left.right = binaryHeap(4)
binary_heap_root.right.left = binaryHeap(7)
binary_heap_root.right.right = binaryHeap(6)
binary_heap_root.viewList()