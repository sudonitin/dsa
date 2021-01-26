from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.next = None
    # level order traversal using next pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()

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

def referredLogic(root):
    queue = deque()
    queue.append(root)
    while queue:
        previousNode = None
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.popleft()
            if previousNode:
                previousNode.next = currentNode
            previousNode = currentNode
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    # root.left.right = TreeNode(5)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    # print(ownLogic(root))
    # ownLogic(root)
    referredLogic(root)
    print("SOlution is")
    root.print_level_order()
main()