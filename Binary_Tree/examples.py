# from binarytree import Node 

# root = Node(3) 
# root.left = Node(6) 
# root.right = Node(8) 

# print('Binary tree :', root) 

# print('List of nodes :', list(root)) 

# print('Inorder of nodes :', root.inorder) 

# print('Size of tree :', root.size) 
# print('Height of tree :', root.height) 

# print('Properties of tree : \n', root.properties)


# Binary Tree in Python

# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key

#     def traversePreOrder(self):
#         print(self.val, end=' ')
#         if self.left:
#             self.left.traversePreOrder()
#         if self.right:
#             self.right.traversePreOrder()

#     def traverseInOrder(self):
#         if self.left:
#             self.left.traverseInOrder()
#         print(self.val, end=' ')
#         if self.right:
#             self.right.traverseInOrder()

#     def traversePostOrder(self):
#         if self.left:
#             self.left.traversePostOrder()
#         if self.right:
#             self.right.traversePostOrder()
#         print(self.val, end=' ')

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)

# print("Pre order Traversal: ", end="")
# root.traversePreOrder()
# print("\nIn order Traversal: ", end="")
# root.traverseInOrder()
# print("\nPost order Traversal: ", end="")

# root.traversePostOrder()

# class Node:
#     def __init__(self,data):
#         self.right = None
#         self.left = None
#         self.data = data
    
#     def displayData(self):
#         if self.right:
#             self.right.displayData()
#         print(self.data)
#         if self.left:
#             self.left.displayData()

# root = Node(10)
# root.left = Node(5)
# root.right = Node(15)
# root.left.left = Node(3)
# root.left.right = Node(7)
# root.right.left = Node(12)
# root.right.right = Node(18)
# root.displayData()


result = 0 

class Node :
	def __init__(self,data) :
		self.data = data  
		self.left = None
		self.right = None  

def calcSum(root, res) :

	global result 
	
	if (root == None) :
		return 
	
	if (root.data % 2 == 0) :
		
		if (root.left) :
			res += root.left.data  
			result = res
   
		if (root.right) :
			res += root.right.data
			result = res
			

	calcSum(root.left, res)
	calcSum(root.right, res)

def findSum(root) :
	res = 0 
	calcSum(root, res)  
	print(result)
	
if __name__ == "__main__" : 
# By checking the value of name using the if __name__ == '__main__' condition, you can control which code is executed in different scenarios. If the condition is True, then the indented code block following the conditional statement is executed, while if it is False, the code block is skipped.

	root = Node(2)  
	root.left = Node(3)  
	root.right = Node(8)  
	root.left.left = Node(2)  
	root.right.left = Node(5)  
	root.right.right = Node(6)  
	root.right.left.left = Node(1)  
	root.right.right.right = Node(3)  
	findSum(root)  

