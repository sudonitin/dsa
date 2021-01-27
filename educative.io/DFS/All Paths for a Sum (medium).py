class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def ownLogics(root, s, count):
    if root is None:
        return count
    if root.val == s and root.left is None and root.right is None:
        return count + 1
    return ownLogics(root.left, s-root.val, count) + ownLogics(root.right, s-root.val, count)

# TREE 1
# root = Node(1)
# root.left = Node(7)
# root.right = Node(9)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(2)
# root.right.right = Node(7)

# TREE 2
root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(4)
root.right.left = Node(10)
root.right.right = Node(5)

print(ownLogics(root, 23, 0))
