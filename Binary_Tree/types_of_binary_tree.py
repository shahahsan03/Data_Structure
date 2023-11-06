# Types of Binary Trees

# * Binary Search Tree (BST):

# This tree is a binary search tree because for each node, all nodes in the left subtree have values less than or equal to the node's value, and all nodes in the right subtree have values greater than the node's value.

#     10
#    /  \
#   5   15
#  / \    \
# 3   7   18

# * Complete Binary Tree:

# In a complete binary tree, all levels are filled from left to right. The last level may not be completely filled, but all nodes are as far to the left as possible.

#     1
#    / \
#   2   3
#  / \  /
# 4  5 6

# * Full Binary Tree:

# In a full binary tree, every node has either 0 or 2 children. There are no nodes with only one child.

#     1
#    / \
#   2   3
#  / \
# 4   5

# * Perfect Binary Tree:

# In a perfect binary tree, all levels are completely filled, and all nodes have two children. The number of nodes is a power of 2.

#     1
#    / \
#   2   3
#  / \ / \
# 4  5 6  7

# * Degenerate Tree (Linked List):

# In a degenerate tree, each parent node has only one associated child node, effectively forming a linked list. The height of the tree is equal to the number of nodes, making it highly unbalanced.

# 1
#  \
#   2
#    \
#     3
#      \
#       4

# * Binary Heap (Min-Heap):

# A binary heap is a complete binary tree with the property that the value of each node is less than or equal to the values of its children (in the case of a min-heap).

#     1
#    / \
#   3   2
#  / \ / \
# 5  4 7  6