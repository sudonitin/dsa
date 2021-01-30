class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def ownLogic(root, sequence, sequence_so_far):
    if root:
        sequence_so_far.append(root.val)
        left_sequence = ownLogic(root.left, sequence, sequence_so_far)
        right_sequence = ownLogic(root.right, sequence, sequence_so_far)
        sequence_so_far.pop()
        return left_sequence or right_sequence
    else:
        # print(sequence_so_far)
        if sequence_so_far == sequence:
            return True
        else:
            return False


# root = Node(1)
# root.left = Node(7)
# root.right = Node(9)
# root.right.left = Node(2)
# root.right.right = Node(9)

root = Node(1)
root.left = Node(0)
root.right = Node(1)
root.left.left = Node(1)
root.right.left = Node(6)
root.right.right = Node(5)

print(ownLogic(root, [1,1,6], []))