# Variant of finding k smallest numbers
from heapq import *
def find_k_closest_points(arr, k):
    og_arr = list(arr)
    for i in range(len(arr)):
        arr[i] = arr[i][0]**2 + arr[i][1]**2
    # print(arr)
    maxheap = []
    result = []
    for i in range(k):
        heappush(maxheap, -arr[i])
    for i in range(k, len(arr)):
        if -arr[i] > maxheap[0]:
            heappop(maxheap)
            heappush(maxheap, -arr[i])
    for i in list(maxheap):
        result.append(og_arr[arr.index(i*-1)])
        og_arr.remove(og_arr[arr.index(i*-1)])
        arr.remove(i*-1)
        # print(i, "**")
    # print(og_arr)
    return result

print(find_k_closest_points([[1,2],[1,3]], 1)) #[[1,2]]
print(find_k_closest_points([[1, 3], [3, 4], [2, -1]], 2)) #[[1, 3], [2, -1]]