class Node:
    def __init__(self, key):
        self.left, self.right = None, None
        self.val = key

def ownLogic(root, s):
    if root:
        s = s*10 + root.val
        if root.left is None and root.right is None:
            return s
        elif root.left is None and root.right is not None:
            leftSum = 0
            rightSum = ownLogic(root.right, s)
        elif root.left is not None and root.right is None:
            leftSum = ownLogic(root.left, s)
            rightSum = 0
        else:
            leftSum = ownLogic(root.left, s)
            rightSum = ownLogic(root.right, s)
        return leftSum + rightSum

root = Node(1)
root.left = Node(7)
root.right = Node(9)
root.right.left = Node(2)
root.right.right = Node(9)

# root = Node(1)
# root.left = Node(0)
# root.right = Node(1)
# root.left.left = Node(1)
# root.right.left = Node(6)
# root.right.right = Node(5)
print(ownLogic(root, 0))
