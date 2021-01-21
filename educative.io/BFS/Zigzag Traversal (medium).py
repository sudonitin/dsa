from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

''' 
        12
        /\
       7  1
      /\
     9 10   
'''

def referredLogic(root):
    result = deque()
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    levelNum = 1
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for i in range(levelSize):
            currentNode = queue.popleft()
            currentLevel.append(currentNode.val)
            if levelNum % 2 == 0:
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            else:
                if currentNode.right:
                    queue.append(currentNode.right)
                if currentNode.left:
                    queue.append(currentNode.left)
        # if levelNum % 2 == 0:    
        result.append(currentLevel)
        # else:
        #     result.append(sorted(currentLevel, key=-1))
        levelNum += 1
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    # root.left.right = TreeNode(5)
    root.left.right = TreeNode(10)
    # root.right.right = TreeNode(5)
    print(referredLogic(root))
main()