class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def apply_sliding_window_to_path(path, given_sum):
    i,j = 0,0
    window_sum = 0
    while i < len(path):
        if window_sum < given_sum:
            window_sum += path[i]
        while window_sum > given_sum and j <= i:
            window_sum -= path[j]
            j += 1
        if window_sum == given_sum:
            # print(window_sum)
            return True
        i += 1
    # print(window_sum)
    return False

def get_all_paths(root, current_path, all_paths, given_sum):
    if root:
        current_path.append(root.val)
        all_paths = get_all_paths(root.left, current_path, all_paths, given_sum)
        all_paths = get_all_paths(root.right, current_path, all_paths, given_sum)
        # print(current_path)
        if apply_sliding_window_to_path(current_path, given_sum):
            all_paths += 1
        # print(all_paths, "count")
        current_path.pop()
        return all_paths
    else:
        return all_paths

root = Node(1)
root.left = Node(7)
root.right = Node(9)
root.left.left = Node(6)
root.left.right = Node(5)
root.right.left = Node(2)
root.right.right = Node(3)

# root = Node(12)
# root.left = Node(7)
# root.right = Node(1)
# root.left.left = Node(4)
# # root.left.right = Node(5)
# root.right.left = Node(10)
# root.right.right = Node(5)

# print(get_all_paths(root, [], 0, 11))
print(get_all_paths(root, [], 0, 12))
