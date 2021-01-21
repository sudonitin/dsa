from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# was not able to handle test case where right subtree ends before left
''' Failed test case in ownLogic
        12
        /\
       7  1
      /\
     9 10   
'''
def ownLogic(root):
    result = [[root]]
    values = [[root.val]]
    i = 0
    while True:
        flag = False
        for node in result[i]:
            if node.left is not None and node.right is not None:
                flag = True
        if not flag:
            break
        temp = []
        newtemp = []
        for node in result[i]:
            if node.left is not None:
                temp.append(node.left)
                newtemp.append(node.left.val)
            if node.right is not None:
                temp.append(node.right)
                newtemp.append(node.right.val)
        result.append(temp)
        values.append(newtemp)
        i += 1

    return values

def referredLogic(root):
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()
            currentLevel.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result.append(currentLevel)
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(10)
    # root.right.right = TreeNode(5)
    print(referredLogic(root))
main()