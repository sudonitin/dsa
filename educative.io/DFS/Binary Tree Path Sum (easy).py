class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

calc = 0
sol = ''

def printPreOrder(root, s, calc, sol):
    if root:
        calc += root.val
        sol += str(root.val) + "=>"
        print(calc, sol)
        if root.left is None:
            if calc == s:
                print("##L")
                return True
            else:
                return
        flag = printPreOrder(root.left, s, calc, sol)
        if flag == False:
            calc -= root.val
            sol = sol[:-3]
        if root.right is None:
            if calc == s:
                print("##R")
                return True
            else:
                return
        flag = printPreOrder(root.right, s, calc, sol)
        if flag == False:
            calc -= root.val
            sol = sol[:-3]
    # else:
    #     if calc == s:
    #         # print(sol)
    #         print("####")
    #         return True
    #     else:
    #         return False
        # flag = True
    # print(calc, sol)
    # return flag

def referredLogic(root, s):
    if root is None:
        return False
    if root.val == s and root.left is None and root.right is None:
    # if root.val == s: -- this line can be used if root node == sum
        return True
    
    return referredLogic(root.left, s-root.val) or referredLogic(root.right, s-root.val)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# print(printPreOrder(root, 10, calc, sol))
print(referredLogic(root, 13))
