from heapq import *

def cost_to_connect_ropes(arr):
    minheap = []
    result = 0
    for i in arr:
        heappush(minheap, i)
    while len(minheap) > 1:
        a = heappop(minheap)
        b = heappop(minheap)
        result += a+b
        heappush(minheap, a+b)
    # print(minheap)
    return (result)

print(cost_to_connect_ropes([1, 3, 11, 5])) #33
print(cost_to_connect_ropes([3, 4, 5, 6])) #36
print(cost_to_connect_ropes([1, 3, 11, 5, 2])) #42