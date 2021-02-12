from heapq import *

# APPROACH 1 :- Sort and give last k elements O(nLogn) o(1)
# APPROACH 2 :- Use MaxHeap Data Structure TC = O(NLogk) SC = O(Logk)
# https://www.geeksforgeeks.org/heap-data-structure/

def find_kth_smallest(arr, k):
    maxheap = []
    for i in range(k):
        heappush(maxheap, -arr[i])
    # print(list(maxheap))
    for i in range(k, len(arr)):
        if -arr[i] > maxheap[0]:
            heappop(maxheap)
            heappush(maxheap, -arr[i])
    # print(list(maxheap))
    return -maxheap[0]

print(find_kth_smallest([1, 5, 12, 2, 11, 5], 3))
print(find_kth_smallest([1, 5, 12, 2, 11, 5], 4))
print(find_kth_smallest([5, 12, 11, -1, 12], 3))