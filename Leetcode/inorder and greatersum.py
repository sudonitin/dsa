class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.val)
        printInOrder(root.right)
	# if root:
	# 	printInOrder(root.left)
    #     print(root.val)
    #     printInOrder(root.right)

def greaterSum(root, totalsum):
    if root:
        totalsum = greaterSum(root.right, totalsum)
        # print(root.val, root.val+totalsum, "test")
        root.val += totalsum
        totalsum = root.val
        totalsum = greaterSum(root.left, totalsum)
        return totalsum
    else:
        return totalsum

def printReversedInOrder(root):
    if root:
        printReversedInOrder(root.right)
        print(root.val)
        printReversedInOrder(root.left)

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

root = Node(7)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(2)
root.left.right = Node(5)

# printReversedInOrder(root)
print("InOrder traversal of binary tree is")
# printInOrder(root)
greaterSum(root, 0)
printInOrder(root)
# printReversedInOrder(root)
