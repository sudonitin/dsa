from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def ownLogic(root):
    if root is None:
        return 0
    queue = deque()
    queue.append(root)
    depth = 1
    while queue:
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.popleft()
            if currentNode.left is None and currentNode.right is None:
                return depth
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        depth += 1
    return depth

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(5)
    # root.right.left = TreeNode(10)
    # root.right.right = TreeNode(5)
    print(ownLogic(root))
main()