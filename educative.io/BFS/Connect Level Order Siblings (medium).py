from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.next = None

def ownLogic(root):
    queue = deque()
    secondQueue = deque()
    queue.append(root)
    secondQueue.append(root)
    while queue:
        levelSize = len(queue)
        i = -1
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()
            if currentNode.left:
                if i > -1 and i < levelSize-1:
                    previousNode = currentLevel[i]
                    if len(queue):
                        previousNode.next = queue[0]
                    else:
                        previousNode.next = currentNode
                i += 1
                currentLevel.append(currentNode)
                queue.append(currentNode.left)
                secondQueue.append(currentNode.left)
            if currentNode.right:
                if i > -1 and i < levelSize-1:
                    previousNode = currentLevel[i]
                    if len(queue):
                        previousNode.next = queue[0]
                    else:
                        previousNode.next = currentNode
                i += 1
                currentLevel.append(currentNode)
                queue.append(currentNode.right)
                secondQueue.append(currentNode.right)
            if currentNode.left is None or currentNode.right is None:
                if i > -1 and i < levelSize-1:
                    previousNode = currentLevel[i]
                    previousNode.next = currentNode
                i += 1
                currentLevel.append(currentNode)
        currentNode.next = None
    for i in range(len(secondQueue)):
        if secondQueue[i].next:
            print(secondQueue[i].val, "=>", secondQueue[i].next.val)
        else:
            print(secondQueue[i].val, "=> null")

    # for i in range(len(secondQueue)):
    #     # print(1)
    #     current = secondQueue[i]
    #     levelStr = ''
    #     while current:
    #         if current:
    #             levelStr += str(current.val) + "=>"
    #         else:
    #             levelStr += "null"
    #         current = current.next
    #         # print(current, "----")
    #     levelStr += "null"
    #     print(levelStr)
    return


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    # print(ownLogic(root))
    ownLogic(root)
main()