# Own logic
# Doesn't work for negative numbers
from heapq import *

class kthLargestInStream:
    def __init__(self, arr, k):
        minheap = []
        for i in arr:
            heappush(minheap, i)
            if len(minheap)  > k:
                heappop(minheap)
        print(list(minheap), "--")
        self.minheap = minheap
        # print()

    # update minheap
    def add(self, num):
        if num > self.minheap[0]:
            heappop(self.minheap)
            heappush(self.minheap, num)
        return self.minheap[0]

kthLargest = kthLargestInStream([3,1,5,12,2,11], 4)
print(kthLargest.add(6)) #5
print(kthLargest.add(13)) #6
print(kthLargest.add(4)) #6
print(kthLargest.add(14)) #6
