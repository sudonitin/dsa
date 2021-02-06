# can be optimised by using simple binary search 
# handle cases for less than and greater than, return for else case
import sys
def ceiling_of_num(arr, key):
    if key > arr[len(arr)-1]:
        return -1
    start, end = 0, len(arr)-1
    middle = (start+end) // 2
    minimum_greatest = sys.maxsize
    minimum_greatest_index = 0
    while start <= end:
        if arr[middle] >= key:
            minimum_greatest = min(arr[middle], minimum_greatest)
            minimum_greatest_index = middle if arr[middle] == minimum_greatest else minimum_greatest_index
            end = middle - 1
            middle = (start+end) // 2
        elif arr[middle] < key:
            start = middle+1
            middle = (start+end) // 2
    return minimum_greatest_index

print(ceiling_of_num([4, 6, 10], 6))
print(ceiling_of_num([1, 3, 8, 10, 15], 12))
print(ceiling_of_num([4, 6, 10], 17))
print(ceiling_of_num([4, 6, 10], -1))