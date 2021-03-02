from heapq import *

# My Approach: Find top k elements of abs difference with x and sort it
# Time: n * kLogk
def kClosestNums(arr, k , x):
    absDiff = [abs(x-i) for i in arr]
    maxheap = []
    for i in range(len(absDiff)):
        heappush(maxheap, (-absDiff[i], arr[i]))
        if len(maxheap) > k:
            heappop(maxheap)
    result = [i[1] for i in maxheap]
    result.sort()
    return result

# print(kClosestNums([5, 6, 7, 8, 9], 3, 7)) #[6, 7, 8]
# print(kClosestNums([2, 4, 5, 6, 9], 3, 6)) #[4, 5, 6]
# print(kClosestNums([2, 4, 5, 6, 9], 3, 10)) #[5, 6, 9]

# Solution: 
# - find the closest number to X and then find the k elements 
# by either using 2 pointer or minheap

# minheap: Time - log n * klogk

def binary_search_closest_number(arr, x):
    start, end = 0, len(arr)-1
    closest_index = (start+end) // 2
    while start < end:
        mid = (start+end) // 2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            closest_index = mid if abs(arr[mid]-x) < abs(arr[closest_index]-x) else closest_index
            start = mid+1
        else:
            closest_index = mid if abs(arr[mid]-x) < abs(arr[closest_index]-x) else closest_index
            end = mid-1
    return closest_index

from collections import deque
def top_k_closest_pointer(arr, k, x):
    closest_index = binary_search_closest_number(arr, x)
    left, right = closest_index, closest_index+1
    result = deque()
    length = len(arr)
    for i in range(k):
        if left >= 0 and right < length:
            diff1 = abs(arr[left]-x)
            diff2 = abs(arr[right]-x)
            if diff1 < diff2:
                result.appendleft(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
        elif left >= 0:
            result.appendleft(arr[left])
            left -= 1
        elif right < length:
            result.append(arr[right])
            right += 1
    return result


print(top_k_closest_pointer([5, 6, 7, 8, 9], 3, 7)) #[6, 7, 8]
print(top_k_closest_pointer([2, 4, 5, 6, 9], 3, 6)) #[4, 5, 6]
print(top_k_closest_pointer([2, 4, 5, 6, 9], 3, 10)) #[5, 6, 9]