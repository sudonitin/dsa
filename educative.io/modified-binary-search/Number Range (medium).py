# optimised approach is to use binary search twice
# 1st search will find the first position
# if first position is -1 then return -1, -1
# else apply 2nd search this will find last position

def find_number_range(arr, key):
    result = [len(arr), 0]
    start, end = 0, len(arr)-1
    while start <= end:
        middle = (start+end) // 2
        if key > arr[middle]:
            start = middle+1
        elif key < arr[middle]:
            end = middle-1
        else:
            result[0] = min(middle, result[0])
            result[1] = max(middle, result[1])
            start += 1
    if result == [len(arr), 0]:
        return [-1, -1]
    # the below code ain't a good approach,
    # as we might end up traversing the whole array
    # so the time complexity will be affected to O(n)
    # rather than O (logn)
    if result[0] != 0 and arr[result[0]-1] == key:
        for i in range(result[0]):
            if arr[i] == key:
                result[0] = i
                break
    return result

print(find_number_range([4, 6, 6, 6, 9], 6)) # [1, 3]
print(find_number_range([1, 3, 8, 10, 15], 10)) # [3, 3]
print(find_number_range([1, 3, 8, 10, 15], 12)) # [-1, -1]