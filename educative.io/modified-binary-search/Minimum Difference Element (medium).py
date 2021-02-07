def find_min_diff_elem(arr, key):
    start, end = 0, len(arr)-1
    min_elem = -1
    while start <= end:
        middle = (start+end) // 2
        if key > arr[middle]:
            start = middle+1
            min_elem = max(arr[middle], min_elem)
        elif key < arr[middle]:
            end = middle-1
        else:
            return arr[middle]
    return min_elem

print(find_min_diff_elem([4, 6, 10], 7)) #6
print(find_min_diff_elem([4, 6, 10], 4)) #4
print(find_min_diff_elem([1, 3, 8, 10, 15], 12)) #10
print(find_min_diff_elem([4, 6, 10], 17)) #10