from heapq import *
def topKFreq(arr, k):
    hashmap = {}
    for i in arr:
        hashmap[i] = hashmap.get(i, 0) + 1
    
    minheap = []
    for key, value in hashmap.items():
        heappush(minheap, (value, key))
        if len(minheap) > k:
            heappop(minheap)
    result = []
    for i in list(minheap):
        result.append(i[1])
    return result

print(topKFreq([5, 12, 11, 3, 11], 2))
print(topKFreq([1, 3, 5, 12, 11, 12, 11], 2))