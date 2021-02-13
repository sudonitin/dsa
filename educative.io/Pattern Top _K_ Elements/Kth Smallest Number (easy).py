from heapq import *

# APPROACH 1 :- Sort and give last k elements O(nLogn) o(1)
# APPROACH 2 :- Use MaxHeap Data Structure TC = O(NLogk) SC = O(Logk)
# https://www.geeksforgeeks.org/heap-data-structure/

# We can't use minheap of size k in this because it will return the smallest number in the given array
# and we want the kth smallest. Hence use maxheap with negative of og numbers

# THE BELOW APPROACH IS NOT ALWAYS FULL PROOF so don't refer
# We can use minheap of size n(array size) and simply return k-1th element
# This will return kth smallest element

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

# WRONG SOLUTION FOR [3,2,3,1,2,4,5,5,6], 3 AND [3,2,1,5,6,4], 2
# def minHeap(arr, k):
#     minheap = []
#     for i in arr:
#         heappush(minheap, i)
#     print(list(minheap))
#     return minheap[k-1]

# print(minHeap([1, 5, 12, 2, 11, 5], 3)) #5
# print(minHeap([1, 5, 12, 2, 11, 5], 4)) #5
# print(minHeap([5, 12, 11, -1, 12], 3)) #11
# print(minHeap([3,2,3,1,2,4,5,5,6], 3))
# print(minHeap([3,2,1,5,6,4], 2))

print(find_kth_smallest([1, 5, 12, 2, 11, 5], 3)) #5
print(find_kth_smallest([1, 5, 12, 2, 11, 5], 4)) #5
print(find_kth_smallest([5, 12, 11, -1, 12], 3)) #11
print(find_kth_smallest([3,2,3,1,2,4,5,5,6], 3))
print(find_kth_smallest([3,2,1,5,6,4], 2))