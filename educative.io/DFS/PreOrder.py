class Node: 
	def __init__(self, key): 
		self.left = None
		self.right = None
		self.val = key 


def printPreOrder(root): 
	if root:
		print(root.val)
		printPreOrder(root.left) 
		printPreOrder(root.right) 
		

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

print("PreOrder traversal of binary tree is")
printPreOrder(root) 
