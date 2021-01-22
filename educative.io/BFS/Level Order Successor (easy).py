from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def ownLogic(root, givenNode):
    if root is None:
        return 0
    queue = deque()
    nodeValues = []
    queue.append(root)
    nodeValues.append(root.val)
    while queue:
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.popleft()
            if currentNode.left:
                queue.append(currentNode.left)
                nodeValues.append(currentNode.left.val)
            if currentNode.right:
                queue.append(currentNode.right)
                nodeValues.append(currentNode.right.val)
    print("####", nodeValues)
    for i in range(len(nodeValues)):
        if nodeValues[i] == givenNode.val:
            return nodeValues[i+1]

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(10)
    # root.right.right = TreeNode(5)
    print(ownLogic(root, root.left.right))
main()