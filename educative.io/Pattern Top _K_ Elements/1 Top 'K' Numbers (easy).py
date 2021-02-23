from heapq import *

# APPROACH 1 :- Sort and give last k elements O(nLogn) o(1)
# APPROACH 2 :- Use Heap Data Structure TC = O(NLogk) SC = O(Logk)
# https://www.geeksforgeeks.org/heap-data-structure/

def find_top_k_nos(arr, k):
    minheap = []
    for i in range(k):
        heappush(minheap, arr[i])
    for i in range(k, len(arr)):
        if arr[i] > minheap[0]:
            heappop(minheap)
            heappush(minheap, arr[i])
    return list(minheap)

print(find_top_k_nos([3, 1, 5, 12, 2, 11], 3))
print(find_top_k_nos([5, 12, 11, -1, 12], 3))