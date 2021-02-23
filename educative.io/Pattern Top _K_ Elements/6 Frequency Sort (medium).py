from heapq import *

def frequencySort(st):
    frequency = {}
    for i in st:
        frequency[i] = frequency.get(i, 0) + 1
    minheap = []
    for alpha, freq in frequency.items():
        heappush(minheap, (-freq, alpha))
    # print(list(minheap))
    result = ""
    while minheap:
        temp = heappop(minheap)
        result += -temp[0]*temp[1]
    return result

print(frequencySort("abcba")) #aabbc
print(frequencySort("Programming")) #rrggmmPiano