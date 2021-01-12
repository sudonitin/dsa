class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
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

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    # root.left.right = TreeNode(5)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(traverse(root))
main()